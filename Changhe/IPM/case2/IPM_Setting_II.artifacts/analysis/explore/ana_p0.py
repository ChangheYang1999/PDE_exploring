import numpy as np, json, sys
sys.path.insert(0, '.')
import p0_forward as P
d = np.load(sys.argv[1])
f, rho, th = d['f'], d['rho'], d['th']
r = np.exp(rho); Nr, Nth = f.shape
drho = rho[1]-rho[0]
wr, wt = P.velocity(f, rho, th)
ar = 1 + wr/r[:, None]; at = wt/r[:, None]
fr = P.d_rho(f, drho); ft = P.d_th(f)
res = ar*fr + at*ft
print('max|res| by radius band:')
for lo, hi in [(-5, -3), (-3, -1), (-1, 0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]:
    m = (rho >= lo) & (rho < hi)
    i, j = np.unravel_index(np.argmax(np.abs(res[m])), res[m].shape)
    print('  rho in [%g,%g): max|res| %.3g at th=%.3f; max|f_th| %.3g, f range [%.3f, %.3f]' % (lo, hi, np.abs(res[m]).max(), th[j], np.abs(ft[m]).max(), f[m].min(), f[m].max()))
# profile near origin along th=0 (x axis) and th=pi/2
j0 = 0; j90 = Nth//4
for k in range(0, Nr, 24):
    print('r=%.4g f(x-axis)=%.5g f/r^2=%.4g  f(y-axis)=%.3g  Y_r/r(th=0)=%.4g Y_r/r(th=90)=%.4g' % (r[k], f[k, j0], f[k, j0]/r[k]**2, f[k, j90], ar[k, j0], ar[k, j90]))
