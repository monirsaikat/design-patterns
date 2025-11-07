from abc import ABC, abstractmethod
from ..simple_factory.base import Notifier

class NotifierSuiteFactory(ABC):
    @abstractmethod
    def create_email(self) -> Notifier:...

    @abstractmethod
    def create_sms(self) -> Notifier: ...
        