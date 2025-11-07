from .base import Notifier
import re

_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

class EmailNotifier(Notifier):
    def send(self, to: str, msg: str) -> None:
        if not _EMAIL_RE.match(to.strip()):
            raise ValueError(f"Invalid email adderss : {to}")    

        print(f"[EMAIL] to={to} msg={msg}")