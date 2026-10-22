import sys, numpy as np, torch
sys.path.insert(0, '.')
from charlib import *
from picard import cheb_q_nodes, r_of_q, omega_on_grid
torch.set_num_threads(1)
P, cT, cO_t, NT, NO, K = load_coefs(sys.argv[1])
cO0 = cO_t.numpy().copy()
rr = r_of_q(P, cheb_q_nodes(80, 0.99)); ph = (np.arange(64) + 0.5) * np.pi / 128
scale_r = np.max(np.abs(omega_on_grid(P, cO0, NO, K, rr, ph)), axis=1) + 1e-300
r_t = torch.tensor(rr, dtype=DT)
# fine radial grid between nodes
q = cheb_q_nodes(80, 0.99); qf = np.sort(np.concatenate([q, 0.5 * (q[1:] + q[:-1])]))
rf = r_of_q(P, qf); rf_t = torch.tensor(rf, dtype=DT)
scale_f = np.interp(np.log(rf), np.log(rr), scale_r)
for n in [1, 2, 6, 12, 24]:
    A = radial_basis(P, r_t, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() / scale_r[:, None]
    Af = radial_basis(P, rf_t, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() / scale_f[:, None]
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    # between-node amplification of each right singular vector: |Af v / s| (values per unit y-coordinate)
    amp = np.linalg.norm(Af @ vt.T, axis=0) / s
    print('mode %d: s/s0 at idx 0,10,20,30,40,50,60,last: %s' % (n, ' '.join('%.1e' % (s[i] / s[0]) for i in [0, 10, 20, 30, 40, 50, 60, len(s) - 1])))
    print('        fine-grid norm per unit y at same idx: %s' % ' '.join('%.1e' % amp[i] for i in [0, 10, 20, 30, 40, 50, 60, len(s) - 1]))
print('--- extrapolation beyond q = 0.99 (r > %.1e)' % rr[-1])
qe = np.linspace(0.99, 0.99999, 60); re_ = r_of_q(P, qe); re_t = torch.tensor(re_, dtype=DT)
for n in [1, 2, 6, 12, 24]:
    A = radial_basis(P, r_t, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() / scale_r[:, None]
    Ae = radial_basis(P, re_t, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() / scale_r[-1]
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    amp = np.max(np.abs(Ae @ vt.T), axis=0) / s
    print('mode %d: max extrapolated value per unit y at idx 0,10,20,30,40,50,60,last: %s' % (n, ' '.join('%.1e' % amp[i] for i in [0, 10, 20, 30, 40, 50, 60, len(s) - 1])))
print('r range of grid %.2e .. %.2e' % (rr[0], rr[-1]))
