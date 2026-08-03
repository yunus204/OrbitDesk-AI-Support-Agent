class TriageNode:

    def __call__(self, state):
        question = state["question"].lower()

        if len(question.strip()) < 10:
            route = "clarification"

        elif any(word in question for word in [
            "refund",
            "billing",
            "legal",
            "complaint"
        ]):
            route = "escalation"

        else:
            route = "retrieval"

        state["classification"] = route

        print(f"[TRIAGE] → {route}")

        return state