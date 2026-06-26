from src.vector_store import get_collection 
from src.config import logger 

def retrieve_for_user(query : str, user_id : str, n : int = 3) : 
    try : 
        collection = get_collection() 
        results = collection.query(
            query_texts = [query],  
            n_results = n, 
            where = {"user_id" : user_id} 
        ) 

        docs = results.get("documents",[[]])[0] 

        if not docs : 
            logger.info(f"No relevant documents found for user {user_id} with query : {query}") 
        else : 
            logger.info(f"Successfully retrived {len(docs)} chumks for user {user_id}") 

    except Exception as e : 
        logger.error(f"Error during retrieval for user {user_id} : {e}") 
        return [] 