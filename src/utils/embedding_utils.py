# /src/utils/embedding_utils.py
from sentence_transformers import SentenceTransformer

# Initialize SentenceTransformer model (using the '' model)
def generate_embedding(texts):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    return embeddings
