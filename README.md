# 🤖 OrbitDesk AI Support Agent

An intelligent Retrieval-Augmented Generation (RAG) support assistant built with **LangGraph**, **FAISS**, **Hugging Face Transformers**, and **Qwen2.5-1.5B-Instruct**.

The agent answers OrbitDesk support questions using a local knowledge base, verifies responses, requests clarification for ambiguous queries, and escalates unsupported requests to a human support engineer.

---

# 🚀 Features

- ✅ Local RAG (Retrieval-Augmented Generation)
- ✅ LangGraph Agent Workflow
- ✅ FAISS Vector Database
- ✅ Hugging Face Embeddings
- ✅ Qwen2.5-1.5B-Instruct Local LLM
- ✅ Knowledge Base Search
- ✅ Automatic Query Classification
- ✅ Verification Node
- ✅ Retry Logic
- ✅ Clarification Handling
- ✅ Human Escalation
- ✅ Confidence Score
- ✅ Source Attribution
- ✅ Structured JSON Output
- ✅ Automated Tests (Pytest)

---

# 🏗️ System Architecture

```
                User Question
                      │
                      ▼
                Triage Node
      ┌─────────┼──────────┐
      │         │          │
      ▼         ▼          ▼
Clarification Retrieval Escalation
                  │
                  ▼
           FAISS Retriever
                  │
                  ▼
            Answer Generator
                  │
                  ▼
          Verification Node
           │              │
           ▼              ▼
        Success        Retry Once
           │              │
           └──────► Final Response
```

---

# 📂 Project Structure

```
orbitdesk-ai-support-agent/
│
├── data/
│   └── knowledge_base/
│
├── graph/
│   ├── builder.py
│   └── state.py
│
├── llm/
│   ├── local_llm.py
│   └── prompts.py
│
├── nodes/
│   ├── answer.py
│   ├── clarification.py
│   ├── escalation.py
│   ├── retrieval.py
│   ├── triage.py
│   └── verification.py
│
├── retrieval/
│   ├── embeddings.py
│   ├── loader.py
│   ├── retriever.py
│   └── vectorstore.py
│
├── vectorstore/
│
├── tests/
│   ├── conftest.py
│   └── test_agent.py
│
├── build_vectorstore.py
├── run_agent.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

- Python 3.13
- LangGraph
- LangChain
- FAISS
- Hugging Face Transformers
- Hugging Face Embeddings
- Qwen2.5-1.5B-Instruct
- PyTorch
- Pytest

---
## Model

LLM:
- Qwen2.5-1.5B-Instruct

Embeddings:
- sentence-transformers/all-MiniLM-L6-v2

Vector Store:
- FAISS

Framework:
- LangGraph

Python:
- 3.13

Hardware:
- Windows 11
- Intel Processor
- 16 GB DDR4 RAM
---
# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/orbitdesk-ai-support-agent.git
cd orbitdesk-ai-support-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🧠 Build the Vector Database

Run:

```bash
python build_vectorstore.py
```

Expected output:

```
✅ FAISS index created successfully!
```

---

# ▶️ Run the AI Support Agent

```bash
python run_agent.py
```

Example questions:

```
How do I create API credentials?

Where are audit logs located?

Help

Refund my subscription
```

---

# 🧪 Run Tests

```bash
pytest tests
```

Expected:

```
========================
3 passed
========================
```
## AI Assistance Disclosure

This project was developed by me as part of the AI Engineer Internship assignment.

During development, I used AI coding assistants (ChatGPT) to:

- Understand LangGraph concepts
- Debug Python errors
- Improve code structure
- Generate documentation
- Review implementation

I understand the complete codebase and can explain the architecture, workflow, and implementation decisions during an interview.
---
workflow diagram: <img width="1536" height="1024" alt="Local Retrieval-Augmented Generation (RAG) Workflow png" src="https://github.com/user-attachments/assets/f34809e4-559b-4493-a5d8-5366fc31b27c" />


---

# 📋 Example Output

```json
{
    "classification": "retrieval",
    "answer": "Owners and Admins can view workspace audit logs from Settings > Audit log.",
    "sources": [
        "09_audit_logs.md",
        "08_escalation_and_diagnostics.md"
    ],
    "confidence": 0.9,
    "verified": true,
    "requires_human": false,
    "reason": "Answer supported by retrieved evidence."
}
```

---

# 🔄 Workflow

1. User submits a question.
2. Triage Node classifies the request.
3. Retrieval Node searches the FAISS vector database.
4. Answer Node generates a response using the local LLM.
5. Verification Node validates the answer.
6. If verification fails, the agent retries once.
7. If still unsuccessful, the final response is returned.
8. Clarification and Escalation requests bypass retrieval when appropriate.

---

# 📈 Current Capabilities

- Answer support questions using a knowledge base.
- Retrieve relevant documents using semantic search.
- Generate responses with a local language model.
- Verify answer quality.
- Handle ambiguous queries with clarification.
- Escalate unsupported requests.
- Return structured JSON responses.

---

# 🔮 Future Improvements

- Streamlit Web Interface
- FastAPI REST API
- Conversation Memory
- Multi-turn Chat Support
- Hybrid Search (BM25 + FAISS)
- Reranking Model
- Docker Support
- Authentication
- Logging & Monitoring
- Deployment on Cloud

---

# 👨‍💻 Author

**MohammadYunus Mulla**

AI & Machine Learning Enthusiast

- Python
- Machine Learning
- Generative AI
- LangChain
- LangGraph
- Retrieval-Augmented Generation (RAG)

---

# 📄 License

This project is intended for educational and internship purposes.
