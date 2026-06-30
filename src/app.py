from contextlib import asynccontextmanager 
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm   
from pydantic import BaseModel 
from src.ingest import  process_and_ingest_pdf 
from src.retrieve import retrieve_for_user  
from src.llm import generate_answer 
from src.history import HistoryManager 
from src.config import logger 
from src.auth import oauth2_scheme, get_user_id_from_token, get_password_hash, authenticate_user, create_access_token   
from src.models import User, ChatHistory  
from src.database import get_db 
from sqlalchemy.orm import Session 
from src.database import get_db, engine, Base 


@asynccontextmanager 
async def lifespan(app : FastAPI) : 
    logger.info("Initializing Database Tables...") 
    try :
        Base.metadata.create_all(bind=engine) 
        logger.info("Database tables initialized successfully.") 
    except Exception as e : 
        logger.error(f"Failed to initialize database: {e}") 
    yield 
    logger.info("Financial RAG API is shutting down.") 

app = FastAPI(title="Financial RAG API", lifespan = lifespan)  
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

class QueryRequest(BaseModel) : 
    question : str 

class UserCreate(BaseModel) : 
    username: str 
    password: str     

async def get_current_user(token : str = Depends(oauth2_scheme)) : 
    try : 
        return get_user_id_from_token(token) 
    except Exception : 
        raise HTTPException(
            status_code = 401, 
            detail = "Invalid or expired token", 
            headers = {"WWW-Authenticate" : "Bearer"}  
        )         

@app.post("/upload") 
async def upload(file : UploadFile = File(...), user_id : str = Depends(get_current_user)) : 
    logger.info(f"User {user_id} uploading : {file.filename}") 
    try : 
        content = await file.read() 
        success = process_and_ingest_pdf(content.decode(errors='ignore'),user_id, file.filename) 
        if not success : 
            raise HTTPException(status_code=500, detail="Ingestion failed.") 
        return {"status":"success","file":file.filename} 
    except Exception as e : 
        logger.error(f"Upload error : {e}") 
        raise HTTPException(status_code=500, detail=str(e))     

@app.post("/ask") 
async def ask(request : QueryRequest, user_id : str = Depends(get_current_user),db : Session = Depends(get_db)) : 
    docs = retrieve_for_user(request.question, str(user_id)) 
    context = "\n".join(docs) if docs else "" 

    user_history = HistoryManager.get_history(db, user_id) 

    answer = generate_answer(request.question, context=context, history=str(user_history)) 

    HistoryManager.add_to_history(db, user_id, "user", request.question) 
    HistoryManager.add_to_history(db, user_id, "assistant", answer) 

    return {"answer": answer, "citations": docs} 

@app.get("/verify-token") 
async def verify_token(user_id : str = Depends(get_current_user)) : 
    return {"status" : "valid"} 

@app.post("/register") 
def register(user_data: UserCreate, db: Session = Depends(get_db)) : 
    existing_user = db.query(User).filter(User.username == user_data.username).first() 
    if existing_user : 
        raise HTTPException(status_code=400, detail="Username already registered")  
    
    hashed_pw = get_password_hash(user_data.password) 
    new_user = User(username=user_data.username, hashed_password=hashed_pw) 
    
    db.add(new_user) 
    db.commit() 
    db.refresh(new_user) 
    
    return {"message": "User created successfully"} 

@app.post("/token")
async def login_for_access_token(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db) ) : 
    user = authenticate_user(db, form_data.username, form_data.password) 
    if not user : 
        raise HTTPException(status_code=401, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"},)  
    
    access_token = create_access_token(data={"sub": user.username}) 

    return {"access_token": access_token, "token_type": "bearer"} 