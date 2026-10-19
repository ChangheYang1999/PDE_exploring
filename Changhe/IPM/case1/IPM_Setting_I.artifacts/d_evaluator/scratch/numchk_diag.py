import numpy as np, sys
z = np.load('runs/numchk/n256R3000_N1500.npz'); o = np.load('../numerics/runs/rep_fields_N256M64R3000L10.npz')
r, th, rho = z['r'], z['theta'], z['rho']
# check exported rho vs r^3 cos^2 sin a
ro, tho = o['r'], o['theta']
print('rho_export vs x^2 y a:', np.abs(o['rho'] - ro[:, None]**3*np.cos(tho)**2*np.sin(tho)*o['a']).max()/np.abs(o['rho']).max())
# local exponent of rho along theta = pi/4 and pi/3
for tq in (np.pi/8, np.pi/4, 3*np.pi/8, 1.5):
    j = np.argmin(abs(th - tq)); f = rho[:, j]
    s = np.gradient(np.log(np.abs(f)), np.log(r))
    idx = [np.argmin(abs(r - q)) for q in (1, 10, 50, 100, 300, 1000, 2000, 2900)]
    print('theta %.3f' % th[j], ' '.join('%g:%.4f' % (r[i], s[i]) for i in idx))
# same on the exporter's nodes (finite differences in log r on the Radau grid, interior only)
for tq in (np.pi/8, np.pi/4, 3*np.pi/8):
    j = np.argmin(abs(tho - tq)); f = o['rho'][1:, j]
    s = np.gradient(np.log(np.abs(f)), np.log(ro[1:]))
    idx = [np.argmin(abs(ro[1:] - q)) for q in (1, 10, 100, 1000, 2900)]
    print('exp theta %.3f' % tho[j], ' '.join('%g:%.4f' % (ro[1:][i], s[i]) for i in idx))
# their residual check: W.grad rho - rho on their nodes by spectral derivative? use W1, W2 exported with FD in my resample
print('W1 at large r, theta ~ pi/4:', o['W1'][-5:, 32], 'c_l r cos =', o['c_l']*ro[-5:]*np.cos(tho[32]))
print('U1/r at r=100,1000:', [float(np.abs(o['U1'][np.argmin(abs(ro-q))]).max()/q) for q in (10,100,1000,2900)])
