from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def supported_currencies(self):
        pass
    
    @abstractmethod
    def pay(self, amount: float) -> None: ...