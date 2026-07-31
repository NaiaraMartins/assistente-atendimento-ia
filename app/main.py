from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.messages import router as messages_router

app = FastAPI(
    title="Assistente Atendimento IA",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(messages_router)