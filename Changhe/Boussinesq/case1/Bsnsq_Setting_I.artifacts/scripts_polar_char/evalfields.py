"""Point-wise evaluation of the candidate fields, residuals, normalizers and desingularized residuals
at arbitrary polar points (including exactly on the axes).  Uses the same basis/inverse as polarlib
(the modal Green inverse recomputed on the evaluation radii, so no interpolation)."""
import math, numpy as np, torch
from polarlib import *


def sinratio(m, th):
    """sin(m th)/sin(th) for integer m >= 1 and th in [0, pi], stable at th = 0 and th = pi."""
    th = torch.as_tensor(th)
    flip = th > math.pi / 2
    phi = torch.where(flip, math.pi - th, th)
    sgn = torch.where(flip, torch.full_like(th, -((-1.0) ** m)), torch.ones_like(th))
    small = phi.abs() < 1e-5
    s = torch.where(small, torch.ones_like(phi), torch.sin(phi))
    out = torch.sin(m * phi) / s
    taylor = m * (1.0 - (m * m - 1.0) * phi * phi / 6.0)
    return sgn * torch.where(small, taylor, out)


def load_coefs(npz):
    d = np.load(npz, allow_pickle=True)
    beta = float(d['beta']); L = float(d['L'])
    P = Params(beta, L=L)
    # allow stored exponents to override (frozen-basis runs store the beta-consistent ones)
    if 'gamma_T' in d: P.gamma_T = float(d['gamma_T']); P.gamma_O = float(d['gamma_O']); P.mu = float(d['mu'])
    NT, NO, K = int(d['NT']), int(d['NO']), int(d['K'])
    cT = torch.tensor(d['cT'], dtype=DT).reshape(NT, K); cO = torch.tensor(d['cO'], dtype=DT).reshape(NO, K)
    return P, cT, cO, NT, NO, K


def radial_profiles(P, cT, cO, r, NT, NO, K, ngl=16, ngl_tail=192, nref=4000):
    """Radial functions f_n, f_n', g_n, g_n', psi_n, psi_n' on radii r (N,). Returns dict of (Nmodes, N) tensors.
    The inverse is integrated on the union of r with a geometric auxiliary grid (40 radii per decade, 1e-8 L .. 1e9 L), so that
    the quadrature panels are always fine regardless of the requested radii; the tail formula is applied at the largest radius (>= 1e9 L)."""
    device = r.device
    cT = cT.to(device); cO = cO.to(device)
    r_req = r
    # auxiliary radii geometric in r (40 per decade from 1e-8 L to 1e9 L): every quadrature panel has ratio <= 10^(1/40),
    # for which the 16-point Gauss rule is exact to rounding for the basis integrands (checked on a slow-tail manufactured field)
    # the auxiliary grid must cover the requested radii (found 2026-10-20: requested radii beyond 1e9 L produced panels
    # with ratios up to 43 and a 15 percent error in psi there, 5e-5 in the strain; earlier evaluations used r <= 1e7 L)
    top = max(9.0, math.ceil(math.log10(float(r_req.max()) / P.L) + 0.5))
    raux = torch.logspace(-8, top, int(round((top + 8) * 40)) + 1, dtype=DT, device=device) * P.L
    r_all, _ = torch.sort(torch.unique(torch.cat([r_req, raux])))
    idx = torch.searchsorted(r_all, r_req)
    r = r_all
    f = []; df = []
    for n in range(NT):
        H, dH = radial_basis(P, r, 2 * n + 1, P.gamma_T, K)
        f.append(H @ cT[n]); df.append(dH @ cT[n])
    g = []; dg = []; psi = []; dpsi = []
    for n in range(1, NO + 1):
        m = 2 * n
        H, dH = radial_basis(P, r, m, P.gamma_O, K)
        g.append(H @ cO[n - 1]); dg.append(dH @ cO[n - 1])
        tail = basis_tail(P, r[-1], m, P.gamma_O, K, ngl_tail=ngl_tail)
        Jin, Jout = modal_inverse(P, r, m, basis_gfun(P, m, P.gamma_O, K), tail, ngl=ngl)
        psi.append(((Jin + Jout) @ cO[n - 1]) / (4.0 * n)); dpsi.append(((Jout - Jin) @ cO[n - 1]) / (2.0 * r))
    c = float(c_row(P, P.gamma_O, K).to(device) @ cO[0])
    out = dict(f=torch.stack(f), df=torch.stack(df), g=torch.stack(g), dg=torch.stack(dg), psi=torch.stack(psi), dpsi=torch.stack(dpsi))
    out = {k: v[:, idx] for k, v in out.items()}
    out['c'] = c
    return out


