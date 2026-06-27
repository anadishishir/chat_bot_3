import streamlit as st 
from frontend.utils.api_client import ask_api 

def render_chat_interface(token) : 
    if "messages" not in st.session_state : 
        st.session_state.messages = [] 

    for msg in st.session_state.messages : 
        with st.chat_message(msg["role"]) : 
            st.markdown(msg["content"]) 
    
    if prompt := st.chat_input("Ask a question about your documents") : 
        st.session_state.messages.append({"role": "user", "content": prompt}) 
        with st.chat_message("user") : 
            st.markdown(prompt) 

        with st.chat_message("assistant") : 
            with st.spinner("Thinking...") : 
                response = ask_api(prompt, token) 
                answer = response.get("answer", "Error: Could not get response.") 
                citations = response.get("citations", []) 
                
                st.markdown(answer) 
                if citations : 
                    with st.expander("View Sources") : 
                        for i, doc in enumerate(citations) : 
                            st.write(f"*Source {i+1}:* {doc[:200]}...") 
                            
        st.session_state.messages.append({"role": "assistant", "content": answer}) 