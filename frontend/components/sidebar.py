import streamlit as st 
from utils.api_client import perform_login, upload_file_to_api, verify_token_api 

def render_sidebar() : 
    with st.sidebar : 
        st.title("Financial AI Setup") 

        if "token" not in st.session_state or not st.session_state["token"] : 
            mode = st.radio("Action:", ["Login", "Register"]) 
            username = st.text_input("Username") 
            password = st.text_input("Password", type="password") 
            
            if st.button("Submit") : 
                if mode == "Login" : 
                    token = perform_login(username, password) 
                    if token : 
                        st.session_state["token"] = token 
                        st.rerun() 
                    else : 
                        st.error("Login failed. Check credentials.") 
                else : 
                    import requests
                    res = requests.post(f"https://financial-bot-api.onrender.com/register", 
                                        json={"username": username, "password": password})
                    if res.status_code == 200:
                        st.success("Account created! Please login.")
                    else:
                        st.error("Registration failed.")
            return None
        
        else:
            st.success("Logged in!") 
            if st.button("Logout") : 
                st.session_state["token"] = None 
                st.rerun() 
            
            st.divider() 
            st.header("Document Management") 
            uploaded_file = st.file_uploader("Upload Financial PDF", type="pdf") 
            if uploaded_file and st.button("Ingest Document") : 
                with st.spinner("Processing...") : 
                    res = upload_file_to_api(uploaded_file, st.session_state["token"]) 
                    st.success(f"Uploaded: {res.get('file')}") 
            return st.session_state["token"]    