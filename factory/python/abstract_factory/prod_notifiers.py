from ..simple_factory.base import Notifier 

class ProductionEmailNotifer(Notifier):
    def send(self, to: str, msg: str) -> None:
        # eikhane amra smtp or jekono mail service use korte pari
        print(f"[PROD EMAIL] to={to} msg={msg}")

class ProductionSMSNotifier(Notifier):
    def send(self, to: str, msg: str) -> None:
        # eikhan theke amra sms provider use korte pari
        print(f"[PROD SMS] to={to} msg={msg}")