"""Real-line exponential-type norms of the canonical log coefficients at delta=2/3, f1=sin(theta).

For a coefficient H(t,theta)=sum_q t^q sum_j a_{q,j} sin(m_j theta) define
    V_H(t) = sum_j |sum_q a_{q,j} t^q|          (sine-amplitude l1 norm at fixed t = log r)
    N_eta(H) = sup_{t real} exp(-eta |t|) V_H(t).
V_H is evaluated in ball arithmetic (the checkpoint radii are carried) on the grid t = k*h, |t| <= TMAX.
The grid maximum is a lower estimate of the supremum; a point counts as resolved if its ball excludes
values below half its midpoint.  For comparison the column bound U_H(t) = sum_q ||[t^q]H||_l1 |t|^q is
also recorded; V_H <= U_H, and exp(-eta|t|) U_H(t) is maximal near the factorial norm with sigma = 1/eta.
Usage: exptype_norm.py CHECKPOINT OUT.json n1 n2 ...
"""
import sys, json, pickle, time, math
from flint import arb, arb_poly, fmpz, ctx

ctx.prec = 1024
H_STEP, TMAX = 0.25, 640.0
ck, out = sys.argv[1], sys.argv[2]
orders = [int(x) for x in sys.argv[3:]]
t0 = time.time()
state = pickle.load(open(ck, 'rb'))
assert (state['A'], state['B']) == ('2', '3')
two = arb(2)


def ball(rec):
    m, e, r = rec
    if m == '0' and r == '0':
        return arb(0)
    M, E = r.split('*2^') if '*2^' in r else (r, '0')
    x = arb(fmpz(int(m))) * two ** int(e)
    rad = arb(fmpz(int(M))) * two ** int(E)
    return arb(x.mid(), rad.mid())


def log10a(x):
    """log10 of the upper end of |x| (float), or None for zero."""
    u = abs(x).upper()
    if u == 0:
        return None
    return float((arb(u).log() / arb(10).log()).mid())


grid = [k * H_STEP for k in range(-int(TMAX / H_STEP), int(TMAX / H_STEP) + 1)]
res = {}
for n in orders:
    row = {}
    for field in ('f', 'g'):
        cols = state[field][n]
        K = len(cols) - 1
        nmodes = max(len(c) for c in cols)
        polys = []
        for j in range(nmodes):
            coeffs = [ball(cols[q][j]) if j < len(cols[q]) else arb(0) for q in range(K + 1)]
            polys.append(arb_poly(coeffs))
        colnorm = [sum((abs(ball(z)) for z in cols[q]), arb(0)) for q in range(K + 1)]
        U = arb_poly(colnorm)
        Vlog, Ulog, unresolved = [], [], 0
        for t in grid:
            ta = arb(t)
            v = sum((abs(p(ta)) for p in polys), arb(0))
            lo, mid = v.lower(), v.mid()
            if not (lo > mid / 2):
                unresolved += 1
            Vlog.append(float((arb(v.upper()).log() / arb(10).log()).mid()) if v.upper() > 0 else None)
            ua = U(arb(abs(t)))
            Ulog.append(float((arb(ua.mid()).log() / arb(10).log()).mid()))
        row[field] = dict(degree=K, modes=nmodes, unresolved_points=unresolved,
                          log10V=Vlog, log10U=Ulog)
    res[n] = row
    print(n, 'done', round(time.time() - t0, 1), 'unresolved', row['f']['unresolved_points'],
          row['g']['unresolved_points'], flush=True)
json.dump(dict(checkpoint=ck.split('/')[-1], grid_step=H_STEP, tmax=TMAX, prec=1024,
               note='ball evaluation of checkpoint balls on a grid; grid maxima are lower estimates of sup',
               orders=res, elapsed_s=time.time() - t0), open(out, 'w'))
print('all done', time.time() - t0)
