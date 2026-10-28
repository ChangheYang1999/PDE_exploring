"""Third computation for verification topic 96 (independent full-plane bounds for the exact original state 131:
B1 = I - sym Du + A >= (972875/1000000) I, B2 >= (293619/500000) I, B3 >= -(307719/250000) I and
||sym Du||_op <= 101349/125000, with A = [[rho_y, -rho_x/2], [-rho_x/2, 0]],
Bk = (1 + c + V.D log omega) I - k sym DV + A, V = cX + u, omega = (1 + 4 r^2)^(2/5)).

Written from the statement of topic 96 only; no verifier code is imported. Routes:

1. Exact (sympy, Fraction): the closed forms of B1, B2, B3, ||sym Du||^2, rho_y and rho_x in terms of
   chi22 = chi_xxyy, chi04, chi31, chi13 and e = u.X/r^2, derived from the definitions for a generic potential;
   e = -d_theta chi_xy / r^2; r^2/(1 + 4 r^2) = t/(1 + 3t); the eigenvalue lemma (the identity (a - L)(b - L) = C^2
   at L = (a + b - ((a - b)^2 + 4 C^2)^(1/2))/2 with a - L >= 0, and exact tests of min(a, b) - C as a lower bound
   for perturbed matrices); the four targets against the thresholds 9/10, 1/2, -5/4, 17/20 and the compact-region
   numbers 0.972874, 0.587237, -1.230877, 0.810792.
2. The records (read only): for each of the four certificates, status COMPLETE with no failed or pending cell, the
   stated target, the leaf count (99, 144, 164, 49), every rectangle recomputed from its path, the paths forming a
   complete binary tree of [0, 1] x [-1, 1] (prefix-free, the two children of every internal node split the same
   variable, total area 2), every directed lower bound after the target positive (arb balls), the reported worst
   value equal to the smallest leaf value; the recheck companion: all pass at 448 bits, the same paths, every row
   passing with a positive lower bound, and the hashes binding it to the primary record and the polynomial record,
   which in turn records the hash of the exact source record.
3. FLOAT: the 20 branch polynomials (field = sum_j w^(j+1) p_(l,j)(t, z), with the factor (1 - z^2)^(1/2) for the
   odd-odd chi31, chi13; t = r^2/(1 + r^2), z = cos 2 theta, w = (1 - t)^(delta/2)) agree with mpmath numerical
   derivatives (50 digits) of the exact original potential at sample points; the four quantities at the points of a
   grid of the compactified quadrant (from the polynomials, Arb balls at each point; a sample, not a cover), whose
   extremes lie on the correct side of the targets.

Usage: python3 check_p96.py VERIFIER_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib, math, random
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import mpmath
from flint import arb, arb_poly, fmpq, ctx
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
t00 = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
chk, out = {}, {'inputs': {}}
rng = random.Random(96)
V96 = ROOT / '96_original_auxiliary_recomputation/verification'

ps = ROOT / 'source_audit/state131_exact.json'
src = json.loads(ps.read_text()); out['inputs']['source_audit/state131_exact.json'] = sha(ps)
cl = Q(src['exact_parameters']['cl']); a0 = Q(src['exact_parameters']['a0'])
coef = [(tuple(t), Q(v)) for t, v in zip(src['canonical_order'], src['canonical_coefficients'])]
chk['input: 860 canonical coefficients, c = 4076476460239181/2^51'] = len(coef) == 860 and cl == Q(4076476460239181, 2 ** 51)

# 1. exact
x, y = sp.symbols('x y', real=True)
cS = sp.Symbol('c', positive=True)
chi = sp.Function('chi')(x, y)
u = sp.Matrix([-chi.diff(x, y, y), chi.diff(x, x, y)])
Du = u.jacobian([x, y]); sDu = (Du + Du.T) / 2
rho = -sp.diff(chi.diff(x, 2) + chi.diff(y, 2), y)
A = sp.Matrix([[rho.diff(y), -rho.diff(x) / 2], [-rho.diff(x) / 2, 0]])
X = sp.Matrix([x, y]); V = cS * X + u
r2 = x ** 2 + y ** 2
lw = sp.log(1 + 4 * r2) * sp.Rational(2, 5)
VD = sp.expand((V.T * sp.Matrix([lw.diff(x), lw.diff(y)]))[0])
DV = V.jacobian([x, y]); sDV = (DV + DV.T) / 2
c22, c04, c31, c13, ee, tt = sp.symbols('chi22 chi04 chi31 chi13 e t')
rep = {chi.diff(x, 2, y, 2): c22, chi.diff(y, 4): c04, chi.diff(x, 3, y): c31, chi.diff(x, y, 3): c13}
sub = lambda M: M.subs(rep)
uX = (u.T * X)[0]
chk['96: u.X = -d_theta chi_xy (d_theta = x d_y - y d_x), so e = u.X/r^2 = -d_theta chi_xy / r^2'] = \
    sp.simplify(uX + (x * chi.diff(x, y).diff(y) - y * chi.diff(x, y).diff(x))) == 0
tr = r2 / (1 + r2)
scal = sp.Rational(16, 5) * tr * (cS + uX / r2) / (1 + 3 * tr)
chk['96: V.D log omega = (16/5) r^2 (c + e)/(1 + 4 r^2) = (16/5) t (c + e)/(1 + 3t), t = r^2/(1 + r^2)'] = \
    sp.simplify(VD - scal) == 0 and sp.simplify(r2 / (1 + 4 * r2) - tr / (1 + 3 * tr)) == 0
B1 = sub(sp.eye(2) - sDu + A)
chk['96: B1 = I - sym Du + A = [[1 - chi04, chi13], [chi13, 1 - chi22]]'] = \
    sp.simplify(B1 - sp.Matrix([[1 - c04, c13], [c13, 1 - c22]])) == sp.zeros(2)
okB = True
for k, (d11, d12, d22) in ((2, (c22 - c04, (-c31 + 3 * c13) / 2, -2 * c22)), (3, (2 * c22 - c04, -c31 + 2 * c13, -3 * c22))):
    Bk = sub((1 + cS + VD) * sp.eye(2) - k * sDV + A)
    stated = (1 - (k - 1) * cS + scal) * sp.eye(2) + sp.Matrix([[d11, d12], [d12, d22]])
    okB = okB and sp.simplify(sub(Bk - stated)) == sp.zeros(2)
chk['96: B2 = [1 - c + (16/5) t (c + e)/(1 + 3t)] I + [[chi22 - chi04, (-chi31 + 3 chi13)/2], [., -2 chi22]], '
    'B3 = [1 - 2c + ...] I + [[2 chi22 - chi04, -chi31 + 2 chi13], [., -3 chi22]]'] = okB
sD = sub(sDu)
chk['96: sym Du = [[-chi22, (chi31 - chi13)/2], [., chi22]], trace 0, ||sym Du||^2 = chi22^2 + (chi31 - chi13)^2/4; '
    'rho_y = -chi22 - chi04, rho_x = -chi31 - chi13'] = \
    sp.simplify(sD - sp.Matrix([[-c22, (c31 - c13) / 2], [(c31 - c13) / 2, c22]])) == sp.zeros(2) and \
    sp.simplify(-sD.det() - (c22 ** 2 + (c31 - c13) ** 2 / 4)) == 0 and \
    sp.simplify(sub(rho.diff(y)) + c22 + c04) == 0 and sp.simplify(sub(rho.diff(x)) + c31 + c13) == 0
a_, b_, C_ = sp.symbols('a b C', real=True)
s_ = sp.sqrt((a_ - b_) ** 2 + 4 * C_ ** 2); L_ = (a_ + b_ - s_) / 2
okl = True
for _ in range(2000):
    a, b, C = (Q(rng.randint(-500, 500), rng.randint(1, 60)) for _ in range(3)); C = abs(C)
    a2, b2 = a + Q(rng.randint(0, 50), rng.randint(1, 20)), b + Q(rng.randint(0, 50), rng.randint(1, 20))
    q = C * Q(rng.randint(-100, 100), 100)
    L1 = min(a, b) - C
    okl = okl and a2 - L1 >= 0 and b2 - L1 >= 0 and (a2 - L1) * (b2 - L1) - q * q >= 0
chk['96 lemma: (a - L)(b - L) = C^2 and a - L = (a - b + s)/2 >= 0 at L = (a + b - s)/2, s = ((a - b)^2 + 4C^2)^(1/2); '
    'min(a, b) - C is a lower bound for [[a\', q], [q, b\']], a\' >= a, b\' >= b, |q| <= C (2000 exact tests)'] = \
    sp.expand((a_ - L_) * (b_ - L_) - C_ ** 2) == 0 and sp.simplify(a_ - L_ - (a_ - b_ + s_) / 2) == 0 and okl
T = {'B1': Q(972875, 1000000), 'B2': Q(293619, 500000), 'B3': -Q(307719, 250000), 'symDU': Q(101349, 125000)}
chk['96: targets imply the thresholds: 972875/10^6 >= 9/10, 293619/500000 >= 1/2, -307719/250000 >= -5/4, 101349/125000 < 17/20'] = \
    T['B1'] >= Q(9, 10) and T['B2'] >= Q(1, 2) and T['B3'] >= Q(-5, 4) and T['symDU'] < Q(17, 20)
chk['96: targets imply the compact-region numbers 0.972874, 0.587237, -1.230877 (lower) and 0.810792 (upper)'] = \
    T['B1'] >= Q('0.972874') and T['B2'] >= Q('0.587237') and T['B3'] >= Q('-1.230877') and T['symDU'] <= Q('0.810792')

# 2. the records
pp = V96 / 'polynomials.json'
poly = json.loads(pp.read_text()); out['inputs']['96/polynomials.json'] = sha(pp)
chk['records: the polynomial record carries the hash of the exact source record and c'] = \
    poly['source_sha256'] == sha(ps) and Q(poly['cl']) == cl and Q(poly['delta']) == 1 - 1 / cl
LEAVES = {'B1': 99, 'B2': 144, 'B3': 164, 'symDU': 49}


def rect(path):
    t0, t1, z0, z1 = Q(0), Q(1), Q(-1), Q(1)
    for ch in path:
        if ch in 'tT':
            m = (t0 + t1) / 2; t0, t1 = (t0, m) if ch == 't' else (m, t1)
        else:
            m = (z0 + z1) / 2; z0, z1 = (z0, m) if ch == 'z' else (m, z1)
    return t0, t1, z0, z1


def complete_tree(paths):
    ps_ = set(paths)
    if len(ps_) != len(paths):
        return False
    pref = {p[:i] for p in paths for i in range(len(p))}
    if ps_ & pref:
        return False
    for p in pref:
        kids = {q[len(p)] for q in paths if len(q) > len(p) and q.startswith(p)}
        if kids not in ({'t', 'T'}, {'z', 'Z'}):
            return False
    return True


rows = {}
for kind, nl in LEAVES.items():
    pr = V96 / f'{kind}_global.json'; pc = V96 / f'{kind}_global.recheck.json'
    d = json.loads(pr.read_text()); r = json.loads(pc.read_text())
    out['inputs'][f'96/{kind}_global.json'] = sha(pr); out['inputs'][f'96/{kind}_global.recheck.json'] = sha(pc)
    acc = d['accepted']; paths = [a['path'] for a in acc]
    okr = all(rect(a['path']) == (Q(a['t'][0]), Q(a['t'][1]), Q(a['z'][0]), Q(a['z'][1])) for a in acc)
    area = sum((Q(a['t'][1]) - Q(a['t'][0])) * (Q(a['z'][1]) - Q(a['z'][0])) for a in acc)
    lows = [arb(a['lower_numerator_after_target']) for a in acc]
    worst = arb(d['worst'])
    imin = min(range(len(lows)), key=lambda i: float(lows[i].mid()))
    chk[f'records {kind}: COMPLETE, no failed or pending cell, target {T[kind]}, root t in [0, 1], {nl} leaves'] = \
        d['status'] == 'COMPLETE' and d['failed'] == [] and d['pending_paths'] == [] and Q(d['target']) == T[kind] and \
        d['root_t'] == ['0', '1'] and len(acc) == nl and d['kind'] == kind
    chk[f'records {kind}: rectangles equal their paths; complete binary tree of [0, 1] x [-1, 1]; total area 2'] = \
        okr and complete_tree(paths) and area == 2
    chk[f'records {kind}: every directed lower bound after the target is positive; worst = smallest leaf'] = \
        all(v > 0 for v in lows) and worst > 0 and lows[imin].overlaps(worst)
    rr = r['direct_restriction_rows']
    chk[f'records {kind}: recheck all pass at 448 bits, same {nl} paths, every row positive; hashes bind primary and polynomials'] = \
        r['all_pass'] is True and r['precision_bits'] == 448 and r['leaves'] == nl and sorted(x_['path'] for x_ in rr) == sorted(paths) and \
        all(x_['pass'] is True and arb(x_['lower']) > 0 for x_ in rr) and r['primary_sha256'] == sha(pr) and \
        r['polynomials_sha256'] == sha(pp) == d['source_sha256'] and Q(r['target']) == T[kind]
    rows[kind] = {'leaves': nl, 'worst_lower_after_target': str(worst), 'worst_path': acc[imin]['path'], 'precision_bits': d['precision_bits']}
out['records'] = rows

# 3. FLOAT: polynomials against the original potential, then a grid
delta = 1 - 1 / cl
P = {key: {(int(i), int(k)): Q(v) for i, k, v in val} for key, val in poly['polynomials'].items()}
FIELDS = ['chi22', 'chi04', 'chi31', 'chi13', 'e']
ODD = {'chi31', 'chi13'}
mpmath.mp.dps = 50
md = mpmath.mpf(delta.numerator) / delta.denominator


def field_mp(l, t, z):
    w = (1 - t) ** (md / 2); tot = mpmath.mpf(0)
    for j in range(4):
        pj = P[f'{l}_{j}']
        tot += w ** (j + 1) * mpmath.fsum(mpmath.mpf(v.numerator) / v.denominator * t ** i * z ** k for (i, k), v in pj.items())
    return tot * (mpmath.sqrt(1 - z * z) if l in ODD else 1)


mc = mpmath.mpf(cl.numerator) / cl.denominator; mg = 1 / mc
groups = {}
for (j, m, k), a in coef:
    if a != 0:
        groups.setdefault((j, m), []).append((k - m, mpmath.mpf(a.numerator) / a.denominator))
gl = []
for (j, m), terms in groups.items():
    deg = max(l for l, _ in terms); cf = [mpmath.mpf(0)] * (deg + 1)
    for l, a in terms:
        cf[l] += a
    gl.append(((3 + mg - j * (1 - mg)) / 2 - m, m, cf[::-1]))


def chi_f(xv, yv):
    qv = xv * xv + yv * yv; oq = 1 + qv; v = qv / oq
    zz = mpmath.mpc(xv, yv); tot = mpmath.mpf(0)
    for e_, m, cf in gl:
        tot += (zz ** (2 * m)).real * oq ** e_ * mpmath.polyval(cf, v)
    return tot


hd = mpmath.mpf(10) ** -12
worst_rel = mpmath.mpf(0); ns = 0
for rv in ('0.05', '0.3', '1', '2.5', '7', '40', '300'):
    for th in (0.2, 0.7, 1.1, 1.45):
        r_ = mpmath.mpf(rv); xv, yv = r_ * mpmath.cos(th), r_ * mpmath.sin(th)
        t = r_ * r_ / (1 + r_ * r_); z = mpmath.cos(2 * th)
        num = {'chi22': mpmath.diff(chi_f, (xv, yv), (2, 2), h=hd), 'chi04': mpmath.diff(chi_f, (xv, yv), (0, 4), h=hd),
               'chi31': mpmath.diff(chi_f, (xv, yv), (3, 1), h=hd), 'chi13': mpmath.diff(chi_f, (xv, yv), (1, 3), h=hd)}
        num['e'] = (-xv * mpmath.diff(chi_f, (xv, yv), (1, 2), h=hd) + yv * mpmath.diff(chi_f, (xv, yv), (2, 1), h=hd)) / (r_ * r_)
        scale = max(abs(v) for v in num.values())
        for l in FIELDS:
            worst_rel = max(worst_rel, abs(field_mp(l, t, z) - num[l]) / scale)
        ns += 1
chk[f'96 FLOAT: the 20 branch polynomials reproduce chi22, chi04, chi31, chi13, e from numerical derivatives of the '
    f'original potential at {ns} points (r = 0.05 to 300), relative difference < 1e-15'] = worst_rel < 1e-15
out['poly_vs_potential_max_rel_FLOAT'] = float(worst_rel)
# grid of the compactified quadrant: the polynomials in Arb ball arithmetic (200 bits) at each grid point
ctx.prec = 200
AP = {}
for key, pj in P.items():
    nt = max(i for i, _ in pj) + 1; nz = max(k for _, k in pj) + 1
    cols = [[fmpq(0)] * nt for _ in range(nz)]
    for (i, k), v in pj.items():
        cols[k][i] = fmpq(v.numerator, v.denominator)
    AP[key] = [arb_poly([arb(c_) for c_ in col]) for col in cols]
ad = arb(fmpq(delta.numerator, delta.denominator)); acl = arb(fmpq(cl.numerator, cl.denominator))


def fields_arb(t, z):
    w = (1 - t) ** (ad / 2) if t != 1 else arb(0)
    s2 = (1 - z * z).sqrt() if z * z != 1 else arb(0)
    F = {}
    for l in FIELDS:
        tot = arb(0)
        for j in range(4):
            zk = arb(1); acc = arb(0)
            for pk in AP[f'{l}_{j}']:
                acc += pk(t) * zk; zk *= z
            tot += w ** (j + 1) * acc
        F[l] = tot * s2 if l in ODD else tot
    return F


def lmin(a, b, q):
    return (a + b - ((a - b) ** 2 + 4 * q * q).sqrt()) / 2


tg = [fmpq(i, 50) for i in range(46)] + [1 - fmpq(1, 10 ** e) for e in (2, 3, 4, 6, 8, 12)] + [fmpq(1)]
tg = sorted(set(tg + [fmpq(i, 1000) for i in range(905, 1000, 5)]))
zg = [fmpq(k, 20) - 1 for k in range(41)]
ext = {'B1': None, 'B2': None, 'B3': None, 'symDU': None}; at = {}
for tq in tg:
    for zq in zg:
        t, z = arb(tq), arb(zq)
        F = fields_arb(t, z)
        sc = arb(16) / 5 * t * (acl + F['e']) / (1 + 3 * t)
        vals = {'B1': lmin(1 - F['chi04'], 1 - F['chi22'], F['chi13']),
                'B2': lmin(1 - acl + sc + F['chi22'] - F['chi04'], 1 - acl + sc - 2 * F['chi22'], (-F['chi31'] + 3 * F['chi13']) / 2),
                'B3': lmin(1 - 2 * acl + sc + 2 * F['chi22'] - F['chi04'], 1 - 2 * acl + sc - 3 * F['chi22'], -F['chi31'] + 2 * F['chi13']),
                'symDU': (F['chi22'] ** 2 + (F['chi31'] - F['chi13']) ** 2 / 4).sqrt()}
        for k_, v in vals.items():
            lo = float(v.lower()) if k_ != 'symDU' else float(v.upper())
            if ext[k_] is None or (lo < ext[k_] if k_ != 'symDU' else lo > ext[k_]):
                ext[k_] = lo; at[k_] = (float(tq), float(zq), float(v.rad()))
npts = len(tg) * len(zg)
chk[f'96 sampled (Arb balls at {npts} grid points of [0, 1] x [-1, 1], t up to 1 - 1e-12 and t = 1): the smallest lower '
    'ends of lambda_min(B1), lambda_min(B2), lambda_min(B3) exceed the targets and the largest upper end of '
    '||sym Du|| is below its target'] = \
    all(ext[k_] > float(T[k_]) for k_ in ('B1', 'B2', 'B3')) and ext['symDU'] < float(T['symDU'])
out['grid_sampled'] = {'extreme': ext, 'at_t_z_radius': at, 'points': npts,
                       'margin_over_target_display': {k_: (ext[k_] - float(T[k_])) * (1 if k_ != 'symDU' else -1) for k_ in ext}}
out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t00, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
