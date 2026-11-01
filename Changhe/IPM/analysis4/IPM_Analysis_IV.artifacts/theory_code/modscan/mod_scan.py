"""First compatibility coefficient at delta = 2h/Q (gcd(h,Q) = 1, h >= 2, 2h < Q) by the polar Fourier recursion over
GF(ell), ell a prime below 2^25 (so int64 convolutions cannot overflow).

Recursion (as in code/tuned/hh_tune.py): lambda_n f_n = sum_{i+j=n} [P_i g_i f_j' - p_j g_i' f_j], lambda_n = (n-1)(c-1),
p_n = 1 - n delta, P_n = 2 - n delta, c - 1 = 2h/(Q-2h); Poisson inverse
Pi_n sin(l theta) = sin((l-1) theta)/(2(l-1-P_n)) - sin((l+1) theta)/(2(l+1+P_n)) (no first term for l = 1).
All orders n < Q are nonresonant (no Poisson denominator vanishes), and the first obstruction is the coefficient
kappa = [sin((2h-3) theta)] f_Q.  The recursion only divides by the rationals lambda_n, 2(l -+ 1 -+ P_n) and 2; every such
divisor is checked to be nonzero modulo ell (its numerator is a small nonzero integer), so the computation is the exact
reduction modulo ell of the rational recursion, and kappa mod ell != 0 proves kappa != 0.  If kappa = 0 mod ell, a second
prime is tried; zero modulo both is reported as 'zero mod both primes' (consistent with kappa = 0, not a proof of it).

usage: mod_scan.py profile Qmax lo hi [out.jsonl]     profile: 'sin1', 'cand007' or 'm1:c1,m2:c2,...' (rationals)
"""
import sys, json, time, math
from fractions import Fraction as Fr
import numpy as np

PRIMES = [33554393, 33554383, 33554371]          # primes just below 2^25


def load_profile(name):
    if name == 'sin1':
        return {1: Fr(1)}
    if name == 'cand007':
        d = json.load(open('../tuned/candidate007_leading_exact.json'))
        return {int(k): Fr(v) for k, v in d['density'].items() if Fr(v) != 0}
    return {int(a): Fr(b) for a, b in (x.split(':') for x in name.split(','))}


def red(x, ell):
    x = Fr(x)
    num, den = x.numerator % ell, x.denominator % ell
    assert den != 0, ('denominator divisible by ell', x)
    return num * pow(den, ell - 2, ell) % ell


def kappa_mod(F1, Q, h, ell):
    dl = Fr(2 * h, Q)
    cm1 = Fr(2 * h, Q - 2 * h)
    L = max(F1)
    B = L + 1
    M = B * Q + 2                                   # array length (frequencies 0..M-1)
    inv2 = pow(2, ell - 2, ell)
    idx = np.arange(M, dtype=np.int64)
    F, G = {}, {}
    f1 = np.zeros(M, dtype=np.int64)
    for m, v in F1.items():
        f1[m] = red(v, ell)
    F[1] = f1

    def pois(f, n):
        Pn = 2 - n * dl
        g = np.zeros(M, dtype=np.int64)
        nz = np.nonzero(f)[0]
        for l in nz:
            a = int(f[l])
            d1 = 2 * (l + 1 + Pn)
            assert d1 != 0 and red(d1, ell) != 0, ('divisor', n, l)
            g[l + 1] = (g[l + 1] - a * red(1 / d1, ell)) % ell
            if l != 1:
                d2 = 2 * (l - 1 - Pn)
                assert d2 != 0 and red(d2, ell) != 0, ('divisor', n, l)
                g[l - 1] = (g[l - 1] + a * red(1 / d2, ell)) % ell
        return g

    G[1] = pois(F[1], 1)
    top = {1: L + 1}                                  # highest stored frequency (+1) of g_n / f_n
    for n in range(2, Q + 1):
        acc = np.zeros(M, dtype=np.int64)
        for i in range(1, n):
            j = n - i
            Pi, pj = red(2 - i * dl, ell), red(1 - j * dl, ell)
            ti, tj = B * i + 1, B * j + 1
            b = G[i][:ti]
            a = F[j][:tj]
            ma = (a * idx[:tj]) % ell
            lb = (b * idx[:ti]) % ell
            # sum frequencies l + m: (P_i m - p_j l) b_l a_m / 2
            s = (Pi * (np.convolve(b, ma) % ell) - pj * (np.convolve(lb, a) % ell)) % ell
            k = min(len(s), M)
            acc[:k] = (acc[:k] + s[:k]) % ell
            # difference m - l: (-p_j l - P_i m) b_l a_m / 2, index d = m - l, s = d + (ti - 1)
            c = (-(pj * (np.convolve(a, lb[::-1]) % ell)) - Pi * (np.convolve(ma, b[::-1]) % ell)) % ell
            off = ti - 1
            # d > 0
            pos = c[off + 1:]
            k = min(len(pos), M - 1)
            acc[1:1 + k] = (acc[1:1 + k] + pos[:k]) % ell
            # d < 0: sin(d theta) = -sin(|d| theta)
            neg = c[:off][::-1]                       # d = -1, -2, ...
            k = min(len(neg), M - 1)
            acc[1:1 + k] = (acc[1:1 + k] - neg[:k]) % ell
        lam = (n - 1) * cm1
        coef = red(Fr(1, 2) / lam, ell)
        F[n] = (acc * coef) % ell
        if n < Q:
            G[n] = pois(F[n], n)
    return int(F[Q][2 * h - 3]), F


def main():
    prof = sys.argv[1]
    Qmax = int(sys.argv[2])
    lo, hi = Fr(sys.argv[3]), Fr(sys.argv[4])
    out = open(sys.argv[5], 'a') if len(sys.argv) > 5 else None
    F1 = load_profile(prof)
    cases = []
    for Q in range(5, Qmax + 1):
        for h in range(2, Q):
            if math.gcd(h, Q) == 1 and 2 * h < Q and lo < Fr(2 * h, Q) < hi:
                cases.append((Q, h))
    print('profile %s, %d modes, top frequency %d; %d cases with Q <= %d in (%s, %s)' %
          (prof, len(F1), max(F1), len(cases), Qmax, lo, hi), flush=True)
    t0 = time.time()
    nz = 0
    for Q, h in cases:
        t1 = time.time()
        res = []
        for ell in PRIMES[:2]:
            k, _ = kappa_mod(F1, Q, h, ell)
            res.append((ell, k))
            if k != 0:
                break
        status = 'nonzero' if res[-1][1] != 0 else 'zero mod both primes'
        nz += status == 'nonzero'
        dlt = Fr(2 * h, Q)
        rec = {'profile': prof, 'delta': str(dlt), 'Q': Q, 'h': h, 'first_resonance': Q, 'mode': 2 * h - 3,
               'residues': res, 'status': status, 'seconds': round(time.time() - t1, 2)}
        print(json.dumps(rec), flush=True)
        if out:
            out.write(json.dumps(rec) + '\n'); out.flush()
    print('done: %d of %d nonzero; %.1fs' % (nz, len(cases), time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
