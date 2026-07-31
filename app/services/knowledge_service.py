from pathlib import Path


class KnowledgeService:

    def load(self) -> str:
        knowledge_file = Path("company/knowledge.md")

        return knowledge_file.read_text(encoding="utf-8")