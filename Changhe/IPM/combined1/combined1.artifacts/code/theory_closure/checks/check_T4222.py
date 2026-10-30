"""c1-t1 R1-027: exact checks for T4-222 (finite tail amplitudes contain the fixed-c dilation orbit of 007).

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4222.py > check_T4222.out

1. First sine harmonics R_(j,1)(1), j = 0..7, of the 007 branch profiles Theta_j, computed exactly (fmpq) from the
   raw density generators (fields from the head of check_T4182.py, same data/ copies as tail_profiles_007.py), and
   compared for exact equality with the canonical-potential values first_sine_exact in c1-t4
   research/dilation_chart_audit/verification/result.json (read only; formula (5) of that PROOF.md).
2. Exact thresholds 1 + e_j = 1 + 1 - (j+1) delta, j = 3,2,1,0 (dimension drops of formula (4)), and their order.
3. Exact determinant of the 4 x 4 matrix z_i^k - 1, z = 2,3,4,5, k = 1..4.
Writes no file.
"""
import json
from pathlib import Path
exec(compile(Path("check_T4182.py").read_text().split("# ---------------- pairing forms (copied from c1-t2 PREP")[0], "h", "exec"))
from flint import fmpq_mat
RES = "RUN_ROOT/theory_audit_T4/research/dilation_chart_audit/verification/result.json"
import hashlib
print("c1-t4 result.json sha256", hashlib.sha256(Path(RES).read_bytes()).hexdigest())
ref = {b["j"]: fmpq(*map(int, b["first_sine_exact"].split("/"))) if "/" in b["first_sine_exact"]
       else fmpq(int(b["first_sine_exact"])) for b in json.loads(Path(RES).read_text())["branches"]}
ok = True
for jj in range(8):
    v = R[(jj, 1)](fmpq(1)) if (jj, 1) in R else fmpq(0)
    eq = (jj in ref) and (v == ref[jj])
    ok &= eq and v != 0
    print(f"j = {jj}: R_(j,1)(1) = {float(v):+.15e}; nonzero {v != 0}; equals c1-t4 canonical value exactly: {eq}")
thr = [1 + (1 - (j + 1) * delta) for j in (3, 2, 1, 0)]
order = all(thr[i] < thr[i + 1] for i in range(3)) and thr[0] > 0
print("thresholds 4g-2, 3g-1, 2g, 1+g:", [str(t) for t in thr], [f"{float(t):.12f}" for t in thr], "order 0<...:", order)
print("e_4 = 5 gamma - 4 =", f"{float(1 - 5 * delta):.12f}", "< -1:", 1 - 5 * delta < -1)
M = fmpq_mat(4, 4, [fmpq(z) ** k - 1 for z in (2, 3, 4, 5) for k in (1, 2, 3, 4)])
d = M.det()
print("det(z_i^k - 1), z = 2..5, k = 1..4:", d)
ok &= order and d == 288 and (1 - 5 * delta < -1)
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
