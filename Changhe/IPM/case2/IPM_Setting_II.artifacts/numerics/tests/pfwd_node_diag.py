"""Near-node structure of a forward-evolution state: angular profile g(theta)/max at several radii, angular zero order near
+-90 deg, local radial exponent of rho along theta = 0, and where (in theta) the pointwise stationarity residual is largest."""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd, fd_dlr
torch.set_default_dtype(torch.float64)
fn = sys.argv[1]
dd = np.load(fn); g = torch.tensor(dd['g'], device='cuda'); lr = dd['lr']; args = json.loads(str(dd['args'])); p = args['p']
Nr, Nth = g.shape; S = PFwd(Nr, Nth, float(lr[0]), float(lr[-1]), p, dev='cuda')
rho = S.r[:, None] ** p * g
Wr, Wt = S.velocity(rho)
rho_lr = fd_dlr(rho, S.d); rho_t = S.d_theta(rho)
Vr = S.cl * S.r[:, None] + Wr
Rres = (Vr * rho_lr + Wt * rho_t) / S.r[:, None] - rho
th = S.th.cpu().numpy(); deg = np.degrees(th)
gn = g.cpu().numpy(); rr = S.r.cpu().numpy(); Rn = Rres.cpu().numpy(); rhon = rho.cpu().numpy()
print("file %s p=%g grid %dx%d" % (fn, p, Nr, Nth))
# local radial exponent of rho along theta=0 and theta = 45 deg
j0 = 0; j45 = int(round(45 / 360 * Nth)); j90 = int(round(90 / 360 * Nth))
for k in (30, 60, 100, 150, 200, 250, 300, 361, 420, 480, 540, 600):
    if k + 1 >= Nr: break
    ex0 = (np.log(rhon[k + 1, j0]) - np.log(rhon[k - 1, j0])) / (2 * S.d)
    ex45 = (np.log(rhon[k + 1, j45]) - np.log(rhon[k - 1, j45])) / (2 * S.d)
    prof = gn[k] / gn[k].max()
    # angular zero order near 90 deg: fit log prof vs log|theta - pi/2| over the 3 points nearest the axis (excluding the axis point)
    jj = [j90 - 3, j90 - 2, j90 - 1]
    xs = np.log(np.abs(th[jj] - math.pi / 2)); ys = np.log(np.maximum(prof[jj], 1e-300))
    slope = np.polyfit(xs, ys, 1)[0]
    jmax = int(np.argmax(np.abs(Rn[k]))); relR = np.abs(Rn[k]).max() / rhon[k].max()
    print("r=%.2e  d log rho/d log r: th=0: %.4f  th=45: %.4f | g/max at 0,30,60,80,85,89 deg: %s | zero order at 90: %.3f | max|R|/max rho = %.2e at th=%.1f deg (rho/max there %.2e)" %
          (rr[k], ex0, ex45, ' '.join('%.3f' % prof[int(round(a / 360 * Nth))] for a in (0, 30, 60, 80, 85, 89)), slope, relR, deg[jmax], rhon[k, jmax] / rhon[k].max()))
