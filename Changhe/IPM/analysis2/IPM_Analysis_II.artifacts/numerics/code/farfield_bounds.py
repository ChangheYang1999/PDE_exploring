import os
"""Far-field enclosures (r >= R) of the background fields from the exact sector expansion, with rigorous tails.

Potential: phi = sum_{j<=3} sum_{q>=0} r^{s_{jq}} sum_m C_{m,j,q} cos(2m theta), s_{jq} = 2 p_j - 2q, C_{m,j,q} = sum_k a_{mkj} binom(p_j - k, q), valid for r > 1.
Derivative rules on a term r^sigma T(theta), T = sin(k theta) or cos(k theta) (own derivation; checked numerically against the arb evaluator):
  d_x [r^s sin k]  = r^{s-1} [ (s-k)/2 sin(k+1) + (s+k)/2 sin(k-1) ]
  d_y [r^s sin k]  = r^{s-1} [ (s+k)/2 cos(k-1) - (s-k)/2 cos(k+1) ]
  d_x [r^s cos k]  = r^{s-1} [ (s-k)/2 cos(k+1) + (s+k)/2 cos(k-1) ]
  d_y [r^s cos k]  = r^{s-1} [ (s-k)/2 sin(k+1) - (s+k)/2 sin(k-1) ]
  Lap [r^s cos k]  = (s^2 - k^2) r^{s-2} cos k        (sin(-k) = -sin k, cos(-k) = cos k, sin 0 = 0 folded)
rho = -d_y Lap phi, psi = d_x d_y phi, U = (-psi_y, psi_x), DU = [[-psi_xy, -psi_yy],[psi_xx, psi_xy]].
Each field is sum_{j,q} r^{s_{jq} - d} S_{jq}(theta) with S a trig polynomial (exact rationals -> arb). For r >= R:
  |field| <= sum_{j, q<=Q} r^{s_{jq}-d} sup|S_{jq}| + tail_d(R) r^{s_{j0} - d - 2(Q+1)} ... we return a bound of the form
  B(R) = sum_{j} sum_{q<=Q} R^{(s_{jq}-d) - e} sup|S| + tails, scaled to the leading exponent e (so |field| <= B r^e for r >= R when all exponents <= e).
Tails: |C_{m,j,q}| <= sum_k |a_{mkj}| binom(B_k + q - 1, q), B_k = ceil(|p_j - k|) (since |p-k-i| <= B_k + i), and a d-th order derivative field of
r^s cos(n theta) has sum of |coefficients| <= |C| prod_{i<d} (|s| + n + 2 + 2i)   (each derivative rule multiplies the coefficient sum by at most
|sigma| + k and raises k by at most 1; the Laplacian contributes (|s|+n)^2 <= (|s|+n+2)^2).
sup over theta of a trig polynomial: rigorous by a fine grid plus the Bernstein inequality |T'| <= deg * sup|T|.
"""
import json, math, sys, os
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, ctx, fmpq

def canon(j, m, k): return 215*j + 26*m - m*(m-1)//2 + (k-m)
def binom_fr(p, q):
    out = Fr(1)
    for i in range(q): out = out*(p-i)/(i+1)
    return out
def A(fr): return arb(fmpq(fr.numerator, fr.denominator))

# trig series: dict {('s', k): coef} or {('c', k): coef}, k >= 0 (cos 0 allowed), coefficients Fraction or arb
def tadd(T, kind, k, v):
    if v == 0: return
    if k < 0:
        k = -k
        if kind == 's': v = -v
    if kind == 's' and k == 0: return
    key = (kind, k); T[key] = T.get(key, 0) + v
    if T[key] == 0: del T[key]

def dx(T, s):
    out = {}
    for (kind, k), c in T.items():
        if kind == 's': tadd(out, 's', k+1, c*(s-k)/2); tadd(out, 's', k-1, c*(s+k)/2)
        else: tadd(out, 'c', k+1, c*(s-k)/2); tadd(out, 'c', k-1, c*(s+k)/2)
    return out
