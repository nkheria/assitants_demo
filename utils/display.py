# utils/display.py

def show_banner():
    print("\n==============================")
    print("   DataBot Assistant Started")
    print("==============================\n")


def show_reply(reply: str):
    print(f"\nDataBot: {reply}\n")


def show_usage(usage: dict):
    if usage:
        print(
            f"[Tokens] Prompt: {usage.prompt_tokens}, "
            f"Completion: {usage.completion_tokens}, "
            f"Total: {usage.total_tokens}"
        )