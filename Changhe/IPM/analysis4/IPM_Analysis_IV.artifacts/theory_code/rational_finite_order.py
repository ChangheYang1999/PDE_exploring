"""Lead: Theorem E constants (finite-order geometric bound below the first resonance at rational delta).

For rational delta with delta/2 = p/q in lowest terms, convergent denominators q_0 = 1, ..., q_K = q, put
  B_rat = sum_{k=0}^{K-1} log(q_{k+1}) / q_k,
  lambda = 3/2 + delta/2 + 1/delta,  K = 2 lambda (B+1)/(c-1)  (B = top frequency + 1),
  A = 8 K exp(2 B_rat) alpha_1 / delta.
Theorem E: alpha_n <= A^n/(8 K n) for 1 <= n < q, and the stationary residual of the order-N truncation (N < q) obeys
  sup_theta r^{-gamma} |res| <= lambda (B+1) A /(64 K^2) * N t^N / (1-t),   t = A r^{-delta} < 1.
Usage: python3 rational_finite_order.py [leading_exact.json]
"""
import sys
import json
import os
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 50


def cf(fr):
    a = []
    p, q = fr.numerator, fr.denominator
    while q:
        a.append(p // q)
        p, q = q, p - (p // q) * q
    return a


def dens(a):
    q = [1, a[1]]
    for k in range(2, len(a)):
        q.append(a[k] * q[-1] + q[-2])
    return q


def constants(delta, alpha1, L):
    a = cf(delta / 2)
    q = dens(a)
    Brat = mp.fsum(mp.log(q[k + 1]) / q[k] for k in range(len(q) - 1))
    d = mp.mpf(delta.numerator) / delta.denominator
    c = 1 / (1 - d)
    lam = mp.mpf(3) / 2 + d / 2 + 1 / d
    K = 2 * lam * (L + 2) / (c - 1)
    A = 8 * K * mp.e ** (2 * Brat) * alpha1 / d
    out = dict(q_last=q[-1], n_cf=len(a), B_rat=Brat, lam=lam, K=K, A=A, log10_R0=mp.log10(A) / d)
    # residual at R = (2A)^(1/delta) (t = 1/2) for N = q - 1
    N = q[-1] - 1
    pref = lam * (L + 2) * A / (64 * K ** 2)
    out['N'] = N
    out['log2_residual_bound_t_half'] = mp.log(pref * 2, 2) + mp.log(N, 2) - N
    return out


def main():
    d007 = Fraction(1824676646553933, 4076476460239181)
    cases = [('sin', d007, mp.mpf(1), 1)]
    if len(sys.argv) > 1:
        dens_ = json.load(open(sys.argv[1]))['density']
        coef = {int(k): Fraction(v) for k, v in dens_.items()}
        a1 = sum(abs(v) for v in coef.values())
        cases.append(('cand007_raw', d007, mp.mpf(a1.numerator) / a1.denominator, max(coef)))
    for dl in (Fraction(4, 9), Fraction(1, 2), Fraction(2, 5), Fraction(9, 20), Fraction(2, 3)):
        cases.append(('sin', dl, mp.mpf(1), 1))
    res = []
    for name, dl, a1, L in cases:
        o = constants(dl, a1, L)
        print(name, dl, {k: (mp.nstr(v, 10) if isinstance(v, mp.mpf) else v) for k, v in o.items()})
        res.append(dict(profile=name, delta=str(dl), **{k: (mp.nstr(v, 15) if isinstance(v, mp.mpf) else v)
                                                        for k, v in o.items()}))
    os.makedirs('logs', exist_ok=True)
    json.dump(res, open('logs/rational_finite_order.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
