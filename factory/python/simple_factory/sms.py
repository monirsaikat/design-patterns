from .base import Notifier

class SMSNotifier:
    def send(self, to: str, msg: str) -> None:
        print(f"[SMS] to={to} msg={msg}")