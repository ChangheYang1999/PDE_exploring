"""Gauss-Newton / Levenberg-Marquardt profile search (dense Jacobian, GPU float64).
Unknowns: Chebyshev coefficients of Theta modes (NT*K), Omega modes (NO*K), optionally beta.
Rows: weighted R_Theta, weighted R_Omega on a polar collocation grid, and the centre constraint c+2=0 (heavy weight).
Frozen-basis treatment of beta: far-field exponents follow beta; after beta changes the basis is rebuilt and the
fields are re-projected onto the new basis.
"""
import argparse, json, math, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from polarlib import *

ap = argparse.ArgumentParser()
ap.add_argument('--beta', type=float, default=3.0)
ap.add_argument('--free-beta', action='store_true')
ap.add_argument('--NT', type=int, default=16)
ap.add_argument('--NO', type=int, default=16)
ap.add_argument('--K', type=int, default=40)
ap.add_argument('--umax', type=float, default=1e3, help='fit domain r_max/L')
ap.add_argument('--qmax', type=float, default=None, help='fit domain as q_max (overrides umax)')
ap.add_argument('--Nr', type=int, default=200)
ap.add_argument('--Nth', type=int, default=40)
ap.add_argument('--L', type=float, default=1.0)
ap.add_argument('--iters', type=int, default=30)
ap.add_argument('--lam', type=float, default=1e-3, help='initial LM damping (relative to max singular value)')
ap.add_argument('--a0', type=float, default=10.0)
ap.add_argument('--init', type=str, default='basic')
ap.add_argument('--seed', type=int, default=0)
ap.add_argument('--noise', type=float, default=0.0, help='relative random perturbation of the initial coefficients')
ap.add_argument('--wc', type=float, default=1e3, help='weight of the centre constraint row')
ap.add_argument('--eps-th', type=float, default=0.05)
ap.add_argument('--wmode', type=str, default='current', help='proxy | current')
ap.add_argument('--floor', type=float, default=0.03)
ap.add_argument('--colscale', type=int, default=1)
ap.add_argument('--center-rows', type=int, default=1, help='add Taylor identity rows T1, T2 at the origin')
ap.add_argument('--wcenter', type=float, default=1.0)
ap.add_argument('--fix-a0', type=float, default=None, help='constrain a0 = value (heavy linear row)')
ap.add_argument('--n2x', type=float, default=1.0, help='N2 gauge: Theta_y(n2x*L, 0) = a0/2 (choose n2x = current half-width to avoid a transient)')
ap.add_argument('--out', type=str, required=True)
ap.add_argument('--gauge', type=str, default='none', help="none | thxxy=<value> : fix Theta_xxy(0)/a0 (scaling gauge)")
args = ap.parse_args()

torch.manual_seed(args.seed)
device = dev()
os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
logf = open(args.out + '.log', 'a')
def log(s):
    print(s); logf.write(s + '\n'); logf.flush()
log(f'# {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} args={vars(args)}')

NT, NO, K = args.NT, args.NO, args.K
nT, nO = NT * K, NO * K

def make_grid(P):
    qmax = args.qmax if args.qmax is not None else P.q_of_u(torch.tensor(args.umax, dtype=DT)).item()
    # Chebyshev-clustered nodes in q on (0, qmax]
    j = torch.arange(args.Nr, dtype=DT, device=device)
    q = qmax * 0.5 * (1 - torch.cos(math.pi * (j + 0.5) / args.Nr))
    r = P.u_of_q(q) * P.L
    r, _ = torch.sort(r)
    xg, wg = np.polynomial.legendre.leggauss(args.Nth)
    th = torch.tensor((xg + 1) * 0.25 * math.pi, dtype=DT, device=device)
    return Grid(r, th)

def a0_of(cT, P):
    sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device)
    return float(cT[:K] @ sgn) / P.L

def omxy0_of(cO, P):
    sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device)
    return 2.0 * float(cO[:K] @ sgn) / P.L ** 2

