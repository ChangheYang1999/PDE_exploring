# Lead (2026-10-18): axis law with the transverse strain taken directly from the computed velocity,
# a_dir = (V_r + d_th V_th)/r on the axis, versus a_div = 2l - dV_r/dr (uses div V = 2l). Reports max|a_dir - a_div| on
# lr in [-8, 0] per half-axis, the spread of q = log h - 2 log k - law (lr >= -8) for both choices, and D_ax for both
# (q_down - q_up at lr_max, k = 1 at the innermost point), plus the half-axis h ratio at lr = -10.
# Usage: python3 adir.py state.npz [m1] [fd]   (fd: h from the local angular second difference instead of the FFT)
import sys, json, numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); g, lr, th = d['g'], d['lr'], d['th']; p = float(d['p']); l = 1 / p; r = np.exp(lr); N = len(th)
m1 = float(sys.argv[2]) if len(sys.argv) > 2 else float(d['m1'])
rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
kk = np.fft.rfftfreq(N, 1.0 / N)
dwt = np.fft.irfft(1j * kk * np.fft.rfft(wt, axis=1), N, axis=1)
gtt = np.fft.irfft(-(kk ** 2) * np.fft.rfft(g, axis=1), N, axis=1)
if 'fd' in sys.argv[3:]:                                  # local second difference (V72: FFT g_thth has Gibbs sign changes)
    gtt = (np.roll(g, -1, axis=1) - 2 * g + np.roll(g, 1, axis=1)) / (2 * np.pi / N) ** 2
res = dict(state=sys.argv[1].split('/')[-1], Nth=N, Nr=len(lr), m1=round(m1, 4), h='fd' if 'fd' in sys.argv[3:] else 'fft'); q = {}
w8 = (lr >= -8) & (lr <= 0); wq = lr >= -8
for name, j in (('up', N // 4), ('down', 3 * N // 4)):
    Vr = l * r + wr[:, j]; adiv = 2 * l - np.gradient(Vr, r); adir = (Vr + dwt[:, j]) / r; h = r ** (p - 2) * gtt[:, j]
    law = np.concatenate([[0], np.cumsum(0.5 * ((1 - 2 * m1) / Vr[1:] + (1 - 2 * m1) / Vr[:-1]) * np.diff(r))])
    for tag, a in (('div', adiv), ('dir', adir)):
        f = -(a - m1) / Vr; logk = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(r))])
        q[name + tag] = np.log(np.abs(h)) - 2 * logk - law
        res['spread_%s_%s' % (name, tag)] = round(float(np.ptp(q[name + tag][wq])), 4)
    res['maxdiv_err_' + name] = round(float(np.max(np.abs(adir - adiv)[w8])), 4)
    res['h_lrmin_' + name] = float('%.4g' % h[0])
for tag in ('div', 'dir'):
    res['D_ax_' + tag] = round(float(q['down' + tag][-1] - q['up' + tag][-1]), 4)
if 'thA' in d:
    deg = np.degrees(d['thA']); lg = d['logGt']; pk = lambda a: float(lg[np.argmin(np.abs(deg - a))])
    res['D_samp'] = round(pk(269) - pk(89), 4)
print(json.dumps(res))
