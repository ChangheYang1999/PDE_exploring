"""Psi-only characteristic (slaved-transport) solver: Levenberg-Marquardt with a batched finite-difference Jacobian (GPU).
Unknowns: Psi Chebyshev coefficients cP (NO x K), a0, optionally beta.  Theta and Omega are reconstructed from the velocity
by backward characteristics with the centre jets (charlib2.transport), so (P1), (P2) hold to ODE tolerance by construction.
Rows: w_i (Omega_basis_i - Omega_char_i) on a polar grid (w = proxy Omega scale), wc (c + 2), wc (h10 - h10_target) [gauge].
"""
import argparse, json, math, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from charlib2 import *

ap = argparse.ArgumentParser()
ap.add_argument('--init', required=True, help='npz with cP, a0, beta (proj_psi.py or charsolve output)')
ap.add_argument('--out', required=True)
ap.add_argument('--NO', type=int, default=None); ap.add_argument('--K', type=int, default=None)
ap.add_argument('--beta', type=float, default=None, help='override beta (basis exponents follow)')
ap.add_argument('--free-beta', action='store_true')
ap.add_argument('--Nr', type=int, default=150); ap.add_argument('--Nth', type=int, default=32)
ap.add_argument('--qmax', type=float, default=0.999)
ap.add_argument('--dt', type=float, default=0.005); ap.add_argument('--rstop', type=float, default=1e-3); ap.add_argument('--Tmax', type=float, default=40.0)
ap.add_argument('--iters', type=int, default=20)
ap.add_argument('--lam', type=float, default=1e-3)
ap.add_argument('--wc', type=float, default=1e2)
ap.add_argument('--eps-th', type=float, default=0.01)
ap.add_argument('--fdeps', type=float, default=1e-6)
ap.add_argument('--batch', type=int, default=32)
ap.add_argument('--gauge', type=str, default='h10', help='h10 | none')
ap.add_argument('--jac-every', type=int, default=1, help='recompute the FD Jacobian every k iterations (Broyden updates in between)')
ap.add_argument('--diag', action='store_true', help='only evaluate the initial state (consistency diagnostics) and exit')
ap.add_argument('--a0', type=float, default=None)
ap.add_argument('--fix-a0', type=float, default=None, help='hold a0 fixed at this value (no a0 column)')
ap.add_argument('--save-jac', type=int, default=0, help='save the reduced Jacobian, rows and Nfull of each FD iteration to <out>.jac<it>.npz')
ap.add_argument('--w0', type=float, default=1.0, help='weight of the centre Poisson closure row (relative)')
ap.add_argument('--hard', type=int, default=1, help='impose c = -2 and the gauge exactly (null-space parametrization of the LM step; initial cP rescaled to c = -2)')
args = ap.parse_args()

