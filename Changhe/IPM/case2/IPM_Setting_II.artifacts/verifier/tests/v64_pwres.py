"""V64g: pointwise residual of the stationary equation, independent of the characteristic map T.
With rho = r^p g, t = log r, alpha = V_r/r, beta = V_th/r:  V.grad rho = rho  <=>  R := alpha g_t + beta g_th + (alpha p - 1) g = 0.
g_t: per-panel Gauss-Lagrange differentiation; g_th: FFT (Nyquist dropped for the first derivative). alpha, beta: own velocity
of the state (code/fwdstat.py). Ring-wise relative residual max_th |R| / max_th (|alpha g_t| + |beta g_th| + |alpha p - 1||g|),
reported as the max over the rings in each t band, with the angle of the worst point.  Usage: python3 tests/v64_pwres.py STATE.npz ..."""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
from charsolve import lagrange_diff
DT = torch.float64
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)),
                ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
    rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
    al, be, _, _ = F.fields(rho); al = al.cpu().numpy(); be = be.cpu().numpy()
    r = F.r.cpu().numpy(); g = d['rho']/r[:, None]**p; q = F.q; P = len(r)//q; edges = F.S.edges
    Dg = lagrange_diff(np.polynomial.legendre.leggauss(q)[0]); gr = np.zeros_like(g)
    for k in range(P):
        sl = slice(k*q, (k + 1)*q); gr[sl] = Dg @ g[sl]/((edges[k + 1] - edges[k])/2)
    gt = r[:, None]*gr
    mm = np.fft.fftfreq(nt, 1.0/nt); mm[nt//2] = 0.0
    gth = np.real(np.fft.ifft(1j*mm*np.fft.fft(g, axis=1), axis=1))
    R = al*gt + be*gth + (al*p - 1)*g
    sc = np.abs(al*gt) + np.abs(be*gth) + np.abs(al*p - 1)*np.abs(g)
    rel = np.abs(R).max(1)/sc.max(1); t = np.log(r); th = np.degrees(F.th.cpu().numpy())
    out = dict(state=fn.split('/')[-1], nt=nt, p=p); b = {}
    for a_, b_ in ((-13, -12), (-12, -11), (-11, -10), (-10, -9), (-9, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 8), (8, 10)):
        m = (t >= a_) & (t < b_)
        if not m.any():
            continue
        i = np.where(m)[0][np.argmax(rel[m])]
        b['%g..%g' % (a_, b_)] = dict(max_rel=float('%.3g' % rel[i]), at_t=round(float(t[i]), 2),
                                      at_deg=round(float(th[np.argmax(np.abs(R[i]))]), 1))
    out['ringwise_rel_residual'] = b
    print(json.dumps(out), flush=True)
