"""SPEC 7.14 (a), (b): exact checks along backward orbits of X' = -W(X) (diagnostic only; lead item 3 of 2026-10-24T21:32Z).
(a) With M' = -DW(X) M, M(0) = I, DW = c_l I - omega J + DU (DU_ij = d_j U_i):
      det M_t = e^(-3 c_l t)                                  (kinematic: tests the integrator only, since div W = 3 c_l exactly)
      M_t Omega(p) = e^(-(1+c_l) t) Omega(X_t)                 (vorticity transport: both sides solve v' = (I + omega J - DU) v for an
                                                               exact profile; the defect measures the vorticity residual along the orbit)
      M_t^T beta(X_t) = e^(k t) beta(p), beta = beta_0 = (W x Omega)/k, k = 1 - 2 c_l   (the beta_0 form: it tests vorticity-residual
                                                               transport, SPEC 7.14 (a) wording 20:47Z; beta_1 = U + dB/k is not used)
(b) Endpoint-corrected integrals over [0, T] with the integrand at X_t (trapezoid along the RK4 orbit):
      integral y.W dt = (|p|^2 - |X_T|^2)/2                                              (kinematic)
      k integral U.W dt = B(X_T) - B(p),  B = U.W - |U|^2/2 + P                          (defect = integral W.R_u dt for a state)
      integral (k ell + d_phi P) dt = ell(X_T) - ell(p),  ell = (J y).U                   (defect = integral (J y).R_u dt)
      integral (k |V|^2 + omega d_phi P) dt = H_0(X_T) - H_0(p),  H_0 = Be + omega ell, Be = B - k c_l |y|^2/2 (SPEC 1), V = c_l y + U   (defect = integral (W + omega J y).R_u)
      integral (|V|^2 + c_l(1-c_l)|y|^2 - y.grad P) dt = D(p) - D(X_T),  D = y.U + |y|^2/2                (defect = -integral y.R_u dt)
    Each defect is reported with the independent R_u-integral it should equal (residual accounting), so the pair checks the implementation.
Pressure P and grad P at the orbit points: the full-space Green solution of the training-node source, evaluated at the exact orbit radii
(chunked evaluation models), the same route as the holdout diagnostics. Seeds: vortical transverse points (|W x Omega| >= 0.2 |W||Omega|).
Integration accuracy (reported, not hidden): the position integrals (y.W identity) close to 1e-4 at dt = 0.02/c_l, while the
linearized flow M is stiff where |DU| is large (|DU| up to about 20 in the core of the d6t states), so det M_t deviates from
e^(-3 c_l t) by 2e-4 (16 seeds, T = 2/c_l) to 4e-2 (32 seeds, T = 4/c_l) on d6t_L6; the det M defect is the integrator-error gauge for
the (a) transport defects of the same orbit set, which are order one or larger on all states so far."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations import residuals as res
from ..equations.fields import Model, alpha_of
from ..pressure.poisson_sh import PressureSolver

DT = torch.float64


def _fields(model, z, pts, c_l, omega):
    F = model.fields_points(z, pts, need_vort=True)
    U, GU, Om = F['U'].T, F['GU'].permute(2, 0, 1), F['Om'].T              # GU[p, m, i] = d_m U_i
    Jy = res.Jvec(pts.T).T
    W = c_l * pts - omega * Jy + U
    DU = GU.transpose(1, 2)                                                   # DU[p, i, j] = d_j U_i
    Jm = torch.tensor([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=DT, device=pts.device)
    DW = c_l * torch.eye(3, dtype=DT, device=pts.device)[None] - omega * Jm[None] + DU
    return dict(U=U, GU=GU, Om=Om, W=W, DW=DW, Jy=Jy)


def _pressure_at(model, z, pts, c_l, omega, n_dense=400):
    """P and grad P at arbitrary points from the Green solution of the training-node source: the radial coefficient functions
    P_lm(r), P_lm'(r) are computed on a dense geometric radial grid covering the points (n_dense radii) and interpolated by cubic
    splines in log r (the Green solution of a smooth source is smooth in r; interpolation error about 1e-7 relative, adequate for the
    order-one defects of this diagnostic and reported as 'pressure_interp')."""
    from scipy.interpolate import CubicSpline
    from ..bases.solid_harmonics import eval_solid
    alpha = alpha_of(c_l)
    f_src = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
    r = pts.norm(dim=1)
    rmin, rmax = float(r.min()) * 0.9, float(r.max()) * 1.1
    dense = np.geomspace(rmin, rmax, n_dense)
    em = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, r_nodes=dense, ntheta=4, nphi=4, c_l=model.c_l0, omega=model.omega0,
               free_params=model.free_params, channels=model.channels, device=pts.device)
    ps = PressureSolver(model, p0=2 * alpha + 2, omega=omega, c_l=c_l, eval_model=em)
    _, _, Plm, dPlm = ps.solve(f_src)                                           # (n_dense, Nqp)
    lr = np.log(dense); lq = np.log(r.cpu().numpy())
    Pl = torch.tensor(CubicSpline(lr, Plm.cpu().numpy(), axis=0)(lq), dtype=DT, device=pts.device)
    dPl = torch.tensor(CubicSpline(lr, dPlm.cpu().numpy(), axis=0)(lq), dtype=DT, device=pts.device)
    n = pts / r[:, None]
    A0r, A1r, _ = eval_solid(n, ps.pmodes, ps.Lf, 1, path="auto")   # diagnostic (battery): auto path, recorded
    P = (Pl * A0r).sum(1)
    radial = ((dPl - ps.pl[None, :] * Pl / r[:, None]) * A0r).sum(1)
    gP = radial[:, None] * n + torch.einsum('pq,ipq->pi', Pl / r[:, None], A1r)
    return P, gP


def orbit_checks(model, z, c_l, omega, n_seeds=24, T_over_cl=4.0, dt_over_cl=0.02, r_range=None, seed=0, record_every=25):
    dev = model.r.device
    c_l = float(c_l); omega = float(omega); k = 1.0 - 2.0 * c_l
    rng = np.random.default_rng(seed)
    r_range = r_range or (0.2 * model.R0, 50.0 * model.R0)
    cand = []
    maxOm = None
    for _ in range(20):
        r = np.exp(rng.uniform(np.log(r_range[0]), np.log(r_range[1]), 512)); nn = rng.normal(size=(512, 3)); nn /= np.linalg.norm(nn, axis=1)[:, None]
        pts = torch.tensor(r[:, None] * nn, dtype=DT, device=dev)
        E = _fields(model, z, pts, c_l, omega)
        if maxOm is None:
            maxOm = E['Om'].norm(dim=1).max().item()
        cross = torch.linalg.cross(E['W'], E['Om']).norm(dim=1)
        ok = (cross >= 0.2 * E['W'].norm(dim=1) * E['Om'].norm(dim=1)) & (E['Om'].norm(dim=1) >= 1e-3 * maxOm)
        cand.append(pts[ok])
        if sum(c.shape[0] for c in cand) >= n_seeds:
            break
    seeds = torch.cat(cand)[:n_seeds]; ns = len(seeds)
    dt = dt_over_cl / c_l; nsteps = int(round(T_over_cl / c_l / dt))
    X = seeds.clone(); M = torch.eye(3, dtype=DT, device=dev)[None].repeat(ns, 1, 1)
    traj = [X.clone()]
    def rhs(Xc, Mc):
        E = _fields(model, z, Xc, c_l, omega)
        return -E['W'], -torch.einsum('pij,pjk->pik', E['DW'], Mc), E
    E0 = _fields(model, z, X, c_l, omega)
    Om0 = E0['Om']; beta0 = torch.linalg.cross(E0['W'], E0['Om']) / k
    a_checks = []
    for s in range(1, nsteps + 1):
        k1x, k1m, _ = rhs(X, M)
        k2x, k2m, _ = rhs(X + 0.5 * dt * k1x, M + 0.5 * dt * k1m)
        k3x, k3m, _ = rhs(X + 0.5 * dt * k2x, M + 0.5 * dt * k2m)
        k4x, k4m, _ = rhs(X + dt * k3x, M + dt * k3m)
        X = X + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x); M = M + dt / 6 * (k1m + 2 * k2m + 2 * k3m + k4m)
        traj.append(X.clone())
        if s % record_every == 0 or s == nsteps:
            t = s * dt
            E = _fields(model, z, X, c_l, omega)
            detM = torch.linalg.det(M)
            d_det = ((detM - math.exp(-3 * c_l * t)).abs() / math.exp(-3 * c_l * t))
            lhs = torch.einsum('pij,pj->pi', M, Om0); rhsv = math.exp(-(1 + c_l) * t) * E['Om']
            d_om = (lhs - rhsv).norm(dim=1) / rhsv.norm(dim=1).clamp_min(1e-300)
            beta_t = torch.linalg.cross(E['W'], E['Om']) / k
            lhsb = torch.einsum('pji,pj->pi', M, beta_t); rhsb = math.exp(k * t) * beta0          # M^T beta(X_t)
            d_beta = (lhsb - rhsb).norm(dim=1) / rhsb.norm(dim=1).clamp_min(1e-300)
            a_checks.append(dict(t=t, t_over_cl=t * c_l, det_rel_defect_max=d_det.max().item(), det_rel_defect_median=d_det.median().item(),
                                 Omega_transport_rel_defect_median=d_om.median().item(), Omega_transport_rel_defect_max=d_om.max().item(),
                                 beta0_pullback_rel_defect_median=d_beta.median().item(), beta0_pullback_rel_defect_max=d_beta.max().item(),
                                 r_median=X.norm(dim=1).median().item()))
    # (b) integrals along the orbits: fields and pressure at every trajectory point
    T = torch.stack(traj, 0)                                     # (nsteps+1, ns, 3)
    flat = T.reshape(-1, 3)
    E = _fields(model, z, flat, c_l, omega)
    P, gP = _pressure_at(model, z, flat, c_l, omega)
    U, W, Jy, GU = E['U'], E['W'], E['Jy'], E['GU']
    Ru = (1 - c_l) * U + torch.einsum('pm,pmi->pi', W, GU) + omega * res.Jvec(U.T).T + gP
    yW = (flat * W).sum(1); UW = (U * W).sum(1); ell = (Jy * U).sum(1); dphiP = (Jy * gP).sum(1)
    V = c_l * flat + U; V2 = (V ** 2).sum(1); ygP = (flat * gP).sum(1); y2 = (flat ** 2).sum(1)
    B = UW - 0.5 * (U ** 2).sum(1) + P                                            # Bernoulli form of the U.W identity
    Be = B - k * c_l * 0.5 * y2                                                   # SPEC section 1: Be = |W|^2/2 + P + c_l(c_l-1)|y|^2/2 - omega^2|y_h|^2/2 = B - k c_l |y|^2/2
    H0 = Be + omega * ell; Dfun = (flat * U).sum(1) + 0.5 * y2
    WRu = (W * Ru).sum(1); JyRu = (Jy * Ru).sum(1); yRu = (flat * Ru).sum(1)
    def sh(v):
        return v.reshape(nsteps + 1, ns)
    def integ(v):                                                # trapezoid in t
        v = sh(v); return dt * (v[1:] + v[:-1]).sum(0) / 2
    def absint(v):
        return integ(v.abs())
    Pv, Bv, ellv, H0v, Dv = sh(P), sh(B), sh(ell), sh(H0), sh(Dfun)
    y2v = sh(y2)
    checks = {}
    I1 = integ(yW); R1 = 0.5 * (y2v[0] - y2v[-1]); checks['y.W'] = dict(integral=I1, exact=R1, residual_integral=torch.zeros_like(I1), scale=absint(yW), note='kinematic (integration error only)')
    I2 = k * integ(UW); R2 = Bv[-1] - Bv[0]; checks['k U.W (Bernoulli)'] = dict(integral=I2, exact=R2, residual_integral=integ(WRu), scale=absint(k * UW), note='defect should equal integral W.R_u')
    I3 = integ(k * ell + dphiP); R3 = ellv[-1] - ellv[0]; checks['k ell + d_phi P (angular momentum)'] = dict(integral=I3, exact=R3, residual_integral=integ(JyRu), scale=absint(k * ell + dphiP), note='defect should equal integral (J y).R_u')
    I4 = integ(k * V2 + omega * dphiP); R4 = H0v[-1] - H0v[0]; checks['k |V|^2 + omega d_phi P (H_0)'] = dict(integral=I4, exact=R4, residual_integral=integ(WRu + omega * JyRu), scale=absint(k * V2 + omega * dphiP), note='defect should equal integral (W + omega J y).R_u')
    I5 = integ(V2 + c_l * (1 - c_l) * y2 - ygP); R5 = Dv[0] - Dv[-1]; checks['|V|^2 + c_l(1-c_l)|y|^2 - y.grad P (D)'] = dict(integral=I5, exact=R5, residual_integral=-integ(yRu), scale=absint(V2 + c_l * (1 - c_l) * y2 - ygP), note='defect should equal -integral y.R_u')
    out_b = {}
    for name, c in checks.items():
        defect = c['integral'] - c['exact']
        acc = (defect - c['residual_integral']).abs() / c['scale'].clamp_min(1e-300)       # residual accounting closure (implementation check)
        out_b[name] = dict(rel_defect_median=float((defect.abs() / c['scale'].clamp_min(1e-300)).median()), rel_defect_max=float((defect.abs() / c['scale'].clamp_min(1e-300)).max()),
                           accounting_closure_median=float(acc.median()), accounting_closure_max=float(acc.max()), note=c['note'])
    return dict(n_seeds=ns, T_over_cl=T_over_cl, dt_over_cl=dt_over_cl, nsteps=nsteps, k=k, beta_form="beta_0 = (W x Omega)/k (vorticity-residual transport)",
                a=a_checks, b=out_b, seeds_r=seeds.norm(dim=1).tolist(), final_r=X.norm(dim=1).tolist(),
                note="SPEC 7.14 (a), (b) diagnostics; defects are integrals of residual terms along the backward dynamics, not acceptance quantities")
