import streamlit as st 
from utils.api_client import upload_file_to_api, verify_token_api 

def render_sidebar() : 
    with st.sidebar : 
        st.title("Configuration") 
        token = st.text_input("Enter API Token", type="password") 
        
        if token : 
            if verify_token_api(token) : 
                st.success("Token Validated !!!") 
                st.divider() 
                st.header("Document Management") 
                uploaded_file = st.file_uploader("Upload Financial PDF", type="pdf") 
                
                if uploaded_file and token : 
                    if st.button("Ingest Document") : 
                        with st.spinner("Processing...") : 
                            res = upload_file_to_api(uploaded_file, token) 
                            st.success(f"Uploaded: {res.get('file')}") 
            else : 
                st.error("Invalid Token. Please check your credentials.") 
        return token 
