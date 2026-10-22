"""Linearized analysis of a saved reduced Jacobian (charsolve --save-jac): is the remaining closure defect reducible within the
basis to first order?  For truncation levels k (number of leading singular directions kept), report the least-squares residual of
the linear model |rows + J d_k| / |rows|, the step norm |d_k|, and the predicted regional maxima of the weighted closure rows."""
import sys, json, math, numpy as np
d = np.load(sys.argv[1]); J = d['J']; rows = d['rows']; N = int(d['N']); w = d['w']
U, S, Vt = np.linalg.svd(J, full_matrices=False)
UtR = U.T @ rows
print(f'# {sys.argv[1]}: J {J.shape}, |rows| {np.linalg.norm(rows):.4e} (grid rows {N}, constraint rows {rows.size - N}); singular values: max {S[0]:.3e}, min {S[-1]:.3e}')
print('#  k      s_k        |rows + J d_k|/|rows|   |d_k|      max weighted closure row predicted   (regional r<0.1, 0.1-1, 1-10, 10-1e2, 1e2-1e4, 1e4-1e6, >1e6)')
# regional structure: rows are ordered as the polar grid (Nr x Nth, radius-major); recover radii from the companion state file if given
reg_bins = None
if len(sys.argv) > 2:
    st = np.load(sys.argv[2], allow_pickle=True)
    import torch, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from charlib2 import PsiBasis
    bas = PsiBasis(float(st['beta']), int(st['NO']), int(st['K']), L=float(st['L']))
    Nr, Nth, qmax = int(st['Nr']), int(st['Nth']), float(st['qmax'])
    j = np.arange(Nr); q = qmax * 0.5 * (1 - np.cos(math.pi * (j + 0.5) / Nr)); r = bas.u_of_q(torch.tensor(q)).numpy() * float(st['L'])
    R = np.repeat(r, Nth)
    reg_bins = [(0, 0.1), (0.1, 1), (1, 10), (10, 1e2), (1e2, 1e4), (1e4, 1e6), (1e6, 1e13)]
for k in [0, 10, 20, 50, 100, 200, 300, 400, 500, 600, 700, len(S)]:
    k = min(k, len(S))
    coef = np.zeros_like(S); coef[:k] = UtR[:k] / S[:k]
    dk = -(Vt.T @ coef)
    pred = rows + J @ dk
    line = f'  {k:4d}  {S[k-1] if k > 0 else float("nan"):9.3e}   {np.linalg.norm(pred)/np.linalg.norm(rows):10.4e}   {np.linalg.norm(dk):9.3e}   {np.abs(pred[:N]).max():9.3e}'
    if reg_bins is not None:
        regs = []
        for lo, hi in reg_bins:
            m = (R >= lo) & (R < hi); regs.append(float(np.abs(pred[:N][m]).max()) if m.any() else float('nan'))
        line += '   ' + ' '.join('%.2f' % v for v in regs)
    print(line)
print('# current weighted closure rows: max %.3e' % np.abs(rows[:N]).max())

# ---- irreducible part: residual component orthogonal to the range of J (all directions, and the 700 best-conditioned ones)
print('# residual component orthogonal to range(J): regional maxima of |r_perp| (weighted closure units) and |r_perp|/|rows|')
for k in [700, len(S)]:
    rp = rows - U[:, :k] @ UtR[:k]
    line = f'  k={k:4d}: |r_perp|/|rows| = {np.linalg.norm(rp)/np.linalg.norm(rows):.4f}; max |r_perp| grid {np.abs(rp[:N]).max():.3f}'
    if reg_bins is not None:
        regs = []
        for lo, hi in reg_bins:
            m = (R >= lo) & (R < hi); regs.append(float(np.abs(rp[:N][m]).max()) if m.any() else float('nan'))
        line += '   regional ' + ' '.join('%.2f' % v for v in regs)
    print(line)
# ---- equilibrated view (unit column norms): truncated LS residual vs k
cn = np.sqrt((J * J).sum(0)); cn[cn == 0] = 1.0
Je = J / cn[None, :]
Ue, Se, Vte = np.linalg.svd(Je, full_matrices=False); UtRe = Ue.T @ rows
print('# equilibrated Jacobian: singular values max %.3e min %.3e; truncated LS residual |rows + Je d_k|/|rows| and step norm (coefficient units):' % (Se[0], Se[-1]))
for k in [50, 100, 200, 300, 400, 500, 600, 650, 700, 730, 750, len(Se)]:
    k = min(k, len(Se)); coef = np.zeros_like(Se); coef[:k] = UtRe[:k] / Se[:k]; dk = -(Vte.T @ coef) / cn
    pred = rows + J @ dk
    print('   k=%4d s_k=%.3e  residual %.4f  |d_k| %.3e  max grid row %.3f' % (k, Se[k - 1], np.linalg.norm(pred) / np.linalg.norm(rows), np.linalg.norm(dk), np.abs(pred[:N]).max()))
