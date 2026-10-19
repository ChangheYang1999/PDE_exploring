"""D-free natural-parameter continuation on m1 = 1/2 (notes of the lead analyst 09:48Z 2(b), 10:10Z 2(d); specification M27(g)): for each a_2 in the list run the
dfree=1 fix2=1 exit-map Newton of code/pfwd_bnewton.py (unknowns a_1, a_3..a_K, D, p; rows m1 - 1/2 and the LSQ coefficients of
log Gt - mean - D s(th), s = -(1/2) sin th), warm-started from the previous converged state (B-spline relaxation nsteps_relax steps, then the
safeguarded exit-map polish), and append the full diagnostics (pfwd_diag2) to runs/pfwd/df/<tag>_summary.jsonl.  Stops when min |V|/r < vmin_stop.
Usage: python3 tests/pfwd_dfchain.py tag K Nth g0.npz "a1,...,aK" p0 D0 "a2_1,a2_2,..." [maxit=4] [nsteps0=0] [nsteps_relax=300] [nsteps_J=500]
       [nsteps_T=700] [exit_maxit=25] [lams=0.6,0.3] [vmin_stop=0.05] [lo=-14] [Nr=721] [lr0=-13] [wm=3] [cut=0.02] [h_a=0.01] [h_p=0.004] [dp_max=0.03] [da_max=0.2]"""
import sys, json, math, time, os; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_bnewton import BNewton
from pfwd_diag2 import full_diag, summary_line
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; K = int(sys.argv[2]); Nth = int(sys.argv[3]); g0fn = sys.argv[4]
a0 = [float(v) for v in sys.argv[5].split(',')]; p0 = float(sys.argv[6]); D0 = float(sys.argv[7]); a2s = [float(v) for v in sys.argv[8].split(',')]
opt = dict(maxit=4, nsteps0=0, nsteps_relax=300, nsteps_J=500, nsteps_T=700, exit_maxit=25, exit_tol=2e-5, lams='0.6,0.3', vmin_stop=0.05, lo=-14.0, Nr=721, lr0=-13.0, wm=3.0, cut=0.02,
           h_a=0.01, h_p=0.004, dp_max=0.03, da_max=0.2, mu0=0.01, jac='bs', jac_its=10, broyden_keep=0, wD=0.0, dfree=1, J0='', J0_wD=0.0, J0_wm=0.0)
for s_ in sys.argv[9:]:
    k, v = s_.split('=', 1); opt[k] = v if k in ('lams', 'jac', 'J0') else (int(v) if k in ('maxit', 'nsteps0', 'nsteps_relax', 'nsteps_J', 'nsteps_T', 'exit_maxit', 'Nr', 'jac_its', 'broyden_keep', 'dfree') else float(v))
# dfree=0 (referee recommendation for a candidate search): no D unknown; rows = m1, the 16 RAW LSQ coefficients of log Gt, and the D_ax row (wD): rectangular LM
os.makedirs('runs/pfwd/df', exist_ok=True); os.makedirs('runs/pfwd/bn', exist_ok=True)
summ = open('runs/pfwd/df/%s_summary.jsonl' % tag, 'a')
log = open('runs/pfwd/bn/%s.log' % tag, 'a')
BN = BNewton(K, [], Nr=opt['Nr'], Nth=Nth, lo=opt['lo'], lr0=opt['lr0'], cut=opt['cut'], wm=opt['wm'], nsteps_J=opt['nsteps_J'], nsteps_T=opt['nsteps_T'], h_a=opt['h_a'], h_p=opt['h_p'],
             log=log, tag=tag, exit=1, exit_maxit=opt['exit_maxit'], exit_tol=opt['exit_tol'], dfree=opt['dfree'], fix2=1, exit_safe=1, diag=1, jac=opt['jac'], jac_its=opt['jac_its'], broyden_keep=opt['broyden_keep'], wD=opt['wD'])
n = BN.n
x = np.zeros(n); x[:len(a0)] = a0; x[-1] = p0
if opt['dfree']: x[-2] = D0
if opt['J0']:
    JJ = np.load(opt['J0'], allow_pickle=True)['J']
    if JJ.shape[1] == n + 1 and not opt['dfree']:
        JJ = np.delete(JJ, JJ.shape[1] - 2, axis=1)                                # drop the D column of a dfree Jacobian
    if JJ.shape[0] == n + 1 - (0 if opt['wD'] > 0 else 1) and opt['wD'] > 0 and JJ.shape[0] != 1 + K + 1:
        pass
    assert JJ.shape[1] == n, (JJ.shape, n)
    if opt['J0_wD'] > 0 and opt['wD'] > 0: JJ[-1, :] *= opt['wD'] / opt['J0_wD']       # the saved D_ax row carries the weight it was computed with: rescale to this run's wD
    if opt['J0_wm'] > 0: JJ[0, :] *= opt['wm'] / opt['J0_wm']                           # same for the m1 row
    BN.J_broyden = JJ; BN.broyden_keep = True
    BN.emit(dict(J0=opt['J0'], shape=list(JJ.shape), sv=[float('%.4g' % v) for v in np.linalg.svd(JJ, compute_uv=False)]))
