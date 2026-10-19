#!/usr/bin/env python3
"""Exit-angle sensitivity of the Gamma-slaved exit map to x-odd state perturbations, as a function of the relative step eps and of the angular resolution.
usage: python3 tests/pfwd_exit_sens.py base.npz Nth tag [polish_its=20] [eps=1e-6,3e-6,...] [dirs=b1rhs,bump_far,bump_inner] [lr_g=-12]
The base (512 angles) is subsampled (Nth | 512) or Fourier-upsampled (Nth > 512) in the angle, re-polished x-even (projected safeguarded Anderson), then for each x-odd direction v
(unit in the solver variable u = g/scale) and each eps the exits th_1, th_2 of the strong manifold at the state u + e v, e = eps |u| / |v|, are recorded together with the band norms
of the finite-difference product (T(g + e v scale) - T(g)) / (e scale).  Output: runs/pfwd/par/<tag>.out (JSON lines) and the polished state runs/pfwd/par/<tag>_base.npz."""
import sys, os, json, math, time, numpy as np, torch
sys.path.insert(0, 'code'); sys.dont_write_bytecode = True
from pfwd_parity import ParityMap, load_base, save_state
fn, Nth, tag = sys.argv[1], int(sys.argv[2]), sys.argv[3]
opt = dict(polish_its=20, eps='1e-6,3e-6,1e-5,3e-5,1e-4,3e-4,1e-3,3e-3,1e-2', dirs='b1rhs,bump_far,bump_inner', lr_g=-12.0, tol=2e-5)
for s_ in sys.argv[4:]:
    k, v = s_.split('=', 1); opt[k] = v if k in ('eps', 'dirs') else (int(v) if k in ('polish_its',) else float(v))
out = open('runs/pfwd/par/%s.out' % tag, 'a')
def log(d): s = json.dumps(d); print(s, flush=True); out.write(s + '\n'); out.flush()
d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'], float)
if a.get('kind') == 'bnewton': coef = coef[:int(a['K'])]
Nth0 = g0.shape[1]
if Nth <= Nth0:
    assert Nth0 % Nth == 0; g0 = g0[:, ::Nth0 // Nth]; how = 'subsampled'
else:
    assert Nth % Nth0 == 0
    G = np.fft.rfft(g0, axis=1); G2 = np.zeros((g0.shape[0], Nth // 2 + 1), complex); G2[:, :G.shape[1]] = G; g0 = np.fft.irfft(G2, n=Nth, axis=1) * (Nth / Nth0); how = 'fourier-upsampled'
g0 = np.maximum(g0, 0.0)
Nr = g0.shape[0]; lo, hi = float(lr[0]), float(lr[-1]); K = 16
F_even = np.zeros(K); F_even[:min(K, len(coef))] = coef[:K]
PM = ParityMap(Nr, Nth, lo, hi, p, F_even, np.zeros(K), xeven=True, lr_g=opt['lr_g']); PM.safe = True
t0 = time.time(); log(dict(tag=tag, base=fn, Nth=Nth, Nr=Nr, how=how, p=p, opt=opt, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
g = torch.tensor(g0, device='cuda')
g, Tg, hist = PM.solve(g, maxit=opt['polish_its'], tol=opt['tol'], log=lambda s_: log(dict(polish=json.loads(s_))))
F, info, lg = PM.rows(g); save_state('runs/pfwd/par/%s_base.npz' % tag, PM, g, PM.get_x(), F, info, lg)
log(dict(polished=True, defect=hist[-1]['defect_max'], defect_rms=hist[-1]['defect_rms'], converged=hist[-1]['converged'], evaluations=hist[-1].get('evaluations'), m1=info['m1'], D_ax=info.get('D_ax'), D_ax_dir=info.get('D_ax_dir'), D_band=info.get('D_band'), psi_yy0=info['psi_yy0'], c=info['c'], normF=info['normF'], R_reduced=info.get('R_reduced'), beta1_raw=info.get('beta1_raw'), F_parts=info.get('F_parts'), exits=[info['exit1_deg'], info['exit2_deg']], minVr_r=info.get('minVr_r'), wall=round(time.time() - t0, 1)))
S = PM.S; u = (g / PM.scale).reshape(-1); un = float(u.norm())
Tg0, info0, THex = PM.T_exit(g); Tu0 = (Tg0 / PM.scale).reshape(-1)
th = S.th[None, :].expand(Nr, Nth); lrm = S.lr[:, None].expand(Nr, Nth)
def odd(v): vm = v.reshape(Nr, Nth); return (0.5 * (vm - vm[:, PM.flip])).reshape(-1)
dirs = {}
dirs['b1rhs'] = odd((Tg0 * torch.cos(THex) / PM.scale).reshape(-1))                                   # analytic datum derivative dT/db_1 (x-odd)
dirs['bump_far'] = odd((u.reshape(Nr, Nth) * torch.cos(th) * torch.exp(-0.5 * (lrm + 2.0) ** 2)).reshape(-1))      # smooth x-odd bump at lr -2
dirs['bump_inner'] = odd((u.reshape(Nr, Nth) * torch.cos(th) * torch.exp(-0.5 * (lrm + 6.0) ** 2)).reshape(-1))    # smooth x-odd bump at lr -6
bands = [(-14, -8), (-8, -6), (-6, -2), (-2, 10.01)]
lrflat = lrm.reshape(-1)
for name in [q for q in opt['dirs'].split(',') if q]:
    v = dirs[name]; vn = float(v.norm()); base = dict(dir=name, v_norm=vn, exits0=[info0['exit1_deg'], info0['exit2_deg']])
    log(base)
    for eps in [float(q) for q in opt['eps'].split(',')]:
        e = eps * un / vn
        gp = (u + e * v).reshape(Nr, Nth) * PM.scale
        Tgp, infop, THp = PM.T_exit(gp)                                                                 # unprojected map with the exit angles in info and the per-cell exit angles THp
        prod = ((Tgp / PM.scale).reshape(-1) - Tu0) / e
        bn = {('%g_%g' % b): float(prod[(lrflat >= b[0]) & (lrflat < b[1])].norm()) for b in bands}
        pe = float((prod - odd(prod)).norm() / max(float(prod.norm()), 1e-300))
        dTH = torch.rad2deg(torch.remainder(THp - THex + math.pi, 2 * math.pi) - math.pi).abs().reshape(-1)        # change of the forward-orbit exit angle per cell (deg)
        qs = [0.5, 0.9, 0.99, 0.999, 1.0]; quant = {}
        for b in bands:
            m = (lrflat >= b[0]) & (lrflat < b[1]); dq = dTH[m]
            quant['%g_%g' % b] = [float(torch.quantile(dq, q)) if q < 1.0 else float(dq.max()) for q in qs]
            quant['%g_%g_switched' % b] = int((dq > 90.0).sum())                                                  # cells whose exit moved by more than 90 deg (branch switch)
        log(dict(dir=name, eps=eps, exit1=infop['exit1_deg'], exit2=infop['exit2_deg'], dth1=infop['exit1_deg'] - info0['exit1_deg'], dth2=infop['exit2_deg'] - info0['exit2_deg'],
                 dth1_per_eps=(infop['exit1_deg'] - info0['exit1_deg']) / eps, gamma_ok=infop.get('gamma_ok'), unfinished=infop.get('unfinished'), prod_bands=bn, prod_norm=float(prod.norm()), prod_even_frac=pe,
                 exit_change_quantiles_deg=dict(quantiles=qs, bands=quant), wall=round(time.time() - t0, 1)))
log(dict(done=True, wall=round(time.time() - t0, 1)))
