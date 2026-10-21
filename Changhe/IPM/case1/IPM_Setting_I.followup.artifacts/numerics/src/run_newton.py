"""Driver: Newton solve on a given grid from a seed, then diagnostics and the smallest singular values of the Jacobian.
Usage:
  python3 src/run_newton.py --N 120 --M 32 --L 8 --seed x3 --tag n120m32L8 [--maxit 12] [--nsv 8] [--fixcl] [--cl 5.5753626]
  --seed x3            : initial guess from the published candidate X3 (data/c6g_shape.npz) through the first run's evaluator
  --seed runs/foo.npz  : initial guess interpolated from a saved state (any grid / L)
Outputs: runs/<tag>.npz (state), runs/<tag>.log, runs/<tag>_diag.json.
"""
import sys, os, time, json, argparse, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch
import ipm_newton as ipn

LANE = '.'


def seed_from_x3(model, cl=None, shape=LANE + '/data/c6g_shape.npz'):
    import rayshape_firstrun as rs
    P = rs.load_shape(shape)
    if cl is None: cl = P['c_l']
    ev = rs.ShapeEval(P, model.dev)
    r, w, v = model.radii(cl)
    k = 1.0 / cl
    rr = r.copy(); rr[-1] = 1e100
    R, TH = np.meshgrid(rr, model.ang.theta_np, indexing='ij')
    Rt = torch.tensor(R.ravel(), device=model.dev); Tt = torch.tensor(TH.ravel(), device=model.dev)
    H, _, _ = ev._H(Rt, Tt)
    # b = rho/(r^3 w Pi) = e^H / w,  w = (1 + (r/L)^2)^((k-3)/2)  ->  log b = H + (3-k)/2 log(1 + (r/L)^2)
    logb = H + (3.0 - k) / 2.0 * torch.log1p((Rt / model.L) ** 2)
    b = torch.exp(logb).reshape(model.N + 1, model.M)
    b[0, :] = 1.0
    return model.pack(b, cl)


def axis_data(model, x, nx=4000, xmax=None):
    """W_1(x, 0), h(x) = d_y W_2(x, 0), g(x) = rho_y(x, 0) on a fine x-grid (numpy)."""
    b, cl = model.unpack(x); cl = float(cl); k = 1.0 / cl
    g = model.geom(torch.tensor(cl, device=model.dev)); fl = model.fields(b, torch.tensor(cl, device=model.dev), g)
    psit_n = fl['psit_n'].cpu().numpy(); psit_nq = fl['psit_nq'].cpu().numpy()
    nf = model.nf_np
    if xmax is None: xmax = 4 * model.L
    xs = np.linspace(1e-3, xmax, nx)
    qs = model.q_of_r(xs, cl); th0 = np.zeros_like(xs)
    vv = (1.0 + (xs / model.L) ** 2) ** ((k - 1) / 2)
    omP1 = (xs / model.L) ** 2 / (1 + (xs / model.L) ** 2); S = (1 - k) * (1 - qs) * omP1; ov = (k - 1) * omP1
    ps_th = model.eval_modes(psit_n, qs, th0, nf, deriv_th=1)
    psq_th = model.eval_modes(psit_nq, qs, th0, nf, deriv_th=1)
    U1 = -(xs * vv) * ps_th                               # U_1(x,0) = -(r v) psit_theta
    w_ax = cl * xs + U1
    h_ax = cl + vv * ((1.0 + ov) * ps_th + S * psq_th)    # d_y W_2 (x, 0)
    # g = rho_y(x,0) = x^2 a(x,0) = x^2 w(r) b(q, 0)
    ww = (1.0 + (xs / model.L) ** 2) ** ((k - 3) / 2)
    b0 = model.eval_EE(b, qs, th0)
    g_ax = xs ** 2 * ww * b0
    return xs, w_ax, h_ax, g_ax


