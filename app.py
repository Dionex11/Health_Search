from fastapi import FastAPI,Query,HTTPException,status,Header,Depends
from fastapi.responses import JSONResponse,HTMLResponse
from model import Note
from database import init,fetchrec,addrec
import sqlite3
import util
app= FastAPI(title="Healthsearch")
from embed import Embed
Embedder=Embed()
from logger import logger

API_TOKEN = "mysecrettoken123"

def verify_token(x_api_token: str = Header(..., alias="X-API-Token")):
    """
    Verifies the provided API token.
    Usage: Include header 'X-API-Token: <token>' in each request.
    """
    if x_api_token != API_TOKEN:
        logger.warning("Unauthorized access attempt with invalid token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Token",
        )

    
@app.on_event("startup")
def startup_event():
    try:
        init()
        logger.info("Database intialization is successfull")
    except Exception as e:
        logger.exception("Error initializing database")
        

@app.post("/add_note")
def add(data:Note,tok=Depends(verify_token)):
    """Post API End Point to add records into database"""
    try:
        if not data.patient_id or not data.note:
            raise HTTPException(status_code=400,detail="Data fields are missing")
        vec=Embedder.vectorize(data.note)
        addrec(data.patient_id,data.note,vec)
        return JSONResponse(status_code=201,content={"data":data.model_dump()})
    except sqlite3.DatabaseError:
        logger.exception("Database error while adding note")
        raise HTTPException(status_code=500, detail="Database operation failed")
    except Exception:
        logger.exception("Unexpected error while adding note")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.get("/search_notes")
def search(q: str = Query(..., description="Query string to search for"),tok=Depends(verify_token)):
    """Get API End Point to search records"""
    try:
        if not q.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        query_embed=Embedder.vectorize(q)
        notes=fetchrec()
        res=util.searchdb(notes,query_embed)
        return res
        
    except sqlite3.DatabaseError:
        logger.exception("Database error while searching notes")
        raise HTTPException(status_code=500, detail="Database operation failed")
    except Exception:
        logger.exception("Unexpected error while searching notes")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


