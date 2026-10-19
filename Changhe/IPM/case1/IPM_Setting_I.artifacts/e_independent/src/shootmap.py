"""The fixed-c_l characteristics map Phi(b) (see run_shoot2.py) as a function, plus Anderson acceleration."""
import sys, math, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, charac


def phi_map(m, b, cl, dt=0.01, delta=1e-6, info_out=None):
    r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
    fe = charac.FieldEval(m, b, cl)
    Pi = fe.find_P()
    if Pi is None:
        return None
    xs_ = Pi['x_star']
    x_eval, y_tiny = 1e-4, 1e-12
    etaA = charac.eta_P(fe, torch.tensor([x_eval], device=m.dev), torch.tensor([y_tiny], device=m.dev), xs_, C=1.0, dt=dt, delta=delta)[0]
    a0 = (etaA / y_tiny / x_eval ** 2).item()
    X = (r * cos).reshape(-1); Y = (r * sin).reshape(-1); mask = X > 0
    eta = torch.zeros_like(X); eta[mask] = charac.eta_P(fe, X[mask], Y[mask], xs_, C=1.0, dt=dt, delta=delta)[0]
    eta = eta.reshape(m.N + 1, m.M)
    b_eta = eta / (r ** 3 * m.wR[:, None] * cos ** 2 * sin); b_eta[0, :] = a0
    c_eta = m.psi_xy0(m.fields(b_eta)).item()
    C = (3 * cl - 1) / c_eta
    Lsc = math.sqrt(C * a0)
    Xs = X / Lsc; Ys = Y / Lsc
    rho = torch.zeros_like(X); rho[mask] = Lsc * C * charac.eta_P(fe, Xs[mask], Ys[mask], xs_, C=1.0, dt=dt, delta=delta)[0]
    rho = rho.reshape(m.N + 1, m.M)
    bnew = rho / (r ** 3 * m.wR[:, None] * cos ** 2 * sin); bnew[0, :] = 1.0
    if info_out is not None:
        info_out.update(dict(P=Pi, a0=a0, C=C, Lsc=Lsc, c_eta=c_eta, c_new=m.psi_xy0(m.fields(bnew)).item()))
    return bnew


def anderson(m, b, cl, iters=30, mem=6, beta=0.5, dt=0.01, delta=1e-6, log=None, verbose=True):
    """Anderson acceleration (type II) on G(b) = Phi(b) - b with damping beta."""
    n = b.numel()
    Fs, Xs = [], []
    import time
    for it in range(iters):
        t0 = time.time()
        info = {}
        pb = phi_map(m, b, cl, dt=dt, delta=delta, info_out=info)
        if pb is None:
            print("no stagnation point; stop"); return b, False
        g = (pb - b).reshape(-1)
        Fs.append(g.clone()); Xs.append(b.reshape(-1).clone())
        if len(Fs) > mem + 1:
            Fs.pop(0); Xs.pop(0)
        if len(Fs) >= 2:
            dF = torch.stack([Fs[i + 1] - Fs[i] for i in range(len(Fs) - 1)], 1)   # (n, k)
            dX = torch.stack([Xs[i + 1] - Xs[i] for i in range(len(Xs) - 1)], 1)
            # least squares: min |g - dF gamma|
            gam = torch.linalg.lstsq(dF, g.unsqueeze(1), rcond=1e-10).solution.squeeze(1)
            bnew = b.reshape(-1) + beta * g - (dX + beta * dF) @ gam
        else:
            bnew = b.reshape(-1) + beta * g
        bnew = bnew.reshape(m.N + 1, m.M); bnew[0, :] = 1.0
        rel = g.abs().max().item() / b.abs().max().item()
        Pi = info['P']
        msg = (f"it {it:3d}: |Phi(b)-b|/|b|={rel:.3e}  x*={Pi['x_star']:.5f} mu1={Pi['mu1']:.4f} h(P)={Pi['h']:.6f} C={info['C']:.3e} Lsc={info['Lsc']:.4f} "
               f"c_new={info['c_new']:.5f} max b={b.abs().max().item():.4g} min b={b[1:].min().item():.3g} ({time.time()-t0:.0f}s)")
        if verbose: print(msg, flush=True)
        if log is not None:
            log.write(f"{it} {rel:.6e} {Pi['x_star']:.8f} {Pi['mu1']:.6f} {Pi['h']:.8f} {info['C']:.6e} {info['Lsc']:.6f} {b.abs().max().item():.6e}\n"); log.flush()
        b = bnew
        if rel < 1e-9:
            return b, True
    return b, False
