"""Independent exact audit of the topic240 jump-constraint matrices (Fraction only, no numpy).

Part A: load the exported 6x38 and 9x38 matrices and nullspace bases from
        240/evidence/exact_constraints.json; own elimination for ranks,
        nullspace identities, independence, containment.
Part B: rebuild every jump row from scratch: own Cox-de Boor on the two end
        spans of the coarse knot vector of 239/evidence/exact_inputs.json,
        own Vandermonde solve for the inner C3 matching, own Lagrange weights
        for the inner powers and outer columns (pair list of topic235 PROOF.md
        line 9), scales from the 239 export; compare entry by entry.
Reads only; writes nothing (output goes to stdout).
"""
import json, time
from fractions import Fraction as F
from math import factorial

T0 = time.monotonic()
P = 'verification/proofs/'
EX = json.load(open(P + '240_s1j1_high_intersections/evidence/exact_constraints.json'))
IN = json.load(open(P + '239_s1j1_full_input/evidence/exact_inputs.json'))
fr = lambda M: [[F(x) for x in row] for row in M]

# ---------------------------------------------------------------- elimination
def rank(rows, colorder=None):
    """Plain Gaussian elimination over Q, pivoting along colorder."""
    M = [list(r) for r in rows]
    if not M:
        return 0
    n = len(M[0]); colorder = colorder or list(range(n))
    r = 0
    for c in colorder:
        piv = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                piv = i; break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(r + 1, len(M)):
            if M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r

def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))

out = []
def say(s):
    out.append(s); print(s, flush=True)

# ---------------------------------------------------------------- part A
say('PART A: exported matrices and bases')
A6 = fr(EX['high_input']['matrix']); A9 = fr(EX['high_graph']['matrix'])
N32 = fr(EX['high_input']['basis_columns']); N29 = fr(EX['high_graph']['basis_columns'])
say('shapes: input %dx%d, graph %dx%d, input basis %d x %d, graph basis %d x %d' % (
    len(A6), len(A6[0]), len(A9), len(A9[0]), len(N32), len(N32[0]), len(N29), len(N29[0])))
say('row labels input: %s' % EX['high_input']['rows'])
say('row labels graph: %s' % EX['high_graph']['rows'])
rev = list(range(37, -1, -1))
say('rank(input matrix)  natural order = %d, reversed order = %d' % (rank(A6), rank(A6, rev)))
say('rank(graph matrix)  natural order = %d, reversed order = %d' % (rank(A9), rank(A9, rev)))
bad6 = sum(1 for v in N32 for row in A6 if dot(row, v) != 0)
bad9 = sum(1 for v in N29 for row in A9 if dot(row, v) != 0)
badc = sum(1 for v in N29 for row in A6 if dot(row, v) != 0)
say('nonzero A6*v over 32 input vectors: %d (of %d identities)' % (bad6, 6 * 32))
say('nonzero A9*v over 29 graph vectors: %d (of %d identities)' % (bad9, 9 * 29))
say('nonzero A6*v over 29 graph vectors (containment): %d (of %d identities)' % (badc, 6 * 29))
say('rank(input basis) = %d, rank(graph basis) = %d' % (rank(N32), rank(N29, rev)))
say('rank(input basis + graph basis) = %d  (32 means graph span inside input span)' % rank(N32 + N29))
# rows of A6 are rows of A9 (graph = input + three sixth-jump rows)
lab6 = [tuple(x) for x in EX['high_input']['rows']]; lab9 = [tuple(x) for x in EX['high_graph']['rows']]
sub = all(A6[i] == A9[lab9.index(l)] for i, l in enumerate(lab6))
say('every input row equals the identically labelled graph row: %s' % sub)
say('rank + nullity: input %d + %d = %d, graph %d + %d = %d' % (
    rank(A6), rank(N32), rank(A6) + rank(N32), rank(A9), rank(N29), rank(A9) + rank(N29)))

# ---------------------------------------------------------------- part B
say('')
say('PART B: independent reconstruction of all jump rows')
kn = [F(x) for x in IN['coarse_knots']]; p = 7; nb = len(kn) - p - 1
say('knots %d, splines %d, degree %d; clamped: %s; interior knots simple: %s' % (
    len(kn), nb, p, kn[:8] == [kn[0]] * 8 and kn[-8:] == [kn[-1]] * 8,
    len(set(kn[8:-8])) == len(kn[8:-8]) and all(kn[i] < kn[i + 1] for i in range(7, len(kn) - 8))))
