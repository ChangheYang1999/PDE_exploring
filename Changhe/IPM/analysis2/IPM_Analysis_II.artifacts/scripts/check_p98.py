"""Third computation for verification topic 98 (exact origin remainder bounds for the exact original state 131: on
the closed disk r <= r0, |field - b| <= K r^2 for rho_y, rho_x and the four entries of Du, and K r^3 for the two
entries of u - Du(0)X; 32 original numerical targets, seven displayed decimals named in V208 and eight improved
bounds at r0 = 1/10).

Written from the statement of topic 98 only; no verifier code is imported. Routes:

1. Exact (sympy, Fraction): c, a0 and delta = 1 - 1/c from the source record, q_j = (j + 1) delta/2 in (0, 1);
   the Taylor-division lemma ((1 - t)^q = 1 - sum a_n(q) t^n with a_n = (-1)^(n+1) binom(q, n), a_(n+1)/a_n =
   (n - q)/(n + 1), symbolic in q; for the four exact q_j every a_n > 0 and decreasing, so the tail after degree N is
   at most a_(N+1) t^(N+1)/(1 - t)); the stored tail coefficients equal a_13(q_j); the origin constants b from the
   degree-four Taylor part of the potential computed directly from the 860 source coefficients (rho_y(0) = a0,
   rho_x(0) = 0, Du(0) = diag(c - 1, 1 - c), and the linear part of u equal to Du(0)X); the stored origins equal b and
   sum_j P_j(0, z) = b identically; the stored H equals (1 - t)[sum_j W_(N, j) P_j - b]/t recomputed by exact
   polynomial division; the six fourth-derivative fields equal the combinations of the topic 96 polynomials
   (rho_y = -chi22 - chi04, rho_x = -chi31 - chi13, Du11 = -chi22, Du12 = -chi13, Du21 = chi31, Du22 = chi22) branch by
   branch; the error constant E = t0^N sum_j a_(N+1)(q_j) sum |p_(j,i,k)| t0^i recomputed for every statement.
2. The records (read only): 47 statements (8 fields x 4 radii with the original binary64 targets of the numerical
   record taken exactly, the seven V208 decimals, the eight improved r <= 1/10 bounds), every one COMPLETE with no
   failed or pending cell, t0 = r0^2/(1 + r0^2), the stored E equal to the recomputed one; the leaves form a complete
   binary tree of [0, t0] x [-1, 1] with rectangles equal to their paths; every leaf upper bound (arb ball) is below
   the exact target and the reported upper bound is the largest leaf; the 32-statement record agrees; the recheck
   record passes all 47 at 448 bits with the same leaf counts; hashes bind recheck, certificates, polynomials and the
   source and numerical records; the status record is V209 CONFIRMED.
3. Independent cover (Arb, 256 bits): for all 47 statements, an adaptive cover of [0, t0] x [-1, 1] by the mean-value
   form of F = s(z)^2 H(t, z)^2 (s^2 = 1, 1 - z^2, (1 + z)/2, (1 - z)/2), with H recomputed here; a cell is accepted
   when the upper bound of F is below (T - E)^2, which gives |s|(|H| + E) < T since |s| <= 1.
4. FLOAT: the 32 branch polynomials against mpmath numerical derivatives (50 digits) of the exact original potential
   at sample points of the first quadrant (r = 0.05 to 300); the normalized remainders (field - b)/r^2 and
   (u - Du(0)X)/r^3 from those derivatives against s H at small radii; sampled maxima of s |H| below every target.

Usage: python3 check_p98.py VERIFIER_RESEARCH_DIR NUMERICAL_DATA_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib, math
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import mpmath
from flint import arb, arb_poly, fmpq, ctx
ROOT = Path(sys.argv[1]); NUMD = Path(sys.argv[2])
OUT = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(__file__).with_suffix('.json')
t00 = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
chk, out = {}, {'inputs': {}}
V98 = ROOT / '98_original_origin_recomputation/verification'
FIELDS = ['rho_y', 'rho_x', 'DU11', 'DU12', 'DU21', 'DU22', 'U1', 'U2']
FACTOR = {'rho_y': 'one', 'rho_x': 'sin2', 'DU11': 'one', 'DU12': 'sin2', 'DU21': 'sin2', 'DU22': 'one', 'U1': 'cos', 'U2': 'sin'}
THIRD = {'U1', 'U2'}
RADII = ['1/100', '1/50', '1/20', '1/10']

ps = ROOT / 'source_audit/state131_exact.json'
src = json.loads(ps.read_text()); out['inputs']['source_audit/state131_exact.json'] = sha(ps)
cl = Q(src['exact_parameters']['cl']); a0 = Q(src['exact_parameters']['a0'])
coef = [(tuple(t), Q(v)) for t, v in zip(src['canonical_order'], src['canonical_coefficients'])]
chk['input: 860 canonical coefficients, c = 4076476460239181/2^51'] = len(coef) == 860 and cl == Q(4076476460239181, 2 ** 51)
delta = 1 - 1 / cl
qs = [(j + 1) * delta / 2 for j in range(4)]
pp = V98 / 'polynomials.json'
poly = json.loads(pp.read_text()); out['inputs']['98/polynomials.json'] = sha(pp)
N = poly['N']
chk['98: N = 12, the record c and delta = 1 - 1/c equal the source; q_j = (j + 1) delta/2 lie in (0, 1) for j = 0..3'] = \
    N == 12 and Q(poly['cl']) == cl and Q(poly['delta']) == delta and all(0 < q < 1 for q in qs)

# 1. exact
qS, tS = sp.symbols('q t', positive=True)
nS = sp.Symbol('n', integer=True, positive=True)
aS = lambda n: (-1) ** (n + 1) * sp.binomial(qS, n)
ser = sp.series((1 - tS) ** qS, tS, 0, N + 2).removeO()
chk['98 lemma: (1 - t)^q = 1 - sum_n a_n(q) t^n with a_n = (-1)^(n+1) binom(q, n) through degree 13 (symbolic q), '
    'and a_(n+1)/a_n = (n - q)/(n + 1) (symbolic n, q)'] = \
    sp.expand(ser - (1 - sum(sp.expand_func(aS(n)) * tS ** n for n in range(1, N + 2)))) == 0 and \
    sp.simplify(sp.combsimp(sp.expand_func(aS(nS + 1) / aS(nS))) - (nS - qS) / (nS + 1)) == 0


def a_list(q, n_max):
    a = [None, q]
    for n in range(1, n_max):
        a.append(a[n] * (n - q) / (n + 1))
    return a


A = [a_list(q, 40) for q in qs]
chk['98 lemma: for the four exact q_j, a_1 = q_j > 0 and 0 < (n - q_j)/(n + 1) < 1, so a_n > 0 decreases and '
    'sum_(n > N) a_n t^n <= a_(N+1) t^(N+1) sum_m t^m = a_(N+1) t^(N+1)/(1 - t) (checked through n = 40)'] = \
    all(A[j][1] == qs[j] and all(A[j][n] > 0 and A[j][n + 1] < A[j][n] for n in range(1, 40)) for j in range(4))
# sharpness of the tail bound at sample points (exact in Arb): |(1 - t)^q - W_N(t)| <= a_(N+1) t^(N+1)/(1 - t)
ctx.prec = 256
okt = True
for j in range(4):
    for tq in (fmpq(1, 10001), fmpq(1, 2501), fmpq(1, 401), fmpq(1, 101), fmpq(1, 10)):
        tv = arb(tq); W = arb(1) - sum(arb(fmpq(A[j][n].numerator, A[j][n].denominator)) * tv ** n for n in range(1, N + 1))
        lhs = abs((1 - tv) ** arb(fmpq(qs[j].numerator, qs[j].denominator)) - W)
        rhs = arb(fmpq(A[j][N + 1].numerator, A[j][N + 1].denominator)) * tv ** (N + 1) / (1 - tv)
        okt = okt and bool(lhs < rhs)
chk['98 lemma (Arb at t = 1/10001, 1/2501, 1/401, 1/101, 1/10, each q_j): |(1 - t)^q - W_N(t)| < a_(N+1) t^(N+1)/(1 - t)'] = okt
ok_tail = True
for f in FIELDS:
    ok_tail = ok_tail and [Q(v) for v in poly['fields'][f]['tail_coefficients']] == [A[j][N + 1] for j in range(4)]
chk['98: the stored tail coefficients of all eight fields equal a_13(q_j), j = 0..3'] = ok_tail

# origin constants from the degree-four Taylor part of the potential
x, y = sp.symbols('x y', real=True)
mg = 1 / cl
groups = {}
for (j, m, k), a in coef:
    if a != 0:
        groups.setdefault((j, m), []).append((k - m, a))
chk['source: every generator has l = k - m >= 0 (power of v = r^2/(1 + r^2)) and m <= 9'] = \
    all(l >= 0 for terms in groups.values() for l, _ in terms) and max(m for _, m in groups) <= 9


def binom_q(a, n):
    out_ = Q(1)
    for i in range(n):
        out_ = out_ * (a - i) / (i + 1)
    return out_


T4 = 0
qq = x ** 2 + y ** 2
for (j, m), terms in groups.items():
    if m > 2:
        continue
    e = (3 + mg - j * (1 - mg)) / 2 - m
    # sum_l cf_l q^l (1 + q)^(e - l): coefficient of q^(2 - m)
    cq = sum(a * binom_q(e - l, 2 - m - l) for l, a in terms if l <= 2 - m)
    T4 += sp.re(sp.expand((x + sp.I * y) ** (2 * m))) * sp.Rational(cq.numerator, cq.denominator) * qq ** (2 - m)
T4 = sp.expand(T4)
d = lambda i, k: sp.diff(T4, x, i, y, k) if i and k else (sp.diff(T4, x, i) if i else sp.diff(T4, y, k))
c22, c04, c31, c13 = (sp.nsimplify(d(2, 2)), sp.nsimplify(d(0, 4)), sp.nsimplify(d(3, 1)), sp.nsimplify(d(1, 3)))
S = lambda v: Q(int(sp.fraction(v)[0]), int(sp.fraction(v)[1]))
B = {'rho_y': S(-c22 - c04), 'rho_x': S(-c31 - c13), 'DU11': S(-c22), 'DU12': S(-c13), 'DU21': S(c31), 'DU22': S(c22)}
B['U1'], B['U2'] = B['DU11'], B['DU22']
chk['98: from the degree-four Taylor part of the potential (source coefficients, exact): rho_y(0) = a0, rho_x(0) = 0, '
    'Du(0) = diag(c - 1, 1 - c); the linear part of u is (-T4_xyy, T4_xxy) = ((c - 1) x, (1 - c) y)'] = \
    B['rho_y'] == a0 and B['rho_x'] == 0 and B['DU11'] == cl - 1 and B['DU22'] == 1 - cl and B['DU12'] == 0 and \
    B['DU21'] == 0 and sp.expand(-sp.diff(T4, x, 1, y, 2) - sp.Rational((cl - 1).numerator, (cl - 1).denominator) * x) == 0 and \
    sp.expand(sp.diff(T4, x, 2, y, 1) - sp.Rational((1 - cl).numerator, (1 - cl).denominator) * y) == 0
chk['98: the potential is even in x and in y (Re((x + iy)^(2m)) and r^2 are), so each field is even or odd in each '
    'variable and the first-quadrant bound extends by reflection'] = \
    all(sp.expand(sp.re(sp.expand((x + sp.I * y) ** (2 * m))).subs(x, -x) - sp.re(sp.expand((x + sp.I * y) ** (2 * m)))) == 0 and
        sp.expand(sp.re(sp.expand((x + sp.I * y) ** (2 * m))).subs(y, -y) - sp.re(sp.expand((x + sp.I * y) ** (2 * m)))) == 0
        for m in range(10))

BR = {f: [{(int(i), int(k)): Q(v) for i, k, v in br} for br in poly['fields'][f]['branches']] for f in FIELDS}
HS = {f: {(int(i), int(k)): Q(v) for i, k, v in poly['fields'][f]['H']} for f in FIELDS}
chk['98: the stored factors and origins: s = 1 (rho_y, Du11, Du22), (1 - z^2)^(1/2) (rho_x, Du12, Du21), '
    '((1 + z)/2)^(1/2) (u1), ((1 - z)/2)^(1/2) (u2); origin = b'] = \
    all(poly['fields'][f]['factor'] == FACTOR[f] and Q(poly['fields'][f]['origin']) == B[f] for f in FIELDS)
chk['98: sum_j P_j(0, z) = b identically in z for all eight fields'] = \
    all(sum(BR[f][j].get((0, k), 0) for j in range(4)) == (B[f] if k == 0 else 0)
        for f in FIELDS for k in range(1 + max(k_ for br in BR[f] for _, k_ in br)))


def recompute_H(f):
    num = {}
    for j in range(4):
        W = [Q(1)] + [-A[j][n] for n in range(1, N + 1)]
        for (i, k), v in BR[f][j].items():
            for n, w in enumerate(W):
                num[(i + n, k)] = num.get((i + n, k), 0) + w * v
    num[(0, 0)] = num.get((0, 0), 0) - B[f]
    assert all(v == 0 for (i, k), v in num.items() if i == 0)
    h = {}
    for (i, k), v in num.items():  # (1 - t) * num / t
        if i == 0 or v == 0:
            continue
        h[(i - 1, k)] = h.get((i - 1, k), 0) + v
        h[(i, k)] = h.get((i, k), 0) - v
    return {key: v for key, v in h.items() if v != 0}


HR = {f: recompute_H(f) for f in FIELDS}
chk['98: H = (1 - t)[sum_j W_(N,j) P_j - b]/t recomputed by exact division (the t^0 row of the numerator vanishes) '
    'equals the stored H for all eight fields'] = all(HR[f] == {k_: v for k_, v in HS[f].items() if v != 0} for f in FIELDS)
p96 = ROOT / '96_original_auxiliary_recomputation/verification/polynomials.json'
P96 = json.loads(p96.read_text()); out['inputs']['96/polynomials.json'] = sha(p96)
G = lambda name, j: {(int(i), int(k)): Q(v) for i, k, v in P96['polynomials'][f'{name}_{j}']}


def lin(*terms):
    res = {}
    for sgn, pj in terms:
        for key, v in pj.items():
            res[key] = res.get(key, 0) + sgn * v
    return {key: v for key, v in res.items() if v != 0}


ok96 = True
for j in range(4):
    want = {'rho_y': lin((-1, G('chi22', j)), (-1, G('chi04', j))), 'rho_x': lin((-1, G('chi31', j)), (-1, G('chi13', j))),
            'DU11': lin((-1, G('chi22', j))), 'DU12': lin((-1, G('chi13', j))), 'DU21': lin((1, G('chi31', j))),
            'DU22': lin((1, G('chi22', j)))}
    for f, w in want.items():
        ok96 = ok96 and lin((1, BR[f][j])) == w
chk['98: the six fourth-derivative fields equal the combinations of the topic 96 polynomials branch by branch '
    '(rho_y = -chi22 - chi04, rho_x = -chi31 - chi13, Du11 = -chi22, Du12 = -chi13, Du21 = chi31, Du22 = chi22)'] = \
    ok96 and poly['fourth_polynomials_sha256'] == sha(p96) and P96['source_sha256'] == sha(ps)


def E_of(f, t0):
    return t0 ** N * sum(A[j][N + 1] * sum(abs(v) * t0 ** i for (i, k), v in BR[f][j].items()) for j in range(4))


# 2. the records
pn = NUMD / 'origin_N4_131.json'
num = json.loads(pn.read_text()); out['inputs']['numerics/origin_N4_131.json'] = sha(pn)
NUMKEY = {'rho_y': 'rho_y - a0', 'rho_x': 'rho_x', 'DU11': 'DU11 - (cl-1)', 'DU12': 'DU12', 'DU21': 'DU21',
          'DU22': 'DU22 - (1-cl)', 'U1': 'U1 - (cl-1)x', 'U2': 'U2 - (1-cl)y'}
RKEY = {'1/100': '0.01', '1/50': '0.02', '1/20': '0.05', '1/10': '0.1'}
V208 = [('DU11', '1/20', '0.609886'), ('U2', '1/20', '0.283275'), ('rho_x', '1/50', '1.18167'), ('DU21', '1/50', '0.602244'),
        ('U1', '1/100', '0.275744'), ('U2', '1/100', '0.280694'), ('DU21', '1/100', '0.600802')]
IMPROVED = {'rho_y': '3.04', 'rho_x': '1.24', 'DU11': '0.65', 'DU12': '0.59', 'DU21': '0.66', 'DU22': '0.65', 'U1': '0.285', 'U2': '0.293'}
expected = {(f, r, Q(num[NUMKEY[f]][RKEY[r]][0]), 'original_number') for f in FIELDS for r in RADII}
expected |= {(f, r, Q(dv), 'independent_decimal') for f, r, dv in V208}
expected |= {(f, '1/10', Q(dv), 'independent_decimal') for f, dv in IMPROVED.items()}
chk['records: the original targets are the exact binary64 values of the numerical record; each of the seven V208 '
    'decimals is below the stored binary64 value it was displayed for (so it does not follow by outward rounding)'] = \
    all(Q(num[NUMKEY[f]][RKEY[r]][0]) == Q(float(num[NUMKEY[f]][RKEY[r]][0])) for f in FIELDS for r in RADII) and \
    all(Q(dv) < Q(num[NUMKEY[f]][RKEY[r]][0]) for f, r, dv in V208)
pc = V98 / 'certificates.json'; po = V98 / 'certificates.original32.json'; pr = V98 / 'recheck.json'
cert = json.loads(pc.read_text()); c32 = json.loads(po.read_text()); rec = json.loads(pr.read_text())
for p_, k_ in ((pc, 'certificates.json'), (po, 'certificates.original32.json'), (pr, 'recheck.json')):
    out['inputs'][f'98/{k_}'] = sha(p_)
res = cert['results']
got = {(x_['field'], x_['radius'], Q(x_['target']), x_['label']) for x_ in res}
chk['records: 47 statements, exactly the 32 original targets, the seven V208 decimals and the eight improved r <= 1/10 '
    'bounds; source and numerics hashes bind the polynomial and numerical records'] = \
    len(res) == 47 and got == expected and len(expected) == 47 and cert['source_sha256'] == sha(pp) and \
    cert['numerics_sha256'] == sha(pn) and poly['source_sha256'] == sha(ps)


def rect(path, t0):
    ta, tb, za, zb = Q(0), t0, Q(-1), Q(1)
    for ch in path:
        if ch in 'tT':
            m = (ta + tb) / 2; ta, tb = (ta, m) if ch == 't' else (m, tb)
        else:
            m = (za + zb) / 2; za, zb = (za, m) if ch == 'z' else (m, zb)
    return ta, tb, za, zb


def complete_tree(paths):
    s_ = set(paths)
    if len(s_) != len(paths):
        return False
    pref = {p[:i] for p in paths for i in range(len(p))}
    if s_ & pref:
        return False
    for p in pref:
        kids = {q[len(p)] for q in paths if len(q) > len(p) and q.startswith(p)}
        if kids not in ({'t', 'T'}, {'z', 'Z'}):
            return False
    return True


ok_st = ok_E = ok_tree = ok_up = True
leafcount = {}
for x_ in res:
    r0 = Q(x_['radius']); t0 = r0 * r0 / (1 + r0 * r0); T = Q(x_['target'])
    ok_st = ok_st and x_['status'] == 'COMPLETE' and x_['failed'] == [] and x_['pending_paths'] == [] and \
        Q(x_['t0']) == t0 and x_['precision_bits'] == 384
    ok_E = ok_E and Q(x_['E']) == E_of(x_['field'], t0)
    acc = x_['accepted']; paths = [a['path'] for a in acc]
    area = sum((Q(a['t'][1]) - Q(a['t'][0])) * (Q(a['z'][1]) - Q(a['z'][0])) for a in acc)
    ok_tree = ok_tree and complete_tree(paths) and area == 2 * t0 and \
        all(rect(a['path'], t0) == (Q(a['t'][0]), Q(a['t'][1]), Q(a['z'][0]), Q(a['z'][1])) for a in acc)
    ups = [arb(a['upper']) for a in acc]; Ta = arb(fmpq(T.numerator, T.denominator))
    imax = max(range(len(ups)), key=lambda i: float(ups[i].mid()))
    ok_up = ok_up and all(bool(u < Ta) for u in ups) and arb(x_['upper']).overlaps(ups[imax]) and bool(arb(x_['upper']) < Ta)
    leafcount[(x_['field'], x_['radius'], x_['target'])] = len(acc)
chk['records: every statement COMPLETE, no failed or pending cell, t0 = r0^2/(1 + r0^2), 384 bits'] = ok_st
chk['records: the stored E of every statement equals t0^N sum_j a_(N+1)(q_j) sum |p_(j,i,k)| t0^i recomputed exactly'] = ok_E
chk['records: rectangles equal their paths; the leaves form a complete binary tree of [0, t0] x [-1, 1] (area 2 t0)'] = ok_tree
chk['records: every leaf upper bound of |s|(|H| + E) is below the exact target; the reported bound is the largest leaf'] = ok_up
r32 = c32['results']
chk['records: the 32-statement record has the same 32 original statements, all COMPLETE with upper below target, '
    'and the same source and numerics hashes'] = \
    len(r32) == 32 and {(x_['field'], x_['radius'], Q(x_['target'])) for x_ in r32} == \
    {(f, r, T) for f, r, T, lab in expected if lab == 'original_number'} and \
    all(x_['status'] == 'COMPLETE' and x_['failed'] == [] and x_['pending_paths'] == [] and
        bool(arb(x_['upper']) < arb(fmpq(Q(x_['target']).numerator, Q(x_['target']).denominator))) for x_ in r32) and \
    c32['source_sha256'] == sha(pp) and c32['numerics_sha256'] == sha(pn)
rr = rec['results']
chk['records: recheck all pass at 448 bits for all 47 statements with the same leaf counts, every row below its '
    'target; it binds the certificates and polynomial records by hash'] = \
    rec['all_pass'] is True and rec['precision_bits'] == 448 and len(rr) == 47 and \
    {(x_['field'], x_['radius'], Q(x_['target']), x_['label']) for x_ in rr} == expected and \
    all(x_['pass'] is True and x_['leaves'] == leafcount[(x_['field'], x_['radius'], x_['target'])] and
        bool(arb(x_['upper']) < arb(fmpq(Q(x_['target']).numerator, Q(x_['target']).denominator))) for x_ in rr) and \
    rec['certificates_sha256'] == sha(pc) and rec['polynomials_sha256'] == sha(pp)
pst = V98 / 'status.json'; st = json.loads(pst.read_text()); out['inputs']['98/status.json'] = sha(pst)
chk['records: status V209 CONFIRMED'] = st['ledger'] == 'V209' and st['verdict'] == 'CONFIRMED'
out['status_proof_sha256'] = st['proof_sha256']

# 3. independent cover: mean-value form of F = s^2 H^2 on adaptive cells
S2 = {'one': [Q(1)], 'sin2': [Q(1), Q(0), Q(-1)], 'cos': [Q(1, 2), Q(1, 2)], 'sin': [Q(1, 2), Q(-1, 2)]}


def to_arb_rows(h):
    nk = max(k for _, k in h) + 1; nt = max(i for i, _ in h) + 1
    rows = [[fmpq(0)] * nt for _ in range(nk)]
    for (i, k), v in h.items():
        rows[k][i] = fmpq(v.numerator, v.denominator)
    return [arb_poly([arb(c_) for c_ in row]) for row in rows]


def build_F(f):
    Hr = to_arb_rows(HR[f]); K = len(Hr)
    H2 = [arb_poly([0]) for _ in range(2 * K - 1)]
    for a_ in range(K):
        for b_ in range(K):
            H2[a_ + b_] += Hr[a_] * Hr[b_]
    s2 = S2[FACTOR[f]]
    F = [arb_poly([0]) for _ in range(len(H2) + len(s2) - 1)]
    for i, sv in enumerate(s2):
        if sv:
            for k, hp in enumerate(H2):
                F[i + k] += arb(fmpq(sv.numerator, sv.denominator)) * hp
    Ft = [p.derivative() for p in F]
    Fz = [(k + 1) * F[k + 1] for k in range(len(F) - 1)]
    return F, Ft, Fz


def ev(P, t, z):
    acc = P[-1](t)
    for p in reversed(P[:-1]):
        acc = acc * z + p(t)
    return acc


def ball(a, b):
    return arb(a).union(arb(b))


def cover(f, r0, T, E, max_cells=400000):
    t0 = r0 * r0 / (1 + r0 * r0)
    F, Ft, Fz = build_F(f)
    thr = (arb(fmpq(T.numerator, T.denominator)) - arb(fmpq(E.numerator, E.denominator))) ** 2
    stack = [(fmpq(0), fmpq(t0.numerator, t0.denominator), fmpq(-1), fmpq(1))]
    n_acc = n_cells = 0; worst = None
    while stack:
        ta, tb, za, zb = stack.pop(); n_cells += 1
        if n_cells > max_cells:
            return False, n_acc, n_cells, worst
        tm, zm = (ta + tb) / 2, (za + zb) / 2
        tB, zB = ball(ta, tb), ball(za, zb)
        gt = abs(ev(Ft, tB, zB)) * arb((tb - ta) / 2); gz = abs(ev(Fz, tB, zB)) * arb((zb - za) / 2)
        up = ev(F, arb(tm), arb(zm)) + gt + gz
        nat = ev(F, tB, zB)
        ub = min(float(up.upper()), float(nat.upper()))
        if bool(up < thr) or bool(nat < thr):
            n_acc += 1
            worst = ub if worst is None else max(worst, ub)
            continue
        if float(gt.upper()) >= float(gz.upper()):
            stack += [(ta, tm, za, zb), (tm, tb, za, zb)]
        else:
            stack += [(ta, tb, za, zm), (ta, tb, zm, zb)]
    return True, n_acc, n_cells, worst


rows_cov = []; okc = True
for x_ in sorted(res, key=lambda r_: (r_['field'], Q(r_['radius']), Q(r_['target']))):
    r0 = Q(x_['radius']); T = Q(x_['target']); t0 = r0 * r0 / (1 + r0 * r0); E = E_of(x_['field'], t0)
    t1 = time.monotonic()
    ok, nacc, ncell, worst = cover(x_['field'], r0, T, E)
    okc = okc and ok
    rows_cov.append({'field': x_['field'], 'radius': x_['radius'], 'target': x_['target'], 'label': x_['label'], 'pass': ok,
                     'cells_accepted': nacc, 'cells_visited': ncell,
                     'largest_cell_bound_sqrt_display': math.sqrt(worst) + float(E) if worst is not None else None,
                     'target_display': float(T), 'record_upper_display': float(arb(x_['upper']).mid()),
                     'seconds': round(time.monotonic() - t1, 2)})
    print(rows_cov[-1], flush=True)
chk['98 independent cover (Arb 256 bits, mean-value form of s^2 H^2 with H recomputed here): all 47 statements, '
    '|s|(|H| + E) < T on complete adaptive covers of [0, t0] x [-1, 1]'] = okc
out['independent_cover'] = rows_cov

# 4. FLOAT: branch polynomials against the original potential, normalized remainders, sampled maxima
mpmath.mp.dps = 50
mc = mpmath.mpf(cl.numerator) / cl.denominator; mgf = 1 / mc
gl = []
for (j, m), terms in groups.items():
    deg = max(l for l, _ in terms); cf = [mpmath.mpf(0)] * (deg + 1)
    for l, a in terms:
        cf[l] += mpmath.mpf(a.numerator) / a.denominator
    gl.append(((3 + mgf - j * (1 - mgf)) / 2 - m, m, cf[::-1]))


def chi_f(xv, yv):
    qv = xv * xv + yv * yv; oq = 1 + qv; v = qv / oq
    zz = mpmath.mpc(xv, yv); tot = mpmath.mpf(0)
    for e_, m, cf in gl:
        tot += (zz ** (2 * m)).real * oq ** e_ * mpmath.polyval(cf, v)
    return tot


mq = [mpmath.mpf(q.numerator) / q.denominator for q in qs]
SF = {'one': lambda z: mpmath.mpf(1), 'sin2': lambda z: mpmath.sqrt(1 - z * z),
      'cos': lambda z: mpmath.sqrt((1 + z) / 2), 'sin': lambda z: mpmath.sqrt((1 - z) / 2)}
mpoly = lambda pj, t, z: mpmath.fsum(mpmath.mpf(v.numerator) / v.denominator * t ** i * z ** k for (i, k), v in pj.items())


def field_rep(f, r_, t, z):
    tot = mpmath.fsum((1 - t) ** mq[j] * mpoly(BR[f][j], t, z) for j in range(4))
    return SF[FACTOR[f]](z) * tot * (r_ if f in THIRD else 1)


def field_num(xv, yv, hd):
    D = lambda i, k: mpmath.diff(chi_f, (xv, yv), (i, k), h=hd)
    c22_, c04_, c31_, c13_ = D(2, 2), D(0, 4), D(3, 1), D(1, 3)
    return {'rho_y': -c22_ - c04_, 'rho_x': -c31_ - c13_, 'DU11': -c22_, 'DU12': -c13_, 'DU21': c31_, 'DU22': c22_,
            'U1': -D(1, 2), 'U2': D(2, 1)}


hd = mpmath.mpf(10) ** -12
worst_rel = mpmath.mpf(0); ns = 0
for rv in ('0.05', '0.3', '1', '2.5', '7', '40', '300'):
    for th in (0.2, 0.7, 1.1, 1.45):
        r_ = mpmath.mpf(rv); xv, yv = r_ * mpmath.cos(th), r_ * mpmath.sin(th)
        t = r_ * r_ / (1 + r_ * r_); z = mpmath.cos(2 * th)
        nf = field_num(xv, yv, hd)
        for grp in (THIRD, set(FIELDS) - THIRD):
            scale = max(abs(nf[f]) for f in grp)
            for f in grp:
                worst_rel = max(worst_rel, abs(field_rep(f, r_, t, z) - nf[f]) / scale)
        ns += 1
chk[f'98 FLOAT: the 32 branch polynomials reproduce rho_y, rho_x, Du and u from numerical derivatives of the original '
    f'potential at {ns} points (r = 0.05 to 300), relative difference < 1e-14'] = worst_rel < 1e-14
out['poly_vs_potential_max_rel_FLOAT'] = float(worst_rel)
mH = {f: {key: mpmath.mpf(v.numerator) / v.denominator for key, v in HR[f].items()} for f in FIELDS}
evH = lambda f, t, z: mpmath.fsum(v * t ** i * z ** k for (i, k), v in mH[f].items())
worst_n = mpmath.mpf(0)
for rv in ('0.01', '0.03', '0.1'):
    for th in (0.15, 0.6, 1.0, 1.4):
        r_ = mpmath.mpf(rv); xv, yv = r_ * mpmath.cos(th), r_ * mpmath.sin(th)
        t = r_ * r_ / (1 + r_ * r_); z = mpmath.cos(2 * th)
        nf = field_num(xv, yv, hd)
        Bm = {f: mpmath.mpf(B[f].numerator) / B[f].denominator for f in FIELDS}
        for f in FIELDS:
            if f == 'U1':
                normd = (nf[f] - Bm[f] * xv) / r_ ** 3
            elif f == 'U2':
                normd = (nf[f] - Bm[f] * yv) / r_ ** 3
            else:
                normd = (nf[f] - Bm[f]) / r_ ** 2
            worst_n = max(worst_n, abs(normd - SF[FACTOR[f]](z) * evH(f, t, z)) / max(abs(normd), 1))
chk['98 FLOAT: (field - b)/r^2 and (u - Du(0)X)/r^3 from numerical derivatives of the potential equal s H within 1e-8 '
    'at r = 0.01, 0.03, 0.1 (12 points per field)'] = worst_n < 1e-8
out['normalized_vs_sH_max_rel_FLOAT'] = float(worst_n)
okm = True; smax = {}
fH = {f: [(i, k, float(v)) for (i, k), v in HR[f].items()] for f in FIELDS}
fS = {'one': lambda z: 1.0, 'sin2': lambda z: math.sqrt(max(0.0, 1 - z * z)), 'cos': lambda z: math.sqrt((1 + z) / 2),
      'sin': lambda z: math.sqrt((1 - z) / 2)}
best_fr = {}
for f in FIELDS:
    for rq in RADII:
        r0 = Q(rq); t0 = float(r0 * r0 / (1 + r0 * r0)); best = 0.0
        for i in range(9):
            for k in range(81):
                t = t0 * i / 8; z = k / 40 - 1
                best = max(best, fS[FACTOR[f]](z) * abs(sum(v * t ** i_ * z ** k_ for i_, k_, v in fH[f])))
        best_fr[(f, rq)] = best
for x_ in res:
    best = best_fr[(x_['field'], x_['radius'])]
    smax[f'{x_["field"]} {x_["radius"]} {x_["target"]}'] = best
    okm = okm and best <= float(arb(x_['upper']).mid()) * (1 + 1e-12) and best < float(Q(x_['target']))
chk['98 FLOAT: on a 9 x 81 grid of [0, t0] x [-1, 1] the sampled maxima of s|H| lie below the record upper bounds '
    'and the targets (47 statements)'] = okm
out['sampled_max_sH_FLOAT'] = smax
out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t00, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
