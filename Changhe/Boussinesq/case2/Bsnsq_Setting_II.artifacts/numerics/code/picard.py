"""Forward (characteristics) fixed-point solver for Setting A2, beta > 2.  Second method, independent of the
collocation least squares: the velocity is represented by the smooth-part coefficients cG of G = Omega/(xy) in the
t-basis (only used for the Biot-Savart inverse and for evaluating W); Theta and Omega are computed by transport from
the source P = (x*,0) with local Taylor data (forward.py), with NO far-field assumption. Parameters (beta, g*) are
fixed at each step by the two necessary conditions c = Psi_xy(0) = 2 beta + 2 and lambda = W1'(x*,0) = beta + 2 for the
velocity of the current shape. Iteration: Omega_new = transport(W[cG]) -> fit -> cG_new; damped Picard.
The fixed-point defect is measured with the LM residual (same metric as the collocation runs).
"""
import sys, time, json, math, numpy as np, torch
sys.path.insert(0, 'code')
from a2core import DT
from lm_solve import LMProblem, load_state, problem_from_state, fit_fields, dev, make_model, rad_of_r, save_state
from charcheck import evalW
from forward import transport_from_source, local_solution
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq, fsolve


def build_from_coeffs(prob, cG, beta, rmin=1e-3, rmax=1e6, nr=3000):
    """evaluator dict B for charcheck.evalW using only the velocity (ca = 0) of coefficients cG, transport beta.
    The fine-grid model (Green matrices at nr radii) is cached on prob and reused across iterations."""
    m0 = prob.model
    rg = np.geomspace(rmin, rmax, nr); M = prob.M
    th = (np.arange(M) + 0.5) * np.pi / (2 * M)
    key = (rmin, rmax, nr)
    if getattr(prob, '_fine_key', None) != key:
        rad = rad_of_r(m0, prob.mapname, rg)
        t0 = time.time()
        prob._fine_model = make_model(prob.mapname, prob.N, prob.M, prob.L, prob.beta_map, prob.sigma_a, prob.sigma_G, rad, th)
        prob._fine_key = key
        print(f"  [fine-grid model built in {time.time()-t0:.0f}s]", flush=True)
    m = prob._fine_model
    ca = torch.zeros((M, prob.N), dtype=DT, device=dev)
    f = m.fields(ca, cG, beta)
    h = f['h'].cpu().numpy(); hd = f['hd'].cpu().numpy(); u = np.log(rg)
    C = np.cos(np.outer(th, 2 * np.arange(M)))
    gamma = np.linalg.solve(C, f['G'].cpu().numpy().T)
    S = dict(h=[CubicSpline(u, h[l]) for l in range(M)], hd=[CubicSpline(u, hd[l]) for l in range(M)],
             alpha=[CubicSpline(u, 0 * u) for l in range(M)], gamma=[CubicSpline(u, gamma[l]) for l in range(M)])
    return dict(S=S, M=M, beta=beta, rmin=rmin, rmax=rmax, c=float(f['c']))


def xstar_lambda(B):
    w1 = lambda x: evalW(B, np.array([x]), np.array([1e-12]))['W1'][0] / x
    xs = np.geomspace(0.05, 2000, 600); v = np.array([w1(x) for x in xs])
    i = np.where(np.diff(np.sign(v)) != 0)[0]
    if len(i) == 0: return None, None
    x0 = brentq(w1, xs[i[0]], xs[i[0] + 1], xtol=1e-13)
    d = 1e-6 * x0
    lam = (evalW(B, np.array([x0 + d]), np.array([1e-12]))['W1'][0] - evalW(B, np.array([x0 - d]), np.array([1e-12]))['W1'][0]) / (2 * d)
    return x0, lam


