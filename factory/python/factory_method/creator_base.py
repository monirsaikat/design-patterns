from abc import ABC, abstractmethod
from ..simple_factory.base import Notifier

class NotifierCreator(ABC):
    # factory method
    @abstractmethod
    def create_notifier(self) -> Notifier:
        ...
    
    # a template method to consume
    def send_welcome(self, to: str, name: str) -> None:
        n = self.create_notifier()
        n.send(to, f"Welcome, {name}")
        
    # ekhane ekta simple way dekhano hoiche, jegula real life a use hoite pare 
    def send_invoice_due(self, to: str, name: str, amount: float) -> None:
        n = self.create_notifier()
        n.send(to, f"Hey, {name}. You have an invoice due of {amount} USD. Please make a payment asap.")