def thxxy0_of(cT, P):
    # Theta = f_0 sin th + f_1 sin 3th + ...; near 0 f_0 = a0 r + a02 r^3, f_1 = b r^3. Theta_xxy(0) = coefficient of x^2 y times 2.
    # r^3 sin th = y r^2 = x^2 y + y^3 ; r^3 sin 3th = 3 x^2 y - y^3.  So x^2 y coefficient = a02 + 3 b, Theta_xxy = 2(a02 + 3b).
    # f_0 = u E^{(gT-1)/2} P_0(q) ; r^3 coefficient of f_0 / L^3: from E^{(gT-1)/2} ~ 1 + (gT-1)/2 u^2 and P_0(q) ~ P_0(0) + P_0'(0) q, q ~ mu u^2 /2
    sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device)
    dsgn = torch.tensor([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(K)], dtype=DT, device=device)  # d/dq T_k(2q-1) at q=0 = 2 T_k'(-1) = 2 (-1)^{k+1} k^2
    P0 = float(cT[:K] @ sgn); dP0 = float(cT[:K] @ dsgn)
    a02 = (P0 * (P.gamma_T - 1) / 2 + dP0 * P.mu / 2) / P.L ** 3
    b = float(cT[K:2 * K] @ sgn) / P.L ** 3 if NT > 1 else 0.0
    return 2.0 * (a02 + 3 * b)

def center_functionals(P):
    """Linear functionals (as coefficient vectors) for a0, b1, b2 (from cT) and G2, M2 (from cO):
    Theta = a0 y + b1 x^2 y + b2 y^3 + ..., Omega = 2 G2 x y + ..., M2 = int_0^inf g_2(s) s^-3 ds.
    d1 = -G2/6 + M2/2, d2 = -G2/6 - M2/2 (Psi = -2xy + d1 x^3 y + d2 x y^3 + ...)."""
    sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device)
    dsgn = torch.tensor([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(K)], dtype=DT, device=device)
    va0 = torch.zeros(nT, dtype=DT, device=device); va0[:K] = sgn / P.L
    va02 = torch.zeros(nT, dtype=DT, device=device); va02[:K] = ((P.gamma_T - 1) / 2 * sgn + P.mu / 2 * dsgn) / P.L ** 3
    vb = torch.zeros(nT, dtype=DT, device=device)
    if NT > 1: vb[K:2 * K] = sgn / P.L ** 3
    vb1 = va02 + 3 * vb; vb2 = va02 - vb
    vG2 = torch.zeros(nO, dtype=DT, device=device); vG2[:K] = sgn / P.L ** 2
    vM2 = torch.zeros(nO, dtype=DT, device=device)
    if NO > 1:
        # M_n = (1/(2 L^{2n-2})) (2/mu) int_0^1 (1-q)^{(2n-2) beta_eff} T_k dq with (2n-2)beta_eff = -(gamma_O-2n)/mu - 2/mu - 1 ; n = 2
        xq, wq = gl_nodes(256, device); q = 0.5 * (xq + 1); w = 0.5 * wq
        T2, _ = cheb_T_and_dT(q, K)
        expo = -(P.gamma_O - 4) / P.mu - 2.0 / P.mu - 1.0
        vM2[K:2 * K] = (1.0 / (2 * P.L ** 2)) * (2.0 / P.mu) * torch.einsum('g,gk->k', w * (1 - q) ** expo, T2)
    return dict(a0=va0, b1=vb1, b2=vb2, G2=vG2, M2=vM2)

def center_rows(P, cT, cO, beta):
    """Returns (values (2,), Jacobian (2, nT+nO)) of T1 = (2beta+4) b1 + 3 a0 d1 and T2 = 2(beta-2) b2 + a0 d2."""
    F = center_functionals(P)
    a0 = float(F['a0'] @ cT); b1 = float(F['b1'] @ cT); b2 = float(F['b2'] @ cT)
    G2 = float(F['G2'] @ cO); M2 = float(F['M2'] @ cO)
    d1 = -G2 / 6 + M2 / 2; d2 = -G2 / 6 - M2 / 2
    vd1 = -F['G2'] / 6 + F['M2'] / 2; vd2 = -F['G2'] / 6 - F['M2'] / 2
    T1 = (2 * beta + 4) * b1 + 3 * a0 * d1; T2 = 2 * (beta - 2) * b2 + a0 * d2
    J1 = torch.cat([(2 * beta + 4) * F['b1'] + 3 * d1 * F['a0'], 3 * a0 * vd1])
    J2 = torch.cat([2 * (beta - 2) * F['b2'] + d2 * F['a0'], a0 * vd2])
    return torch.tensor([T1, T2], dtype=DT, device=device), torch.stack([J1, J2]), dict(a0=a0, b1=b1, b2=b2, d1=d1, d2=d2, G2=G2, M2=M2)