tm, tp = kn[0], kn[-1]

def pmul_lin(poly, a, b):          # poly * (a*u + b)
    res = [F(0)] * (len(poly) + 1)
    for i, c in enumerate(poly):
        res[i] += b * c; res[i + 1] += a * c
    return res
def padd(x, y):
    n = max(len(x), len(y)); x = x + [F(0)] * (n - len(x)); y = y + [F(0)] * (n - len(y))
    return [a + b for a, b in zip(x, y)]

def span_polys(s, c):
    """Polynomials in u=t-c of all degree-p B-splines on knot span [kn[s],kn[s+1]]."""
    B = {i: ([F(1)] if i == s else [F(0)]) for i in range(len(kn) - 1)}
    for d in range(1, p + 1):
        NB = {}
        for i in range(len(kn) - d - 1):
            acc = [F(0)]
            den1 = kn[i + d] - kn[i]
            if den1 != 0:      # (t-k_i)/den1 = (u + c - k_i)/den1
                acc = padd(acc, pmul_lin(B[i], 1 / den1, (c - kn[i]) / den1))
            den2 = kn[i + d + 1] - kn[i + 1]
            if den2 != 0:      # (k_{i+d+1}-t)/den2
                acc = padd(acc, pmul_lin(B[i + 1], -1 / den2, (kn[i + d + 1] - c) / den2))
            NB[i] = acc
        B = NB
    return [B[i] + [F(0)] * (p + 1 - len(B[i])) for i in range(nb)]

def jets(poly, N=8):
    return [poly[n] * factorial(n) if n < len(poly) else F(0) for n in range(N)]

left = [jets(q) for q in span_polys(7, tm)]          # derivatives at t_minus+
right = [jets(q) for q in span_polys(len(kn) - p - 2, tp)]   # derivatives at t_plus-
# partition of unity on both spans
pu = all(sum((left[i][0] for i in range(nb)), F(0)) == 1 for _ in [0]) and \
     sum((right[i][0] for i in range(nb)), F(0)) == 1
def order(j):
    return next((n for n, x in enumerate(j) if x != 0), None)
lo = [order(left[i]) for i in range(nb)]; ro = [order(right[i]) for i in range(nb)]
say('partition of unity at both ends: %s' % pu)
say('left vanishing orders b_0..b_7: %s; b_8..b_33 vanish to order >=8 at t_minus: %s' % (
    lo[:8], all(o is None for o in lo[8:])))
say('right vanishing orders b_26..b_33: %s; b_0..b_25 vanish to order >=8 at t_plus: %s' % (
    ro[26:], all(o is None for o in ro[:26])))

# inner C3 matching (own Vandermonde solve) and inner powers
e = [F(2 * j) for j in range(1, 8)]
def solve(Mt, rhs):
    n = len(Mt); A = [list(Mt[i]) + [rhs[i]] for i in range(n)]
    for c in range(n):
        pv = next(i for i in range(c, n) if A[i][c] != 0); A[c], A[pv] = A[pv], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]; A[i] = [x - f * y for x, y in zip(A[i], A[c])]
    return [A[i][n] for i in range(n)]
V4 = [[e[j] ** n for j in range(4)] for n in range(4)]
D = []
for i in range(4):
    D.append(solve(V4, left[i][:4]) + [F(0)] * 3)
for qq in range(4, 7):
    row = [F(0)] * 7; row[qq] = F(1)
    for j in range(4):
        L = F(1)
        for l in range(4):
            if l != j:
                L *= (e[qq] - e[l]) / (e[j] - e[l])
        row[j] = -L
    D.append(row)
say('own inner coefficients equal 239 export: %s' % (D == [[F(x) for x in r] for r in IN['inner_coefficients']]))

# outer exponents from the topic235 pair list and the exact k
k = F(IN['k'])
pairs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (0, 1), (1, 1), (2, 1), (0, 2)]
al = [k - 3 - j * (1 - k) - 2 * l for j, l in pairs]
say('k = %s, 0<k<1/4: %s; own outer exponents equal 239 export: %s; alpha_1..9 distinct: %s' % (
    k, 0 < k < F(1, 4), al == [F(x) for x in IN['outer_exponents']], len(set(al[1:])) == 9))
