# Near-y-axis residual profile from a resmap (verifier, verifier). Usage: python3 yaxis_look.py tag
import sys, numpy as np
for t in sys.argv[1:]:
    d = np.load('runs/audit/%s_resmap.npz' % t); r, th, R, Nf, Nv, rho = d['r'], d['th'], d['R'], d['Nf'], d['Nv'], d['rho']
    print(t, 'theta step %.5f, n_th %d, max theta %.6f (pi/2 = %.6f)' % (th[1] - th[0], len(th), th.max(), np.pi / 2))
    with np.errstate(all='ignore'):
        F = np.abs(R) / Nf; V = np.abs(R) / Nv
    tp = np.pi / 2 - th
    for lo, hi in [(0, 1e-6), (1e-6, 0.003), (0.003, 0.006), (0.006, 0.012), (0.012, 0.03), (0.03, 0.1), (0.1, 0.5)]:
        j = (tp >= lo) & (tp < hi)
        if not j.any(): continue
        sf = F[:, j]; sv = V[:, j]; a = np.unravel_index(np.nanargmax(sf), sf.shape)
        print('  pi/2 - th in [%.4f, %.4f): N_f max %.3e at r %.3f th %.5f | N_v max %.3e | |R| max %.2e | |rho| max %.2e'
              % (lo, hi, np.nanmax(sf), r[a[0]], th[j][a[1]], np.nanmax(sv), np.abs(R[:, j]).max(), np.abs(rho[:, j]).max()))
    # radial profile at the theta column nearest the axis but not on it
    j = np.where(tp > 1e-6)[0]; j = j[np.argmin(tp[j])]
    i = np.argmax(F[:, j])
    print('  nearest column th %.6f (pi/2 - th %.5f): N_f max %.3e at r %.3f; R %.3e, N_f %.3e, rho %.3e' % (th[j], tp[j], F[i, j], r[i], R[i, j], Nf[i, j], rho[i, j]))
    for jj in sorted(np.where((tp > 1e-6) & (tp < 0.02))[0], key=lambda k: -tp[k])[-8:]:
        print('    th %.5f tp %.5f  max_r N_f %.3e (r %.3f)  R/N_f at r 9.38: %.3e' % (th[jj], tp[jj], F[:, jj].max(), r[np.argmax(F[:, jj])], F[np.argmin(abs(r - 9.382)), jj]))
