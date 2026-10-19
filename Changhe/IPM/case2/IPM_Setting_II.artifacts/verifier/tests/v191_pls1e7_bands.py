# V190: anatomy of the numerics PLS1e7 column (slaved datum, b1, eps_rel 1e-6, smoothed, TSVD 0.1; read only):
# band norms of the response v = dg / scale (dg = (g_j - g)/h as stored; clamping at 0 can only affect cells where
# u + h v < 0) and the record of PLF1.out.
import numpy as np, json
P = '../numerics/'
d = np.load(P + 'runs/pfwd/par/PLS1e7_resp_b1.npz'); b = np.load(P + 'runs/pfwd/bn/DR512_a2-1.000_it0.npz')
rec = [json.loads(l)['lin_col'] for l in open(P + 'runs/pfwd/par/PLS1e7.out') if l.startswith('{"lin_col"')][0]
for k in ('eps_rel', 'smooth', 'kang', 'sig_lr', 'tsvd', 'n_kept', 'resid_tsvd', 'resid_true', 'b_norm', 'v_norm', 'defect_of_linear_state', 'dF_norm', 'm1_j', 'psi_yy0_j'):
    print(k, rec[k])
print('H_sv', rec['H_sv'][:6], '...', rec['H_sv'][-3:])
p = json.loads(str(d['info'])).get('p', None) if 'p' in json.loads(str(d['info'])) else None
p = float(json.loads(str(b['args']))['p']) if p is None else p
lr = b['lr']; r = np.exp(lr); scale = (r**2/(1 + r**2))**(1 - p/2)
v = d['dg'].astype(float)/scale[:, None]
g = b['g']; u = g/scale[:, None]
print('p %.6f |v| %.4e (record %.4e) |u| %.4e' % (p, np.linalg.norm(v), rec['v_norm'], np.linalg.norm(u)))
for a, c in [(-14, -12), (-12, -10), (-10, -8), (-8, -4), (-4, 0), (0, 4), (4, 10.01)]:
    m = (lr >= a) & (lr < c)
    print('lr in [%5.1f, %5.1f): |v| %.3e (%.4f of |v|^2), |u| %.3e, |v scale| = |dg| %.3e' % (a, c, np.linalg.norm(v[m]), (v[m]**2).sum()/(v**2).sum(), np.linalg.norm(u[m]), np.linalg.norm(d['dg'][m])))