def dy(T, s):
    out = {}
    for (kind, k), c in T.items():
        if kind == 's': tadd(out, 'c', k-1, c*(s+k)/2); tadd(out, 'c', k+1, -c*(s-k)/2)
        else: tadd(out, 's', k+1, c*(s-k)/2); tadd(out, 's', k-1, -c*(s+k)/2)
    return out
def lap(T, s):
    return {key: c*(s*s - key[1]*key[1]) for key, c in T.items() if c*(s*s - key[1]*key[1]) != 0}
def scale(T, f): return {k: v*f for k, v in T.items()}

def sector_fields(cl, a, Q):
    """For each (j,q): dict of field -> (exponent, trig dict), fields: rho, rho_x, rho_y, psi, U1, U2, DU11, DU12, DU21, DU22."""
    g = Fr(1)/cl; lam = 1-g; p = [(3+g-j*lam)/2 for j in range(4)]
    out = {}
    for j in range(4):
        for q in range(Q+1):
            s = 2*p[j] - 2*q
            C = {}
            for m in range(10):
                v = sum((a[canon(j, m, k)]*binom_fr(p[j]-k, q) for k in range(m, 26)), Fr(0))
                tadd(C, 'c', 2*m, v)
            fields = {}
            L = lap(C, s)                     # exponent s-2
            rho = scale(dy(L, s-2), -1)       # s-3
            fields['rho'] = (s-3, rho)
            fields['rho_x'] = (s-4, dx(rho, s-3)); fields['rho_y'] = (s-4, dy(rho, s-3))
            psi = dx(dy(C, s), s-1)           # s-2
            fields['psi'] = (s-2, psi)
            psix = dx(psi, s-2); psiy = dy(psi, s-2)      # s-3
            fields['U1'] = (s-3, scale(psiy, -1)); fields['U2'] = (s-3, psix)
            fields['DU11'] = (s-4, scale(dy(psix, s-3), -1)); fields['DU12'] = (s-4, scale(dy(psiy, s-3), -1))
            fields['DU21'] = (s-4, dx(psix, s-3)); fields['DU22'] = (s-4, dx(psiy, s-3))
            out[(j, q)] = fields
    return out, p

def eval_trig(T, theta):
    v = 0.0
    for (kind, k), c in T.items(): v += float(c)*(math.sin(k*theta) if kind == 's' else math.cos(k*theta))
    return v

def sup_trig(T, M=20000):
    """Rigorous upper bound of sup_theta |T| (arb). Float evaluation on M equispaced angles with a proved rounding margin, then the
    Bernstein inequality |T'| <= deg sup|T|:  sup <= (grid max + margin) / (1 - pi deg / M'), M' the exact grid spacing bound.
    Rounding margin (binary64, glibc sin/cos within 1 ulp): for n terms, |float sum - exact| <= (2n + 4) 2^-53 sum_k |c_k| plus the
    error from the float angle (|theta_float - theta| <= 2^-52 theta <= 2^-50): deg * sum|c_k| * 2^-50."""
    if not T: return arb(0)
    deg = max(k for (_, k) in T); n = len(T)
    th = np.linspace(0, 2*math.pi, M, endpoint=False)
    vals = np.zeros(M); csum = 0.0
    for (kind, k), c in T.items():
        cf = float(c); csum += abs(cf)
        vals += cf*(np.sin(k*th) if kind == 's' else np.cos(k*th))
    margin = (2*n + 4)*2.0**-53*csum + deg*csum*2.0**-50 + sum(abs(float(c) - c) if not isinstance(c, arb) else float(c.rad()) for c in T.values())
    gmax = arb(float(np.abs(vals).max())) + arb(margin)
    spacing = 2*arb.pi()/M*(1 + arb(2)**-40)       # float angles are within relative 2^-50 of the exact equispaced grid
    fac = 1 - spacing*deg/2                         # Bernstein: sup <= gridmax + (spacing/2) deg sup
    if not fac > 0: raise ValueError('grid too coarse')
    return gmax/fac

