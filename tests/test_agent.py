from graph.builder import graph


def run_query(question):

    state = {
        "question": question,
        "classification": "",
        "retrieved_docs": [],
        "answer": "",
        "sources": [],
        "confidence": 0.0,
        "verified": False,
        "requires_human": False,
        "reason": "",
        "retry_count": 0,
    }

    return graph.invoke(state)


def test_retrieval():

    result = run_query("How do I create API credentials?")

    assert result["classification"] == "retrieval"
    assert result["verified"] is True
    assert "API" in result["answer"]


def test_clarification():

    result = run_query("Help")

    assert result["classification"] == "clarification"
    assert "more details" in result["answer"].lower()


def test_escalation():

    result = run_query("Refund my subscription")

    assert result["classification"] == "escalation"
    assert result["requires_human"] is True