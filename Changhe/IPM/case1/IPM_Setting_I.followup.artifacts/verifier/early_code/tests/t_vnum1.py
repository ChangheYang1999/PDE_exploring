"""verifier: tests of the reader vnum.NumTrial on a numerics-lane state.
(1) own node sets vs stored; (2) the interpolant reproduces b at the nodes; (3) radial jets vs central differences;
(4) rho_theta vs differences; (5) axis jets g, G3 vs a small-y polynomial fit of rho(x, y); (6) angular spectrum of
d_x rho (decay of the sin(2n theta) coefficients) at several r.
usage: python3 t_vnum1.py state.npz"""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch
from vnum import NumTrial
from vres import analyse_sin, theta_grid
import jets as J
DT = torch.float64
path = sys.argv[1]
tr = NumTrial(path, 'cuda')
print('state %s: N %d M %d L %g beta %g c_l %.15f C %s' % (path, tr.N, tr.M, tr.L, tr.beta, tr.c_l, tr.Cfile))
print('(1) node sets: max |q_own - q_file| %.2e, |theta_own - theta_file| %.2e' % (tr.node_check['q'], tr.node_check['theta']))
# (2) nodes
k = tr.k
qi = tr.qn[1:-1]
ri = tr.L * np.sqrt((1 - qi) ** (-2 / (1 - k)) - 1)
rad = tr.radial(ri, 0)
an = tr.angular(torch.as_tensor(tr.thn, dtype=DT))
rho, _ = tr.field(rad, an, 0, theta=False)
den = rad['W0'][0][:, None] * an['Pi'][None, :]
bb = (rho[0] / den).cpu().numpy()
print('(2) interpolant at the nodes: max |b_own - b_file| = %.2e (max |b| %.3f)' % (np.abs(bb - tr.bnodes[1:-1]).max(), np.abs(tr.bnodes).max()))
# (3) radial jets vs differences, (4) theta derivative
th = torch.as_tensor(np.array([0.05, 0.4, 0.9, 1.3, 1.55]), dtype=DT)
an = tr.angular(th)
for r0 in [1e-3, 0.3, 3.0, 8.6, 50.0, 1e4]:
    rad = tr.radial(np.array([r0]), 3)
    rj, rt = tr.field(rad, an, 3)
    h = 1e-3 * r0
    vals = []
    for s in (-2, -1, 1, 2):
        rr, _ = tr.field(tr.radial(np.array([r0 + s * h]), 0), an, 0, theta=False)
        vals.append(rr[0, 0])
    fd1 = (8 * (vals[2] - vals[1]) - (vals[3] - vals[0])) / (12 * h)
    fd2 = (-(vals[3] + vals[0]) + 16 * (vals[2] + vals[1]) - 30 * rj[0, 0]) / (12 * h * h)
    e1 = float((rj[1, 0] - fd1).abs().max() / rj[1, 0].abs().max())
    e2 = float((2 * rj[2, 0] - fd2).abs().max() / (2 * rj[2, 0]).abs().max())
    ht = 1e-4
    a1 = tr.angular(th + ht); a2 = tr.angular(th - ht)
    rp, _ = tr.field(tr.radial(np.array([r0]), 0), a1, 0, theta=False)
    rm, _ = tr.field(tr.radial(np.array([r0]), 0), a2, 0, theta=False)
    e3 = float(((rp - rm)[0, 0] / (2 * ht) - rt[0, 0]).abs().max() / rt[0, 0].abs().max())
    print('(3,4) r %8g: rho_r rel %.1e  rho_rr rel %.1e  rho_theta rel %.1e' % (r0, e1, e2, e3))
# (5) axis jets
for x0 in [0.05, 1.0, 5.0, 8.6, 20.0]:
    ax = tr.axis(torch.as_tensor([x0], dtype=DT, device='cuda'), 3)
    ys = x0 * np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    rr = np.sqrt(x0 ** 2 + ys ** 2); tt = np.arctan2(ys, x0)
    vals = []
    for r_, t_ in zip(rr, tt):
        rho, _ = tr.field(tr.radial(np.array([r_]), 0), tr.angular(torch.as_tensor([t_], dtype=DT)), 0, theta=False)
        vals.append(float(rho[0, 0, 0]))
    V = np.vstack([ys, ys ** 3, ys ** 5, ys ** 7]).T
    cf = np.linalg.solve(V[:4], np.array(vals[:4]))
    cf5 = np.linalg.lstsq(V, np.array(vals), rcond=None)[0]
    g, G3 = float(ax['g'][0, 0]), float(ax['G3'][0, 0])
    print('(5) x %5g: g %.12e (fit rel %.1e)  G3 %.10e (fit rel %.1e, %.1e)' % (x0, g, abs(cf[0] - g) / abs(g), G3, abs(cf[1] - G3) / abs(G3), abs(cf5[1] - G3) / abs(G3)))
# (6) angular spectrum of d_x rho
for Nth in [4096, 16384]:
    th = theta_grid(Nth, 'cuda')
    an = tr.angular(th)
    for r0 in [0.01, 1.0, 8.6, 100.0, 1e4, 1e8]:
        rad = tr.radial(np.array([r0]), 1)
        rj, rt = tr.field(rad, an, 1)
        co, si = torch.cos(th), torch.sin(th)
        rx = co * rj[1, 0] - si * rt[0, 0] / r0
        sn, cs = analyse_sin(rx[None, :], th, Nth // 2 - 2)
        a = sn[0, 2::2].abs().cpu().numpy()
        amax = a.max()
        ns = [32, 64, 96, 128, 256, 512, 1024, 2048]
        txt = ' '.join('n%d %.1e' % (n, a[n - 1:n + 3].max() / amax) for n in ns if n + 3 < len(a))
        print('(6) Nth %5d r %8g: |f_n|/max: %s; odd/cos leak %.1e' % (Nth, r0, txt, max(float(sn[0, 1::2].abs().max()), float(cs.abs().max())) / amax))
