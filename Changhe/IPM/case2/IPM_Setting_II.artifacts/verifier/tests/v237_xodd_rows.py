"""V237: the V225 metric (relative difference of the x-odd rows 17-36 of the column, relative to each column) for the
core-frozen slaved b_1 pairs, including the kmax-40 repeat PLM1024Ak6 / Ak7. Reads the numerics records only."""
import numpy as np, json
P = 'runs/pfwd/par/'
def col(t):
    out = [json.loads(l) for l in open(P + t + '.out') if l.startswith('{')]
    return np.array([o['col_values'] for o in out if 'col_values' in o][0]), [o['lin_col'] for o in out if 'lin_col' in o][0]
for a, c in (('PLM256e6', 'PLM256e7'), ('PLM1e6', 'PLM1e7'), ('PLM1024Ae6', 'PLM1024Ae7'), ('PLM1024Ak6', 'PLM1024Ak7'),
             ('PLM1024Ak6', 'PLM1024Ae6'), ('PLM1024Ak7', 'PLM1024Ae7')):
    (x, ra), (y, rc) = col(a), col(c)
    xa, ya = x[17:37], y[17:37]
    d = np.linalg.norm(xa - ya)
    print('%-11s vs %-11s x-odd rows 17-36: rel. to first %.3f, rel. to second %.3f; resid_true %.4f / %.4f; kmax %s / %s;'
          ' b_1 %.3f / %.3f' % (a, c, d / np.linalg.norm(xa), d / np.linalg.norm(ya), ra['resid_true'], rc['resid_true'],
          ra.get('kmax'), rc.get('kmax'), x[17], y[17]))