def fields_at(prof, r, th, beta, NT, NO):
    """Fields, residuals, normalizers and desingularized residuals at the tensor grid (r_i, th_j), th in [0, pi/2]
    (axes included exactly).  All desingularized quantities are assembled from pieces that are finite on the axes."""
    N, M = r.shape[0], th.shape[0]
    R = r[:, None]; TH = th[None, :]
    cs = torch.cos(th)[None, :]; sn = torch.sin(th)[None, :]
    dlt = math.pi / 2 - th
    Z = lambda: torch.zeros(N, M, dtype=DT, device=r.device)
    Th = Z(); Thr = Z(); Thth_r = Z(); Th_y = Z(); Thr_y = Z(); Thth_r_x = Z()
    for n in range(NT):
        m = 2 * n + 1
        fn = prof['f'][n][:, None]; dfn = prof['df'][n][:, None]
        s_m = torch.sin(m * TH); c_m = torch.cos(m * TH)
        SR = sinratio(m, th)[None, :]                      # sin(m th)/sin th
        CR = ((-1) ** n) * sinratio(m, dlt)[None, :]       # cos(m th)/cos th  (odd m)
        Th += fn * s_m; Thr += dfn * s_m; Thth_r += m * (fn / R) * c_m
        Th_y += (fn / R) * SR; Thr_y += (dfn / R) * SR; Thth_r_x += m * (fn / R / R) * CR
    Thx = cs * Thr - sn * Thth_r; Thy = sn * Thr + cs * Thth_r
    Thx_y = cs * Thr_y - Thth_r / R                        # Theta_x / y
    Thx_xy = Thr_y / R - Thth_r_x / R                      # Theta_x / (x y)
    Om = Z(); Omr = Z(); Omth_r = Z(); Om_xy = Z(); Omr_y = Z(); Omr_x = Z()
    Psi = Z(); Psir = Z(); Psith_r = Z(); Psir_y = Z(); Psir_x = Z()
    for n in range(1, NO + 1):
        m = 2 * n
        gn = prof['g'][n - 1][:, None]; dgn = prof['dg'][n - 1][:, None]
        pn = prof['psi'][n - 1][:, None]; dpn = prof['dpsi'][n - 1][:, None]
        s_m = torch.sin(m * TH); c_m = torch.cos(m * TH)
        SR = sinratio(m, th)[None, :]                      # sin(2n th)/sin th
        SX = -((-1) ** n) * sinratio(m, dlt)[None, :]      # sin(2n th)/cos th
        S2 = 2.0 * sinratio(n, 2 * th)[None, :]            # sin(2n th)/(sin th cos th)
        Om += gn * s_m; Omr += dgn * s_m; Omth_r += m * (gn / R) * c_m
        Om_xy += (gn / R / R) * S2; Omr_y += (dgn / R) * SR; Omr_x += (dgn / R) * SX
        Psi += pn * s_m; Psir += dpn * s_m; Psith_r += m * (pn / R) * c_m
        Psir_y += (dpn / R) * SR; Psir_x += (dpn / R) * SX
    Omx = cs * Omr - sn * Omth_r; Omy = sn * Omr + cs * Omth_r
    Omx_y = cs * Omr_y - Omth_r / R                        # Omega_x / y
    Omy_x = sn * Omr_x + Omth_r / R                        # Omega_y / x
    U1 = -(sn * Psir + cs * Psith_r); U2 = cs * Psir - sn * Psith_r
    U1_x = -(sn * Psir_x + Psith_r / R)                    # U1 / x
    U2_y = cs * Psir_y - Psith_r / R                       # U2 / y
    X = R * cs; Y = R * sn
    W1 = beta * X + U1; W2 = beta * Y + U2
    W1_x = beta + U1_x; W2_y = beta + U2_y
    out = dict(Th=Th, Thx=Thx, Thy=Thy, Om=Om, Omx=Omx, Omy=Omy, Psi=Psi, U1=U1, U2=U2, W1=W1, W2=W2, X=X, Y=Y,
               Th_y=Th_y, Thx_y=Thx_y, Thx_xy=Thx_xy, Om_xy=Om_xy, Omx_y=Omx_y, Omy_x=Omy_x, W1_x=W1_x, W2_y=W2_y, U1_x=U1_x, U2_y=U2_y)
    out['RT'] = W1 * Thx + W2 * Thy - (beta - 2) * Th
    out['RO'] = W1 * Omx + W2 * Omy + Om - Thx
    out['NT'] = (W1 * Thx).abs() + (W2 * Thy).abs() + abs(beta - 2) * Th.abs()
    out['NO'] = (W1 * Omx).abs() + (W2 * Omy).abs() + Om.abs() + Thx.abs()
    out['RT_y'] = W1 * Thx_y + W2_y * Thy - (beta - 2) * Th_y
    out['NT_y'] = (W1 * Thx_y).abs() + (W2_y * Thy).abs() + abs(beta - 2) * Th_y.abs()
    out['RO_xy'] = W1_x * Omx_y + W2_y * Omy_x + Om_xy - Thx_xy
    out['NO_xy'] = (W1_x * Omx_y).abs() + (W2_y * Omy_x).abs() + Om_xy.abs() + Thx_xy.abs()
    return out
