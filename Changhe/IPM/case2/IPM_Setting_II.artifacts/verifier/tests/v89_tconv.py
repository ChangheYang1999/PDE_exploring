"""V89 (lead team notes 08:14Z item 3: the lead's exact image of my a_2 -1.2 state has dm1 -0.0029, all at the slow window):
convergence of my exit map T in its own discretisation parameters on an own-format fixed point. For (hs, dti) in (0.03, 0.01)
[the solver's], (0.015, 0.01), (0.03, 0.005), (0.015, 0.005): dm1 = m1(T rho) - m1(rho) (my moment), its band split (T rho
substituted on one t band only), and max |log(T rho / rho)| on the slow upper window (80-100 deg) and elsewhere, by band, over
points with g > 1e-3 ring max.
Usage: python3 tests/v89_tconv.py OWN.npz"""
import sys, math, json, time, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p'])
par = [float(v) for v in args['par'].split(':')]
def A(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)
nt = len(d['th']); t0 = time.time()
bands = ((-20, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 10))
for hs, dti in ((0.03, 0.01), (0.015, 0.01), (0.03, 0.005), (0.015, 0.005)):
    F = FwdStat(p, A, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=dti, nstep=800)
    assert np.allclose(F.r.cpu().numpy(), d['r'])
    F.smode = True; F.hs = hs; F.nmax = int(8000*0.03/hs); F.xsym = bool(int(args.get('xsym', 0)))
    rho = torch.tensor(d['rho'], dtype=DT, device='cuda'); Rp = F.R**p
    Tr, _ = F.T(rho); m1s = F.node(rho)['m1']
    t = F.t_nodes[:, None].expand_as(F.R); deg = torch.rad2deg(F.TH)
    rec = dict(hs=hs, dti=dti, m1=round(m1s, 6), dm1=float('%.3g' % (F.node(Tr)['m1'] - m1s)),
               defect=float('%.3g' % float(((Tr - rho)/Rp).abs().max())))
    sp = {}; mx = {}
    rm = rho.abs().amax(1, keepdim=True); ok = rho.abs() > 1e-3*rm
    with torch.no_grad():
        lg = torch.where(ok, torch.log(torch.abs(Tr/rho)), torch.zeros_like(rho))
    win = (deg >= 80) & (deg <= 100)
    for lo, hi in bands:
        msk = (t >= lo) & (t < hi)
        sp['%g..%g' % (lo, hi)] = float('%.2g' % (F.node(torch.where(msk, Tr, rho))['m1'] - m1s))
        mx['%g..%g' % (lo, hi)] = [float('%.2g' % float(lg[msk & win].abs().max())), float('%.2g' % float(lg[msk & ~win].abs().max()))]
    rec['dm1_band'] = sp; rec['maxlog_win80-100_rest'] = mx; rec['wall'] = round(time.time() - t0, 1)
    print(json.dumps(rec), flush=True)
