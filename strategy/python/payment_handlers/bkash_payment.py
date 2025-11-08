from ..payment_strategy import PaymentStrategy
from .payment_error import PaymentError

class BkashPayment(PaymentStrategy):
    def pay(self, amount: float, currency: str):
        if not currency in self.supported_currencies():
            raise PaymentError(f"Currency does not support. Supported currencies {self.supported_currencies()}")

        print(f"[bkash]: paid {amount} successfully")

    def supported_currencies(self):
        return ['BDT']