from contextlib import asynccontextmanager 
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File 
from fastapi.security import OAuth2PasswordBearer  
from pydantic import BaseModel 
from src.ingest import  process_and_ingest_pdf 
from src.retrieve import retrieve_for_user  
from src.llm import generate_answer 
from src.history import HistoryManager 
from src.config import logger 
from src.auth import oauth2_scheme, get_user_id_from_token 

@asynccontextmanager 
async def lifespan(app : FastAPI) : 
    logger.info("Financial RAG API is starting up ...") 
    app.state.history_manager = HistoryManager 
    yield 
    logger.info("Financial RAG API is shutting down.") 

app = FastAPI(title="Financial RAG API", lifespan = lifespan)  
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

class QueryRequest(BaseModel) : 
    question : str 

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
async def ask(request : QueryRequest, user_id : str = Depends(get_current_user)) : 
    history_manager = app.state.history_manager 

    docs = retrieve_for_user(request.question,user_id) 
    if not docs : 
        raise HTTPException(status_code = 404, detail = "No relevant data found.") 
    
    context = "\n".join(docs) 
    user_history = history_manager.get_history(user_id) 
    answer = generate_answer(request.question, context = context, history = user_history)  

    history_manager.add_to_history(user_id, "user", request.question) 
    history_manager.add_to_history(user_id, "assistant", answer) 

    return {"answer" : answer, "citations" : docs} 

@app.get("/verify-token") 
async def verify_token(user_id : str = Depends(get_current_user)) : 
    return {"status" : "valid"} 