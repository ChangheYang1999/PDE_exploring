"""c1-t1 R1-033 review of T4-281 (c1-t4 research/compact_correction_tail): no compactly supported L^2 correction.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4281.py > check_T4281.out

Independent of c1-t4 code and of its canonical files.  Part A checks the kernel step of the T4-281 proof symbolically
(sympy): K = (-d_xy Phi, d_xx Phi) with Phi = -(log r)/(2 pi), its polar form, the singular values of DK (both equal to
1/(pi r^3)), the disk moment int_{|Y|<A} |Y|^2 dY = pi A^4/2 and the constant (8/pi) sqrt(pi/2) = 4 sqrt(2/pi).
Part B rebuilds the polar fields R = r sum v^(a_j) R_jn(t) sin(n theta), psi = r^2 sum v^(a_j) S_jm(t) sin(m theta)
of 007, 013 and 014 exactly (fmpq) from the raw c1-n1 generator snapshots with the c1-t2 constructor copied in
check_T4182.py, computes the first descendants D_(l,n) = -a_j R_jn(1) - R_jn'(1) and -a_j S_jm(1) - S_jm'(1), finds
the first branch with a nonzero density descendant, checks that every lower density and stream descendant vanishes,
that the exponent e = 1 - l delta - 2 exceeds gamma - 4 and that no two exponents 1 - l delta - 2q (1 <= l <= 16)
of different l coincide.  Part C compares the predicted residual coefficient (c e - 1) D_(l,n) of formula (4) with the
residual sector table that c1-n1 computed with its own code (sector_table.json of each snapshot, FLOAT coefficients):
an independent check of formula (4), including the factor (c e - 1).  Writes no file.
"""
import hashlib
import json
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

exec(compile(Path("check_T4182.py").read_text().split("# ---------------- pairing forms (copied from c1-t2 PREP")[0],
             "h", "exec"))

ok = True
# ---------------- Part A: kernel step (symbolic) ----------------
x, y = sp.symbols("x y", real=True)
rr, th, A_ = sp.symbols("r theta A", positive=True)
Phi = -sp.log(sp.sqrt(x ** 2 + y ** 2)) / (2 * sp.pi)
K1, K2 = -sp.diff(Phi, x, y), sp.diff(Phi, x, 2)
r2 = x ** 2 + y ** 2
okA = [sp.simplify(K1 - (-x * y / (sp.pi * r2 ** 2))) == 0,
       sp.simplify(K2 - (x ** 2 - y ** 2) / (2 * sp.pi * r2 ** 2)) == 0]
pol = {x: rr * sp.cos(th), y: rr * sp.sin(th)}
okA += [sp.simplify(K1.subs(pol) + sp.sin(2 * th) / (2 * sp.pi * rr ** 2)) == 0,
        sp.simplify(K2.subs(pol) - sp.cos(2 * th) / (2 * sp.pi * rr ** 2)) == 0]
DK = sp.Matrix([[sp.diff(K1, x), sp.diff(K1, y)], [sp.diff(K2, x), sp.diff(K2, y)]])
G = sp.simplify((DK.T * DK).subs(pol))
okA += [sp.simplify(G - sp.eye(2) / (sp.pi ** 2 * rr ** 6)) == sp.zeros(2, 2)]   # DK = (pi r^3)^-1 x orthogonal
okA += [sp.simplify(sp.integrate(sp.integrate(rr ** 2 * rr, (rr, 0, A_)), (th, 0, 2 * sp.pi)) - sp.pi * A_ ** 4 / 2)
        == 0,
        sp.simplify(8 / sp.pi * sp.sqrt(sp.pi / 2) - 4 * sp.sqrt(2 / sp.pi)) == 0]
okA += [sp.simplify(sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2)) == 0]                 # Phi harmonic off the origin
names = ["K1 = -xy/(pi r^4)", "K2 = (x^2-y^2)/(2 pi r^4)", "K1 polar", "K2 polar", "DK^T DK = I/(pi^2 r^6)",
         "int |Y|^2 = pi A^4/2", "(8/pi) sqrt(pi/2) = 4 sqrt(2/pi)", "Phi harmonic for r > 0"]
for n_, v in zip(names, okA):
    print(f"A  {n_}: {v}")
ok &= all(okA)

