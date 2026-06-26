import bcrypt 
from datetime import datetime, timedelta, timezone  
from jose import jwt, JWTError  
from passlib.context import CryptContext 
from fastapi.security import OAuth2PasswordBearer 
from src.config import SECRET_KEY 

SECRET_KEY = SECRET_KEY 
ALGORITHM = "HS256" 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

def verify_password(plain_password, hashed_password) : 
    return pwd_context.verify(plain_password, hashed_password) 

def get_password_hash(password) : 
    return pwd_context.hash(password) 

def create_access_token(data : dict) : 
    to_encode = data.copy() 
    expire = datetime.now(timezone.utc) + timedelta(minutes=30) 
    to_encode.update({"exp" : expire}) 
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) 

def get_user_id_from_tokrn(token : str) : 
    try : 
        payload = jwt.decode(token, SECRET_KEY, algorithms = ["HS256"]) 
        user_id = payload.get("sub") 
        if user_id is None : 
            raise Exception("Invalid Token") 
        return user_id 
    except JWTError : 
        raise Exception("Could not validate credentials !!!")     