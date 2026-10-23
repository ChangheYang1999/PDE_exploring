"""taylor_resid.py -- residual Taylor coefficients at the origin from the jets (lead 00:08Z item 2; identities confirmed by the verifier 00:19Z):
R = r01 y + r21 x^2 y + r03 y^3 + ..., psi = s0 x y + q1 x^3 y + q2 x y^3 + ..., C0 = c_l + s0 - 1 (s0 = c):
  r01 = a0 C0,  r21 = (2A - C0) b + 3 a0 q1,  r03 = (2 + 3 C0) e + a0 q2;  (T1) defect 6e - (a0 - 2A) b = r21 + 3 r03 - C0 (9e - b) - 3 a0 P,
  (T2) defect (q1 - q2) - (a0 - 4A) b/(3 a0) = 2 (r21 + C0 b)/(3 a0) - P,  P = q1 + q2 + b/3 (Poisson defect of the discrete state).
usage: python3 src/taylor_resid.py states..."""
import sys, math
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
from local_exponent import jets
print(f"{'state':>26s} {'N':>4s} {'a0':>10s} {'C0':>10s} {'r01':>10s} {'r21':>10s} {'r03':>10s} {'P':>10s} {'T1 defect':>10s} {'T1 via r':>10s} {'T2 defect':>10s} {'T2 via r':>10s}")
for f in [a for a in sys.argv[1:] if '=' not in a]:
    S = qdiag.State(f); cl = S.cl; A = 2 * cl - 1
    a0, b, e, c, q1, q2 = jets(S); C0 = cl + c - 1; P = q1 + q2 + b / 3
    r01 = a0 * C0; r21 = (2 * A - C0) * b + 3 * a0 * q1; r03 = (2 + 3 * C0) * e + a0 * q2
    T1 = 6 * e - (a0 - 2 * A) * b; T1r = r21 + 3 * r03 - C0 * (9 * e - b) - 3 * a0 * P
    T2 = (q1 - q2) - (a0 - 4 * A) * b / (3 * a0); T2r = 2 * (r21 + C0 * b) / (3 * a0) - P
    print(f"{f.split('/')[-1]:>26s} {S.N:4d} {a0:10.5f} {C0:+10.3e} {r01:+10.3e} {r21:+10.4f} {r03:+10.4f} {P:+10.3e} {T1:+10.4f} {T1r:+10.4f} {T2:+10.4f} {T2r:+10.4f}")
