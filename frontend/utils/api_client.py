import requests 
import streamlit as st 

BASE_URL = "https://financial-bot-api.onrender.com" 

def upload_file_to_api(file_obj, token) : 
    headers = {"Authorization": f"Bearer {token}"} 
    files = {"file": (file_obj.name, file_obj, "application/pdf")} 
    response = requests.post(f"{BASE_URL}/upload", files=files, headers=headers) 
    return response.json() 

def ask_api(question, token) : 
    headers = {"Authorization": f"Bearer {token}"} 
    response = requests.post(
        f"{BASE_URL}/ask", 
        json={"question": question}, 
        headers=headers
    ) 
    return response.json() 

def verify_token_api(token) : 
    headers = {"Authorization" : f"Bearer {token}"} 
    try : 
        response = requests.get(f"{BASE_URL}/verify-token", headers = headers) 
        return response.status_code == 200 
    except : 
        return False 

def perform_login(username, password) : 
    data = {"username": username, "password": password} 
    try : 
        response = requests.post(f"{BASE_URL}/token", data=data) 
        if response.status_code == 200 : 
            return response.json().get("access_token") 
        else : 
            return None 
    except Exception as e : 
        print(f"Login error: {e}") 
        return None     