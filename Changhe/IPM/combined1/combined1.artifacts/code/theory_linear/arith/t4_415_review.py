"""Independent review of T4-415 (c1-t4 research/pointwise_profile_velocity/PROOF.md, sha256 asserted below): the
pointwise-gradient certificate N(z) <= (93/250) G(z) on span(A, 100000 P) for 007, 013 and 014, with T4-422
(research/pointwise_profile_radial_cap/PROOF.md): the retained-shape radial cap with E = 93/250 (reviews/REVIEW_T4_415.md).

Run from artifacts/:  python3 -B -u arith/t4_415_review.py
Needs numpy and python-flint (fmpq, arb). Reads c1-t4's two PROOFs, result.json files, manifests, parameters and the
endpoint JSON files (hash-bound, read only), the lane copy repro/t4_415_audit (its verification/result.json is written
by the copied check.py, see README), and this lane's data/t4_375_review_results.json (Phi(theta*), |U_lead(0)|) and
data/t4_414_review_results.json (the rooms of REVIEW_T4_414).
Parts:
  (A) exact rationals, own code (the complex exponential form of (9) of T4-402, proved mode by mode in
      arith/t4_402_review.py part (A)): cosine coefficients of F_ij = V_q[f_i] . V_q[f_j], f1 = A, f2 = 100000 P; only
      even degrees occur.
  (B) the saved certificate: coverage of [-1/2, 1/2] by the saved projective cells (contiguous, dyadic, widths match
      depths), then the bound (4)-(5) of the PROOF recomputed in Arb with the own F and Q at every saved cell, witness
      and theta cell: every gap positive; minimum gap and its theta cell against result.json; the lane rerun of the
      copied check.py gives the same rows.
  (C) an independent certificate of (1) with other bounds and grids: the exact minimum of c0 + cc cos 2alpha +
      cs sin 2alpha on each alpha arc (no Taylor step in alpha), a two-sided first order term and a ball second order
      term in theta restricted to the cell, own witness list, own theta cells and own adaptive alpha cells.
  (D) the constant: a rigorous lower bound for sup_z N(z)/G(z) at one rational z (no certificate of (1) can use a
      smaller constant), and FLOAT diagnostics of the sup.
  (E) exec of the lane copy repro/t4_415_audit/code/geometry.py (byte-identical to c1-t4's, sha256 asserted; in memory,
      nothing written): its velocity and dot give exactly the own F_ij of (A).
  (F) T4-422: own B, g0, Phi, r0, cap, cap/beta and Ecrit at E = 93/250, V = 0, H0 integer; comparison with its
      result.json, its rational enclosures and its flags; the same caps with V = |U_lead(0)| (not claimed by T4-422).
Output: logs/t4_415_review.log, data/t4_415_review_results.json.
"""
import hashlib
import json
import math
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from flint import arb, ctx, fmpq

HERE = Path(__file__).resolve().parents[1]
R6 = Path("RUN_ROOT")
SRC = R6 / "c1-t4/research/pointwise_profile_velocity"
CAP = R6 / "c1-t4/research/pointwise_profile_radial_cap"
SPV = R6 / "c1-t4/research/profile_specific_velocity"
SHP = R6 / "c1-t4/research/profile_velocity_shape_cap"
REP = HERE / "repro/t4_415_audit"
NAMES = ("007", "013", "014")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# =============================== inputs ===============================
H415 = {"PROOF.md": "57110fd5b3c62f0fa06b6e6194c53e6d9cf1fac091e89a8a3cd514f38ac9fab6",
        "code/check.py": "af67e89181b470eebdcd1eb8487e5cbc1e0a8da8ff91a23b676f9d1de43787ba",
        "code/geometry.py": "4a241764133e76d8d78b56398ebc0d531d80c822c90d9da56444ea4701ef03e6",
        "data/manifest.json": "699627f6b83a9fe10d6faeac7ee2778606d2f5c2ec15e69e842afd53bb969327",
        "verification/result.json": "bd9d38cb021f4009288a1444e55c5d2ca31dbe9477218a0b30695b531d796520"}
H422 = {"PROOF.md": "fb03764b22fd8ab33a6da10b2422d0678a36bc3951fc2fac643204a3f2b45302",
        "code/check.py": "b8c8154955dd5ad8bc5f1ce3efe65648c7468998660623ffe53bb7170242a82c",
        "data/manifest.json": "94d536f049824545992fcc889e0a31870b8a1a7eaeda53dc57ea00a504ca3365",
        "verification/result.json": "2d23b763e2bf9aa1a9caaafd427f61f19a87c8405a54a3216a7c59e3ee301d21"}
for base_, hh in ((SRC, H415), (CAP, H422)):
    for k_, v_ in hh.items():
        assert sha(base_ / k_) == v_, (base_, k_)
MAN = json.loads((SRC / "data/manifest.json").read_text())
MAN2 = json.loads((CAP / "data/manifest.json").read_text())
assert MAN["proof_sha256"] == H415["PROOF.md"] and MAN["geometry_sha256"] == H415["code/geometry.py"]
assert MAN2["proof_sha256"] == H422["PROOF.md"]
for base_, man_ in ((SRC, MAN), (CAP, MAN2)):
    for k_, v_ in man_["inputs"].items():
        assert sha(base_ / k_) == v_, (base_, k_)
