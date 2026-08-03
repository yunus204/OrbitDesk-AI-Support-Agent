from pathlib import Path
from langchain_community.vectorstores import FAISS

INDEX_PATH = "data/faiss_index"


class VectorStore:

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def create(self, documents):
        vectorstore = FAISS.from_documents(
            documents,
            self.embedding_model
        )

        Path(INDEX_PATH).mkdir(parents=True, exist_ok=True)

        vectorstore.save_local(INDEX_PATH)

        return vectorstore

    def load(self):
        return FAISS.load_local(
            INDEX_PATH,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )