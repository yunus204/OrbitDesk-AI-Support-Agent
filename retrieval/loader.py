from pathlib import Path
import json
from langchain_core.documents import Document


class KnowledgeBaseLoader:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.kb_dir = self.data_dir / "knowledge_base"
        self.cases_file = self.data_dir / "resolved_cases.json"

    def load_markdown_files(self):
        documents = []

        if not self.kb_dir.exists():
            raise FileNotFoundError(f"{self.kb_dir} not found.")

        for file in self.kb_dir.rglob("*.md"):
            text = file.read_text(encoding="utf-8")

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": file.name,
                        "type": "knowledge_base",
                    },
                )
            )

        return documents

    def load_resolved_cases(self):
        documents = []

        if not self.cases_file.exists():
            return documents

        with open(self.cases_file, "r", encoding="utf-8") as f:
            cases = json.load(f)

        for case in cases:
            content = f"""
Issue:
{case.get('issue', '')}

Resolution:
{case.get('resolution', '')}
"""

            documents.append(
                Document(
                    page_content=content.strip(),
                    metadata={
                        "source": "resolved_cases.json",
                        "case_id": case.get("id", ""),
                        "type": "resolved_case",
                    },
                )
            )

        return documents

    def load_all_documents(self):
        documents = []

        documents.extend(self.load_markdown_files())
        documents.extend(self.load_resolved_cases())

        return documents