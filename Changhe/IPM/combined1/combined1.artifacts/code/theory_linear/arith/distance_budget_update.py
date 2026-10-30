"""Distance budgets of the c1 frameworks against the CONFIRMED fixed-c L2 distances, and directed q bounds for the
FW-T-T4L2-defect-v1 sample boxes (corrections to reviews/REVIEW_T4ALT.md after c1-t4 T4-064 and T4-065).

Run from artifacts/:  python3 -B arith/distance_budget_update.py
Needs python-flint.  Under a second.

(1) For a scalar-gap family beta = mu0 - C s - c_U r/sqrt(s) > 0 the radius is r < (mu0 - C s) sqrt(s)/c_U; its supremum
    over s > 0 is (2 mu0/3) sqrt(mu0/(3C))/c_U at s* = mu0/(3C).  An L2 correction then has ||h||_2 <= r/sqrt(w2).
    Graded boxes (T4-013): ||h||_2 < sup_s sqrt(s)(1/2 - 4708 s)/(217/50) (Proposition G, REVIEW_R1_004_GRADED.md).
(2) Ratios against the CONFIRMED distances (fixed c, every L2 distributional divergence-form correction):
    d2 > 0.0027197370 (N4-057, T4-048), > 0.0029920 (T4-048, N4-061), > 0.29552675 (N4-065, T4-064);
    Mpen2 > 0.55006675 (N4-065, T4-064).  The lower bounds are entered rounded down.
(3) Directed upper bounds for q <= c_s r/2, c_s = (4 pi s (1+s))^(-1/2), for the five R3 sample boxes.
"""
import sys
from fractions import Fraction as Q

from flint import arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 256


def A(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


fams = (("baseline-gap balls (A2, T4ALT)", Q(1, 10), 4800, Q(5), 512),
        ("FW-T-TB-rebal-v1", Q(297, 1000), 4800, Q(5), 512),
        ("FW-T-TB-sharp-v1", Q(297, 1000), 402, Q(8, 5), 512),
        ("FW-T-T4L2-sharp-v1", Q(259, 1000), 401, Q(8, 5), 512),
        ("FW-T-T4L2-sharpw-v1", Q(97, 250), 397, Q(8, 5), 1024))
dists = (("d2 N4-057", Q(27197370, 10**10)), ("d2 T4-048", Q(29920, 10**7)),
         ("d2 T4-064", Q(29552675, 10**8)), ("Mpen2 T4-064", Q(55006675, 10**8)))
print("(1), (2) L2 radius budget and ratio (distance / budget); > 1 means no exact solution in any ball of the family")
print("    " + "framework".ljust(34) + "s*".ljust(14) + "L2 budget".ljust(28) + "".join(n.ljust(15) for n, _ in dists))
rows = []
for name, mu0, C, cU, sw2 in fams:
    sstar = mu0 / (3 * C)
    rsup = (2 * A(mu0) / 3) * (A(mu0) / (3 * C)).sqrt() / A(cU)
    l2 = rsup / sw2
    rows.append((name, str(sstar), l2))
g = A(Q(50, 217)) * A(Q(1, 3)) / arb(28248).sqrt()
rows.append(("graded / gradedL2 boxes (Prop. G)", "1/28248", g))
for name, ss, l2 in rows:
    rat = [A(d) / l2 for _, d in dists]
    assert all(x > 1 for x in rat)
    print("    " + name.ljust(34) + ss.ljust(14) + l2.str(5).ljust(28)
          + "".join(f"{float(x.mid().str(8, radius=False)):.4g}".ljust(15) for x in rat))
print("    all ratios > 1: d2 and Mpen2 have no exact fixed-c solution in any ball or box of these families")

print("(3) directed upper bounds for the L2 contraction q <= c_s r/2 of the FW-T-T4L2-defect-v1 sample boxes")
boxes = (("sharpw", Q(1, 5184), "m = 0, B = 0", Q(201799, 149299200)),
         ("sharpw", Q(1, 5184), "m = 2^-12, B = 1/100", Q(143, 100000)),
         ("sharpw", Q(1, 5184), "m = 2^-10, B = 1/100", Q(449, 250000)),
         ("sharp", Q(1, 7744), "m = 0, B = 0", Q(200587, 272588800)),
         ("sharp", Q(1, 7744), "m = 2^-12, B = 1/100", Q(411, 500000)))
pi = arb.pi()
for name, s, lab, r in boxes:
    cs = 1 / (4 * pi * A(s) * (1 + A(s))).sqrt()
    qv = cs * A(r) / 2
    up = Q(int((qv.upper() * 10**5).floor().unique_fmpz()) + 1, 10**5)
    assert qv < A(up)
    print(f"    {name:6s} s = {s}, {lab:22s} r = {r}: q in {qv.str(10)}, q < {float(up):.5f}")
print("done")
