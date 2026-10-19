"""V237 addendum: Krylov-dimension dependence of the 1024 core-frozen slaved b_1 columns, all four cross pairs,
x-odd rows 17-36, relative to each column and relative to the eps 3e-6 column of the same Krylov dimension."""
import numpy as np, json
P = 'runs/pfwd/par/'
def col(t):
    out = [json.loads(l) for l in open(P + t + '.out') if l.startswith('{')]
    return np.array([o['col_values'] for o in out if 'col_values' in o][0])[17:37]
C = {t: col(t) for t in ('PLM1024Ae6', 'PLM1024Ae7', 'PLM1024Ak6', 'PLM1024Ak7')}
for a, c in (('PLM1024Ak6', 'PLM1024Ae6'), ('PLM1024Ak7', 'PLM1024Ae7'), ('PLM1024Ak6', 'PLM1024Ae7'),
             ('PLM1024Ak7', 'PLM1024Ae6')):
    d = np.linalg.norm(C[a] - C[c])
    print('%s vs %s: rel. to %s %.3f, rel. to %s %.3f, rel. to Ak6 %.3f, rel. to Ae6 %.3f' % (
        a, c, a, d / np.linalg.norm(C[a]), c, d / np.linalg.norm(C[c]), d / np.linalg.norm(C['PLM1024Ak6']),
        d / np.linalg.norm(C['PLM1024Ae6'])))
for t in C: print(t, 'norm rows 17-36 %.4f' % np.linalg.norm(C[t]))
