class VerificationNode:

    def __call__(self, state):

        answer = state["answer"].strip()

        # Rule 1: Empty answer
        if not answer:
            state["verified"] = False
            state["reason"] = "Empty answer generated."

        # Rule 2: Sources must exist
        elif not state["sources"]:
            state["verified"] = False
            state["reason"] = "No supporting sources."

        # Rule 3: Safe failure response
        elif "I couldn't find" in answer:
            state["verified"] = True
            state["confidence"] = 0.30
            state["reason"] = "No matching information found."

        # Rule 4: Normal successful answer
        else:
            state["verified"] = True
            state["confidence"] = 0.90
            state["reason"] = "Answer supported by retrieved evidence."

        print(f"[VERIFICATION] Verified = {state['verified']}")

        return state