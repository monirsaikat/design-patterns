from .factory_base import NotifierSuiteFactory
from ..simple_factory.base import Notifier
from .prod_notifiers import ProductionEmailNotifer, ProductionSMSNotifier

class ProdFactory(NotifierSuiteFactory):
    def create_email(self) -> Notifier:
        return ProductionEmailNotifer()

    def create_sms(self) -> Notifier:
        return ProductionSMSNotifier()
