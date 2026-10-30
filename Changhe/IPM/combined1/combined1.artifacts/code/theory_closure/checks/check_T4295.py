"""c1-t1 R1-034 review of T4-295 (c1-t4 research/forced_integrable_tail, section 3): exact cancellation of the (4,1)
residual sector of 007, 013 and 014 by a branch-3 potential correction, and a check of c1-t2 REVIEW_T4_281 R2.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4295.py > check_T4295.out

Independent of c1-t4 code and of its canonical files and sector tables.  The fields are built exactly (fmpq) from the
raw c1-n1 generator snapshots with the c1-t2 constructor copied in check_T4182.py: chi = sum_j W^(-p_j) P_jm(t)
cos(m theta) (m even), rho = r W^(a_j) R_jn(t) sin(n theta), psi = r^2 W^(a_j) S_jm(t) sin(m theta), W = 1 - t,
t = r^2/(1 + r^2), a_j = (j + 1) delta/2, p_j = (3 + gamma - j delta)/2.
Part A: own far-field sector expansion.  With z = r^-2, W = z/(1 + z) and t = 1/(1 + z), the z^q coefficient of
(1 + z)^(-a_j) R_jn(1/(1 + z)) is the density sector (l, q) = (j + 1, q) at r^(1 - l delta - 2q), and likewise for psi
at r^(2 - l delta - 2q).  The residual F = c r d_r rho - rho + (1/r)(psi_r rho_theta - psi_theta rho_r) (U = (-psi_y,
psi_x), psi = chi_xy) is expanded sector by sector for every exponent >= -7/2 and compared with the c1-n1 sector
tables (all 16 rows: exact status, maximal harmonic, FLOAT coefficients).
Part B: the T4-295 correction.  For branch j = 3, p = p_3, A1_m = p P_m(1) - P_m'(1) and chi_3m -> chi_3m - A1_m
t^(m/2 + 4)(1 - t) (cos(m theta), m = 2k, so t^(k+4)).  Rebuild rho and psi, recheck the branch jets, the origin
orders, the residual sectors (all exponents >= -7/2), and compare A1 and the sector records with the c1-t4 data files.
Part C: REVIEW_T4_281 R2: F_(1,2) = -4c Theta_(1,2), and the circle L2 residual of F_(1,2) after the best multiple of
P = gamma cos(2 theta) Theta_0 + sin(2 theta) Theta_0', before and after the correction.  Writes no file.
"""
import hashlib
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

exec(compile(Path("check_T4182.py").read_text().split("# ---------------- pairing forms (copied from c1-t2 PREP")[0],
             "h", "exec"))

ok = True
QMAX = 2
ECUT = Fr(-7, 2)
F_ = lambda q: Fr(int(q.p), int(q.q))
CANDS = [("007", "data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json",
          "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21",
          "data/c1n1_007_sector_table.json", "9d54471429323126d6270de5779ef6566f6753a1ce943bee65073be75b68f42a",
          "data/T4295_007_tail_repair.json", "bad9b06a64a3f045e3de487d63793f8ec0c6b021a692c5e11cea91279ed5fcd6"),
         ("013", "data/c1n1_013_pairU_m16_exact.json",
          "c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940",
          "data/c1n1_013_sector_table.json", "bac5f78f424fa812c82f17e385a22ed0a6313039311c4b5b19a4f756e3e7d0a5",
          "data/T4295_013_tail_repair.json", "5485a201200fe4cdd57560775c32c0e09938a06f352127a605a780dceaa1c0e4"),
         ("014", "data/c1n1_014_pairB_m16_exact.json",
          "8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746",
          "data/c1n1_014_sector_table.json", "b1f237688d61cf98fb4f07ea9bddaf9beaa7c18fa8a443a86192a3a9ec74d0b7",
          "data/T4295_014_tail_repair.json", "b69aa6a844b89409b92c6e3c94de220289a6f6c486b7d5e3e6a8c91b1327999d")]


def put(d, n, v):
    if n == 0 or v == 0:
        return
    if n < 0:
        n, v = -n, -v
    d[n] = d.get(n, fmpq(0)) + v
    if d[n] == 0:
        del d[n]


