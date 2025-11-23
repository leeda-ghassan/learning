# /src/vector_db/chroma_db.py
from chromadb import Client

class ChromaDBWrapper:
    def __init__(self):
        self.client = Client(
            persist_directory="./chroma_db",
            chroma_db_impl="duckdb+parquet"
        )
        # Create or access a collection for courses
        self.collection = self.client.get_or_create_collection(
            name="courses",
            metadata={"description": "Course embeddings"}
        )

    def add_embeddings(self, ids, embeddings, metadatas):
        # Add embeddings to Chroma DB collection
        self.collection.add(
            documents=metadatas,
            embeddings=embeddings,
            ids=ids
        )

    def query(self, embedding, n_results=3):
        # Query top N similar courses based on user embedding
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )
        return results