def field_bound(sectors, p, cl, a, name, R, e_target, Q):
    """Upper bound B such that |field| <= B r^{e_target} for all r >= R (requires every sector exponent <= e_target)."""
    R = arb(R); total = arb(0); rows = []
    for (j, q), fields in sectors.items():
        e, T = fields[name]
        if e > e_target: raise ValueError('sector exponent above target')
        sup = sup_trig(T)
        contrib = sup*R**A(e - e_target) if (e - e_target) != 0 else sup
        total += contrib; rows.append(((j, q), float(e), float(sup), float(contrib)))
    # tail q > Q for each j: field of order d from the potential (d = 3 for rho, U; 4 for grad rho, DU; 2 for psi)
    d = {'rho': 3, 'U1': 3, 'U2': 3, 'psi': 2, 'rho_x': 4, 'rho_y': 4, 'DU11': 4, 'DU12': 4, 'DU21': 4, 'DU22': 4}[name]
    tail = arb(0)
    for j in range(4):
        pj = p[j]
        # coefficient bound per m: sum_k |a_mkj| binom(B_k+q-1, q); sum over m with the derivative factor prod_{i<d}(|s|+n+2+2i), n = 2m
        def term(q):
            s = 2*pj - 2*q; tot = arb(0)
            for m in range(10):
                cm = arb(0)
                for k in range(m, 26):
                    ak = a[canon(j, m, k)]
                    if ak == 0: continue
                    Bk = math.ceil(abs(float(pj - k))) + 1
                    cm += abs(A(ak))*math.comb(Bk+q-1, q)
                fac = arb(1); n = 2*m
                for i in range(d): fac *= (abs(A(s)) + n + 2 + 2*i)
                tot += cm*fac
            return tot*R**A(s - d - e_target)
        # sum q = Q+1 .. Q+40 explicitly, then geometric bound with ratio <= rho_q
        acc = arb(0); q = Q+1
        while q <= Q+40: acc += term(q); q += 1
        # ratio bound for q >= Q+41: term(q+1)/term(q) <= (1 + Bmax/(q+1)) * ((|s|+2+... )) ... use crude: ratio <= (1 + 27/(q+1)) * (1 + 2/(2q)) ^ d * R^-2
        qq = Q+41; ratio = (1 + arb(27)/(qq+1))*(1 + arb(2)/(2*qq - 2))**d*R**-2
        if not ratio < 1: raise ValueError('R too small for the geometric tail')
        last = term(qq)
        acc += last/(1 - ratio)
        tail += acc
    return total + tail, rows, float(tail)

if __name__ == '__main__':
    from ipm_arb import State
    d = json.load(open(sys.argv[1])); cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    ctx.prec = 128
    Q = 6
    sectors, p = sector_fields(cl, a, Q)
    S = State(sys.argv[1], prec=192)
    # check the rules at far points against the arb evaluator
    for (x, y) in [(1000.0, 300.0), (50.0, 2000.0), (300.0, 300.0)]:
        r = math.hypot(x, y); th = math.atan2(y, x)
        f = S.fields(x, y, 4)
        ref = {'rho': f['rho'], 'rho_x': f['rho_x'], 'rho_y': f['rho_y'], 'psi': f['psi'], 'U1': f['U1'], 'U2': f['U2'], 'DU11': f['DU'][0][0], 'DU12': f['DU'][0][1], 'DU21': f['DU'][1][0], 'DU22': f['DU'][1][1]}
        print('point (%g,%g):' % (x, y))
        for name in ref:
            val = 0.0
            for (j, q), fields in sectors.items():
                e, T = fields[name]; val += r**float(e)*eval_trig(T, th)
            print('   %6s sectors=%.12e  arb=%s  reldiff=%.1e' % (name, val, ref[name].str(12), abs(val - float(ref[name].mid()))/max(abs(float(ref[name].mid())), 1e-300)))
    # bounds for r >= R
    g = float(1/cl)
    for R in (200, 1000, 10000):
        print('R =', R)
        for name, e in [('rho_x', g-1), ('rho_y', g-1), ('DU11', g-1), ('DU12', g-1), ('DU21', g-1), ('DU22', g-1), ('rho', g), ('U1', g), ('U2', g)]:
            B, rows, tail = field_bound(sectors, p, cl, a, name, R, Fr(e).limit_denominator(10**12) if False else (Fr(1)/cl - 1 if e < g - 0.1 else Fr(1)/cl), Q)
            print('   |%s| <= %.6g r^%.4f for r >= %g (leading sector sup %.5g, tail %.2e)' % (name, float(B), e, R, rows[0][2], tail))

