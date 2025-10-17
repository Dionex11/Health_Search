# 🏥 HealthSearch API — Semantic Medical Note Retrieval

A **FastAPI-based semantic search engine** for medical patient notes.  
It uses **Sentence Transformers** to find related notes based on *meaning*, not just keywords — making it ideal for clinical and healthcare search use cases.

---

## ✨ Features

- 🔍 **Semantic Search** using Sentence Transformers  
- 🧱 **Modular Architecture** (FastAPI + SQLite)  
- 🔐 **API Token Authentication**  
- 🧾 **Detailed Logging & Error Handling**  
- ⚙️ **Lightweight & Portable**, zero setup needed  

---

## 🧠 System Architecture

| Module | Purpose |
|---------|----------|
| `app.py` | Main API — routes, authentication, orchestration |
| `model.py` | Defines Pydantic schemas for validation |
| `database.py` | Handles SQLite storage and CRUD operations |
| `embed.py` | Loads Sentence Transformer and vectorizes text |
| `util.py` | Provides similarity calculation utilities |
| `logger.py` | Centralized logging setup |
| `init_db.sql` | Database initialization script |

---

## ⚙️ Setup & Installation

### 🧩 Prerequisites
- **Python 3.9+**
- All project files (`app.py`, `database.py`, `embed.py`, `util.py`, `model.py`, `logger.py`, `init_db.sql`, `test_api.sh`) in one directory.

---

### 🪜 Steps

#### 1️⃣ Install Dependencies
```bash
To start virtual env:
  python -m venv env
  ./env/Scripts/activate
pip install -r requirements.txt

```

#### 2️⃣ Run the Application Server
```
uvicorn app:app --reload

  ➡️ Access the API at: http://127.0.0.1:8000
  
  📘 Interactive Swagger Docs: http://127.0.0.1:8000/docs
  
  📗 ReDoc Interface: http://127.0.0.1:8000/redoc
```
3️⃣ Test the API (Auto Script)
```
./test.sh


This script:

Inserts test data

Runs a search query

Automatically includes the X-API-Token header
```
4️⃣ Make Manual API Requests

Include the authentication header in all requests:
```
-H "X-API-Token: mysecrettoken123"


Example:

curl -H "X-API-Token: mysecrettoken123" \
"http://127.0.0.1:8000/search_notes?q=difficulty%20getting%20enough%20air"
```
🔐 Authentication
```
Header	Example
X-API-Token	mysecrettoken123

Defined globally in app.py for simplicity.
Unauthorized requests return a 401 Unauthorized response.
```
🧱 Database Design
```
Backend: SQLite (lightweight and file-based)

Schema: Defined in init_db.sql

Each record includes:

patient_id

note

embedding (stored as serialized vector)
```
🧩 API Endpoints
Method	Endpoint	Description
```
POST	/add_note	Add a new patient note
GET	/search_notes?q=...	Search existing notes semantically
```

🧾 Example Usage
➕ Add a Note
```
curl -X POST "http://127.0.0.1:8000/add_note" \
-H "Content-Type: application/json" \
-H "X-API-Token: mysecrettoken123" \
-d '{"patient_id": 101, "note": "Patient reports severe headache and dizziness"}'
```
🔍 Search Notes
```
curl -H "X-API-Token: mysecrettoken123" \
"http://127.0.0.1:8000/search_notes?q=headache"
```
💡 Design Decisions

  🧬 Sentence Transformers
  
    Used to generate dense vector embeddings for clinical notes.
    Model: all-MiniLM-L6-v2 → lightweight, fast, and semantically accurate.
  
  🗃️ SQLite
  
    Chosen for:
    
    Zero configuration
    
    Portability
    
    Perfect for demos and small projects
    
    ⚙️ Search Algorithm
    Aspect	Current	Future
    Search Type	Linear (O(N))	ANN-based
    Technology	Manual cosine similarity	FAISS / Chroma / Pinecone
    ⚖️ Trade-offs & Future Improvements
    Area	Current Implementation	Future Plan
    Scalability	Linear in-memory search	Vector index with FAISS/Chroma
    Authentication	Static API Token	OAuth2 / JWT
    Database	SQLite	PostgreSQL or managed DB
    Deployment	Local uvicorn	Docker / Kubernetes
    Shutdown Handling	Manual	Graceful teardown via context manager
  
  🧰 Logging & Error Handling
  
    Uses logger.exception() for full stack traces
    
    Handles:
    
    sqlite3.DatabaseError
    
    Generic exceptions
    
    Returns structured JSON with appropriate HTTP codes



