from retrieval.embeddings import EmbeddingModel
from retrieval.vectorstore import VectorStore


class Retriever:

    def __init__(self, k=4):
        embedding = EmbeddingModel()
        store = VectorStore(embedding.get_model())
        self.vectorstore = store.load()
        self.k = k

    def search(self, query):
        return self.vectorstore.similarity_search(query, k=self.k)