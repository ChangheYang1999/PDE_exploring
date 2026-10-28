import json, sys, numpy as np
r = json.load(open(sys.argv[1]))
nodes = np.array(r['nodes']); u = np.array(r['u']); lab = np.array(r['labels']); m = np.array(r['masses'])
alpha = r['alpha']; beta = r['beta']; info = r['info']
i0 = info['idx_origin']; i1 = info['idx_e1']
print(f"alpha={alpha} beta={beta:.4f} V_h={r['V_h']:.5f} u(0)={u[i0]:.4f} u(e1)={u[i1]:.4f} N={len(u)}")
ntheta = r['params']['ntheta']; J = info['J']
for (name, center, idx, lo, hi) in [('near e1', np.array([1.0, 0.0]), i1, info['n_near0'], info['n_near0'] + J*ntheta), ('near 0', np.array([0.0, 0.0]), i0, 0, J*ntheta)]:
    print(f"--- {name}: (u - u_center)/rho^alpha by shell (rows: shells j=0 (rho=R) .. ; cols: angles from beta+pi/4)")
    uu = u[lo:hi].reshape(J, ntheta); pp = nodes[lo:hi].reshape(J, ntheta, 2)
    rho = np.sqrt(((pp - center)**2).sum(axis=2))[:, 0]
    for j in list(range(0, min(J, 6))) + list(range(6, J, max(1, J//8))):
        vals = (uu[j] - u[idx])/rho[j]**alpha
        print(f"  rho={rho[j]:.2e}: " + " ".join(f"{v:+.3f}" for v in vals))
# far field
lo = info['n_near0'] + info['n_near1']; hi = lo + info['n_far']
ntf = r['params']['ntheta_f']; Jf = info['Jf']
uf = u[lo:hi].reshape(Jf, ntf); pf = nodes[lo:hi].reshape(Jf, ntf, 2)
rhof = np.sqrt(((pf - np.array([0.5, 0]))**2).sum(axis=2))[:, 0]
print("--- far field: u/rho^alpha by shell about m=e1/2 (cols: angles from 0)")
for j in list(range(0, min(Jf, 5))) + list(range(5, Jf, max(1, Jf//6))):
    print(f"  rho={rhof[j]:.2e}: " + " ".join(f"{v:+.3f}" for v in uf[j]/rhof[j]**alpha))
# contributions by region
for l, name in enumerate(['near0', 'near1', 'far', 'leftover']):
    print(f"  sum m u over {name:8s}: {np.sum(m[lab==l]*u[lab==l]):+.4f}")
