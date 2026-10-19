"""Probe of the between-node residual found by tests/cand_eval.py: (1) validate the Chebyshev-series derivative on the seed
interpolated in the same basis; (2) absolute Chebyshev coefficients of the state; (3) zeta_m at nodes and midpoints."""
import numpy as np, torch, sys, json
sys.path.insert(0, 'tests')
import cand_eval as ce
path = sys.argv[1]
st = torch.load(path, map_location='cpu', weights_only=False)
Z = ce.ZetaRep(st)
a = st['args']; p0 = 1/float(a['cl0']); ay = float(a['ay'])
# (1) seed in the same basis: q_m(x_j) = zeta0_m(r_j)/r_j^kappa_m
nf = 256; th = 2*np.pi*np.arange(nf)/nf
zz = ce.seed_zeta(Z.rn[:, None]*np.cos(th)[None], Z.rn[:, None]*np.sin(th)[None], ay, p0)
zm = np.fft.fft(zz, axis=1)[:, :Z.M + 1]/nf
qs = (zm/Z.rn[:, None]**Z.kap[None]).T
st2 = dict(st); st2['q'] = torch.tensor(qs)
Zs = ce.ZetaRep(st2)
xm = 0.5*(Z.xn[:-1] + Z.xn[1:]); rm = Z.L*np.sqrt(np.exp(Z.xi_max*(1 + xm)/2) - 1)
thc = 2*np.pi*np.arange(64)/64
z, zx, zy = ce.zeta_grad_rep(Zs, rm, thc)
s0, sx, sy = ce.seed_grad(rm[:, None]*np.cos(thc)[None], rm[:, None]*np.sin(thc)[None], ay, p0)
print('seed in basis: max|z - z0| at midpoints', np.abs(z - s0).max(), ' max|grad err|*r', (np.maximum(np.abs(zx - sx), np.abs(zy - sy))*rm[:, None]).max())
# (2) absolute Chebyshev coefficients of the state, modes 1..6, last 6 degrees
np.set_printoptions(precision=2, linewidth=200)
for m in range(1, 8):
    print('m=%d  max|b|=%.2e  last6 |b| =' % (m, np.abs(Z.b[m]).max()), np.abs(Z.b[m][-6:]))
# (3) |zeta_m| at nodes and midpoints near R for m = 1..4
zn = Z.modes_at(Z.rn); zmid = Z.modes_at(rm)
print('r, |zeta_m| (m=1..4), nodes and midpoints interleaved, r > 50')
pts = sorted([(Z.rn[j], 'n', zn[j]) for j in range(len(Z.rn))] + [(rm[j], 'm', zmid[j]) for j in range(len(rm))], key=lambda t: t[0])
for rr, kind, v in pts:
    if rr > 50: print('%8.2f %s ' % (rr, kind), ' '.join('%10.5f%+10.5fi' % (v[m].real, v[m].imag) for m in (1, 2, 3, 4)))
