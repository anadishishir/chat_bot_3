import google.generativeai as genai 
from src.config import GEMINI_API_KEY, logger 

genai.configure(api_key=GEMINI_API_KEY) 
model = genai.GenerativeModel("gemini-2.5-flash") 

def generate_answer(question, context, history) : 
    recent_history = history[-2:] if len(history) > 2 else history 

    formatted_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_history])  

    prompt = f""" 
    You are a professional Financial AI assistant. Use the provided context to answer the user's question accurately. 
    
    [Context - Data to use for facts] : 
    {context} 
    
    [Conversation History - For context on pronouns and follow-up questions] : 
    {formatted_history} 
    
    [Current Question] : 
    {question} 
    
    Answer : 
    """ 
    
    try : 
        response = model.generate_content(prompt) 
        return response.text 
    except Exception as e : 
        logger.error(f"Gemini API error: {e}") 
        return "I am unable to answer at this moment due to a generation error." 