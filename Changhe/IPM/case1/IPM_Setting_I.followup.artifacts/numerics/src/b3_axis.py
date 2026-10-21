"""Axis data w = W_1(x,0), w', w'' from a state (analytic derivatives of the modal representation) on a log grid, and B_3 by
the lead researcher's B_3 evaluator (b3_functional/b3infl/b3core.py in the lead researcher's artifacts, which wraps the first run's verifier evaluator vb3ibp.py).
Usage: python3 src/b3_axis.py runs/state.npz [tag]      (or 'x3:N,M,beta' to use the X3 seed projected on that grid)"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '../lead/b3_functional/b3infl')
import numpy as np, torch, ipm_newton as ipn

def axis_w(model, x, xs):
    """w, w', w'' at points xs (numpy) on the x-axis."""
    b, cl = model.unpack(x); cl = float(cl); k = 1.0 / cl; L = model.L
    g = model.geom(torch.tensor(cl, device=model.dev)); fl = model.fields(b, torch.tensor(cl, device=model.dev), g)
    psit = fl['psit_n']; Dq = model.Dqpsi
    psit_q = Dq @ psit; psit_qq = Dq @ psit_q
    nf = model.nf_np
    q = model.q_of_r(xs, cl); th0 = np.zeros_like(xs)
    Ps = model.eval_modes(psit, q, th0, nf, deriv_th=1)        # sum nu psit_nu
    Psq = model.eval_modes(psit_q, q, th0, nf, deriv_th=1)
    Psqq = model.eval_modes(psit_qq, q, th0, nf, deriv_th=1)
    u2 = (xs / L) ** 2; op = 1 + u2
    v = op ** ((k - 1) / 2); vp = (k - 1) * xs / L ** 2 * op ** ((k - 3) / 2)
    vpp = (k - 1) / L ** 2 * op ** ((k - 3) / 2) + (k - 1) * (k - 3) * xs ** 2 / L ** 4 * op ** ((k - 5) / 2)
    qp = (1 - k) * xs / L ** 2 * op ** (-(3 - k) / 2)
    qpp = (1 - k) / L ** 2 * op ** (-(3 - k) / 2) - (1 - k) * (3 - k) * xs ** 2 / L ** 4 * op ** (-(5 - k) / 2)
    f = xs * v * Ps
    fp = v * Ps + xs * vp * Ps + xs * v * Psq * qp
    fpp = 2 * vp * Ps + 2 * v * Psq * qp + xs * vpp * Ps + 2 * xs * vp * Psq * qp + xs * v * Psqq * qp ** 2 + xs * v * Psq * qpp
    w = cl * xs - f; wp = cl - fp; wpp = -fpp
    return w, wp, wpp, cl

def b3_of_state(model, x, verbose=True):
    import b3core
    xs = np.geomspace(7.7e-4, 60.0, 5500)
    w, wp, wpp, cl = axis_w(model, x, xs)
    t0 = time.time()
    Bo, Bi, d = b3core.b3_one(xs, w, wp, wpp, cl, both=True)
    s = b3core.b3_median(xs, w, wp, wpp, cl)
    out = dict(B3_orig=float(Bo), B3_ibp=float(Bi), xstar=float(d['xs']), gstar=float(np.interp(d['xs'], d['x'], d['g'])),
               median_orig=float(s['orig_median']), orig_min=float(s['orig_min']), orig_max=float(s['orig_max']),
               median_ibp=float(s['ibp_median']), ibp_min=float(s['ibp_min']), ibp_max=float(s['ibp_max']), c_l=cl,
               wprime0=float(np.polyfit(xs[xs < 0.05], w[xs < 0.05], 1)[0]), A=2 * cl - 1)
    if verbose:
        print('B_3 one cfg: orig %.5f ibp %.5f; median orig %.5f [%.5f, %.5f] ibp %.5f [%.5f, %.5f]; x* %.7f g* %.5f; w\'(0) %.6f vs -A %.6f (%.1fs)' %
              (Bo, Bi, s['orig_median'], s['orig_min'], s['orig_max'], s['ibp_median'], s['ibp_min'], s['ibp_max'], d['xs'], out['gstar'], out['wprime0'], -(2 * cl - 1), time.time() - t0))
    return out, (xs, w, wp, wpp)

if __name__ == '__main__':
    arg = sys.argv[1]
    if arg.startswith('x3:'):
        import run_newton as rn
        N, M, beta = arg[3:].split(','); model = ipn.Model(int(N), int(M), 8.0, device='cuda', beta=float(beta)); x = rn.seed_from_x3(model)
        tag = sys.argv[2] if len(sys.argv) > 2 else f'x3seed_n{N}m{M}'
    else:
        model, x, d = ipn.load_state(arg); tag = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(arg).replace('.npz', '')
    out, (xs, w, wp, wpp) = b3_of_state(model, x)
    np.savez(f'./runs/axis_{tag}.npz', x=xs, w=w, wp=wp, wpp=wpp, c_l=out['c_l'])
    json.dump(out, open(f'./runs/b3_{tag}.json', 'w'), indent=1)
