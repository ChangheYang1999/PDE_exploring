"""Independent exact-rational recheck of topic246 (fractions only, no arb).
Reads the 239 Gram/strain endpoint data, 240 constraints, 242 cvec and the
exported 246 dyadic whiteners. Re-derives eps, D^2, A^2 rigorously."""
import json, hashlib, time
from fractions import Fraction as F
from pathlib import Path
P = Path('verification/proofs')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
t0 = time.monotonic()
for p, h in [(P/'239_s1j1_full_input/evidence/check.json', 'c6d2e2c862f5023e90f24bb8ec550e655ea75e153ba9ccf22abb9f2599079858'),
             (P/'240_s1j1_high_intersections/evidence/exact_constraints.json', '96f271d72ec6190011166d747dff391d783cedff8203b97eb31a87f49bc05344'),
             (P/'242_s1j1_completed_audit/evidence/source/meta.json', 'bd16b7d2bd321e4e931016354ab3e08b5235a9f06e186587b6ed108bc86913f7'),
             (P/'246_exact_strain_hyperplane/evidence/dyadic_whiteners.json', 'a6eb01a6ef45a3d08cb949e7955e1e0ccc2aaa49ebf097f84f9f561175f01087')]:
    assert sha(p) == h, p
cert = json.loads((P/'239_s1j1_full_input/evidence/check.json').read_text())
con = json.loads((P/'240_s1j1_high_intersections/evidence/exact_constraints.json').read_text())
meta = json.loads((P/'242_s1j1_completed_audit/evidence/source/meta.json').read_text())
wh = json.loads((P/'246_exact_strain_hyperplane/evidence/dyadic_whiteners.json').read_text())
def ends(d): return [F(int(d[k][0])) * F(2)**int(d[k][1]) for k in ('lo_binary', 'hi_binary')]
run = cert['runs'][1]; assert run['precision_bits'] == 640
N = 38
Glo = [[ends(v)[0] for v in row] for row in run['scaled_input_Gram']]
Ghi = [[ends(v)[1] for v in row] for row in run['scaled_input_Gram']]
alo = [ends(v)[0] for v in run['exact_scaled_strain']]
ahi = [ends(v)[1] for v in run['exact_scaled_strain']]
assert all(Glo[i][j] <= Ghi[i][j] for i in range(N) for j in range(N))
# symmetry of enclosures (overlap)
assert all(max(Glo[i][j], Glo[j][i]) <= min(Ghi[i][j], Ghi[j][i]) for i in range(N) for j in range(N))
Gm = [[(Glo[i][j]+Ghi[i][j])/2 for j in range(N)] for i in range(N)]
Gr = [[(Ghi[i][j]-Glo[i][j])/2 for j in range(N)] for i in range(N)]
am = [(alo[i]+ahi[i])/2 for i in range(N)]; ar = [(ahi[i]-alo[i])/2 for i in range(N)]
b = [F.from_float(float(x)) for x in meta['cvec']]
assert alo[13] > 0 and b[13] > 0 and meta['new'][13][1] == 'sp10'
print('a13 lo', float(alo[13]), 'b13', b[13], 'max |a-b| entry', float(max(max(abs(alo[i]-b[i]), abs(ahi[i]-b[i])) for i in range(N))))
def up(x, bits=80):
    # rational upper bound of nonnegative x by a short dyadic
    x = F(x); assert x >= 0
    if x == 0: return F(0)
    e = x.numerator.bit_length() - x.denominator.bit_length() - bits
    y = x * F(2)**(-e)
    n = -((-y.numerator) // y.denominator)  # ceil(y)
    r = F(n) * F(2)**e; assert r >= x; return r
def rank(M):
    M = [list(r) for r in M]; rk = 0; cols = len(M[0]) if M else 0
    for c in range(cols):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]; M[i] = [M[i][k] - f*M[rk][k] for k in range(cols)]
        rk += 1
    return rk
out = {}
for name, n in [('whole', 38), ('high_input', 32), ('high_graph', 29)]:
    if name == 'whole':
        Q = [[F(int(i == j)) for j in range(N)] for i in range(N)]
    else:
        A = [[F(x) for x in row] for row in con[name]['matrix']]
        cols = [[F(x) for x in v] for v in con[name]['basis_columns']]
        assert len(cols) == n and all(len(v) == N for v in cols)
        assert all(sum(A[r][k]*v[k] for k in range(N)) == 0 for r in range(len(A)) for v in cols)
        assert all(A[r][13] == 0 for r in range(len(A)))
        rA = rank(A); rQ = rank(cols)
        assert rA == N - n and rQ == n, (rA, rQ)
        Q = [[cols[j][i] for j in range(n)] for i in range(N)]
    T = [[F(x) for x in row] for row in wh[name]]
    assert len(T) == n and all(len(r) == n for r in T)
    assert all(t.denominator & (t.denominator - 1) == 0 for r in T for t in r)  # dyadic
    QT = [[sum(Q[i][k]*T[k][j] for k in range(n) if Q[i][k] and T[k][j]) for j in range(n)] for i in range(N)]
    GQT = [[sum(Gm[i][k]*QT[k][j] for k in range(N) if QT[k][j]) for j in range(n)] for i in range(N)]
    M = [[sum(QT[k][i]*GQT[k][j] for k in range(N) if QT[k][i]) - int(i == j) for j in range(n)] for i in range(n)]
    aQT = [[up(abs(x)) for x in row] for row in QT]
    Gru = [[up(x) for x in row] for row in Gr]
    RQ = [[sum(Gru[i][k]*aQT[k][j] for k in range(N)) for j in range(n)] for i in range(N)]
    Rad = [[sum(aQT[k][i]*RQ[k][j] for k in range(N)) for j in range(n)] for i in range(n)]
    eps = max(sum(abs(M[i][j]) + Rad[i][j] for j in range(n)) for i in range(n))
    assert eps < 1
    # ell = (QT)^T a and (QT)^T (a-b), midpoint +- radius
    la = [sum(QT[k][i]*am[k] for k in range(N)) for i in range(n)]
    lar = [sum(aQT[k][i]*up(ar[k]) for k in range(N)) for i in range(n)]
    ld = [sum(QT[k][i]*(am[k]-b[k]) for k in range(N)) for i in range(n)]
    A2lo = sum(max(F(0), abs(la[i]) - lar[i])**2 for i in range(n)) / (1 + eps)
    D2hi = sum((abs(ld[i]) + lar[i])**2 for i in range(n)) / (1 - eps)
    d2 = D2hi / A2lo
    ok = (D2hi < F(3253, 10**20)**2, A2lo > F(52024, 10**6)**2, d2 < F(6244, 10**19)**2)
    print(name, 'n', n, 'eps<=%.3e' % float(eps), 'D<=%.12e' % float(D2hi)**0.5, 'A>=%.12e' % float(A2lo)**0.5,
          'delta<=%.12e' % float(d2)**0.5, 'checks', ok, 'kernel dims', n-1, flush=True)
    assert all(ok)
    out[name] = dict(n=n, eps=float(eps), D=float(D2hi)**0.5, A=float(A2lo)**0.5, delta=float(d2)**0.5)
print('ALL PASS', round(time.monotonic()-t0, 2), 's')
