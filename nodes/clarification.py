class ClarificationNode:

    def __call__(self, state):

        state["answer"] = (
            "Could you please provide more details "
            "about your issue?"
        )

        print("[CLARIFICATION]")

        return state