BO = []
for qq in range(5, 10):
    row = [F(0)] * 10; row[qq] = F(1)
    for i in range(1, 5):
        L = F(1)
        for j in range(1, 5):
            if j != i:
                L *= (al[qq] - al[j]) / (al[i] - al[j])
        row[i] = -L
    BO.append(row)
say('own outer Lagrange rows equal 239 export: %s' % (BO == [[F(x) for x in r] for r in IN['outer_B']]))

# jump rows J_(v,n)[col], unscaled
fin = {i: i for i in range(4)}; fin.update({i: i - 3 for i in range(7, 33)})
def J(v, n):
    row = [F(0)] * 38
    if v == 'minus':
        for c, b in fin.items():
            row[c] += left[b][n]
        for c in range(7):
            row[c] -= sum((D[c][j] * e[j] ** n for j in range(7)), F(0))
    elif v == 'plus':
        for c, b in fin.items():
            row[c] -= right[b][n]
    else:
        for m in range(5):
            row[33 + m] = sum((BO[m][j] * al[j] ** n for j in range(10)), F(0))
    return row
C3 = all(x == 0 for v in ('minus', 'plus', 'outer') for n in range(4) for x in J(v, n))
say('all 38 columns C3 at t_minus, t_plus, t_J (jumps of order 0..3 vanish): %s' % C3)
sc = [F(x) for x in IN['scales']]
say('scales from 239 equal 240 export and all positive: %s' % (
    sc == [F(x) for x in EX['scales']] and all(s > 0 for s in sc)))
S = lambda row: [x / s for x, s in zip(row, sc)]
R6 = [S(J(v, n)) for v in ('minus', 'plus', 'outer') for n in (4, 5)]
R9 = [S(J(v, n)) for v in ('minus', 'plus', 'outer') for n in (4, 5, 6)]
say('rebuilt 6x38 matrix equals exported high_input matrix entrywise: %s' % (R6 == A6))
say('rebuilt 9x38 matrix equals exported high_graph matrix entrywise: %s' % (R9 == A9))
supp = {v: sorted({c for n in (4, 5, 6) for c, x in enumerate(J(v, n)) if x != 0}) for v in ('minus', 'plus', 'outer')}
say('column supports of order-4..6 rows: %s' % supp)
say('supports pairwise disjoint: %s' % (not (set(supp['minus']) & set(supp['plus'])) and
                                        not (set(supp['minus']) & set(supp['outer'])) and
                                        not (set(supp['plus']) & set(supp['outer']))))
for v, cols in (('minus', [7, 8, 9]), ('plus', [32, 31, 30])):
    M = [[J(v, n)[c] for c in cols] for n in (4, 5, 6)]
    tri = all(M[a][b] == 0 for a in range(3) for b in range(3) if b > a) and all(M[a][a] != 0 for a in range(3))
    say('%s rows on columns %s lower triangular with nonzero diagonal: %s' % (v, cols, tri))
O = [[J('outer', n)[c] for c in range(33, 38)] for n in (4, 5, 6)]
say('outer block ranks: orders 4-5 -> %d, orders 4-6 -> %d' % (rank(O[:2]), rank(O)))
for v in ('minus', 'plus', 'outer'):
    say('%s block ranks (scaled): orders 4-5 -> %d, orders 4-6 -> %d' % (
        v, rank([S(J(v, n)) for n in (4, 5)]), rank([S(J(v, n)) for n in (4, 5, 6)])))
# monic interpolation error check of 235: J_4 = P(alpha_q)
Pq = [F(1) for _ in range(5)]
for m in range(5):
    for i in range(1, 5):
        Pq[m] *= (al[5 + m] - al[i])
say('outer fourth jumps equal P(alpha_q) of topic235: %s' % (O[0] == Pq))
say('rank(rebuilt input) = %d, rank(rebuilt graph) = %d' % (rank(R6, rev), rank(R9)))
# seventh jumps are not needed but are reported for completeness
say('seconds: %.3f' % (time.monotonic() - T0))
