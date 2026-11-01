"""Independent exact check of the prime-denominator congruence.

For delta = a/p (p odd prime, a even, 4 <= a < p) and f_1 = sin(theta), compute the pure
recursion (R), (B) exactly up to order p and report kappa = coefficient of sin((a-3)theta)
in f_p, its residue mod p, the predicted residue (-1)^((a-4)/2), and whether every sine
coefficient of f_p reduces to the predicted pattern ((-1)^l at mode 2l+1, 0 at mode p).
Usage: prime_kappa_check.py pmax
"""
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


def run(a, p):
    delta = Fr(a, p)
    c = 1 / (1 - delta)
    f = {1: {1: Fr(1)}}
    g = {}
    for n in range(1, p + 1):
        if n >= 2:
            acc = defaultdict(Fr)
            for i in range(1, n):
                j = n - i
                Pi = 2 - i * delta
                pj = 1 - j * delta
                fjp = {k: k * v for k, v in f[j].items()}            # cosine series
                gip = {k: k * v for k, v in g[i].items()}            # cosine series
                for k, v in mul_sin_cos(g[i], fjp).items():
                    acc[k] += Pi * v
                for k, v in mul_sin_cos(f[j], gip).items():
                    acc[k] -= pj * v
            lam = (n - 1) * (c - 1)
            f[n] = {k: v / lam for k, v in acc.items() if v != 0}
        if n < p:
            Pn = 2 - n * delta
            gn = defaultdict(Fr)
            for k, v in f[n].items():          # k = 2m+1, a_m = v
                m = (k - 1) // 2
                # a_m enters b_{m+1} with -1/(2(2(m+1)+P)) and b_m with +1/(2(2m-P))
                gn[2 * (m + 1)] += -v / (2 * (2 * (m + 1) + Pn))
                if m >= 1:
                    gn[2 * m] += v / (2 * (2 * m - Pn))
            g[n] = dict(gn)
    fp = f[p]
    kappa = fp.get(a - 3, Fr(0))
    def red(x):
        return (x.numerator * pow(x.denominator, -1, p)) % p
    pattern_ok = True
    for l in range(p):
        mode = 2 * l + 1
        want = 0 if mode == p else (-1) ** l
        if red(fp.get(mode, Fr(0))) != want % p:
            pattern_ok = False
    return kappa, red(kappa), ((-1) ** ((a - 4) // 2)) % p, pattern_ok


if __name__ == "__main__":
    pmax = int(sys.argv[1])
    for p in range(5, pmax + 1):
        if not is_prime(p):
            continue
        for a in range(4, p, 2):
            kappa, r, want, ok = run(a, p)
            print(f"p={p} a={a} kappa={float(kappa):.6e} kappa mod p={r} predicted={want} "
                  f"match={r == want} full_pattern={ok}", flush=True)
