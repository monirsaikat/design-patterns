from ..simple_factory.base import Notifier
from .debug_email_notifer import DebugEmailNotifier
from .debug_sms_notifer import DebugSMSNotifier
from .factory_base import NotifierSuiteFactory

class DebugFactory(NotifierSuiteFactory):
    def create_email(self) -> Notifier:
        return DebugEmailNotifier()

    def create_sms(self) -> Notifier:
        return DebugSMSNotifier()
