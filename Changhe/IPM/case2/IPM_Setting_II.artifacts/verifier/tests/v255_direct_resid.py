"""V255: independent recomputation of numerics R21 (direct residuals R and E on the R20 x-even base states).
Velocity: my class-S law code/charsolve.py (Gauss-Legendre panels in r, exact per-mode radial Green's function, tail
r^p A beyond L), on rho imported from the numerics grid by quintic splines in log r (same angles, no angular
interpolation); W is brought back to the numerics nodes by exact panel Lagrange interpolation.
Differentiation (different from the numerics' 6th-order finite differences in log r): quintic interpolating spline in
log r; in theta either FFT (variant 'fft') or 8th-order periodic central differences (variant 'fd8').
  R = V.grad rho - rho, V = l X + W, l = 1/p:   R / r^p = (l + W_r/r)(p g + g_lr) + (W_th/r) g_th - g
  E = -Lap psi - d_x rho = -curl W - d_x rho,   curl W = r^-2 d_lr(r W_th) - r^-1 d_th W_r
Normalisations as in R21: R / max_ring |rho|, E / max_ring |d_x rho|; bands in log r; 3-degree windows at 90 / 270
deg ('near'), weak-axis sectors within 10 deg of 0 / 180; the three end rows at each end excluded from the bands.
Also R21(b): K = rho(r, -off) / rho(r, +off) across the positive x-axis against exp(D_ax), and the step location.
Usage: python3 -B tests/v255_direct_resid.py STATE.npz [ppu] [q]"""
import sys, math, json, time, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import make_interp_spline
sys.path.insert(0, 'code')
from charsolve import CharSolver, lagrange_eval
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
g, lr, th = d['g'].astype(float), d['lr'].astype(float), d['th'].astype(float)
info = json.loads(str(d['info'])); p = float(json.loads(str(d['args']))['p']); l = 1.0/p
ppu = int(sys.argv[2]) if len(sys.argv) > 2 else 4
q = int(sys.argv[3]) if len(sys.argv) > 3 else 8
nt = len(th); assert np.allclose(th, 2*math.pi*np.arange(nt)/nt)
t0 = time.time()
tmin, tmax = float(lr[0]), float(lr[-1])
P = int(round((tmax - tmin)*ppu))
edges = np.concatenate([[0.0], np.exp(np.linspace(tmin, tmax, P + 1))])
S = CharSolver(edges, q, nt, math.exp(tmin), 'cuda')
assert np.allclose(S.th.cpu().numpy(), th)
rr = S.r.cpu().numpy(); lrr = np.log(rr)
spl = make_interp_spline(lr, g, k=5, axis=0)
G = spl(np.clip(lrr, tmin, tmax)); G[lrr < tmin] = 0.0
rho_my = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
W1, W2 = S.velocity(rho_my, p)
W1, W2 = W1.cpu().numpy(), W2.cpu().numpy()
# panel Lagrange interpolation from my Gauss nodes to the numerics radii
xg = np.polynomial.legendre.leggauss(q)[0]
r0 = np.exp(lr); I = np.zeros((len(r0), S.Nr))
for i, x in enumerate(r0):
    k = np.searchsorted(edges, x, side='right') - 1
    k = min(max(k, 1), len(edges) - 2)
    a, b = edges[k], edges[k + 1]
    I[i, k*q:(k + 1)*q] = lagrange_eval(xg, 2*(x - a)/(b - a) - 1)
