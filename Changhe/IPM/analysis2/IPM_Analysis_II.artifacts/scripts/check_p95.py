"""Third computation for verification topic 95 (the exact algebraic refit d2: the three matrix bounds
M = (2c + 1) I + sym Du + A >= (19/5) I, M1 = (1 + c + V.D log omega1) I - sym DV + A >= I/2 and
M2 = (1 + c + V.D log omega2) I - 2 sym DV + A >= I/2 at every point of the plane, A = [[rho_y, -rho_x/2], [-rho_x/2, 0]],
rho = -d_y Delta chi, u = (-chi_xyy, chi_xxy), V = cX + u, omega1 = (1 + r^2)^(-1/10), omega2 = (1 + 4 r^2)^(2/5)).

Written from the statement of topic 95 only; no verifier code is imported. Routes:

1. Exact (sympy, Fraction): the closed forms M = (2c + 1) I + [[-2 chi22 - chi04, chi31], [chi31, chi22]],
   M1 = [1 - t (c + e)/5] I + [[-chi04, chi13], [chi13, -chi22]] and
   M2 = [1 - c + (16/5) t (c + e)/(1 + 3t)] I + [[chi22 - chi04, (3 chi13 - chi31)/2], [., -2 chi22]] for a generic
   potential, with t = r^2/(1 + r^2) and e = u.X/r^2 = -d_theta chi_xy/r^2; conjugation by diag(1, -1) (the reflection
   x -> -x flips chi31 and chi13) leaves the eigenvalues unchanged; the eigenvalue lemma; the generator file of d2 (c
   equal to the original exponent, the shifted Legendre factors expanded and checked against sympy, every generator of
   the form r^(2k) cos(2m theta) (1 + r^2)^(p_j - k), k >= m).
2. Independent fields: the fourth derivatives chi22, chi04, chi31, chi13 and the radial velocity quotient e of every
   generator by Wirtinger calculus (d_x = d + dbar, d_y = i (d - dbar), d_theta = i (Z d - Zbar dbar), acting exactly on
   Z^A Zbar^B (1 + Z Zbar)^(E - s)); every term lands on t^i w^(j + 1) e^(i K theta) with integer i >= 0 and even K
   (asserted), so field = sum_j w^(j+1) P_j(t, z) with exact rational P_j (cos 2n theta = T_n(z),
   sin 2n theta = (1 - z^2)^(1/2) U_(n-1)(z)); z = cos 2 theta, w = (1 - t)^(delta/2). The values at the center are
   checked exactly.
3. The records (read only): for each matrix the primary certificate (COMPLETE, no failed or pending cell, 41, 79 and 119
   leaves, rectangles equal to their paths, complete binary tree of [0, 1] x [-1, 1] of area 2, every directed lower
   bound positive, the reported worst equal to the smallest leaf), the 640-bit recheck (all pass, the same paths, every
   row positive, hashes binding it to the primary and to the polynomial record), the audits and the status.
4. BALL at points (a sample, not a cover): the certified quantities lambda_min(M) - 19/5, lambda_min(M1) - 1/2 and
   (1 + 3t)(lambda_min(M2) - 1/2) from the fields of route 2 in 512-bit Arb at nine points of every leaf, each at least
   the leaf's certified lower bound; and on a grid of [0, 1] x [-1, 1] with t up to 1 - 1e-12 and t = 1.
5. FLOAT: the fields of route 2 against mpmath numerical derivatives of the exact potential at sample points.

Usage: python3 check_p95.py VERIFIER_RESEARCH_DIR NUMERICAL_DATA_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib, random, math
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import sympy as sp
import mpmath
from flint import arb, arb_poly, fmpq, ctx
ROOT = Path(sys.argv[1]); NUMD = Path(sys.argv[2])
OUT = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(__file__).with_suffix('.json')
sys.set_int_max_str_digits(0)
t00 = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
chk, out = {}, {'inputs': {}}
rng = random.Random(95)
V95 = ROOT / '95_refit_global_hypotheses/verification'
CL = Q(4076476460239181, 2 ** 51)
KINDS = {'M': 41, 'M1': 79, 'M2': 119}

# 1. exact
x, y = sp.symbols('x y', real=True)
chi = sp.Function('chi')(x, y)
u = sp.Matrix([-chi.diff(x, y, y), chi.diff(x, x, y)])
Du = u.jacobian([x, y]); sDu = (Du + Du.T) / 2
rho = -sp.diff(chi.diff(x, 2) + chi.diff(y, 2), y)
A = sp.Matrix([[rho.diff(y), -rho.diff(x) / 2], [-rho.diff(x) / 2, 0]])
cS = sp.Symbol('c', positive=True)
c22, c04, c31, c13 = sp.symbols('chi22 chi04 chi31 chi13')
rep = {chi.diff(x, 2, y, 2): c22, chi.diff(y, 4): c04, chi.diff(x, 3, y): c31, chi.diff(x, y, 3): c13}
r2 = x ** 2 + y ** 2; tS = r2 / (1 + r2)
eS = (u[0] * x + u[1] * y) / r2
V = sp.Matrix([cS * x, cS * y]) + u; sDV = cS * sp.eye(2) + sDu
dlog = lambda om: sp.Matrix([sp.diff(sp.log(om), x), sp.diff(sp.log(om), y)])
VD1 = (V.T * dlog((1 + r2) ** sp.Rational(-1, 10)))[0]; VD2 = (V.T * dlog((1 + 4 * r2) ** sp.Rational(2, 5)))[0]
Msym = ((2 * cS + 1) * sp.eye(2) + sDu + A).subs(rep)
M1sym = ((1 + cS + VD1) * sp.eye(2) - sDV + A).subs(rep)
M2sym = ((1 + cS + VD2) * sp.eye(2) - 2 * sDV + A).subs(rep)
M1cl = (1 - tS * (cS + eS) / 5) * sp.eye(2) + sp.Matrix([[-c04, c13], [c13, -c22]])
M2cl = (1 - cS + sp.Rational(16, 5) * tS * (cS + eS) / (1 + 3 * tS)) * sp.eye(2) + \
    sp.Matrix([[c22 - c04, (3 * c13 - c31) / 2], [(3 * c13 - c31) / 2, -2 * c22]])
psi = chi.diff(x, y)
chk['95: M = (2c + 1) I + sym Du + A = (2c + 1) I + [[-2 chi22 - chi04, chi31], [chi31, chi22]] (generic potential)'] = \
    sp.simplify(Msym - ((2 * cS + 1) * sp.eye(2) + sp.Matrix([[-2 * c22 - c04, c31], [c31, c22]]))) == sp.zeros(2)
chk['95: M1 = [1 - t (c + e)/5] I + [[-chi04, chi13], [chi13, -chi22]] and M2 = [1 - c + (16/5) t (c + e)/(1 + 3t)] I + '
    '[[chi22 - chi04, (3 chi13 - chi31)/2], [., -2 chi22]], t = r^2/(1 + r^2), e = u.X/r^2 (generic potential); '
    'e = -d_theta chi_xy/r^2'] = \
    sp.simplify(M1sym - M1cl) == sp.zeros(2) and sp.simplify(M2sym - M2cl) == sp.zeros(2) and \
    sp.simplify(eS + (-y * psi.diff(x) + x * psi.diff(y)) / r2) == 0
S = sp.diag(1, -1)
chk['95: diag(1, -1) M_k diag(1, -1) is M_k with (chi31, chi13) -> (-chi31, -chi13) (the reflection x -> -x, which '
    'keeps e), same eigenvalues'] = \
    all(sp.simplify(S * Mk * S - Mk.subs({c31: -c31, c13: -c13}, simultaneous=True)) == sp.zeros(2)
        for Mk in (Msym, M1cl, M2cl))
okl = True
for _ in range(2000):
    a, b, C = (Q(rng.randint(-500, 500), rng.randint(1, 60)) for _ in range(3)); C = abs(C)
    a2, b2 = a + Q(rng.randint(0, 50), rng.randint(1, 20)), b + Q(rng.randint(0, 50), rng.randint(1, 20))
    q = C * Q(rng.randint(-100, 100), 100)
    if a > 0 and b > 0 and a * b > C * C:
        okl = okl and a2 > 0 and b2 > 0 and a2 * b2 - q * q > 0
a_, b_, C_ = sp.symbols('a b C', real=True)
s_ = sp.sqrt((a_ - b_) ** 2 + 4 * C_ ** 2); L_ = (a_ + b_ - s_) / 2
chk['95 lemma: lambda_min([[a, C], [C, b]]) = (a + b - ((a - b)^2 + 4 C^2)^(1/2))/2; a, b > 0, ab > C^2 give a positive '
    'definite [[a\', q], [q, b\']] for a\' >= a, b\' >= b, |q| <= C (2000 exact tests)'] = \
    sp.expand((a_ - L_) * (b_ - L_) - C_ ** 2) == 0 and okl

ps = NUMD / 'nb_d2_exact.json'
src = json.loads(ps.read_text()); out['inputs']['numerics_data/nb_d2_exact.json'] = sha(ps)
cl = Q(src['cl']); gam = 1 / cl; delta = 1 - gam
chk['source: c of d2 equals the original exponent 4076476460239181/2^51; 1/2 > delta = 1 - 1/c > 4/9'] = \
    cl == CL and Q(1, 2) > delta > Q(4, 9)
pj = [(3 + gam - j * delta) / 2 for j in range(6)]
a = {}
nleg = set(); okspec = True
for g in src['generators']:
    j, m, v, spec = g['j'], g['m'], Q(g['coef']), g['spec']
    okspec = okspec and 0 <= j <= 5 and m >= 0
    if spec[0] == 'mono':
        okspec = okspec and spec[1] >= 0
        terms = {m + spec[1]: v}
    else:
        okspec = okspec and spec[0] == 'leg' and spec[1] >= 0 and spec[2] >= 0
        w_, n = spec[1], spec[2]; nleg.add(n)
        terms = {m + w_ + h: v * (-1) ** (n - h) * comb(n, h) * comb(n + h, h) for h in range(n + 1)}
    for k, vv in terms.items():
        a[j, m, k] = a.get((j, m, k), 0) + vv
a = {key: v for key, v in a.items() if v != 0}
ts = sp.Symbol('t')
okleg = all(sp.Poly(sp.expand(sp.legendre(n, 2 * ts - 1)), ts).all_coeffs()[::-1] ==
            [(-1) ** (n - h) * comb(n, h) * comb(n + h, h) for h in range(n + 1)] for n in sorted(nleg))
chk[f'source: {len(src["generators"])} generators H_m (1 + r^2)^(p_j - m) T(t), H_m = Re (x + iy)^(2m), T = t^h or '
    f't^w P_n(2t - 1); P_n(2t - 1) = sum_h (-1)^(n-h) C(n, h) C(n + h, h) t^h checked against sympy for the '
    f'{len(nleg)} degrees used; {len(a)} nonzero a_jmk, all with 0 <= m <= k, j <= 5'] = \
    okspec and okleg and all(0 <= m <= k for (j, m, k) in a)
out['source'] = {'generators': len(src['generators']), 'a_jmk': len(a), 'max_m': max(m for _, m, _ in a),
                 'max_k': max(k for _, _, k in a)}

# 2. independent fields by Wirtinger calculus
X_, Y_ = sp.symbols('X Y')
OPS = {'chi22': (2, 2), 'chi04': (0, 4), 'chi31': (3, 1), 'chi13': (1, 3)}
FIELDS = list(OPS) + ['e']
opc = {}
for f, (ax, ay) in OPS.items():
    pe = sp.Poly(sp.expand((X_ + Y_) ** ax * (sp.I * (X_ - Y_)) ** ay), X_, Y_)
    opc[f] = {mon: (Q(int(sp.re(cf))), Q(int(sp.im(cf)))) for mon, cf in pe.terms()}


def addto(D, key, v):
    if v != 0:
        D[key] = D.get(key, 0) + v


def dZ(D, E):
    o = {}
    for (A_, B_, s), v in D.items():
        if A_:
            addto(o, (A_ - 1, B_, s), v * A_)
        addto(o, (A_, B_ + 1, s + 1), v * (E - s))
    return o


def dZb(D, E):
    o = {}
    for (A_, B_, s), v in D.items():
        if B_:
            addto(o, (A_, B_ - 1, s), v * B_)
        addto(o, (A_ + 1, B_, s + 1), v * (E - s))
    return o


def cheb(n, kind):
    z_ = sp.Symbol('z')
    p_ = sp.chebyshevt(n, z_) if kind == 'T' else sp.chebyshevu(n, z_)
    return [int(cf) for cf in sp.Poly(p_, z_).all_coeffs()[::-1]]


trig = {f: {} for f in FIELDS}       # (j, i, kind, n) -> coefficient of t^i w^(j+1) cos/sin(2 n theta)
okexp = True
groups = {}
for (j, m, k), v in a.items():
    groups.setdefault((j, k), []).append((m, v))
for (j, k), ms in groups.items():
    E = fmpq((pj[j] - k).numerator, (pj[j] - k).denominator)
    base = {(m + k, k - m, 0): fmpq(v.numerator, v.denominator) for m, v in ms}
    Dq = {0: base}
    for q in range(1, 5):
        Dq[q] = dZb(Dq[q - 1], E)
    Dpq = {}
    for q in range(5):
        Dc = Dq[q]
        for p_ in range(4 - q):
            Dc = dZ(Dc, E)
        Dpq[(4 - q, q)] = Dc
    for f in OPS:
        for (pX, pY), (cr, ci) in opc[f].items():
            for (A_, B_, s), vv in Dpq[(pX, pY)].items():
                okexp = okexp and (A_ + B_) % 2 == 0 and s + k - (A_ + B_) // 2 == 2 and (A_ - B_) % 2 == 0
                i_ = (A_ + B_) // 2; K = A_ - B_; n = abs(K) // 2
                vq = Q(int(vv.p), int(vv.q))
                if cr:
                    addto(trig[f], (j, i_, 'c', n), cr * vq)
                if ci and n:
                    addto(trig[f], (j, i_, 's', n), -ci * vq * (1 if K > 0 else -1))
    # e = -d_theta chi_xy / (Z Zbar), chi_xy = i (d^2 - dbar^2) chi, d_theta = i (A - B) on Z^A Zbar^B (1 + Z Zbar)^p
    for sg, Dc in ((1, dZ(dZ(base, E), E)), (-1, dZb(dZb(base, E), E))):
        for (A_, B_, s), vv in Dc.items():
            i_ = (A_ + B_ - 2) // 2; K = A_ - B_; n = abs(K) // 2
            okexp = okexp and (A_ + B_) % 2 == 0 and K % 2 == 0 and (K == 0 or i_ >= 0) and s + k - i_ == 2
            if K:
                addto(trig['e'], (j, i_, 'c', n), sg * K * Q(int(vv.p), int(vv.q)))
chk['95 fields: every Wirtinger term of chi22, chi04, chi31, chi13 and e is t^i w^(j + 1) e^(i K theta) with integer '
    'i >= 0 and even K (the integer power of 1 - t is exactly zero)'] = okexp
trig = {f: {key: v for key, v in d.items() if v != 0} for f, d in trig.items()}
chk['95 fields: chi22, chi04 and e have only cosine terms and chi31, chi13 only sine terms (parity)'] = \
    all(key[2] == 'c' for f in ('chi22', 'chi04', 'e') for key in trig[f]) and \
    all(key[2] == 's' for f in ('chi31', 'chi13') for key in trig[f])
P = {f: [dict() for _ in range(6)] for f in FIELDS}
for f in FIELDS:
    for (j, i_, kind, n), v in trig[f].items():
        cf = cheb(n, 'T') if kind == 'c' else cheb(n - 1, 'U')
        for kz, cc in enumerate(cf):
            if cc:
                addto(P[f][j], (i_, kz), v * cc)
    P[f] = [{key: v for key, v in d.items() if v != 0} for d in P[f]]
SINE = {'chi31', 'chi13'}
deg = {f: [max(i for i, _ in d) if d else 0 for d in P[f]] for f in FIELDS}
degz = {f: [max(k for _, k in d) if d else 0 for d in P[f]] for f in FIELDS}
out['field_degrees_t'] = deg; out['field_degrees_z'] = degz
ser = json.dumps({f: [[[i, k, str(v)] for (i, k), v in sorted(d.items())] for d in P[f]] for f in FIELDS}, sort_keys=True)
out['fields_sha256'] = hashlib.sha256(ser.encode()).hexdigest()
# center values: sum over j of P_j(0, z)
cen = {}
for f in FIELDS:
    tot = {}
    for d in P[f]:
        for (i_, kz), v in d.items():
            if i_ == 0:
                addto(tot, kz, v)
    cen[f] = {k_: v for k_, v in tot.items() if v != 0}
okc = all(set(cen[f]) <= {0} for f in OPS)
c0 = {f: cen[f].get(0, Q(0)) for f in OPS}
a0 = -c0['chi22'] - c0['chi04']
lm0 = {'M': min(2 * cl + 1 - 2 * c0['chi22'] - c0['chi04'], 2 * cl + 1 + c0['chi22']),
       'M1': min(1 - c0['chi04'], 1 - c0['chi22']), 'M2': min(1 - cl + c0['chi22'] - c0['chi04'], 1 - cl - 2 * c0['chi22'])}
chk['95 fields: at the center chi22, chi04, chi31, chi13 are independent of the angle; chi22(0) = 1 - c, chi31(0) = '
    'chi13(0) = 0 (strain normalization Du(0) = diag(c - 1, 1 - c)), e(0, theta) = (c - 1) cos 2 theta, a_0 = '
    '-chi22(0) - chi04(0) > 1; lambda_min at the center: M c + 2 > 19/5, M1 c > 1/2, M2 c - 1 > 1/2'] = \
    okc and c0['chi22'] == 1 - cl and c0['chi31'] == 0 and c0['chi13'] == 0 and cen['e'] == {1: cl - 1} and a0 > 1 and \
    lm0['M'] == cl + 2 and lm0['M1'] == cl and lm0['M2'] == cl - 1 and \
    cl + 2 > Q(19, 5) and cl > Q(1, 2) and cl - 1 > Q(1, 2)
out['center'] = {'a0': str(a0), 'a0_display': float(a0),
                 'lambda_min_at_center': {k_: str(v) for k_, v in lm0.items()}}

# 3. the records


def rect(path):
    t0, t1, z0, z1 = Q(0), Q(1), Q(-1), Q(1)
    for ch in path:
        if ch in 'tT':
            mm = (t0 + t1) / 2; t0, t1 = (t0, mm) if ch == 't' else (mm, t1)
        else:
            mm = (z0 + z1) / 2; z0, z1 = (z0, mm) if ch == 'z' else (mm, z1)
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


pa = V95 / 'audit.json'; pam = V95 / 'audit_matrices.json'; pst = V95 / 'status.json'
au = json.loads(pa.read_text()); aum = json.loads(pam.read_text()); st = json.loads(pst.read_text())
for pth in (pa, pam, pst):
    out['inputs'][f'95/{pth.name}'] = sha(pth)
REC = {}
out['records'] = {}
for kind, nleaf in KINDS.items():
    pp = V95 / f'nb_d2_exact.{kind}.correlated.json'; pc = V95 / f'nb_d2_exact.{kind}.correlated.recheck.json'
    d = json.loads(pp.read_text()); r = json.loads(pc.read_text())
    out['inputs'][f'95/{pp.name}'] = sha(pp); out['inputs'][f'95/{pc.name}'] = sha(pc)
    acc = d['accepted']; paths = [x_['path'] for x_ in acc]
    okr = all(rect(x_['path']) == (Q(x_['t'][0]), Q(x_['t'][1]), Q(x_['z'][0]), Q(x_['z'][1])) for x_ in acc)
    area = sum((Q(x_['t'][1]) - Q(x_['t'][0])) * (Q(x_['z'][1]) - Q(x_['z'][0])) for x_ in acc)
    lows = [arb(x_['lower_numerator_after_target']) for x_ in acc]
    worst = arb(d['worst']); imin = min(range(len(lows)), key=lambda i: float(lows[i].mid()))
    chk[f'records {kind}: primary COMPLETE, no failed or pending cell, name nb_d2_exact, {nleaf} leaves, 512 bits'] = \
        d['status'] == 'COMPLETE' and d['failed'] == [] and d['pending_paths'] == [] and d['kind'] == kind and \
        d['name'] == 'nb_d2_exact' and len(acc) == nleaf and d['precision_bits'] == 512
    chk[f'records {kind}: rectangles equal their paths; complete binary tree of [0, 1] x [-1, 1]; total area 2'] = \
        okr and complete_tree(paths) and area == 2
    chk[f'records {kind}: every directed lower bound of the certified quantity is positive; worst = smallest leaf'] = \
        all(v > 0 for v in lows) and worst > 0 and lows[imin].overlaps(worst)
    rr = r['rows']
    chk[f'records {kind}: recheck all pass at 640 bits, the same {nleaf} paths, every row positive; it binds the '
        f'primary, and both bind the same polynomial record as the audits'] = \
        r['all_pass'] is True and r['precision_bits'] == 640 and r['leaves'] == nleaf and \
        sorted(x_['path'] for x_ in rr) == sorted(paths) and \
        all(x_['pass'] is True and arb(x_['lower']) > 0 for x_ in rr) and \
        r['primary_sha256'] == sha(pp) and r['polynomials_sha256'] == d['input_sha256'] == \
        au['source_polynomials_sha256'] and aum['files'][pp.name] == sha(pp) and aum['files'][pc.name] == sha(pc)
    REC[kind] = (acc, lows)
    out['records'][kind] = {'leaves': len(acc), 'worst_lower': str(worst), 'worst_display': float(worst.mid()),
                            'worst_path': acc[imin]['path'], 'worst_t': acc[imin]['t'], 'worst_z': acc[imin]['z']}
chk['records: audit all_pass with 41 primary and 41 independent leaves for M; matrix audit all_pass with 41, 79 and 119 '
    'leaves and the same proof hash; status V217 CONFIRMED'] = \
    au['all_pass'] is True and au['primary_leaves'] == 41 and au['independent_leaves'] == 41 and \
    au['files']['nb_d2_exact.M.correlated.json'] == aum['files']['nb_d2_exact.M.correlated.json'] and \
    aum['all_pass'] is True and aum['leaves'] == KINDS and aum['proof_sha256'] == au['proof_sha256'] == st['proof_sha256'] and \
    st['ledger'] == 'V217' and st['verdict'] == 'CONFIRMED'
out['records']['polynomials_sha256'] = au['source_polynomials_sha256']

# 4. BALL at points
ctx.prec = 512
AP = {}
for f in FIELDS:
    AP[f] = []
    for dd in P[f]:
        nz = max((k_ for _, k_ in dd), default=0) + 1; nt = max((i_ for i_, _ in dd), default=0) + 1
        cols = [[fmpq(0)] * nt for _ in range(nz)]
        for (i_, k_), v in dd.items():
            cols[k_][i_] = fmpq(v.numerator, v.denominator)
        AP[f].append([arb_poly([arb(c_) for c_ in col]) for col in cols])
ad = arb(fmpq(delta.numerator, delta.denominator)); acl = arb(fmpq(cl.numerator, cl.denominator))
TCACHE = {}


def columns_at(tq):
    key = (int(tq.p), int(tq.q))
    if key not in TCACHE:
        t = arb(tq)
        w = (1 - t) ** (ad / 2) if tq != 1 else arb(0)
        TCACHE[key] = {f: [(w ** (j + 1), [pk(t) for pk in AP[f][j]]) for j in range(6)] for f in FIELDS}
    return TCACHE[key]


def fields_at(tq, zq):
    z = arb(zq)
    s2 = (1 - z * z).sqrt() if zq * zq != 1 else arb(0)
    F = {}
    for f, cols in columns_at(tq).items():
        tot = arb(0)
        for wj, vals in cols:
            sm = arb(0)
            for vk in reversed(vals):
                sm = sm * z + vk
            tot += wj * sm
        F[f] = tot * s2 if f in SINE else tot
    return F


def lmin2(aa, bb, qq):
    # only the lower endpoint is used; a discriminant ball that meets the negatives is replaced by its upper endpoint
    dd = aa - bb
    disc = dd * dd + 4 * qq * qq
    if not disc >= 0:
        disc = disc.upper()
    return (aa + bb - disc.sqrt()) / 2


def certified(kind, tq, zq):
    F = fields_at(tq, zq); t = arb(tq)
    # lambda_min(sc I + B) = sc + lambda_min(B)
    if kind == 'M':
        return 2 * acl + 1 + lmin2(-2 * F['chi22'] - F['chi04'], F['chi22'], F['chi31']) - arb(fmpq(19, 5))
    if kind == 'M1':
        sc = 1 - t * (acl + F['e']) / 5
        return sc + lmin2(-F['chi04'], -F['chi22'], F['chi13']) - arb(fmpq(1, 2))
    sc = 1 - acl + arb(fmpq(16, 5)) * t * (acl + F['e']) / (1 + 3 * t)
    return (1 + 3 * t) * (sc + lmin2(F['chi22'] - F['chi04'], -2 * F['chi22'], (3 * F['chi13'] - F['chi31']) / 2)
                          - arb(fmpq(1, 2)))


out['leaf_points_min_slack'] = {}
for kind in KINDS:
    oklf = True; slack = None
    for x_, lo in zip(*REC[kind]):
        t0, t1, z0, z1 = (Q(v) for v in (*x_['t'], *x_['z']))
        for tq in (t0, (t0 + t1) / 2, t1):
            for zq in (z0, (z0 + z1) / 2, z1):
                v = certified(kind, fmpq(tq.numerator, tq.denominator), fmpq(zq.numerator, zq.denominator))
                gap = float(v.lower()) - float(lo.upper())
                oklf = oklf and math.isfinite(gap) and gap > -1e-60
                slack = gap if slack is None else min(slack, gap)
    chk[f'95 BALL {kind}: at the corners, edge midpoints and center of all {KINDS[kind]} leaves, the certified quantity '
        f'from the independent fields (512-bit Arb) is at least the leaf\'s certified lower bound'] = oklf
    out['leaf_points_min_slack'][kind] = slack
tg = sorted(set([fmpq(i, 40) for i in range(40)] + [1 - fmpq(1, 10 ** e) for e in (2, 3, 4, 6, 8, 12)] + [fmpq(1)]))
zg = [fmpq(k_, 16) - 1 for k_ in range(33)]
out['grid_sampled'] = {}
for kind in KINDS:
    gmin = None; gat = None
    for tq in tg:
        for zq in zg:
            lo = float(certified(kind, tq, zq).lower())
            if not math.isfinite(lo):
                gmin, gat = float('nan'), (float(tq), float(zq)); break
            if gmin is None or lo < gmin:
                gmin, gat = lo, (float(tq), float(zq))
    chk[f'95 BALL {kind} sampled ({len(tg) * len(zg)} grid points of [0, 1] x [-1, 1], t up to 1 - 1e-12 and t = 1): '
        f'the certified quantity is positive at every point'] = gmin > 0
    out['grid_sampled'][kind] = {'min_lower': gmin, 'at_t_z': gat, 'points': len(tg) * len(zg)}

# 5. FLOAT: the fields against numerical derivatives of the exact potential
mpmath.mp.dps = 60
mpj = [mpmath.mpf(p_.numerator) / p_.denominator for p_ in pj]
gl = {}
for (j, m, k), v in a.items():
    gl.setdefault((j, m), []).append((k, mpmath.mpf(v.numerator) / v.denominator))


def chi_f(xv, yv):
    qv = xv * xv + yv * yv; oq = 1 + qv
    zz = mpmath.mpc(xv, yv); tot = mpmath.mpf(0)
    bj = [oq ** e_ for e_ in mpj]
    for (j, m), terms in gl.items():
        hm = (zz ** (2 * m)).real
        tot += hm * bj[j] * mpmath.fsum(v * qv ** (k - m) / oq ** k for k, v in terms)
    return tot


hd = mpmath.mpf(10) ** -14
worst_rel = mpmath.mpf(0); npt = 0
mcl = mpmath.mpf(cl.numerator) / cl.denominator
for rv in ('0.05', '0.4', '1.3', '4', '30'):
    for th in (0.3, 1.2):
        r_ = mpmath.mpf(rv); xv, yv = r_ * mpmath.cos(th), r_ * mpmath.sin(th)
        dv = lambda o: mpmath.diff(chi_f, (xv, yv), o, h=hd)
        num = {f: dv(o) for f, o in OPS.items()}
        num['e'] = (-xv * dv((1, 2)) + yv * dv((2, 1))) / (r_ * r_)
        tq = r_ * r_ / (1 + r_ * r_); zq = mpmath.cos(2 * th); w = (1 - tq) ** ((1 - 1 / mcl) / 2)
        scale = max(abs(v) for v in num.values())
        for f in FIELDS:
            tot = mpmath.mpf(0)
            for j in range(6):
                tot += w ** (j + 1) * mpmath.fsum(mpmath.mpf(v.numerator) / v.denominator * tq ** i_ * zq ** k_
                                                  for (i_, k_), v in P[f][j].items())
            if f in SINE:
                tot *= mpmath.sqrt(1 - zq * zq)
            worst_rel = max(worst_rel, abs(tot - num[f]) / scale)
        npt += 1
chk[f'95 FLOAT: the independent fields reproduce chi22, chi04, chi31, chi13 and e from numerical derivatives of the '
    f'exact potential at {npt} points (r = 0.05 to 30), relative difference < 1e-20'] = worst_rel < 1e-20
out['fields_vs_potential_max_rel_FLOAT'] = float(worst_rel)

out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t00, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
