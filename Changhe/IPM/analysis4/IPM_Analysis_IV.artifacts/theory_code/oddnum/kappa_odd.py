"""Exact first compatibility coefficient at delta = a/p with a odd (first resonance n0 = 2p, j0 = a-1).
kappa = coefficient of sin((2a-3)theta) in f_{2p}.  Prints v_p(kappa) and the p-adic unit part mod p.
Usage: kappa_odd.py pmax [profile: sin1 | list of (mode,coef) as m:c,m:c]"""
import sys
from fractions import Fraction as Fr
from collections import defaultdict


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def add(d, k, v):
    if k == 0:
        return
    if k < 0:
        k, v = -k, -v
    d[k] += v


def mul_sin_cos(S, C):
    out = defaultdict(Fr)
    for A, a in S.items():
        for B, b in C.items():
            add(out, A + B, a * b / 2)
            add(out, A - B, a * b / 2)
    return out


def poisson(fn, Pn):
    gn = defaultdict(Fr)
    for k, v in fn.items():
        m = (k - 1) // 2
        # a_m enters b_{m+1} via (P - 2(m+1)) ... use formula (4): b_j = [(p-2j+1)a_{j-1}+(p+2j+1)a_j]/(2(4j^2-(p+1)^2)), P=p+1
        j = m + 1
        den = 2 * (4 * j * j - Pn * Pn)
        gn[2 * j] += (Pn - 2 * j) * v / den
        j = m
        if j >= 1:
            den = 2 * (4 * j * j - Pn * Pn)
            gn[2 * j] += (Pn + 2 * j) * v / den
    return {k: v for k, v in gn.items() if v != 0}


def run(a, p, f1, nmax):
    delta = Fr(a, p)
    c = 1 / (1 - delta)
    f = {1: dict(f1)}
    g = {}
    for n in range(1, nmax + 1):
        if n >= 2:
            acc = defaultdict(Fr)
            for i in range(1, n):
                j = n - i
                Pi = 2 - i * delta
                pj = 1 - j * delta
                fjp = {k: k * v for k, v in f[j].items()}
                gip = {k: k * v for k, v in g[i].items()}
                for k, v in mul_sin_cos(g[i], fjp).items():
                    acc[k] += Pi * v
                for k, v in mul_sin_cos(f[j], gip).items():
                    acc[k] -= pj * v
            lam = (n - 1) * (c - 1)
            f[n] = {k: v / lam for k, v in acc.items() if v != 0}
        if n < nmax:
            Pn = 2 - n * delta
            g[n] = poisson(f[n], Pn)
    return f, g


def vp(x, p):
    if x == 0:
        return None
    v = 0
    num, den = x.numerator, x.denominator
    while num % p == 0:
        num //= p; v += 1
    while den % p == 0:
        den //= p; v -= 1
    return v, (num * pow(den, -1, p)) % p


if __name__ == '__main__':
    pmax = int(sys.argv[1])
    prof = sys.argv[2] if len(sys.argv) > 2 else 'sin1'
    if prof == 'sin1':
        f1 = {1: Fr(1)}
    else:
        f1 = {int(t.split(':')[0]): Fr(t.split(':')[1]) for t in prof.split(',')}
    for p in range(5, pmax + 1):
        if not is_prime(p):
            continue
        for a in range(3, p, 2):
            f, g = run(a, p, f1, 2 * p)
            kap = f[2 * p].get(2 * a - 3, Fr(0))
            # also valuations of f_n at n = p, p+1
            minv = {}
            for n in (p - 1, p, p + 1, 2 * p - 1, 2 * p):
                vals = [vp(v, p)[0] for v in f[n].values() if v != 0]
                minv[n] = min(vals) if vals else None
            gv = [vp(v, p)[0] for v in g[p].values()]
            print(f"p={p} a={a} delta={a}/{p} kappa_vp={vp(kap, p)} minv_f={minv} minv_g_p={min(gv) if gv else None}", flush=True)
