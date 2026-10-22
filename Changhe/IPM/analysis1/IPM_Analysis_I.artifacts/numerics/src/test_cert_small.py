"""Consistency test of the certificate machinery on the truncated trial (M = 20): Taylor-model residual (cert_resid) vs
the floating closed-form pipeline (trial_green), and the rigorous scalars (cert_scalars) vs float Newton."""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen
from cert_resid import Certifier
from cert_scalars import ScalarCert
from flint import arb

green = "data/cert_small_green.npz"; trial = "data/trial_small_M20.npz"
T = Trial(np.load(trial)); G = TrialGreen(T); G.build()
C = Certifier(green, trial, Q=12)
print("Certifier: nc = %d, Nf = %d, M = %d" % (C.nc, C.Nf, C.M))
# compare boundary values A, B (Arb export) with the float pipeline at a few sub-cell boundaries
for ci in (0, 1000, 4000, C.nc):
    t = C.tb.m[ci]
    Af, Bf = G.AB_at(np.array([t]))
    da = np.abs(Af[0] - C.A.m[ci]) / (np.abs(C.A.m[ci]).max() + 1e-300); db = np.abs(Bf[0] - C.B.m[ci]) / (np.abs(C.B.m[ci]).max() + 1e-300)
    print("boundary %d (r=%.4g): max rel diff A %.2e, B %.2e; max rel radius A %.1e B %.1e" % (ci, np.exp(t), da.max(), db.max(), (C.A.r[ci] / (np.abs(C.A.m[ci]) + 1e-300)).max(), (C.B.r[ci] / (np.abs(C.B.m[ci]) + 1e-300)).max()))
# cells: TM at midpoint vs float eps_N
for ci in (10, 2000, 4500, 6000, C.nc - 1):
    t0 = time.time(); row = C.cell(ci); dt = time.time() - t0
    ta = C.tb.m[ci]; h = C.tb.m[ci + 1] - ta; tm = ta + 0.5 * h
    eps_f = G.residual_modes(np.array([tm]))[0]           # (2M+3,)
    # evaluate the TM polynomial at tau = h/2 (recompute inside: replicate via C internals is heavy; use the returned sup bounds instead)
    W_float = np.abs(eps_f).sum()
    print("cell %d r=%.4g h=%.4f: W bound %.4e vs float W(mid) %.4e (ratio %.3f); sup_eps bound %.3e vs float max|eps_N| %.3e; remA %.1e remB %.1e rem_eps %.1e; %.2fs" % (
        ci, np.exp(ta), h, row["W"], W_float, row["W"] / W_float, row["sup_eps_max"], np.abs(eps_f).max(), row["remA"], row["remB"], row["rem_eps"], dt))
# scalars
S = ScalarCert(green, trial)
tstar, ok = S.find_xstar(x_guess=8.6)
V1, mu, g = S.axis(tstar)
print("x_* (truncated trial):", tstar.exp().str(18), "contracted:", ok, " V1:", V1.str(3), " mu-1:", (mu - 1).str(6), " g_*:", g.str(12))
# float check of x_* for the truncated trial: root of V1(x,0) = c_l x - sum 2n psi_n / x
from scipy.optimize import brentq
def V1f(x):
    psi, dpsi = G.psi_at(np.array([np.log(x)]))
    return G.c_l * x - (2 * G.n * psi[0]).sum() / x
xs = brentq(V1f, 7.0, 10.0, xtol=1e-14)
print("float x_* =", repr(xs))
