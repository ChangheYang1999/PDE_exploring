"""V41(b): stationarity residual of the lead forward state pf_cos2_p05_deep (rho = r^p g, p = 0.5, l = 2):
V.grad rho - rho = r^p [ (l + W_r/r)(p g + g_lr) + (W_th/r) g_th - g ], W from my inverse (code/charsolve.py, as in
tests/v41_m22_state.py, cubic-spline interpolation, 1 and 2 band densities) interpolated back to the lead lr grid; own
derivatives: g_lr by 4th-order central differences, g_th spectral (FFT). Reported per radial band: max|res_g| / max g
and max|res_g| / max(|g|, |p g + g_lr|) (res_g the bracket)."""
import numpy as np, torch, sys, math, json
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from charsolve import CharSolver
dev = 'cuda'; DT = torch.float64
d = np.load('runs/pf_cos2_p05_deep.npz')
g, lr, th = d['g'], d['lr'], d['th']; p = 0.5; l = 1/p; nt = len(th); h = lr[1] - lr[0]
glr = np.full_like(g, np.nan)
glr[2:-2] = (-g[4:] + 8*g[3:-1] - 8*g[1:-3] + g[:-4])/(12*h)
m = np.fft.fftfreq(nt, 1.0/nt); m[nt//2] = 0
gth = np.fft.ifft(1j*m[None]*np.fft.fft(g, axis=1), axis=1).real
for nb in (1, 2):
    L = math.exp(10.0); r1 = 1e-6
    edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12*nb), np.geomspace(0.1, 10, 25*nb)[1:],
                            np.geomspace(10, L, int(round(np.log10(L/10)*5*nb)) + 1)[1:]])
    S = CharSolver(edges, 8, nt, r1, dev)
    rr = S.r.cpu().numpy(); lrr = np.log(np.maximum(rr, 1e-300))
    G = CubicSpline(lr, g, axis=0)(np.clip(lrr, lr[0], lr[-1])); G[lrr < lr[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device=dev)
    W1, W2 = S.velocity(rho, p)
    W1 = W1.cpu().numpy(); W2 = W2.cpu().numpy()
    # back to the lead grid (log-r spline, same angles)
    ok = rr > 0
    W1l = CubicSpline(lrr[ok], W1[ok], axis=0)(lr); W2l = CubicSpline(lrr[ok], W2[ok], axis=0)(lr)
    c, s_ = np.cos(th)[None], np.sin(th)[None]; r = np.exp(lr)[:, None]
    Wr = W1l*c + W2l*s_; Wt = -W1l*s_ + W2l*c
    res = (l + Wr/r)*(p*g + glr) + (Wt/r)*gth - g
    out = dict(bands=nb, rows=[])
    for a_, b_ in ((-11.9, math.log(1e-3)), (math.log(1e-3), 0.0), (0.0, math.log(100.0)), (math.log(100.0), 9.0)):
        k = (lr > a_) & (lr < b_)
        R = np.abs(res[k]); sc1 = np.abs(g[k]).max(); sc2 = np.maximum(np.abs(g[k]), np.abs(p*g[k] + glr[k])).max()
        out['rows'].append(dict(r=[math.exp(a_), math.exp(b_)], max_res=float(np.nanmax(R)), rel_gmax=float(np.nanmax(R)/sc1),
                                rel_scale=float(np.nanmax(R)/sc2), gmax=float(sc1)))
    print(json.dumps(out), flush=True)
# location of the maxima and a finite-difference angular derivative (2nd order) for comparison (last nb)
gth2 = (np.roll(g, -1, 1) - np.roll(g, 1, 1))/(2*(th[1] - th[0]))
res2 = (l + Wr/r)*(p*g + glr) + (Wt/r)*gth2 - g
for a_, b_ in ((-11.9, math.log(1e-3)), (math.log(1e-3), 0.0), (0.0, math.log(100.0))):
    k = np.where((lr > a_) & (lr < b_))[0]
    for name, RR in (('spectral', res), ('fd2', res2)):
        sub = np.abs(RR[k]); i, j = np.unravel_index(np.nanargmax(sub), sub.shape)
        q95 = float(np.nanpercentile(sub, 95))
        print(json.dumps(dict(band=[math.exp(a_), math.exp(b_)], dth=name, max=float(sub[i, j]), r=float(math.exp(lr[k[i]])),
                              th_deg=float(np.degrees(th[j])), g_there=float(g[k[i], j]), p95=q95,
                              gmax=float(np.abs(g[k]).max()))), flush=True)
