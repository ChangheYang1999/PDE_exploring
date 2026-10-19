"""V193: row-block norms and row-subset agreement of the numerics b1 columns PLS1e6, PLS1e7, PLM1e6, PLM1e7 (read only)."""
import numpy as np, json
P = 'runs/pfwd/par/'
C = {}
for t in ('PLS1e6', 'PLS1e7', 'PLM1e6', 'PLM1e7'):
    out = [json.loads(l) for l in open(P + t + '.out') if l.startswith('{')]
    c = np.array([o['col_values'] for o in out if 'col_values' in o][0]); lc = [o['lin_col'] for o in out if 'lin_col' in o][0]
    C[t] = c
    print('%s |rows 0-16| %.4f |rows 17-36| %.4f even fraction of |col|^2 %.3f; rows 33-36 (D_ax, M_up, M_dn, psi_yy0) %s; '
          'dF_even %.4f dF_odd %.4f th12_j %s' % (t, np.linalg.norm(c[:17]), np.linalg.norm(c[17:]), (c[:17]**2).sum() / (c**2).sum(),
          np.round(c[33:], 4), lc['dF_even'], lc['dF_odd'], np.round(lc['th12_j'], 3)))
for a, c in [('PLM1e6', 'PLM1e7'), ('PLM1e7', 'PLS1e7'), ('PLM1e6', 'PLS1e6'), ('PLS1e6', 'PLS1e7')]:
    for lo, hi, nm in [(17, 33, 'b1-b16 (rows 17-32)'), (19, 33, 'b3-b16 (rows 19-32)'), (33, 37, 'D_ax, M_up, M_dn, psi_yy0 (rows 33-36)')]:
        x, y = C[a][lo:hi], C[c][lo:hi]
        print('%s vs %s %s: |a - c|/|c| %.3f |a - c|/|a| %.3f cos %.4f' % (a, c, nm, np.linalg.norm(x - y) / np.linalg.norm(y),
              np.linalg.norm(x - y) / np.linalg.norm(x), x @ y / np.linalg.norm(x) / np.linalg.norm(y)))
