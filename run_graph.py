from graph.builder import graph
import json

state = {
    "question": input("Ask: "),
    "classification": "",
    "retrieved_docs": [],
    "answer": "",
    "sources": [],
    "confidence": 0.0,
    "requires_human": False,
    "reason": "",
    "verified": False,
    "retry_count": 0,
}

result = graph.invoke(state)

print("\n========== RESULT ==========")

print(f"Answer:\n{result['answer']}\n")

print("Sources:")
for source in result["sources"]:
    print("-", source)

print(f"\nConfidence : {result['confidence']}")
print(f"Verified   : {result['verified']}")
print(f"Reason     : {result['reason']}")
final_output = {
    "classification": result["classification"],
    "answer": result["answer"],
    "sources": result["sources"],
    "confidence": result["confidence"],
    "verified": result["verified"],
    "requires_human": result["requires_human"],
    "reason": result["reason"],
}

print("\n========== FINAL OUTPUT ==========\n")
print(json.dumps(final_output, indent=4))