from .email_creator import EmailNotifierCreator
from .sms_creator import SMSNotifierCreator

if __name__ == '__main__':
    # EmailNotifierCreator().send_welcome('alice@gmail.com', 'Mr Alice')
    EmailNotifierCreator().send_invoice_due('bob@gmail.com', 'Bob', 200)
    SMSNotifierCreator().send_invoice_due("+8801XXXXXXX", "Saikat", 1999)
