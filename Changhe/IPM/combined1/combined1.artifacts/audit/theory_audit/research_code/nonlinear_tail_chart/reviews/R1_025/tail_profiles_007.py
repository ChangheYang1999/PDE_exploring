"""Far-field branch profiles of candidate 007 (c1-t1 R1-025 remark R3). Exact test of nonvanishing; writes no file.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B tail_profiles_007.py > tail_profiles_007.out

rho = r sum_(j,l) W^((j+1) delta/2) R_(j,l)(t) sin(l theta), W = 1/(1+r^2), t = 1 - W, so branch j has leading term
r^(1 - (j+1) delta) Theta_j(theta), Theta_j = sum_l R_(j,l)(1) sin(l theta). The script evaluates R_(j,l)(1) exactly
(fmpq) and reports, for j = 0..7, the exponent 1 - (j+1) delta, whether Theta_j is nonzero (some exact coefficient
nonzero) and the largest |R_(j,l)(1)|. Fields from the head of check_T4182.py (same data/ copies).
"""
from pathlib import Path
exec(compile(Path("check_T4182.py").read_text().split("# ---------------- pairing forms (copied from c1-t2 PREP")[0], "h", "exec"))
for jj in range(8):
    vals = {l: P(fmpq(1)) for (j, l), P in R.items() if j == jj}
    nz = [l for l, v in vals.items() if v != 0]
    e = 1 - (jj + 1) * delta
    big = max((abs(float(v)) for v in vals.values()), default=0.0)
    print(f"j = {jj}: exponent 1 - (j+1) delta = {float(e):+.6f}; modes {len(vals)}; Theta_j nonzero (exact): {bool(nz)};"
          f" lowest nonzero l {min(nz) if nz else None}; max |R_(j,l)(1)| = {big:.6e}")
