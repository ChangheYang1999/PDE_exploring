"""fixedsrc.py -- fixed SOURCE-VELOCITY block for the additive-forcing lambda path (lead 22:53Z/23:03Z, verifier 22:48Z).

W_lambda = beta X + U_rel[Omega] + lambda U_rel[f],  f = E - Omega_S fixed in its SEED representation (geometry g_src with
beta_basis = beta_seed), while the UNKNOWN fields Omega, Theta are represented in a basis retied to the current beta
(beta_basis = beta).  The source is never re-projected: its stream-function sine modes Psi_k^f(r), d/dr Psi_k^f(r)
(k = 1..K, k = 1 once-subtracted so that U_f(0) = 0) are evaluated at ARBITRARY target radii by the same full-plane modal
Green formula as bq3core.Geometry._build_inverse,
    I^-_k(r) = int_0^r (rho/r)^{k+1} Omega_k(rho) drho,   I^+_k(r) = int_r^inf (r/rho)^{k-1} Omega_k(rho) drho (k >= 2),
    I^+_1(r) = -int_0^r Omega_1(rho) drho,   Psi_k = (r/2k)(I^-_k + I^+_k),   Psi_k' = (I^+_k - I^-_k)/2,
    Omega_1 = rho (g_0 - g_2/2),  Omega_k = (rho/2)(g_{k-1} - g_{k+1}),
by Gauss quadrature on the seed's compactified t-grid (the last knot interval geometrically refined to t = 1, so the
integrals to infinity are complete) plus Gauss on the two partial intervals around each target radius.
The centre Taylor data of Psi_f (strain c_f = Psi_xy(0), h20, h30, h40, G_f(0,0), g_1^f'(0)) are linear functionals of
the seed coefficients and are computed once in the seed geometry with the formulas of charnewton.CharResidual.prepare.
Running this file performs the validation tests (see __main__)."""
import sys, os, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from numpy.polynomial.legendre import leggauss
from bq3core import DT


def omega_modes_at(g, cG, t, rho):
    """Omega_k(rho) for k = 1..K at arbitrary t (torch, any shape) with rho = r_of_t(t), from coefficients cG (K*Nb,) in geometry g.
    Returns (K, *t.shape)."""
    b = g.b; K, Nb = b.K, b.Nb
    shp = t.shape
    tn = np.clip(t.detach().cpu().numpy().ravel(), 0.0, 1.0 - 1e-16)
    Bv, _ = b._design(tn)
    Bv = torch.tensor(Bv, dtype=DT, device=t.device)                      # (n, Nb)
    gk = []
    for k in range(K):
        fac, _ = g.radial_factor(k, t.reshape(-1), g.pG)
        ck = cG[k * Nb:(k + 1) * Nb] * g.mask_k[k]
        gk.append(fac * (Bv @ ck))
    gk = torch.stack(gk, 0)                                                # (K, n)  g_k(rho)
    rho_f = rho.reshape(-1)
    Om = []
    for k in range(1, K + 1):
        lo = gk[k - 1] * (1.0 if k == 1 else 0.5)
        hi = 0.5 * gk[k + 1] if k + 1 < K else torch.zeros_like(lo)
        Om.append(rho_f * (lo - hi))
    return torch.stack(Om, 0).reshape(K, *shp)


