from retrieval.loader import KnowledgeBaseLoader

loader = KnowledgeBaseLoader()

docs = loader.load_all_documents()

print(f"Loaded {len(docs)} documents\n")

for doc in docs:
    print("=" * 60)
    print(doc.metadata)
    print(doc.page_content[:200])
    print()