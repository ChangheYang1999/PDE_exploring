"""Format test for vcand.py: rho = x^2 y exp(-r^2) on an exporter-style quarter grid; exact c = 1/8."""
import numpy as np, json, subprocess
N, nq = 512, 129
r = np.exp(np.linspace(np.log(1e-3), np.log(12.0), N))
th = np.linspace(0, np.pi / 2, nq)
X, Y = r[:, None] * np.cos(th), r[:, None] * np.sin(th)
rho = X ** 2 * Y * np.exp(-r[:, None] ** 2)
np.savez('../runs/cand/test_gauss.npz', r=r, theta=th, rho=rho)
from vcand import main
out, ev, ax = main('../runs/cand/test_gauss.npz', dict(Mmax=127, b3=False))
print(json.dumps({k: out[k] for k in ('recon_err_rel', 'top_mode_share', 'c', 'c_l', 'parity_bad')}, default=float))
print('c error', out['c'] - 0.125)