RES = json.loads((SRC / "verification/result.json").read_text())
RES2 = json.loads((CAP / "verification/result.json").read_text())
assert (RES["proof_sha256"], RES["code_sha256"], RES["geometry_sha256"], RES["manifest_sha256"]) == \
    (H415["PROOF.md"], H415["code/check.py"], H415["code/geometry.py"], H415["data/manifest.json"])
assert (RES2["proof_sha256"], RES2["code_sha256"], RES2["manifest_sha256"]) == \
    (H422["PROOF.md"], H422["code/check.py"], H422["data/manifest.json"])
# sources: T4-402 (REVIEW_T4_402, AUDITED by T4-413), T4-414 (REVIEW_T4_414), T4-415 itself
assert sha(SRC / "source/profile_PROOF.md") == sha(SPV / "PROOF.md") == \
    "a98e64b04a4ab8f8e46f311c028d55138e9483f761d84e140ed550066e5ab3d9"
assert sha(CAP / "source/T4_414_PROOF.md") == sha(SHP / "PROOF.md") == \
    "0e0f608d167b2c3453568d06ccc4ba8319e67e5c2d066e4c4ee6854c8fb3a66b"
assert sha(CAP / "source/T4_415_PROOF.md") == H415["PROOF.md"]
assert sha(CAP / "source/T4_415_result.json") == H415["verification/result.json"]
assert sha(SHP / "verification/result.json") == "e94368caabeca952aa08be744c4df75e840d4d6e73ef9b9f990dfc3b950ffe10"
for n_ in NAMES:
    assert sha(SRC / f"data/{n_}_endpoint.json") == sha(SPV / f"data/{n_}_endpoint.json") == \
        sha(CAP / f"data/{n_}_endpoint.json") == sha(SHP / f"data/{n_}_endpoint.json")
PAR = json.loads((SRC / "data/parameters.json").read_text())
assert PAR == {"E": "93/250", "profile_scale": "100000", "precision_bits": 192, "theta_cells": 1024,
               "witness_cells": 512, "initial_projective_cells": 16, "max_depth": 14, "candidates": list(NAMES)}
PAR2 = json.loads((CAP / "data/parameters.json").read_text())
PARS = json.loads((SHP / "data/parameters.json").read_text())
RESS = json.loads((SHP / "verification/result.json").read_text())
assert PAR2["E"] == "93/250" and PAR2["H0"] == PARS["H0"] and PAR2["betas"] == PARS["betas"] \
    and PAR2["angles"] == PARS["angles"] and PAR2["c"] == PARS["c"]
# the lane copy: identical files, and the rerun of the copied check.py reproduces the saved rows
for k_ in ("PROOF.md", "code/check.py", "code/geometry.py", "data/manifest.json", "data/parameters.json",
           "source/profile_PROOF.md", *[f"data/{n_}_endpoint.json" for n_ in NAMES]):
    assert sha(REP / k_) == sha(SRC / k_), k_
REPRES = json.loads((REP / "verification/result.json").read_text())
strip = lambda rows: [{k_: v_ for k_, v_ in r_.items() if k_ != "elapsed_s"} for r_ in rows]
OUT["inputs"] = {"T4-415": dict(H415), "T4-415 manifest inputs": MAN["inputs"], "T4-422": dict(H422),
                 "T4-422 manifest inputs": MAN2["inputs"],
                 "lane rerun result.json": sha(REP / "verification/result.json"), "lane rerun utc": REPRES["utc"],
                 "lane rerun rows equal saved rows": strip(REPRES["rows"]) == strip(RES["rows"]),
                 "lane rerun other fields equal": all(REPRES[k_] == RES[k_] for k_ in RES if k_ not in ("utc", "elapsed_s", "rows"))}
assert OUT["inputs"]["lane rerun rows equal saved rows"] and OUT["inputs"]["lane rerun other fields equal"]
print("inputs: all hashes asserted; lane rerun of the copied check.py (utc %s) gives the saved rows: True" % REPRES["utc"])

# =============================== (A) exact rationals, own code ===============================
cF = Fr(4076476460239181, 2**51)
assert Fr(PAR2["c"]) == cF
qF = 1 / cF - 4
pF = qF + 2
EF = Fr(93, 250)
SCALE = Fr(100000)
assert -5 < qF < -3


def vel(b):
    """b: {n: sin coefficient}. Returns V1, V2 of (9) of T4-402 as maps k -> (re, im) coefficient of e^{ik theta}."""
    v1, v2 = {}, {}

    def put(d, k, z):
        re_, im_ = d.get(k, (Fr(0), Fr(0)))
        d[k] = (re_ + z[0], im_ + z[1])
    for n, bn in b.items():
        Dn = 4 * (pF * pF - n * n)
        a_, c_ = bn * (pF + n) * (pF + n - 2) / Dn, bn * (pF - n) * (pF - n - 2) / Dn
        for k, w in ((n - 2, a_), (-(n - 2), a_), (n + 2, -c_), (-(n + 2), -c_)):   # cos(k th) = (e^{ik} + e^{-ik})/2
            put(v1, k, (w / 2, Fr(0)))
        for k, w in ((n, -bn / 2), (n - 2, -a_), (n + 2, -c_)):                       # sin(k th) = (e^{ik} - e^{-ik})/(2i)
            put(v2, k, (Fr(0), -w / 2))
            put(v2, -k, (Fr(0), w / 2))
    return v1, v2


