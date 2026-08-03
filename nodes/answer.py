from llm.local_llm import LocalLLM
from llm.prompts import SYSTEM_PROMPT


class AnswerNode:

    def __init__(self):
        self.llm = LocalLLM()

    def __call__(self, state):

        context = "\n\n".join(
            doc.page_content for doc in state["retrieved_docs"]
        )

        prompt = f"""
Context:
{context}

Question:
{state["question"]}

Answer:
"""

        answer = self.llm.generate(prompt)

        state["answer"] = answer.strip()

        # Remove duplicate source names
        seen = set()
        sources = []

        for doc in state["retrieved_docs"]:
            source = doc.metadata.get("source", "Unknown")

            if source not in seen:
                seen.add(source)
                sources.append(source)

        state["sources"] = sources

        state["confidence"] = 0.85
        state["requires_human"] = False
        state["reason"] = "Generated using retrieved knowledge base."

        print("[ANSWER] Generated response")

        return state