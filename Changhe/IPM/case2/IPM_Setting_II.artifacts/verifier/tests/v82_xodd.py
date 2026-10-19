"""V82 (lead team notes 07:50Z item 5(b)): leading x-odd eigenvalue of DT, the derivative of my exit map (code/fwdstat.py, arclength
orbits, NO x-even projection) at an x-even fixed point rho* (own format: rho, r, th, p, args). For x-even data T commutes with the
reflection th -> pi - th, so DT preserves parity, and the odd part of T(rho* + eps d) is eps DT d + O(eps^3) for odd d. Power
iteration: d_0 = rho* cos th (x-odd), d_{k+1} = odd(T(rho* + eps d_k) - T(rho*)) / eps, normalised each step (norm: Frobenius norm
of d / r^p on my grid). Printed per step: ratio |d_{k+1}| / |d_k|, the Rayleigh quotient <d_{k+1}, d_k> / <d_k, d_k>, and the x-odd
moment b of rho* + eps d per unit eps. The first step is repeated with eps / 10 (linearity check).
Usage: python3 tests/v82_xodd.py OWN.npz [nsteps (10)] [eps_rel (1e-4)]"""
import sys, math, json, time, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; nst = int(sys.argv[2]) if len(sys.argv) > 2 else 10; er = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-4
d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p'])
par = [float(v) for v in args['par'].split(':')]
def A(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)
nt = len(d['th'])
F = FwdStat(p, A, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)), q=8, nt=nt,
            dti=0.01, nstep=800)
assert np.allclose(F.r.cpu().numpy(), d['r'])
F.smode = True; F.hs = 0.03; F.nmax = 8000; F.xsym = False
rho = torch.tensor(d['rho'], dtype=DT, device='cuda'); Rp = F.R**p
xi = torch.tensor((nt//2 - np.arange(nt)) % nt, device='cuda')
odd = lambda f: 0.5*(f - f[:, xi])
nrm = lambda f: float(torch.linalg.norm(f/Rp))
t0 = time.time()
T0, _ = F.T(rho)
out = dict(state=fn.split('/')[-1], p=p, nt=nt, m1=F.node(rho)['m1'], defect=float(((T0 - rho)/Rp).abs().max()),
           odd_T0_over_rho=nrm(odd(T0))/nrm(rho), odd_rho=nrm(odd(rho))/nrm(rho), wall=round(time.time() - t0, 1))
print(json.dumps(out), flush=True)
eps = er*float((rho/Rp).abs().max())
dk = odd(rho*torch.cos(F.TH)); dk = dk/nrm(dk)
for k in range(nst):
    Tk, _ = F.T(rho + eps*dk); dn = odd(Tk - T0)/eps
    rec = dict(k=k + 1, ratio=round(nrm(dn), 5), rayleigh=round(float((dn*dk/Rp**2).sum()), 5),
               b_per_eps_in=round(F.node(rho + eps*dk)['b']/eps, 5), b_per_eps_out=round(F.node(rho + eps*dn)['b']/eps, 5))
    if k == 0:
        Tl, _ = F.T(rho + 0.1*eps*dk); rec['ratio_eps/10'] = round(nrm(odd(Tl - T0)/(0.1*eps)), 5)
    rec['wall'] = round(time.time() - t0, 1)
    print(json.dumps(rec), flush=True)
    dk = dn/nrm(dn)
