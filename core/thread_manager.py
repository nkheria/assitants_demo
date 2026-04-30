# core/thread_manager.py

from openai import OpenAI
from config.settings import OPENAI_API_KEY


class ThreadManager:
    def __init__(self):
        self._client = OpenAI(api_key=OPENAI_API_KEY)
        self.thread_id = None

    def create(self) -> str:
        thread = self._client.beta.threads.create()
        self.thread_id = thread.id
        return self.thread_id

    def delete(self):
        if self.thread_id:
            self._client.beta.threads.delete(self.thread_id)

    def add_user_message(self, content: str):
        self._client.beta.threads.messages.create(
            thread_id=self.thread_id,
            role="user",
            content=content,
        )

    def get_latest_reply(self) -> str:
        messages = self._client.beta.threads.messages.list(
            thread_id=self.thread_id
        )

        for msg in messages.data:
            if msg.role == "assistant":
                return msg.content[0].text.value

        return "(no reply)"