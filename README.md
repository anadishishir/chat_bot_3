🚀 Financial RAG Assistant 

**[👉 Click here to access the Live Demo](https://your-app-name.onrender.com)** 

A robust, enterprise-grade Retrieval-Augmented Generation (RAG) system designed for secure, history-aware financial document analysis. This project emphasizes data isolation, persistent session memory, and a scalable cloud-native architecture. 

📂 Project Structure 
Plaintext 
financial-rag-assistant/ 
├── frontend/               # Streamlit application 
│   ├── components/         # Modular UI components 
│   ├── utils/              # API Client (Backend bridge) 
│   └── app.py              # Frontend entry point 
├── src/                    # Backend (FastAPI) 
│   ├── ingest.py           # Document processing & Vector embedding 
│   ├── retrieve.py         # Metadata-filtered pgvector search 
│   ├── vector_store.py     # Supabase/PostgreSQL connection 
│   ├── history.py          # Persistent chat memory management 
│   └── app.py              # FastAPI main router 
├── requirements.txt        # Dependencies 
└── .env.example            # Environment template 
🛠️ Tech Stack 
Backend : FastAPI (Async API) 

LLM : Google Gemini (via Google GenAI SDK) 

Vector Store : Supabase (PostgreSQL with pgvector & HNSW indexing) 

Frontend : Streamlit (Component-based architecture) 

Security : JWT-based authentication & Row-Level security principles 

Deployment : Render Cloud Platform 

🗝️ Key Features
Cloud-Native Scalability : Migrated from local storage to Supabase/PostgreSQL, allowing for unlimited document storage and high-speed similarity searches. 

Strict Data Isolation : By utilizing metadata-filtered querying at the database level, users are guaranteed to only access their own uploaded financial data, locked to their unique user_id. 

Persistent Conversational Memory : Features a dedicated HistoryManager that stores interactions in Supabase. The AI "remembers" previous turns, providing continuous, context-aware assistance across different login sessions. 

Intelligent Embeddings : Uses text-embedding-004 to ensure high-accuracy semantic search across complex, long-form financial reports. 

State-Aware Generation : The LLM receives the last 10 turns of conversation + retrieved context, ensuring responses are grounded in both document facts and the conversation flow. 

Modular Architecture : Clean separation between the Streamlit UI, FastAPI backend, and database logic ensures the system is maintainable and ready for independent scaling. 

⚙️ Installation & Setup 
Prerequisites 
Python 3.11+ 

Supabase Account 

Google Gemini API Key 

Configuration 
Clone the repository : 

Bash 
git clone https://github.com/anadishishir/chat_bot_3  
cd financial-rag-assistant 
Install dependencies : 

Bash 
pip install -r requirements.txt 
Set Environment Variables : 
Create a .env file with the following : 

Plaintext 
SUPABASE_URL=your_project_url 
SUPABASE_SERVICE_KEY=your_secret_key 
GEMINI_API_KEY=your_gemini_key 
Database Setup: Run the SQL scripts provided in your Supabase SQL Editor to enable pgvector and initialize the chat_history and document tables. 

🔐 Security Principles 
Database-Level Filtering: The system enforces user_id context at the query level before data is sent to the LLM. 

Secret Management: Sensitive credentials are never hardcoded and are injected exclusively via secure environment variables. 

Token Authentication: Secure JWT-based access ensures that only authenticated users can trigger ingestion or chat endpoints. 

📄 License 
This project is licensed under the MIT License. 

💡 Contact 
Developed for high-performance financial analytics. For questions or collaborative inquiries, feel free to reach out. 