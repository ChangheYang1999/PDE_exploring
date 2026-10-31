#!/usr/bin/env python
"""Source moments of the pressure Poisson problem at fixed coefficients (lead 2026-10-25T18:3xZ question): f = sum_ij d_i U_j d_j U_i = -Delta P.
Moment 0 = int f dy and moment 1 = int y_i f dy (Cartesian components, no spherical-harmonic normalization), each split into the finite-ball part over the
solver's quadrature points with s <= r_last (the last source node) and the exterior part s > r_last, where the solver's quadrature continues in lambda = log s
with the source represented as (s/R0)^(-p0) times the Chebyshev interpolant of the factored source frozen at its x = 1 limit (p0 = 2 alpha + 2). The first-moment
integrand decays like s^(1 - 2 alpha), so the exterior part of a finite ball of radius R scales like R^(2 - 2 alpha). Also reported: the l = 1 projection of the
factored source on the nodes (the solver's gradP_origin kernel) for comparison with the verifier's projected moment. Usage: pressure_source_moments.py <start .pt>
[--factors 3,6,9] [--device cpu]"""
import sys, os, json, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.pressure.poisson_sh import PressureSolver
from src.equations import residuals as res
ap = argparse.ArgumentParser(); ap.add_argument("zfile"); ap.add_argument("--factors", default="3,6,9"); ap.add_argument("--device", default="cpu")
ap.add_argument("--ext_factor", type=float, default=1.0, help="multiply the solver exterior cutoff L_ext = 41.5/(p0-2) (lead 19:04Z: the dipole integrand decays like exp(-(p0-4) t), so the default cutoff leaves 5.3e-4 of the exterior part)")
ap.add_argument("--tag", default="")
a = ap.parse_args()
S = torch.load(a.zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(a.device)
c_l, om = (float(z[-2]), float(z[-1])) if S.get("free_params") else (cfg["c_l"], cfg["omega"])
L = cfg["L"]; Nk = cfg["Nk"]; alpha = alpha_of(c_l); p0 = 2 * alpha + 2
out = dict(start=os.path.relpath(os.path.abspath(a.zfile), ROOT), c_l=c_l, omega=om, omega_over_c_l=om / c_l, alpha=alpha, p0=p0, factors={},
           definition="moment0 = int f dy, moment1_i = int y_i f dy (Cartesian, f = sum_ij d_i U_j d_j U_i = -Delta P); finite = quadrature points s <= r_last (last source node), exterior = s > r_last with the factored source frozen at x = 1 (solver quadrature); total = finite + exterior")
for k in [int(v) for v in a.factors.split(",")]:
    t0 = time.time()
    train = Model(L=L, Nk=Nk, m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=k * Nk, c_l=c_l, omega=om,
                  free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
    ps = PressureSolver(train, p0=p0, omega=om, c_l=c_l, ext_factor=a.ext_factor)
    with torch.no_grad():
        f = res.pressure_source(train.fields_grid(z, need_vort=False)["GU"])          # (Nr, Na)
    q = ps._quad; sg, wsg, Phi, logss = q["s"], q["w"], q["Phi"], q["logss"]; r_last = q["r_last"]
    fn = (f[: ps.Nr_src] * ps.sfac[:, None]).cpu().numpy()                             # factored source on the nodes (Nr_src, Na)
    fq = (Phi @ fn) * np.exp(-p0 * logss)[:, None]                                    # f at the quadrature points (Nq, Na)
    wa = train.grid.w.cpu().numpy(); n = train.n.cpu().numpy()                        # angular weights (Na,), unit vectors (Na, 3)
    fin = sg <= r_last + 1e-12
    def integ(g, mask):                                                               # int g dy over the masked radial quadrature points
        return float(((g[mask] * (sg[mask] ** 2 * wsg[mask])[:, None]) * wa[None, :]).sum())
    m0 = dict(finite=integ(fq, fin), exterior=integ(fq, ~fin))
    m1 = dict(finite=[integ(fq * (sg[:, None] * n[None, :, i]), fin) for i in range(3)], exterior=[integ(fq * (sg[:, None] * n[None, :, i]), ~fin) for i in range(3)])
    m0["total"] = m0["finite"] + m0["exterior"]; m1["total"] = [m1["finite"][i] + m1["exterior"][i] for i in range(3)]
    # lead d122 item 5(d): ball moments M_0(R), M_z(R) as functions of R at the outer export radii (cumulative over the radial quadrature, which is ordered in s)
    order = np.argsort(sg, kind="stable"); s_sorted = sg[order]
    g0 = ((fq * wa[None, :]).sum(1) * sg ** 2 * wsg)[order]; gz = ((fq * n[None, :, 2] * wa[None, :]).sum(1) * sg ** 3 * wsg)[order]
    c0 = np.cumsum(g0); cz = np.cumsum(gz)
    R0 = float(train.R0); R_list = [1e1 * R0, 1e2 * R0, 1e3 * R0, 1e4 * R0, 1e5 * R0, 1.6e6 * R0, float(s_sorted[-1])]
    ball = []
    for R in R_list:
        if R > s_sorted[-1] + 1e-9:
            continue
        j = int(np.searchsorted(s_sorted, R, side="right"))
        ball.append(dict(R=R, R_over_R0=R / R0, M0=float(c0[j - 1]) if j > 0 else 0.0, Mz=float(cz[j - 1]) if j > 0 else 0.0, inside_source_nodes=bool(R <= r_last)))
    rec_ball = ball
    # cross-check against the solver's own volume integral (same quadrature)
    with torch.no_grad():
        chk0 = float(ps.volume_integral(f)); ytr = train.r[:, None, None] * train.n[None, :, :]
        chk1 = [float(ps.volume_integral(f * ytr[..., i])) for i in range(3)]
    # l = 1 projection of the factored source on the nodes (solver kernel used for grad P at the origin), m = 0 component
    with torch.no_grad():
        flm = ps.analyze(f); ftw = ps.to_twisted_frame(flm) * ps.sfac[:, None] * ps.lfac
        l1 = [(ps.pl_idx[qq], int(ps.pm[qq]), float(ps.mom1_0 @ ftw[:, qq])) for qq in range(len(ps.pmodes)) if ps.pl_idx[qq] == 1]
    rec = dict(Nr_src=k * Nk, r_last=r_last, n_quad=int(len(sg)), n_quad_finite=int(fin.sum()), moment0=m0, moment1=m1, solver_volume_integral_check=dict(moment0=chk0, moment1=chk1),
               l1_projected_kernel_moments=l1, ball_moments_vs_R=rec_ball, quadrature_s_max=float(sg.max()), seconds=round(time.time() - t0, 1))
    out["factors"][str(k)] = rec
    print(f"Nr_src {k*Nk}: r_last {r_last:.4g}; moment0 finite {m0['finite']:.6e} exterior {m0['exterior']:.6e} total {m0['total']:.6e} (solver {chk0:.6e}); "
          f"moment1_z finite {m1['finite'][2]:.6e} exterior {m1['exterior'][2]:.6e} total {m1['total'][2]:.6e} (solver {chk1[2]:.6e}); l=1 kernel moments {l1}; {rec['seconds']} s", flush=True)
    print("   ball moments M0(R), Mz(R): " + "; ".join(f"R {b['R_over_R0']:.3g} R0: {b['M0']:.4e}, {b['Mz']:.4e}" for b in rec_ball), flush=True)
job = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(a.zfile))))
out["ext_factor"] = a.ext_factor
op = os.path.join(ROOT, "reports", f"pressure_source_moments_{job}{a.tag}.json"); json.dump(out, open(op, "w"), indent=1); print(f"wrote {op}")
