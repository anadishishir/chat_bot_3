import streamlit as st 
from utils.api_client import upload_file_to_api, verify_token_api 

def render_sidebar() : 
    with st.sidebar : 
        st.title("Financial AI Setup") 
        token = st.text_input("Enter API Token", type="password") 
        
        if not token : 
            st.warning("Please enter your token to begin.") 
            return None 

        if not verify_token_api(token) : 
            st.error("Invalid token. Please check your credentials.") 
            return None 

        st.success("Connected!") 
        st.divider() 
        
        st.header("Document Management") 
        uploaded_file = st.file_uploader("Upload Financial PDF", type="pdf") 
        
        if uploaded_file : 
            if st.button("Ingest Document") : 
                with st.spinner("Processing...") : 
                    res = upload_file_to_api(uploaded_file, token) 
                    st.success(f"Uploaded: {res.get('file')}") 
        return token 