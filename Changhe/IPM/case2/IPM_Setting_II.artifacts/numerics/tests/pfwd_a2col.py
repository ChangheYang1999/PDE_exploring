"""Constrained axis derivative dD_ax/da_2 along the corrected branch (referee audit, item 5; lead 15:02Z item 3).
Given a saved exit-map Jacobian J1 (rows: m1 x wm, LSQ C_1..C_K, [D_ax x wD]; columns: a_1..a_K, [D], p; a_2 column zero) and the base state file, compute the
a_2 column by one re-converged fixed point at a_2 + h (safeguarded polish from the rescaled base) and form, with H = (m1 row, C_2..C_K) (the physical block
without the sin th row) and B = D_u H over u = (a_1, a_3..a_K, p):  dd/dt = d_t - d_u B^{-1} H_t  (t = a_2), where d = D_ax (unweighted) and the m1 row is
unweighted as well.  Reports the a_2 column (with the polish defect), dD_ax/da_2 (constrained and unconstrained), dm1/da_2, and B's singular values.
Usage: python3 tests/pfwd_a2col.py J1.npz base_state.npz K Nth wm wD [h=0.02] [jac_its=15] [dfree=1]"""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_bnewton import BNewton
torch.set_default_dtype(torch.float64)
Jf, bf, K, Nth, wm, wD = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
opt = dict(h=0.02, jac_its=15, dfree=1)
for s_ in sys.argv[7:]:
    k, v = s_.split('='); opt[k] = int(v) if k in ('jac_its', 'dfree') else float(v)
JJ = np.load(Jf, allow_pickle=True); J = JJ['J']; xJ = JJ['x']
d = np.load(bf, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = float(a['p'])
if g0.shape[1] != Nth: g0 = g0[:, ::g0.shape[1] // Nth]
BN = BNewton(K, [], Nr=g0.shape[0], Nth=Nth, lo=float(lr[0]), hi=float(lr[-1]), lr0=-13.0, cut=0.02, wm=wm, log=None, tag='a2col', exit=1, exit_maxit=opt['jac_its'], dfree=opt['dfree'], fix2=1, wD=wD, exit_safe=1)
x = np.asarray(xJ, float); n = len(x); assert n == BN.n, (n, BN.n)
g = torch.tensor(g0, device='cuda')
F0, inf0, gg, lg, tm = BN.evaluate(x[None], 0, g_given=g[None]); F0 = F0[0]
xj = x.copy(); xj[1] += opt['h']
Fs, infs, gs, lgs, tms = BN.evaluate(xj[None], 0, g_start=g, x_start=x, want_axis=False)       # rescaled base as the start
gj, eh = BN.exit_polish(xj, gs[0], maxit=opt['jac_its'])
Fj, infj, ggj, lgj, tmj = BN.evaluate(xj[None], 0, g_given=gj[None]); Fj = Fj[0]
col = (Fj - F0) / opt['h']
print(json.dumps(dict(a2_column=[float('%.5g' % v) for v in col], polish_defect_max=eh[-1]['defect_max'], polish_defect_rms=eh[-1]['defect_rms'], base_m1=inf0[0]['m1'], pert_m1=infj[0]['m1'],
                      dm1_da2=(infj[0]['m1'] - inf0[0]['m1']) / opt['h'], base_Dax=inf0[0].get('D_ax_div'), pert_Dax=infj[0].get('D_ax_div'))))
# constrained derivative: unknowns u = (a_1, a_3..a_K, p) -> column indices
jD = (n - 2) if opt['dfree'] else None
ucols = [j for j in range(n) if j != 1 and j != jD]
rows_H = [0] + list(range(2, 1 + K))                 # m1 row and C_2..C_K (sin th row excluded)
B = J[np.ix_(rows_H, ucols)].copy(); B[0, :] /= wm; Ht = col[rows_H].copy(); Ht[0] /= wm
sv = np.linalg.svd(B, compute_uv=False)
if wD > 0:
    d_u = J[-1, ucols] / wD; d_t = col[-1] / wD
    dd_dt = d_t - d_u @ np.linalg.solve(B, Ht)
    print(json.dumps(dict(dDax_da2_unconstrained=float(d_t), dDax_da2_constrained=float(dd_dt), dDax_du=[float('%.4g' % v) for v in d_u], B_sv=[float('%.4g' % v) for v in sv], note='constrained = along the branch where m1 and C_2..C_K are held fixed to first order (referee audit, item 5); valid only if the column polishes are converged')))
else:
    print(json.dumps(dict(B_sv=[float('%.4g' % v) for v in sv], note='no D_ax row in this Jacobian: only dm1/da2 and the a_2 column reported')))
