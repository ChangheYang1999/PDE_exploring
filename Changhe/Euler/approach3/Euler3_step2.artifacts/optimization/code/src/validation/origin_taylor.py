"""SPEC 7.6 / T08 origin Taylor audit, orders 1 and 2 (order 0 is computed exactly in spec_diagnostics from fields_points at y = 0).
tau_j = |D^j R_u(0)| / max(sum_i |D^j T_i(0)|, 1e-3 S_j), j = 0, 1, 2 (Frobenius norms), S_j = U_c r_core^(-j) (1 + U_c/r_core).
Method: the five momentum terms T_1..T_5 (full-space pressure of the training-grid source, evaluated on the small spheres by the
Green solver with panels split at every evaluation radius) are sampled on five small spheres r = eps..5 eps (eps = R0 2^-11 by
default) with the holdout angular Gauss grid, and the quadratic Taylor polynomial of every Cartesian component is fitted by weighted
least squares (degree-4 polynomial, 35 monomials, angular Gauss weights; five radii eps..5 eps). The fit on the interleaved spheres 1.5 eps..5.5 eps is the consistency check ("consistent
with nearby points", T08): the relative change of each tau_j and of each derivative norm is reported. The order-0 coefficient is also
compared with the exact R_u(0) when it is supplied. The contamination by the omitted degree >= 5 Taylor terms is O((5 eps / scale)^5) relative to the
leading orders, where scale is the smallest radial scale of the representation at the origin; the fit/check change reports it."""
from __future__ import annotations
import math
import torch
from ..equations.fields import Model, alpha_of
from ..equations import residuals as res
from ..pressure.poisson_sh import PressureSolver

DT = torch.float64


def _monomials(yh, degree):
    """Columns: all monomials yh^a with |a| <= degree, ordered by total degree; the first 10 are 1, yh_i, yh_i^2 (i = 0..2), yh_0 yh_1, yh_0 yh_2, yh_1 yh_2."""
    import itertools
    cols = [torch.ones_like(yh[:, 0]), yh[:, 0], yh[:, 1], yh[:, 2], yh[:, 0] ** 2, yh[:, 1] ** 2, yh[:, 2] ** 2, yh[:, 0] * yh[:, 1], yh[:, 0] * yh[:, 2], yh[:, 1] * yh[:, 2]]
    for d in range(3, degree + 1):
        for a in itertools.product(range(d + 1), repeat=3):
            if sum(a) == d:
                cols.append(yh[:, 0] ** a[0] * yh[:, 1] ** a[1] * yh[:, 2] ** a[2])
    return torch.stack(cols, 1)


def _taylor_fit(y, vals, w, eps_ref, degree=4):
    """y (Np, 3), vals (Nfield, Np), w (Np,) -> coefficients (Nfield, n_monomials) of the degree-`degree` polynomial in yh = y/eps_ref
    (weighted least squares); the first 10 columns are the constant, linear and quadratic monomials used for D^0, D^1, D^2."""
    X = _monomials(y / eps_ref, degree)
    sw = w.sqrt()[:, None]
    sol = torch.linalg.lstsq((X * sw).cpu(), (vals.T * sw).cpu(), driver="gelsd")
    return sol.solution.T.to(y.device)


def _derivative_norms(c, eps_ref):
    """c (3 components, 10) -> Frobenius norms of D^0, D^1, D^2 of the vector field at 0 (true derivatives)."""
    D0 = c[:, 0]
    D1 = c[:, 1:4] / eps_ref                                  # D1[i(component), m] = d_m f_i
    D2 = torch.zeros(3, 3, 3, dtype=DT, device=c.device)
    for i in range(3):
        D2[:, i, i] = 2 * c[:, 4 + i] / eps_ref ** 2
    for k, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
        D2[:, i, j] = c[:, 7 + k] / eps_ref ** 2; D2[:, j, i] = D2[:, i, j]
    return [D0.norm().item(), D1.norm().item(), D2.norm().item()], (D0, D1, D2)


