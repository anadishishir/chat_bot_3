import uuid 
from pypdf import PdfReader 
from src.vector_store import get_collection 
from src.config import logger 

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
        return False 

    chunks = chunk_text(text) 
    collection = get_collection() 

    ids = [str(uuid.uuid4()) for _ in chunks] 
    metadatas = [{"user_id" : user_id, "filename" : filename} for _ in chunks] 

    collection.add(
        documents = chunks, 
        metadatas = metadatas, 
        ids = ids 
    ) 

    logger.info(f"Successfully ingested {len(chunks)} chunks for {filename}") 
    return True     