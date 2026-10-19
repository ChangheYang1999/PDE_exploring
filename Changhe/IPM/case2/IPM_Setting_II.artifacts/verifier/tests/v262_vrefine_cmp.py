"""V262: test of numerical record R21(d) (the 1e-5 outer floor of V255 is the radial discretisation error of the solver's
velocity routine) by a three-way comparison on the 512-angle base state.
W0 = solver routine (numerics code/pfwd.py PFwd.velocity, the object under test, called read-only) on the state grid
(721 rows, dlr = 1/30); W2 = the same routine on the grid with dlr = 1/60 (quintic spline of rho in log r, every
second row compared); Wm = my class-S law code/charsolve.py (V255 setup: Gauss-Legendre panels, exact radial Green's
function per mode, tail r^p A), at two resolutions (ppu 4 q 8 and ppu 8 q 12).
If W0 has a second-order radial error and Wm is accurate, then Wm - W0 ~ (4/3)(W2 - W0) and |Wm - W2| ~ |Wm - W0|/4.
Also: R = V.grad rho - rho with each velocity, my differentiation (quintic spline in log r, FFT in theta).
Usage: python3 -B tests/v262_vrefine_cmp.py STATE.npz"""
import sys, math, json, time, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import make_interp_spline
sys.path.insert(0, 'code')
from charsolve import CharSolver, lagrange_eval
sys.path.insert(1, 'code')
from pfwd import PFwd
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
g, lr, th = d['g'].astype(float), d['lr'].astype(float), d['th'].astype(float)
p = float(json.loads(str(d['args']))['p']); l = 1.0/p
Nr, nt = g.shape; lo, hi = float(lr[0]), float(lr[-1]); r0 = np.exp(lr); R0 = r0[:, None]
t0 = time.time()
rho_np = R0**p*g
S = PFwd(Nr, nt, lo, hi, p, dev='cuda')
a, b = S.velocity(torch.tensor(rho_np, device='cuda')); Wr0, Wt0 = a.cpu().numpy(), b.cpu().numpy()
del S; torch.cuda.empty_cache()
Nr2 = 2*(Nr - 1) + 1; lr2 = np.linspace(lo, hi, Nr2)
S2 = PFwd(Nr2, nt, lo, hi, p, dev='cuda')
a, b = S2.velocity(torch.tensor(make_interp_spline(lr, rho_np, k=5, axis=0)(lr2), device='cuda'))
Wr2, Wt2 = a.cpu().numpy()[::2], b.cpu().numpy()[::2]
del S2, a, b; torch.cuda.empty_cache()
C, Sn = np.cos(th)[None, :], np.sin(th)[None, :]
def mine(ppu, q):
    P = int(round((hi - lo)*ppu))
    edges = np.concatenate([[0.0], np.exp(np.linspace(lo, hi, P + 1))])
    M = CharSolver(edges, q, nt, math.exp(lo), 'cuda')
    rr = M.r.cpu().numpy(); lrr = np.log(rr)
    G = make_interp_spline(lr, g, k=5, axis=0)(np.clip(lrr, lo, hi)); G[lrr < lo] = 0.0
    W1, W2 = M.velocity(torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda'), p)
    W1, W2 = W1.cpu().numpy(), W2.cpu().numpy()
    xg = np.polynomial.legendre.leggauss(q)[0]; I = np.zeros((Nr, M.Nr))
    for i, x in enumerate(r0):
        k = min(max(np.searchsorted(edges, x, side='right') - 1, 1), len(edges) - 2)
        I[i, k*q:(k + 1)*q] = lagrange_eval(xg, 2*(x - edges[k])/(edges[k + 1] - edges[k]) - 1)
    w1, w2 = I @ W1, I @ W2
    del M; torch.cuda.empty_cache()
    return C*w1 + Sn*w2, -Sn*w1 + C*w2
Wma = mine(4, 8); Wmb = mine(8, 12)
gl = make_interp_spline(lr, g, k=5, axis=0).derivative()(lr)
kk = np.fft.fftfreq(nt, 1.0/nt); kd = 1j*kk; kd[nt//2] = 0.0
gt = np.real(np.fft.ifft(kd[None, :]*np.fft.fft(g, axis=1), axis=1))
def Rn(Wr, Wt): return ((l + Wr/R0)*(p*g + gl) + (Wt/R0)*gt - g)/np.abs(g).max(1, keepdims=True)
mag0 = np.hypot(Wr0, Wt0).max(1, keepdims=True)
def nrm(A, B): return np.hypot(A[0] - B[0], A[1] - B[1])/mag0
W0 = (Wr0, Wt0); W2 = (Wr2, Wt2)
bands = [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -2), (-2, 2), (2, 6), (6, 10.01)]
rows = np.zeros(Nr, bool); rows[3:-3] = True
print('state %s Nr %d nt %d p %.6f; |.| relative to max_ring|W0|, rms over band' % (fn.split('/')[-1], Nr, nt, p))
print('band        |W2-W0|   |Wm-W0|   |Wm-W2|   |Wm-W2|/|Wm-W0|  corr(Wm-W0,W2-W0)  |Wma-Wmb|  |'
      ' R(W0)     R(W2)     R(Wm)     R(Wmb)')
for lo_, hi_ in bands:
    m = rows & (lr >= lo_) & (lr < hi_)
    rms = lambda F: float(np.sqrt((F[m]**2).mean()))
    e20, em0, em2, emm = rms(nrm(W2, W0)), rms(nrm(Wma, W0)), rms(nrm(Wma, W2)), rms(nrm(Wma, Wmb))
    u = np.concatenate([(Wma[0] - Wr0)[m].ravel(), (Wma[1] - Wt0)[m].ravel()])
    v = np.concatenate([(Wr2 - Wr0)[m].ravel(), (Wt2 - Wt0)[m].ravel()])
    corr = float(u @ v/np.linalg.norm(u)/np.linalg.norm(v)); slope = float(u @ v/(v @ v))
    print('[%5.1f,%5.1f) %.2e  %.2e  %.2e  %.3f  %.4f (slope %.3f)  %.2e  | %.2e  %.2e  %.2e  %.2e'
          % (lo_, hi_, e20, em0, em2, em2/em0, corr, slope, emm, rms(Rn(*W0)), rms(Rn(*W2)), rms(Rn(*Wma)), rms(Rn(*Wmb))))
# off-transition table: 8th-order periodic central differences in theta, cells off the weak-axis sectors (10 deg) and
# off the 3-degree windows at 90 / 270 deg (the V255 'rest' set)
c8 = [4/5, -1/5, 4/105, -1/280]; h = 2*math.pi/nt
gt8 = sum(c*(np.roll(g, -j - 1, axis=1) - np.roll(g, j + 1, axis=1)) for j, c in enumerate(c8))/h
def Rn8(Wr, Wt): return ((l + Wr/R0)*(p*g + gl) + (Wt/R0)*gt8 - g)/np.abs(g).max(1, keepdims=True)
thd = np.degrees(th)
near = (np.abs(thd - 90) <= 3) | (np.abs(thd - 270) <= 3)
weak = (np.minimum(np.abs(thd - 0), np.abs(thd - 360)) <= 10) | (np.abs(thd - 180) <= 10)
rest = ~weak & ~near
print('off-transition (fd8 theta, rest set), rms over band:')
print('band          R(W0)     R(W2)     R(Wm)     R(Wmb)    |R(W2)-R(W0)|  |R(Wm)-R(W0)|  |R(Wmb)-R(Wm)|')
A0, A2, Am, Ab = Rn8(*W0), Rn8(*W2), Rn8(*Wma), Rn8(*Wmb)
for lo_, hi_ in bands:
    m = rows & (lr >= lo_) & (lr < hi_)
    rr_ = lambda F: float(np.sqrt((F[m][:, rest]**2).mean()))
    print('[%5.1f,%5.1f) %.2e  %.2e  %.2e  %.2e  %.2e       %.2e       %.2e'
          % (lo_, hi_, rr_(A0), rr_(A2), rr_(Am), rr_(Ab), rr_(A2 - A0), rr_(Am - A0), rr_(Ab - Am)))
# third table: the rest set minus a band around the transition curve y = a x^2 (y > 0, a = 4300, both signs of x),
# |theta - theta_c(r)| < 6 deg, with sin(theta_c) = a r cos(theta_c)^2
u_ = 4300.0*r0; th_c = np.arcsin((np.sqrt(1 + 4*u_**2) - 1)/(2*u_))
tcd = np.degrees(th_c)[:, None]
curve = (np.abs(thd[None, :] - tcd) < 6) | (np.abs(thd[None, :] - (180 - tcd)) < 6)
rest2 = rest[None, :] & ~curve
print('rest set minus 6 deg around y = 4300 x^2 (y > 0); fraction of cells kept per band in the last column')
print('band          R(W0)     R(W2)     R(Wm)     |R(W2)-R(W0)|  |R(Wm)-R(W0)|  kept')
for lo_, hi_ in [(-14, -12), (-12, -11), (-11, -10), (-10, -9), (-9, -8), (-8, -6), (-6, -4), (-4, -2)]:
    m = rows & (lr >= lo_) & (lr < hi_)
    k2 = rest2[m]
    rr_ = lambda F: float(np.sqrt((F[m][k2]**2).mean()))
    print('[%5.1f,%5.1f) %.2e  %.2e  %.2e  %.2e       %.2e       %.2f'
          % (lo_, hi_, rr_(A0), rr_(A2), rr_(Am), rr_(A2 - A0), rr_(Am - A0), k2.mean()))
Wx = (Wr0 + 4/3*(Wr2 - Wr0), Wt0 + 4/3*(Wt2 - Wt0))
print('Richardson-extrapolated solver velocity Wx = W0 + (4/3)(W2 - W0) against my Wm (ppu 8 q 12), rms / max relative to max_ring|W0|')
for lo_, hi_ in bands:
    m = rows & (lr >= lo_) & (lr < hi_)
    e = nrm(Wmb, Wx)[m]
    print('[%5.1f,%5.1f) %.2e  %.2e   (R(Wx) %.2e)' % (lo_, hi_, float(np.sqrt((e**2).mean())), float(e.max()), float(np.sqrt((Rn(*Wx)[m]**2).mean()))))
print('time %.1f s' % (time.time() - t0))
