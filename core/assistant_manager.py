# core/assistant_manager.py

from openai import OpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME, ASSISTANT_NAME, SYSTEM_PROMPT


class AssistantManager:
    def __init__(self):
        self._client = OpenAI(api_key=OPENAI_API_KEY)
        self.assistant_id = None

    def create(self) -> str:
        assistant = self._client.beta.assistants.create(
            name=ASSISTANT_NAME,
            instructions=SYSTEM_PROMPT,
            model=MODEL_NAME,
        )
        self.assistant_id = assistant.id
        return self.assistant_id

    def delete(self):
        if self.assistant_id:
            self._client.beta.assistants.delete(self.assistant_id)