from .creator_base import NotifierCreator
from ..simple_factory.sms import SMSNotifier
from ..simple_factory.base import Notifier

class SMSNotifierCreator(NotifierCreator):
    def create_notifier(self) -> Notifier:
        return SMSNotifier()