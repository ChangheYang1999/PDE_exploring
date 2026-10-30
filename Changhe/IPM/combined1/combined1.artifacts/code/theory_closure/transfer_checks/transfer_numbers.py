"""Arithmetic behind the S1 entries of hou_literature/TRANSFER_MATRIX.md (c1-t1, T1).

All inputs are state 131 values (c_l = 1.81032, a0 = 10.30) and published thresholds of theory_v01.
Exact rational arithmetic where the statement is exact given (B0n) c_l + c[rho] = 1; floats elsewhere.

Usage (from artifacts/transfer_checks):
  OMP_NUM_THREADS=1 python3 -B transfer_numbers.py > transfer_numbers.out
"""
import math
from fractions import Fraction as Q

cl = Q(181032, 100000)
a0 = Q(1030, 100)
gam = 1 / cl
c = 1 - cl                      # c[rho] from (B0n)
a1, a2 = cl - c, cl + c         # grad b(0) = diag(a1, a2), b = c_l X + Ubar
print("1. Linear data at the origin (EXACT given (B0n) and state 131 c_l, a0)")
print(f"   c[rho] = 1 - c_l = {float(c):.5f}; grad b(0) = diag({float(a1):.5f}, {float(a2):.5f}); a1 + a2 = 2 c_l = {float(a1 + a2):.5f}")
print(f"   forward (Chen-Hou direction) local coefficients: eta {float(1 - cl + c):.5f}, xi {float(1 - cl - c):.5f}")

print("2. Transport-only D^2 rates at the origin in the S1 direction d_t h = L h (h = e^(-t) h0(e^(a1 t) x, e^(a2 t) y); the L^2 Jacobian gives e^(-c_l t))")
for name, a in (("d_xx", a1), ("d_yy", a2)):
    print(f"   ||{name} h||_2 ~ exp(({float(2 * a - 1 - cl):+.5f}) t)")
print("3. (B5) matrix M_2 at the origin: (1 + c_l) I - 2 diag(a1, a2) + A(0), A(0) = diag(a0, 0) (V.grad log omega = 0 at 0)")
m11 = 1 + cl - 2 * a1 + a0
m22 = 1 + cl - 2 * a2
print(f"   M_2(0) = diag({float(m11):.5f}, {float(m22):.5f}); transport part of the (1,1) entry {float(1 + cl - 2 * a1):.5f};"
      f" (B5) needs >= 1/2: {m11 >= Q(1, 2) and m22 >= Q(1, 2)}")

print("4. Taylor-mode count for vanishing order k (S1 class: x^a y^b, a even, b odd)")
for k in (3, 5, 9, 13, 15, 25):
    print(f"   k = {k:2d}: modes of degree < k: {sum((d + 1) // 2 for d in range(1, k, 2))}")

print("5. Back-of-envelope vanishing order (HEURISTIC, extraction Part I 17.1 M3)")
cmax = Q(253, 100)
need_linf = Q(515, 100) + a0 * (cmax - Q(1, 2)) - Q(162, 100) - Q(1, 2)
print(f"   C^(1/2) y-axis balance: k > 5.15 + a0 (2.53 - 1/2) - 1.62 - 1/2 = {float(need_linf):.2f}")
print(f"   L^2 block: k > a0 + 1.81 - 1/2 (y-stretching bonus) ~ {float(a0 + cl - Q(1, 2)):.2f}")

print("6. FW-T-T4L2-v1 radius with and without the 1/sqrt(s) rough loss (HEURISTIC scaling only)")
s = 2.0 ** -17
beta = 1 / 9.72
r_now = math.sqrt(s) * (0.25 - 4800 * s - beta) / 5
r_free = (0.25 - beta) / 5
print(f"   with loss (s = 2^-17): r <= {r_now:.4e} (published r = 2^-14 = {2 ** -14:.4e})")
print(f"   if the rough constant were 5 instead of 5/sqrt(s) (s -> 0): r <= {r_free:.4e}; ratio {r_free / 2 ** -14:.0f}")
print(f"   d2 gap against FW-T-T4L2-v1 (theory_v01 sec. 7): X_s(F)/eta >= 4.2e8; remaining after this ratio: {4.2e8 / (r_free / 2 ** -14):.2e}")

print("7. Hou-Nguyen-Wang AM-GM step (2404.09410 l.233): min over S > 0 of 0.002 S + 8 S^-2")
S = 20
print(f"   at S = 20: {0.002 * S + 8 / S ** 2:.4f} >= 0.048, margin {0.002 * S + 8 / S ** 2 - 0.048:.4f}")

print("8. Weight windows (exponent sigma of r^-sigma at infinity; rate 1 + c_l(1 - k - sigma) in the S1 direction)")
for k, name in ((-1, "Hdot^-1"), (0, "L^2"), (1, "gradient"), (2, "Hessian")):
    print(f"   {name:>8}: sigma < {float(1 - k + gam):.4f}")
print(f"   forward (Chen-Hou) h-level window: weight r^-p with gamma = {float(gam):.4f} < p < 1;"
      f" eta-level exponent s in ({float(gam - 1):.4f}, 0)")