def mul(f, g):
    out = {}
    for k1, (a1, b1) in f.items():
        for k2, (a2, b2) in g.items():
            re_, im_ = out.get(k1 + k2, (Fr(0), Fr(0)))
            out[k1 + k2] = (re_ + a1 * a2 - b1 * b2, im_ + a1 * b2 + b1 * a2)
    return out


def addto(acc, f, sc):
    for k, (a_, b_) in f.items():
        re_, im_ = acc.get(k, (Fr(0), Fr(0)))
        acc[k] = (re_ + sc * a_, im_ + sc * b_)


def vdot(u, w):
    d_ = {}
    addto(d_, mul(u[0], w[0]), Fr(1))
    addto(d_, mul(u[1], w[1]), Fr(1))
    return d_


def cosines(e):
    """Exponential coefficients of a real even function -> its cosine coefficients {k >= 0: C_k}."""
    assert all(v_[1] == 0 and e.get(-k, (None,))[0] == v_[0] for k, v_ in e.items())
    return {k: (e[k][0] if k == 0 else 2 * e[k][0]) for k in e if k >= 0 and e[k][0] != 0}


def sinprod(a, b, deriv):
    """Cosine coefficients of f g (deriv False) or f' g' (deriv True) for sine series f = sum a_n sin, g = sum b_m sin."""
    out = {}
    for n, an in a.items():
        for m, bm in b.items():
            w = an * bm * (n * m if deriv else 1) / 2
            for k, sg in ((abs(n - m), 1), (n + m, 1 if deriv else -1)):
                out[k] = out.get(k, Fr(0)) + sg * w
    return {k: v_ for k, v_ in out.items() if v_ != 0}


CAND = {}
OUT["A"] = {}
for name in NAMES:
    ep = json.loads((SRC / f"data/{name}_endpoint.json").read_text())
    assert Fr(ep["c"]) == cF
    A = {int(k_): Fr(v_) for k_, v_ in ep["F12"].items()}
    P = {int(k_): Fr(v_) for k_, v_ in ep["P"].items()}
    th0 = {int(k_): Fr(v_) for k_, v_ in ep["Theta0"].items()}
    f2 = {n: SCALE * v_ for n, v_ in P.items()}
    assert all(n > 0 and n % 2 == 1 for n in list(A) + list(P))
    va, vb = vel(A), vel(f2)
    F11, F12, F22 = cosines(vdot(va, va)), cosines(vdot(va, vb)), cosines(vdot(vb, vb))
    degs = sorted(set(F11) | set(F12) | set(F22))
    assert all(k % 2 == 0 for k in degs)
    # Q_ij(phi) = q^2 f_i f_j + f_i' f_j' as cosine series, for part (D)
    Qc = [{}, {}, {}]
    for i_, (u_, w_) in enumerate(((A, A), (A, f2), (f2, f2))):
        for k, v_ in sinprod(u_, w_, False).items():
            Qc[i_][k] = Qc[i_].get(k, Fr(0)) + qF * qF * v_
        for k, v_ in sinprod(u_, w_, True).items():
            Qc[i_][k] = Qc[i_].get(k, Fr(0)) + v_
    assert all(k % 2 == 0 for d_ in Qc for k in d_)
    CAND[name] = {"A": A, "P": P, "f2": f2, "th0": th0, "F": (F11, F12, F22), "degs": degs, "Qc": Qc}
    OUT["A"][name] = {"modes_A": sorted(A), "modes_P": sorted(P), "F_cosine_degrees": degs, "only_even_degrees": True}
    print("(A) %s: modes of A and P odd, %d..%d; F_ij cosine degrees %s (even only: True)"
          % (name, min(A), max(max(A), max(P)), degs))

# =============================== (B) the saved certificate ===============================
ctx.prec = 256
PI = arb.pi()
A_ = lambda fr_: arb(fr_.numerator) / fr_.denominator


def parse(sv):
    m_, r_ = sv.strip().strip("[]").split("+/-")
    return arb(m_.strip(), r_.strip())


def close(x_, y_, rel):
    return bool(abs(x_ - y_) < arb(10)**-rel * (1 + abs(y_)))


def directed(xv, up, sig=7):
    """Decimal string with sig significant digits, >= every point of the ball if up, else <= (exact endpoints)."""
    m_, e_ = (xv.upper() if up else xv.lower()).man_exp()
    v_ = Fr(int(m_)) * Fr(2)**int(e_)
    if v_ == 0:
        return "0"
    ex = math.floor(math.log10(abs(float(v_))))
    pl = sig - 1 - ex
    n_ = math.ceil(v_ * Fr(10)**pl) if up else math.floor(v_ * Fr(10)**pl)
    out = Fr(n_) / Fr(10)**pl
    assert (out >= v_) if up else (out <= v_)
    return ("%." + str(max(pl, 0)) + "f") % out if pl >= 0 else str(int(out))


