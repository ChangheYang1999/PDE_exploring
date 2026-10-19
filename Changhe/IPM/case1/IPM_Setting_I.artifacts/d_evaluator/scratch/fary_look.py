# Far-field N_v next to the y-axis from a resmap window (verifier, verifier): per band of pi/2 - theta, the N_v and N_f maxima,
# |R| and |rho| maxima; the on-axis |R| (zero by symmetry, so it measures the evaluator floor); and N_v of R minus the on-axis
# value of the same radius (a floor-subtracted reading, as in G67 (c)). Usage: python3 fary_look.py tag [tag ...]
import sys, numpy as np
for t in sys.argv[1:]:
    d = np.load('runs/audit/%s_resmap.npz' % t); r, th, R, Nf, Nv, rho = d['r'], d['th'], d['R'], d['Nf'], d['Nv'], d['rho']
    tp = np.pi / 2 - th
    j0 = np.argmin(np.abs(tp)); print(t, 'r %.3g..%.3g, n_r %d, theta step %.5f, on-axis column pi/2 - th %.1e' % (r[0], r[-1], len(r), th[1] - th[0], tp[j0]))
    print('  on-axis |R| max %.2e, |rho| max %.2e, N_v max %.2e' % (np.abs(R[:, j0]).max(), np.abs(rho[:, j0]).max(), Nv[:, j0].max()))
    with np.errstate(all='ignore'):
        V = np.abs(R) / Nv; F = np.abs(R) / Nf; Vs = np.abs(R - R[:, j0:j0 + 1]) / Nv
    for lo, hi in [(1e-6, 0.003), (0.003, 0.006), (0.006, 0.01), (0.01, 0.02), (0.02, 0.05), (0.05, 0.2), (0.2, 1.0), (1.0, 1.6)]:
        j = (tp >= lo) & (tp < hi)
        if not j.any(): continue
        a = np.unravel_index(np.nanargmax(V[:, j]), V[:, j].shape)
        print('  pi/2-th [%.4f, %.4f): N_v max %.3e at r %.4g th %.5f | floor-subtracted %.3e | N_f max %.3e | |R| max %.2e | |R|/(|R_axis| max) %.2f'
              % (lo, hi, np.nanmax(V[:, j]), r[a[0]], th[j][a[1]], np.nanmax(Vs[:, j]), np.nanmax(F[:, j]), np.abs(R[:, j]).max(),
                 np.abs(R[:, j]).max() / np.abs(R[:, j0]).max()))
    for jj in sorted(np.where((tp > 1e-6) & (tp < 0.03))[0], key=lambda k: tp[k])[:12]:
        i = np.nanargmax(V[:, jj])
        print('    tp %.5f  max_r N_v %.3e (r %.4g)  R %.2e  R_axis(r) %.2e  N_v %.2e  floor-subtracted %.3e' % (tp[jj], V[i, jj], r[i], R[i, jj], R[i, j0], Nv[i, jj], Vs[:, jj].max()))