def stagnation(model, x):
    xs, w_ax, h_ax, g_ax = axis_data(model, x)
    b, cl = model.unpack(x); cl = float(cl)
    i = np.where((w_ax[:-1] < 0) & (w_ax[1:] >= 0))[0]
    if len(i) == 0: return dict(xstar=None)
    i = i[0]
    # refine by secant on the fine grid, then interpolate h
    from scipy.interpolate import CubicSpline
    sel = slice(max(i - 6, 0), min(i + 8, len(xs)))
    cs = CubicSpline(xs[sel], w_ax[sel]); roots = [r for r in cs.roots() if xs[sel][0] <= r <= xs[sel][-1]]
    xstar = float(roots[0]) if roots else float(xs[i])
    hP = float(CubicSpline(xs[sel], h_ax[sel])(xstar)); gP = float(CubicSpline(xs[sel], g_ax[sel])(xstar))
    wpP = float(cs(xstar, 1))
    nzero = int(np.sum(np.sign(w_ax[:-1]) != np.sign(w_ax[1:])))
    return dict(xstar=xstar, hP=hP, hP_minus_1=hP - 1.0, gP=gP, wprimeP=wpP, wprimeP_minus_A=wpP - (2 * cl - 1),
                n_axis_zeros=nzero, min_g_on_0_xstar=float(g_ax[xs < xstar].min()))


