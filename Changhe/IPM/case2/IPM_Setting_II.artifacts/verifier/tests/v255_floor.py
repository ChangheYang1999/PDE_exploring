"""V255 diagnostic: localize the outer-region floor of the directly evaluated R (my evaluator) on an R20 base state.
Variants: base (grid to log r = 10, tail r^p A beyond); ext (my grid to log r = EXT with g held at its last value, i.e.
the same tail made explicit); notail (rho cut at log r = 10, no tail; shows the size of the tail contribution);
k7 (degree-7 splines). Prints rms of R / max_ring|rho| in half-unit bands from log r = -3 and the largest angular modes."""
import sys, math, json, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import make_interp_spline
sys.path.insert(0, 'code')
from charsolve import CharSolver, lagrange_eval
DT = torch.float64
fn = sys.argv[1]; var = sys.argv[2]; d = np.load(fn, allow_pickle=True)
g, lr, th = d['g'].astype(float), d['lr'].astype(float), d['th'].astype(float)
p = float(json.loads(str(d['args']))['p']); l = 1.0/p; nt = len(th)
k = 7 if var == 'k7' else 5
tmin, tmax = float(lr[0]), float(lr[-1]); ppu, q = 4, 8
tm2 = 14.0 if var == 'ext' else tmax
P = int(round((tm2 - tmin)*ppu))
edges = np.concatenate([[0.0], np.exp(np.linspace(tmin, tm2, P + 1))])
S = CharSolver(edges, q, nt, math.exp(tmin), 'cuda')
rr = S.r.cpu().numpy(); lrr = np.log(rr)
G = make_interp_spline(lr, g, k=k, axis=0)(np.clip(lrr, tmin, tmax)); G[lrr < tmin] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
if var == 'notail':
    S.tail_modes = []
W1, W2 = [w.cpu().numpy() for w in S.velocity(rho, p)]
xg = np.polynomial.legendre.leggauss(q)[0]
r0 = np.exp(lr); I = np.zeros((len(r0), S.Nr))
for i, x in enumerate(r0):
    kk_ = min(max(np.searchsorted(edges, x, side='right') - 1, 1), len(edges) - 2)
    a, b = edges[kk_], edges[kk_ + 1]
    I[i, kk_*q:(kk_ + 1)*q] = lagrange_eval(xg, 2*(x - a)/(b - a) - 1)
w1, w2 = I @ W1, I @ W2
C, Sn = np.cos(th)[None, :], np.sin(th)[None, :]
Wr = C*w1 + Sn*w2; Wt = -Sn*w1 + C*w2; R0 = r0[:, None]
gl = make_interp_spline(lr, g, k=k, axis=0).derivative()(lr)
c8 = [4/5, -1/5, 4/105, -1/280]; h = 2*math.pi/nt
gt = sum(c*(np.roll(g, -j - 1, axis=1) - np.roll(g, j + 1, axis=1)) for j, c in enumerate(c8))/h
Rn = ((l + Wr/R0)*(p*g + gl) + (Wt/R0)*gt - g)/np.abs(g).max(1, keepdims=True)
print(var, fn.split('/')[-1])
for lo in np.arange(-3, 10, 0.5):
    m = (lr >= lo) & (lr < lo + 0.5); m[:3] = m[-3:] = False
    if not m.any(): continue
    Rh = np.fft.rfft(Rn[m], axis=1)/nt; amp = np.sqrt((np.abs(Rh)**2).mean(0))
    top = np.argsort(amp)[::-1][:4]
    print('  [%5.1f,%5.1f) rms %.2e  top modes %s' % (lo, lo + 0.5, np.sqrt((Rn[m]**2).mean()), ' '.join('m%d:%.1e' % (t, amp[t]) for t in top)))
