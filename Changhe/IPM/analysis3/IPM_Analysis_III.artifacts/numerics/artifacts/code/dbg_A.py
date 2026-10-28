import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "src"))
import numpy as np
from flint import arb, fmpq, ctx
from exact_trial import ExactTrial, ExpPoly, q2arb, integrate_ep, moment_left
FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "data", "trial_small_M20.npz")
T = ExactTrial.from_npz(FIX, prec=200); T.build_green(verbose=False)
from modal_fit import Trial; from trial_green import TrialGreen
Tf = Trial(dict(np.load(FIX))); Gf = TrialGreen(Tf); Gf.build()
print("float A_n(t_-):", Gf.A[0][:4]); print("exact A_n(t_-):", [T.A[0][i].str(12) for i in range(4)])
print("float B_n(t_-):", Gf.B[0][:4]); print("exact B_n(t_-):", [T.B[0][i].str(12) for i in range(4)])
fin = T.fhat_from_Rhat(T.Rhat_from_a(T.a_inner()))
for n in (1, 2, 3):
    f = fin[n - 1]
    direct = (4 * T.t_lo).exp() * integrate_ep(f.mul_exp(fmpq(2 * n + 4)), "minf")
    s0 = arb(-3) / 2; f0 = f.shift(s0); ta = T.t_lo + s0
    A = (4 * ta).exp() * integrate_ep(f0.mul_exp(fmpq(2 * n + 4)), "minf")
    for (s, h) in ((arb(-3) / 2, arb(1)), (arb(-1) / 2, arb(1) / 2)):
        fs = f.shift(s); tb = T.t_lo + s + h
        inc = arb(0)
        for e, cs in fs.terms.items():
            lam = q2arb(e) + (2 * n + 4)
            for p_, cp in enumerate(cs):
                if cp != 0: inc += cp * moment_left(lam, p_, h)
        A = (-2 * n * h).exp() * A + (4 * tb).exp() * inc
    print("n=%d direct %s split %s diff %s" % (n, direct.str(15), A.str(15), (A - direct).str(5, radius=True)))
    x = arb(-7) / 10
    print("   shift check f(-0.7) = %s ; f0(0.8) = %s ; f_{-1/2}(-0.2) = %s" % (f(x).str(12), f0(x + arb(3) / 2).str(12), f.shift(arb(-1) / 2)(x + arb(1) / 2).str(12)))
    print("   exponents of f:", sorted(float(q2arb(e)) for e in f.terms), " degrees:", [len(c) - 1 for e, c in sorted(f.terms.items(), key=lambda kv: float(q2arb(kv[0])))])
