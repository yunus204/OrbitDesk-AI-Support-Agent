from retrieval.loader import KnowledgeBaseLoader
from retrieval.chunker import DocumentChunker

loader = KnowledgeBaseLoader()
documents = loader.load_all_documents()

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

print(f"Original Documents : {len(documents)}")
print(f"Total Chunks       : {len(chunks)}")

print("\nFirst Chunk\n")
print(chunks[0].page_content)

print("\nMetadata\n")
print(chunks[0].metadata)