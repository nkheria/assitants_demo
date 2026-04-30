# core/chatbot.py

from core.assistant_manager import AssistantManager
from core.thread_manager import ThreadManager
from core.run_manager import RunManager


class Chatbot:
    def __init__(self):
        self._assistant_mgr = AssistantManager()
        self._thread_mgr = ThreadManager()
        self._run_mgr = RunManager()

        self.assistant_id = None
        self.thread_id = None

    def setup(self):
        print("[SETUP] Creating Assistant...")
        self.assistant_id = self._assistant_mgr.create()

        print("[SETUP] Creating Thread...")
        self.thread_id = self._thread_mgr.create()

    def ask(self, user_input: str):
        # Step 1: Add user message
        self._thread_mgr.add_user_message(user_input)

        # Step 2: Execute Run
        result = self._run_mgr.execute(self.thread_id, self.assistant_id)

        # Step 3: Fetch reply
        reply = self._thread_mgr.get_latest_reply()

        return reply, result.get("usage", {})

    def new_conversation(self):
        print("[INFO] Starting new conversation...")
        self._thread_mgr.delete()
        self.thread_id = self._thread_mgr.create()

    def teardown(self):
        print("[CLEANUP] Deleting Thread & Assistant...")
        self._thread_mgr.delete()
        self._assistant_mgr.delete()