_bn = {}


def bneg(b, k):                      # coefficient of z^k in (1 + z)^(-b)
    key = (b, k)
    if key not in _bn:
        v = fmpq(1)
        for i in range(k):
            v = v * (-b - i) / (i + 1)
        _bn[key] = v
    return _bn[key]


def zco(P, a):                       # z^q coefficients, q <= QMAX, of (1 + z)^(-a) P(1/(1 + z))
    co = P.coeffs()
    return [sum((p * bneg(a + i, k) for i, p in enumerate(co) if p != 0), fmpq(0)) for k in range(QMAX + 1)]


def sectors(delta, R, S):
    Th, Ps = {}, {}
    for src, dst in ((R, Th), (S, Ps)):
        for (j, n), P in src.items():
            for q, v in enumerate(zco(P, (j + 1) * delta / 2)):
                if v != 0:
                    dst.setdefault((j + 1, q), {})[n] = v
    return Th, Ps


def residual(c, delta, Th, Ps):
    ex = lambda l, q: 1 - l * delta - 2 * q
    F = {}
    for l in range(1, 17):
        for q in range(QMAX + 1):
            e = ex(l, q)
            if F_(e) < ECUT:
                continue
            out = {}
            for n, v in Th.get((l, q), {}).items():
                put(out, n, (c * e - 1) * v)
            for l1 in range(1, l):
                for q1 in range(q + 1):
                    A_, B_ = Ps.get((l1, q1)), Th.get((l - l1, q - q1))
                    if not A_ or not B_:
                        continue
                    s1, e2 = ex(l1, q1) + 1, ex(l - l1, q - q1)
                    for m, a in A_.items():
                        for n, b in B_.items():
                            ab = a * b / 2
                            put(out, m + n, ab * (s1 * n - e2 * m))
                            put(out, m - n, ab * (s1 * n + e2 * m))
            F[(l, q)] = (e, out)
    return F


def l2(d):                           # circle L2 norm of sum d_n sin(n theta)
    return math.sqrt(math.pi * sum(float(F_(v)) ** 2 for v in d.values()))


def r2_fit(c, Th, F):                # REVIEW_T4_281 R2: F_(1,2) against P = gamma cos2t Theta0 + sin2t Theta0'
    gam = 1 / c
    P = {}
    for n, v in Th[(1, 0)].items():
        put(P, n + 2, gam * v / 2)
        put(P, n - 2, gam * v / 2)
        put(P, n + 2, n * v / 2)
        put(P, n - 2, -n * v / 2)
    e12, F12 = F[(1, 2)]
    T12 = Th.get((1, 2), {})
    lin = all(F12.get(n, 0) == (c * e12 - 1) * T12.get(n, 0) for n in set(F12) | set(T12))
    pp = sum((v * v for v in P.values()), fmpq(0))
    lam = sum((P[n] * F12.get(n, 0) for n in P), fmpq(0)) / pp
    res = {n: F12.get(n, 0) - lam * P.get(n, 0) for n in set(F12) | set(P)}
    return lin, c * e12 - 1 == -4 * c, float(F_(lam)), l2(F12), l2(P), l2(res) / l2(F12)


