"""V225: relative difference of the x-odd rows (17-36) of the b1 columns, pairs at equal resolution and across
resolutions (read only, numerics records)."""
import json, numpy as np
P = 'runs/pfwd/par/'
C = {}
for t in ('PLM256e6', 'PLM256e7', 'PLM1e6', 'PLM1e7', 'PLM1024Ae6', 'PLM1024Ae7'):
    out = [json.loads(l) for l in open(P + t + '.out') if l.startswith('{')]
    C[t] = np.array([o['col_values'] for o in out if 'col_values' in o][0])
    print(t, 'b_1 %.4f' % C[t][17], 'b_3 %.4f' % C[t][19])
for a, c in (('PLM256e6', 'PLM256e7'), ('PLM1e6', 'PLM1e7'), ('PLM1024Ae6', 'PLM1024Ae7'), ('PLM1024Ae6', 'PLM1e7'),
             ('PLM1024Ae6', 'PLM256e7'), ('PLM1024Ae7', 'PLM1e6'), ('PLM1024Ae7', 'PLM256e6')):
    x, y = C[a][17:37], C[c][17:37]
    print('%-10s vs %-10s x-odd rows 17-36: |a-c|/|a| %.3f |a-c|/|c| %.3f' % (a, c, np.linalg.norm(x - y) / np.linalg.norm(x),
          np.linalg.norm(x - y) / np.linalg.norm(y)))
print('all cross pairs, x-odd rows 17-36, relative to the first column:')
for a in ('PLM1024Ae6', 'PLM1024Ae7'):
    for c in ('PLM1e6', 'PLM1e7', 'PLM256e6', 'PLM256e7'):
        x, y = C[a][17:37], C[c][17:37]
        print('  %-10s vs %-8s %.3f' % (a, c, np.linalg.norm(x - y) / np.linalg.norm(x)))
