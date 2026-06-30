from sqlalchemy.orm import Session 
from src.models import ChatHistory 
from src.config import logger 

class HistoryManager : 
    @staticmethod 
    def get_history(db: Session, user_id: int) : 
        return db.query(ChatHistory).filter(ChatHistory.user_id == user_id).order_by(ChatHistory.id.desc()).limit(10).all() 

    @staticmethod 
    def add_to_history(db: Session, user_id: int, role: str, content: str) : 
        try : 
            new_msg = ChatHistory(user_id=user_id, role=role, content=content) 
            db.add(new_msg) 
            db.commit() 
        except Exception as e : 
            logger.error(f"Failed to save history: {e}") 
            db.rollback() 