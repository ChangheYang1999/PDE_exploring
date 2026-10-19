"""Doubly consistent characteristics Picard: for the current shape b_k choose c_l so that h(P) = 1 (with the amplitude
slaved to the identity c = 3c_l - 1); then transport from P (rho = C eta_P, smooth at 0 and at P), renormalise (identity
and a(0)=1 by spatial rescaling) and evaluate on the grid of the new gamma = 1/c_l."""
import sys, time, argparse, math, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, charac, diag
ap = argparse.ArgumentParser()
ap.add_argument('--start', type=str, default='runs/fixcl_3.0.npz'); ap.add_argument('--iters', type=int, default=20)
ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--delta', type=float, default=1e-6); ap.add_argument('--tag', type=str, default='shoot3')
ap.add_argument('--theta', type=float, default=1.0); ap.add_argument('--clmin', type=float, default=1.05); ap.add_argument('--clmax', type=float, default=12.0)
args = ap.parse_args()
dev = 'cuda'; base = ''
m, b, cl, d = diag.load(base + args.start, device=dev)
N, M, L = m.N, m.M, m.L
log = open(base + f'runs/{args.tag}.dat', 'w'); log.write("# it cl x* mu1 h C Lsc a0 maxb minb binf change time\n")

def h_of_cl(mk, bk, c_bk, cl):
    A = (3 * cl - 1) / c_bk
    fe = charac.FieldEval(mk, A * bk, cl)
    P = fe.find_P()
    return (None if P is None else P['h'] - 1.0), P, fe

for it in range(args.iters):
    t0 = time.time()
    c_b = m.psi_xy0(m.fields(b)).item()
    # bracket the root of h(P)(c_l) - 1 on a grid, then bisection
    grid = np.linspace(args.clmin, args.clmax, 23)
    vals = []
    for c in grid:
        f, P, fe = h_of_cl(m, b, c_b, c)
        vals.append(np.nan if f is None else f)
    vals = np.array(vals)
    roots = [(grid[i], grid[i + 1]) for i in range(len(grid) - 1) if np.isfinite(vals[i]) and np.isfinite(vals[i + 1]) and vals[i] * vals[i + 1] < 0]
    print(f"it {it}: h(P)-1 on the c_l grid: " + " ".join(f"{c:.2f}:{v:+.3f}" for c, v in zip(grid, vals)), flush=True)
    if not roots:
        print("  no root of h(P) = 1 in the c_l range for this shape; stop", flush=True); break
    a_, b_ = roots[0]
    fa = h_of_cl(m, b, c_b, a_)[0]
    for _ in range(50):
        mid = 0.5 * (a_ + b_); fm = h_of_cl(m, b, c_b, mid)[0]
        if fm is None: break
        if fa * fm <= 0: b_ = mid
        else: a_, fa = mid, fm
    cl_new = 0.5 * (a_ + b_)
    f, P, fe = h_of_cl(m, b, c_b, cl_new)
    xs_ = P['x_star']
    # new model for gamma = 1/cl_new; transport eta (C=1) onto its grid
    m2 = ipm1.IPM1(N=N, M=M, L=L, gamma=1 / cl_new, device=dev)
    r = m2.rad.rR[:, None]; cos = m2.ang.cos[None, :]; sin = m2.ang.sin[None, :]
    X = (r * cos).reshape(-1); Y = (r * sin).reshape(-1); mask = X > 0
    x_eval, y_tiny = 1e-4, 1e-12
    etaA = charac.eta_P(fe, torch.tensor([x_eval], device=dev), torch.tensor([y_tiny], device=dev), xs_, C=1.0, dt=args.dt, delta=args.delta)[0]
    a0 = (etaA / y_tiny / x_eval ** 2).item()
    eta = torch.zeros_like(X); eta[mask] = charac.eta_P(fe, X[mask], Y[mask], xs_, C=1.0, dt=args.dt, delta=args.delta)[0]
    eta = eta.reshape(N + 1, M)
    b_eta = eta / (r ** 3 * m2.wR[:, None] * cos ** 2 * sin); b_eta[0, :] = a0
    c_eta = m2.psi_xy0(m2.fields(b_eta)).item()
    C = (3 * cl_new - 1) / c_eta
    Lsc = math.sqrt(C * a0)
    rho = torch.zeros_like(X); rho[mask] = Lsc * C * charac.eta_P(fe, X[mask] / Lsc, Y[mask] / Lsc, xs_, C=1.0, dt=args.dt, delta=args.delta)[0]
    rho = rho.reshape(N + 1, M)
    bnew = rho / (r ** 3 * m2.wR[:, None] * cos ** 2 * sin); bnew[0, :] = 1.0
    c_new = m2.psi_xy0(m2.fields(bnew)).item()
    # change measure: compare on the same t-grid (values of b as functions of t)
    change = (bnew - b).abs().max().item() / b.abs().max().item()
    print(f"  -> c_l={cl_new:.8f} x*={xs_:.6f} (rescaled x*={xs_*Lsc:.6f}) mu1={P['mu1']:.6f} (2cl-1={2*cl_new-1:.6f}) h(P)-1={f:+.2e}  a0(C=1)={a0:.4e} C={C:.4e} Lsc={Lsc:.4f}  "
          f"c[new]={c_new:.6f} (target {3*cl_new-1:.6f}) max b={bnew.abs().max().item():.4g} min b={bnew[1:].min().item():.4g} b(inf)max={(m2.rad.ext1_R@bnew).abs().max().item():.4g} change={change:.3e} ({time.time()-t0:.0f}s)", flush=True)
    log.write(f"{it} {cl_new:.10f} {xs_:.8f} {P['mu1']:.6f} {P['h']:.8f} {C:.6e} {Lsc:.6f} {a0:.6e} {bnew.abs().max().item():.6e} {bnew[1:].min().item():.6e} {(m2.rad.ext1_R@bnew).abs().max().item():.6e} {change:.6e} {time.time()-t0:.1f}\n"); log.flush()
    if args.theta != 1.0:
        # mix in physical space: evaluate the old b (function of r, theta on grid m) at the radii of the new grid m2
        fe_old = charac.FieldEval(m, b, cl)
        t_old = fe_old.t_of_r(m2.rad.rR[1:])
        Pm = fe_old.radial_interp_matrix(t_old)
        b_old_on_new = torch.ones_like(bnew); b_old_on_new[1:] = Pm @ b
        # b = a / w with w depending on gamma: convert the old b to the new weight
        w_old_on_new = (1 + m2.rad.rR[1:] ** 2 / L ** 2) ** ((m.gamma - 3) / 2); w_new = m2.wR[1:]
        b_old_on_new[1:] = b_old_on_new[1:] * (w_old_on_new / w_new)[:, None]
        b = (1 - args.theta) * b_old_on_new + args.theta * bnew
        b[0, :] = 1.0
    else:
        b = bnew
    m = m2; cl = cl_new
    np.savez(base + f'runs/{args.tag}_it{it}.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=N, M=M, L=L, p=m.p, x_star=xs_ * Lsc, mu1=P['mu1'], h=P['h'])
