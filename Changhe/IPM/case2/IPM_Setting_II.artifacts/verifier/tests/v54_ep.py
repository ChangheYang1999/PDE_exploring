"""V54(iii): far-field even axis velocity (specification M25(h), referee result 17): for rho = r^p A_e(th), w_e = e_p r^p with
e_p = -((p+1)/sin(pi p/2)) int_0^{pi/2} A_e(th) cos((p+2) th) dth. Own check on own states: w_e(r) = (W_2(0, r) + W_2(0, -r))/2
(W = U - U(0), code/charsolve.py velocity) from spectral interpolation of W_2 at th = 90 / 270 deg, divided by r^p, against the
formula with A_e the y-even part of the state's own datum (expf basis of tests/fs_run.py, bump / cmode included).
Also the exact axis formula 2 log(kappa_+/kappa_-) = 2n int_0^inf (1/B_- - 1/B_+) dr (B_+(r) = V_2(0, r), B_-(r) = -V_2(0, -r),
n = m2), truncated at r_max, against the axis-law values log k (tests/v50_axis.py). Usage: python3 tests/v54_ep.py STATE.npz"""
import sys, math, json, numpy as np, torch
from scipy.integrate import quad
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]
d = np.load(fn, allow_pickle=True)
args = json.loads(str(d['args']))
p = float(d['p']); nt = len(d['th']); th = d['th']
par = [float(v) for v in args['par'].split(':')]
bump = [float(v) for v in args['bump'].split(':')] if args.get('bump') else None
cm = float(args['cmode']) if args.get('cmode') else 0.0
def A(t):
    f = sum(aj*(np.sin((j + 1)*t) if (j + 1) % 2 == 1 else np.cos((j + 1)*t)) for j, aj in enumerate(par))
    f = f + cm*np.sin(3*t)*np.cos(t)**2
    if bump is not None:
        f = f + bump[0]*np.exp(-(1 + np.sin(t))/bump[2]) + bump[1]*np.exp(-(1 - np.sin(t))/bump[2])
    return np.cos(t)**2*np.exp(f)
Ae = lambda t: 0.5*(A(t) + A(-t))
ep = -(p + 1)/math.sin(math.pi*p/2)*quad(lambda t: Ae(t)*math.cos((p + 2)*t), 0, math.pi/2, limit=400, epsabs=1e-13)[0]
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)),
            q=8, nt=nt, dti=0.01, nstep=10)
rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
nd = F.node(rho); n = nd['m2']; l = F.l
_, _, W1, W2 = F.fields(rho)
W2 = W2.cpu().numpy(); r = F.r.cpu().numpy()
mm = np.fft.fftfreq(nt, 1.0/nt); mm[nt//2] = 0.0
def at(f, ths):
    fh = np.fft.fft(f, axis=1)/nt; fh[:, nt//2] = 0.0
    return np.real(fh @ np.exp(1j*mm*(ths - th[0])))
Wup = at(W2, math.pi/2); Wlo = at(W2, 3*math.pi/2)
we = 0.5*(Wup + Wlo)
Bp = l*r + Wup; Bm = l*r - Wlo                                   # outward axis speeds (V_2(0, -r) = -l r + W_2(0, -r))
rows = []
for lt in (0, 2, 4, 6, 8, 9, 9.9):
    k = int(np.argmin(np.abs(np.log(r) - lt)))
    rows.append([round(float(np.log(r[k])), 3), round(float(we[k]/r[k]**p), 5)])
# paired integral on the Gauss grid (weights S.w), cumulative to r_max; near-node check B_+- ~ n r
w = F.S.w.cpu().numpy()
integ = n*(1/Bm - 1/Bp)
I = float(np.sum(w*integ))
out = dict(state=fn.split('/')[-1], p=p, m1=round(nd['m1'], 6), n=round(n, 6), e_p_formula=round(ep, 6),
           we_over_rp_at_lr=rows, min_Bp_over_r=round(float((Bp/r).min()), 4), min_Bm_over_r=round(float((Bm/r).min()), 4),
           two_log_kappa_ratio_paired_to_rmax=round(2*I, 5))
print(json.dumps(out), flush=True)
# band split of log(kappa_+/kappa_-) = n int (1/B_- - 1/B_+) dr (specification M25(g): +0.84 from r < e^-4, -0.46 from (e^-4, e^2),
# -0.16 from r > e^2 on the lead's state), with the tail beyond r_max from w_e = e_p r^p, b_o = l r
lr = np.log(r); bands = [(-99, -8), (-8, -4), (-4, 2), (2, 99)]
split = {'%g..%g' % b: round(float(np.sum((w*integ)[(lr >= b[0]) & (lr < b[1])])), 4) for b in bands}
R = F.L; tail = 2*n*ep/l**2*R**(p - 1)/(1 - p)
split['tail_beyond_rmax'] = round(tail, 4)
split['log_B+/B-_at_rmax'] = round(float(np.log(Bp[-1]/Bm[-1])), 5)
print(json.dumps(dict(log_kappa_ratio_bands=split, log_kappa_ratio_total_inf=round(float(I) + tail, 5))), flush=True)
