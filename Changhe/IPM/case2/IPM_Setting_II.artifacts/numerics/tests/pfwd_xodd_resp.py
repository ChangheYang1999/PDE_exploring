"""x-odd linear response at an x-even exit-map fixed point (notes of the lead analyst 10:00Z (e), 'smaller first step': frozen zeros at +-pi/2, x-odd F only).
Datum A = cos^2 th exp(F_even + eps phi_odd), phi_odd in {cos th (n=1), cos 3th (n=3), sin 2th (n=2), ...}; the UNPROJECTED exit map (xeven=0, safeguarded
Anderson) is iterated from the x-even fixed point; on the result: x-odd part of g (rms relative to g), the strain matrix DW(0) from the angular modes of
W_r/r and W_th/r on the rings lr = -12 / -10 (alpha_0 + alpha_2 cos 2th + beta_2 sin 2th; gamma_0 = rotation), psi_yy(0) = -beta_2, the Gamma mismatch
(backward orbits from (r_max, 90 deg) and (r_max, 270 deg) to lr0 = -8 and -12: arrival angle minus 90 / 270 in degrees), m1 (core-corrected), c,
and the x-odd part of log Gt (rms over |cos th| > 0.3).  Per eps the responses divided by eps are printed (linear if +-eps agree).
Usage: python3 tests/pfwd_xodd_resp.py state_fp.npz "F1,F3,S2,rot,sq" "eps1,..." [maxit=30] [tag=xodd] [Nth=0 (subsample to)]
   directions: F<n> x-odd log-A mode (odd n: cos n th, even n: sin n th; zeros fixed), rot (both zeros shifted), sq (zeros squeezed toward the right)."""
import sys, json, math, time, os; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_exitmap import ExitMap
from pfwd_bnewton import BNewton
from pfwd_diag2 import full_diag
torch.set_default_dtype(torch.float64)
fn = sys.argv[1]; dirs = sys.argv[2].split(','); epss = [float(v) for v in sys.argv[3].split(',')]
# directions: 'F<n>' = x-odd log-A mode (odd n -> cos n th, even n -> sin n th; zeros fixed); 'rot' = both zeros shifted by eps (datum cos^2(th - eps) e^F);
# 'sq' = zeros moved toward the right half-plane ((cos th - sin eps)^2 e^F); notes of the lead analyst 10:45Z: log-A perturbations cannot move zeros, so the bordered x-odd block needs both kinds
opt = dict(maxit=30, tag='xodd', Nth=0, tol=1e-5, grow=10.0)   # grow: rms growth cap of the safeguard (set large to disable: the fixed-zero x-odd fixed points carry a cusp along Gamma', so the defect grows legitimately)
for s_ in sys.argv[4:]:
    k, v = s_.split('='); opt[k] = v if k == 'tag' else (int(v) if k in ('maxit', 'Nth') else float(v))
