"""Independent review of the third cutoff of T4-338 (c1-t4 research/finite_tail_surgery/PROOF.md, sha256
11a6a2eb...c990, Section 2) and of the conditional consequence T4-339 (Section 3) (reviews/REVIEW_T4_338.md).

Run from artifacts/:  python3 -B -u arith/t4_338_review.py
Needs sympy, mpmath, python-flint.

Parts:
  (A) exact exponents: q1, q2, q3, q*, e_(10,0), e_(6,1); the comparisons of Section 2; the list of all lattice
      exponents 1 - K delta - 2L (K, L >= 0) in [q* - 1/2, gamma]; nonresonance (A, B coprime, A odd, 1 - 2A).
  (B) exact (fmpq), for 007, 013, 014, from the raw c1-n1 generator files with my constructor (the prefix of
      arith/t4_294_review.py): A3 two ways, (i) the (5,1) residual with the (4,1) density and stream set to zero
      (the PROOF's recipe) and (ii) the (5,1) residual of my branch-3 algebraic repair of REVIEW_T4_294 (rebuilt from
      the generators). Both against c1-t4's residual_A3; original F_(5,1) differs. B3 = A3/(1 - c q3) against
      density_B3; my descending solve (arith/t4_324_review.py) against potential_cosine_coefficients; my forward
      density map of the stored potential against density_B3; my Poisson stream of B3 against stream_coefficients.
      Then the three-cutoff state (first cutoff: (4,1) := 0; second: (9,0) := B2 = F_(9,0)/(1 - c q2) with its
      Poisson stream; third: (5,1) += B3 with its stream): every residual sector at exponent >= q* (only (1,2), equal
      to the original F_(1,2) and to endpoint_residual_unchanged), and the first nonzero sectors below q*.
  (C) arb: circle norms of A3, B3, F_(1,2) and of the leading residual sectors below q* after three cutoffs.
  (D) exact and arb: P from Theta_(1,0) against c1-t4's endpoint data; a = Pi(F_(1,2))/(4c) and b = Pi(F_(10,0))/D_eps,
      Pi the L2(S1) projection orthogonal to P, F_(10,0) the residual after three cutoffs, D_eps = 1 - c e_(10,0);
      ||a + s b|| for s = r^-eps (eps = 9 delta - 4), its minimum over s >= 0 and its values at r = 10^k.
Output: logs/t4_338_review.log, data/t4_338_review_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

from flint import arb, ctx, fmpq

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parents[1]
T4R = Path("RUN_ROOT/theory_audit_T4/research/finite_tail_surgery")
T0 = time.monotonic()
OUT = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


assert sha(T4R / "PROOF.md") == "11a6a2eb04c60a33e2bae2e8692c839556762a7b47e9485e2dc72cd4d8b7c990"
MAN = json.loads((T4R / "verification/MANIFEST.json").read_text())["files"]
for nm in ("007", "013", "014"):
    assert sha(T4R / f"data/{nm}_third_repair.json") == MAN[f"data/{nm}_third_repair.json"]

# =============================== (A) exact exponents ===============================
cF = Fr(4076476460239181, 2**51)
gF = 1 / cF
dF = 1 - gF
AA, BB = 1824676646553933, 4076476460239181
assert dF == Fr(AA, BB) and gcd(AA, BB) == 1 and AA % 2 == 1
e = lambda K, L: 1 - K * dF - 2 * L
q1, q2, q3, qs = e(4, 1), e(9, 0), e(5, 1), e(1, 2)
assert qs == gF - 4 and q3 == -1 - 5 * dF and q2 == 1 - 9 * dF and q1 == -1 - 4 * dF
res4 = json.loads((T4R / "verification/result.json").read_text())
assert all(Fr(res4["exponents"][k_]) == v for k_, v in (("q1", q1), ("q2", q2), ("q3", q3), ("qstar", qs)))
assert q3 - dF == e(6, 1) < e(10, 0) < qs and 2 * q3 - 1 < qs and q2 - dF == e(10, 0) and 2 * q2 - 1 < qs
assert q1 - dF == q3 and -2 < q3 + 3 < 0 and 1 - 2 * AA == res4["nonresonance_threshold"] == -3649353293107865
lat = sorted({(e(K, L), K, L) for K in range(0, 40) for L in range(0, 6) if qs - Fr(1, 2) <= e(K, L) <= gF},
             reverse=True)
labels = {}
for v, K, L in lat:
    labels.setdefault(v, []).append((K, L))
assert all(len(v) == 1 for v in labels.values())            # no two labels share an exponent in this window
between = [(K, L) for v, K, L in lat if e(10, 0) < v < qs]
assert between == []
print("(A) q1 = %.12f, q2 = %.12f, q3 = %.12f, q* = %.12f; q3 - delta = e_(6,1) = %.12f and e_(10,0) = q2 - delta ="
      " %.12f lie below q*; 2 q3 - 1 = %.6f; q3 + 3 = %.12f in (-2, 0); delta = A/B, gcd 1, A odd, 1 - 2A = %d;"
      " no exponent strictly between e_(10,0) and q*; lattice exponents in [q* - 1/2, gamma]: %s"
      % (float(q1), float(q2), float(q3), float(qs), float(e(6, 1)), float(e(10, 0)), float(2 * q3 - 1),
         float(q3 + 3), 1 - 2 * AA, ", ".join("(%d,%d) %.4f" % (K, L, float(v)) for v, K, L in lat)))
OUT["A"] = {"q1": str(q1), "q2": str(q2), "q3": str(q3), "qstar": str(qs), "e61": str(e(6, 1)), "e100": str(e(10, 0)),
            "lattice_window": [[K, L, str(v)] for v, K, L in lat]}

# =============================== (B) exact ===============================
src = (HERE / "arith/t4_294_review.py").read_text()
assert sha(HERE / "arith/t4_294_review.py") == "229c9bd070a868ec627021c41f08967d61603af807d7d7d7f0616ca03a3b950c"
ns = {"__file__": str(HERE / "arith/t4_294_review.py"), "__name__": "t4_294_prefix"}
print("(B) executing the prefix of arith/t4_294_review.py (its own (A), (B) lines follow)")
exec(compile(src[:src.index("\nRES = {}\n")], "t4_294_review.py (prefix)", "exec"), ns)
s324 = (HERE / "arith/t4_324_review.py").read_text()
assert sha(HERE / "arith/t4_324_review.py") == "fd806d3d4a335e1cd79c38cd7f3d2cf3d85e73648a7bbacda46b779c7fe68bea"
i0, i1 = s324.index("def Hm(a, m):"), s324.index("for a, M in ((a1, 39)")
i2, i3 = s324.index("def forward(a, pot):"), s324.index("# ---------------- B: exact comparison")
ns324 = {}
exec(s324[i0:i1] + "\n" + s324[i2:i3], ns324)
forward, solve, Hm = ns324["forward"], ns324["solve"], ns324["Hm"]
ctx.prec = 400
fq = lambda v: fmpq(v.numerator, v.denominator)
tofr = lambda v: Fr(int(v.p), int(v.q))
rd = lambda dct: {int(k_): Fr(v) for k_, v in dct.items() if Fr(v) != 0}
asfr = lambda dct: {n: tofr(v) for n, v in dct.items() if v != 0}
put, add, scale, poisson, residuals = ns["put"], ns["add"], ns["scale"], ns["poisson"], ns["residuals"]


def anorm(F_):                    # circle L2 norm (arc length), arb
    s_ = sum((Fr(v) ** 2 for v in F_.values()), Fr(0))
    return (arb(s_.numerator) / s_.denominator * arb.pi()).sqrt()


OUT["B"] = {}
prev = None
for name, fn in ns["CANDS"]:
    t1 = time.monotonic()
    assert ns["sha"](HERE / "data" / fn) == ns["EXPECT"][name]
    dat = json.loads((T4R / f"data/{name}_third_repair.json").read_text())
    assert dat["candidate"] == name and Fr(dat["q3"]) == q3 and Fr(dat["c"]) == cF
    c_, chi = ns["load_file"](fn)
    assert tofr(c_) == cF
    delta, R, S = ns["build"](c_, chi)
    expo = lambda K, L: 1 - K * delta - 2 * L
    Th, Ps = ns["sectors"](R, S, delta)
    assert all(K >= 1 for K, L in Th) and all(K >= 1 for K, L in Ps)
    keys_all = [(K, L) for K in range(1, 17) for L in range(3)]
    keys_ge = [kk for kk in keys_all if expo(*kk) >= fq(qs)]
    F0 = residuals(Th, Ps, keys_ge + [(10, 0)], expo, c_)
    nz0 = sorted([kk for kk in keys_ge if F0[kk]], key=lambda kk: -float(expo(*kk)))
    # (i) the PROOF's recipe: (4,1) density and stream set to zero
    Th1 = {k_: dict(v) for k_, v in Th.items()}
    Ps1 = {k_: dict(v) for k_, v in Ps.items()}
    Th1[(4, 1)], Ps1[(4, 1)] = {}, {}
    F1 = residuals(Th1, Ps1, keys_ge, expo, c_)
    A3_i = asfr(F1[(5, 1)])
    # (ii) my algebraic branch-3 repair (REVIEW_T4_294, PROOF (6) of T4-294), rebuilt from the generators
    pp = 2 / c_
    A1 = {}
    for (j, nn), P_ in chi.items():
        if j == 3:
            v = pp * P_(fmpq(1)) - P_.derivative()(fmpq(1))
            if v != 0:
                A1[nn // 2] = v
    chi2 = dict(chi)
    for m, v in A1.items():
        ns["addto"](chi2, (3, 2 * m), -v * ns["tp"] ** (m + 4) * (1 - ns["tp"]))
    _, R2_, S2_ = ns["build"](c_, chi2)
    Th2, Ps2 = ns["sectors"](R2_, S2_, delta)
    F2 = residuals(Th2, Ps2, keys_ge, expo, c_)
    A3_ii = asfr(F2[(5, 1)])
    A3_t = rd(dat["residual_A3"])
    same_A3 = A3_i == A3_ii == A3_t
    assert same_A3 and A3_i != asfr(F0[(5, 1)])
    ge_i = {kk: asfr(F1[kk]) for kk in keys_ge if F1[kk]}
    ge_ii = {kk: asfr(F2[kk]) for kk in keys_ge if F2[kk]}
    assert ge_i == ge_ii and sorted(ge_i) == [(1, 2), (5, 1), (9, 0)]
    # third cutoff: B3, potential, density, stream
    B3 = {n: v / (1 - cF * q3) for n, v in A3_i.items()}
    a3 = q3 + 3
    M3 = (max(B3) - 1) // 2
    assert a3 != 0 and all(a3 != 2 * m and a3 != -2 * m for m in range(1, M3 + 1)) and all(Hm(a3, m) for m in range(M3 + 1))
    pot_t = rd(dat["potential_cosine_coefficients"])
    pot_m = solve(a3, B3)
    chk = {"A3_two_ways_and_c1t4_equal": same_A3, "A3_changed_by_first_cutoff": A3_i != asfr(F0[(5, 1)]),
           "B3_equals_density_B3": B3 == rd(dat["density_B3"]), "my_solve_equals_stored_potential": pot_m == pot_t,
           "forward_of_stored_potential_equals_B3": forward(a3, pot_t) == B3}
    st_m = asfr(poisson({n: fq(v) for n, v in B3.items()}, fq(q3)))
    st_t = rd(dat["stream_coefficients"])
    chk["stream_equals_my_poisson"] = st_m == st_t
    chk["stream_equals_minus_my_poisson"] = st_m == {n: -v for n, v in st_t.items()}
    assert chk["B3_equals_density_B3"] and chk["my_solve_equals_stored_potential"]
    assert chk["forward_of_stored_potential_equals_B3"] and (chk["stream_equals_my_poisson"] or chk["stream_equals_minus_my_poisson"])
    # the three-cutoff state
    B2 = {n: fq(v / (1 - cF * q2)) for n, v in asfr(F1[(9, 0)]).items()}
    Th3 = {k_: dict(v) for k_, v in Th1.items()}
    Ps3 = {k_: dict(v) for k_, v in Ps1.items()}
    assert not Th.get((9, 0)) and not Ps.get((9, 0))
    for kk, Bk, ek in (((9, 0), B2, expo(9, 0)), ((5, 1), {n: fq(v) for n, v in B3.items()}, expo(5, 1))):
        Th3[kk] = add(Th3.get(kk, {}), Bk)
        Ps3[kk] = add(Ps3.get(kk, {}), poisson(Bk, ek))
    below = sorted([kk for kk in keys_all if fq(qs) > expo(*kk) >= fq(qs) - fmpq(3, 4)], key=lambda kk: -float(expo(*kk)))
    F3 = residuals(Th3, Ps3, keys_ge + below, expo, c_)
    nz3 = [kk for kk in keys_ge if F3[kk]]
    end_t = rd(dat["endpoint_residual_unchanged"])
    F12_0 = asfr(F0[(1, 2)])
    assert nz3 == [(1, 2)] and asfr(F3[(1, 2)]) == F12_0 == end_t
    assert F12_0 == {n: -4 * cF * v for n, v in asfr(Th[(1, 2)]).items()}
    lead_same = all(Th3.get((K, 0), {}) == Th.get((K, 0), {}) for K in range(1, 9))
    assert lead_same
    nzb = [(kk, asfr(F3[kk])) for kk in below if F3[kk]]
    rows_below = [{"sector": list(kk), "exponent": float(expo(*kk)), "modes": len(F_), "norm": anorm(F_).str(15),
                   "same_as_original": F_ == asfr(F0[kk]) if kk in F0 else None} for kk, F_ in nzb]
    F100_orig = asfr(F0[(10, 0)])
    chk.update({"residual_sectors_ge_qstar_original": [list(kk) for kk in nz0],
                "residual_sectors_ge_qstar_after_first": [list(kk) for kk in sorted(ge_i, key=lambda kk: -float(expo(*kk)))],
                "residual_sectors_ge_qstar_after_three": [list(kk) for kk in nz3], "F12_unchanged": True,
                "leading_ladder_unchanged": lead_same, "potential_modes": len(pot_m), "top_density_mode": max(B3),
                "A3_norm": anorm(A3_i).str(30), "B3_norm": anorm(B3).str(30), "F12_norm": anorm(F12_0).str(20),
                "F100_original_norm": anorm(F100_orig).str(15) if F100_orig else "0",
                "below_qstar_after_three": rows_below, "A3_same_as_previous_candidate": prev is None or prev == A3_i,
                "seconds": time.monotonic() - t1})
    # (D) two-term endpoint coefficient after three cutoffs (REVIEW_T4_338 R3): a + s b, s = r^-epsilon
    ep = json.loads((T4R / f"source/{name}_endpoint.json").read_text())
    Th10 = Th[(1, 0)]
    Pm = asfr(add(scale(ns["sin_cos"](Th10, {2: fmpq(1)}), 1 / c_), ns["sin_cos"]({2: fmpq(1)}, ns["dsin"](Th10))))
    assert Pm == rd(ep["P"]) and F12_0 == rd(ep["F12"]) and asfr(Th10) == rd(ep["Theta0"])
    dot = lambda u, v: sum((u[n] * v.get(n, 0) for n in u), Fr(0))
    PP = dot(Pm, Pm)
    perp = lambda u: {n: u.get(n, 0) - dot(u, Pm) / PP * Pm.get(n, 0) for n in set(u) | set(Pm)}
    eps = qs - e(10, 0)
    assert eps == 9 * dF - 4
    De = 1 - cF * e(10, 0)
    F10 = asfr(F3[(10, 0)])
    av = {n: v / (4 * cF) for n, v in perp(F12_0).items()}
    bv = {n: v / De for n, v in perp(F10).items()}
    aa, ab, bb = dot(av, av), dot(av, bv), dot(bv, bv)
    assert dot(av, Pm) == 0 and dot(bv, Pm) == 0
    A_ = lambda v: arb(v.numerator) / v.denominator
    nrm = lambda v: (A_(v) * arb.pi()).sqrt()
    epsA = A_(eps)
    f_at = lambda sv: (A_(aa) + 2 * sv * A_(ab) + sv * sv * A_(bb)).sqrt() * arb.pi().sqrt()
    rows_r = []
    for k10 in (0, 3, 6, 12, 35, 100):
        sv = (-(epsA * k10) * arb(10).log()).exp()
        rows_r.append([k10, sv.str(10), f_at(sv).str(12)])
    Dd = {"d_over_4c": nrm(aa).str(20), "perp_F100_over_De": nrm(bb).str(20),
          "F12_over_4c": nrm(dot(F12_0, F12_0) / (16 * cF * cF)).str(15), "F100_over_De": nrm(dot(F10, F10) / De**2).str(15),
          "cosine_a_b": (A_(ab) / (A_(aa) * A_(bb)).sqrt()).str(15), "De": float(De), "eps": str(eps),
          "f_at_r_10k": rows_r}
    if ab < 0:
        s0 = -ab / bb
        Dd["s_min"] = A_(s0).str(15)
        Dd["f_min"] = nrm(aa - ab * ab / bb).str(15)
        Dd["log10_r_at_min"] = (-(A_(s0).log()) / epsA / arb(10).log()).str(12)
    else:
        Dd["s_min"], Dd["f_min"] = "0 (a.b >= 0: the coefficient is smallest at r = infinity)", nrm(aa).str(15)
    chk["D"] = Dd
    print("(D) %s: P, F_(1,2), Theta_(1,0) = c1-t4 endpoint data: True; d/(4c) = %s; ||F_(1,2)||/(4c) = %s;"
          " after three cutoffs ||F_(10,0)||/D_eps = %s, its part orthogonal to P %s, D_eps = %.6f;"
          " cos(a, b) = %s; min over s >= 0 of ||a + s b|| = %s at s = %s (log10 r = %s); ||a + s b|| at"
          " r = 10^k, s = r^-eps: %s"
          % (name, Dd["d_over_4c"], Dd["F12_over_4c"], Dd["F100_over_De"], Dd["perp_F100_over_De"], float(De),
             Dd["cosine_a_b"], Dd["f_min"], Dd["s_min"], Dd.get("log10_r_at_min", "-"),
             "; ".join("k = %d: %s" % (k10, fv) for k10, sv, fv in rows_r)))
    prev = A3_i
    na, nb = anorm(A3_i), anorm(B3)
    assert na.overlaps(arb(res4["rows"][["007", "013", "014"].index(name)]["A3_circle_norm"]))
    assert nb.overlaps(arb(res4["rows"][["007", "013", "014"].index(name)]["B3_circle_norm"]))
    OUT["B"][name] = chk
    print("(B) %s (%.1f s): residual sectors >= q*: original %s; after the first cutoff %s (recipe (i) = repair (ii));"
          " A3 (i) = (ii) = c1-t4: %s, changed by the first cutoff: %s; B3 = stored density: %s; my solve = stored"
          " potential (%d modes, m <= %d): %s; forward(stored potential) = B3: %s; stored stream = my Poisson stream:"
          " %s (negated: %s); after three cutoffs the only residual sector >= q* is %s, equal to the original F_(1,2)"
          " and to endpoint_residual_unchanged: True; ladder (K,0) unchanged: True"
          % (name, time.monotonic() - t1, nz0, sorted(ge_i, key=lambda kk: -float(expo(*kk))), same_A3,
             chk["A3_changed_by_first_cutoff"], chk["B3_equals_density_B3"], len(pot_m), max(pot_m),
             chk["my_solve_equals_stored_potential"], chk["forward_of_stored_potential_equals_B3"],
             chk["stream_equals_my_poisson"], chk["stream_equals_minus_my_poisson"], nz3))
    print("    ||A3|| = %s, ||B3|| = %s (overlap c1-t4), ||F_(1,2)|| = %s; A3 equal to the previous candidate's: %s;"
          " original ||F_(10,0)|| = %s; nonzero sectors in [q* - 3/4, q*) after three cutoffs: %s"
          % (na.str(15), nb.str(15), anorm(F12_0).str(12), chk["A3_same_as_previous_candidate"],
             chk["F100_original_norm"],
             "; ".join("(%d,%d) %.6f norm %s%s" % (rw["sector"][0], rw["sector"][1], rw["exponent"], rw["norm"],
                                                   "" if rw["same_as_original"] is None else
                                                   (" (= original)" if rw["same_as_original"] else " (changed)"))
                       for rw in rows_below)))
OUT["elapsed_s"] = time.monotonic() - T0
(HERE / "data/t4_338_review_results.json").write_text(json.dumps(OUT, indent=1))
print("done, %.1f s" % (time.monotonic() - T0))
