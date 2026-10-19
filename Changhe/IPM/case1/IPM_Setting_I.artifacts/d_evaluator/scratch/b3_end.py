import sys
exec(open('scratch/b3_clean_run.py').read().split("res = {}")[0])
from scipy.special import roots_jacobi
be2 = 2 / A
out = {}
for name, qf, xx in (('mine', q_my, xs), ('lead_pipeline', q_ld, d.xs)):
    print(name)
    vals = []
    for (u_lo, uc, K) in ((0.03, 0.3, 6), (0.04, 0.3, 6), (0.04, 0.4, 6), (0.06, 0.4, 7), (0.04, 0.4, 8), (0.06, 0.5, 7)):
        row = []
        for ue, uf, ux, dE in ((0.95, 0.88, 0.95, 1), (0.95, 0.88, 0.955, 2), (0.94, 0.9, 0.95, 1), (0.96, 0.9, 0.96, 2),
                               (0.95, 0.94, 0.95, 0), ('lead', 0, 0, 0)):
            if ue == 'lead':
                # [0.95, 1] with the lead pipeline's own phi at Gauss-Jacobi nodes (their regularization next to x*)
                o = fp_clean(qf, xx, p3, be2, u_lo, uc, K, 0.95, 0.88, 0.95, 1)
                tj, wj = roots_jacobi(80, be2 - 1, 0.0)
                uu = 0.95 + 0.05 * (tj + 1) / 2
                phl = q_ld(d.xs * uu) * (1 - uu) ** (1 - be2)
                endl = float((0.05 / 2) ** be2 * np.sum(wj * uu ** (1 - p3) * phl))
                row.append(o['B'] - o['endp'] + endl)
            else:
                row.append(fp_clean(qf, xx, p3, be2, u_lo, uc, K, ue, uf, ux, dE)['B'])
        vals += row
        print('  u_lo %.2f uc %.1f K %d:' % (u_lo, uc, K), ' '.join('%.4f' % v for v in row))
    print('  range %.4f .. %.4f median %.4f' % (min(vals), max(vals), np.median(vals)))
    out[name] = vals
