"""V193: the numerics core-frozen b1 columns PLM1e6 / PLM1e7 (lrcut -8, lrw 1) against the slaved PLS1e6 / PLS1e7, read
only: Hessenberg least-squares residual recomputed from the stored H, y, beta; band shares of v = dg/scale; core part
of v (the mask should freeze lr < -8.5); column values and their row-subset agreement; the acceptance rule."""
import numpy as np, json, os, itertools
P = 'runs/pfwd/'
b = np.load(P + 'bn/DR512_a2-1.000_it0.npz'); lr = b['lr']; r = np.exp(lr)
p = float(json.loads(str(b['args']))['p']); scale = (r**2 / (1 + r**2))**(1 - p / 2)
tags = [t for t in ('PLS1e6', 'PLS1e7', 'PLM1e6', 'PLM1e7') if os.path.exists(P + 'par/%s_resp_b1.npz' % t)]
V, C, R = {}, {}, {}
for t in tags:
    d = np.load(P + 'par/%s_resp_b1.npz' % t)
    V[t] = d['dg'].astype(float) / scale[:, None]
    out = [json.loads(l) for l in open(P + 'par/%s.out' % t) if l.startswith('{')]
    R[t] = [o['lin_col'] for o in out if 'lin_col' in o][0]
    C[t] = np.array([o['col_values'] for o in out if 'col_values' in o][0])
    H, y, be = d['H'], d['y'], float(d['beta'])
    e1 = np.zeros(H.shape[0]); e1[0] = be
    sv = np.linalg.svd(H, compute_uv=False)
    print('%s: eps_rel %g lrcut %s resid_true %.4f resid_tsvd %.4f (recomputed |beta e1 - H y|/beta %.4f) resid_full %s '
          'resid_core %s n_kept %d H_sv %.4g .. %.4g' % (t, R[t]['eps_rel'], R[t].get('lrcut'), R[t]['resid_true'],
          R[t]['resid_tsvd'], np.linalg.norm(e1 - H @ y) / be, R[t].get('resid_full'), R[t].get('resid_core'),
          R[t]['n_kept'], sv[0], sv[-1]))
    v = V[t]; tot = (v**2).sum()
    sh = [(v[(lr >= lo) & (lr < hi)]**2).sum() / tot for lo, hi in [(-14, -12), (-12, -10), (-10, -8.5), (-8.5, -8), (-8, -4), (-4, 0), (0, 4), (4, 10.01)]]
    print('   |v| %.4e (record v_norm %.4e); |v|^2 share by lr band [-14,-12) [-12,-10) [-10,-8.5) [-8.5,-8) [-8,-4) [-4,0) '
          '[0,4) [4,10]:' % (np.sqrt(tot), R[t]['v_norm']), ' '.join('%.4f' % s for s in sh))
def cmp(a, c, nm):
    x, y = C[a], C[c]
    print('%s vs %s (%s): column values |ca - cc|/|cc| = %.3f, cos %.4f' % (a, c, nm, np.linalg.norm(x - y) / np.linalg.norm(y),
          x @ y / np.linalg.norm(x) / np.linalg.norm(y)))
    for lo, hi, w in [(0, 17, 'rows 0-16'), (17, 37, 'rows 17-36'), (17, 19, 'rows 17-18')]:
        print('   %s: rel diff (to %s) %.3f, (to %s) %.3f, cos %.4f' % (w, c, np.linalg.norm(x[lo:hi] - y[lo:hi]) / np.linalg.norm(y[lo:hi]),
              a, np.linalg.norm(x[lo:hi] - y[lo:hi]) / np.linalg.norm(x[lo:hi]),
              (x[lo:hi] * y[lo:hi]).sum() / np.linalg.norm(x[lo:hi]) / np.linalg.norm(y[lo:hi])))
    va, vc = V[a], V[c]
    for lo, hi in [(-8, -4), (-4, 0), (0, 4), (4, 10.01)]:
        m = (lr >= lo) & (lr < hi)
        print('   v band lr [%g,%g): |va - vc|/|vc| %.3f cos %.4f' % (lo, hi, np.linalg.norm(va[m] - vc[m]) / np.linalg.norm(vc[m]),
              (va[m] * vc[m]).sum() / np.linalg.norm(va[m]) / np.linalg.norm(vc[m])))
rn = [str(s) for s in np.load(P + 'par/%s_J.npz' % tags[-1])['row_names']]
print('row names', rn)
for t in tags:
    print('%s rows 17-36:' % t, ' '.join('%.4f' % z for z in C[t][17:]))
for a, c in [('PLM1e6', 'PLS1e6'), ('PLM1e7', 'PLM1e6'), ('PLM1e7', 'PLS1e7')]:
    if a in C and c in C:
        cmp(a, c, 'same eps' if a[-2:] == c[-2:] else 'two eps')
for t in [t for t in tags if t.startswith('PLM')]:
    print('acceptance, resid_true < 0.1: %s %.4f -> %s' % (t, R[t]['resid_true'], R[t]['resid_true'] < 0.1))
if 'PLM1e6' in C and 'PLM1e7' in C:
    x, y = C['PLM1e6'], C['PLM1e7']
    print('acceptance, eps consistency within 10 %%: rel diff %.3f -> %s' % (np.linalg.norm(x - y) / np.linalg.norm(y), np.linalg.norm(x - y) / np.linalg.norm(y) < 0.1))
