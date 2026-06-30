import os 
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from src.config import logger 

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db") 

logger.info(f"Connecting to database: {'PostgreSQL' if 'postgresql' in SQLALCHEMY_DATABASE_URL else 'SQLite'}") 

connect_args = {} if "postgresql" in SQLALCHEMY_DATABASE_URL else {"check_same_thread": False} 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() 

def get_db() : 
    db = SessionLocal() 
    try : 
        yield db 
    except Exception as e : 
        logger.error(f"Database session error: {e}") 
        raise 
    finally : 
        db.close() 