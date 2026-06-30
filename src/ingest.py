import uuid 
from pypdf import PdfReader 
from src.vector_store import get_collection 
from src.config import GEMINI_API_KEY, logger 
from google import genai 

client = genai.Client(api_key=GEMINI_API_KEY) 

def generate_embedding(text: str) : 
    result = client.models.embed_content( 
        model="text-embedding-004",  
        contents= text 
    ) 
    return result.embeddings[0].values 

def extract_text_from_pdf(pdf_path) : 
    try : 
        reader = PdfReader(pdf_path) 
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()]) 
        return text 
    except Exception as e : 
        logger.error(f"Failed to extract text from {pdf_path} : {e}") 
        return None 
    
def chunk_text(text, size = 1000, overlap = 100) : 
    chunks = [text[i:i+size] for i in range(0, len(text), size - overlap)] 
    return chunks 

def process_and_ingest_pdf(pdf_path, user_id, filename) : 
    logger.info(f"Starting ingest for : {filename}") 

    text = extract_text_from_pdf(pdf_path) 
    if not text : 
        logger.error(f"Failed to extract text from {pdf_path}") 
        return False 

    chunks = chunk_text(text) 
    supabase = get_collection() 

    ingested_count = 0 
    for chunk in chunks : 
        try : 
            embedding = generate_embedding(chunk) 
            supabase.table("documents").insert({ 
                    "content": chunk, 
                    "metadata": {"user_id": user_id, "filename": filename}, 
                    "embedding": embedding 
                }).execute() 
                
            ingested_count += 1 
        except Exception as e : 
            logger.error(f"Failed to ingest chunk for {filename}: {e}") 
            continue 
    logger.info(f"Successfully ingested {len(chunks)} chunks for {filename}") 
    return True     