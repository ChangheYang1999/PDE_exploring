"""Where the plain stream sum N_n = ||G_n||_* gains on the density sum M_n = ||F_n||_* at delta=2/3, f1=sin(theta).

For each order n, stream frequency 2j (list index j) and log column q, the plain mass |g_{n,q,j}| is grouped by the
smallest Poisson shift of that frequency, s_j = min(|P_n+2j|, |P_n-2j|) (P_n = 2-2n/3), and by q.
Density masses are grouped by the distance of the frequency 2k+1 to |P_n|.  Midpoints of the checkpoint balls only.
Usage: stream_ratio_modes.py CHECKPOINT OUT.json n1 n2 ...
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
print('loaded', round(time.time() - t0, 1), flush=True)


def val(rec):
    m, e, _ = rec
    return mp.ldexp(abs(mp.mpf(int(m))), int(e))


def l10(x):
    return float(mp.log10(x)) if x > 0 else None


res = {}
for n in orders:
    P = Fraction(2) - Fraction(2 * n, 3)
    G, F = state['g'][n], state['f'][n]
    # stream: by shift class and column
    shift_mass, col_mass, tot = {}, {}, mp.mpf(0)
    near_col = {}
    for q, col in enumerate(G):
        for j, rec in enumerate(col):
            if j == 0:
                continue
            v = val(rec)
            if v == 0:
                continue
            s = min(abs(P + 2 * j), abs(P - 2 * j))
            key = str(s) if s <= 4 else 'far'
            shift_mass[key] = shift_mass.get(key, 0) + v
            col_mass[q] = col_mass.get(q, 0) + v
            if s <= Fraction(2, 3):
                near_col[q] = near_col.get(q, 0) + v
            tot += v
    Mtot, Fcol, Fnear = mp.mpf(0), {}, mp.mpf(0)
    for q, col in enumerate(F):
        for k, rec in enumerate(col):
            v = val(rec)
            if v == 0:
                continue
            Mtot += v
            Fcol[q] = Fcol.get(q, 0) + v
            if abs(abs(P) - (2 * k + 1)) <= Fraction(4, 3):
                Fnear += v
    qmaxG = max(col_mass, key=lambda q: col_mass[q])
    res[n] = dict(log10N=l10(tot), log10M=l10(Mtot), log10ratio=l10(tot / Mtot),
                  stream_share_by_shift={k: float(v / tot) for k, v in sorted(shift_mass.items())},
                  stream_col_argmax=qmaxG, stream_col0_share=float(col_mass.get(0, 0) / tot),
                  stream_near_by_col_log10={q: l10(v) for q, v in sorted(near_col.items())},
                  stream_log10_col={q: l10(v) for q, v in sorted(col_mass.items())},
                  density_log10_col={q: l10(v) for q, v in sorted(Fcol.items())},
                  density_near_share=float(Fnear / Mtot))
    r = res[n]
    print(n, 'log10 N/M %.3f' % r['log10ratio'], 'argmax q', qmaxG, 'col0 share %.3f' % r['stream_col0_share'],
          'shares', {k: round(v, 4) for k, v in r['stream_share_by_shift'].items()}, flush=True)
json.dump(dict(checkpoint=ck.split('/')[-1], note='midpoints only', orders=res, elapsed_s=time.time() - t0),
          open(out, 'w'))
print('all done', round(time.time() - t0, 1))
