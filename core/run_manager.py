# core/run_manager.py

import time
from openai import OpenAI
from config.settings import OPENAI_API_KEY, POLL_INTERVAL_SECONDS, MAX_POLL_ATTEMPTS


class RunManager:
    def __init__(self):
        self._client = OpenAI(api_key=OPENAI_API_KEY)

    def execute(self, thread_id: str, assistant_id: str) -> dict:
        run = self._client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )

        attempts = 0

        while attempts < MAX_POLL_ATTEMPTS:
            time.sleep(POLL_INTERVAL_SECONDS)

            run = self._client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id,
            )

            if run.status == "completed":
                return {"status": "completed", "usage": run.usage}

            if run.status in ["failed", "expired"]:
                return {"status": run.status}

            attempts += 1

        return {"status": "timeout"}