abc = lambda x, y, z: ((x + z) / 2, (x - z) / 2, y)
quad = lambda co, ca, sa: co[0] + co[1] * ca + co[2] * sa
E2 = A_(EF * EF)
qA = A_(qF)


def prepare(cd):
    """Arb (c0, cc, cs) cosine coefficients of F, keyed by degree."""
    F11, F12, F22 = cd["F"]
    return {n: tuple(A_(v_) for v_ in abc(F11.get(n, Fr(0)), F12.get(n, Fr(0)), F22.get(n, Fr(0)))) for n in cd["degs"]}


def witness(cd, ph):
    """(c0, cc, cs) of Q(ph) in Arb, own evaluation of f_i(ph) and f_i'(ph)."""
    vals = []
    for f in (cd["A"], cd["f2"]):
        fv = sum((A_(v_) * (n * ph).sin() for n, v_ in f.items()), arb(0))
        fd = sum((n * A_(v_) * (n * ph).cos() for n, v_ in f.items()), arb(0))
        vals.append((qA * fv, fd))
    a_, b_ = vals
    return abc(a_[0]**2 + a_[1]**2, a_[0] * b_[0] + a_[1] * b_[1], b_[0]**2 + b_[1]**2)


OUT["B"] = {}
M = PAR["theta_cells"]
DW = PAR["witness_cells"]
hk = PI / (4 * M)
total_rect = 0
for name in NAMES:
    cd = CAND[name]
    co = prepare(cd)
    cd["co"] = co
    row = next(r_ for r_ in RES["rows"] if r_["candidate"] == name)
    cells = row["cells"]
    L = [Fr(c_["left_pi"]) for c_ in cells]
    R = [Fr(c_["right_pi"]) for c_ in cells]
    cov = {"first left = -1/2": L[0] == Fr(-1, 2), "last right = 1/2": R[-1] == Fr(1, 2),
           "contiguous": all(R[i] == L[i + 1] for i in range(len(cells) - 1)),
           "width = (1/16)/2^depth": all(R[i] - L[i] == Fr(1, 16) / 2**c_["depth"] for i, c_ in enumerate(cells)),
           "dyadic aligned": all((L[i] * 16 * 2**c_["depth"]).denominator == 1 for i, c_ in enumerate(cells)),
           "witness index in 0..512": all(0 <= c_["witness_index"] <= DW for c_ in cells),
           "theta cells checked = 1024": all(c_["theta_cells_checked"] == M for c_ in cells),
           "rectangle count": row["accepted_rectangle_count"] == len(cells) * M == row["accepted_projective_cells"] * M,
           "max depth": row["max_depth"] == max(c_["depth"] for c_ in cells), "q exact": Fr(row["q_exact"]) == qF}
    total_rect += len(cells) * M
    Fj, FPj = [], []
    for j in range(M):
        th = PI * (2 * j + 1) / (4 * M)
        sc = {n: (n * th).sin_cos() for n in co}
        Fj.append(tuple(sum((c_[k] * sc[n][1] for n, c_ in co.items()), arb(0)) for k in range(3)))
        FPj.append(tuple(sum((-n * c_[k] * sc[n][0] for n, c_ in co.items()), arb(0)) for k in range(3)))
    QWs = {}
    recs = []
    allpos = True
    for c_, l_, r_ in zip(cells, L, R):
        w = c_["witness_index"]
        if w not in QWs:
            QWs[w] = witness(cd, PI * w / (2 * DW))
        base = tuple(E2 * x_ for x_ in QWs[w])
        mid, half = (l_ + r_) / 2, (r_ - l_) / 2
        am, h = PI * A_(mid), PI * A_(half)
        sa, ca = (2 * am).sin(), (2 * am).cos()
        sia, cia = (2 * arb(am, h)).sin_cos()                    # the PROOF's ball for alpha in the cell, as in check.py
        M2 = sum((n * n * abs(quad(c2, cia, sia)) for n, c2 in co.items()), arb(0))
        err2 = M2 * hk * hk / 2
        gmin, jmin = None, None
        for j in range(M):
            t = tuple(base[k] - Fj[j][k] for k in range(3))
            slope = 2 * (-t[1] * sa + t[2] * ca)
            rem = 2 * (t[1] * t[1] + t[2] * t[2]).sqrt() * h * h
            low = quad(t, ca, sa) - abs(slope) * h - rem
            gap = low - abs(quad(FPj[j], cia, sia)) * hk - err2
            allpos = allpos and bool(gap > 0)
            if gmin is None or gap.lower() < gmin:
                gmin, jmin = gap.lower(), j                       # the lower end of the gap ball, as saved by check.py
        saved = parse(c_["minimum_gap_lower"])
        recs.append({"cell": [str(l_), str(r_)], "depth": c_["depth"], "witness": w, "own_min_gap": gmin.str(20),
                     "saved_min_gap": c_["minimum_gap_lower"], "argmin_theta_cell_own": jmin,
                     "argmin_theta_cell_saved": c_["minimum_theta_cell"],
                     "rel_diff_min_gap": float(abs(gmin - saved).upper() / abs(saved).lower()),
                     "min gap agrees (rel 1e-8)": close(gmin, saved, 8), "argmin agrees": jmin == c_["minimum_theta_cell"],
                     "min gap > 0": bool(gmin > 0)})
    ok = all(cov.values()) and allpos and all(x_["min gap agrees (rel 1e-8)"] and x_["argmin agrees"] for x_ in recs)
    tight = min(recs, key=lambda x_: float(parse(x_["own_min_gap"]).mid()))
    OUT["B"][name] = {"coverage": cov, "all gaps positive": allpos, "cells": recs, "ok": ok, "cells_count": len(cells),
                      "depths": [c_["depth"] for c_ in cells], "tightest": tight}
    assert ok, (name, cov, allpos, [(x_["cell"], x_["rel_diff_min_gap"], x_["argmin_theta_cell_own"],
                                     x_["argmin_theta_cell_saved"]) for x_ in recs])
    print("(B) %s: %d saved cells cover [-1/2, 1/2] (%s); bound (4)-(5) with own F and Q: all %d gaps > 0: %s; minimum gaps"
          " and their theta cells equal result.json: True (largest relative difference %.1e); tightest cell %s, own min gap %s"
          % (name, len(cells), all(cov.values()), len(cells) * M, allpos, max(x_["rel_diff_min_gap"] for x_ in recs),
             tight["cell"], tight["own_min_gap"]))
