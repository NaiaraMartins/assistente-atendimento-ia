from app.services.llm_service import LLMService
from app.services.knowledge_service import KnowledgeService


class ConversationService:

    def __init__(self):
        self.llm_service = LLMService()
        self.knowledge_service = KnowledgeService()

    def process(self, message: str) -> str:

        knowledge = self.knowledge_service.load()

        return self.llm_service.generate(
            message=message,
            knowledge=knowledge
        )