# ---------------- Part B and C: descendants of the three candidates ----------------
CANDS = [("007", "data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json",
          "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21",
          "data/c1n1_007_sector_table.json", "9d54471429323126d6270de5779ef6566f6753a1ce943bee65073be75b68f42a"),
         ("013", "data/c1n1_013_pairU_m16_exact.json",
          "c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940",
          "data/c1n1_013_sector_table.json", "bac5f78f424fa812c82f17e385a22ed0a6313039311c4b5b19a4f756e3e7d0a5"),
         ("014", "data/c1n1_014_pairB_m16_exact.json",
          "8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746",
          "data/c1n1_014_sector_table.json", "b1f237688d61cf98fb4f07ea9bddaf9beaa7c18fa8a443a86192a3a9ec74d0b7")]
F_ = lambda q: Fr(int(q.p), int(q.q))
for name, snap, ssha, tab, tsha in CANDS:
    SNAP = Path(snap)
    assert sha(SNAP) == ssha and sha(Path(tab)) == tsha
    c, chi = load()
    delta, R, S = build(c, chi)
    cF, dF = F_(c), F_(delta)
    gam = 1 / cF
    assert dF == 1 - gam
    nb = 1 + max(j for j, _ in list(R) + list(S))
    D, Sd = {}, {}
    for j in range(nb):
        aj = fmpq(j + 1) * delta / 2
        for (jj, n), P in R.items():
            if jj == j:
                v = F_(-aj * P(fmpq(1)) - P.derivative()(fmpq(1)))
                if v != 0:
                    D.setdefault(j, {})[n] = v
        for (jj, m), P in S.items():
            if jj == j:
                v = F_(-aj * P(fmpq(1)) - P.derivative()(fmpq(1)))
                if v != 0:
                    Sd.setdefault(j, {})[m] = v
    js = min(D)
    lstar = js + 1
    lower = all(j not in D and j not in Sd for j in range(js))
    e = 1 - lstar * dF - 2
    above = e > gam - 4
    # no coincidence of exponents 1 - l delta - 2q for different l in 1..16 (q integer): (l2 - l1) delta not in 2Z
    nocoin = all(((l2 - l1) * dF / 2).denominator != 1 for l1 in range(1, 17) for l2 in range(l1 + 1, 17))
    pred = {n: (cF * e - 1) * v for n, v in D[js].items()}
    print(f"{name}: c = {cF}, {nb} branches; density first descendants nonzero for branches j = {sorted(D)}, "
          f"stream first descendants nonzero for j = {sorted(Sd)}")
    print(f"  first nonzero density descendant: branch j = {js} (l* = {lstar}); all lower density and stream "
          f"descendants vanish: {lower}")
    print(f"  e = 1 - l* delta - 2 = {e} = {float(e):.12f} > gamma - 4 = {float(gam - 4):.12f}: {above}; "
          f"exponent noncoincidence for 1 <= l <= 16: {nocoin}")
    print(f"  D_(l*,n) nonzero for {len(D[js])} odd harmonics n = {min(D[js])} .. {max(D[js])}; "
          f"(c e - 1) D_(l*,1) = {float(pred.get(1, 0)):.13g}")
    tabd = json.loads(Path(tab).read_text())
    rows = [r_ for r_ in tabd["rows"] if Fr(r_["exponent_exact"]) == e]
    row = rows[0] if len(rows) == 1 else None
    fz = tabd["first_nonzero"]
    if row is None:
        print("  c1-n1 sector table: no unique row at e")
        okC = False
    else:
        cf = {int(k): v for k, v in (row["coefficients_float"] or {}).items()}
        rel = max(abs(float(pred.get(n, 0)) - cf.get(n, 0.0)) / max(abs(float(pred.get(n, 0))), 1e-300)
                  for n in set(cf) | set(pred))
        okC = (row["status"] == "EXACT-NONZERO" and row["max_harmonic"] == max(pred) and set(cf) == set(pred)
               and rel < 1e-9 and Fr(fz["exponent_exact"]) == e)
        print(f"  c1-n1 sector table at e: status {row['status']}, max harmonic {row['max_harmonic']}, first nonzero "
              f"sector of the table is this one: {Fr(fz['exponent_exact']) == e}; largest relative difference of "
              f"the {len(cf)} FLOAT coefficients from (c e - 1) D: {rel:.2e}")
        higher = [r_ for r_ in tabd["rows"] if Fr(r_["exponent_exact"]) > e and r_["status"] != "EXACT-ZERO"]
        print(f"  table rows above e that are not EXACT-ZERO: {len(higher)}")
        okC &= not higher
    okB = lower and above and nocoin and bool(pred)
    print(f"  checks B (descendants, exponent) {okB}; C (formula (4) against the c1-n1 table) {okC}")
    ok &= okB and okC
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
