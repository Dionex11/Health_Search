import sqlite3
import json
import numpy as np
from logger import logger
DB_PATH="health_search.db"

def init():
  
  """Database intialization"""
try:
    con=sqlite3.connect(DB_PATH)
    cur=con.cursor()
    with open("init.sql", 'r') as f:
        script = f.read()
    cur.executescript(script)
    logger.info("Database schema initialized successfully.")
    #cur.execute("DELETE FROM notes;")
    con.commit()
    con.close()
except:
    logger.exception(f"Error initializing database")
    
def addrec(id:str,note:str,vec):
    """ To add a record into database """
    try:
        emb_list = vec.tolist()
        emb_json = json.dumps(emb_list)
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM notes WHERE patient_id=? AND note=?", (id, note))
        exists = cur.fetchone()[0]
    
        if exists:
            logger.info(f"Note already exists for patient_id={id}. Skipping insert.")
        else:
            cur.execute("INSERT INTO notes (patient_id, note, embedding) VALUES (?, ?, ?)",(id, note, emb_json))
        con.commit()
        con.close()
        logger.info(f"Record added for patient ID: {id}")
      
    except:
        logger.exception(f"Database error while adding record for {id}")
def fetchrec():
    """ To fecth all records from database"""
    try:
        con=sqlite3.connect(DB_PATH)
        cur=con.cursor()
        cur.execute("SELECT patient_id, note, embedding FROM notes")
        rows=cur.fetchall()
        con.commit()
        con.close()

        results = []
        for patient_id, note, emb_json in rows:
            emb = np.array(json.loads(emb_json), dtype=np.float32)
        
            results.append((patient_id, note, emb))
        logger.info(f"Records fetched")
        return results
    except:
        logger.exception(logger.info(f"Error while fetching record"))
