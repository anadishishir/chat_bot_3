import streamlit as st 
from components.sidebar import render_sidebar 
from components.chat import render_chat_interface 

st.set_page_config(page_title="Financial AI", layout="wide") 
st.title("Financial RAG Assistant") 

token = render_sidebar() 

if token : 
    render_chat_interface(token) 
else : 
    st.info("Please log in or register in the sidebar to begin.") 