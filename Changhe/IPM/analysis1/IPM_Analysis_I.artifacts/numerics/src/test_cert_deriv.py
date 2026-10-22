"""Test of the derivative Taylor models on the small trial: compare the TM polynomial values of d_t^i eps_N at the cell
midpoint (via sup bounds) against finite differences of the float residual modes (trial_green)."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen
from cert_resid import Certifier
green = "data/cert_small_green.npz"; trial = "data/trial_small_M20.npz"
T = Trial(np.load(trial)); G = TrialGreen(T); G.build()
C = Certifier(green, trial, Q=12)
for ci in (2000, 4500, 6000):
    t0 = time.time(); row = C.cell_deriv(ci, nder=2); dt = time.time() - t0
    ta = C.tb.m[ci]; h = C.tb.m[ci + 1] - ta; tm = ta + 0.5 * h; d = 1e-4
    e0 = G.residual_modes(np.array([tm]))[0]; ep = G.residual_modes(np.array([tm + d]))[0]; em = G.residual_modes(np.array([tm - d]))[0]
    e1 = (ep - em) / (2 * d); e2 = (ep - 2 * e0 + em) / d ** 2
    print("cell %d r=%.4g (%.2fs): W_0_0 %.3e vs float %.3e | W_1_0 %.3e vs float sum|d_t eps| %.3e | W_2_0 %.3e vs %.3e | W_0_1 %.3e vs %.3e | eps-dteps %.3e vs %.3e | W_K %.3e | remA %.1e" % (
        ci, np.exp(ta), dt, row["W_0_0"], np.abs(e0).sum(), row["W_1_0"], np.abs(e1).sum(), row["W_2_0"], np.abs(e2).sum(),
        row["W_0_1"], (np.abs(e0) * (2 * np.arange(len(e0)) + 1)).sum(), row["W_eps_minus_dteps"], np.abs(e0 - e1).sum(), row["W_K"], row["remA"]))
    # K~ float: modes R - Rt at tm
    R, Rt = G.rho_modes(np.array([tm])); print("      float sum|R - Rt| = %.3e" % np.abs(R - Rt).sum())
