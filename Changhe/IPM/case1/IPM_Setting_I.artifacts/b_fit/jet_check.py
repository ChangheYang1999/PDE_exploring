import sys, numpy as np
from scipy.interpolate import CubicSpline
z = np.load(sys.argv[1])
r, th = z['r'], z['theta']
ax = z['axis_x']; sel = (ax > 0) & (ax < 40); x = ax[sel]
sp = lambda n: CubicSpline(x, z[n][sel])
g, gp, w, h, G3, G3p, a2, b3 = [sp(n) for n in ['axis_G1','axis_G1_prime','axis_w','axis_h','axis_G3','axis_G3_prime','axis_A2','axis_B3W']]
print('b3 + a2\'/3 rel:', [float((b3(t) + a2.derivative()(t)/3)/ (abs(b3(t))+1e-30)) for t in (1,4,8)])
print('G3p - dG3 rel:', [float((G3p(t) - G3.derivative()(t))/abs(G3p(t))) for t in (1,4,8)])
print('gp - dg rel:', [float((gp(t) - g.derivative()(t))/abs(gp(t))) for t in (1,4,8)])
for r0 in (1., 4., 8.):
    i = int(np.argmin(abs(r - r0)))
    print('ring', r[i])
    for j in (1, 2, 4, 8):
        X, Y = r[i]*np.cos(th[j]), r[i]*np.sin(th[j])
        W1, W2, rx, ry, rh = z['W1'][i,j], z['W2'][i,j], z['rho_x'][i,j], z['rho_y'][i,j], z['rho'][i,j]
        R = W1*rx + W2*ry - rh
        print(f'  y={Y:.4f} a2fd={(W1-w(X))/Y**2: .6f} a2={a2(X): .6f} | h_fd={W2/Y: .6f} h={h(X): .6f} | b3fd={(W2-Y*h(X))/Y**3: .5f} b3={b3(X): .5f}'
              f' | rhox jet={(rx - Y*gp(X))/Y**3: .5f} G3p={G3p(X): .5f} | R/y^3={R/Y**3: .4e} T3={w(X)*G3p(X)+(3*h(X)-1)*G3(X)+a2(X)*gp(X)+b3(X)*g(X): .4e} | R/rho={R/rh: .2e} resid={z["residual"][i,j]: .2e}')
