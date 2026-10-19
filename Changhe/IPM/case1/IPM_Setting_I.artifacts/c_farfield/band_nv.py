"""Lead's own far-band reading (not the verifier's test): maxima of |R| / N_v over 1000 L < r <= 9000 L, 9000 L < r <= 1e4 L
and r > 1e4 L, over all columns and with pi/2 - theta >= 0.006 (A5), each with its location. The trial's density
everywhere, the velocity by the lead's modal inverse on r <= Rinv L with the two-term exterior beyond (as ptest.py).
Rinv = R_shape is the fit's own convention (no r > R_shape on the grid); a large Rinv is the formula continued.
The fields file is deleted afterwards.
usage (from work/c7): python3 ../far/band_nv.py <shape.npz> <nr> <nt> <Rinv_in_L> <out.json>"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.getcwd())
from diagnose import diagnostic

shape, nr, nt, Rinv, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
fields = out.replace('.json', '_fields.npz')
diagnostic(shape, nr, nt, Rinv, export=fields, tail="two-term")
z = np.load(fields)
r, th = z['r'], z['theta']; D = z['denominator']
with np.errstate(divide='ignore', invalid='ignore'):
    Q = np.where(D > 0, np.abs(z['residual'])/D, 0.)    # 0/0 on the x-axis column (rho = 0 there) is not a value
L = float(np.load(shape)['L'])
rec = dict(shape=shape, nr=nr, nt=nt, Rinv_L=Rinv, c_l_export=float(z['c_l']), bands={})
a5 = (np.pi/2 - th) >= 0.006
for name, lo, hi in (('1000L<r<=9000L', 1000, 9000), ('9000L<r<=1e4L', 9000, 1e4), ('r>1e4L', 1e4, np.inf)):
    rs = (r > lo*L) & (r <= hi*L)
    if not rs.any():
        continue
    for tag, ts in (('all', np.ones_like(a5)), ('A5', a5)):
        sub = Q[np.ix_(rs, ts)]
        i, j = np.unravel_index(int(np.argmax(sub)), sub.shape)
        rr, tt = r[rs][i], th[ts][j]
        rec['bands']['%s/%s' % (name, tag)] = dict(max=float(sub[i, j]), r=float(rr), r_L=float(rr/L), theta=float(tt))
        print('%-16s %-3s  max %.4e  at r/L %.4g  theta %.5f' % (name, tag, sub[i, j], rr/L, tt))
json.dump(rec, open(out, 'w'), indent=1)
os.remove(fields)
