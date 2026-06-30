import os 
from supabase import create_client 
from src.config import logger 

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")) 

def get_collection() : 
    return supabase 