def solve_params(prob, cG_shape, beta0, g0):
    """Given the shape cG_shape (velocity of Omega/g*), find (beta, g*) with c = 2beta+2 and lambda = beta+2.
    W = beta X + g* U_shape;  c = g* c_shape  =>  beta(g) = (g c_shape - 2)/2;  then solve the scalar equation
    F2(g) = g dU1_shape/dx(x*) - 2 = 0 by bracketing, where x*(g) is the first zero of beta(g) + g U1_shape(x,0)/x."""
    B1 = build_from_coeffs(prob, cG_shape, 1.0)
    c_shape = B1['c']
    B0 = dict(B1, beta=0.0)
    xgrid = np.geomspace(0.05, 5000, 400)
    U1x = np.array([evalW(B0, np.array([x]), np.array([1e-12]))['W1'][0] / x for x in xgrid])   # U1_shape/x on the axis
    def xstar_of(beta, g):
        v = beta + g * U1x
        i = np.where(np.diff(np.sign(v)) != 0)[0]
        if len(i) == 0: return None
        f = lambda x: beta + g * evalW(B0, np.array([x]), np.array([1e-12]))['W1'][0] / x
        return brentq(f, xgrid[i[0]], xgrid[i[0] + 1], xtol=1e-12)
    def dU1(x, g):
        d = 1e-6 * x
        return g * (evalW(B0, np.array([x + d]), np.array([1e-12]))['W1'][0] - evalW(B0, np.array([x - d]), np.array([1e-12]))['W1'][0]) / (2 * d)
    def F2(g):
        beta = (g * c_shape - 2) / 2
        if beta <= 2.0: return np.nan
        x0 = xstar_of(beta, g)
        if x0 is None: return np.nan
        return dU1(x0, g) - 2.0
    gs = np.geomspace(g0 / 20, g0 * 20, 120)
    vals = np.array([F2(g) for g in gs])
    ok = np.isfinite(vals)
    roots = []
    for i in range(len(gs) - 1):
        if ok[i] and ok[i + 1] and vals[i] * vals[i + 1] < 0:
            roots.append(brentq(F2, gs[i], gs[i + 1], xtol=1e-10))
    if not roots:
        return beta0, g0, [np.nan, np.nan], c_shape
    # choose the root closest to g0
    g = min(roots, key=lambda r: abs(np.log(r / g0)))
    beta = (g * c_shape - 2) / 2
    return float(beta), float(g), [float(g * c_shape - 2 * beta - 2), float(F2(g))], c_shape


