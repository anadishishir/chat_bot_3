import chromadb 
from src.config import COLLECTION_NAME, logger 

client = chromadb.PersistentClient(path="./chroma_db") 

def get_collection() : 
    try : 
        return client.get_or_create_collection(name=COLLECTION_NAME) 
    except Exception as e : 
        logger.error(f"Error occurred while fetching collection: {e}") 
        raise 