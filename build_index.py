from retrieval.loader import KnowledgeBaseLoader
from retrieval.chunker import DocumentChunker
from retrieval.embeddings import EmbeddingModel
from retrieval.vectorstore import VectorStore

print("Loading documents...")

loader = KnowledgeBaseLoader()
documents = loader.load_all_documents()

print(f"Loaded {len(documents)} documents")

print("Chunking...")

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

print(f"Created {len(chunks)} chunks")

print("Loading embedding model...")

embedding = EmbeddingModel()

print("Building FAISS index...")

store = VectorStore(embedding.get_model())

store.create(chunks)

print("✅ FAISS index created successfully!")