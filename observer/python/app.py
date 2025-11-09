from .subject import Subject
from .observer import Observer

# A concrete observer
class ConsoleObserver(Observer):
    def update(self, data):
        print("Received:", data)

# Subject
subject = Subject()

# Attach observer
obs1 = ConsoleObserver()
subject.attach(obs1)

# Notify
subject.notify("Bro, something changed!")
subject.notify({"price": 200, "symbol": "AAPL"})
