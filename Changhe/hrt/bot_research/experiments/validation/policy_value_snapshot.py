"""Canonical logical policy values, including nested objects and bound methods.

Shared module globals and process time are outside this snapshot. Object fields,
function defaults and closure values are included; unexpected values fail closed.
"""
from dataclasses import fields, is_dataclass
from types import FunctionType, MethodType


def freeze_state(value, active=None):
    if active is None:
        active = set()
    if value is None or isinstance(value, (bool,int,float,str)):
        return (type(value).__name__,value)
    identity = id(value)
    if identity in active:
        raise ValueError('Cyclic policy value is outside this checker scope.')
    active.add(identity)
    try:
        rec = lambda v:freeze_state(v,active)
        if isinstance(value,dict):
            return ('dict',tuple(sorted(((rec(k),rec(v)) for k,v in value.items()),key=repr)))
        if isinstance(value,(list,tuple)):
            return (type(value).__name__,tuple(rec(v) for v in value))
        if isinstance(value,(set,frozenset)):
            return (type(value).__name__,tuple(sorted((rec(v) for v in value),key=repr)))
        if isinstance(value,MethodType):
            return ('method',rec(value.__func__),rec(value.__self__))
        if isinstance(value,FunctionType):
            return ('function',value.__module__,value.__qualname__,
                    tuple((n,rec(c.cell_contents)) for n,c in zip(value.__code__.co_freevars,value.__closure__ or ())),
                    rec(value.__defaults__),rec(value.__kwdefaults__),rec(vars(value)))
        if is_dataclass(value):
            return ('dataclass',type(value).__module__,type(value).__qualname__,
                    tuple((f.name,rec(getattr(value,f.name))) for f in fields(value)))
        if type(value).__module__.startswith(('bot_research.','td_game.')) and hasattr(value,'__dict__'):
            return ('object',type(value).__module__,type(value).__qualname__,rec(vars(value)))
        raise TypeError(f'Unsupported policy value {type(value).__module__}.{type(value).__qualname__}')
    finally:
        active.remove(identity)
