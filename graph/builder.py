from langgraph.graph import StateGraph, END

from graph.state import AgentState

from nodes.triage import TriageNode
from nodes.retrieval import RetrievalNode
from nodes.answer import AnswerNode
from nodes.verification import VerificationNode
from nodes.clarification import ClarificationNode
from nodes.escalation import EscalationNode



def router(state):
    return state["classification"]

    # return state["route"] 
def verification_router(state):

    if state["verified"]:
        return "success"

    if state["retry_count"] >= 1:
        return "fail"

    state["retry_count"] += 1

    return "retry"

workflow = StateGraph(AgentState)

workflow.add_node("triage", TriageNode())
workflow.add_node("retrieval", RetrievalNode())
workflow.add_node("answer", AnswerNode())
workflow.add_node("verification", VerificationNode())


workflow.set_entry_point("triage")
workflow.add_node("clarification", ClarificationNode())
workflow.add_node("escalation", EscalationNode())


workflow.add_conditional_edges(
    "triage",
    router,
    {
        "retrieval": "retrieval",
        "clarification": "clarification",
        "escalation": "escalation",
    },
)

workflow.add_edge("clarification", END)
workflow.add_edge("escalation", END)


workflow.add_edge("retrieval", "answer")
workflow.add_edge("answer", "verification")
workflow.add_conditional_edges(
    "verification",
    verification_router,
    {
        "success": END,
        "retry": "answer",
        "fail": END,
    },
)


graph = workflow.compile()