def cross_inverse(g, cG, r_tgt, ng_part=None):
    """Psi_k(r_tgt), Psi_k'(r_tgt) for the sine modes k = 1..K of the vorticity x G[cG] represented in geometry g,
    at arbitrary radii r_tgt (torch 1D, all > ~1e-8; the map and its derivative are singular at r = 0).  Returns (Psi, dPsi) of shape (K, n)."""
    b = g.b; K = b.K; dev = r_tgt.device
    assert bool((r_tgt > 1e-8).all()), 'cross_inverse: target radii must be positive (> 1e-8); the centre data come from source_jets'
    ng = b.ng_quad if ng_part is None else ng_part
    t_t = g.t_of_r(r_tgt)
    tc = t_t.detach().cpu().numpy()
    edges = b.edges_q
    idx = np.clip(np.searchsorted(edges, tc, side='right') - 1, 0, len(edges) - 2)
    wq = b.w_quad; Nq = len(wq); n = len(tc)
    Wlow = np.zeros((n, Nq)); Whigh = np.zeros((n, Nq))
    for i in range(n):
        Wlow[i, : idx[i] * b.ng_quad] = wq[: idx[i] * b.ng_quad]
        Whigh[i, (idx[i] + 1) * b.ng_quad:] = wq[(idx[i] + 1) * b.ng_quad:]
    xg, wg = leggauss(ng)
    a = edges[idx]; bb = edges[idx + 1]
    tpl = 0.5 * (tc - a)[:, None] * xg[None, :] + 0.5 * (tc + a)[:, None]
    wpl = 0.5 * (tc - a)[:, None] * wg[None, :]
    tph = 0.5 * (bb - tc)[:, None] * xg[None, :] + 0.5 * (bb + tc)[:, None]
    wph = 0.5 * (bb - tc)[:, None] * wg[None, :]
    T = lambda z: torch.tensor(z, dtype=DT, device=dev)
    Wlow, Whigh, tpl, wpl, tph, wph = T(Wlow), T(Whigh), T(tpl), T(wpl), T(tph), T(wph)
    # vorticity modes on the full quadrature grid and on the partial intervals
    tq = b.t_quad_t; rq, drq = g.rq, g.drdtq
    Omq = omega_modes_at(g, cG, tq, rq)                                   # (K, Nq)
    rpl, drpl = g.r_of_t(tpl); rph, drph = g.r_of_t(tph)
    Ompl = omega_modes_at(g, cG, tpl, rpl)                                # (K, n, ng)
    Omph = omega_modes_at(g, cG, tph, rph)
    r = r_tgt
    with torch.no_grad():
        lr = torch.log(r)[:, None]; lrq = torch.log(rq)[None, :]; lrpl = torch.log(rpl); lrph = torch.log(rph)
    Psi = torch.zeros(K, n, dtype=DT, device=dev); dPsi = torch.zeros_like(Psi)
    for k in range(1, K + 1):
        Km = torch.exp((k + 1) * torch.clamp(lrq - lr, max=0.0)) * Wlow * drq[None, :]            # (n, Nq)
        Kpl = torch.exp((k + 1) * torch.clamp(lrpl - lr, max=0.0)) * wpl * drpl                   # (n, ng)
        Im = (Km * Omq[k - 1][None, :]).sum(1) + (Kpl * Ompl[k - 1]).sum(1)
        if k >= 2:
            Kp = torch.exp((k - 1) * torch.clamp(lr - lrq, max=0.0)) * Whigh * drq[None, :]
            Kph = torch.exp((k - 1) * torch.clamp(lr - lrph, max=0.0)) * wph * drph
            Ip = (Kp * Omq[k - 1][None, :]).sum(1) + (Kph * Omph[k - 1]).sum(1)
        else:
            I0 = ((Wlow * drq[None, :]) * Omq[0][None, :]).sum(1) + ((wpl * drpl) * Ompl[0]).sum(1)
            Ip = -I0
        Psi[k - 1] = r / (2 * k) * (Im + Ip)
        dPsi[k - 1] = 0.5 * (Ip - Im)
    return Psi, dPsi


