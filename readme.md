🏥 Healthsearch API: Semantic Medical Note Retrieval

This is a prototype API designed to demonstrate semantic search capabilities on a corpus of medical patient notes. It utilizes Sentence Transformers to convert clinical text into dense vector embeddings, enabling retrieval based on semantic meaning rather than just keyword matching.

The application is built using  modular architecture in Python with FastAPI and SQLite.

🚀 Setup Instructions

Environment Prerequisites

Python 3.9+

All project files (app.py, database.py, embed.py, util.py, model.py, logger.py, init_db.sql, test_api.sh) must be in the same directory.

Dependency Installation

The project relies on standard data science and web development libraries.

# Install dependencies:

pip install -r requirements.txt

Configuration Requirements

The application uses a simple API token for access control. This token is defined as a global constant in app.py.

API Token: mysecrettoken123

Header: All requests must include the header X-API-Token: mysecrettoken123.

Commands to Run the Service

Command to start the server directly: uvicorn app:app --reload     

The server will be accessible at http://127.0.0.1:8000.

-How to Test the Endpoints

Use the provided test.sh script to quickly populate the database and run a search query.

Make the script executable:

chmod +x test_api.sh


Run the script in new terminal(Use gitbash):

./test.sh

(Note: The script handles the required X-API-Token header automatically.)

💡 Design Decisions

Technology Choices and Rationale

Sentence Transformers

Essential for converting text into semantically meaningful vectors, enabling search capabilities beyond simple keyword matching. We use all-MiniLM-L6-v2 for its excellent balance of speed and quality.

SQLite

Chosen for simplicity, zero-configuration setup, and ease of demonstration, making the project portable.



app.py: Handles only routing, authentication, and orchestrates calls.

model.py: Holds data validation schemas (Pydantic).

database.py: Manages all persistent storage logic (CRUD operations, connection management).

embed.py: Contains all logic related to the embedding model (loading, vectorization).

util.py: Houses mathematical utilities (cosine_sim).

Database Design Decisions (database.py and init_db.sql)


Trade-offs Considered

Linear Search vs. Vector Index (Scalability):

Current Choice: We fetch all data from SQLite and perform a linear search (O(N)) by iterating through every note and calculating similarity.

Trade-off: This is simple and requires no extra infrastructure but is not scalable. For a production application with thousands of notes, this would be replaced by a specialized vector database or library (e.g., FAISS, Chroma, Pinecone) to perform fast Approximate Nearest Neighbor (ANN) search.


Authentication: Simple API Token verification using X-API-Token header. Robust Error Handling: Specific sqlite3.DatabaseError and general exceptions are caught and logged with stack traces (logger.exception). Input Validation: Manual check for missing patient_id or note.

Known Limitations / Future Improvements

1. Scalability: Must migrate search to a dedicated vector index (FAISS/Chroma). 2. Authentication: Upgrade from simple token to OAuth2 or similar framework. 3. Shutdown: Implement the lifespan context manager to ensure the DB connection is gracefully closed.