def picard(prob, cG, beta, iters=20, damp=0.5, eps_frac=0.01, order=3, log=None, name='picard', max_steps=4000, r_fit_frac=30.0):
    """Damped Picard iteration on the vorticity coefficients cG (full amplitude).
    Each step: (beta, g) from the two conditions for the shape cG (velocity amplitude g, c = 2beta+2, lambda = beta+2);
    transport with unit source amplitude; Theta amplitude from a_0 = 1; fit; defect = LM residual of the fit."""
    hist = []
    for it in range(iters):
        t0 = time.time()
        beta_n, g, Fcond, c_shape = solve_params(prob, cG, beta, 1.0)
        if not (np.all(np.isfinite(Fcond)) and 2.05 < beta_n < 12 and 0.02 < g < 50):
            print(f"it {it}: parameter solve failed (beta={beta_n}, g={g}, res={Fcond}); stopping", flush=True); break
        cG = g * cG; beta = beta_n
        if abs(beta - prob.beta_map) > 0.05:
            prob = LMProblem(prob.N, prob.M, prob.L, beta, None, None, prob.a0_target, prob.w_origin, None, ov=prob.Ne / prob.N, mapname=prob.mapname, Rw=prob.Rw)
        B = build_from_coeffs(prob, cG, beta)
        xs, lam = xstar_lambda(B)
        m = prob.model
        R, TH = np.meshgrid(m.r, m.th, indexing='ij'); X, Y = R * np.cos(TH), R * np.sin(TH)
        sel = (R <= r_fit_frac * xs)
        targets = np.stack([X[sel], Y[sel]], 1)
        loc = local_solution(B, xs, 1.0, order)
        res = transport_from_source(B, xs, 1.0, targets, eps=eps_frac * xs, order=order, loc=loc, max_steps=max_steps)
        rr_t = np.hypot(targets[:, 0], targets[:, 1])
        s_ok = res['s'] < 2.0 * (np.log(np.maximum(rr_t, xs) / xs) / beta + np.log(1.0 / eps_frac) / max(lam, 1e-3)) + 2.0
        fin = np.zeros(R.shape, bool); fin[sel] = res['finished'] & s_ok
        Theta = np.zeros(R.shape); Omega = np.zeros(R.shape); Theta[sel] = res['Theta']; Omega[sel] = res['Omega']
        a1 = np.where(fin, Theta / (X ** 2 * Y), 0.0); G1 = np.where(fin, Omega / (X * Y), 0.0)
        r_unf = R[sel & ~fin]
        r_fit_eff = min(r_fit_frac * xs, 0.8 * r_unf.min()) if r_unf.size else r_fit_frac * xs
        # Theta amplitude from a_0 = 1: a_0 of the unit-amplitude transported field
        z1 = fit_fields(prob, a1, G1, m.r, m.th, beta, r_fit=r_fit_eff, mask=fin)
        ca1, cG1, _ = prob.unpack(z1); a0_1 = float(m.fields(ca1, cG1, beta)['a0'])
        gstar = 1.0 / a0_1
        ca_new, cG_new = gstar * ca1, gstar * cG1
        z_new = prob.pack(ca_new, cG_new, beta)
        d = prob.diagnostics(z_new)
        f_new = m.fields(ca_new, cG_new, beta)
        upd = dict(it=it, xs=xs, lam=lam, lam_over=lam / (beta + 2), beta=beta, g_vel=g, gstar=gstar, c_shape_vel=B['c'],
                   c_new=float(f_new['c']), Fnorm=d['Fnorm'], Ra_max=d['Ra_max'], RG_max=d['RG_max'], a0=d['a0'], G0=d['G0'],
                   unfinished=float((~fin[sel]).mean()), r_fit_eff=r_fit_eff, dcG=float((cG_new - cG).norm() / cG.norm()), t=time.time() - t0)
        hist.append(upd)
        msg = (f"it {it:2d} beta={beta:.5f} g_vel={g:.4f} x*={xs:.4f} lam/(b+2)={upd['lam_over']:.5f} c_vel={B['c']:.4f} | transported: g*={gstar:.4f} "
               f"c_new={upd['c_new']:.4f} |F|={d['Fnorm']:.3e} Ra={d['Ra_max']:.2e} RG={d['RG_max']:.2e} G0={d['G0']:.4f} unfin={upd['unfinished']:.3f} r_fit={r_fit_eff:.1f} dcG={upd['dcG']:.2e} t={upd['t']:.0f}s")
        print(msg, flush=True)
        if log: log.write(msg + "\n"); log.flush()
        save_state(f'runs/{name}.npz', prob, z_new, hist)
        cG = (1 - damp) * cG + damp * cG_new
    return prob, cG, beta, hist


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--init', type=str, required=True); ap.add_argument('--iters', type=int, default=10)
    ap.add_argument('--damp', type=float, default=0.5); ap.add_argument('--name', type=str, default='P1')
    ap.add_argument('--eps_frac', type=float, default=0.01); ap.add_argument('--order', type=int, default=3)
    ap.add_argument('--r_fit_frac', type=float, default=30.0)
    args = ap.parse_args()
    d = load_state(args.init); prob, z = problem_from_state(d)
    ca, cG, beta = prob.unpack(z); beta = float(beta)
    log = open(f'runs/{args.name}.log', 'a')
    prob, cG, beta, hist = picard(prob, cG, beta, iters=args.iters, damp=args.damp, eps_frac=args.eps_frac, order=args.order, log=log, name=args.name, r_fit_frac=args.r_fit_frac)
