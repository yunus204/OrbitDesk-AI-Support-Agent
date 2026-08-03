from retrieval.retriever import Retriever
from nodes.answer import AnswerNode

retriever = Retriever()
answer_node = AnswerNode()

question = input("Ask: ")

docs = retriever.search(question)

state = {
    "question": question,
    "route": "retrieval",
    "retrieved_docs": docs,
    "answer": "",
    "retry_count": 0,
    "verified": False
}

result = answer_node(state)

print("\nGenerated Answer:\n")
print(result["answer"])