from src.vector_store import get_collection 
from src.ingest import generate_embedding 
from src.config import logger 

def retrieve_for_user(query: str, user_id: str, n: int = 3) : 
    try : 
        supabase = get_collection() 
        query_embedding = generate_embedding(query) 
        response = supabase.rpc("match_documents", { 
            "query_embedding": query_embedding, 
            "match_threshold": 0.5, 
            "match_count": n, 
            "filter": {"user_id": user_id} 
        }).execute() 

        docs = [item['content'] for item in response.data] 
        
        if not docs : 
            logger.info(f"No relevant documents found for user {user_id}") 
        else : 
            logger.info(f"Successfully retrieved {len(docs)} chunks for user {user_id}") 
            
        return docs 

    except Exception as e : 
        logger.error(f"Error during retrieval for user {user_id}: {e}") 
        return []             