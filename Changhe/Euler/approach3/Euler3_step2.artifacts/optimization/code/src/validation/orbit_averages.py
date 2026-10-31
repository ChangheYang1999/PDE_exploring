"""SPEC 7.12 orbit averages along the backward flow dy/dt = -W(y) (diagnostic, not an acceptance criterion).
For each seed p and horizon T: <f>_T = (1/T) int_0^T f(y_t) dt with
  (O1) <s + rho_Om>_T = 1 + [log|Omega(p)| - log|Omega(y_T)|]/T,  s = Omega.S Omega/|Omega|^2, rho_Om = Omega.R_Omega/|Omega|^2
  (O2) (1-2c_l) <U.W>_T = <W.R_u>_T + [g(y_T) - g(p)]/T,  g = U.W - |U|^2/2 + P
  (O4) <(1-2c_l) ell + d_phi P>_T = <(J y).R_u>_T + [ell(y_T) - ell(p)]/T,  ell = y_1 U_2 - y_2 U_1
(O3 uses H_0, omitted here). Pressure terms need P and grad P at arbitrary points, which the spherical-harmonic Green
solver does not give directly; O2 and O4 are evaluated with the residual R_u0 without grad P and the pressure
contribution reported as 'not evaluated' unless a pressure callback is supplied. O1 needs no pressure.
Integration: RK4 with fixed step dt = 0.01/c_l (the flow has unit-order rates), fields from Model.fields_points.
Seeds: random points with |W x Omega| >= 0.2 |W||Omega| and |Omega| >= 1e-3 max|Omega| (vortical, transverse)."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations import residuals as res

DT = torch.float64


def _eval(model, z, pts, c_l, omega):
    F = model.fields_points(z, pts, need_vort=True)
    U, GU, Om, GOm = F['U'].T, F['GU'].permute(2, 0, 1), F['Om'].T, F['GOm'].permute(2, 0, 1)
    yv = pts
    Jy = res.Jvec(yv.T).T
    W = c_l * yv - omega * Jy + U
    S = 0.5 * (GU + GU.transpose(1, 2))
    q = (Om ** 2).sum(1).clamp_min(1e-300)
    s = torch.einsum('pi,pij,pj->p', Om, S, Om) / q
    # vorticity residual (no pressure needed)
    ROm = Om + torch.einsum('pm,pmi->pi', W, GOm) + omega * res.Jvec(Om.T).T - torch.einsum('pm,pmi->pi', Om, GU)
    rho_Om = (Om * ROm).sum(1) / q
    return dict(U=U, W=W, Om=Om, q=q, s=s, rho_Om=rho_Om)


def orbit_averages(model, z, c_l, omega, n_seeds=64, horizons=(2, 4, 8, 16), r_range=(0.05, 20.0), seed=0, max_abs_Omega=None):
    dev = model.r.device
    rng = np.random.default_rng(seed)
    # candidate seeds, filtered
    cand = []
    for _ in range(20):
        r = np.exp(rng.uniform(np.log(r_range[0]), np.log(r_range[1]), 512)); n = rng.normal(size=(512, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
        pts = torch.tensor(r[:, None] * n, dtype=DT, device=dev)
        E = _eval(model, z, pts, c_l, omega)
        if max_abs_Omega is None:
            max_abs_Omega = E['q'].sqrt().max().item()
        cross = torch.linalg.cross(E['W'], E['Om']).norm(dim=1)
        ok = (cross >= 0.2 * E['W'].norm(dim=1) * E['Om'].norm(dim=1)) & (E['q'].sqrt() >= 1e-3 * max_abs_Omega)
        cand.append(pts[ok])
        if sum(c.shape[0] for c in cand) >= n_seeds:
            break
    seeds = torch.cat(cand)[:n_seeds]
    Tmax = max(horizons) / c_l
    dt = 0.01 / c_l
    nsteps = int(round(Tmax / dt))
    y = seeds.clone()
    E0 = _eval(model, z, y, c_l, omega)
    acc_s = torch.zeros(len(y), dtype=DT, device=dev); acc_rho = torch.zeros_like(acc_s); acc_UW = torch.zeros_like(acc_s)
    results = {}
    def vel(pts):
        E = _eval(model, z, pts, c_l, omega)
        return -E['W'], E
    tcur = 0.0
    # trapezoid accumulation of s and rho_Om along RK4 trajectory
    E = E0
    for k in range(nsteps):
        k1, Ek = vel(y)
        k2, _ = vel(y + 0.5 * dt * k1)
        k3, _ = vel(y + 0.5 * dt * k2)
        k4, _ = vel(y + dt * k3)
        ynew = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        Enew = _eval(model, z, ynew, c_l, omega)
        acc_s += 0.5 * dt * (Ek['s'] + Enew['s']); acc_rho += 0.5 * dt * (Ek['rho_Om'] + Enew['rho_Om'])
        acc_UW += 0.5 * dt * ((Ek['U'] * Ek['W']).sum(1) + (Enew['U'] * Enew['W']).sum(1))
        y = ynew; tcur += dt
        for T in horizons:
            if abs(tcur - T / c_l) < 0.5 * dt and T not in results:
                bterm = (torch.log(E0['q'].sqrt()) - torch.log(Enew['q'].sqrt())) / tcur
                lhs = (acc_s + acc_rho) / tcur
                rhs = 1 + bterm
                results[T] = dict(T_over_cl=T, T=tcur, mean_s=(acc_s / tcur).tolist(), mean_rho_Om=(acc_rho / tcur).tolist(),
                                  O1_boundary=bterm.tolist(), O1_defect=(lhs - rhs).abs().max().item(),
                                  mean_UW=(acc_UW / tcur).tolist(), r_final=ynew.norm(dim=1).tolist(),
                                  summary=dict(median_mean_s=float((acc_s / tcur).median()), min_mean_s=float((acc_s / tcur).min()), max_mean_s=float((acc_s / tcur).max()),
                                               median_mean_rho_Om=float((acc_rho / tcur).median()), O1_max_defect=(lhs - rhs).abs().max().item()))
    return dict(n_seeds=int(len(y)), dt=dt, seeds=seeds.tolist(), horizons=results, note="O1 exact for any field (defect measures integration error); O2-O4 pressure parts not evaluated")
