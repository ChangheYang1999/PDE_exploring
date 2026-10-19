# Envelope of the absolute residual R and of R/N_f near P by r and theta band (verifier, verifier).
import sys, numpy as np
for t in sys.argv[1:]:
    d = np.load('runs/audit/%s_resmap.npz' % t); r, th, R, Nf = d['r'], d['th'], d['R'], d['Nf']
    with np.errstate(all='ignore'): X = np.where(Nf > 0, R / Nf, 0.0)
    print(t, 'x*', float(d['x_star']))
    bands = [(0, .05), (.05, .15), (.15, .3), (.3, .6), (.6, 1.5)]
    print('   r      ' + '  '.join(['|R| th%.2f-%.2f' % b for b in bands]) + '   |R/Nf| th0-0.05  th.05-.15')
    for a in np.arange(7.9, 9.3, 0.1):
        i = (r >= a) & (r < a + 0.1)
        s = []
        for b in bands:
            j = (th > b[0]) & (th <= b[1])
            s.append('%.2e' % np.abs(R[np.ix_(i, j)]).max())
        j1 = (th > 1e-6) & (th <= .05); j2 = (th > .05) & (th <= .15)
        print('  %.1f-%.1f ' % (a, a + .1) + '       '.join(s) + '      %.2e  %.2e' % (np.abs(X[np.ix_(i, j1)]).max(), np.abs(X[np.ix_(i, j2)]).max()))
