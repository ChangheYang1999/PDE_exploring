"""Independent numerical review of T4-182 (c1-t1 R1-021): the rational span probe for candidate 007.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4182.py > check_T4182.out

Weak test (T4-172 / c1-t2 T2-W4, analytic statement AUDITED): a = 0, w = 1, C_U = 1, phi = y W^2 P(t),
t = r^2/(1+r^2), W = 1 - t, P = sum_k p_k t^k with T4's frozen rational coefficients. Then every S1 correction h with
F(rho + h; c) = 0 has ||h||_2 >= 2|I|/(D + sqrt(D^2 + 4 H |I|)), I = int F(rho) phi, D = ||M_phi||_2 + ||phi |D rho| ||_2,
M_phi = (2c+1) phi + (cX + U[rho]).D phi, H = sup |D phi| = sup_t W^2 max(|P|, |(1-4t)P + 2tW P'|).

Independence from T4: the fields are built from the c1-n1 generator snapshot
  candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json
with the code of c1-t2 artifacts/arith/weighted_weak_sharp.py (sections (2) and (3): Top, legendre_shift, load, build,
the exact M and C quadratic forms GM, GC and the exact pairing), copied with the file name changed.  T4 builds its fields
from its own canonical file (c1-t4 research/projected_laplacian/data/candidate007_canonical.json) with its own code.
The sup H is certified here by an own adaptive bisection (second-order mean value bounds), not by either peer's grid.
Inputs (copies, sha256 checked): data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json = the snapshot above;
data/T4182_a0.json = c1-t4 research/optimized_probe_007/verification/a0.json (frozen coefficients, values compared).
"""
import hashlib
import json
import sys
import time
from pathlib import Path

from flint import arb, arb_poly, ctx, fmpq, fmpq_poly

sys.set_int_max_str_digits(0)
T0 = time.monotonic()
SNAP = Path("data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json")
T4JSON = Path("data/T4182_a0.json")
T4_SHA = "b5b510bbabe556d2e07008473d9d92eb7098bac38cc36955cac0799bd0de425e"
SNAP_SHA = "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(SNAP) == SNAP_SHA
print(f"snapshot sha256 {SNAP_SHA} (matches c1-t2 t4_094_review.py header)")
assert sha(T4JSON) == T4_SHA
print(f"T4 a0.json sha256 {T4_SHA}")
T4 = json.loads(T4JSON.read_text())


def a4(n, m):   # alpha(n, m) / (pi/4) for n, m >= 1
    return 2 * (n == m) - (abs(n - m) == 2) + (n + m == 2)


def b4(n, m):   # beta(n, m) / (pi/4) for n, m >= 1
    return 2 * (n == m) - (abs(n - m) == 2) - (n + m == 2)


# ---------------- copied from c1-t2 weighted_weak_sharp.py section (2) ----------------
tp = fmpq_poly([0, 1])
Wq = fmpq_poly([1, -1])


def Top(P, beta, e):
    return fmpq_poly([e, -2 * beta]) * P + 2 * tp * Wq * P.derivative()


def legendre_shift(n):          # P_n(2t - 1)
    xx = fmpq_poly([-1, 2])
    p0, p1 = fmpq_poly([1]), xx
    if n == 0:
        return p0
    for m in range(1, n):
        p0, p1 = p1, (fmpq(2 * m + 1, m + 1) * xx * p1 - fmpq(m, m + 1) * p0)
    return p1


def addto(d, key, P):
    d[key] = d.get(key, fmpq_poly([0])) + P


def load():
    d = json.loads(SNAP.read_text())
    c = fmpq(*map(int, d.get("cl", d.get("cl_exact")).split("/")))
    chi = {}
    for g in d["generators"]:
        num, den = (g["coef"].split("/") + ["1"])[:2]
        co = fmpq(int(num), int(den))
        sp_ = g["spec"]
        if sp_[0] == "mono":
            T = tp**sp_[1]
        else:
            assert sp_[0] == "leg"
            T = tp**sp_[1] * legendre_shift(sp_[2])
        addto(chi, (g["j"], 2 * g["m"]), co * tp**g["m"] * T)
    return c, chi


