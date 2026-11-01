"""Leading p-adic pattern of f_n at delta=a/p (a odd), f1 = sin theta: for n in a list, print min valuation and
the residues of p^{-v} * coefficient mod p for all modes (v = min valuation), plus the next layer.
Usage: pattern_odd.py p a n1,n2,..."""
import sys
from fractions import Fraction as Fr
from kappa_odd import run


def val(x, p):
    v = 0; num, den = x.numerator, x.denominator
    while num % p == 0: num //= p; v += 1
    while den % p == 0: den //= p; v -= 1
    return v


def res(x, p, v):
    y = x / Fr(p) ** v
    if y.denominator % p == 0: return None
    return (y.numerator * pow(y.denominator, -1, p)) % p


p, a = int(sys.argv[1]), int(sys.argv[2])
ns = [int(t) for t in sys.argv[3].split(',')]
f, g = run(a, p, {1: Fr(1)}, max(ns))
for n in ns:
    for name, ser in (('f', f[n]), ('g', g.get(n, {}))):
        if not ser: continue
        vmin = min(val(x, p) for x in ser.values() if x != 0)
        modes = sorted(ser)
        for v in (vmin, vmin + 1):
            row = []
            for k in modes:
                x = ser[k]
                if val(x, p) < v: row.append('*')
                else: row.append(str(res(x, p, v)))
            print(f"{name}_{n} v={v}: " + ' '.join(f"{k}:{r}" for k, r in zip(modes, row) if r != '0'))
