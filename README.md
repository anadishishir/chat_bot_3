🚀 Financial RAG Assistant   
A robust, enterprise-grade Retrieval-Augmented Generation (RAG) system designed for secure, history-aware financial document analysis. This project emphasizes data isolation, secure authentication, and a modular architecture. 
📂 Project Structure  
financial-rag-assistant/ 
├── docker/                 # Docker configuration 
├── frontend/               # Streamlit application 
│   ├── components/         # Modular UI components (chat, sidebar) 
│   ├── utils/              # API Client (Backend bridge) 
│   └── app.py              # Frontend entry point 
├── src/                    # Backend (FastAPI) 
│   ├── auth.py             # JWT & Security enforcement 
│   ├── history.py          # User-session memory manager 
│   ├── ingest.py           # Unified document processor 
│   ├── llm.py              # Gemini LLM integration (history-aware) 
│   ├── retrieve.py         # Metadata-filtered vector search 
│   └── app.py              # FastAPI main router 
├── requirements.txt        # Dependencies 
├── Dockerfile              # Containerization 
└── LICENSE                 # MIT License  
🛠️ Tech Stack 
Backend: FastAPI (Async API)
LLM: Google Gemini 1.5 Flash (via Generative AI SDK) 
Vector Store: ChromaDB (Persistent storage with Metadata filtering) 
Frontend: Streamlit (Component-based architecture) 
Security: JWT (JSON Web Tokens) for user identity protection 
Containerization : Docker 
🗝️ Key Features 
Strict Data Isolation : Using metadata-filtered querying, users can only retrieve data belonging to their verified user_id. 
Conversational Memory : A persistent HistoryManager allows the LLM to understand multi-turn financial queries without losing context. 
Modular Frontend: Designed with a clean separation of concerns, allowing for independent UI updates and easier testing. 
Production Logging : Full observability with automated logging of all ingestion, retrieval, and generation events. 
⚙️ Installation & Setup 
Prerequisites 
Python 3.11+ 
Docker (Optional for production deployment) 
Google Gemini API Key 
Step-by-Step 
Clone the repository :  
git clone https://github.com/anadishishir/chat_bot_3  
cd financial-rag-assistant  
Install dependencies :  
pip install -r requirements.txt  
TConfigure Environment : 
Create a .env file and set the following :  
GOOGLE_API_KEY=your_key_here 
SECRET_KEY=your_secure_random_string 
Launch the System : 
Backend: uvicorn src.app:app --reload 
Frontend: cd frontend && streamlit run app.py 
🔐 Security Principles 
JWT Authorization: Every request to /upload or /ask requires a valid JWT. 
Metadata Filtering: Queries are hard-scoped to the user's sub claim in the JWT. 
Environment Protection: Secrets and API keys are managed through secure environment injection. 
📄 License 
This project is licensed under the MIT License. See the LICENSE file for details. 
💡 Contact 
Developed for high-performance financial analytics. For questions or collaborative inquiries, feel free to reach out.  
