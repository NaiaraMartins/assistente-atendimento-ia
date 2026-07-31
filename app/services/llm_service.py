from openai import OpenAI

from app.config.settings import Settings


class LLMService:

    def __init__(self):
        self.settings = Settings()

        self.client = OpenAI(
            api_key=self.settings.openai_api_key
        )

    def generate(
        self,
        message: str,
        knowledge: str
    ) -> str:

        prompt = f"""
Você é um assistente virtual.

Responda utilizando exclusivamente as informações abaixo.

Conhecimento:
{knowledge}

Pergunta:
{message}
"""

        response = self.client.responses.create(
            model=self.settings.openai_model,
            input=prompt
        )

        return response.output_text