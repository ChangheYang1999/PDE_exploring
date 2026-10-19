"""Independent transport residual at the ray-check nodes: R = (c_l X + U_ray) . grad rho - rho with grad rho analytic (src/rayshape.py)
and U_ray from a raycheck JSON; compared with the lead's exported residual and denominator at the same nodes (runs/ray/c6d_nodes.npz).
Usage: python3 src/ray_residual.py <shape.npz> <raycheck.json> <nodes.npz>"""
import sys, json, numpy as np, torch
sys.path.insert(0, 'src')
from rayshape import load_shape, ShapeEval
dev = torch.device('cuda')
shape, jpath, npath = sys.argv[1:4]
P = load_shape(shape); E = ShapeEval(P, dev)
J = json.load(open(jpath)); rows = J['rows']
N = np.load(npath)
X = np.array([[r['x'], r['y']] for r in rows]); U = np.array([r['U_ray'] for r in rows])
rho, fx, fy = E.rho_f(torch.tensor(X[:, 0], device=dev), torch.tensor(X[:, 1], device=dev), want_y=True)
rho, fx, fy = rho.cpu().numpy(), fx.cpu().numpy(), fy.cpu().numpy()
# FD check of rho_y
h = 1e-5 * np.maximum(np.hypot(X[:, 0], X[:, 1]), 1e-2)
rp = E.rho_f(torch.tensor(np.r_[X[:, 0], X[:, 0], X[:, 0], X[:, 0]], device=dev), torch.tensor(np.r_[X[:, 1] + h, X[:, 1] - h, X[:, 1] + 2 * h, X[:, 1] - 2 * h], device=dev))[0].cpu().numpy().reshape(4, -1)
fy_fd = (8 * (rp[0] - rp[1]) - (rp[2] - rp[3])) / (12 * h)
print('rho_y analytic vs FD: max rel %.1e' % (np.abs(fy - fy_fd) / np.maximum(np.abs(fy), 1e-12)).max())
cl = P['c_l']
# lead export values at the nodes (same order as select_targets)
assert np.allclose(N['t_rho_x'], np.array([r['rho_x'] for r in rows])), 'node order mismatch'
print('grad rho vs export: max rel rho_x %.1e, rho_y %.1e, rho %.1e' % (
    (np.abs(fx - N['t_rho_x']) / np.maximum(np.abs(N['t_rho_x']), 1e-12)).max(), (np.abs(fy - N['t_rho_y']) / np.maximum(np.abs(N['t_rho_y']), 1e-12)).max(),
    (np.abs(rho - N['t_rho']) / np.maximum(np.abs(N['t_rho']), 1e-12)).max()))
W1 = cl * X[:, 0] + U[:, 0]; W2 = cl * X[:, 1] + U[:, 1]
R = W1 * fx + W2 * fy - rho
D_lead = N['t_denominator']; R_lead = N['t_residual']
D_mine = cl * np.hypot(X[:, 0], X[:, 1]) * np.hypot(fx, fy) + np.abs(rho)
print('%-9s %-9s | %-12s %-12s %-10s | %-10s %-10s | %-10s' % ('x', 'y', 'R_ray', 'R_lead', 'R diff', 'R/D_lead', 'Rlead/D', 'D_lead/D_mine'))
for i in np.argsort(np.hypot(X[:, 0] - J['xstar'], X[:, 1])):
    print('%-9.4f %-9.4f | %-12.4e %-12.4e %-10.2e | %-10.2e %-10.2e | %-10.3f' % (X[i, 0], X[i, 1], R[i], R_lead[i], R[i] - R_lead[i],
          R[i] / D_lead[i] if D_lead[i] > 0 else float('nan'), R_lead[i] / D_lead[i] if D_lead[i] > 0 else float('nan'), D_lead[i] / D_mine[i]))
ok = D_lead > 0
print('summary: max|R_ray - R_lead| = %.3e; max |R_ray|/D_lead = %.3e (lead %.3e); max |R_ray - R_lead|/D_lead = %.3e' % (
    np.abs(R - R_lead).max(), (np.abs(R[ok]) / D_lead[ok]).max(), (np.abs(R_lead[ok]) / D_lead[ok]).max(), (np.abs(R - R_lead)[ok] / D_lead[ok]).max()))
