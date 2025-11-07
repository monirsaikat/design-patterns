from .creator_base import NotifierCreator
from ..simple_factory.email import EmailNotifier
from ..simple_factory.base import Notifier

class EmailNotifierCreator(NotifierCreator):
    def create_notifier(self) -> Notifier:
        return EmailNotifier()