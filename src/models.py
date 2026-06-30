from sqlalchemy import Column, Integer, String, ForeignKey  
from src.database import Base 

class User(Base) : 
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String, unique=True, index=True) 
    hashed_password = Column(String) 

class ChatHistory(Base) : 
    __tablename__ = "chat_histories" 
    id = Column(Integer, primary_key=True, index=True) 
    user_id = Column(Integer, ForeignKey("users.id")) 
    role = Column(String)  
    content = Column(String) 