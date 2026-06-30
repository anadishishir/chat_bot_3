🚀 Financial RAG Assistant 
A robust, enterprise-grade Retrieval-Augmented Generation (RAG) system designed for secure, history-aware financial document analysis. This project emphasizes data isolation, secure authentication, and a scalable cloud-native architecture. 
 
📂 Project Structure 
Plaintext 
financial-rag-assistant/ 
├── frontend/               # Streamlit application 
│   ├── components/         # Modular UI components (chat, sidebar) 
│   ├── utils/              # API Client (Backend bridge) 
│   └── app.py              # Frontend entry point 
├── src/                    # Backend (FastAPI) 
│   ├── ingest.py           # Document processing & Vector embedding 
│   ├── retrieve.py         # Metadata-filtered pgvector search 
│   ├── vector_store.py     # Supabase/PostgreSQL connection 
│   └── app.py              # FastAPI main router 
├── requirements.txt        # Dependencies 
└── .env.example            # Environment template 
🛠️ Tech Stack 
Backend: FastAPI (Async API) 

LLM : Google Gemini (via Google GenAI SDK) 

Vector Store : Supabase (PostgreSQL with pgvector) 

Frontend : Streamlit (Component-based architecture) 

Security : JWT-based authentication & Row-Level security principles 

Deployment : Render Cloud Platform 

🗝️ Key Features 
Cloud-Native Scalability: Migrated from local storage to Supabase/PostgreSQL, allowing for virtually unlimited document storage and high-speed similarity searches using HNSW indexing. 

Strict Data Isolation : By utilizing metadata-filtered querying at the database level, users are guaranteed to only access their own uploaded financial data. 

Intelligent Embeddings : Uses text-embedding-004 to ensure high-accuracy semantic search across complex financial reports. 

Modular Architecture : Clean separation between the Streamlit UI and the FastAPI backend ensures easy maintenance and independent scaling. 
 
⚙️ Installation & Setup 
Prerequisites 
Python 3.11+ 
 
Supabase Account (for your database) 
 
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

SUPABASE_URL=your_project_url 
SUPABASE_SERVICE_KEY=your_secret_key 
GEMINI_API_KEY=your_gemini_key 
Database Setup : 
Run the vector extension and schema script provided in the Supabase SQL Editor to enable pgvector and the match_documents search function. 

🔐 Security Principles 
Database-Level Filtering : The system employs custom PostgreSQL functions to perform vector similarity searches, ensuring user_id context is enforced before the query ever hits the LLM. 

Service-Role Security : Backend communication with Supabase uses the service_role key to ensure administrative integrity, while frontend interactions remain gated by your custom JWT/Token authentication. 

Secret Management : No API keys or connection strings are stored in code. All sensitive data is injected via secure environment variables. 

📄 License 
This project is licensed under the MIT License. 

💡 Contact 
Developed for high-performance financial analytics. For questions or collaborative inquiries, feel free to reach out.  