OUT["B"]["rectangles"] = total_rect
print("(B) rectangles rechecked: %d" % total_rect)

# =============================== (C) an independent certificate ===============================
MC, DC, NC, MAXD = 1536, 1536, 12, 16
kC = PI / (4 * MC)
OUT["C"] = {"theta_cells": MC, "witness_cells": DC, "initial_cells": NC, "max_depth": MAXD}


def arcmin(T, cl, sl, cr, sr):
    """Lower bound of t(alpha) = T0 + T1 cos 2alpha + T2 sin 2alpha on an arc of 2alpha of length < pi with endpoint
    values (cl, sl), (cr, sr). An interior minimum needs t' < 0 at the left end and t' > 0 at the right end."""
    tl = T[0] + T[1] * cl + T[2] * sl
    tr = T[0] + T[1] * cr + T[2] * sr
    dl = -T[1] * sl + T[2] * cl
    dr = -T[1] * sr + T[2] * cr
    if dl > 0 or dr < 0:
        return tl if tl.lower() < tr.lower() else tr
    return T[0] - (T[1] * T[1] + T[2] * T[2]).sqrt()


for name in NAMES:
    st = time.monotonic()
    cd = CAND[name]
    co = cd["co"]
    Fj, FPj, F2J = [], [], []
    for j in range(MC):
        th = PI * (2 * j + 1) / (4 * MC)
        J = (th - kC).union(th + kC)
        sc = {n: (n * th).sin_cos() for n in co}
        cJ = {n: (n * J).cos() for n in co}
        Fj.append(tuple(sum((c_[k] * sc[n][1] for n, c_ in co.items()), arb(0)) for k in range(3)))
        FPj.append(tuple(sum((-n * c_[k] * sc[n][0] for n, c_ in co.items()), arb(0)) for k in range(3)))
        F2J.append(tuple(sum((-n * n * c_[k] * cJ[n] for n, c_ in co.items()), arb(0)) for k in range(3)))
    # float witness table for the selection only; Arb witnesses computed when used
    phf = np.arange(DC + 1) * np.pi / (2 * DC)
    QFf = []
    for f in (cd["A"], cd["f2"]):
        fv = sum(float(v_) * np.sin(n * phf) for n, v_ in f.items())
        fd = sum(n * float(v_) * np.cos(n * phf) for n, v_ in f.items())
        QFf.append((float(qF) * fv, fd))
    (a0, a1), (b0, b1) = QFf
    W11, W12, W22 = a0 * a0 + a1 * a1, a0 * b0 + a1 * b1, b0 * b0 + b1 * b1
    QW = {}
    stack = [(Fr(-1, 2) + Fr(j, NC), Fr(-1, 2) + Fr(j + 1, NC), 0) for j in reversed(range(NC))]
    cells, attempts, checks = [], 0, 0
    while stack:
        l_, r_, depth = stack.pop()
        attempts += 1
        am = float((l_ + r_) / 2) * math.pi
        z1, z2 = math.cos(am), math.sin(am)
        w = int(np.argmax(W11 * z1 * z1 + 2 * W12 * z1 * z2 + W22 * z2 * z2))
        if w not in QW:
            QW[w] = witness(cd, PI * w / (2 * DC))
        base = tuple(E2 * x_ for x_ in QW[w])
        al, ar = 2 * PI * A_(l_), 2 * PI * A_(r_)
        sl, cl = al.sin(), al.cos()
        sr, cr = ar.sin(), ar.cos()
        arc = al.union(ar)
        sia, cia = arc.sin(), arc.cos()
        passed, gmin, jmin = True, None, None
        for j in range(MC):
            lup = quad(F2J[j], cia, sia).upper()                  # >= z^T F''(xi) z for alpha in I, xi in J
            second = kC * kC / 2 * (lup if lup > 0 else arb(0))
            g = None
            for s in (1, -1):
                T = tuple(base[k] - Fj[j][k] - s * kC * FPj[j][k] for k in range(3))
                m_ = arcmin(T, cl, sl, cr, sr) - second
                g = m_ if g is None or m_.lower() < g.lower() else g
            checks += 1
            if not g > 0:
                passed = False
                break
            if gmin is None or g.lower() < gmin.lower():
                gmin, jmin = g, j
        if passed:
            cells.append({"cell": [str(l_), str(r_)], "depth": depth, "witness": w, "min_gap_lower": directed(gmin, False, 10),
                          "argmin_theta_cell": jmin})
        else:
            assert depth < MAXD, (name, str(l_), str(r_), j)
            mid = (l_ + r_) / 2
            stack.append((mid, r_, depth + 1))
            stack.append((l_, mid, depth + 1))
    cells.sort(key=lambda x_: Fr(x_["cell"][0]))
    assert Fr(cells[0]["cell"][0]) == Fr(-1, 2) and Fr(cells[-1]["cell"][1]) == Fr(1, 2)
    assert all(Fr(cells[i]["cell"][1]) == Fr(cells[i + 1]["cell"][0]) for i in range(len(cells) - 1))
    assert all(Fr(x_["cell"][1]) - Fr(x_["cell"][0]) <= Fr(1, NC) for x_ in cells)          # arc of 2 alpha < pi
    tight = min(cells, key=lambda x_: float(x_["min_gap_lower"]))
    OUT["C"][name] = {"cells": cells, "accepted": len(cells), "attempts": attempts, "theta_checks": checks,
                      "rectangles": len(cells) * MC, "max_depth": max(x_["depth"] for x_ in cells), "tightest": tight,
                      "elapsed_s": time.monotonic() - st}
    print("(C) %s: independent certificate PASSES: %d alpha cells (max depth %d, %d attempts) x %d theta cells; tightest"
          " cell %s with gap >= %s; %.1f s"
          % (name, len(cells), OUT["C"][name]["max_depth"], attempts, MC, tight["cell"], tight["min_gap_lower"],
             OUT["C"][name]["elapsed_s"]))