def origin_taylor(prob, z, c_l, omega, U_c, r_core, eps=None, ntheta=None, nphi=None, exact_Ru0=None, exact_M0=None):
    model = prob.model; dev = model.r.device
    alpha = alpha_of(float(c_l)); R0 = model.R0
    eps = eps if eps is not None else R0 * 2.0 ** -11
    radii = [k * eps for k in (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5)]       # fit set: 1..5 eps; check set: 1.5..5.5 eps
    Lx = getattr(model, "L_ext", model.L)
    ntheta = ntheta or (2 * Lx + 12); nphi = nphi or (4 * Lx + 18)
    em = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=R0, r_nodes=radii, ntheta=ntheta, nphi=nphi, c_l=model.c_l0, omega=model.omega0,
               free_params=model.free_params, channels=model.channels, device=dev, phi0=math.pi / (2 * nphi))
    F = em.fields_grid(z, need_vort=False)
    ps = PressureSolver(model, p0=2 * alpha + 2, omega=float(omega), c_l=float(c_l), eval_model=em)
    f_src = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
    P, gradP, _, _ = ps.solve(f_src)
    from .spec_diagnostics import five_term_split
    T = five_term_split(F, gradP); Ru = sum(T)
    y = F['y']                                                # (Nr, Na, 3)
    w_ang = em.grid.w / (4 * math.pi)
    fit_idx, chk_idx = [0, 2, 4, 6, 8], [1, 3, 5, 7, 9]
    out = dict(eps=eps, radii_fit=[radii[j] for j in fit_idx], radii_check=[radii[j] for j in chk_idx], ntheta=ntheta, nphi=nphi, fit_degree=4)
    res_sets = {}
    for label, idx in (("fit", fit_idx), ("check", chk_idx)):
        pts = torch.cat([y[j] for j in idx], 0); w = torch.cat([w_ang for _ in idx], 0); eps_ref = radii[idx[-1]]
        norms = {}
        tens = {}
        for name, X in (("R_u", Ru), ("T1", T[0]), ("T2", T[1]), ("T3", T[2]), ("T4", T[3]), ("T5", T[4]), ("U", F['U'])):
            vals = torch.cat([X[:, j, :] for j in idx], 1)    # (3, Np)
            c = _taylor_fit(pts, vals, w, eps_ref)
            norms[name], tens[name] = _derivative_norms(c, eps_ref)
        S = [U_c * r_core ** (-j) * (1 + U_c / r_core) for j in range(3)]
        den = [sum(norms[f"T{i}"][j] for i in range(1, 6)) for j in range(3)]
        tau_raw = [norms["R_u"][j] / den[j] if den[j] > 0 else None for j in range(3)]
        tau_fl = [norms["R_u"][j] / max(den[j], 1e-3 * S[j]) for j in range(3)]
        res_sets[label] = dict(norms_Ru=norms["R_u"], den=den, floor=[1e-3 * s for s in S], tau_raw=tau_raw, tau_floored=tau_fl, norms_U=norms["U"], tens=tens)
    a, b = res_sets["fit"], res_sets["check"]
    out.update(tau_raw=a["tau_raw"], tau_floored=a["tau_floored"], D_Ru_norms=a["norms_Ru"], den_sum_terms=a["den"], floor_1e3_S=a["floor"], D_U_norms=a["norms_U"],
               tau_floored_check=b["tau_floored"], consistency_rel_change_tau=[abs(x - yv) / max(abs(x), abs(yv), 1e-300) for x, yv in zip(a["tau_floored"], b["tau_floored"])],
               consistency_rel_change_DRu=[abs(x - yv) / max(abs(x), abs(yv), 1e-300) for x, yv in zip(a["norms_Ru"], b["norms_Ru"])],
               u0_fit=[float(v) for v in a["tens"]["U"][0]], trace_M_fit=float(a["tens"]["U"][1].trace()))
    if exact_Ru0 is not None:
        e = torch.as_tensor(exact_Ru0, dtype=DT, device=dev)
        out["D0_Ru_vs_exact_rel"] = float((a["tens"]["R_u"][0] - e).norm() / max(e.norm().item(), 1e-300))
    if exact_M0 is not None:                                 # exact_M0[m, i] = d_m U_i(0); the fit's D1[i, m] = d_m U_i
        e = torch.as_tensor(exact_M0, dtype=DT, device=dev)
        out["D1_U_vs_exact_rel"] = float((a["tens"]["U"][1] - e.T).norm() / max(e.norm().item(), 1e-300))
    return out