def build(c, chi):
    delta = 1 - 1 / c
    beta = lambda j: -(3 + 1 / c - j * delta) / 2       # W^(-p_j)
    lapc = {}
    for (j, n), P in chi.items():                        # e = 0 -> -2
        TP = Top(P, beta(j), 0)
        addto(lapc, (j, n), Top(TP, beta(j), 0) - n * n * P)

    def dy_cos(cd, e):
        out = {}
        for (j, n), P in cd.items():
            TP = Top(P, beta(j), e)
            addto(out, (j, n + 1), fmpq(1, 2) * (TP - n * P))
            if n - 1 > 0:
                addto(out, (j, n - 1), fmpq(-1, 2) * (TP + n * P))
            elif n - 1 < 0:
                addto(out, (j, 1), fmpq(1, 2) * (TP + n * P))
        return out

    def dx_cos(cd, e):
        out = {}
        for (j, n), P in cd.items():
            TP = Top(P, beta(j), e)
            addto(out, (j, n + 1), fmpq(1, 2) * (TP - n * P))
            addto(out, (j, abs(n - 1)), fmpq(1, 2) * (TP + n * P))
        return out

    rho3 = dy_cos(lapc, -2)                                # -rho, at e = -3
    psi2 = dy_cos(dx_cos(chi, 0), -1)                      # psi = chi_xy, at e = -2
    t2 = tp * tp
    R, S = {}, {}
    for key, P in rho3.items():
        q, rem = divmod(-P, t2)
        assert rem == 0, ("rho not divisible by t^2", key)
        if q != 0:
            R[key] = q
    for key, P in psi2.items():
        q, rem = divmod(P, t2)
        assert rem == 0, ("psi not divisible by t^2", key)
        if q != 0:
            S[key] = q
    for j in {j for j, _ in list(R) + list(S)}:
        assert beta(j) + 2 == (j + 1) * delta / 2          # r^-3 W^beta = r W^(beta+2) t^-2, beta + 2 = a_j
    return delta, R, S


ctx.prec = 1024
pi = arb.pi()


def A(q):
    q = fmpq(q) if not isinstance(q, fmpq) else q
    return arb(q.p) / arb(q.q)


c, chi = load()
delta, R, S = build(c, chi)
a0 = sum((P(0) for (j, n), P in R.items() if n == 1), fmpq(0))
norm8 = c + 2 * sum((P(0) for (j, n), P in S.items() if n == 2), fmpq(0)) - 1
assert norm8 == 0
assert all(n % 2 == 1 for _, n in R) and all(n % 2 == 0 and n >= 2 for _, n in S)
print(f"(2) C1-N1-007: c = {c}; rho modes {len(R)}, psi modes {len(S)}, max poly degree "
      f"{max(P.degree() for P in list(R.values()) + list(S.values()))}; c + d_y u2(0) = 1 exactly; "
      f"a0 = {A(a0).str(12)} [{time.monotonic() - T0:.1f} s]", flush=True)

_bcache = {}


def bseq(b, Mmax):
    """[B(M, b+1) for M = 0..Mmax] (index 0 unused), recurrence B(M+1, v) = B(M, v) M/(M+v)."""
    have = _bcache.get(b)
    if have is not None and len(have) > Mmax:
        return have
    v = A(b + 1)
    assert b + 1 > 0
    seq = [arb(0), 1 / v]
    for M in range(1, Mmax):
        seq.append(seq[-1] * M / (M + v))
    _bcache[b] = seq
    return seq


def integ(P, K, b):
    """int_0^1 t^K W^b P(t) dt for an arb_poly P (expanded in powers of t)."""
    co = P.coeffs()
    if not co:
        return arb(0)
    seq = bseq(b, K + len(co) + 1)
    return sum((co[l] * seq[K + l + 1] for l in range(len(co))), arb(0))


def to_arb(P):
    return arb_poly([A(q) for q in P.coeffs()]) if P.degree() >= 0 else arb_poly([])


# ---------------- pairing forms (copied from c1-t2 PREP, lin, N0, N1 only) ----------------
aj = lambda j: (j + 1) * delta / 2
Ra = {key: to_arb(P) for key, P in R.items()}
Sa = {key: to_arb(P) for key, P in S.items()}
TSa = {(j, n): to_arb(Top(P, aj(j), 2)) for (j, n), P in S.items()}
lin = {j: Ra[(j, 1)] for (j, n) in Ra if n == 1}
N0, N1 = {}, {}
for (j, m), Sp in Sa.items():
    for (i, n), Rp in Ra.items():
        if abs(n - m) != 1:
            continue
        sg = 1 if n > m else -1
        N0[i + j] = N0.get(i + j, arb_poly([])) + Rp * (Sp * arb_poly([1, -4]) * (sg * m) - TSa[(j, m)])
        N1[i + j] = N1.get(i + j, arb_poly([])) + Rp * Sp * arb_poly([2, -2]) * (sg * m)
print(f"(3) pairing forms prepared [{time.monotonic() - T0:.1f} s]", flush=True)