device = dev()
logf = open(args.out + '.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f'# {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} args={vars(args)}')

d = np.load(args.init, allow_pickle=True)
beta = float(d['beta']) if args.beta is None else args.beta
L = float(d['L']); NO0, K0 = int(d['NO']), int(d['K'])
NO = args.NO or NO0; K = args.K or K0
cP0 = np.zeros((NO, K)); nn, kk = min(NO, NO0), min(K, K0); cP0[:nn, :kk] = d['cP'].reshape(NO0, K0)[:nn, :kk]
cP = torch.tensor(cP0, dtype=DT, device=device)
a0 = float(d['a0']) if args.a0 is None else args.a0
if args.fix_a0 is not None: a0 = args.fix_a0
if args.hard:
    _F0 = PsiBasis(beta, NO, K, L=L).centre_functionals(device); _c0 = float(cP.reshape(-1) @ _F0['c'])
    if abs(_c0 + 2.0) > 1e-14:
        cP = cP * (-2.0 / _c0); a0 = a0   # velocity rescaled so that c = -2 exactly (a0 unchanged; the jets use c = -2)
        print(f'# initial c {_c0:.10f} rescaled to -2 (factor {-2.0 / _c0:.8f})')
log(f'# init {args.init}: beta {beta} NO {NO} K {K} a0 {a0:.6f}' + (f' (truncated from {NO0}x{K0})' if (NO, K) != (NO0, K0) else ''))

def make_basis(beta_):
    return PsiBasis(beta_, NO, K, L=L)

# collocation grid (Chebyshev-clustered in q up to qmax; Gauss angles)
def make_grid(bas):
    j = torch.arange(args.Nr, dtype=DT, device=device)
    q = args.qmax * 0.5 * (1 - torch.cos(math.pi * (j + 0.5) / args.Nr))
    r = bas.u_of_q(q) * bas.L
    xg, wg = np.polynomial.legendre.leggauss(args.Nth)
    th = torch.tensor((xg + 1) * 0.25 * math.pi, dtype=DT, device=device)
    R, TH = torch.meshgrid(r, th, indexing='ij'); R = R.reshape(-1); TH = TH.reshape(-1)
    return dict(r=r, th=th, R=R, TH=TH, x=R * torch.cos(TH), y=R * torch.sin(TH))

bas = make_basis(beta); grid = make_grid(bas)
N = grid['R'].shape[0]
log(f'# grid Nr {args.Nr} Nth {args.Nth} N {N} r in [{float(grid["r"][0]):.3e}, {float(grid["r"][-1]):.3e}]')
F = bas.centre_functionals(device)
h10_target = float(cP.reshape(-1) @ F['h10'])

def proxy_weights(bas, g00):
    u = grid['R'] / bas.L; E = 1 + u * u
    SO = max(abs(g00), 1e-12) * grid['R'] ** 2 * E ** (-1.0 - 0.5 / bas.beta) * (0.5 * torch.sin(2 * grid['TH']) + args.eps_th)
    return 1.0 / SO

def evaluate(bas, cPb, a0b, beta_, w):
    """cPb (B, NO, K), a0b (B,). Returns rows (B, nrows), info dict (B-wise tensors)."""
    tr = transport(bas, cPb, a0b, beta_, grid['x'], grid['y'], dt=args.dt, r_stop=args.rstop, T_max=args.Tmax)
    fb = bas.fields(cPb, grid['x'], grid['y'])
    Fv = fb['Om'] - tr['Om']                                        # (B, N)
    Fv = torch.where(tr['fail'], torch.zeros_like(Fv), Fv)          # failed points: zero here, but any failure REJECTS the trial (see below)
    rows = [w[None, :] * Fv, args.wc * (tr['c'] + 2.0)[:, None]]
    if args.gauge == 'h10':
        rows.append(args.wc * (tr['h10'] - h10_target)[:, None])
    # centre Poisson closure (external review charreview finding 4): g00_basis = -6 (h10 + h01) must equal the jet g00 = 2 f10/(2 beta + 1)
    f10_, f01_, g00_ = jets(beta_, a0b, tr['h10'], tr['h01'])
    rows.append((args.w0 * (-6.0 * (tr['h10'] + tr['h01']) - g00_) / (g00_.abs() + 1e-300))[:, None])
    rows = torch.cat(rows, 1)
    info = dict(Om_basis=fb['Om'], Om_char=tr['Om'], Th=tr['Th'], Thx=tr['Thx'], Thy=tr['Thy'], fail=tr['fail'], c=tr['c'], h10=tr['h10'], h01=tr['h01'], T=tr['T'], nsteps=tr['nsteps'])
    return rows, info

def summarize(info, w):
    Ob, Oc = info['Om_basis'][0], info['Om_char'][0]
    rel = (Ob - Oc).abs() / (Oc.abs() + Ob.abs() + 1e-300)
    sel = (Oc.abs() > 1e-6 * Oc.abs().max()) & ~info['fail'][0]
    relmax = float(rel[sel].max()); imax = int(torch.nonzero(sel)[rel[sel].argmax()])
    wF = (w * (Ob - Oc)).abs(); wmax = float(wF.max()); jmax = int(wF.argmax())
    # regional maxima of the weighted (floored relative) consistency defect
    bins = [(0, 0.1), (0.1, 1), (1, 10), (10, 1e2), (1e2, 1e4), (1e4, 1e6), (1e6, 1e9), (1e9, 1e13)]
    reg = []
    for lo, hi in bins:
        m = (grid['R'] >= lo) & (grid['R'] < hi)
        reg.append(float(wF[m].max()) if m.any() else None)
    return dict(relmax=relmax, relmax_r=float(grid['R'][imax]), relmax_deg=float(grid['TH'][imax]) * 180 / math.pi,
                wmax=wmax, wmax_r=float(grid['R'][jmax]), wmax_deg=float(grid['TH'][jmax]) * 180 / math.pi, regional=reg,
                nfail=int(info['fail'][0].sum()), Tmax=float(info['T'][0].max()), nsteps=info['nsteps'])

def point_diagnostics(bas, cP, a0, beta_):
    """Omega/(xy) basis vs transport-consistent at the authors' test points (phi = 85 deg and 5-20 deg)."""
    pts = [(0.1, 85), (0.3, 85), (1.0, 85), (2.0, 85), (0.03, 85), (0.5, 10), (0.7, 10), (1.0, 10), (0.5, 20), (1.0, 45), (10.0, 45), (100.0, 45), (1e4, 45), (1e6, 60), (1e8, 80)]
    x = torch.tensor([r * math.cos(math.radians(p)) for r, p in pts], dtype=DT, device=device); y = torch.tensor([r * math.sin(math.radians(p)) for r, p in pts], dtype=DT, device=device)
    tr = transport(bas, cP[None], a0, beta_, x, y, dt=args.dt, r_stop=args.rstop, T_max=args.Tmax)
    fb = bas.fields(cP[None], x, y)
    out = []
    for i, (r, p) in enumerate(pts):
        xy = float(x[i] * y[i])
        out.append(dict(r=r, deg=p, Om_basis_xy=float(fb['Om'][0, i]) / xy, Om_char_xy=float(tr['Om'][0, i]) / xy, Thx_char_xy=float(tr['Thx'][0, i]) / xy, Th_char_y=float(tr['Th'][0, i]) / float(y[i]), T=float(tr['T'][0, i]), fail=bool(tr['fail'][0, i])))
    return out

# ---------------- initial evaluation
f10, f01, g00 = jets(beta, a0, float(cP.reshape(-1) @ F['h10']), float(cP.reshape(-1) @ F['h01']))
w = proxy_weights(bas, g00)
t0 = time.time()
rows0, info0 = evaluate(bas, cP[None], torch.tensor([a0], dtype=DT, device=device), beta, w)
torch.cuda.synchronize(); tev = time.time() - t0
obj = float((rows0[0] ** 2).sum()); summ = summarize(info0, w)
log(json.dumps(dict(it=-1, obj=obj, a0=a0, beta=beta, c=float(info0['c'][0]), h10=float(info0['h10'][0]), h01=float(info0['h01'][0]), g00=g00, **summ, t_eval=tev)))
if args.diag or True:
    pd = point_diagnostics(bas, cP, a0, beta)
    log('# point diagnostics (Omega/(xy): basis vs transport-consistent; Theta_x/(xy) char; Theta/y char):')
    for p in pd:
        log('#   r=%8.3g phi=%2d: Om/xy basis %+.5f  char %+.5f  (rel diff %.3e)   Thx/xy char %+.5f  Th/y %.5f  T %.2f %s' % (p['r'], p['deg'], p['Om_basis_xy'], p['Om_char_xy'], abs(p['Om_basis_xy'] - p['Om_char_xy']) / (abs(p['Om_char_xy']) + 1e-300), p['Thx_char_xy'], p['Th_char_y'], p['T'], 'FAIL' if p['fail'] else ''))
if args.diag:
    sys.exit(0)

# ---------------- LM loop
nunk = NO * K + 1 + (1 if args.free_beta else 0)
J = None; hist = []; lam_rel = args.lam
x_prev = None; rows_prev = None
for it in range(args.iters):
    t0 = time.time()
    xcur = torch.cat([cP.reshape(-1), torch.tensor([a0] + ([beta] if args.free_beta else []), dtype=DT, device=device)])
    F = bas.centre_functionals(device)
    if args.free_beta: h10_target = float(cP.reshape(-1) @ F['h10'])   # floating gauge target: each step is orthogonal to the current dilation direction
    need_full = (J is None) or (it % args.jac_every == 0)
    if need_full:
        ncol = NO * K
        if args.hard:
            Cm = torch.stack([F['c']] + ([F['h10']] if args.gauge == 'h10' else []))
            Qc, Rc = torch.linalg.qr(Cm.T, mode='complete'); Nc = Qc[:, Cm.shape[0]:]                    # (ncol, ncol - nc) admissible directions in cP
            assert float(Rc.diagonal().abs().min()) > 1e-12, 'dependent constraints'
        else:
            Nc = torch.eye(ncol, dtype=DT, device=device)
        nd = Nc.shape[1]
        Jc = torch.zeros(rows0.shape[1], nd, dtype=DT, device=device)
        eps = args.fdeps
        for s in range(0, nd, args.batch):
            idx = list(range(s, min(s + args.batch, nd))); Bn = len(idx)
            cPb = cP.reshape(-1)[None, :] + eps * Nc[:, idx].T                                            # every probe satisfies c = -2 and the gauge exactly
            rows_b, info_b = evaluate(bas, cPb.reshape(Bn, NO, K), torch.full((Bn,), a0, dtype=DT, device=device), beta, w)
            if bool(info_b['fail'].any()): log(f'#   warning: {int(info_b["fail"].sum())} failed trajectories in FD probes {s}..{s + Bn}')
            Jc[:, idx] = ((rows_b - rows0[0][None, :]) / eps).T
            if (s // args.batch) % 8 == 0: log(f'#   jacobian columns {s + Bn}/{nd} ({time.time() - t0:.0f}s)')
        # a0 column (Omega_char linear in a0; unit-amplitude form): d rows/d a0 = -w Om_char/a0 on the grid rows; closure row depends on a0 through g00 only (ratio is a0-free)
        col = torch.zeros(rows0.shape[1], dtype=DT, device=device)
        col[:N] = -w * info0['Om_char'][0] / a0
        # centre-closure row (last row) depends on a0 through g00 = kappa a0: d/da0 [w0 (B - g00)/|g00|] = -w0 B/(|g00| a0), B = -6(h10+h01)
        # (missing entry found by the verifier, 22:51Z; value 0.0203 for the cs6 state)
        _B = -6.0 * (float(info0['h10'][0]) + float(info0['h01'][0])); _g00 = jets(beta, a0, float(info0['h10'][0]), float(info0['h01'][0]))[2]
        col[-1] = -args.w0 * _B / (abs(_g00) * a0 + 1e-300)
        if args.fix_a0 is not None: col[:] = 0.0
        cols = [Jc, col[:, None]]
        if args.free_beta:
            db = 1e-4
            bas_p = make_basis(beta + db)
            rows_p, _ = evaluate(bas_p, cP[None], torch.tensor([a0], dtype=DT, device=device), beta + db, w)
            cols.append(((rows_p[0] - rows0[0]) / db)[:, None])
        J = torch.cat(cols, 1)                                                                            # reduced Jacobian (admissible directions, a0[, beta])
        # map from reduced step z to the full step: delta = Nfull z
        Nfull = torch.zeros(nunk, J.shape[1], dtype=DT, device=device); Nfull[:ncol, :nd] = Nc; Nfull[ncol, nd] = 1.0
        if args.free_beta: Nfull[ncol + 1, nd + 1] = 1.0
        jac_kind = 'fd'
        if args.save_jac:
            np.savez(f'{args.out}.jac{it}.npz', J=J.cpu().numpy(), rows=rows0[0].cpu().numpy(), Nfull=Nfull.cpu().numpy(), w=w.cpu().numpy(), x=xcur.cpu().numpy(), N=N)
    else:
        # Broyden rank-1 update with the last accepted step
        dx = Nfull.T @ (xcur - x_prev); dF = rows0[0] - rows_prev
        J = J + torch.outer(dF - J @ dx, dx) / (dx @ dx)
        jac_kind = 'broyden'
    tj = time.time() - t0
    Jr = J
    cn = torch.sqrt((Jr * Jr).sum(0)); cn = torch.where(cn > 0, cn, torch.ones_like(cn))
    Js = Jr / cn[None, :]
    U, S, Vh = torch.linalg.svd(Js, full_matrices=False)
    UtR = U.T @ rows0[0]
    smax = float(S[0]); smin = float(S[-1])
    accepted = False; obj_n = obj
    for trial in range(8):
        lam = lam_rel * smax
        delta = -(Vh.T @ (S / (S * S + lam * lam) * UtR)) / cn
        delta = Nfull @ delta
        cP_n = cP + delta[:NO * K].reshape(NO, K); a0_n = a0 + (0.0 if args.fix_a0 is not None else float(delta[NO * K]))
        if abs(a0_n) < 1e-3 * abs(a0): lam_rel *= 10; continue
        beta_n = beta + float(delta[NO * K + 1]) if args.free_beta else beta
        if args.free_beta and (beta_n < 2.05 or beta_n > 20): lam_rel *= 10; continue
        bas_n = make_basis(beta_n) if args.free_beta else bas
        rows_n, info_n = evaluate(bas_n, cP_n[None], torch.tensor([a0_n], dtype=DT, device=device), beta_n, w)
        obj_n = float((rows_n[0] ** 2).sum())
        if bool(info_n['fail'].any()) or not math.isfinite(obj_n):
            log(f'#   trial rejected: {int(info_n["fail"].sum())} failed trajectories / nonfinite objective'); lam_rel *= 10; continue
        if obj_n < obj:
            accepted = True
            x_prev = xcur.clone(); rows_prev = rows0[0].clone()
            cP, a0, beta, bas = cP_n, a0_n, beta_n, bas_n
            rows0, info0 = rows_n, info_n; obj = obj_n
            lam_rel = max(lam_rel / 3, 1e-9)
            break
        lam_rel *= 10
    summ = summarize(info0, w)
    rec = dict(it=it, obj=obj, a0=a0, beta=beta, c=float(info0['c'][0]), h10=float(info0['h10'][0]), h01=float(info0['h01'][0]), **summ,
               smax=smax, smin=smin, s_last5=[float(v) for v in S[-5:]], lam_rel=lam_rel, accepted=accepted, jac=jac_kind, t_jac=tj, dt=time.time() - t0)
    hist.append(rec); log(json.dumps(rec))
    np.savez(args.out + '.npz', cP=cP.cpu().numpy(), a0=a0, beta=beta, L=L, NO=NO, K=K, gamma_P=bas.gamma_P, mu=bas.mu, Nr=args.Nr, Nth=args.Nth, qmax=args.qmax,
             dt=args.dt, rstop=args.rstop, h10_target=h10_target, hist=json.dumps(hist))
    if not accepted:
        if jac_kind == 'broyden':
            J = None; log('# no decrease with the Broyden Jacobian; recomputing the FD Jacobian'); continue
        log('# no decrease found; stopping'); break
    # weights are recomputed from the new g00 only at the start of the next full-Jacobian iteration (frozen objective otherwise)
    if (it + 1) % args.jac_every == 0:
        f10, f01, g00 = jets(beta, a0, float(info0['h10'][0]), float(info0['h01'][0]))
        w_new = proxy_weights(bas, g00)
        if float(((w_new - w).abs() / w).max()) > 1e-3:
            obj_old = obj; w = w_new; rows0, info0 = evaluate(bas, cP[None], torch.tensor([a0], dtype=DT, device=device), beta, w); obj = float((rows0[0] ** 2).sum())
            log(f'# reweighted (g00 {g00:.6f}): objective {obj_old:.6e} -> {obj:.6e} for the same state')
pd = point_diagnostics(bas, cP, a0, beta)
log('# final point diagnostics:')
for p in pd:
    log('#   r=%8.3g phi=%2d: Om/xy basis %+.5f  char %+.5f  (rel diff %.3e)   Thx/xy char %+.5f  Th/y %.5f  T %.2f %s' % (p['r'], p['deg'], p['Om_basis_xy'], p['Om_char_xy'], abs(p['Om_basis_xy'] - p['Om_char_xy']) / (abs(p['Om_char_xy']) + 1e-300), p['Thx_char_xy'], p['Th_char_y'], p['T'], 'FAIL' if p['fail'] else ''))
log('# done')