for name, snap, ssha, tab, tsha, rep, rsha in CANDS:
    SNAP = Path(snap)
    assert sha(SNAP) == ssha and sha(Path(tab)) == tsha and sha(Path(rep)) == rsha
    c, chi = load()
    delta, R, S = build(c, chi)
    gam = 1 / c
    ex = lambda l, q: 1 - l * delta - 2 * q
    print(f"== {name}: c = {c}; potential modes {len(chi)}, density modes {len(R)}, stream modes {len(S)}")
    # ---------------- Part A ----------------
    Th, Ps = sectors(delta, R, S)
    F = residual(c, delta, Th, Ps)
    tabd = json.loads(Path(tab).read_text())
    okA = len(tabd["rows"]) == len(F)
    worst = 0.0
    for row in tabd["rows"]:
        hit = [k for k, (e, _) in F.items() if F_(e) == Fr(row["exponent_exact"])]
        if len(hit) != 1:
            okA = False
            continue
        e, out = F[hit[0]]
        st = "EXACT-NONZERO" if out else "EXACT-ZERO"
        okA &= st == row["status"] and (max(out) if out else 0) == row["max_harmonic"]
        cf = {int(k): v for k, v in (row["coefficients_float"] or {}).items()}
        okA &= set(cf) == set(out)
        for n, v in out.items():
            worst = max(worst, abs(float(F_(v)) - cf[n]) / abs(float(F_(v))))
    okA &= worst < 1e-12
    nzA = sorted(((float(F_(e)), k) for k, (e, out) in F.items() if out), reverse=True)
    print(f"A  own residual sectors with exponent >= -7/2: {len(F)}; nonzero: "
          + ", ".join(f"{k} at {x:.4f}" for x, k in nzA))
    print(f"A  agreement with the c1-n1 sector table (16 rows: status, max harmonic, harmonic set): {okA}; largest "
          f"relative difference of FLOAT coefficients {worst:.1e}")
    ok &= okA
    # ---------------- Part B ----------------
    p = (3 + gam - 3 * delta) / 2
    okB = p == 2 * gam
    A1, chi2 = {}, dict(chi)
    for (j, mm), P in chi.items():
        if j != 3:
            continue
        a1 = p * P(fmpq(1)) - P.derivative()(fmpq(1))
        if a1 != 0:
            k = mm // 2
            A1[k] = a1
            chi2[(j, mm)] = P - a1 * tp ** (k + 4) * Wq
    _, R2, S2 = build(c, chi2)
    # T4 data: A1_m and the potential correction -A1 t^(m+4) + A1 t^(m+5)
    T4 = json.loads(Path(rep).read_text())
    t4A1 = {int(x["m"]): Fr(x["A1"]) for x in T4["moment_checks"]}
    t4corr = {}
    for x in T4["potential_correction"]:
        j, k, d = x["order"]
        t4corr[(j, k, d)] = t4corr.get((j, k, d), 0) + Fr(x["coefficient"])
    mine = {}
    for k, a1 in A1.items():
        mine[(3, k, k + 4)] = -F_(a1)
        mine[(3, k, k + 5)] = F_(a1)
    okT4 = t4A1 == {k: F_(v) for k, v in A1.items()} and t4corr == mine
    print(f"B  p = (3 + gamma - 3 delta)/2 = 2 gamma: {okB}; nonzero A1_m for {len(A1)} potential modes "
          f"m = {min(A1)} .. {max(A1)} (cos(2m theta)); A1 and the correction equal the c1-t4 data file exactly: "
          f"{okT4}")
    same = all(R2.get(kk) == R.get(kk) for kk in set(R) | set(R2) if kk[0] != 3) and \
        all(S2.get(kk) == S.get(kk) for kk in set(S) | set(S2) if kk[0] != 3)
    a3 = 4 * delta / 2
    lead = all(R2.get((3, n), fmpq_poly([0]))(fmpq(1)) == R.get((3, n), fmpq_poly([0]))(fmpq(1))
               for n in {n for j, n in list(R) + list(R2) if j == 3}) and \
        all(S2.get((3, n), fmpq_poly([0]))(fmpq(1)) == S.get((3, n), fmpq_poly([0]))(fmpq(1))
            for n in {n for j, n in list(S) + list(S2) if j == 3})
    desc = [n for (j, n), P in list(R2.items()) + list(S2.items())
            if j == 3 and -a3 * P(fmpq(1)) - P.derivative()(fmpq(1)) != 0]

    def val(P):                       # t-adic valuation
        co = P.coeffs()
        return next(i for i, v in enumerate(co) if v != 0) if P != 0 else None
    vr = [val(R2.get((3, n), fmpq_poly([0])) - R.get((3, n), fmpq_poly([0]))) for n in
          {n for j, n in list(R) + list(R2) if j == 3}]
    vs = [val(S2.get((3, n), fmpq_poly([0])) - S.get((3, n), fmpq_poly([0]))) for n in
          {n for j, n in list(S) + list(S2) if j == 3}]
    vr, vs = [v for v in vr if v is not None], [v for v in vs if v is not None]
    print(f"B  branches j != 3 unchanged: {same}; branch-3 leading density and stream coefficients unchanged: {lead}; "
          f"branch-3 first descendants left nonzero: {len(desc)}")
    print(f"B  origin: rho change = r W^a3 t^v (...), min v = {min(vr)} (order >= {2 * min(vr) + 1}); psi change "
          f"= r^2 W^a3 t^v (...), min v = {min(vs)} (order >= {2 * min(vs) + 2}, velocity order >= {2 * min(vs) + 1})")
    okB &= okT4 and same and lead and not desc and min(vr) >= 2 and min(vs) >= 2
    Th2, Ps2 = sectors(delta, R2, S2)
    F2 = residual(c, delta, Th2, Ps2)
    above = [k for k, (e, out) in F2.items() if F_(e) >= -3 and out]
    nz2 = sorted(((F_(e), k) for k, (e, out) in F2.items() if out), reverse=True)
    first = nz2[0]
    eps1 = -3 - first[0]
    print(f"B  after: sectors with exponent >= -3 that are nonzero: {above}; first nonzero sector {first[1]} at "
          f"{first[0]} = {float(first[0]):.12f}, epsilon1 = {eps1} = {float(eps1):.6f}")
    chg = []
    for k in F:
        if F[k][1] != F2[k][1]:
            chg.append(f"{k} ({l2(F[k][1]):.6g} -> {l2(F2[k][1]):.6g})")
    print(f"B  sectors (exponent >= -7/2) changed by the correction, circle L2 before -> after: {', '.join(chg)}")
    t4rec = {(x["K"], x["L"]): (x["residual_zero"], x["nonzero_angular_modes"]) for x in T4["after_residual_sectors"]}
    myrec = {k: (not out, len(out)) for k, (e, out) in F2.items() if k[1] <= 1 and k[0] <= 9}
    okrec = all(t4rec.get(k) == v for k, v in myrec.items())
    print(f"B  c1-t4 after_residual_sectors records ({len(t4rec)}) agree with own expansion on the {len(myrec)} "
          f"common sectors: {okrec}")
    okB &= not above and first[1] == (9, 0) and eps1 > 0 and okrec and F2[(1, 2)] == F[(1, 2)] \
        and F2[(9, 0)] == F[(9, 0)]
    print(f"   (1,2) and (9,0) unchanged exactly: {F2[(1, 2)] == F[(1, 2)] and F2[(9, 0)] == F[(9, 0)]}")
    # ---------------- Part D: size of the reference change ----------------
    # eta = r W^a3 sum_n D_n(t) sin(n theta), D_n(1) = 0; ||eta||_2^2 = (pi/2) sum_n int_0^1 t W^(4 delta - 1) E_n^2 dt,
    # E_n = D_n/(1 - t) (r dr = dt/(2 W^2), r^2 = t/W).
    tot = arb(0)
    for n in {n for j, n in list(R) + list(R2) if j == 3}:
        Dn = R2.get((3, n), fmpq_poly([0])) - R.get((3, n), fmpq_poly([0]))
        if Dn == 0:
            continue
        En, rem = divmod(Dn, Wq)
        assert rem == 0
        tot += integ(to_arb(En * En), 1, 4 * delta - 1)
    nrm = (pi / 2 * tot).sqrt()
    print(f"D  ||eta||_2 = {nrm.str(10)} (the L2 size of the reference change R -> R + eta)")
    # ---------------- Part C ----------------
    for lab, ThX, FX in (("before", Th, F), ("after", Th2, F2)):
        lin, m4c, lam, nF, nP, rel = r2_fit(c, ThX, FX)
        print(f"C  R2 {lab}: F_(1,2) = (c e - 1) Theta_(1,2): {lin}, c e - 1 = -4c: {m4c}; ||F_(1,2)|| = {nF:.6f}, "
              f"||P|| = {nP:.4f}, best lambda = {lam:.1f}, relative residual {rel:.6f}")
        okC = lin and m4c and rel > 0.5
        ok &= okC
    print(f"   checks A {okA}, B {okB}")
    ok &= okB
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
