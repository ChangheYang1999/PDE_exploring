import sys, json, numpy as np
sys.path.insert(0, '.')
from far1 import run
G = ''
C = ''
fits = [('X3', G+'c6g/c6g_shape.npz'), ('F3', G+'c6gF/c6gF_shape.npz'), ('X2', G+'s2g/s2g_shape.npz'),
        ('F2', G+'seg3g/seg3g_shape.npz'), ('X1', C+'fixc_c6f_m1.0e-03_shape.npz'), ('F0', C+'c6f_seg1_shape.npz'),
        ('dom90g', G+'dom90g/dom90g_shape.npz')]
rows = {}
for nm, p in fits:
    for N in ([1 << 14, 1 << 15, 1 << 16] if nm == 'X3' else [1 << 15]):
        o, (th, T0, T1f, T1e) = run(p, N=N, verbose=False)
        cl = o['c_l']
        sel = (th > 1e-3) & (th < np.pi/2-1e-3)
        d = (T1e-T1f)
        pick = {}
        for t0 in [0.1, 0.3, 0.6, 0.84, 1.0, 1.2, 1.4, 1.5, 1.55, 1.565]:
            i = np.argmin(np.abs(th-t0)); pick['%.3f' % t0] = [float(T1f[i]), float(d[i]), float(d[i]/abs(T1f[i]))]
        bulk = (th > 0.05) & (th < 1.4)
        row = dict(N=N, c_l=cl, maxabs_d=float(np.max(np.abs(d[sel]))), at=float(th[sel][np.argmax(np.abs(d[sel]))]),
                   max_rel_bulk=float(np.max(np.abs(d[bulk]/T1f[bulk]))), maxabs_d_bulk=float(np.max(np.abs(d[bulk]))),
                   C_axis=float((cl-1)*d[np.argmin(np.abs(th-1.565))]), pick=pick)
        rows['%s_N%d' % (nm, N)] = row
        print(nm, N, 'c_l %.10f' % cl, 'max|Th1e-Th1f| %.4e at %.4f' % (row['maxabs_d'], row['at']),
              'bulk(0.05-1.4) max %.3e rel %.3e' % (row['maxabs_d_bulk'], row['max_rel_bulk']), 'C(1.565) %+.4e' % row['C_axis'], flush=True)
json.dump(rows, open('far1_multi.json', 'w'), indent=1)
