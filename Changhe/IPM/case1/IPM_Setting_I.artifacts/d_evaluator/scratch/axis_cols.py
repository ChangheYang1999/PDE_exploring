"""Verifier scratch (shift 6): the residual on the columns next to the y-axis (c6h whole-box N_f question). The formula is
sampled by code/gen_shape.py (formula continued, no closure) and evaluated by vcand (cfg as the row audits: Mmax only); N_f and
N_v as in code/vaudit.py. For the columns theta_j = pi/2 - s * 2 pi / Nt, s = 1 .. 24, it prints the maxima over r in
[ra, rb] of |R| / N_f and |R| / N_v with their radii; on a smooth field |R| / N tends to a finite limit at the axis
(R, N_f and N_v are O(x^2) there by the parity of rho, psi and U).
With AXC_SIDE=x in the environment the columns are theta_j = s * 2 pi / Nt next to the x-axis instead (R, N_f, N_v are O(y)
there by parity; no cancellation floor, since every sine mode vanishes on the x-axis).
Usage: python3 axis_cols.py shape.npz N nq M out.json [ra rb]"""
import sys, os, json, subprocess, time
import numpy as np
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE + '/code')
import vcand
shape, N, nq, M, outp = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
ra, rb = (float(sys.argv[6]), float(sys.argv[7])) if len(sys.argv) > 7 else (1.0, 20.0)
t0 = time.time()
tmp = HERE + '/runs/gen4/axc_%d_%s_%s.npz' % (os.getpid(), N, nq)
subprocess.run(['python3', HERE + '/code/gen_shape.py', shape, '7.652e-4', '7.652e6', N, nq, tmp], check=True)
out, ev, ax = vcand.main(tmp, dict(Mmax=M, b3=False))
d, g, ms, F = vcand.load_modes(tmp, M)
os.remove(tmp)
Nt = out['Nt']
th = 2 * np.pi * np.arange(Nt) / Nt
r = g.r
sel = (r >= ra) & (r <= rb)
rows = []
for s in range(1, 25):
    j = s if os.environ.get('AXC_SIDE') == 'x' else Nt // 4 - s
    t = th[j]
    rho = F[sel] @ np.sin(ms * t)
    ct, st = np.cos(t), np.sin(t)
    R = ev.R[sel, j]
    rr = r[sel]
    rx = ct * ev.rho_r[sel, j] - st * ev.rho_t[sel, j] / rr
    ry = st * ev.rho_r[sel, j] + ct * ev.rho_t[sel, j] / rr
    U1 = ev.Ur[sel, j] * ct - ev.Ut[sel, j] * st
    U2 = ev.Ur[sel, j] * st + ev.Ut[sel, j] * ct
    W1, W2 = ev.c_l * rr * ct + U1, ev.c_l * rr * st + U2
    Nf = np.abs(W1 * rx) + np.abs(W2 * ry) + np.abs(rho)
    ef, evv = np.abs(R) / Nf, np.abs(R) / ev.Rnorm[sel, j]
    i, iv = int(np.argmax(ef)), int(np.argmax(evv))
    rows.append(dict(s=s, dtheta=float(t if os.environ.get('AXC_SIDE') == 'x' else np.pi / 2 - t), Nf_max=float(ef[i]), Nf_r=float(rr[i]), Nv_max=float(evv[iv]),
                     Nv_r=float(rr[iv]), R_over_rho_at_Nf=float(R[i] / rho[i])))
res = dict(side=os.environ.get('AXC_SIDE', 'y'), file=shape, N=int(N), nq=int(nq), M=M, Nt=Nt, c_l=float(ev.c_l), ra=ra, rb=rb, rows=rows, t_total=time.time() - t0)
json.dump(res, open(outp, 'w'), indent=1)
print('%s N %s nq %s M %d Nt %d c_l %.10f  r in [%g, %g]' % (shape.split('/')[-1], N, nq, M, Nt, ev.c_l, ra, rb))
for x in rows:
    print('  s %2d  dtheta %.5f  N_f %.4e at r %.4f   N_v %.4e at r %.4f   R/rho %+.3e' % (
        x['s'], x['dtheta'], x['Nf_max'], x['Nf_r'], x['Nv_max'], x['Nv_r'], x['R_over_rho_at_Nf']))
print('t_total %.1f s' % res['t_total'])
