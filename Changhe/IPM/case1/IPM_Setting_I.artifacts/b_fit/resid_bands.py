import sys, numpy as np
z = np.load(sys.argv[1])
r, th = z['r'], z['theta']; rr = r[:, None] + 0*th
nr = z['residual'] / np.where(z['denominator'] > 0, z['denominator'], np.inf)
R = z['W1']*z['rho_x'] + z['W2']*z['rho_y'] - z['rho']
den2 = np.abs(z['W1']*z['rho_x']) + np.abs(z['W2']*z['rho_y']) + np.abs(z['rho'])
alt = np.where(den2 > 0, R / np.where(den2>0, den2, 1), 0)
T = th[None, :] + 0*rr
for name, m in [('r<=2', rr <= 2), ('2<=r<=10', (rr >= 2) & (rr <= 10)), ('10<=r<=100', (rr>=10)&(rr<=100)), ('100<=r<=1000',(rr>=100)&(rr<=1000))]:
    m = m & (T > 0) & (T < np.pi/2 - 1e-12)
    for bn, b in [('theta<0.05', T < 0.05), ('0.05<=theta<=pi/2-0.05', (T >= 0.05) & (T <= np.pi/2 - 0.05)), ('theta>pi/2-0.05', T > np.pi/2 - 0.05)]:
        mm = m & b
        if mm.sum() == 0: continue
        a = np.abs(nr[mm]); i = np.argmax(a)
        b2 = np.abs(alt[mm]); i2 = np.argmax(b2)
        print(f'{name:14s} {bn:24s} max|elog/dlog|={a[i]:.2e} at r={rr[mm][i]:.2f},th={T[mm][i]:.4f}  rms={np.sqrt(np.mean(a**2)):.1e} | FD-fields R/(|W1 rx|+|W2 ry|+|rho|) max={b2[i2]:.2e} at r={rr[mm][i2]:.2f},th={T[mm][i2]:.4f}')