def smallest_singular(J, nsv=8, full_limit=26000):
    n = J.shape[0]
    if n <= full_limit:
        t0 = time.time(); s = torch.linalg.svdvals(J); t1 = time.time()
        s = s.cpu().numpy()
        return dict(method='svdvals', smax=float(s[0]), smin=[float(v) for v in s[-nsv:][::-1]], time=t1 - t0)
    # block inverse iteration on J^T J using the LU of J
    t0 = time.time()
    LU = torch.linalg.lu_factor(J)
    V = torch.randn(n, nsv, device=J.device)
    for it in range(30):
        Y = torch.linalg.lu_solve(*LU, V, adjoint=True)       # J^-T V
        Z = torch.linalg.lu_solve(*LU, Y)                     # J^-1 J^-T V = (J^T J)^-1 V
        V, _ = torch.linalg.qr(Z)
    # Rayleigh-Ritz: singular values of J V
    JV = J @ V
    s = torch.linalg.svdvals(JV).cpu().numpy()
    smax = torch.linalg.matrix_norm(J, ord=2).item() if n <= 40000 else float('nan')
    return dict(method='inverse_iteration', smax=smax, smin=[float(v) for v in s[::-1]], time=time.time() - t0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, required=True); ap.add_argument('--M', type=int, required=True)
    ap.add_argument('--L', type=float, default=8.0); ap.add_argument('--seed', default='x3'); ap.add_argument('--tag', required=True)
    ap.add_argument('--maxit', type=int, default=12); ap.add_argument('--nsv', type=int, default=8)
    ap.add_argument('--fixcl', action='store_true'); ap.add_argument('--cl', type=float, default=None)
    ap.add_argument('--batch', type=int, default=256); ap.add_argument('--nosvd', action='store_true')
    ap.add_argument('--lm', action='store_true'); ap.add_argument('--Delta', type=float, default=0.05);
    ap.add_argument('--device', default='cuda'); ap.add_argument('--beta', type=float, default=0.0); ap.add_argument('--nmodes', type=int, default=None)
    a = ap.parse_args()
    os.makedirs(LANE + '/runs', exist_ok=True)
    log = open(f'{LANE}/runs/{a.tag}.log', 'a')
    def P(*s):
        msg = ' '.join(str(v) for v in s); print(msg, flush=True); log.write(msg + '\n'); log.flush()
    P(f'# run_newton {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} args {vars(a)}')
    t0 = time.time()
    model = ipn.Model(a.N, a.M, a.L, device=a.device, beta=a.beta, nmodes=a.nmodes)
    if a.seed == 'x3':
        x = seed_from_x3(model, cl=a.cl)
    else:
        m0, x0, d0 = ipn.load_state(a.seed, device=a.device)
        x = ipn.project_state(m0, x0, model)
        if a.cl is not None: x[-1] = a.cl
    P(f'grid N={a.N} M={a.M} L={a.L} beta={a.beta} nmodes={model.nmodes} Mq={model.Mq}: n = {a.N*a.M+1} unknowns; seed {a.seed}; setup {time.time()-t0:.1f}s')
    r, w, v = model.radii(float(x[-1]))
    P(f'radii: r_1 = {r[1]:.4g}, r_2 = {r[2]:.4g}, r_(N-1) = {r[-2]:.4g}; nodes with r < 1: {np.sum(r < 1)}, r < 10: {np.sum(r < 10)}, r < 100: {np.sum(r < 100)}')
    F0 = model.F(x)
    P(f'seed residual |F|_inf {F0.abs().max().item():.3e}  |F|_2 {F0.norm().item():.3e}  identity row {F0[-1].item():.3e}')
    if a.lm:
        x, hist = model.newton_lm(x, maxit=a.maxit, log=log, fix_cl=a.fixcl, batch=a.batch, Delta=a.Delta)
    else:
        x, hist = model.newton(x, maxit=a.maxit, log=log, fix_cl=a.fixcl, batch=a.batch)
    F1 = model.F(x)
    b, cl = model.unpack(x)
    diag = dict(N=a.N, M=a.M, L=a.L, beta=a.beta, nmodes=model.nmodes, n=a.N * a.M + 1, seed=a.seed, fixcl=a.fixcl, c_l=float(cl),
                F_inf=float(F1.abs().max()), F_2=float(F1.norm()), identity=float(F1[-1]), hist=hist,
                b_min=float(b.min()), b_max=float(b.max()), b_far_min=float(b[-1].min()), b_far_max=float(b[-1].max()))
    P(f'converged: c_l = {float(cl):.10f}  |F|_inf {diag["F_inf"]:.3e}  identity {diag["identity"]:.3e}  b range [{diag["b_min"]:.4g}, {diag["b_max"]:.4g}]')
    st = stagnation(model, x); diag.update(st)
    P(f'stagnation: {json.dumps(st)}')
    ipn.save_state(f'{LANE}/runs/{a.tag}.npz', model, x, extra=dict(tag=a.tag))
    if not a.nosvd:
        J = model.jacobian(x, batch=a.batch)
        sv = smallest_singular(J, nsv=a.nsv); diag['sv'] = sv
        P(f'singular values ({sv["method"]}, {sv["time"]:.1f}s): smax {sv["smax"]:.4e}; smallest {" ".join("%.4e" % s for s in sv["smin"])}')
        # the c_l component and the energy distribution of the smallest right singular vector (inverse iteration)
        LU = torch.linalg.lu_factor(J)
        vv = torch.randn(J.shape[0], 1, device=J.device)
        for it in range(40):
            y = torch.linalg.lu_solve(*LU, vv, adjoint=True); z = torch.linalg.lu_solve(*LU, y); vv = z / z.norm()
        sig = (J @ vv).norm().item()
        vb = vv[:-1, 0].reshape(a.N, a.M).cpu().numpy(); vcl = vv[-1, 0].item()
        rr = r[1:]
        en = vb ** 2
        bands = {'r<1': float(en[rr < 1].sum()), '1-10': float(en[(rr >= 1) & (rr < 10)].sum()), '10-100': float(en[(rr >= 10) & (rr < 100)].sum()),
                 '100-1e4': float(en[(rr >= 100) & (rr < 1e4)].sum()), '>1e4': float(en[rr >= 1e4].sum())}
        th = model.ang.theta_np * 180 / np.pi
        abands = {'0-10deg': float(en[:, th < 10].sum()), '10-80': float(en[:, (th >= 10) & (th < 80)].sum()), '80-90': float(en[:, th >= 80].sum())}
        diag['vmin'] = dict(sigma=sig, cl_component=vcl, radial_energy=bands, angular_energy=abands)
        P(f'smallest right singular vector: sigma {sig:.4e}, c_l component {vcl:.4e}, radial energy {json.dumps(bands)}, angular {json.dumps(abands)}')
        del J, LU
    json.dump(diag, open(f'{LANE}/runs/{a.tag}_diag.json', 'w'), indent=1)
    P(f'done in {time.time()-t0:.1f}s')


if __name__ == '__main__':
    main()
