from pydantic import BaseModel

class Note(BaseModel):
    patient_id:str
    note:str
