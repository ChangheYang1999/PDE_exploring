"""Size of the stream-to-density feedback term at delta=2/3, f1=sin(theta), from checkpoint midpoints.

The density forcing is S_n = sum_{i+j=n} [ -(D g_i)(p_j + T) f_j + ((P_i + T) g_i)(D f_j) ], T = d/dt, D = d/dtheta,
and (lambda_n - c T) f_n = S_n with lambda_n = (n-1)(c-1).  This script
  (1) checks the conventions by recomputing f_n from the full sum at a few low orders,
  (2) at high orders, computes the single terms i = n-1 (stream g_{n-1} against f_1) and i = 1 (g_1 against f_{n-1}),
      applies the exact inverse of (lambda_n - c T) to each, and compares their plain norms with M_n = ||f_n||_*;
  (3) does the same for the edge terms i = 1, 2, 3, n-3, n-2, n-1 and reports the plain norm of f_n minus their sum
      (the contribution of the middle products) and of f_n minus the two terms with i = 1 and i = n-1.
Midpoints only (80-bit mpmath).  Usage: feedback_term.py CHECKPOINT OUT.json n1 n2 ...
"""
import sys, json, pickle, time
from fractions import Fraction
import mpmath as mp
mp.mp.prec = 80
t0 = time.time()
ck, out = sys.argv[1], sys.argv[2]
orders = [int(x) for x in sys.argv[3:]]
state = pickle.load(open(ck, 'rb'))
assert (state['A'], state['B']) == ('2', '3')
dl = Fraction(2, 3); c = 3
print('loaded', round(time.time() - t0, 1), flush=True)


def val(rec):
    m, e, _ = rec
    return mp.ldexp(mp.mpf(int(m)), int(e))


def field(n, which):
    """dict (q, frequency) -> real sine amplitude."""
    cols = state[which][n]
    d = {}
    for q, col in enumerate(cols):
        for k, rec in enumerate(col):
            v = val(rec)
            if v != 0:
                fr = 2 * k + 1 if which == 'f' else 2 * k
                if fr > 0:
                    d[(q, fr)] = v
    return d


def tshift(h, s):
    """(s + T) h on sine or cosine series (keys (q, freq))."""
    o = {}
    for (q, m), v in h.items():
        o[(q, m)] = o.get((q, m), 0) + s * v
        if q > 0:
            o[(q - 1, m)] = o.get((q - 1, m), 0) + q * v
    return o


def dtheta(h):
    """sine series -> cosine series (keys (q, freq))."""
    return {(q, m): m * v for (q, m), v in h.items()}


def mul_cos_sin(cs, sn):
    """(sum a cos(m th)) * (sum b sin(k th)) -> sine series; cos m sin k = [sin(k+m) + sin(k-m)]/2."""
    o = {}
    for (q1, m), a in cs.items():
        for (q2, k), b in sn.items():
            q = q1 + q2
            o[(q, k + m)] = o.get((q, k + m), 0) + a * b / 2
            d = k - m
            if d > 0:
                o[(q, d)] = o.get((q, d), 0) + a * b / 2
            elif d < 0:
                o[(q, -d)] = o.get((q, -d), 0) - a * b / 2
    return o


def add(a, b, s=1):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, 0) + s * v
    return o


def term(i, j):
    gi, fj = field(i, 'g'), field(j, 'f')
    Pi, pj = 2 - i * dl, 1 - j * dl
    t1 = mul_cos_sin(dtheta(gi), tshift(fj, mp.mpf(pj.numerator) / pj.denominator))
    t2 = mul_cos_sin(dtheta(fj), tshift(gi, mp.mpf(Pi.numerator) / Pi.denominator))
    return add(t2, t1, -1)


def inv_density(S, n):
    """exact inverse of (lambda_n - c T) on polynomials in t: x = sum_h (cT)^h S / lambda^(h+1)."""
    lam = (n - 1) * (c - 1)
    x, cur = {}, {k: v / lam for k, v in S.items()}
    while cur:
        x = add(x, cur)
        nxt = {}
        for (q, m), v in cur.items():
            if q > 0:
                nxt[(q - 1, m)] = nxt.get((q - 1, m), 0) + c * q * v / lam
        cur = nxt
    return x


def norm(h):
    return sum((abs(v) for v in h.values()), mp.mpf(0))


def l10(x):
    return float(mp.log10(x)) if x > 0 else None


res = {}
for n in orders:
    fn = field(n, 'f')
    Mn = norm(fn)
    row = dict(log10M=l10(Mn), log10N_prev=l10(norm(field(n - 1, 'g'))))
    if n <= 12:
        S = {}
        for i in range(1, n):
            S = add(S, term(i, n - i))
        x = inv_density(S, n)
        diff = norm(add(x, fn, -1))
        row['convention_check_rel_diff'] = float(diff / Mn)
    x1 = inv_density(term(n - 1, 1), n)
    xb = inv_density(term(1, n - 1), n)
    row['log10_feedback_g_prev_f1'] = l10(norm(x1))
    row['log10_term_g1_f_prev'] = l10(norm(xb))
    row['log10_ratio_feedback_over_M'] = l10(norm(x1) / Mn)
    # edge terms: i = 1, 2, 3 (low-order stream transporting f_{n-i}) and i = n-1, n-2, n-3 (g_{n-i'} against low f)
    edge = {}
    for i in sorted({1, 2, 3, n - 1, n - 2, n - 3}):
        if 1 <= i <= n - 1:
            xi = inv_density(term(i, n - i), n)
            row['log10_term_i%d_over_M' % (i if i <= 3 else i - n)] = l10(norm(xi) / Mn)
            edge = add(edge, xi)
    row['log10_edge_sum_over_M'] = l10(norm(edge) / Mn)
    row['log10_remainder_over_M'] = l10(norm(add(fn, edge, -1)) / Mn)
    lin = add(xb, x1)
    row['log10_linear_pair_remainder_over_M'] = l10(norm(add(fn, lin, -1)) / Mn)
    res[n] = row
    print(n, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in row.items()},
          round(time.time() - t0, 1), flush=True)
json.dump(dict(checkpoint=ck.split('/')[-1], note='midpoints only', orders=res, elapsed_s=time.time() - t0),
          open(out, 'w'))
print('all done', round(time.time() - t0, 1))