# =============================== (D) the best constant ===============================
OUT["D"] = {}
thf = np.linspace(0, np.pi / 2, 16385)
for name in NAMES:
    cd = CAND[name]
    F11, F12, F22 = cd["F"]
    ev = lambda d_: sum(float(v_) * np.cos(k * thf) for k, v_ in d_.items())
    Ff = [ev(F11), ev(F12), ev(F22)]
    Qf = [ev(d_) for d_ in cd["Qc"]]

    def ratio(al):
        z1, z2 = math.cos(al), math.sin(al)
        num = (Ff[0] * z1 * z1 + 2 * Ff[1] * z1 * z2 + Ff[2] * z2 * z2).max()
        den = (Qf[0] * z1 * z1 + 2 * Qf[1] * z1 * z2 + Qf[2] * z2 * z2).max()
        return math.sqrt(max(num, 0) / den)
    ag = np.linspace(-np.pi / 2, np.pi / 2, 4001)
    rv = np.array([ratio(a_) for a_ in ag])
    i0 = int(rv.argmax())
    af = np.linspace(ag[max(i0 - 1, 0)], ag[min(i0 + 1, len(ag) - 1)], 2001)
    rf = np.array([ratio(a_) for a_ in af])
    a_star = float(af[int(rf.argmax())])
    # rigorous lower bound at the rational z = (1, w), w close to tan(alpha*)
    wF = Fr(round(math.tan(a_star) * 10**6), 10**6)
    z1z = [Fr(1), wF]
    num_c = {k: F11.get(k, Fr(0)) + 2 * wF * F12.get(k, Fr(0)) + wF * wF * F22.get(k, Fr(0)) for k in cd["degs"]}
    den_c = {}
    for i_, sc_ in ((0, Fr(1)), (1, 2 * wF), (2, wF * wF)):
        for k, v_ in cd["Qc"][i_].items():
            den_c[k] = den_c.get(k, Fr(0)) + sc_ * v_
    z1_, z2_ = 1.0, float(wF)
    nf = Ff[0] * z1_ * z1_ + 2 * Ff[1] * z1_ * z2_ + Ff[2] * z2_ * z2_
    th_star = Fr(round(float(thf[int(nf.argmax())]) * 10**8), 10**8)
    Nlow = sum((A_(v_) * (k * A_(th_star)).cos() for k, v_ in num_c.items()), arb(0)).sqrt()
    dA_ = {k: A_(v_) for k, v_ in den_c.items()}
    NG = 8192
    hw = PI / (4 * NG)
    M2g = sum((abs(v_) * k * k for k, v_ in dA_.items()), arb(0))
    gup = None
    for i in range(NG):
        tm = (2 * i + 1) * hw
        val = sum((v_ * (k * tm).cos() for k, v_ in dA_.items()), arb(0))
        der = sum((-v_ * k * (k * tm).sin() for k, v_ in dA_.items()), arb(0))
        bnd = val + abs(der) * hw + M2g * hw * hw / 2
        gup = bnd if gup is None or bnd.upper() > gup.upper() else gup
    Glow_ratio = Nlow / arb(gup.upper()).sqrt()
    assert Glow_ratio < A_(EF)
    OUT["D"][name] = {"FLOAT_sup_ratio": float(rf.max()), "FLOAT_alpha_star": a_star,
                      "FLOAT_t_star": 1e5 * math.tan(a_star), "w": str(wF), "theta0": str(th_star),
                      "best_constant_lower": directed(Glow_ratio, False, 7),
                      "margin_93_250_minus_lower_upper": directed(A_(EF) - Glow_ratio, True, 4)}
    print("(D) %s: sup_z N/G >= %s (Arb, z = (1, %s), theta0 = %s, G by a Taylor bound on %d cells); FLOAT sup %.7f at"
          " alpha = %.6f (t = 1e5 tan alpha = %.6g); 93/250 minus the lower bound <= %s"
          % (name, OUT["D"][name]["best_constant_lower"], wF, th_star, NG, rf.max(), a_star, 1e5 * math.tan(a_star),
             OUT["D"][name]["margin_93_250_minus_lower_upper"]))

