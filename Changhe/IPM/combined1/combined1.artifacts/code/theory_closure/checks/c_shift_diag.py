"""c-direction diagnostic for candidate 007 (c1-t1, theory_v03 section R, Lemma S remark).

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B c_shift_diag.py > c_shift_diag.out

At fixed rho the pairing with phi_P = y W^2 P(t) is affine in c:
  int F(rho; c') phi_P = I_P + (c' - c) J_P,  J_P = int (X.D rho) phi_P dX = (pi/2) sum_j int_0^1 t W^(a_j - 1) T_j(t) P(t) dt,
where rho = r sum_j W^(a_j) R_(j,n)(t) sin(n theta), d_r rho = sum_j W^(a_j) T_(j,n)(t) sin(n theta) (T = Top(R, a_j, 1)), and only
n = 1 meets y = r sin(theta). (r dr = dt/(2 W^2), r^2 = t/W.) The shift dc_P = -I_P/J_P would cancel the pairing of P.
If dc_P were nearly the same for all probes, the weak residual would look like a pure c error on that probe span.
Arb values (certified for the stated quantities); the interpretation is a diagnostic, not a distance bound: at c' != c the
far-field exponent changes, so rho itself is not a candidate at c'.
Inputs and field code: as check_T4182.py (same data/ copies; builder copied from c1-t2 weighted_weak_sharp.py).
"""
import json, sys
from pathlib import Path
exec(compile(Path("check_T4182.py").read_text().split("# ---------------- (4) checks against confirmed single-probe values")[0],
             "check_T4182_head", "exec"))
TR1 = {j: to_arb(Top(P, aj(j), 1)) for (j, n), P in R.items() if n == 1}


def J(Pa):
    return pi / 2 * sum((integ(T * Pa, 1, aj(j) - 1) for j, T in TR1.items()), arb(0))


rows = []
for k in list(range(0, 9)) + [128]:
    Pa = arb_poly([0] * k + [1])
    Ik, Jk = pairing(k), J(Pa)
    rows.append((f"t^{k}", Ik, Jk))
coef = {int(k): fmpq(*map(int, (v.split("/") + ["1"])[:2])) for k, v in T4["probe_coefficients"].items()}
Ip = sum((A(q) * pairing(k) for k, q in coef.items()), arb(0))
Pp = fmpq_poly([0])
for k, q in coef.items():
    Pp += q * tp**k
rows.append(("T4-182 vector", Ip, J(to_arb(Pp))))
print("probe            I_P                        J_P                        dc_P = -I_P/J_P")
for lab, Ik, Jk in rows:
    print(f"{lab:15s} {Ik.str(12):>26s} {Jk.str(12):>26s} {(-Ik / Jk).str(8):>22s}")
Path("c_shift_diag.json").write_text(json.dumps({lab: dict(I=Ik.str(25), J=Jk.str(25), dc=(-Ik / Jk).str(15)) for lab, Ik, Jk in rows}, indent=1))
