import sys, numpy as np, torch
sys.path.insert(0, '..'); sys.path.insert(0, '.')
from vgen import Trial
import jets as J
P = '../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz'
tr = Trial(P)
print('k', tr.k, 'c_l', tr.c_l, 'file c_l', tr.c_l_file, 'p3', tr.p3, 'L', tr.L)
r = np.array([1e-3, 0.05, 0.7, 3.0, 8.6, 8.61, 25.0, 900.0, 1e5, 1e9])
th = np.array([0.0, 1e-3, 0.3, 0.9, 1.4, np.pi/2 - 1e-3, np.pi/2, 2.0, 3.5, 5.0])
rad = tr.radial(r, 3); an = tr.angular(th)
rho, rhot = tr.field(rad, an, 3)
# cross-check against the first-run verifier's formula implementation (read-only comparison)
sys.path.insert(0, '../IPM_Setting_I.artifacts/d_evaluator/code')
import gen_shape
d = np.load(P, allow_pickle=True)
rho1, H1, _ = gen_shape.shape_rho(d, r, th)
mine = rho[0].cpu().numpy()
print('rel diff vs first-run formula implementation:', np.nanmax(np.abs(mine - rho1) / (np.abs(rho1) + 1e-300)))
# finite differences in r and theta of my rho (from the formula at shifted points)
def rv(rr, tt):
    a = tr.radial(np.array(rr), 0); b = tr.angular(np.array(tt)); return tr.field(a, b, 0, theta=False)[0][0].cpu().numpy()
for i in [1, 3, 4, 6]:
    for jj in [2, 3, 7]:
        h = 1e-4 * r[i]
        fd = (rv([r[i]+h],[th[jj]]) - rv([r[i]-h],[th[jj]]))/(2*h)
        fdt = (rv([r[i]],[th[jj]+1e-5]) - rv([r[i]],[th[jj]-1e-5]))/(2e-5)
        print(i, jj, 'rho_r', float(rho[1, i, jj]), float(fd), ' rho_th', float(rhot[0, i, jj]), float(fdt))
# second radial derivative via jets vs FD
i, jj = 4, 2; h = 1e-3
f2 = (rv([r[i]+h],[th[jj]]) - 2*rv([r[i]],[th[jj]]) + rv([r[i]-h],[th[jj]]))/h**2
print('rho_rr', 2*float(rho[2, i, jj]), float(f2))
# axis functions
ax = tr.axis(np.array([0.5, 2.0, 8.6]), 3)
print('g', J.ders(ax['g'])[:, :].cpu().numpy())
# g = x^2 e^{H(x,0)} vs rho_theta/r at theta = 0
print('g check', (rhot[0, 2:5, 0] / torch.as_tensor(r[2:5], device='cuda')).cpu().numpy())
# own G3 vs finite difference in y of rho at (x, y): (rho(x,y) - y g)/y^3 for small y
x = 2.0
for y in [0.02, 0.01, 0.005]:
    rr = np.hypot(x, y); tt = np.arctan2(y, x)
    print('G3 FD', y, (rv([rr],[tt])[0,0] - y*float(ax['g'][0,1]))/y**3, 'jet', float(ax['G3'][0,1]))
