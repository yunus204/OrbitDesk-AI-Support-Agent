from retrieval.retriever import Retriever

retriever = Retriever()

question = input("Enter your question: ")

results = retriever.search(question)

print("\nRetrieved Documents\n")

for i, doc in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print(f"Source : {doc.metadata.get('source')}")
    print(f"Type   : {doc.metadata.get('type')}")
    print("-" * 60)
    print(doc.page_content[:500])
    print()