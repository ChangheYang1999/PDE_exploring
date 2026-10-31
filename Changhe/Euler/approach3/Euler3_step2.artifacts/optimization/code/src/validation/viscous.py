"""Stage II S8 (artificial viscosity, lead 2026-10-25T05:18Z; stage2_plan_draft S8 / R7): holdout diagnostics of the viscous residual
R^nu = R_u - nu Delta U on the SPEC shell family: per shell RMS of R^nu, the six-term denominator (T1..T5 and T6 = -nu Delta U), the single-term
ratio sigma^nu = RMS(R^nu)/RMS((1 - c_l) U), the inviscid rho_u and sigma_u of the same state (how far it is from an Euler profile), and the
tail-constraint residuals at the state (R7 (d)). Every S8 state is a 'viscous continuation state (nu = ...)', never an Euler candidate."""
from __future__ import annotations
import math
import torch
from ..equations import residuals as res
from ..equations.fields import alpha_of

DT = torch.float64


def viscous_diagnostics(prob, z, holdout, nu):
    from .spec_diagnostics import five_term_split
    model = prob.model
    aT, aS, c_l, omega = model.unpack(z)
    c_lf, omf = float(c_l), float(omega)
    em = holdout.model
    F = em.fields_grid(z, need_vort=False)
    ps = holdout.pressure_solver(model, c_lf, omf)
    f = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
    P, gradP, _, _ = ps.solve(f)
    T = five_term_split(F, gradP)
    lap = em.laplacian_grid(z)
    T6 = -nu * lap
    Ru = sum(T); Rnu = Ru + T6
    sh = holdout
    rmsT = [sh.rms(t) for t in T] + [sh.rms(T6)]
    rmsRu = sh.rms(Ru); rmsRnu = sh.rms(Rnu)
    nsh = sh.n
    den6 = [sum(rmsT[i][k] for i in range(6)) for k in range(nsh)]; den5 = [sum(rmsT[i][k] for i in range(5)) for k in range(nsh)]
    rho_nu = [rmsRnu[k] / den6[k] if den6[k] > 0 else None for k in range(nsh)]
    rho_u = [rmsRu[k] / den5[k] if den5[k] > 0 else None for k in range(nsh)]
    sigma_nu = [rmsRnu[k] / rmsT[0][k] if rmsT[0][k] > 0 else None for k in range(nsh)]
    sigma_u = [rmsRu[k] / rmsT[0][k] if rmsT[0][k] > 0 else None for k in range(nsh)]
    visc_share = [rmsT[5][k] / den6[k] if den6[k] > 0 else None for k in range(nsh)]
    dmax = max(den6); valid = [k for k in range(nsh) if den6[k] > 1e-14 * dmax]
    vmax = lambda lst: max(lst[k] for k in valid if lst[k] is not None)
    # dissipation integral D = int |DU|^2 over the holdout range (normalized-volume shell weights)
    GU = F['GU']; vol = [(4 * math.pi / 3) * (b ** 3 - a ** 3) for (a, b) in sh.edges]
    rmsDU = sh.rms(GU.reshape(9, *GU.shape[2:]))
    D = sum(vol[k] * rmsDU[k] ** 2 for k in range(nsh))
    return dict(nu=nu, c_l=c_lf, omega=omf, shells=sh.edges, rho_nu=rho_nu, rho_u=rho_u, sigma_nu=sigma_nu, sigma_u=sigma_u, visc_share=visc_share,
                rms_Rnu=rmsRnu, rms_Ru=rmsRu, rms_T6=rmsT[5], rho_nu_max=vmax(rho_nu), rho_u_max=vmax(rho_u), sigma_nu_max=vmax(sigma_nu), sigma_u_max=vmax(sigma_u),
                visc_share_max=vmax(visc_share), dissipation_D_holdout_range=D, label=f"viscous continuation state (nu = {nu:.4e}); not an Euler candidate")


def viscous_text(vd):
    return (f"nu={vd['nu']:.3e} | rho^nu_max (six-term)={vd['rho_nu_max']:.3e} | sigma^nu_max (single-term)={vd['sigma_nu_max']:.3f} | inviscid rho_u_max of the same state={vd['rho_u_max']:.3e} "
            f"sigma_u_max={vd['sigma_u_max']:.3f} | viscous share of the terms max={vd['visc_share_max']:.3f} | D(holdout range)={vd['dissipation_D_holdout_range']:.3e} | omega={vd['omega']:.4f} c_l={vd['c_l']:.4f} | {vd['label']}")