dd = np.load(g0fn, allow_pickle=True); gsrc = dd['g']; asrc = json.loads(str(dd['args'])); p_src = float(asrc['p'])
coef_src = np.array(asrc['par']) if 'par' in asrc else dd['x'][:-1]
if gsrc.shape[1] != Nth:
    assert gsrc.shape[1] % Nth == 0; gsrc = gsrc[:, ::gsrc.shape[1] // Nth]
x_start = np.zeros(n); x_start[:min(len(coef_src), K)] = coef_src[:K]; x_start[-1] = p_src
if opt['dfree']: x_start[-2] = D0
g_start = torch.tensor(gsrc, device='cuda')
BN.emit(dict(chain=tag, K=K, Nth=Nth, g0=g0fn, a2s=a2s, x0=x.tolist(), opt=opt, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
for step, a2 in enumerate(a2s):
    x0 = x.copy(); x0[1] = a2
    BN.tag = '%s_a2%+.3f' % (tag, a2)
    if not (step == 0 and opt['J0']): BN.J_broyden = None           # fresh Jacobian at every a_2 value (kept across the iterations of one value if broyden_keep); J0 used for the first value
    t0 = time.time()
    BN.emit(dict(chain_step=step, a2=a2, x0=[round(float(v), 6) for v in x0], start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    xr, F, info = BN.newton(x0, maxit=opt['maxit'], mu0=opt['mu0'], da_max=opt['da_max'], dp_max=opt['dp_max'], nsteps0=(opt['nsteps0'] if step == 0 else opt['nsteps_relax']),
                            lams=tuple(float(v) for v in opt['lams'].split(',')), g_start=g_start, x_start=x_start)
    g = BN.g_last; x = BN.x_last; info = BN.info_last
    d = full_diag(BN.SB, g, float(x[-1]), np.asarray(x[:K]), Afun=BN.Afun(torch.tensor(np.asarray(x, float)[None], device='cuda')))
    rec = dict(step=step, a2=a2, x=[float(v) for v in x], D_unknown=(float(x[-2]) if opt['dfree'] else None), p=float(x[-1]), normF=info['normF'], F_parts=info.get('F_parts'), R_reduced=info.get('R_reduced'), beta1_raw=info.get('beta1_raw'), m1=info['m1'], exit_defect=info.get('exit_defect'),
               bulk_std=info['bulk_std'], rms_unresolved=info['rms_unresolved'], wall=round(time.time() - t0, 1), diag=d, end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    summ.write(json.dumps(rec) + '\n'); summ.flush()
    print('CHAIN_STEP', step, 'a2', a2, 'normF %.4f R_reduced %s beta1_raw %s m1 %.5f D_unk %s D_div %.4f D_dir %.4f p %.4f Q %.3f min|V|/r %.3f' % (info['normF'], info.get('R_reduced'), info.get('beta1_raw'), info['m1'], ('%.4f' % x[-2]) if opt['dfree'] else 'none', d['D_div'], d['D_dir'], x[-1], d['Q'], d['minVabs_r']), flush=True)
    np.savez('runs/pfwd/df/%s_step%d.npz' % (tag, step), g=g.cpu().numpy(), lr=BN.SB.S.lr.cpu().numpy(), th=BN.SB.S.th.cpu().numpy(), x=x, info=json.dumps(info), diag=json.dumps(d),
             args=json.dumps(dict(p=float(x[-1]), kind='dfchain', par=[float(v) for v in x[:K]], D=(float(x[-2]) if opt['dfree'] else None), a2=a2, dfree=opt['dfree'], wD=opt['wD'])))
    if d['minVabs_r'] < opt['vmin_stop']:
        print('CHAIN_STOP min|V|/r %.4f at (lr %.2f, %.1f deg) below %.3f' % (d['minVabs_r'], d['minVabs_at'][0], d['minVabs_at'][1], opt['vmin_stop']), flush=True); break
    g_start = g; x_start = x.copy()
print('DFCHAIN_DONE', flush=True)
