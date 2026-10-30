"""Independent 2D quadrature check of G0 and rF for a small legqs candidate (lane c1-n3): the residual F is evaluated at exact rational
points from the tuple-key representation (exact rational polynomial part, mpmath for the fractional powers and trig), the angular integral
by the trapezoid rule (exact for trigonometric polynomials with M > 2 nmax points), the radial integral in t by composite Gauss-Legendre on
geometrically graded panels toward t = 1 (r -> infinity) and t = 0. This checks the exact R1 + R2 I0 integration route (legqs_norms) to the
quadrature accuracy (about 10 digits). Usage: legqs_quadcheck.py <out json>"""
from fractions import Fraction as Q
from pathlib import Path
import json, sys, tempfile, time, mpmath
sys.set_int_max_str_digits(0); sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import fmpq
import e2norms as E, legqs_e2norms as LS, legqs_norms as LN
from e2norms import fq
mpmath.mp.dps = 30
gens = [{'m': 2, 'j': 1, 'spec': ['legqs', 0, 2, 4, 25], 'coef': '3/7'}, {'m': 3, 'j': 0, 'spec': ['legqs', 0, 1, 4, 25], 'coef': '-2/5'},
        {'m': 1, 'j': 2, 'spec': ['legqs', 0, 1, 4, 25], 'coef': '5/11'}, {'m': 0, 'j': 0, 'spec': ['legqs', 1, 2, 4, 25], 'coef': '1/3'},
        {'m': 1, 'j': 3, 'spec': ['legqs', 0, 0, 4, 25], 'coef': '7/2'}, {'m': 2, 'j': 3, 'spec': ['legqs', 1, 0, 4, 10], 'coef': '-1/9'}]
f = Path(tempfile.mkdtemp()) / 'g.json'; f.write_text(json.dumps({'cl': str(Q(4076476460239181, 2251799813685248)), 'generators': gens}))
c, A, A_s, _, meta = LS.load_reference_legqs(f); delta = 1 - 1 / c
t0 = time.time()
D, fields = LN.residual_t(A, A_s, c, 0, log=lambda *a: None); F = D[0, 0]
tables = LN.ScaleTables()
rG0 = LN.norm_t(D, 0, delta, Q(0), 0, (), 56, 'G0', tables); rrF = LN.norm_t(D, 0, delta, Q(-1), 1, (), 56, 'rF', tables)
print('norm_t G0', rG0['norm_lower_ball'][:40], 'rF', rrF['norm_lower_ball'][:40], f'{time.time()-t0:.0f}s', flush=True)
def mpq(x): x = Q(x); return mpmath.mpf(x.numerator) / x.denominator
dm = mpq(delta)
keys = [(ell, kind, n, sc, p) for (ell, kind, n, sc), p in F.items()]
nmax = max(n for (ell, kind, n, sc, p) in keys); M = 2 * nmax + 6
def F_at(t, th):
    """F at the point with compactified radius t (rational) and angle th (mpf)."""
    v = 1 - t; r2 = t / v; tot = mpmath.mpf(0)
    for ell, kind, n, sc, p in keys:
        val = Q(str(p(fq(t))))
        for a, N in sc: val /= (1 + a * v) ** N
        trig = mpmath.cos(n * th) if kind == 'c' else mpmath.sin(n * th)
        tot += mpq(v) ** (ell * dm / 2) * mpq(val) * trig
    return mpmath.sqrt(mpq(r2)) * tot
def ang_sum(t, weight):
    s = mpmath.mpf(0); r2 = t / (1 - t)
    for k in range(M):
        th = 2 * mpmath.pi * k / M; Fv = F_at(t, th); s += Fv * Fv
    return s * (2 * mpmath.pi / M) * weight(mpq(r2)) / (2 * mpq(1 - t) ** 2)       # r dr = dt / (2 (1-t)^2)
# Gauss-Legendre nodes (20 points) as exact rationals
import numpy as np
xg, wg = np.polynomial.legendre.leggauss(20)
xg = [Q(str(repr(float(x)))) for x in xg]; wg = [Q(str(repr(float(w)))) for w in wg]
# partition of [0, 1] without overlap (N4-301 found the first version double counting [0, 1/2]):
# [0, 2^-12], [2^-(k+1), 2^-k] for k = 11..1 (covers [2^-12, 1/2]), [1 - 2^-k, 1 - 2^-(k+1)] for k = 1..45 (covers [1/2, 1 - 2^-46]), [1 - 2^-46, 1]
panels = [(Q(0), Q(1, 2 ** 12))]
for k in range(11, 0, -1): panels.append((Q(1, 2 ** (k + 1)), Q(1, 2 ** k)))
for k in range(1, 46): panels.append((1 - Q(1, 2 ** k), 1 - Q(1, 2 ** (k + 1))))
panels.append((1 - Q(1, 2 ** 46), Q(1)))
assert panels[0][0] == 0 and panels[-1][1] == 1 and all(panels[i][1] == panels[i + 1][0] for i in range(len(panels) - 1)), 'partition gap or overlap'
out = {}
for label, weight in (('G0', lambda r2: 1), ('rF', lambda r2: r2)):
    total = mpmath.mpf(0); t1 = time.time()
    for (a, b) in panels:
        h = (b - a) / 2; mid = (a + b) / 2
        for x, w in zip(xg, wg):
            t = mid + h * x
            total += mpq(w) * mpq(h) * ang_sum(t, weight)
    val = mpmath.sqrt(total); rec = rG0 if label == 'G0' else rrF
    print(f"{label}: quadrature {mpmath.nstr(val, 16)} vs norm_t [{rec['norm_lower'][:24]}, {rec['norm_upper'][:24]}] rel diff {mpmath.nstr(abs(val - mpmath.mpf(rec['norm_lower'].strip('[]').split(' +/-')[0][:40]))/val, 3)} ({time.time()-t1:.0f}s)", flush=True)
    out[label] = {'quadrature': mpmath.nstr(val, 20), 'norm_t_lower': rec['norm_lower'], 'norm_t_upper': rec['norm_upper']}
Path(sys.argv[1]).write_text(json.dumps({'candidate': gens, 'panels': len(panels), 'gauss_points': 20, 'angular_points': M, 'results': out}, indent=1) + '\n')
