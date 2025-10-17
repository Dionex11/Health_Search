import numpy as np
def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    """ Calculates Cosine Similarity"""
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)

def searchdb(notes,query_embed):
    result=[]
    for patient_id,note,embedding in notes:
        score=cosine_sim(embedding,query_embed)
        result.append((patient_id,note,score))
        result.sort(key=lambda x : x[2],reverse=True)
    top=result[:3]
    ans=[]
    for patient_id, note,score in top:
        ans.append({"patient_id": patient_id, "note": note, "similarity": round(score, 6)})
    return ans