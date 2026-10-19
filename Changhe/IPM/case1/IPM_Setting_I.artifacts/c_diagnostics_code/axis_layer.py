"""Near-axis layer probe on a construct1-style export (polar grid r[i], theta[j]).
For rings r ~ r0, print theta, y, normalized residual, (rho - y g(x))/y^3, and the prediction y^2 T3/g of the
y-expansion, where T3 = w G3' + (3h-1) G3 + a2 g' + b3 g uses the exported axis jets.
Usage: python axis_layer.py fields.npz r0 [r0 ...]"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
z = np.load(sys.argv[1], allow_pickle=False)
r, th = z['r'], z['theta']
rho, res = z['rho'], z['residual']
den = z['denominator'] if 'denominator' in z.files else None
ax = z['axis_x']
sel = (ax > 0) & (ax < 40)
x = ax[sel]
def sp(name):
    return CubicSpline(x, z[name][sel])
g, gp, w, h = sp('axis_G1'), sp('axis_G1_prime'), sp('axis_w'), sp('axis_h')
G3 = sp('axis_G3')
G3p = sp('axis_G3_prime') if 'axis_G3_prime' in z.files else G3.derivative()
a2 = sp('axis_A2'); b3 = sp('axis_B3W')
T3 = lambda t: w(t) * G3p(t) + (3 * h(t) - 1) * G3(t) + a2(t) * gp(t) + b3(t) * g(t)
print('nr, nt =', len(r), len(th), ' theta[0:3] =', th[:3])
for r0 in map(float, sys.argv[2:]):
    i = int(np.argmin(abs(r - r0)))
    print(f'ring r = {r[i]:.5f}')
    print('   theta        y          resid        (rho-yg)/y^3   G3(x)      pred y^2 T3/g')
    for j in list(range(0, 12)) + list(range(12, 120, 12)):
        if j >= len(th):
            break
        xx, yy = r[i] * np.cos(th[j]), r[i] * np.sin(th[j])
        cub = (rho[i, j] - yy * g(xx)) / yy ** 3
        print(f'  {th[j]:.5f}  {yy:.5f}  {res[i, j]: .3e}   {cub: .6f}   {G3(xx): .6f}  {yy**2 * T3(xx) / g(xx): .3e}')
