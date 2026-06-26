import os 
import logging 
from dotenv import load_dotenv 

load_dotenv() 

# Centralized Logging SetUp 
logging.basicConfig(
    level = logging.INFO, 
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    handlers = [logging.FileHandler("app.log"), logging.StreamHandler()] 
) 

logger = logging.getLogger("financial_rag") 

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
COLLECTION_NAME = "financial_docs" 
SECRET_KEY = os.getenv("SECRET_KEY") 