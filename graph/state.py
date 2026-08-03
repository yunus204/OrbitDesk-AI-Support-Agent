from typing import TypedDict, List
from langchain_core.documents import Document


class AgentState(TypedDict):
    question: str
    classification: str

    retrieved_docs: List[Document]

    answer: str

    sources: list

    confidence: float

    requires_human: bool

    reason: str

    verified: bool

    retry_count: int