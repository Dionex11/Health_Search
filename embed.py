from sentence_transformers import SentenceTransformer

class Embed:
    def __init__(self,model_name="all-MiniLM-L6-v2"):
        self.model_name=model_name
        self.model=SentenceTransformer(model_name)
    def vectorize(self,text):
        vecs=self.model.encode(text,convert_to_numpy=True)
        return vecs

