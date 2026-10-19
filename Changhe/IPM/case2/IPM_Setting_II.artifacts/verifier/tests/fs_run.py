"""Driver for code/fwdstat.py (independent forward-route stationary solver). key=value arguments:
p, kind (cos2|cosk|plateau|rhoa|expsin3|expf), par (expf: colon list a1:a2:...), ppu, nt, nstep, tmin, tmax, dti, iters, init (npz: lead/numerics format g, lr, th
or own format rho, r, th, p), bump (V52, 'bl:bu:w': log A += bl exp(-(1 + sin)/w) + bu exp(-(1 - sin)/w), the lead's zero-window
bumps at 270 / 90 deg, explore/fpnloc.py), cmode (V52(d), 'a': log A += a sin 3th cos^2 th, a sin 3th compensator that vanishes
to second order at the zeros), out (npz), beta (mixing), mand (Anderson depth), dT (> 0: pseudo-time map T_partial with advance dT
in log r instead of the full exit map), polish (full-map Anderson iterations after a dT run), aerr (Anderson only once the max fixed-point defect is below aerr;
plain damped Picard above), smode (1: arclength orbits, V_r <= 0 lobes allowed; hs step, nmax steps; V74), xsym (1: x-even projection of the exit
map, V79; for x-even data). SUMMARY reports err_fullT.
Initial state: g = rho/r^p interpolated from init (cubic spline in log r, clamped beyond the init range; periodic cubic
in theta), rho = 0 inside the init range's inner radius."""
import sys, time, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
a = dict(p='0.5', kind='cos2', par='0', ppu='3', nt='128', nstep='400', tmin='-12', tmax='10', dti='0.01', iters='15',
         init='', out='', bump='', cmode='', beta='1.0', mand='6', dT='0', polish='0', aerr='inf', smode='0', hs='0.03',
         nmax='6000', xsym='0')
for s in sys.argv[1:]:
    k, v = s.split('=', 1); a[k] = v
p = float(a['p']); kind = a['kind']
par = [float(v) for v in a['par'].split(':')] if kind == 'expf' else float(a['par'])
bump = [float(v) for v in a['bump'].split(':')] if a['bump'] else None
cmode = float(a['cmode']) if a['cmode'] else 0.0
def Afun(t):
    A0 = Afun0(t)*np.exp(cmode*np.sin(3*t)*np.cos(t)**2)
    if bump is None: return A0
    s = np.sin(t); bl, bu, w = bump
    return A0*np.exp(bl*np.exp(-(1 + s)/w) + bu*np.exp(-(1 - s)/w))
def Afun0(t):
    c, s = np.cos(t), np.sin(t)
    if kind == 'cos2': return c**2
    if kind == 'cosk': return np.abs(c)**par
    if kind == 'plateau': return np.tanh(par*c**2)/math.tanh(par)
    if kind == 'rhoa': return c**2*(1 + par*s)**2
    if kind == 'expsin3': return c**2*np.exp(-par*np.sin(3*t))     # numerics A_b (notes to the lead analyst 23:52Z)
    if kind == 'expf':                                                # cos^2 exp(sum a_j phi_j), phi = sin t, cos 2t, sin 3t, ...
        f = np.zeros_like(t)
        for j, aj in enumerate(par):
            n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
        return c**2*np.exp(f)
    raise ValueError(kind)
t0 = time.time()
F = FwdStat(p, Afun, tmin=float(a['tmin']), tmax=float(a['tmax']), ppu=int(a['ppu']), q=8, nt=int(a['nt']),
            dti=float(a['dti']), nstep=int(a['nstep']))
if a['smode'] == '1': F.smode = True; F.hs = float(a['hs']); F.nmax = int(a['nmax'])      # V74: arclength orbits
if a['xsym'] == '1': F.xsym = True                                                         # V79: x-even projection
d = np.load(a['init'])
if 'g' in d.files:
    g0, lr0, th0 = d['g'], d['lr'], d['th']
else:
    p0 = float(d['p']); r0 = d['r']; th0 = d['th']; g0 = d['rho']/r0[:, None]**p0; lr0 = np.log(r0)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
if len(th0) != len(thn) or not np.allclose(th0, thn):
    th_ext = np.concatenate([th0, [2*math.pi]]); G_ext = np.concatenate([G, G[:, :1]], 1)
    G = CubicSpline(th_ext, G_ext, axis=1, bc_type='periodic')(thn)
G[lrr < lr0[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=torch.float64, device='cuda')
print(json.dumps(dict(args=a, Nr=F.S.Nr, L=F.L)), flush=True)
dT = float(a['dT'])
rho2, hist = F.solve(rho, iters=int(a['iters']), tol=1e-10, m_and=int(a['mand']), beta_mix=float(a['beta']), verbose=True,
                     dT=dT if dT > 0 else None, aerr=float(a['aerr']))
if dT > 0 and int(a['polish']) > 0:                              # full exit-map Anderson polish; solve() keeps the best iterate
    try:
        rho2, hist2 = F.solve(rho2, iters=int(a['polish']), tol=1e-10, m_and=int(a['mand']), beta_mix=float(a['beta']), verbose=True)
        hist = hist + [dict(phase='polish')] + hist2
    except RuntimeError as e:
        print(json.dumps(dict(polish_failed=str(e)[:40])), flush=True)
try:                                                             # residual of the full exit map at the returned state
    Tr, _ = F.T(rho2); err_full = float(((Tr - rho2)/F.R**p).abs().max())
except RuntimeError:
    err_full = None
nd = F.node(rho2)
last = [h for h in hist if 'm1' in h][-6:]                      # restart records (code/fwdstat.py) carry no m1
summ = dict(final=nd, m1_last6=[h['m1'] for h in last], err_last6=[h['err'] for h in last],
            m1_spread=max(h['m1'] for h in last) - min(h['m1'] for h in last), err_fullT=err_full, ident=F.identities(rho2, nd['m1']),
            wall=time.time() - t0)
print('SUMMARY ' + json.dumps(summ), flush=True)
if a['out']:
    np.savez(a['out'], rho=rho2.cpu().numpy(), r=F.r.cpu().numpy(), th=F.th.cpu().numpy(), p=p, args=json.dumps(a),
             hist=json.dumps(hist))
