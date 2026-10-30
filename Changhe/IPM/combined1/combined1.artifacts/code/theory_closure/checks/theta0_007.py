"""Leading far-field profile of candidate 007 (c1-t1 R1-023 remark R2). FLOAT print only; writes no file.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B theta0_007.py > theta0_007.out

rho = r sum_j W^(a_j) R_(j,l)(t) sin(l theta) with a_0 = delta/2, so rho = r^(1/c) Theta_0(theta) + o(r^(1/c)) with
Theta_0 = sum_l R_(0,l)(1) sin(l theta). Fields from the head of check_T4182.py (same data/ copies).
"""
from pathlib import Path
exec(compile(Path("check_T4182.py").read_text().split("# ---------------- pairing forms (copied from c1-t2 PREP")[0], "h", "exec"))
vals = {l: P(fmpq(1)) for (j, l), P in R.items() if j == 0}
print("j=0 modes:", sorted(vals))
for l in sorted(vals)[:12]:
    print(l, float(vals[l]))
print("max |R_(0,l)(1)|", max(abs(float(v)) for v in vals.values()))
