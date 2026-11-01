"""Explicit constants of Theorem A (lead).

Brjuno sum B(alpha) = sum_{k>=0} log(q_{k+1}) / q_k for alpha = delta/2, where q_k are the denominators of the
convergents (q_0 = 1). Constants of Theorem A (finite sine polynomial f_1 with top frequency L, B = L + 1):
  lambda_delta = 3/2 + delta/2 + 1/delta
  K = 2 lambda_delta (B + 1) / (c - 1)
  A = 8 K exp(2 B(alpha)) alpha_1 / delta,      alpha_1 = ||f_1||_{l1}
  alpha_n <= A^n / (8 K n),   convergence for r > R0 = A^(1/delta).
Analytic version (f_1 in A_sigma0): K' = 2 e^{sigma0} (1 + sigma0) lambda_delta / (c - 1), A' = 8 K' e^{2B} ||f_1||_{sigma0}/delta,
  ||f_n||_sigma <= A'^n / (8 K' n (sigma0 - sigma)^(n-1)).

The Brjuno sum is evaluated from exact integer convergents; for a quadratic irrational the tail after k terms is bounded
by a geometric series (q_{k+2} >= 2 q_k gives q_k >= 2^{(k-1)/2}; we bound the tail by sum_{k>k0} (log q_{k+1})/q_k with
q_{k+1} <= (a_max + 1) q_k, and q_k growing at least like the Fibonacci numbers).
"""
import sys
import json
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 60


def cf_of_quadratic(alpha, kmax=80):
    a = []
    x = alpha
    for _ in range(kmax):
        ai = int(mp.floor(x))
        a.append(ai)
        fr = x - ai
        x = 1 / fr
    return a


def cf_frac(fr):
    a = []
    p, q = fr.numerator, fr.denominator
    while q:
        a.append(p // q)
        p, q = q, p - (p // q) * q
    return a


def denominators(a):
    """a = [a0; a1, a2, ...]; returns q_0 = 1, q_1 = a1, q_{k+1} = a_{k+1} q_k + q_{k-1}."""
    q = [1, a[1]]
    for k in range(2, len(a)):
        q.append(a[k] * q[-1] + q[-2])
    return q


def brjuno_sum(q, kmax=None):
    s = mp.mpf(0)
    for k in range(len(q) - 1 if kmax is None else kmax):
        s += mp.log(q[k + 1]) / q[k]
    return s


def tail_bound(q, k0, amax):
    """Upper bound for sum_{k>=k0} log(q_{k+1})/q_k when all partial quotients a_k <= amax and q_k grows at least
    like Fibonacci: q_{k0+m} >= F_m q_{k0} ... we use q_{k+2} >= 2 q_k, and log(q_{k+1}) <= log(amax+1) + log(q_k)."""
    s = mp.mpf(0)
    qk = mp.mpf(q[k0])
    for m in range(0, 400):
        qm = qk * mp.mpf(2) ** (m // 2)
        s += (mp.log(amax + 1) + mp.log(qm)) / qm
    return s


def theorem_constants(delta, c, alpha1, L, Bsum):
    lam = mp.mpf(3) / 2 + delta / 2 + 1 / delta
    K = 2 * lam * (L + 2) / (c - 1)
    A = 8 * K * mp.e ** (2 * Bsum) * alpha1 / delta
    R0 = A ** (1 / delta)
    return dict(lambda_delta=lam, K=K, A=A, log10_R0=mp.log10(R0))


def main():
    out = {}
    # delta = 1/sqrt5
    d = 1 / mp.sqrt(5)
    c = 1 / (1 - d)
    a = cf_of_quadratic(d / 2, 60)
    q = denominators(a)
    k0 = 25
    B_head = brjuno_sum(q, k0)
    B_tail = tail_bound(q, k0, max(a[1:]))
    Bup = B_head + B_tail
    print('delta = 1/sqrt5: alpha cf', a[:12], 'q', q[:10])
    print('  B(alpha) head(25) =', mp.nstr(B_head, 15), ' tail bound =', mp.nstr(B_tail, 5), ' upper =', mp.nstr(Bup, 15))
    out['delta_inv_sqrt5'] = dict(cf=a[:12], q=q[:10], B_head=str(mp.nstr(B_head, 15)), B_upper=str(mp.nstr(Bup, 15)))
    for name, alpha1, L in [('sin', mp.mpf(1), 1), ('sin+sin3/2', mp.mpf(3) / 2, 3)]:
        t = theorem_constants(d, c, alpha1, L, Bup)
        print('  f1 =', name, {k: mp.nstr(v, 6) for k, v in t.items()})
        out['delta_inv_sqrt5'][name] = {k: str(mp.nstr(v, 8)) for k, v in t.items()}
    # Candidate 007 profile (unnormalized and normalized) at delta = 1/sqrt5
    f1 = json.load(open(sys.argv[1]))['f1_sine_coefficients_exact'] if len(sys.argv) > 1 else None
    if f1:
        coef = [Fraction(s) for s in f1]
        alpha1 = mp.mpf(sum(abs(x) for x in coef).numerator) / sum(abs(x) for x in coef).denominator
        L = 2 * len(coef) - 1
        t = theorem_constants(d, c, alpha1, L, Bup)
        print('  f1 = Candidate 007 profile (alpha_1 = %s, L = %d):' % (mp.nstr(alpha1, 8), L),
              {k: mp.nstr(v, 6) for k, v in t.items()})
        out['delta_inv_sqrt5']['cand007_f1'] = {k: str(mp.nstr(v, 8)) for k, v in t.items()}
        out['delta_inv_sqrt5']['cand007_f1']['alpha1'] = str(mp.nstr(alpha1, 12))
    # Candidate 007 rational delta: partial Brjuno sum over the convergents (finite cf)
    N = 4076476460239181
    D = 2 ** 51
    dl = 1 - Fraction(D, N)
    a7 = cf_frac(dl / 2)
    q7 = denominators(a7)
    print('007 rational delta/2 cf', a7)
    partial = [mp.nstr(brjuno_sum(q7, k), 8) for k in range(1, len(q7))]
    print('  partial Brjuno sums', partial)
    out['cand007_rational'] = dict(cf=a7, q=[str(x) for x in q7], partial_B=[str(x) for x in partial])
    json.dump(out, open('constants_out.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
