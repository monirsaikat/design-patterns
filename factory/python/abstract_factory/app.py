from .prod_factory import ProdFactory
from .debug_factory import DebugFactory
from .factory_base import NotifierSuiteFactory

def run_flow(factory: NotifierSuiteFactory) -> None:
    email = factory.create_email()
    sms = factory.create_sms()

    email.send("email@gmail.com", "Welcome via Email (family selected)")
    sms.send("+8801712345678", "Welcome via SMS (family selected)")

if __name__ == "__main__":
    print("== PROD family ==")
    run_flow(ProdFactory())

    print("\n== DEBUG family ==")
    run_flow(DebugFactory())
