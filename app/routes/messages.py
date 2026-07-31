from fastapi import APIRouter

from app.models.message import MessageRequest
from app.services.conversation_service import ConversationService

router = APIRouter()

conversation_service = ConversationService()


@router.post("/messages")
def send_message(request: MessageRequest):
    return {
        "response": conversation_service.process(request.message)
    }