from ..simple_factory.base import Notifier

class DebugSMSNotifier(Notifier):
    def send(self, to: str, msg: str) -> None:
        print(f"[DEBUG SMS] (no-op) to={to} msg={msg}")
