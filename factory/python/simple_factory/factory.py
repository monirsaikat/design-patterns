from .email import EmailNotifier
from .sms import SMSNotifier
from typing import Dict, Type

"""Simple use of factory"""
def make_notifier(kind: str):
    if kind == 'email':
        return EmailNotifier()
    if kind == 'sms':
        return SMSNotifier()
    raise ValueError(f"Unknown kind: {kind}")

"""Registry based uses of factory"""
_REGISTRY: Dict[str, Type] = {
    'email': EmailNotifier,
    'sms': SMSNotifier
}

# this is an function to register a new notifier at runtime
def register(kind: str, cls: Type):
    _REGISTRY[kind] = cls 
    
def make_notifier_v2(kind: str):
    try:
        return _REGISTRY[kind]()
    except KeyError:
        raise ValueError(f"Unknow kind: {kind} Known: {list(_REGISTRY)}")