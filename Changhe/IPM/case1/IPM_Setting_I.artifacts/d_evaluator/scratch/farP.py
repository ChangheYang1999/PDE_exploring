"""Verifier (verifier), 2026-10-18 shift 6: test of the lead's prediction P (NOTES 18:04:24Z item 2) on a formula-global shape
in the formula-continued convention. Own evaluator (vcand / vresid, k_self tails), own far-field prediction (code/far1_ver.py).
For columns theta_j = 2 pi j / Nt (Nt = 4 (M + 1)) and rows r near the requested multiples of L it prints the signed
R / N_v, its product with r^(1-k), the predicted C(theta_j)/(1+k), and the ratio; also the same with c_l = 1/k (R_k = R +
(1/k - c_l,ev) X.grad rho), since an identity offset delta = c_l,ev - 1/k leaves a constant k delta/(1+k) in R/N_v.
Window: min / max of the ratio over the 11 nodes centred on the row.
Usage: python3 farP.py shape.npz r0 R N nq M out.json
"""
import sys, os, json, subprocess, time
import numpy as np
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE + '/code')
import vcand
from far1_ver import main as far1

shape, r0, R, N, nq, M, outp = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]), sys.argv[7]
t0 = time.time()
tmp = HERE + '/runs/gen4/farP_%d_%s_%s.npz' % (os.getpid(), N, R)
subprocess.run(['python3', HERE + '/code/gen_shape.py', shape, r0, R, N, nq, tmp], check=True)
out, ev, ax = vcand.main(tmp, dict(Mmax=M, k_self=True, b3=False))
os.remove(tmp)
d = np.load(shape, allow_pickle=True)
L = float(d['L']); k = float(d['z'][0])
Nt = out['Nt']
fo, prof = far1(shape, Nt * 16)
Cp = prof['C'][::16] / (1 + k)                     # predicted limit of R/N_v r^(1-k) on the evaluator's columns
r = np.exp(np.linspace(np.log(float(r0)), np.log(float(R)), int(N)))
th = 2 * np.pi * np.arange(Nt) / Nt
cols = sorted(set(int(round(t / (2 * np.pi) * Nt)) for t in
                  (0.1001, 0.3001, 0.6, 0.818, 1.0, 1.2, 1.3999, 1.5, 1.5501, 1.5610, 1.5634, 1.565, 1.5683)))
rows_L = [1e3, 3e3, 4701, 9503, 1e4, 3e4, 1e5, 3e5, 5e5, 1e6, 3e6]
xg = ev.rho_r * r[:, None]                          # X.grad rho
Rk = ev.R + (1 / k - ev.c_l) * xg
absrho = ev.Rnorm - np.abs(xg) - np.abs(ev.Ur * ev.rho_r + ev.Ut * ev.rho_t / r[:, None])
res = dict(file=shape, N=int(N), nq=int(nq), M=M, R=float(R), r0=float(r0), Nt=Nt, k=k, cl_ev=float(ev.c_l), cl_k=1 / k,
           delta=float(ev.c_l - 1 / k), const_offset=float(k * (ev.c_l - 1 / k) / (1 + k)),
           far1=dict(Vr_axis=fo['Vr_axis'], C_axis_over_1pk=fo['C_axis_over_1pk']), rows=[])
for rl in rows_L:
    i = int(np.argmin(np.abs(np.log(r / (rl * L)))))
    if i < 8 or i > len(r) - 9 or abs(np.log(r[i] / (rl * L))) > 0.01:
        continue
    w = slice(i - 5, i + 6)
    for j in cols:
        for lab, RR in (('ev', ev.R), ('1/k', Rk)):
            q = RR[:, j] / ev.Rnorm[:, j]
            s = q * r ** (1 - k)
            rat = s / Cp[j]
            res['rows'].append(dict(r_L=float(r[i] / L), r=float(r[i]), theta=float(th[j]), j=j, cl=lab,
                                    R_over_Nv=float(q[i]), scaled=float(s[i]), pred=float(Cp[j]), ratio=float(rat[i]),
                                    ratio_win=[float(rat[w].min()), float(rat[w].max())],
                                    Nv_over_rho=float(ev.Rnorm[i, j] / absrho[i, j])))
res['t_total'] = time.time() - t0
json.dump(res, open(outp, 'w'), indent=1)
print('cl_ev %.10f 1/k %.10f delta %.3e const %.3e  C_axis/(1+k) %.6e' % (ev.c_l, 1 / k, res['delta'], res['const_offset'],
                                                                         fo['C_axis_over_1pk']))
for x in res['rows']:
    if x['cl'] == 'ev':
        print('r %9.4g L th %.5f  R/Nv %+.4e  scaled %+.4e  pred %+.4e  ratio %+.4f [%+.4f %+.4f]' % (
            x['r_L'], x['theta'], x['R_over_Nv'], x['scaled'], x['pred'], x['ratio'], *x['ratio_win']))
print('t_total %.1f s' % res['t_total'])
