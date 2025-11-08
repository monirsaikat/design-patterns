from .payment_strategy import PaymentStrategy

class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy, currency = 'usd'):
        self.currency = currency
        self.total_paid = 0
        self.payment_strategy = payment_strategy;

    def set_currency(self, curr: str):
        self.currency = curr

    def set_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self, amount: float):
        self.total_paid += amount
        self.payment_strategy.pay(amount, self.currency)

    def get_total_paid_amount(self):
        return self.total_paid