def source_jets(g, cG):
    """Centre Taylor data of the stream function of x G[cG] in geometry g (formulas of CharResidual.prepare):
    c = Psi_xy(0) (strain), h20, h30, h40, G0 = G(0,0), g1p = g_1'(0).  Returns a dict of Python floats."""
    b = g.b; K, Nb = b.K, b.Nb
    wq = b.w_quad_t * g.drdtq; rq = g.rq
    def gq(k):
        return (cG[k * Nb:(k + 1) * Nb] @ g.Wq_k[k].T) / rq
    def Omq(k):
        lo = gq(k - 1) * (1.0 if k == 1 else 0.5)
        hi = 0.5 * gq(k + 1) if k + 1 < K else 0.0
        return rq * (lo - hi)
    h20 = 0.25 * (Omq(2) / rq) @ wq
    h30 = (1.0 / 6.0) * (Omq(3) / rq ** 2) @ wq if K >= 3 else torch.zeros((), dtype=DT, device=g.dev)
    h40 = (1.0 / 8.0) * (Omq(4) / rq ** 3) @ wq if K >= 4 else torch.zeros((), dtype=DT, device=g.dev)
    G0 = cG[0]
    g1p = g.g1prime0(cG[None])[0] if K > 1 else torch.zeros((), dtype=DT, device=g.dev)
    c = g.c_op @ cG
    return dict(c=float(c), h20=float(h20), h30=float(h30), h40=float(h40), G0=float(G0), g1p=float(g1p))


def velocity_from_modes(Psi, dPsi, x, y):
    """Cartesian (U1, U2) at points (x > 0, y) from sine-mode data Psi_k, Psi_k' (K, n) at the points' radii."""
    K = Psi.shape[0]
    r = torch.sqrt(x ** 2 + y ** 2); phi = torch.atan2(x, -y)
    ks = torch.arange(1, K + 1, dtype=DT, device=x.device)[:, None]
    Psir = (dPsi * torch.sin(ks * phi[None, :])).sum(0)
    Psiphi = (ks * Psi * torch.cos(ks * phi[None, :])).sum(0)
    s, c = torch.sin(phi), torch.cos(phi)
    U2 = s * Psir + c / r * Psiphi
    U1 = c * Psir - s / r * Psiphi
    return U1, U2


def make_grid(basis, device):
    """Radial interpolation grid descriptor of a Basis for CharResidual.interp(grid=...): Gauss nodes per knot interval and the monomial
    coefficients of the Lagrange basis on the reference interval (same construction as CharResidual.__init__)."""
    ng = len(basis.t_coll) // basis.Nt
    xi = leggauss(ng)[0]
    V = np.vander(xi, increasing=True)
    Lmono = torch.tensor(np.linalg.inv(V).T.copy(), dtype=DT, device=device)
    return dict(Nt=basis.Nt, edges=torch.tensor(basis.edges, dtype=DT, device=device), grade=basis.grade, ng=ng, Lmono=Lmono)


def make_source_block(g_src, cG_src, res, lam):
    """Attach the fixed source (coefficients cG_src in the SEED geometry g_src, with its OWN basis g_src.b: K_src, Nt_src, ... may differ
    from the unknown's) with multiplier lam to a CharResidual res whose unknown basis is retied (res.g may have any beta_basis).
    The source's modal data S_k^f = Psi_k^f(r_i)/r_i^{pk} are stored at the SEED geometry's collocation radii (exact modal inverse,
    Psi_op of g_src) and interpolated by CharResidual.velocity on the source's own radial grid in the seed's own t variable (where
    S_k^f is smooth; interpolating in the retied t fails in the far field, see the tests). Centre data from source_jets."""
    bs = g_src.b
    Psi = torch.einsum('kia,a->ki', g_src.Psi_op, cG_src)                  # (K_src, Nc_src) exact at the seed radii
    dev = Psi.device
    pk = torch.tensor([2.0 + (k % 2) for k in range(1, bs.K + 1)], dtype=DT, device=dev)
    ks = torch.arange(1, bs.K + 1, dtype=DT, device=dev)
    nodal = (Psi / g_src.r[None, :] ** pk[:, None]).T[None].contiguous()   # (1, Nc_src, K_src)
    jets = source_jets(g_src, cG_src)
    blk = dict(lam=float(lam), g=g_src, b=bs, grid=make_grid(bs, dev), pk=pk, ks=ks, nodal=nodal, Psi_nodal=Psi, cG_src=cG_src.clone(),
               beta_src=g_src.beta, K_src=bs.K, **jets)
    res.src = blk
    return blk


