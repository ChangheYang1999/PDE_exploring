"""FLOATING estimate of eta = ||F(rho~)||_Y (Y = E G (+) L^2(w_a), S2_L2_THEORY 5.2) and ||F(rho~)||_{L^2(e^{mu~})}, by pointwise evaluation.
At each quadrature node (fsec prep nodes) the exact background modes are evaluated (floats of the exact balls) and the factor
e^{-3t} F(rho~) = (V_r/r) (rho_r/r^2) + (V_theta/r) (rho_theta/r^3) - rho~/r^3 is formed on a theta grid of M points,
   V_r/r = c_l - sum_n Pe_n cos 2n theta,  V_theta/r = sum_n Qe_n sin 2n theta,  rho_r/r^2 = sum_j dR_j sin (2j+1) theta,
   rho_theta/r^3 = sum_j (2j+1) Rhat_j cos (2j+1) theta,  rho~/r^3 = sum_j Rhat_j sin (2j+1) theta,
then its sine modes G_N (N <= NM) by FFT (exact for trigonometric polynomials of degree < M/2; F has degree <= 3*260). Jet gamma, remainder
quotient by cos^4 and the Y energies as in fsec_ang/fsec; L^2(e^{mu~}) energy pi sum_N G_N^2 e^{8t + mu~}. Regions r < 1, 1 <= r <= 100, r > 100.
Float cancellation: the three O(1) terms cancel to the residual; double precision leaves ~1e-15 absolute noise per node in the factor.
Usage: python3 eta2.py <tag> [M=4096] [NM=800] [prec=256]
"""
import sys, os, time, json, pickle, math
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background
from run_section import HERE
from eta import mu_tilde
from fsec import mu_a, gG, ep_eval
import fsec_ang as ang

def I_half_vec(kmax):
    """I(k) = int_0^{2pi} cos(k th) |cos th|^{-1/2} dth for even k <= kmax by the recurrence I(k+2) = -I(k) (k + 1/2)/(k + 3/2)"""
    I = {0: ang.I_half(0)}
    k = 0
    while k + 2 <= kmax:
        I[k + 2] = -I[k] * (k + 0.5) / (k + 1.5); k += 2
    return I

def A_half_fast(n):
    I = I_half_vec(2 * (2 * n + 2))
    A = np.zeros((n, n))
    for j in range(n):
        for jp in range(n):
            A[j, jp] = 0.5 * (I[abs(2 * (j - jp))] - I[2 * (j + jp + 1)])
    return A

