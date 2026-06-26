import google.generativeai as genai 
from src.config import GEMINI_API_KEY, logger 

genai.configure(api_key=GEMINI_API_KEY) 
model = genai.GenerativeModel("gemini-2.5-flash") 

def generate_answer(question, context, history) : 
    prompt = f"Use only the context below to answer accurately. \n\nContext : {context}\n\nQuestion : {question}\n\n History : {history}" 
    try : 
        response = model.generate_content(prompt) 
        return response.txt 
    except Exception as e : 
        logger.error(f"Gemini API error : {e}") 
        return "I am unable to answer at this moment due to generation error."  