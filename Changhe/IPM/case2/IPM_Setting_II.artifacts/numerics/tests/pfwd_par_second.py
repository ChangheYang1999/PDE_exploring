#!/usr/bin/env python3
"""Second-order quantities of the parity-free functional from saved nsolve states (lead 18:18Z; V185; referee audit).
usage: python3 tests/pfwd_par_second.py <base_out.log or .out with the base record> <state_plus.npz> <state_minus.npz>
The state files are written by code/pfwd_parity.py mode=nsolve (keys F, x, info, args with tamp, sign, vdir).  Prints per row q_k = (F_k(+) + F_k(-) - 2 F_k(0)) / (2 t^2),
a_k = (F_k(+) - F_k(-)) / (2 t), the full-functional curvature vHv = (f(+) + f(-) - 2 f(0)) / (2 t^2) with f = |F|^2, |F_o(+-)|^2 / t^2 (estimates |J_oo v|^2),
2 sum_k F_e,k(0) q_k, and the same for the info quantities m1, m1_true, D_ax, D_ax_dir, M_up, M_dn, psi_yy0, D_band; plus the convergence records of the two states."""
import sys, json, numpy as np
base_log, fp, fm = sys.argv[1:4]
Fb = None
for line in open(base_log):
    if '"base": true' in line:
        d = json.loads(line); Fb = np.array(d['F'], float); infob = d['info']; break
assert Fb is not None, 'no base record in ' + base_log
def load(fn):
    d = np.load(fn, allow_pickle=True); a = json.loads(str(d['args'])); info = json.loads(str(d['info']))
    return np.array(d['F'], float), a, info
Fp, ap, ip = load(fp); Fm, am, im = load(fm)
t = float(ap['tamp']); assert abs(float(am['tamp']) - t) < 1e-12 and ap['sign'] > 0 and am['sign'] < 0, (ap.get('tamp'), am.get('tamp'), ap.get('sign'), am.get('sign'))
assert np.allclose(ap['vdir'], am['vdir']), 'different directions'
v = np.array(ap['vdir'], float); K = 16
names = ['m1'] + ['a%d' % (j + 1) for j in range(K)] + ['b%d' % (j + 1) for j in range(K)] + ['D_ax', 'M_up', 'M_dn', 'psi_yy0'] + (['G_up', 'G_dn'] if len(Fb) > 37 else [])
odd = np.array([n.startswith('b') or n in ('M_up', 'M_dn', 'psi_yy0', 'G_up', 'G_dn') for n in names]); even = ~odd
q = (Fp + Fm - 2 * Fb) / (2 * t ** 2); a = (Fp - Fm) / (2 * t)
f0 = float(Fb @ Fb); fpl = float(Fp @ Fp); fmi = float(Fm @ Fm)
print('direction v (nonzero):', {names[j]: round(float(v[j]), 4) for j in range(len(v)) if v[j] != 0}, ' |v| %.4f  t %.4g' % (np.linalg.norm(v), t))
print('convergence: + state exit_defect %s converged %s merit %s | - state exit_defect %s converged %s merit %s' % (ip.get('exit_defect'), ip.get('exit_converged'), ip.get('merit'), im.get('exit_defect'), im.get('exit_converged'), im.get('merit')))
print('x-odd rms of the states: + %.4g  - %.4g ; exits + %s  - %s' % (ip.get('godd_rel_rms', float('nan')), im.get('godd_rel_rms', float('nan')), [round(ip['th1_deg'], 3), round(ip['th2_deg'], 3)], [round(im['th1_deg'], 3), round(im['th2_deg'], 3)]))
print('f(0) %.6f  f(+t) %.6f  f(-t) %.6f   vHv_from_f = %.5f   f_odd_part (f(+)-f(-))/(2t) = %.5f' % (f0, fpl, fmi, (fpl + fmi - 2 * f0) / (2 * t ** 2), (fpl - fmi) / (2 * t)))
print('|F_o(+)|^2/t^2 %.5f  |F_o(-)|^2/t^2 %.5f  (estimate |J_oo v|^2);  2 sum_k F_e,k(0) q_k = %.5f ;  |F_e(0)|^2 %.5f' % ((Fp[odd] ** 2).sum() / t ** 2, (Fm[odd] ** 2).sum() / t ** 2, 2 * (Fb[even] * q[even]).sum(), (Fb[even] ** 2).sum()))
print('check: vHv_from_f - [ |F_o|^2/t^2 (mean of signs) + 2 sum F_e q ] = %.5f (should be O(t^2))' % ((fpl + fmi - 2 * f0) / (2 * t ** 2) - (0.5 * ((Fp[odd] ** 2).sum() + (Fm[odd] ** 2).sum()) / t ** 2 + 2 * (Fb[even] * q[even]).sum())))
print('%-8s %12s %12s %12s %12s %12s' % ('row', 'F(0)', 'F(+t)', 'F(-t)', 'q', 'a'))
for n, f0k, fpk, fmk, qk, ak in zip(names, Fb, Fp, Fm, q, a):
    print('%-8s %12.6f %12.6f %12.6f %12.5f %12.5f' % (n, f0k, fpk, fmk, qk, ak))
print('info quantities (unweighted): q = (x(+) + x(-) - 2 x(0)) / (2 t^2), a = (x(+) - x(-)) / (2 t)')
for k in ('m1', 'm1_true', 'c', 'D_ax', 'D_ax_dir', 'M_up', 'M_dn', 'psi_yy0', 'D_band', 'rms_unresolved', 'bulk_std'):
    if k in ip and k in im and k in infob:
        print('  %-14s x0 %12.6f  x+ %12.6f  x- %12.6f  q %12.5f  a %12.5f' % (k, infob[k], ip[k], im[k], (ip[k] + im[k] - 2 * infob[k]) / (2 * t ** 2), (ip[k] - im[k]) / (2 * t)))
