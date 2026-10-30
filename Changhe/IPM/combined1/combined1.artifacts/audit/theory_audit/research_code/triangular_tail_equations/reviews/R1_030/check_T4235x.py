"""c1-t1 R1-030 cross-check of T4-235 by a raw-generator path (theory-lane cross-check, not the N4 confirmation).

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4235x.py > check_T4235x.out

The 007 density and stream endpoint profiles Theta_j = sum_n R_(j,n)(1) sin(n t), Psi_j = sum_n S_(j,n)(1) sin(n t)
are computed exactly (fmpq) from the raw c1-n1 generator snapshot with the head of check_T4182.py (the route of
check_T4222.py, not the canonical potential of c1-t4).  Then, with the independent exact Fourier code of
check_T4234.py: (a) Psi_j solves the angular Poisson equation (1) of T4-234 for j = 0..3; (b) the recurrence (4)
seeded with Theta_0 alone reproduces Theta_1, Theta_2, Theta_3 exactly; (c) the counts of nonzero harmonics and the
largest harmonic are printed for comparison with T4-235 (20, 30, 40 through 39, 59, 79).  Writes no file.
"""
from fractions import Fraction as Fr
from pathlib import Path
exec(compile(Path("check_T4182.py").read_text().split("# ---------------- pairing forms (copied from c1-t2 PREP")[0],
             "h", "exec"))
src = Path("check_T4234.py").read_text()
exec(compile(src[src.index("def add("):src.index("theta0 = {")], "f", "exec"))

F = lambda q: Fr(int(q.p), int(q.q))
cF = F(c)
deltaF = 1 - 1 / cF
assert F(delta) == deltaF
Th, Ps = {}, {}
for (j, n), P in R.items():
    v = F(P(fmpq(1)))
    if v != 0:
        Th.setdefault(j, {})[n] = v
for (j, n), P in S.items():
    v = F(P(fmpq(1)))
    if v != 0:
        Ps.setdefault(j, {})[n] = v
e = [1 - (j + 1) * deltaF for j in range(8)]
N = sum(1 for j in range(8) if e[j] >= -1)
print(f"c = {cF} = {float(cF):.15f}; N = {N}; branches with nonzero density endpoint: {sorted(Th)}")
ok = N == 4
for j in range(N):
    th = Th.get(j, {})
    print(f"Theta_{j}: {len(th)} nonzero odd harmonics, largest {max(th) if th else None}; "
          f"Psi_{j}: {len(Ps.get(j, {}))} nonzero even harmonics")
    pj = psi_from(th, e[j])
    good = pj == Ps.get(j, {})
    ok &= good
    print(f"  (a) Psi_{j} equals the unique sine-even solution of (1): {good}")
_, _, th_rec, _ = tails(cF, Th[0])
for j in range(1, N):
    good = th_rec[j] == Th.get(j, {})
    ok &= good
    print(f"  (b) recurrence (4) from Theta_0 alone reproduces Theta_{j}: {good}")
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
