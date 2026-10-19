"""Test of vcand.d10: for any field, Q3 - (c_l - 1) pi c = -int phi R dX with R = W.grad rho - rho, phi = sin(3t) r^-3.
The right side is computed from the residual array directly (independent of the Q3 quadrature)."""
import numpy as np, json, sys
from scipy.integrate import simpson
import vcand
path = sys.argv[1] if len(sys.argv) > 1 else '../runs/cand/test_gauss.npz'
Mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 63
out, ev, ax = vcand.main(path, {'Mmax': Mmax, 'b3': False})
g = vcand.LogGrid(out['N'], out['r0'], out['R'])
r = g.r
Nt = out['Nt']
th = 2 * np.pi * np.arange(Nt) / Nt
prof = (np.sin(3 * th)[None, :] * ev.R / r[:, None]).sum(1) * (2 * np.pi / Nt)
lhs = out['D10']['Q3'] - out['D10']['Q3_target']
rhs = -simpson(prof, x=np.log(r))
print(json.dumps(dict(D10=out['D10'], lhs=lhs, rhs=float(rhs), rel=float(abs(lhs - rhs) / abs(out['D10']['Q3_target'])),
                      c=out['c'], c_l=out['c_l']), indent=1))