if __name__ == "__main__":
    a = sys.argv; tag = a[1]; M = int(a[2]) if len(a) > 2 else 4096; NM = int(a[3]) if len(a) > 3 else 800; PREC = int(a[4]) if len(a) > 4 else 256
    OUT = os.path.join(HERE, "runs", tag); os.makedirs(OUT, exist_ok=True)
    ctx.prec = PREC; T0 = time.time()
    T = ExactTrial(prec=PREC); T.build_green(verbose=False)
    CELLS = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    bg = Background(T, CELLS, nmax=None)
    NODES = pickle.load(open(os.path.join(HERE, "runs", "fsec_prep_L40_ng3_8_16.pkl"), "rb"))[0]
    c_l = float((1 / T.k).mid()); Nf = T.Nf; Mj = T.Mj
    th = np.arange(M) * (2 * np.pi / M)                     # unshifted grid: rfft(sin((2N+1) th))[2N+1] = -i M/2 exactly
    n_ = np.arange(1, Nf + 1); j_ = np.arange(Mj)
    COS2n = np.cos(np.outer(2 * n_, th)); SIN2n = np.sin(np.outer(2 * n_, th)); SINj = np.sin(np.outer(2 * j_ + 1, th)); COSj = np.cos(np.outer(2 * j_ + 1, th))
    nm = NM + 1; AH = A_half_fast(nm - 2); M4, DIV = ang.div_cos4(nm)
    check = np.linalg.eigvalsh(AH); print("A_half(%d) eig min %.3e max %.3e (build %.0fs)" % (nm - 2, check[0], check[-1], time.time() - T0), flush=True)
    # one-node check of the FFT mode extraction against the exact residual modes (Operator.residual_modes, N <= 8) on a mid cell
    from opimage import Operator
    OPc = Operator(T, CELLS, bg, Nmax=8); icc = 300; sc = NODES[icc][0][1]; dc = bg.get(icc)
    ex = OPc.residual_modes(icc, Nmax=8)
    Pe = np.array([ep_eval(dc["Pe"][i], sc) for i in range(Nf)]); Qe = np.array([ep_eval(dc["Qe"][i], sc) for i in range(Nf)])
    dR = np.array([ep_eval(dc["dR"][j], sc) for j in range(Mj)]); Rh = np.array([ep_eval(dc["Rhat"][j], sc) for j in range(Mj)])
    Fc = (c_l - Pe @ COS2n) * (dR @ SINj) + (Qe @ SIN2n) * (((2 * j_ + 1) * Rh) @ COSj) - Rh @ SINj
    fc = np.fft.rfft(Fc); Gc = -2.0 * fc[2 * np.arange(9) + 1].imag / M
    exv = np.array([ep_eval(ex[N], sc) if N in ex else 0.0 for N in range(9)])
    print("FFT-vs-exact residual modes at cell %d node t=%.3f: max |diff| %.3e, max |exact| %.3e, |F| max on grid %.3e" % (icc, NODES[icc][1][1], np.max(np.abs(Gc - exv)), np.max(np.abs(exv)), np.max(np.abs(Fc))), flush=True)
    E_G = np.zeros(3); E_R = np.zeros(3); E_mu = np.zeros(3); E_img = 0.0; E_ax = 0.0; E_div = 0.0; E_top = 0.0; max_gam = (0.0, None); maxF = (0.0, None)
    per_cell = []
    for ic in range(CELLS.n):
        cl = CELLS.cells[ic]
        saved = ctx.prec; ctx.prec = 512 if cl["kind"] != "mid" else PREC
        d = bg.get(ic); s_nodes, t_nodes, w_nodes = NODES[ic]
        for a_, s in enumerate(s_nodes):
            t = t_nodes[a_]; w = w_nodes[a_]; reg = 0 if t < 0 else (1 if t <= math.log(100.0) else 2)
            Pe = np.array([ep_eval(d["Pe"][i], s) for i in range(Nf)]); Qe = np.array([ep_eval(d["Qe"][i], s) for i in range(Nf)])
            dR = np.array([ep_eval(d["dR"][j], s) for j in range(Mj)]); Rh = np.array([ep_eval(d["Rhat"][j], s) for j in range(Mj)])
            Vr = c_l - Pe @ COS2n; Vth = Qe @ SIN2n; rr = dR @ SINj; rth = ((2 * j_ + 1) * Rh) @ COSj; rho = Rh @ SINj
            F = Vr * rr + Vth * rth - rho                                  # e^{-3t} F(rho~) on the theta grid
            fft = np.fft.rfft(F); G = np.zeros(nm)
            kk = 2 * np.arange(nm) + 1; kk = kk[kk < len(fft)]
            G[:len(kk)] = -2.0 * fft[kk].imag / M
            gam, R, a0 = ang.jet_split(G); Q, res = DIV(R)
            wR = math.exp(8 * t + mu_a(t)); wG = gG(t); wmu = math.exp(8 * t + mu_tilde(t))
            E_G[reg] += w * wG * gam * gam; E_R[reg] += w * wR * float(Q @ AH @ Q); E_mu[reg] += w * wmu * math.pi * float(G @ G)
            tot = float(G @ G); E_img += w * wR * tot; E_ax += w * wR * a0 * a0; E_div += w * wR * res * res; E_top += w * wR * float(np.sum(G[-10:] ** 2))
            if abs(gam) > max_gam[0]: max_gam = (abs(gam), t)
            fm = float(np.max(np.abs(F)))
            if fm > maxF[0]: maxF = (fm, t)
        ctx.prec = saved
        if ic % 100 == 0: print("cell %d/%d: E_G %s E_R %s (%.0fs)" % (ic, CELLS.n, np.array2string(E_G, precision=3), np.array2string(E_R, precision=3), time.time() - T0), flush=True)
    eta_G = math.sqrt(E_G.sum()); eta_R = math.sqrt(E_R.sum()); eta = math.sqrt(eta_G ** 2 + eta_R ** 2); eta_mu = math.sqrt(E_mu.sum())
    res = dict(tag=tag, M=M, NM=NM, prec=PREC, eta_Y=eta, eta_G_axis_part=eta_G, eta_R_remainder_part=eta_R, eta_L2_mu_tilde=eta_mu,
               split_regions=["r < 1", "1 <= r <= 100", "r > 100"], G_energy_by_region=E_G.tolist(), R_energy_by_region=E_R.tolist(), L2mu_energy_by_region=E_mu.tolist(),
               diag=dict(axis_residual_energy_fraction=E_ax / (E_img + 1e-300), division_residual_energy_fraction=E_div / (E_img + 1e-300), top10_mode_energy_fraction=E_top / (E_img + 1e-300),
                         max_abs_gamma=max_gam[0], at_t=max_gam[1], max_abs_factor_F=maxF[0], at_t_F=maxF[1]),
               status="FLOATING (numerical estimate; pointwise evaluation + FFT, float cancellation noise ~1e-15 per node)", seconds=time.time() - T0)
    json.dump(res, open(os.path.join(OUT, "eta.json"), "w"), indent=1); print(json.dumps(res, indent=1))