GRID0 = [None]
def build(P):
    if GRID0[0] is None:
        GRID0[0] = make_grid(P)
    grid = GRID0[0]
    Mx = field_matrices(P, grid, NT, NO, K)
    return grid, Mx

def weights(P, grid, a0, g0, Rs=None):
    u = grid.R / P.L; E = 1 + u * u
    ST = max(abs(a0), 1e-12) * grid.R * E ** (-1.0 / P.beta) * (grid.sin + args.eps_th)
    SO = max(abs(g0), 1e-12) * grid.R ** 2 * E ** (-1.0 - 0.5 / P.beta) * (0.5 * torch.sin(2 * grid.TH) + args.eps_th)
    if Rs is None or args.wmode == 'proxy':
        return 1.0 / ST, 1.0 / SO
    # current pointwise normalizers with a floor (args.floor * proxy)
    return 1.0 / torch.maximum(Rs['NT'], args.floor * ST), 1.0 / torch.maximum(Rs['NO'], args.floor * SO)

# ---------------- initial state
beta = args.beta
P = Params(beta, L=args.L)
grid, Mx = build(P)
if args.init == 'basic':
    cT = torch.zeros(nT, dtype=DT, device=device); cO = torch.zeros(nO, dtype=DT, device=device)
    cT[0] = args.a0 * P.L
    cO[0] = -4.0 / beta     # c = (beta/2) * Q_10 = -2
else:
    d = np.load(args.init)
    def repad(c, Nold, Kold, Nnew, Knew):
        c = c.reshape(Nold, Kold)
        out = np.zeros((Nnew, Knew))
        nn, kk = min(Nold, Nnew), min(Kold, Knew)
        out[:nn, :kk] = c[:nn, :kk]
        return out.reshape(-1)
    cT = torch.tensor(repad(d['cT'], int(d['NT']), int(d['K']), NT, K), dtype=DT, device=device)
    cO = torch.tensor(repad(d['cO'], int(d['NO']), int(d['K']), NO, K), dtype=DT, device=device)
    if not args.free_beta and abs(float(d['beta']) - beta) > 1e-12:
        log(f'# init file beta {float(d["beta"])} differs from --beta {beta}; re-projecting fields')
        P_old = Params(float(d['beta']), L=float(d['L']))
        Mx_old = field_matrices(P_old, grid, NT, NO, K)
        cT = torch.linalg.lstsq(Mx['TH'], (Mx_old['TH'] @ cT)[:, None]).solution[:, 0]
        cO = torch.linalg.lstsq(Mx['OM'], (Mx_old['OM'] @ cO)[:, None]).solution[:, 0]
    elif args.free_beta:
        beta = float(d['beta']); P = Params(beta, L=args.L); grid, Mx = build(P)
if args.noise > 0:
    cT = cT + args.noise * cT.abs().max() * torch.randn_like(cT)
    cO = cO + args.noise * cO.abs().max() * torch.randn_like(cO)

A0NORM = [1.0]   # frozen per iteration (denominator of the Taylor rows), so that the Jacobian of those rows is exact
def gauge_rows_values(P_, cT_, cO_, beta_):
    """Values of the linear constraint rows (fix-a0, gauge n2, b1=, thxxy=) at the given state; list of floats."""
    vals = []
    if args.fix_a0 is not None:
        vals.append(float(center_functionals(P_)['a0'] @ cT_) - args.fix_a0)
    if args.gauge == 'n2':
        Fc = center_functionals(P_); r1 = torch.tensor([args.n2x * P_.L], dtype=DT, device=device)
        v = torch.zeros(nT, dtype=DT, device=device)
        for n in range(NT):
            H, _ = radial_basis(P_, r1, 2 * n + 1, P_.gamma_T, K); v[n * K:(n + 1) * K] = (2 * n + 1) * H[0] / r1[0]
        vals.append(float((v - 0.5 * Fc['a0']) @ cT_))
    if args.gauge.startswith('b1='):
        vals.append(0.5 * thxxy0_of(cT_, P_) - float(args.gauge.split('=')[1]))
    if args.gauge.startswith('thxxy='):
        vals.append(thxxy0_of(cT_, P_) - float(args.gauge.split('=')[1]) * a0_of(cT_, P_))
    return vals

