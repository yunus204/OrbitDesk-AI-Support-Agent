from llm.local_llm import LocalLLM

print("Loading model...")

llm = LocalLLM()

print("Model loaded successfully!")

prompt = """
You are a helpful assistant.

Question:
What is Python?

Answer:
"""

response = llm.generate(prompt)

print("\nResponse:\n")
print(response)