def pairing(k):
    cA = A(c)
    ell = arb_poly([3 * cA + 1 + 2 * cA * k, -2 * cA * k - 4 * cA])
    lin_v = -pi / 2 * sum((integ(P * ell, k + 1, (j + 1) * delta / 2 - 1) for j, P in lin.items()), arb(0))
    non_v = pi / 4 * sum((integ(N0[J] + N1[J] * k, k + 1, (J + 2) * delta / 2 - 1) for J in N0), arb(0))
    return lin_v + non_v


# ---------------- exact M and C forms (copied from c1-t2 section (3)) ----------------
g0, g1 = fmpq_poly([1, -4]), fmpq_poly([2, -2])
X = {0: {}, 1: {}}
addto(X[0].setdefault(1, {}), 0, fmpq_poly([3 * c + 1, -4 * c]))
addto(X[1].setdefault(1, {}), 0, fmpq_poly([2 * c, -2 * c]))
for (j, m), P in S.items():
    TS = Top(P, aj(j), 2)
    for n, sg in ((m + 1, -1), (m - 1, 1)):
        addto(X[0].setdefault(n, {}), j + 1, fmpq(1, 2) * (TS + sg * m * P * g0))
        addto(X[1].setdefault(n, {}), j + 1, fmpq(1, 2) * (sg * m * P * g1))
Xa = {p: {n: {key: to_arb(P) for key, P in d.items()} for n, d in X[p].items()} for p in (0, 1)}
E = {(0, 0): {}, (0, 1): {}, (1, 1): {}}
for n in set(Xa[0]) | set(Xa[1]):
    for (p, q), Ed in E.items():
        for k1, P1 in Xa[p].get(n, {}).items():
            for k2, P2 in Xa[q].get(n, {}).items():
                Ed[k1 + k2] = Ed.get(k1 + k2, arb_poly([])) + P1 * P2
byn = {}
for (j, n), P in R.items():
    byn.setdefault(n, []).append((j, to_arb(P), to_arb(Top(P, aj(j), 1))))
Ec = {}
for n, lst in byn.items():
    for m in (n - 2, n, n + 2):
        if m < 1 or m not in byn:
            continue
        al, be = a4(n, m), b4(n, m)
        for i, Ri, TRi in lst:
            for j, Rj, TRj in byn[m]:
                Ec[i + j] = Ec.get(i + j, arb_poly([])) + TRi * TRj * al + Ri * Rj * (n * m * be)
print(f"(3) exact M and C forms prepared [{time.monotonic() - T0:.1f} s]", flush=True)


def GM(a, k1, k2):
    tot = arb(0)
    for key in set(E[(0, 0)]) | set(E[(0, 1)]) | set(E[(1, 1)]):
        P = E[(0, 0)].get(key, arb_poly([])) + E[(0, 1)].get(key, arb_poly([])) * (k1 + k2) \
            + E[(1, 1)].get(key, arb_poly([])) * (k1 * k2)
        b = 1 - a + key * delta / 2
        assert b > -1
        tot += integ(P, k1 + k2 + 1, b)
    return pi / 2 * tot


def GC(a, k1, k2):
    return pi / 8 * sum((integ(P, k1 + k2 + 1, 1 - a + (J + 2) * delta / 2) for J, P in Ec.items()), arb(0))


# ---------------- (4) checks against confirmed single-probe values ----------------
I0 = pairing(0)
n4_091_k0 = arb("0.00015509843384403807441") # N4-091, CONFIRMED by T4 (printed to 20 digits)
print(f"(4) pairing k = 0: {I0.str(25)}; N4-091 (CONFIRMED) 0.00015509843384403807441;"
      f" |difference| {abs(I0 - n4_091_k0).str(3)}")
assert abs(I0 - n4_091_k0) < arb("1e-22")

# ---------------- (5) T4's frozen vector ----------------
a = fmpq(0)
coef = {int(k): fmpq(*map(int, (v.split("/") + ["1"])[:2])) for k, v in T4["probe_coefficients"].items()}
Ks = sorted(coef)
print(f"(5) frozen probe: {len(Ks)} powers {Ks}")
cA = [A(coef[k]) for k in Ks]
f = [pairing(k) for k in Ks]
nK = len(Ks)
Gm = [[None] * nK for _ in range(nK)]
Gc = [[None] * nK for _ in range(nK)]
for i in range(nK):
    for j in range(i, nK):
        Gm[i][j] = Gm[j][i] = GM(a, Ks[i], Ks[j])
        Gc[i][j] = Gc[j][i] = GC(a, Ks[i], Ks[j])