def objective(Mx, grid, cT, cO, beta, wT, wO, P_=None):
    P_ = P_ if P_ is not None else P
    Rs = residuals(Mx, grid, cT, cO, beta)
    cval = float(Mx['crow'] @ cO)
    rows = torch.cat([wT * Rs['RT'], wO * Rs['RO'], torch.tensor([args.wc * (cval + 2.0)], dtype=DT, device=device)])
    if args.center_rows:
        Tv, _, info = center_rows(P_, cT, cO, beta)
        rows = torch.cat([rows, args.wcenter * Tv / A0NORM[0]])
    gv = gauge_rows_values(P_, cT, cO, beta)
    if gv:
        rows = torch.cat([rows, args.wc * torch.tensor(gv, dtype=DT, device=device)])
    return rows, Rs, cval

lam_rel = args.lam
nunk = nT + nO + (1 if args.free_beta else 0)
hist = []
for it in range(args.iters):
    t0 = time.time()
    a0 = a0_of(cT, P); g0 = omxy0_of(cO, P)
    A0NORM[0] = max(abs(a0), 1e-12)
    Rs0 = residuals(Mx, grid, cT, cO, beta)
    wT, wO = weights(P, grid, a0, g0, Rs0)
    rows, Rs, cval = objective(Mx, grid, cT, cO, beta, wT, wO)
    obj = float(rows @ rows)
    nrmT = float((Rs['RT'].abs() / (Rs['NT'] + 1e-300)).max()); nrmO = float((Rs['RO'].abs() / (Rs['NO'] + 1e-300)).max())
    # Jacobian
    U1, U2 = Rs['U1'][:, None], Rs['U2'][:, None]
    x, y = grid.x[:, None], grid.y[:, None]
    JT_T = wT[:, None] * (beta * (x * Mx['THx'] + y * Mx['THy']) - (beta - 2) * Mx['TH'] + U1 * Mx['THx'] + U2 * Mx['THy'])
    JT_O = wT[:, None] * (Rs['Thx'][:, None] * Mx['U1'] + Rs['Thy'][:, None] * Mx['U2'])
    JO_T = wO[:, None] * (-Mx['THx'])
    JO_O = wO[:, None] * (beta * (x * Mx['OMx'] + y * Mx['OMy']) + Mx['OM'] + U1 * Mx['OMx'] + U2 * Mx['OMy']
                          + Rs['Omx'][:, None] * Mx['U1'] + Rs['Omy'][:, None] * Mx['U2'])
    Jc = torch.cat([torch.zeros(1, nT, dtype=DT, device=device), args.wc * Mx['crow'][None, :]], 1)
    J = torch.cat([torch.cat([JT_T, JT_O], 1), torch.cat([JO_T, JO_O], 1), Jc], 0)
    if args.center_rows:
        Tv, Jcen, cinfo = center_rows(P, cT, cO, beta)
        J = torch.cat([J, args.wcenter * Jcen / A0NORM[0]], 0)
    else:
        cinfo = dict(T1=None)
    # linear constraint rows (same order as gauge_rows_values): fix-a0, n2, b1=, thxxy=
    extra_rows = []
    if args.fix_a0 is not None:
        Fc = center_functionals(P); e = torch.zeros(nT + nO, dtype=DT, device=device); e[:nT] = Fc['a0']; extra_rows.append(e)
    if args.gauge == 'n2':
        Fc = center_functionals(P); r1 = torch.tensor([args.n2x * P.L], dtype=DT, device=device)
        v = torch.zeros(nT, dtype=DT, device=device)
        for n in range(NT):
            H, _ = radial_basis(P, r1, 2 * n + 1, P.gamma_T, K); v[n * K:(n + 1) * K] = (2 * n + 1) * H[0] / r1[0]
        e = torch.zeros(nT + nO, dtype=DT, device=device); e[:nT] = v - 0.5 * Fc['a0']; extra_rows.append(e)
    if args.gauge.startswith('b1=') or args.gauge.startswith('thxxy='):
        val = float(args.gauge.split('=')[1]); isb1 = args.gauge.startswith('b1=')
        base = torch.zeros(nT, dtype=DT, device=device)
        for jdx in range(min(2 * K, nT)):
            ej = torch.zeros(nT, dtype=DT, device=device); ej[jdx] = 1.0
            base[jdx] = (0.5 * thxxy0_of(ej, P)) if isb1 else (thxxy0_of(ej, P) - val * a0_of(ej, P))
        e = torch.zeros(nT + nO, dtype=DT, device=device); e[:nT] = base; extra_rows.append(e)
    if extra_rows:
        J = torch.cat([J, args.wc * torch.stack(extra_rows)], 0)
    if args.free_beta:
        # full beta derivative (basis exponents move with beta, coefficients fixed) by central differences; covers all rows
        db = 1e-4
        _, Mx_p = build(Params(beta + db, L=args.L)); _, Mx_m = build(Params(beta - db, L=args.L))
        rows_p, _, _ = objective(Mx_p, grid, cT, cO, beta + db, wT, wO, Params(beta + db, L=args.L))
        rows_m, _, _ = objective(Mx_m, grid, cT, cO, beta - db, wT, wO, Params(beta - db, L=args.L))
        J = torch.cat([J, ((rows_p - rows_m) / (2 * db))[:, None]], 1)
        del Mx_p, Mx_m
    assert J.shape[0] == rows.shape[0], (J.shape, rows.shape)
    # SVD-based LM step with simple trust strategy; optional column equilibration (Jacobi scaling)
    if args.colscale:
        cn = torch.sqrt((J * J).sum(0)); cn = torch.where(cn > 0, cn, torch.ones_like(cn))
        J = J / cn[None, :]
    else:
        cn = torch.ones(J.shape[1], dtype=DT, device=device)
    Usvd, S, Vh = torch.linalg.svd(J, full_matrices=False)
    UtR = Usvd.T @ rows
    smax = float(S[0]); smin = float(S[-1])
    accepted = False
    for trial in range(8):
        lam = lam_rel * smax
        delta = -(Vh.T @ (S / (S * S + lam * lam) * UtR)) / cn
        cT_n = cT + delta[:nT]; cO_n = cO + delta[nT:nT + nO]
        beta_n = beta + float(delta[-1]) if args.free_beta else beta
        if args.free_beta and (beta_n < 2.05 or beta_n > 50):
            lam_rel *= 10; continue
        if args.free_beta and abs(beta_n - beta) > 1e-12:
            P_n = Params(beta_n, L=args.L)
            grid_n, Mx_n = build(P_n)
        else:
            P_n, grid_n, Mx_n = P, grid, Mx
        # evaluate the trial with the SAME weights (same objective) unless the grid changed (beta step)
        wT_n, wO_n = wT, wO
        rows_n, Rs_n, cval_n = objective(Mx_n, grid_n, cT_n, cO_n, beta_n, wT_n, wO_n, P_n)
        obj_n = float(rows_n @ rows_n)
        if obj_n < obj:
            accepted = True
            cT, cO, beta, P, grid, Mx = cT_n, cO_n, beta_n, P_n, grid_n, Mx_n
            lam_rel = max(lam_rel / 3, 1e-10)
            break
        lam_rel *= 10
    Tv0, _, cinfo = center_rows(P, cT, cO, beta)
    Rs_post = residuals(Mx, grid, cT, cO, beta)
    nrmT = float((Rs_post['RT'].abs() / (Rs_post['NT'] + 1e-300)).max()); nrmO = float((Rs_post['RO'].abs() / (Rs_post['NO'] + 1e-300)).max())
    Rs = Rs_post
    rec = dict(it=it, obj=obj, obj_new=obj_n if accepted else obj, beta=beta, a0=a0_of(cT, P), omxy0=omxy0_of(cO, P), c=float(Mx['crow'] @ cO), thy10=float(0.0), T1=float(Tv0[0]), T2=float(Tv0[1]), b2=cinfo['b2'], d1=cinfo['d1'], d2=cinfo['d2'], thxxy0=thxxy0_of(cT, P), b1=0.5 * thxxy0_of(cT, P),
               maxnormT=nrmT, maxnormO=nrmO, maxabsT=float(Rs['RT'].abs().max()), maxabsO=float(Rs['RO'].abs().max()),
               smax=smax, smin=smin, s_last5=[float(v) for v in S[-5:]], lam_rel=lam_rel, accepted=accepted, dt=time.time() - t0)
    hist.append(rec)
    log(json.dumps(rec))
    np.savez(args.out + '.npz', cT=cT.cpu().numpy(), cO=cO.cpu().numpy(), beta=beta, L=args.L, NT=NT, NO=NO, K=K,
             umax=args.umax, Nr=args.Nr, Nth=args.Nth, gamma_T=P.gamma_T, gamma_O=P.gamma_O, mu=P.mu, hist=json.dumps(hist))
    if not accepted:
        log('# no decrease found; stopping'); break
log('# done')
