"""Global closure test, weight-independent: the strain induced at the origin by the slaved vorticity,
    c_char = (1/pi) int_R2 xy r^-4 Omega_char dX = (4/pi) int_0^inf (dr/r) int_0^{pi/2} sin(phi) cos(phi) Omega_char(r, phi) dphi,
must equal c = Psi_xy(0) = -2 at a fixed point of the slaved closure (and the same integral of Omega_basis gives exactly c).
Quadrature: trapezoid in ln r (per-decade points) on [rmin, rmax] plus the analytic tail beyond rmax assuming Omega ~ r^(-1/beta)
(tail = beta rmax^(-1/beta) x angular integral of Omega_char(rmax) rmax^(1/beta)), Gauss-Legendre in phi."""
import sys, os, math, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from charlib2 import *
ap = argparse.ArgumentParser(); ap.add_argument('npz'); ap.add_argument('--per-decade', type=int, default=24); ap.add_argument('--Nth', type=int, default=32)
ap.add_argument('--rmin', type=float, default=1e-3); ap.add_argument('--rmax', type=float, default=1e9); ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--rstop', type=float, default=1e-3)
args = ap.parse_args(); dv = dev()
d = np.load(args.npz, allow_pickle=True); beta = float(d['beta']); L = float(d['L']); NO = int(d['NO']); K = int(d['K']); a0 = float(d['a0'])
bas = PsiBasis(beta, NO, K, L=L, gamma_P=float(d['gamma_P']) if 'gamma_P' in d else None, mu=float(d['mu']) if 'mu' in d else None)
cP = torch.tensor(d['cP'], dtype=DT, device=dv).reshape(NO, K)
nd = int(round(math.log10(args.rmax / args.rmin) * args.per_decade)) + 1
lr = torch.linspace(math.log(args.rmin * L), math.log(args.rmax * L), nd, dtype=DT, device=dv); r = torch.exp(lr); dlr = float(lr[1] - lr[0])
xg, wg = np.polynomial.legendre.leggauss(args.Nth); th = torch.tensor((xg + 1) * 0.25 * math.pi, dtype=DT, device=dv); wth = torch.tensor(wg * 0.25 * math.pi, dtype=DT, device=dv)
R, TH = torch.meshgrid(r, th, indexing='ij'); X = (R * torch.cos(TH)).reshape(-1); Y = (R * torch.sin(TH)).reshape(-1)
tr = transport(bas, cP[None], a0, beta, X, Y, dt=args.dt, r_stop=args.rstop, T_max=60.0)
fb = bas.fields(cP[None], X, Y)
Omc = tr['Om'][0].reshape(nd, -1); Omb = fb['Om'][0].reshape(nd, -1); fail = tr['fail'][0].reshape(nd, -1)
ang = (torch.sin(th) * torch.cos(th) * wth)[None, :]
Ic = (Omc * ang).sum(1); Ib = (Omb * ang).sum(1)                   # angular integrals (nd,)
wr = torch.full((nd,), dlr, dtype=DT, device=dv); wr[0] *= 0.5; wr[-1] *= 0.5
def total(I):
    main = float((I * wr).sum()); tail = float(I[-1]) * beta          # int_rmax^inf r^(-1/beta) dr/r * rmax^(1/beta) = beta
    inner = float(I[0]) * 2.0 * 0.5 if False else float(I[0]) / 2.0   # Omega ~ r^2 near 0: int_0^rmin r^2 dr/r = rmin^2/2 -> I(rmin)/2
    return (4.0 / math.pi) * (main + tail + inner), (4.0 / math.pi) * main, (4.0 / math.pi) * tail, (4.0 / math.pi) * inner
cc, cc_main, cc_tail, cc_inner = total(Ic); cb, cb_main, cb_tail, cb_inner = total(Ib)
F = bas.centre_functionals(dv); c_exact = float(cP.reshape(-1) @ F['c'])
print(f'# {args.npz}: beta {beta} a0 {a0:.5f}; grid {nd} radii x {args.Nth} angles, nfail {int(fail.sum())}')
print(f'# c (exact functional of the basis)       = {c_exact:.8f}')
print(f'# c from the basis Omega by quadrature    = {cb:.8f}   (main {cb_main:.6f}, tail>{args.rmax:.0e} {cb_tail:.6f}, inner<{args.rmin:.0e} {cb_inner:.2e})  [quadrature check: should equal c]')
print(f'# c_char from the slaved Omega            = {cc:.8f}   (main {cc_main:.6f}, tail {cc_tail:.6f}, inner {cc_inner:.2e})')
print(f'# closure defect c_char - c = {cc - c_exact:+.6f}  ({(cc - c_exact) / abs(c_exact) * 100:+.3f} percent)')
# radial distribution of the defect: cumulative (4/pi) int (I_c - I_b) dr/r
cum = (4.0 / math.pi) * torch.cumsum((Ic - Ib) * wr, 0)
for rv in [1e-2, 1e-1, 1, 10, 100, 1e3, 1e4, 1e6, 1e8, 1e9]:
    i = int(torch.argmin((r - rv * L).abs())); print(f'#   cumulative defect up to r = {float(r[i]):.1e}: {float(cum[i]):+.6f}')
