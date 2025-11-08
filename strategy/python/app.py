from .payment_handlers.bkash_payment import BkashPayment
from .payment_handlers.nagad_payment import NagadPayment
from .payment_handlers.card_payment import CardPayment
from .payment_processor import PaymentProcessor

if __name__ == '__main__':
    payment_processor = PaymentProcessor(BkashPayment(), 'BDT')
    payment_processor.checkout(100)

    payment_processor.set_currency('USD')
    payment_processor.set_strategy(CardPayment())
    payment_processor.checkout(200)

    print(payment_processor.get_total_paid_amount())