w1, w2 = I @ W1, I @ W2
C, Sn = np.cos(th)[None, :], np.sin(th)[None, :]
Wr = C*w1 + Sn*w2; Wt = -Sn*w1 + C*w2
R0 = r0[:, None]
def dlr(F): return make_interp_spline(lr, F, k=5, axis=0).derivative()(lr)
kk = np.fft.fftfreq(nt, 1.0/nt)
def dth_fft(F):
    Fh = np.fft.fft(F, axis=1); kd = 1j*kk.copy()
    if nt % 2 == 0: kd[nt//2] = 0.0
    return np.real(np.fft.ifft(kd[None, :]*Fh, axis=1))
c8 = [4/5, -1/5, 4/105, -1/280]
def dth_fd8(F):
    h = 2*math.pi/nt
    return sum(c*(np.roll(F, -j - 1, axis=1) - np.roll(F, j + 1, axis=1)) for j, c in enumerate(c8))/h
gl = dlr(g)
rec = dict(state=fn.split('/')[-1], nt=nt, p=p, ppu=ppu, q=q, D_ax=info['D_ax'], m1_info=info['m1'])
mc, mb = S.moments(rho_my, p); rec['c_my'] = float(mc); rec['b_my'] = float(mb)
rec['m1_my'] = l - math.hypot(float(mc), float(mb))
bands = [(-14, -13), (-13, -12), (-12, -11), (-11, -10), (-10, -9), (-9, -8), (-8, -7), (-7, -6), (-6, -5), (-5, -4),
         (-4, -3), (-3, -2), (-2, 2), (2, 10.01)]
thd = np.degrees(th)
near = (np.abs(thd - 90) <= 3) | (np.abs(thd - 270) <= 3)
weak = (np.minimum(np.abs(thd - 0), np.abs(thd - 360)) <= 10) | (np.abs(thd - 180) <= 10)
rows = np.zeros(len(lr), bool); rows[3:-3] = True
for var, dth in (('fft', dth_fft), ('fd8', dth_fd8)):
    gt = dth(g)
    Rn = ((l + Wr/R0)*(p*g + gl) + (Wt/R0)*gt - g)/np.abs(g).max(1, keepdims=True)
    # d_x rho and curl W, all divided by r^(p-1)
    rx = C*(p*g + gl) - Sn*gt                       # d_x rho / r^(p-1)
    curl = (dlr(R0*Wt)/R0**2 - dth(Wr)/R0)/R0**(p - 1)
    En = (-curl - rx)/np.abs(rx).max(1, keepdims=True)
    out = []
    for lo, hi in bands:
        m = rows & (lr >= lo) & (lr < hi)
        a = np.abs(Rn[m][:, ~near]); e = np.abs(En[m][:, ~near])
        jm = np.unravel_index(np.argmax(a), a.shape); thmax = thd[~near][jm[1]]
        out.append(dict(band=[lo, hi], R_rms=float(np.sqrt((a**2).mean())), R_max=float(a.max()), R_max_thdeg=float(thmax),
                        R_near_max=float(np.abs(Rn[m][:, near]).max()), R_weak_rms=float(np.sqrt((Rn[m][:, weak]**2).mean())),
                        R_rest_rms=float(np.sqrt((Rn[m][:, ~weak & ~near]**2).mean())), frac_R_gt_1e2=float((a > 1e-2).mean()),
                        E_rms=float(np.sqrt((e**2).mean())), E_max=float(e.max()),
                        E_weak_rms=float(np.sqrt((En[m][:, weak]**2).mean())), E_rest_rms=float(np.sqrt((En[m][:, ~weak & ~near]**2).mean()))))
    rec[var] = out
    rec[var + '_endrows_Rmax'] = float(np.abs(Rn[~rows]).max())
print(json.dumps(rec), flush=True)
for var in ('fft', 'fd8'):
    print('variant', var)
    for o in rec[var]:
        print('  lr [%g,%g): R rms %.2e max %.2e at %.0f deg | near-zero max %.2e | weak %.2e rest %.2e | frac>1e-2 %.2f || E rms %.2e max %.2e weak %.2e rest %.2e'
              % (o['band'][0], o['band'][1], o['R_rms'], o['R_max'], o['R_max_thdeg'], o['R_near_max'], o['R_weak_rms'], o['R_rest_rms'],
                 o['frac_R_gt_1e2'], o['E_rms'], o['E_max'], o['E_weak_rms'], o['E_rest_rms']))
    print('  end rows: R max %.2e' % rec[var + '_endrows_Rmax'])
print('m1 (my moments, grid only) %.6f; info m1 %.6f; c %.6f b %.2e' % (rec['m1_my'], rec['m1_info'], rec['c_my'], rec['b_my']))
# R21(b): ratio across the positive x-axis, rho(r, -off)/rho(r, +off) = g[:, nt - j]/g[:, j]
print('exp(D_ax) = %.4f' % math.exp(info['D_ax']))
for L0 in (-13, -12, -11, -10, -9, -6):
    i = int(np.argmin(np.abs(lr - L0)))
    js = [1, 2, 4, 8, int(round(5/(360/nt)))]
    K = [g[i, nt - j]/g[i, j] for j in js]
    # step: largest relative jump of rho/(r^2 cos^2 th) between neighbouring cells for th in (0, 12 deg)
    jj = np.arange(0, int(12/(360/nt)) + 1)
    f = g[i, jj]*np.exp((p - 2)*lr[i])/np.cos(th[jj])**2
    jr = np.abs(np.diff(np.log(np.abs(f))))
    js_ = int(np.argmax(jr))
    print('  lr %.2f: K at offsets %s cells (%s deg) = %s; largest step of log(rho/x^2) on (0,12 deg): %.3f between %.2f and %.2f deg (ratio %.4f), y/x^2 there %.0f'
          % (lr[i], js, ['%.2f' % (j*360/nt) for j in js], ['%.4f' % k for k in K], jr[js_], thd[jj[js_]], thd[jj[js_ + 1]],
             f[js_]/f[js_ + 1], math.tan(th[jj[js_]] + th[1]/2)/(math.exp(lr[i])*math.cos(th[jj[js_]]))))
print('time %.1f s' % (time.time() - t0))
