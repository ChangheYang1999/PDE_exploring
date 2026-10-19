"""Fixed-c_l Picard with characteristics (SPEC Lemma 4), identity and normalisation enforced each step:
   rho_k (identity exact: c[rho_k] = 3c_l-1, a(0)=1)  ->  W_k = c_l X + U[rho_k]  ->  P_k, h_k
   eta = eta_P^delta[W_k] (C=1) on the grid and the axis  ->  C from c[C eta] = 3c_l-1  ->  spatial rescale for a(0)=1
   -> rho_{k+1} = (1-theta) rho_k + theta rho'.
At a fixed point: transport exact outside the delta-box at P, identity, normalisation; h(P) is the shooting output.
"""
import sys, time, argparse, math, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve, charac, diag
ap = argparse.ArgumentParser()
ap.add_argument('--cl', type=float, required=True); ap.add_argument('--start', type=str, default='')
ap.add_argument('--N', type=int, default=48); ap.add_argument('--M', type=int, default=10); ap.add_argument('--L', type=float, default=1.0)
ap.add_argument('--iters', type=int, default=20); ap.add_argument('--theta', type=float, default=1.0)
ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--delta', type=float, default=1e-6); ap.add_argument('--tag', type=str, default='shoot2')
args = ap.parse_args()
dev = 'cuda'; base = ''
cl = args.cl; gamma = 1 / cl
m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=gamma, device=dev)
r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
if args.start:
    m0, b0, cl0, d0 = diag.load(base + args.start, device=dev)
    if (m0.N, m0.M) == (m.N, m.M) and abs(m0.gamma - gamma) < 1e-12 and m0.L == m.L:
        b = b0
    else:
        raise SystemExit("start grid mismatch (same N, M, L, gamma required)")
else:
    s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th if False else r ** 2 / (m.L ** 2 + r ** 2) + 0 * cos
    b = torch.ones_like(s2) + s2   # placeholder shape, amplitude fixed below

def normalise(b):
    """scale amplitude so that c[b] = 3c_l - 1 (c is linear in b); keep b(0)=1 by spatial rescaling afterwards."""
    c = m.psi_xy0(m.fields(b)).item()
    return b * ((3 * cl - 1) / c), c

def rescale_space(rho_fun, L_):
    """rho''(X) = L rho'(X/L): returns b'' on the grid given a callable rho_fun(x, y) for rho'."""
    X = (r * cos).reshape(-1) / L_; Y = (r * sin).reshape(-1) / L_
    mask = X > 0
    rho = torch.zeros_like(X)
    rho[mask] = L_ * rho_fun(X[mask], Y[mask])
    rho = rho.reshape(m.N + 1, m.M)
    bb = rho / (r ** 3 * m.wR[:, None] * cos ** 2 * sin)
    bb[0, :] = 1.0
    return bb

b, c_init = normalise(b)
print(f"start: c before amplitude fix {c_init:.6f} -> set to 3c_l-1 = {3*cl-1:.6f}; b(0) now {b[0,0].item():.6f} (will be fixed by spatial rescale in the loop)", flush=True)
log = open(base + f'runs/{args.tag}.dat', 'w'); log.write("# it c_in x* mu1 h C Lscale a0 maxb minb change time\n")
for it in range(args.iters):
    t0 = time.time()
    fe = charac.FieldEval(m, b, cl)
    Pi = fe.find_P()
    if Pi is None:
        print("no stagnation point; stop"); break
    xs_ = Pi['x_star']
    # axis: a(0) for C=1 (g(x)/x^2 at small x)
    xs_small = torch.tensor([1e-6, 1e-5, 1e-4], device=dev)
    g, _ = charac.axis_g(fe, xs_, xs_small, C=1.0, delta=args.delta)
    a0_vals = (g / xs_small ** 2).cpu().numpy()
    # eta on the grid (C=1) to get c[eta]
    eta_fun = lambda x, y: charac.eta_P(fe, x, y, xs_, C=1.0, dt=args.dt, delta=args.delta)[0]
    X = (r * cos).reshape(-1); Y = (r * sin).reshape(-1); mask = X > 0
    eta = torch.zeros_like(X); eta[mask] = eta_fun(X[mask], Y[mask]); eta = eta.reshape(m.N + 1, m.M)
    b_eta = eta / (r ** 3 * m.wR[:, None] * cos ** 2 * sin); b_eta[0, :] = a0_vals[0]
    c_eta = m.psi_xy0(m.fields(b_eta)).item()
    C = (3 * cl - 1) / c_eta
    # spatial rescale so that a''(0) = C a0 / L^2 = 1
    Lsc = math.sqrt(C * a0_vals[0])
    bnew = rescale_space(lambda x, y: C * eta_fun(x, y), Lsc)
    # sanity: identity and a(0) for bnew
    c_new = m.psi_xy0(m.fields(bnew)).item()
    change = (bnew - b).abs().max().item() / b.abs().max().item()
    b = (1 - args.theta) * b + args.theta * bnew
    msg = (f"it {it:3d}: c_l={cl} x*={xs_:.6f} mu1={Pi['mu1']:.5f} (2cl-1={2*cl-1:.3f}) h(P)={Pi['h']:.6f}  a0(C=1)={a0_vals[0]:.4e} ratio {a0_vals[-1]/a0_vals[0]:.4f}  "
           f"c[eta]={c_eta:.4e} C={C:.4e} Lscale={Lsc:.4f}  c[new]={c_new:.6f} (target {3*cl-1:.4f})  max b'={bnew.abs().max().item():.4g} min b'={bnew[1:].min().item():.4g} b'(inf)max={(m.rad.ext1_R@bnew).abs().max().item():.4g} change={change:.3e} ({time.time()-t0:.0f}s)")
    print(msg, flush=True)
    log.write(f"{it} {c_new:.8f} {xs_:.8f} {Pi['mu1']:.6f} {Pi['h']:.8f} {C:.6e} {Lsc:.6f} {a0_vals[0]:.6e} {bnew.abs().max().item():.6e} {bnew[1:].min().item():.6e} {change:.6e} {time.time()-t0:.1f}\n"); log.flush()
    np.savez(base + f'runs/{args.tag}_last.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=m.N, M=m.M, L=m.L, p=m.p, h=Pi['h'], x_star=xs_)