# fit R = R0 + eps * T, T = W.grad rho / max_ring|rho| (a relative scale error eps of W), per band
T = ((Wr/R0)*(p*g + gl) + (Wt/R0)*gt)/np.abs(g).max(1, keepdims=True)
Xr = (p*g + gl)/np.abs(g).max(1, keepdims=True)          # a constant shift of l: R = R0 + dl * Xr
for lo in np.arange(-2, 10, 1.0):
    m = (lr >= lo) & (lr < lo + 1); m[:3] = m[-3:] = False
    a = Rn[m].ravel(); t = T[m].ravel(); x = Xr[m].ravel()
    eps = (a @ t)/(t @ t); A2 = np.stack([t, x], 1); co = np.linalg.lstsq(A2, a, rcond=None)[0]
    print('  [%4.0f,%4.0f) rms R %.2e | eps (W scale) %.3e, rms after %.2e | 2-param eps %.3e dl %.3e rms after %.2e'
          % (lo, lo + 1, np.sqrt((a**2).mean()), eps, np.sqrt(((a - eps*t)**2).mean()), co[0], co[1], np.sqrt(((a - A2 @ co)**2).mean())))
# fit against fields dW in {e_x, e_y, (x,-y), (y,x), (-y,x), W}: T_k = dW.grad rho / max_ring|rho|
X_, Y_ = R0*C, R0*Sn
def Tk(dx, dy):
    dWr = C*dx + Sn*dy; dWt = -Sn*dx + C*dy
    return (dWr*(p*g + gl) + dWt*gt)/R0/np.abs(g).max(1, keepdims=True)
one = np.ones_like(X_)
basis = dict(ex=Tk(one, 0*one), ey=Tk(0*one, one), strain1=Tk(X_, -Y_), strain2=Tk(Y_, X_), rot=Tk(-Y_, X_), Wscale=T)
names = list(basis)
print('  shape of R: x-even part rms / x-odd part rms (theta -> pi - theta)')
jref = (nt//2 - np.arange(nt)) % nt
for lo in np.arange(-2, 10, 1.0):
    m = (lr >= lo) & (lr < lo + 1); m[:3] = m[-3:] = False
    a = Rn[m]; ae = 0.5*(a + a[:, jref]); ao = 0.5*(a - a[:, jref])
    A2 = np.stack([basis[k][m].ravel() for k in names], 1)
    co = np.linalg.lstsq(A2, a.ravel(), rcond=None)[0]
    print('  [%4.0f,%4.0f) rms %.2e even %.2e odd %.2e | fit %s | rms after %.2e'
          % (lo, lo + 1, np.sqrt((a**2).mean()), np.sqrt((ae**2).mean()), np.sqrt((ao**2).mean()),
             ' '.join('%s %.2e' % (k, c) for k, c in zip(names, co)), np.sqrt(((a.ravel() - A2 @ co)**2).mean())))
# my W: div W and the curl law, relative to max_ring |d_x rho|, per band (fd8 in theta, quintic spline in log r)
def dlr(F): return make_interp_spline(lr, F, k=k, axis=0).derivative()(lr)
def dth(F): return sum(c*(np.roll(F, -j - 1, axis=1) - np.roll(F, j + 1, axis=1)) for j, c in enumerate(c8))/h
rx = C*(p*g + gl) - Sn*gt
div = (dlr(R0*Wr)/R0**2 + dth(Wt)/R0)/R0**(p - 1)/np.abs(rx).max(1, keepdims=True)
cur = ((dlr(R0*Wt)/R0**2 - dth(Wr)/R0)/R0**(p - 1) + rx)/np.abs(rx).max(1, keepdims=True)
for lo in (-2, 0, 2, 4, 6, 8):
    m = (lr >= lo) & (lr < lo + 2); m[:3] = m[-3:] = False
    print('  [%d,%d) my W: div rms %.2e max %.2e | curl W + d_x rho rms %.2e max %.2e' % (lo, lo + 2, np.sqrt((div[m]**2).mean()), np.abs(div[m]).max(),
          np.sqrt((cur[m]**2).mean()), np.abs(cur[m]).max()))
