"""FLOATING (evidence only; lead 01:51Z): the four jets at the trial's source point P = (x_*, 0) of h = X3 - rho~ (X3 from its exact formula,
rho~ the certified modal trial):  z = h_y(P),  v = h_xy(P),  u = W[h]_1(P) = U_1[h](P) + x_* c[h]/3,  w = d_y W[h]_2(P) = d_y U_2[h](P) + c[h]/3,
with c[h] = psi[h]_xy(0) the raw strain of h and U[h] the canonical velocity of h (grid modal Green inverse src/inverse.py on a log-polar grid,
power-law tail fit).  On the axis (theta = 0): U_1[h] = -psi_y = -sum_n 2n psi_n/r;  d_y U_2[h] = d_y d_x psi = sum_n 2n (psi_n/r)';
h_y(x, 0) from the gradient arrays; h_xy = d_x h_y along the axis (spline derivative).  Also V_1^{X3}(x_*, 0) with the stored c_l and with the
canonical (1 + c[X3])/3, and the implied shift of X3's source point.
Usage: python3 src/x3_minus_trial_jets.py Nr Nt rmin_L rmax_L out.json
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import CubicSpline
from x3 import X3
from inverse import ModalInverse
from modal_fit import Trial
from trial_green import TrialGreen
from trial_jets import TrialJets
XS = 8.600063805157177


def main(Nr, Nt, rmin_L, rmax_L, out):
    t0 = time.time()
    X = X3(); L = X.L; k = X.k
    r = np.exp(np.linspace(np.log(rmin_L * L), np.log(rmax_L * L), Nr)); t = np.log(r)
    th = np.linspace(0, np.pi / 2, Nt + 1)
    F = X.rho(r, th); rho3, rho3x, rho3y = F["rho"], F["rho_x"], F["rho_y"]
    rho3x[:, -1] = 0.0
    print("X3 fields: %.0fs" % (time.time() - t0), flush=True)
    T = Trial(np.load("data/trial_v2_h0.008.npz")); G = TrialGreen(T); G.build(); J = TrialJets(G, K=1)
    rhoT = np.zeros_like(rho3); rhoTx = np.zeros_like(rho3); rhoTy = np.zeros_like(rho3)
    chunk = 1500
    for i0 in range(0, Nr, chunk):
        sl = slice(i0, min(Nr, i0 + chunk))
        E, RHO, PSI = J.eps_jets(t[sl], th, K=1)
        D = TrialJets.polar_to_cart(RHO, t[sl], th, 1)
        rhoT[sl] = RHO[(0, 0)]; rhoTx[sl] = D[(1, 0)]; rhoTy[sl] = D[(0, 1)]
    rhoTx[:, -1] = 0.0
    print("trial fields: %.0fs" % (time.time() - t0), flush=True)
    h = rho3 - rhoT; hx = rho3x - rhoTx; hy = rho3y - rhoTy
    print("sup|h| %.3e, sup|h|/sup|rho| %.3e" % (np.abs(h).max(), np.abs(h).max() / np.abs(rho3).max()), flush=True)
    inv = ModalInverse(r, th, p=6, tail_powers=[k - 1, 2 * k - 2, k - 3, 3 * k - 3], k=k, tail_decades=1.0)
    psi, dpsi, c_h = inv.solve(hx)            # psi_n^h(r) (Nr, Nt-1), psi_n' , c[h] = psi[h]_xy(0)
    n = inv.n.astype(float)
    print("inverse of h_x: %.0fs ; c[h] = %.6e" % (time.time() - t0, c_h), flush=True)
    # axis quantities as functions of r, then cubic-spline interpolation at x_*
    U1 = -(psi * (2 * n)[None, :]).sum(1) / r                      # -psi_y(r, 0)
    dyU2 = ((2 * n)[None, :] * (dpsi / r[:, None] - psi / r[:, None] ** 2)).sum(1)   # sum 2n (psi_n/r)'
    hy0 = hy[:, 0]
    cs_hy = CubicSpline(t, hy0); cs_U1 = CubicSpline(t, U1); cs_dyU2 = CubicSpline(t, dyU2)
    ts = np.log(XS)
    z = float(cs_hy(ts)); v = float(cs_hy(ts, 1) / XS)             # d_x = (1/r) d_t on the axis
    U1P = float(cs_U1(ts)); dyU2P = float(cs_dyU2(ts))
    u = U1P + XS * c_h / 3; w = dyU2P + c_h / 3
    # X3's own V_1 on the axis at x_* (stored c_l and canonical)
    invX = ModalInverse(r, th, p=6, tail_powers=[k - 1, 2 * k - 2, k - 3, 3 * k - 3], k=k, tail_decades=1.0)
    psiX, dpsiX, cX = invX.solve(rho3x)
    U1X = -(psiX * (2 * n)[None, :]).sum(1) / r; cs_U1X = CubicSpline(t, U1X)
    cl_stored = 1.0 / k; cl_canon = (1 + cX) / 3
    V1_stored = cl_stored * XS + float(cs_U1X(ts)); V1_canon = cl_canon * XS + float(cs_U1X(ts))
    wP = 10.1507252438                                                 # certified w'(P) of the trial (S1), for the shift estimate
    res = dict(Nr=Nr, Nt=Nt, rmin=float(r[0]), rmax=float(r[-1]), x_star=XS, sup_h=float(np.abs(h).max()), c_h=c_h, c_X3=cX, c_trial_target=float(3.0 / k - 1),
               z_hy=z, v_hxy=v, U1_h=U1P, dyU2_h=dyU2P, u_W1=u, w_dyW2=w, V1_X3_stored_cl=V1_stored, V1_X3_canonical_cl=V1_canon,
               cl_stored=cl_stored, cl_canonical_X3=cl_canon, shift_estimate_X3_root_minus_trial_root=-V1_canon / wP,
               note="FLOATING; grid modal Green inverse with power-law tail fit; jets on the axis by modal sums and cubic splines in t = log r")
    for kk, vv in res.items():
        if isinstance(vv, float): print("  %-42s %.6e" % (kk, vv))
    json.dump(res, open(out, "w"), indent=1)
    print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    a = sys.argv
    main(int(a[1]), int(a[2]), float(a[3]), float(a[4]), a[5])
