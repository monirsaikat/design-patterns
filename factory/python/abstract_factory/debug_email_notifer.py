from ..simple_factory.base import Notifier

class DebugEmailNotifier(Notifier):
    def send(self, to: str, msg: str) -> None:
        print(f"[DEBUG EMAIL] (no-op) to={to} msg={msg}")
