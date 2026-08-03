from retrieval.retriever import Retriever


class RetrievalNode:

    def __init__(self):
        self.retriever = Retriever()

    def __call__(self, state):

        docs = self.retriever.search(state["question"])

        state["retrieved_docs"] = docs

        print(f"[RETRIEVAL] Retrieved {len(docs)} documents")

        return state