"""Rigorous scalars of the trial on the Taylor models (SPEC item S1): x_* (root of V_1(x,0)), mu - 1 = d_y V_2(P) - 1,
g_* = rho_y(P), A = 2 c_l - 1, c (from cert_green), c_l = 1/k.
On the x-axis (theta = 0), with tau the local variable of the sub-cell containing x_*:
  V_1(x,0) = c_l x - (1/x) sum_n 2n psi_n,             x = e^{t_a} e^{tau}
  d/dt (x V_1) = x V_1 + x dV_1/dt = 2 c_l x^2 - sum_n 2n dpsi_n/dt,   dpsi_n/dt = (B_n - A_n)/2   (Newton derivative of F = x V_1)
  mu(x)    = c_l + (1/x^2) sum_n 2n [ (B_n - A_n)/2 - psi_n ]
  g(x)     = (1/x) sum_j (2j+1) R_j
Interval Newton in tau on the TM polynomials (+ remainders) of these quantities.
Usage: python3 cert_scalars2.py data/cert_green.npz trial.npz out.json [x_guess]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial
from midrad import MR, succ, U
from cert_resid import Certifier, TMArr, tm_exp, mag


def tm_eval(tm, tau, hpow_sup=None):
    """Enclosure of sum_i c_i tau^i + [-rem, rem] for an MR scalar/interval tau (Horner); tm: TMArr with coefficients (S, Q+1)."""
    Q = tm.Q; c = tm.c
    val = MR(np.zeros(c.m.shape[:-1]), np.zeros(c.m.shape[:-1]))
    for i in range(Q, -1, -1):
        val = val * tau + c[..., i]
    return MR(val.m, succ(val.r + tm.r))


def axis_tms(C, ci):
    """TMs (over the cell) of x V_1(x,0), x dV_1/dt (times x to avoid 1/x), x^2 (mu - c_l), x g(x), using C.cell(ci)."""
    C.cell(ci); T = C._last_tms
    A, B, psi, Rj = T["A"], T["B"], T["psi"], T["Rj"]; hpow = T["hpow"]; Q = C.Q
    n = C.n[:, None]
    def tm_sum(tm):                     # sum over the mode axis
        return TMArr(MR(tm.c.m.sum(0), succ(tm.c.r.sum(0) * (1 + tm.c.m.shape[0] * U) + succ(tm.c.m.shape[0] * U * np.abs(tm.c.m).sum(0)))), succ(tm.r.sum() * (1 + tm.c.m.shape[0] * U)))
    S_psi = tm_sum(TMArr(psi.c * MR(2.0 * n, 0.0), succ(psi.r * 2.0 * n[:, 0])))                      # sum 2n psi_n
    half = MR.exact(0.5)
    dpsi_dt = (B - A).scale(half)
    S_dpsi = tm_sum(TMArr(dpsi_dt.c * MR(2.0 * n, 0.0), succ(dpsi_dt.r * 2.0 * n[:, 0])))             # sum 2n dpsi_n/dt
    S_mu = tm_sum(TMArr((dpsi_dt - psi).c * MR(2.0 * n, 0.0), succ((dpsi_dt - psi).r * 2.0 * n[:, 0])))
    twoj1 = (2.0 * np.arange(C.M + 1) + 1.0)[:, None]
    S_g = tm_sum(TMArr(Rj.c * MR(twoj1, 0.0), succ(Rj.r * twoj1[:, 0])))
    Rtj = T["Rtj"]; dRmR = Rtj - Rj
    S_gp = tm_sum(TMArr(dRmR.c * MR(twoj1, 0.0), succ(dRmR.r * twoj1[:, 0])))        # sum (2j+1)(dR_j/dt - R_j)  -> g' = e^{-2t} S_gp
    # x = e^{t_a} e^{tau}: TM of e^{tau} and e^{2 tau}
    e_ta = T["e_ta"]; E1c, E1r = tm_exp(1.0, T["h_up"], Q); E2c, E2r = tm_exp(2.0, T["h_up"], Q)
    E1 = TMArr(MR(E1c.m[None, :], E1c.r[None, :]), np.array([E1r])); E2 = TMArr(MR(E2c.m[None, :], E2c.r[None, :]), np.array([E2r]))
    def as_row(tm): return TMArr(MR(tm.c.m[None, :], tm.c.r[None, :]), np.array([tm.r]))
    x2 = E2.scale(e_ta * e_ta)                                                 # x^2 as TM (row)
    xV1 = x2.scale(C.c_l) - as_row(S_psi)                                      # x V_1 = c_l x^2 - sum 2n psi_n
    xdV1 = x2.scale(C.c_l) + as_row(S_psi) - as_row(S_dpsi)                     # x dV_1/dt
    dF = xV1 + xdV1                                                            # d/dt (x V_1) = x V_1 + x dV_1/dt  (verifier 15:24Z)
    return dict(xV1=xV1, xdV1=dF, S_mu=as_row(S_mu), S_g=as_row(S_g), S_gp=as_row(S_gp), x2=x2, E1=E1, e_ta=e_ta, h_up=T["h_up"])


def main(green, trial, out, x_guess=8.600063803):
    t0 = time.time(); C = Certifier(green, trial, Q=12)
    tb = C.tb.m; t_guess = np.log(x_guess)
    ci = int(np.searchsorted(tb, t_guess, side="right") - 1)
    tm = axis_tms(C, ci); h_up = tm["h_up"]
    # float Newton on the TM polynomial for the midpoint start
    tau = t_guess - tb[ci]
    for _ in range(6):
        F = tm_eval(tm["xV1"], MR.exact(np.array([tau]))).m[0]; dF = tm_eval(tm["xdV1"], MR.exact(np.array([tau]))).m[0]
        tau = tau - F / dF
    assert 0 <= tau <= h_up, "root left the cell: %g not in [0, %g]" % (tau, h_up)
    ok = False
    for eps in (1e-8, 1e-10, 1e-12, 1e-14):
        I = MR(np.array([tau]), np.array([eps]))
        Fm = tm_eval(tm["xV1"], MR.exact(np.array([tau]))); dFI = tm_eval(tm["xdV1"], I)
        lo_d, hi_d = float(dFI.lower()[0]), float(dFI.upper()[0])
        if lo_d <= 0 <= hi_d: continue
        dmin = min(abs(lo_d), abs(hi_d))
        q = float(Fm.m[0]) / float(dFI.m[0])
        q_r = succ(succ(float(Fm.r[0]) / dmin) + succ(abs(float(Fm.m[0])) * float(dFI.r[0]) / dmin ** 2) + 4 * U * abs(q))
        Nt = MR(np.array([tau - q]), np.array([succ(q_r + U * abs(tau))]))
        if float(Nt.lower()[0]) > float(I.lower()[0]) and float(Nt.upper()[0]) < float(I.upper()[0]):
            ok = True; root = Nt; break
    if not ok:
        print("interval Newton did not contract"); root = MR(np.array([tau]), np.array([1e-8]))
    # x_* = e^{t_a} e^{tau*}: enclose with the TM of e^{tau} at the interval root
    x_star = tm_eval(tm["E1"], root)[0] * tm["e_ta"]
    x2 = tm_eval(tm["x2"], root)[0]
    inv_x2 = MR(1.0 / x2.m, succ(x2.r / (x2.mig() ** 2) + U / abs(x2.m)))
    mu_minus1 = tm_eval(tm["S_mu"], root)[0] * inv_x2 + C.c_l - MR.exact(1.0)
    inv_x = MR(1.0 / x_star.m, succ(x_star.r / (x_star.mig() ** 2) + U / abs(x_star.m)))
    g_star = tm_eval(tm["S_g"], root)[0] * inv_x
    A = C.c_l * MR.exact(2.0) - MR.exact(1.0)
    gprime = tm_eval(tm["S_gp"], root)[0] * inv_x2                                  # rho~_xy(P)
    Atilde = C.c_l * MR.exact(2.0) - (mu_minus1 + MR.exact(1.0))                      # 2 c_l - mu~
    V1_check = tm_eval(tm["xV1"], root)[0]
    dFdt = tm_eval(tm["xdV1"], root)[0]                                                # d/dt (x V_1) at the root
    wprime = (dFdt - V1_check) * inv_x2                                                # w'(P) = d_x V_1(x_*, 0) = (dF/dt - F)/x^2
    consist = wprime + (mu_minus1 + MR.exact(1.0)) - C.c_l * MR.exact(2.0)              # w'(P) + mu~ - 2 c_l (= 0 at exact solutions)
    res = dict(cell=ci, newton_contracted=ok, x_star_mid=float(x_star.m), x_star_rad=float(x_star.r), xV1_at_root=[float(V1_check.lower()), float(V1_check.upper())],
               mu_minus_1=[float(mu_minus1.lower()), float(mu_minus1.upper())], g_star=[float(g_star.lower()), float(g_star.upper())],
               A=[float(A.lower()), float(A.upper())], A_tilde=[float(Atilde.lower()), float(Atilde.upper())], g_prime=[float(gprime.lower()), float(gprime.upper())],
               c_l=[float(C.c_l.lower()), float(C.c_l.upper())], w_prime_P=[float(wprime.lower()), float(wprime.upper())],
               wprime_plus_mu_minus_2cl=[float(consist.lower()), float(consist.upper())],
               c=[float(np.nextafter(C.d["c_mid"] - C.d["c_rad"], -np.inf)), float(np.nextafter(C.d["c_mid"] + C.d["c_rad"], np.inf))], time=time.time() - t0)
    print(json.dumps(res, indent=1)); json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]) if len(sys.argv) > 4 else 8.600063803)