d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'])
if opt['Nth'] and g0.shape[1] != opt['Nth']:
    g0 = g0[:, ::g0.shape[1] // opt['Nth']]; th = th[::len(th) // opt['Nth']]
Nr, Nth = g0.shape
os.makedirs('runs/pfwd/xodd', exist_ok=True); logf = open('runs/pfwd/xodd/%s.log' % opt['tag'], 'a')
def log(line):
    print(line, flush=True); logf.write(line + '\n'); logf.flush()
def make_Afun(eps, d):
    def Afun(t):
        F = torch.zeros_like(t)
        for j in range(len(coef)):
            m = j + 1; F = F + float(coef[j]) * (torch.sin(m * t) if m % 2 == 1 else torch.cos(m * t))
        if d.startswith('F'):
            n = int(d[1:]); F = F + eps * (torch.cos(n * t) if n % 2 == 1 else torch.sin(n * t))      # x-odd log-A mode, zeros fixed
            return torch.cos(t) ** 2 * torch.exp(F)
        if d == 'rot':
            return torch.cos(t - eps) ** 2 * torch.exp(F)                                                  # both zeros shifted by eps
        if d == 'sq':
            return (torch.cos(t) - math.sin(eps)) ** 2 * torch.exp(F)                                      # zeros at +-(pi/2 - eps): moved toward the right
        return torch.cos(t) ** 2 * torch.exp(F)
    return Afun
def analyse(EM, g, label):
    S = EM.S; Wr, Wt, rho = EM.velocity(g)
    flip = EM.flip
    godd = 0.5 * (g - g[:, flip]); geven = 0.5 * (g + g[:, flip])
    out = dict(label=label, godd_rel_rms=float(torch.sqrt((godd ** 2).mean() / (geven ** 2).mean())), godd_max_over_rowmax=float((godd.abs() / g.max(dim=1, keepdim=True).values.clamp(min=1e-300)).max()))
    lrn = S.lr.cpu().numpy()
    for L in (-12.0, -10.0):
        i = int(np.argmin(np.abs(lrn - L))); r = float(S.r[i])
        vr = (Wr[0, i] / r).cpu().numpy(); vt = (Wt[0, i] / r).cpu().numpy()
        fr = np.fft.rfft(vr) / Nth; ft = np.fft.rfft(vt) / Nth
        alpha0 = fr[0].real; alpha2 = 2 * fr[2].real; beta2 = -2 * fr[2].imag; gamma0 = ft[0].real
        # W_r/r = alpha0 + alpha2 cos2th + beta2 sin2th (+ higher); DW_11 = alpha0 + alpha2, DW_22 = alpha0 - alpha2, (DW_12 + DW_21)/2 = beta2, (DW_21 - DW_12)/2 = gamma0
        DW12 = beta2 - gamma0; DW21 = beta2 + gamma0
        out['DW_lr%g' % L] = dict(DW11=float(alpha0 + alpha2), DW22=float(alpha0 - alpha2), DW12=float(DW12), DW21=float(DW21), psi_yy0=float(-DW12), psi_xx0=float(DW21), div=float(2 * alpha0), rot=float(gamma0),
                                  resid_rel=float(np.sqrt(np.mean((vr - (alpha0 + alpha2 * np.cos(2 * S.th.cpu().numpy()) + beta2 * np.sin(2 * S.th.cpu().numpy()))) ** 2)) / (np.abs(vr).max() + 1e-300)))
    # Gamma mismatch: backward orbits from the zero angles
    thA = torch.tensor([math.pi / 2, 3 * math.pi / 2], device='cuda')
    for lr0 in (-8.0, -12.0):
        T, u0, w0, th0, it, arrived = EM.SB.trace(Wr, Wt, EM.pB, thA, lr0, dt=0.01, max_it=8000)
        thd = np.degrees(th0[0].cpu().numpy()); out['gamma_mismatch_deg_lr%g' % lr0] = [float(((thd[0] - 90 + 180) % 360) - 180), float(((thd[1] - 270 + 180) % 360) - 180), bool(arrived[0].all())]
    # m1, c, log Gt odd part via BNewton machinery (x-even LSQ basis; only m1 / c / logGt used)
    BN = BNewton(len(coef), [], Nr=Nr, Nth=Nth, lo=float(lr[0]), hi=float(lr[-1]), lr0=-13.0, cut=0.02, wm=3.0, log=None, tag='x')
    BN.Afun = lambda xB: EM.Afun                                  # the perturbed datum (for log A on the fine angles)
    xfull = np.concatenate([coef, [p]])
    F, infos, gg, lg, tm = BN.evaluate(xfull[None], 0, g_given=g[None])
    thA_ = BN.thA.cpu().numpy(); lgv = lg[0]; nA = len(thA_)
    idx_flip = (nA // 2 - np.arange(nA)) % nA
    lodd = 0.5 * (lgv - lgv[idx_flip]); bulk = np.abs(np.cos(thA_)) > 0.3
    msk = np.abs(np.cos(thA_)) > 0.02
    OB = np.stack([np.cos(thA_), np.cos(3 * thA_), np.cos(5 * thA_), np.cos(7 * thA_), np.sin(2 * thA_), np.sin(4 * thA_), np.sin(6 * thA_), np.sin(8 * thA_)], 1)   # x-odd basis
    codd = np.linalg.lstsq(OB[msk], lodd[msk], rcond=None)[0]
    out.update(m1=infos[0]['m1'], c=float(1.0 / p - infos[0]['m1']), logGt_odd_rms_bulk=float(np.sqrt(np.mean(lodd[bulk] ** 2))), logGt_odd_max_bulk=float(np.abs(lodd[bulk]).max()),
               logGt_odd_modes=[float(v) for v in codd], logGt_odd_basis=['cos1', 'cos3', 'cos5', 'cos7', 'sin2', 'sin4', 'sin6', 'sin8'], bulk_std=infos[0]['bulk_std'], normF_even=infos[0]['normF'])
    return out
log(json.dumps(dict(tag=opt['tag'], state=fn, p=p, coef=coef.tolist(), Nr=Nr, Nth=Nth, dirs=dirs, epss=epss, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))))
EM0 = ExitMap(Nr, Nth, float(lr[0]), float(lr[-1]), p, coef, dt=0.01, xeven=False, Afun=make_Afun(0.0, 'F0'))
gbase = torch.tensor(g0, device='cuda')
base = analyse(EM0, gbase, 'base'); log(json.dumps(dict(base=base)))
results = []; cols = {}
for d_ in dirs:
    for eps in epss:
        EM = ExitMap(Nr, Nth, float(lr[0]), float(lr[-1]), p, coef, dt=0.01, xeven=False, Afun=make_Afun(eps, d_))
        t0 = time.time()
        g, Tg, hist = EM.solve_safe(gbase.clone(), maxit=opt['maxit'], tol=opt['tol'], m=6, beta=1.0, log=lambda line: None, grow=opt['grow'], grow_picard=opt['grow'])
        res = analyse(EM, g, '%s_eps%+.3f' % (d_, eps))
        res['polish_hist'] = [[h.get('kind', 's')[0], float('%.3g' % h['defect_max']), float('%.3g' % h['defect_rms']), int(h.get('accepted', True))] for h in hist if not h.get('final')]; res.update(dir=d_, eps=eps, defect_max=hist[-1]['defect_max'], defect_rms=hist[-1]['defect_rms'], converged=bool(hist[-1].get('converged', False)), T_evals=len(hist) - 1, wall=round(time.time() - t0, 1))
        # x-odd response column: (odd log Gt modes, b = psi_yy(0)) / eps   (bordered x-odd block at the x-even base; notes of the lead analyst 10:45Z)
        col = np.array(res['logGt_odd_modes'] + [res['DW_lr-12']['psi_yy0']]) / eps
        res['resp'] = dict(psi_yy0_per_eps=res['DW_lr-12']['psi_yy0'] / eps, gamma_up_per_eps=res['gamma_mismatch_deg_lr-8'][0] / eps, gamma_dn_per_eps=res['gamma_mismatch_deg_lr-8'][1] / eps,
                           godd_per_eps=res['godd_rel_rms'] / eps, dm1_per_eps=(res['m1'] - base['m1']) / eps, logGt_odd_per_eps=res['logGt_odd_rms_bulk'] / eps, column=[float(v) for v in col])
        cols.setdefault(d_, []).append(col)
        log(json.dumps(res)); results.append(res)
        np.savez('runs/pfwd/xodd/%s_%s_eps%+.3f.npz' % (opt['tag'], d_, eps), g=g.cpu().numpy(), lr=lr, th=th, args=json.dumps(dict(p=p, kind='xodd', par=coef.tolist(), dir=d_, eps=eps)), res=json.dumps(res))
print("%-14s %-9s %-5s %-9s %-10s %-10s %-10s %-10s %-10s %-10s" % ('case', 'defect', 'conv', 'godd_rel', 'psi_yy0', 'gam_up-8', 'gam_dn-8', 'dm1', 'lgt_odd', 'c'))
for r in results:
    print("%-14s %-9.2e %-5s %-9.4f %-10.5f %-10.4f %-10.4f %-10.5f %-10.4f %-10.4f" % (r['label'], r['defect_max'], r['converged'], r['godd_rel_rms'], r['DW_lr-12']['psi_yy0'], r['gamma_mismatch_deg_lr-8'][0], r['gamma_mismatch_deg_lr-8'][1], r['m1'] - base['m1'], r['logGt_odd_rms_bulk'], r['c']))
# bordered x-odd block J_odd (rows: 8 odd log Gt modes + b; columns: directions, mean over the eps values) and its singular values
if cols:
    names = list(cols.keys()); J = np.stack([np.mean(cols[k], 0) for k in names], 1)
    U, S_, Vt = np.linalg.svd(J, full_matrices=False)
    rec = dict(J_odd_rows=['cos1', 'cos3', 'cos5', 'cos7', 'sin2', 'sin4', 'sin6', 'sin8', 'b=psi_yy0'], J_odd_cols=names, J_odd=[[float(v) for v in row] for row in J], sv=[float(v) for v in S_],
               smallest_input_sv=float(S_[-1]), smallest_input_vector=dict(zip(names, [float(v) for v in Vt[-1]])), note='numerical observation at one resolution (upper bound on nothing; specification M30 wording)')
    log(json.dumps(rec))
    print('J_odd singular values', ['%.4g' % v for v in S_], 'smallest input sv %.4g' % S_[-1], 'vector', rec['smallest_input_vector'])
print('XODD_DONE')