# ---------------- all-arb grid variant (no numpy sine, no float rounding model): env FARFIELD_ARB_GRID=<M> switches sup_trig to it ----------------
_ARB_TABLES = {}
def _arb_tables(M, kmax):
    """sin(k theta_m), cos(k theta_m) as arb for theta_m = 2 pi m / M, 0 <= m < M, 0 <= k <= kmax (cached per M; extended on demand)."""
    S, C = _ARB_TABLES.setdefault(M, ({}, {}))
    if kmax in S: return S, C
    twopi = 2*arb.pi()
    for k in range(kmax + 1):
        if k in S: continue
        S[k] = [(twopi*k*m/M).sin() for m in range(M)]
        C[k] = [(twopi*k*m/M).cos() for m in range(M)]
    return S, C


def _arb_max_upper(balls):
    """exact arb maximum of the upper endpoints of the balls (comparisons of exact arb numbers, no float conversion)."""
    cur = None
    for b in balls:
        u = arb(b.upper())
        if cur is None or u > cur: cur = u
    return cur

def _arb_min_lower(balls):
    cur = None
    for b in balls:
        l = arb(b.lower())
        if cur is None or l < cur: cur = l
    return cur

def _arb_grid_values(T, M):
    deg = max(k for (_, k) in T)
    S, C = _arb_tables(M, deg)
    coefs = [(kind, k, A(c) if not isinstance(c, arb) else c) for (kind, k), c in T.items()]
    vals = []
    for m in range(M):
        v = arb(0)
        for kind, k, c in coefs: v += c*(S[k][m] if kind == 's' else C[k][m])
        vals.append(v)
    return deg, vals

def sup_trig_arb(T, M=None):
    """Rigorous upper bound of sup_theta |T| with every operation in arb: exact (rational or ball) coefficients, arb sin/cos at the exact equispaced
    angles 2 pi m/M, max of the ball upper bounds, then the Bernstein inequality sup <= gridmax / (1 - (spacing/2) deg) with spacing = 2 pi / M in arb.
    No floating-point sine model and no float conversion enter."""
    if not T: return arb(0)
    M = M or int(os.environ.get('FARFIELD_ARB_GRID', '4000'))
    deg, vals = _arb_grid_values(T, M)
    gmax = _arb_max_upper(abs(v) for v in vals)                 # directed arb maximum of the exact upper endpoints (no float key; verifier V223)
    spacing = 2*arb.pi()/M
    fac = 1 - spacing*deg/2
    if not fac > 0: raise ValueError('grid too coarse')
    return gmax/fac

def inf_trig_arb(T, M=None):
    """Rigorous lower bound of inf_theta T (signed), all in arb: grid min of the ball lower bounds minus (spacing/2) deg sup|T|."""
    M = M or int(os.environ.get('FARFIELD_ARB_GRID', '4000'))
    deg, vals = _arb_grid_values(T, M)
    gmin = _arb_min_lower(vals)                                 # directed arb minimum of the exact lower endpoints (V223)
    spacing = 2*arb.pi()/M
    return gmin - spacing/2*deg*sup_trig_arb(T, M)

if os.environ.get('FARFIELD_ARB_GRID'):
    sup_trig_numpy = sup_trig
    sup_trig = sup_trig_arb