if __name__ == '__main__':
    import time
    from bq3core import Basis, Geometry
    torch.set_default_dtype(DT)
    dev = 'cuda' if torch.cuda.is_available() else 'cpu'
    # ---- test 1: cross inverse at the seed's own collocation radii reproduces Psi_op / dPsi_op (same quadrature)
    for rmap, grade in [('r2', 1.5), ('r', 1.5)]:
        b = Basis(40, 5, 12, 24, ng_coll=7, m_reg=2, device=dev, grade=grade)
        g = Geometry(b, 3.0, 1.5, rmap=rmap)
        act = g.active
        Dt = ((1 - b.t_coll_t) ** g.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1 / Dt
        Gt = torch.exp(-(g.x ** 2 + (g.y - 2.85) ** 2) / 2)
        cfit = torch.zeros(b.K * b.Nb, dtype=DT, device=dev)
        cfit[act] = torch.linalg.lstsq((g.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
        cG = (2.5 / (g.c_op @ cfit).item()) * cfit
        t0 = time.time(); Psi, dPsi = cross_inverse(g, cG, g.r); el = time.time() - t0
        Psi_ref = torch.einsum('kia,a->ki', g.Psi_op, cG); dPsi_ref = torch.einsum('kia,a->ki', g.dPsi_op, cG)
        sc = Psi_ref.abs().max(1).values + 1e-300
        print(f"[test1 {rmap}] cross inverse at own radii: max|dPsi|/max|Psi_k| = {((Psi - Psi_ref).abs().max(1).values / sc).max().item():.2e}, "
              f"max|d(dPsi)|/max|Psi_k'| = {((dPsi - dPsi_ref).abs().max(1).values / (dPsi_ref.abs().max(1).values + 1e-300)).max().item():.2e}  ({el:.2f}s)")
        jets = source_jets(g, cG)
        print(f"          jets: c = {jets['c']:.12f} (target 2.5), h20 = {jets['h20']:.6e}, h30 = {jets['h30']:.6e}, h40 = {jets['h40']:.6e}, G0 = {jets['G0']:.6e}, g1p = {jets['g1p']:.6e}")
    # ---- test 2: manufactured algebraic-tail case (test_inverse.make_case, beta_src = 3), velocity at the radii/points of a
    # DIFFERENT geometry (beta_tgt = 2.6 and 3.4) compared with the exact velocity
    from test_inverse import make_case
    import sympy as sp
    x_, y_ = sp.symbols('x y', real=True)
    h2 = (1 + y_ / 2 + x_ ** 2 / 5) * (1 + (x_ ** 2 + y_ ** 2) / 4) ** (-sp.Rational(2, 3))
    fG, fH, fHy, fU2, fU1, v0, c_ex = make_case(h2)
    for rmap in ['r2', 'r']:
        bs = Basis(80, 5, 24, 48, ng_coll=3, m_reg=2, device=dev, grade=1.0)
        gs = Geometry(bs, 3.0, 1.5, rmap=rmap)
        xs, ys = gs.x.cpu().numpy(), gs.y.cpu().numpy()
        Gv = torch.tensor(fG(xs, ys), dtype=DT, device=dev)
        Dt = ((1 - bs.t_coll_t) ** gs.pG)[:, None].expand(bs.Nc, bs.Nphi).reshape(-1); w = 1 / Dt
        cG = torch.zeros(gs.Phi0G.shape[1], dtype=DT, device=dev)
        cG[gs.active] = torch.linalg.lstsq((gs.Phi0G * w[:, None])[:, gs.active], (Gv * w)[:, None], driver='gels').solution[:, 0]
        print(f"[test2 {rmap}] seed fit: weighted G error {((gs.Phi0G @ cG - Gv) / Dt).abs().max().item():.2e}; c = {(gs.c_op @ cG).item():.10f} (exact {c_ex:.10f})")
        for beta_t in [2.6, 3.4]:
            bt = Basis(40, 5, 12, 24, ng_coll=7, m_reg=2, device=dev, grade=1.5)
            gt = Geometry(bt, beta_t, 1.5, rmap=rmap)
            Psi, dPsi = cross_inverse(gs, cG, gt.r)                     # modes at the target radii
            # expand to the target's angular nodes
            Nc, Nphi = bt.Nc, bt.Nphi
            X = gt.x.reshape(Nc, Nphi); Y = gt.y.reshape(Nc, Nphi)
            PsiE = Psi[:, :, None].expand(-1, -1, Nphi).reshape(bs.K, -1); dPsiE = dPsi[:, :, None].expand(-1, -1, Nphi).reshape(bs.K, -1)
            U1, U2 = velocity_from_modes(PsiE, dPsiE, X.reshape(-1), Y.reshape(-1))
            xt, yt = gt.x.cpu().numpy(), gt.y.cpu().numpy()
            U1ex = fU1(xt, yt); U2ex = fU2(xt, yt) - v0
            rr = gt.rr.cpu().numpy(); scale = (1 + rr) ** (1 - 1 / 3.0)
            e = (np.abs(U1.cpu().numpy() - U1ex) + np.abs(U2.cpu().numpy() - U2ex)) / scale
            line = f"   target beta_basis {beta_t}: max scaled U error {e.max():.2e};"
            for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e30)]:
                m = (rr >= lo) & (rr < hi)
                if m.any():
                    line += f" [{lo:g},{hi:g}) {e[m].max():.1e}"
            print(line)
    # ---- test 3: interpolation of the source block along trajectories (the velocity routine interpolates S_k = Psi_k/r^pk
    # in the TARGET geometry's t): compare the interpolated source velocity at off-node points with the exact cross inverse
    from charnewton import CharResidual
    b = Basis(40, 5, 12, 24, ng_coll=7, m_reg=2, device=dev, grade=1.5)
    g = Geometry(b, 3.0, 1.5, rmap='r2')
    act = g.active
    Dt = ((1 - b.t_coll_t) ** g.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1 / Dt
    Gt = torch.exp(-(g.x ** 2 + (g.y - 2.85) ** 2) / 2)
    cfit = torch.zeros(b.K * b.Nb, dtype=DT, device=dev)
    cfit[act] = torch.linalg.lstsq((g.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
    cE = (2.5 / (g.c_op @ cfit).item()) * cfit
    # a slow-tail seed-like source: f = E - (a fitted algebraic-tail field with strain 2.5)
    xs, ys = g.x.cpu().numpy(), g.y.cpu().numpy()
    Gv = torch.tensor(fG(xs, ys), dtype=DT, device=dev)
    cS = torch.zeros_like(cfit); cS[act] = torch.linalg.lstsq((g.Phi0G * wfit[:, None])[:, act], (Gv * wfit)[:, None], driver='gels').solution[:, 0]
    cS = (2.5 / (g.c_op @ cS).item()) * cS
    cF_ = cE - cS
    print(f"[test3] source f = E - S: strain {(g.c_op @ cF_).item():+.2e}")
    for beta_t in [2.6, 3.0, 3.4]:
        res = CharResidual(b, 1.5, beta_t, Nphi_res=24, device=dev, rmap='r2', beta_fixed=beta_t, wc=0.0)
        blk = make_source_block(g, cF_, res, 1.0)
        b2 = Basis(40, 5, 12, 48, ng_coll=9, m_reg=2, device=dev, grade=1.5)
        g2 = Geometry(b2, beta_t, 1.5, rmap='r2')
        X = torch.stack([g2.x, g2.y], 1)[None]
        beta0 = torch.zeros(1, dtype=DT, device=dev)
        nodal0 = torch.zeros(1, b.Nc, b.K, dtype=DT, device=dev)       # no unknown field: W = lam U_f (interpolated block) with beta = 0
        W, aux = res.velocity(X, beta0, nodal0)
        Psi2, dPsi2 = cross_inverse(g, cF_, g2.r)
        Nc2, Nphi2 = b2.Nc, b2.Nphi
        P2 = Psi2[:, :, None].expand(-1, -1, Nphi2).reshape(b.K, -1); dP2 = dPsi2[:, :, None].expand(-1, -1, Nphi2).reshape(b.K, -1)
        U1e, U2e = velocity_from_modes(P2, dP2, g2.x, g2.y)
        e1 = (W[0, :, 0] - U1e).abs(); e2 = (W[0, :, 1] - U2e).abs(); sc = 1 + g2.rr; rr = g2.rr
        line = f"   target beta_basis {beta_t}: source-block interpolation error max|dU|/(1+r) = {(torch.maximum(e1, e2) / sc).max().item():.2e};"
        for lo, hi in [(0, 0.3), (0.3, 3), (3, 100), (100, 1e4), (1e4, 1e99)]:
            m = (rr >= lo) & (rr < hi)
            line += f" [{lo:g},{hi:g}) {(torch.maximum(e1, e2)[m] / sc[m]).max().item():.1e}"
        print(line)
    # ---- test 4: source in its OWN basis different from the unknown's (K 16 / Nt 56 seed source, K 12 / Nt 40 unknown basis, beta 2.8):
    # interpolated block velocity at off-node points versus the exact cross inverse of the seed source
    import os
    seed16 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'runs', 'fb30g16_eps0.npz')
    if os.path.exists(seed16):
        d16 = np.load(seed16)
        b16 = Basis(int(d16['Nt']), int(d16['deg']), int(d16['K']), int(d16['Nphi']), ng_coll=int(d16['ngc']), m_reg=int(d16['mreg']), device=dev, grade=float(d16['grade']))
        g16 = Geometry(b16, float(d16['beta_basis']), float(d16['L']), rmap=str(d16['rmap']))
        cf16 = torch.tensor(d16['cG_ext'] - d16['cG'], dtype=DT, device=dev)
        b12 = Basis(40, 5, 12, 24, ng_coll=7, m_reg=2, device=dev, grade=1.5)
        res = CharResidual(b12, 1.5, 2.8, Nphi_res=24, device=dev, rmap='r2', beta_fixed=2.8, wc=0.0)
        blk = make_source_block(g16, cf16, res, 1.0)
        b2 = Basis(40, 5, 12, 48, ng_coll=9, m_reg=2, device=dev, grade=1.5); g2 = Geometry(b2, 2.8, 1.5, rmap='r2')
        X = torch.stack([g2.x, g2.y], 1)[None]
        W, aux = res.velocity(X, torch.zeros(1, dtype=DT, device=dev), torch.zeros(1, b12.Nc, b12.K, dtype=DT, device=dev))
        Psi2, dPsi2 = cross_inverse(g16, cf16, g2.r)
        P2 = Psi2[:, :, None].expand(-1, -1, b2.Nphi).reshape(b16.K, -1); dP2 = dPsi2[:, :, None].expand(-1, -1, b2.Nphi).reshape(b16.K, -1)
        U1e, U2e = velocity_from_modes(P2, dP2, g2.x, g2.y)
        e = torch.maximum((W[0, :, 0] - U1e).abs(), (W[0, :, 1] - U2e).abs()); sc = 1 + g2.rr; rr = g2.rr
        line = f"[test4] K16/Nt56 seed source (strain {blk['c']:+.1e}) with a K12/Nt40 unknown basis at beta 2.8: block interpolation error max|dU|/(1+r) = {(e / sc).max().item():.2e};"
        for lo, hi in [(0, 0.3), (0.3, 3), (3, 100), (100, 1e4), (1e4, 1e99)]:
            m = (rr >= lo) & (rr < hi)
            line += f" [{lo:g},{hi:g}) {(e[m] / sc[m]).max().item():.1e}"
        print(line)
        print(f"        source centre data: {dict((k, round(blk[k], 8)) for k in ('c', 'h20', 'h30', 'h40', 'G0', 'g1p'))}")
