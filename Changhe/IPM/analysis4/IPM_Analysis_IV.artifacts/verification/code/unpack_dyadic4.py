"""Decode the retained four-field exact dyadic midpoint and radius."""
from stream_precision_audit import dyadic

def unpack(record):
    m, e, r, re = record
    mid, radius = dyadic(m, e), dyadic(r, re)
    assert radius >= 0
    return mid, radius