print(f"    Gram matrices done [{time.monotonic() - T0:.1f} s]", flush=True)
I = sum((cA[i] * f[i] for i in range(nK)), arb(0))
M2 = sum((cA[i] * cA[j] * Gm[i][j] for i in range(nK) for j in range(nK)), arb(0))
C2 = sum((cA[i] * cA[j] * Gc[i][j] for i in range(nK) for j in range(nK)), arb(0))
assert M2 > 0 and C2 > 0
Mn, Cn = M2.sqrt(), C2.sqrt()
cmp = {}
for lab, mine in (("pairing", I), ("M", Mn), ("C", Cn)):
    theirs = arb(T4[lab].strip("[]").split("+/-")[0].strip(), T4[lab].strip("[]").split("+/-")[1].strip())
    cmp[lab] = mine.overlaps(theirs)
    print(f"    {lab:8s} c1-t1 {mine.str(30)}\n             T4    {theirs.str(30)}  overlap {cmp[lab]};"
          f" |difference| {abs(mine - theirs).str(3)}")
assert all(cmp.values())

# ---------------- (6) own certificate for H = sup_t W^2 max(|P|, |Q|) ----------------
ctx.prec = 256
Pp = fmpq_poly([0])
for k, q in coef.items():
    Pp += q * tp**k
Qp = fmpq_poly([1, -4]) * Pp + 2 * tp * Wq * Pp.derivative()
polys = [(to_arb(Z), to_arb(Z.derivative()), to_arb(Z.derivative().derivative())) for Z in (Pp, Qp)]
H_target = fmpq(*map(int, T4["H_upper_exact"].split("/")))


def cell_bound(lo, hi):
    """Upper bound of W^2 max(|P|, |Q|) on [lo, hi]: W^2 <= (1 - lo)^2 and |Z(t)| <= |Z(m)| + r|Z'(m)| + r^2/2 sup|Z''|."""
    m, r = (lo + hi) / 2, (hi - lo) / 2
    mA, rA = A(m), A(r)
    ball = arb(mA, rA * (1 + arb(2) ** -100))
    bnd = [abs(Z(mA)) + rA * abs(dZ(mA)) + rA * rA / 2 * abs(d2Z(ball)) for Z, dZ, d2Z in polys]
    return A((1 - lo) ** 2) * max(b.upper() for b in bnd)


stack, accepted, maxub = [(fmpq(0), fmpq(1))], 0, arb(0)
while stack:
    lo, hi = stack.pop()
    ub = cell_bound(lo, hi)
    if ub < A(H_target):
        accepted += 1
        maxub = max(maxub, ub)
    else:
        assert hi - lo > fmpq(1, 2**44), (lo, hi)
        mid = (lo + hi) / 2
        stack += [(lo, mid), (mid, hi)]
    assert accepted < 200000
print(f"(6) sup_t W^2 max(|P|, |Q|) < T4's H_upper_exact = {H_target} = {A(H_target).str(10)}: CERTIFIED on"
      f" {accepted} cells (largest cell bound {maxub.str(10)}) [{time.monotonic() - T0:.1f} s]", flush=True)
NS = 20000
lowH = max(max(abs(Z(A(fmpq(i, NS)))) for Z, _, _ in polys) * A((1 - fmpq(i, NS)) ** 2) for i in range(NS + 1))
print(f"    sampled lower value on t = i/{NS}: {lowH.str(10)} (T4 sample {T4['H_certificate']['lower_sample']})")
ctx.prec = 1024

# ---------------- (7) radius ----------------
H = A(H_target)
D = Mn + Cn
Iabs = abs(I)
rad = 2 * Iabs / (D + (D * D + 4 * H * Iabs).sqrt())
floor_T4 = fmpq(*map(int, T4["strict_lower_exact"].split("/")))
print(f"(7) D = {D.str(20)}, H <= {H.str(10)}, radius {rad.str(30)}")
print(f"    radius > T4 strict floor {floor_T4} = {A(floor_T4).str(12)}: {rad > A(floor_T4)}")
assert rad > A(floor_T4)
print(f"    ratio to N4-091 4.3987003470e-5: {(rad / arb('4.3987003470e-5')).str(6)}")
for lab, b in (("FW-T-TB-sharp-v1", "3.7930e-6"), ("FW-T-T4L2-sharpw-v1", "2.8496e-6"),
               ("graded boxes (NC-T-GRADED-L2)", "4.5717e-4")):
    print(f"    distance / budget {lab}: {(rad / arb(b)).str(6)}")
out = dict(review="R1-021 (T4-182)", snapshot_sha256=SNAP_SHA, t4_json_sha256=sha(T4JSON), pairing=I.str(40),
           M=Mn.str(40), C=Cn.str(40), H_certified_below=str(H_target), H_cells=accepted, radius=rad.str(40),
           exceeds_T4_floor=bool(rad > A(floor_T4)), overlaps=cmp, seconds=time.monotonic() - T0)
Path("check_T4182.json").write_text(json.dumps(out, indent=1))
print(f"done [{time.monotonic() - T0:.1f} s]")