# =============================== (E) the lane copy of c1-t4's geometry.py, exec in memory ===============================
NS = {}
assert sha(REP / "code/geometry.py") == H415["code/geometry.py"]
exec(compile((REP / "code/geometry.py").read_text(), "lane copy of c1-t4 geometry.py (hash-bound, in memory)", "exec"), NS)
OUT["E"] = {}
qQ = fmpq(qF.numerator, qF.denominator)
for name in NAMES:
    cd = CAND[name]
    ff = [{n: fmpq(v_.numerator, v_.denominator) for n, v_ in f.items()} for f in (cd["A"], cd["f2"])]
    vv = [NS["velocity"](f, qQ + 2) for f in ff]
    polys = [NS["dot"](vv[0], vv[0]), NS["dot"](vv[0], vv[1]), NS["dot"](vv[1], vv[1])]
    conv = [{int(n): Fr(int(v_.p), int(v_.q)) for n, v_ in d_.items() if v_ != 0} for d_ in polys]
    same = [conv[i] == cd["F"][i] for i in range(3)]
    OUT["E"][name] = {"F11": same[0], "F12": same[1], "F22": same[2]}
    assert all(same), name
    print("(E) %s: c1-t4 velocity/dot give exactly the own F11, F12, F22: True" % name)

# =============================== (F) T4-422 ===============================
R375 = json.loads((HERE / "data/t4_375_review_results.json").read_text())
R414 = json.loads((HERE / "data/t4_414_review_results.json").read_text())
OUT["F"] = {"deps": {"t4_375_review_results_sha256": sha(HERE / "data/t4_375_review_results.json"),
                     "t4_414_review_results_sha256": sha(HERE / "data/t4_414_review_results.json")}}
dF = 1 - 1 / cF
DF = 5 * cF - 1
aF = -2 * qF - 2
SF = 2 * dF**2 / (aF * (aF + dF) * (aF + 2 * dF))
assert str(SF) == RES2["shape_factor_exact"] and RES2["E_exact"] == "93/250"
cA, dA, DA, aA, SA = (A_(v_) for v_ in (cF, dF, DF, aF, SF))
s2p = (2 * PI).sqrt()
betas = {k_: Fr(v_) for k_, v_ in PAR2["betas"].items()}
nchk = 0
allF = True
for name in NAMES:
    cd = CAND[name]
    A, P = cd["A"], cd["P"]
    ns = sorted(set(A) | set(P))
    Saa = sum(A.get(n, Fr(0))**2 for n in ns)
    Sap = sum(A.get(n, Fr(0)) * P.get(n, Fr(0)) for n in ns)
    Spp = sum(P.get(n, Fr(0))**2 for n in ns)
    Bv = (PI * A_(Saa - Sap**2 / Spp)).sqrt() / (4 * cA)
    g0F = sum(n * v_ for n, v_ in cd["th0"].items())
    g0v = A_(g0F)
    t_ = A_(Fr(PAR2["angles"][name]))
    av = sum((A_(v_) * (n * t_).sin() for n, v_ in A.items()), arb(0))
    ad = sum((n * A_(v_) * (n * t_).cos() for n, v_ in A.items()), arb(0))
    pv = sum((A_(v_) * (n * t_).sin() for n, v_ in P.items()), arb(0))
    pd = sum((n * A_(v_) * (n * t_).cos() for n, v_ in P.items()), arb(0))
    Phi_line = abs(qA * (av * pd - ad * pv)) / (4 * cA * (qA * qA * pv * pv + pd * pd).sqrt())   # min_t of the gradient
    Phi375 = parse(R375["D"][name]["Phi_theta_star"])
    H0 = arb(PAR2["H0"][name])
    row = next(r_ for r_ in RES2["rows"] if r_["candidate"] == name)
    row414 = next(r_ for r_ in RESS["rows"] if r_["candidate"] == name)
    v0 = A_(Fr(row414["v0_exact"]))
    r0 = (s2p * H0 * A_(EF) * g0v / (DA * Bv))**(1 / dA)
    cap = Bv * r0**(A_(qF) + 1) * SA.sqrt()
    r0V = (s2p * H0 * (v0 + A_(EF) * g0v) / (DA * Bv))**(1 / dA)
    capV = Bv * r0V**(A_(qF) + 1) * SA.sqrt()
    chk = {"H0 integer": row["H0_integer"] == PAR2["H0"][name], "B": close(Bv, parse(row["B"]), 40),
           "g0 exact": str(g0F) == row["g0_exact"], "Phi (line formula, own) equals result.json": close(Phi_line, parse(row["Phi"]), 40),
           "Phi equals own Phi(theta*) of REVIEW_T4_375": close(Phi_line, Phi375, 14),
           "angle is theta* of REVIEW_T4_375": R375["D"][name]["theta_star"] == PAR2["angles"][name],
           "H0 < Phi": bool(H0 < Phi_line), "r0": close(r0, parse(row["r0"]), 40), "cap": close(cap, parse(row["cap"]), 40),
           "cap in its rational enclosure": bool(A_(Fr(row["cap_enclosure"]["lower_exact"])) < cap < A_(Fr(row["cap_enclosure"]["upper_exact"])))}
    tg = {}
    for key, beta in betas.items():
        ratio_ = cap / A_(beta)
        crit = DA * Bv / (s2p * H0 * g0v) * (Bv * SA.sqrt() / A_(beta))**(dA / (-A_(qF) - 1))
        tv = row["targets"][key]
        above = bool(ratio_ > 1)
        chk.update({f"{key}: ratio": close(ratio_, parse(tv["ratio"]), 40), f"{key}: Ecrit": close(crit, parse(tv["Ecrit"]), 40),
                    f"{key}: ratio in its enclosure": bool(A_(Fr(tv["ratio_enclosure"]["lower_exact"])) < ratio_ < A_(Fr(tv["ratio_enclosure"]["upper_exact"]))),
                    f"{key}: decided": above != bool(ratio_ < 1),
                    f"{key}: flags": tv["ceiling_exceeds_target"] == above and tv["ceiling_below_target"] == (not above),
                    f"{key}: ratio > 1 iff Ecrit > 93/250": above == bool(crit > A_(EF)) and (not above) == bool(crit < A_(EF)),
                    f"{key}: Ecrit within 1e-7 below the REVIEW_T4_414 upper bound (3), V = 0, H0 integer":
                        bool(arb(R414["B"][name]["versions"]["V_zero"]["thresholds"][key]["retained_upper_H0"]) >= crit.upper()) and
                        bool(crit.upper() > arb(R414["B"][name]["versions"]["V_zero"]["thresholds"][key]["retained_upper_H0"]) - arb(10)**-7)})
        tg[key] = {"ratio_lower": directed(ratio_, False, 10), "ratio_upper": directed(ratio_, True, 10),
                   "ratio_V_lead_upper": directed(capV / A_(beta), True, 7), "Ecrit_upper": directed(crit, True, 10),
                   "room_93_250_Phi_V0_upper": R414["B"][name]["versions"]["V_zero"]["thresholds"][key]["room_93/250_upper"],
                   "room_93_250_Phi_Vlead_upper": R414["B"][name]["versions"]["V_lead"]["thresholds"][key]["room_93/250_upper"]}
    nchk += len(chk)
    allF = allF and all(chk.values())
    OUT["F"][name] = {"checks": chk, "cap_lower": directed(cap, False, 10), "cap_upper": directed(cap, True, 10),
                      "r0_lower": directed(r0, False, 10), "cap_V_lead_upper": directed(capV, True, 7), "targets": tg}
    print("(F) %s: cap (E = 93/250, V = 0, H0 integer) in [%s, %s], r0 >= %s; all %d checks: %s; with V = |U_lead(0)|:"
          " cap <= %s" % (name, OUT["F"][name]["cap_lower"], OUT["F"][name]["cap_upper"], OUT["F"][name]["r0_lower"],
                          len(chk), all(chk.values()), OUT["F"][name]["cap_V_lead_upper"]))
    for key, tv in tg.items():
        print("    %s: cap/beta in [%s, %s] (V = 0), <= %s (V = |U_lead(0)|); Ecrit <= %s; room for 93/250 (H >= Phi) <= %s"
              " (V = 0), <= %s (V >= |U_lead(0)|)" % (key, tv["ratio_lower"], tv["ratio_upper"], tv["ratio_V_lead_upper"],
                                                     tv["Ecrit_upper"], tv["room_93_250_Phi_V0_upper"], tv["room_93_250_Phi_Vlead_upper"]))
assert allF
OUT["F"]["checks_total"] = nchk
print("(F) T4-422: %d own checks, all pass" % nchk)

OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_415_review_results.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
print("elapsed %.1f s" % OUT["elapsed_s"])
