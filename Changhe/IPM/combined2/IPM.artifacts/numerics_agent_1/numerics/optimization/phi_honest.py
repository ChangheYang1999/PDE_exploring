"""phi_honest.py (lane numerics_agent_1): extended-precision evaluation of the odd-potential correction and of F_* on a product mesh, from the frozen exact JSON
(rational coefficients, Legendre form), in numpy longdouble (x87 80-bit: 64-bit mantissa, unit roundoff 5.4e-20) and, by the same code, in binary64.
Purpose (numerics_agent_2 FINDING 2026-11-03T10:05Z): the binary64 sum of the 12273 atoms cancels by many orders (coefficients up to 3e10 on atoms of natural
size 2^-27), so the float F_* of the near-field-stage centers carries a pointwise roundoff floor; the longdouble value is the honest FLOAT residual
(its own floor is about 500 times lower), the binary64-minus-longdouble difference is one realization of the float noise, and the per-point bound
eps64 * sum_j |a_j| |L atom_j| is a deterministic estimate of that floor.  Everything here is FLOAT (no rounding control).
Usage: phi_honest.py <phi_exact.json> <background.pt> <out.json> [<Fstar_run.npy>]
Fields: h = -Delta phi, grad h, v = U[h] = (-phi_xy, phi_xx); F_* = F0 + (c x + u1) h_x + (c y + u2) h_y - h + rho_x v1 + rho_y v2 + v1 h_x + v2 h_y,
u = (-psi_y, psi_x), on the background's mesh (binary64 base fields; the base residual beyond r = 1000 is the far-fixed series value).
Only the L2 part is evaluated (dmax_h = 1); the derivative energies are not noise-limited (numerics_agent_2 10:05Z item 3(c))."""
import sys, os, json, math, time
from fractions import Fraction
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import phi_atoms as PA

LD = np.longdouble
EPS64 = 2.0**-53

def fr2(fr, dt):
    fr = Fraction(fr)
    return dt(str(fr.numerator))/dt(str(fr.denominator)) if dt is LD else float(fr)

class NJet:
    """truncated power series in eps around every mesh radius: c[a, i] = coefficient of eps^a of f(r_i + eps)"""
    def __init__(self, c): self.c = c
    @property
    def order(self): return self.c.shape[0]-1
    def _wrap(self, o):
        if isinstance(o, NJet): return o
        z = np.zeros_like(self.c); z[0] = o; return NJet(z)
    def __add__(self, o): o = self._wrap(o); return NJet(self.c+o.c)
    __radd__ = __add__
    def __sub__(self, o): o = self._wrap(o); return NJet(self.c-o.c)
    def __rsub__(self, o): o = self._wrap(o); return NJet(o.c-self.c)
    def __mul__(self, o):
        if not isinstance(o, NJet): return NJet(self.c*o)
        A, B = self.c, o.c; m = A.shape[0]; out = np.zeros_like(A)
        for a in range(m):
            acc = A[0]*B[a]
            for i in range(1, a+1): acc = acc+A[i]*B[a-i]
            out[a] = acc
        return NJet(out)
    __rmul__ = __mul__
    def __truediv__(self, o):
        if not isinstance(o, NJet): return NJet(self.c/o)
        A, B = self.c, o.c; m = A.shape[0]; out = np.zeros_like(A)
        for a in range(m):
            acc = A[a].copy()
            for i in range(a): acc = acc-out[i]*B[a-i]
            out[a] = acc/B[0]
        return NJet(out)
    def log(self):
        A = self.c; m = A.shape[0]; u = NJet(np.concatenate([np.zeros_like(A[:1]), A[1:]/A[0]], 0))
        out = np.zeros_like(A); out[0] = np.log(A[0]); term = u
        for k in range(1, m):
            out = out+((-1)**(k+1)/k)*term.c; term = term*u
        return NJet(out)
    def exp(self):
        A = self.c; m = A.shape[0]; u = NJet(np.concatenate([np.zeros_like(A[:1]), A[1:]], 0))
        out = np.zeros_like(A); out[0] = 1.0; term = NJet(np.zeros_like(A)); term.c[0] = 1.0; fact = 1.0
        for k in range(1, m):
            term = term*u; fact *= k; out = out+term.c/fact
        out = out*np.exp(A[0])[None, :]
        return NJet(out)
    def derivs(self):
        f = 1.0; out = []
        for a in range(self.order+1):
            if a > 0: f *= a
            out.append(self.c[a]*f)
        return out

def radial_jets(n, h, b, t, d, r, order, k):
    """G^(a)(r), a <= order, G = r^(n+2h) (1+r^2)^b (t+r^2)^(-d) P_k(2 ts - 1), ts = r^2/(t+r^2); dtype of r"""
    z = np.zeros((order+1, len(r)), dtype=r.dtype); z[0] = r; z[1] = 1.0; x = NJet(z)
    x2 = x*x
    G = ((n+2*h)*x.log()+b*(x2+1.0).log()-d*(x2+t).log()).exp()
    if k > 0:
        y = (x2-t)/(x2+t)
        P0 = NJet(np.zeros_like(z)); P0.c[0] = 1.0; P1 = y
        for kk in range(1, k):
            P0, P1 = P1, (y*P1*(2*kk+1)-P0*kk)/(kk+1)
        G = G*P1
    return G.derivs()

KEYS = [('h', (0, 0)), ('h', (1, 0)), ('h', (0, 1)), ('v1', (0, 0)), ('v2', (0, 0))]

def key_series(n):
    S = PA.atom_series(n, omax=3)
    import ipm_polar as PL
    neg = lambda T: {k: -v for k, v in T.items()}
    return {('h', (0, 0)): neg(PL.add(S[(2, 0)], S[(0, 2)])), ('h', (1, 0)): neg(PL.add(S[(3, 0)], S[(1, 2)])), ('h', (0, 1)): neg(PL.add(S[(2, 1)], S[(0, 3)])),
            ('v1', (0, 0)): neg(S[(1, 1)]), ('v2', (0, 0)): S[(2, 0)]}

def params_from_json_atoms(atoms):
    """(A_str, n, h, b_str, t_str, d, k) tuples from the frozen JSON atom dicts"""
    return [(at['coefficient_exact'], int(at['n']), int(at['h']), at['b_exact'], at['scale_exact'], int(at['d']), int(at.get('legendre_degree', 0))) for at in atoms]

def accumulate(atoms, r, dt, with_abs=False, log=None):
    return accumulate_params(params_from_json_atoms(atoms), r, dt, with_abs=with_abs, log=log)

def accumulate_params(params, r, dt, with_abs=False, log=None):
    """radial mode sums rad[key][(typ, N)] (dtype dt) and, optionally, the absolute sums (binary64) over the atoms; params: (A, n, h, b, t, d, k) with A, b, t
    rational strings or floats (binary64 floats are exact in longdouble)"""
    rad = {key: {} for key in KEYS}; absrad = {key: {} for key in KEYS} if with_abs else None
    rl = r.astype(dt); t0 = time.time(); rpow = {}; ks = {}
    conv = lambda v: (dt(v) if isinstance(v, float) else fr2(v, dt))
    for ia, (A_, n, h, b_, t_, d, k) in enumerate(params):
        A = conv(A_)
        if A == 0: continue
        b = conv(b_); t = conv(t_)
        G = radial_jets(n, h, b, t, d, rl, 3, k)
        if n not in ks: ks[n] = key_series(n)
        for key, S in ks[n].items():
            for (a, bb, N, tt), v in S.items():
                if bb not in rpow: rpow[bb] = rl**(-bb) if bb else None
                term = G[a]*fr2(v, dt)
                if bb: term = term*rpow[bb]
                term = term*A
                kk = ('sin' if tt == 's' else 'cos', N)
                rad[key][kk] = rad[key][kk]+term if kk in rad[key] else term
                if with_abs:
                    ab = np.abs(term.astype(np.float64))
                    absrad[key][kk] = absrad[key][kk]+ab if kk in absrad[key] else ab
        if log and (ia+1) % 2000 == 0: print(f'  {ia+1} atoms, {time.time()-t0:.0f} s', flush=True)
    return rad, absrad

def honest_fields_fstar(params, r, theta, bgf, dt=LD):
    """F_* (binary64 array) from the longdouble evaluation of the correction given by params on the mesh (r, theta) with the base fields bgf"""
    rad, _ = accumulate_params(params, r, dt)
    fl = assemble(rad, theta, dt, nr=len(r))
    return fstar(fl, bgf, dt).astype(np.float64)

def assemble(rad, theta, dt, absolute=False, nr=None):
    """fields (Nr, Nt) from the radial mode sums; absolute=True sums |rad| |trig|; an empty mode sum (all coefficients zero) gives zeros (nr needed then)"""
    th = theta.astype(dt); out = {}
    for key, D in rad.items():
        n_r = len(next(iter(D.values()))) if D else nr
        assert n_r is not None, 'empty field and nr not given'
        tot = np.zeros((n_r, len(th)), dtype=dt)
        for (typ, N), arr in D.items():
            tab = np.sin(N*th) if typ == 'sin' else np.cos(N*th)
            if absolute: tot += np.abs(arr)[:, None]*np.abs(tab)[None, :]
            else: tot += arr[:, None]*tab[None, :]
        out[key] = tot
    return out

def fstar(fl, bgf, dt):
    c = fr2('4076476460239181/2251799813685248', dt)
    x, y = bgf['x'].astype(dt), bgf['y'].astype(dt)
    h, hx, hy, v1, v2 = (fl[k] for k in KEYS)
    u1, u2 = -bgf['psi_y'].astype(dt), bgf['psi_x'].astype(dt)
    return bgf['F0'].astype(dt)+(c*x+u1)*hx+(c*y+u2)*hy-h+bgf['rho_x'].astype(dt)*v1+bgf['rho_y'].astype(dt)*v2+v1*hx+v2*hy

def noise_bound(absf, bgf):
    """eps64 * sum of |terms| of F_* (binary64 evaluation floor estimate, deterministic)"""
    c = float(Fraction('4076476460239181/2251799813685248'))
    x, y = np.abs(bgf['x']), np.abs(bgf['y']); Bh, Bhx, Bhy, Bv1, Bv2 = (absf[k] for k in KEYS)
    u1, u2 = np.abs(bgf['psi_y']), np.abs(bgf['psi_x'])
    return EPS64*((c*x+u1)*Bhx+(c*y+u2)*Bhy+Bh+np.abs(bgf['rho_x'])*Bv1+np.abs(bgf['rho_y'])*Bv2)

def load_bg(pt):
    import torch
    bg = torch.load(pt, weights_only=False); m = bg['mesh']
    s = m['s'].numpy().astype(np.float64); ws = m['ws'].numpy().astype(np.float64); theta = m['theta'].numpy().astype(np.float64); wth = m['wth'].numpy().astype(np.float64)
    r = np.exp(s); x = r[:, None]*np.cos(theta)[None, :]; y = r[:, None]*np.sin(theta)[None, :]
    base = 4*(ws[:, None]*wth[None, :])*(r**2)[:, None]
    bgf = {'x': x, 'y': y, 'F0': bg['F0'][(0, 0)].numpy(), 'rho_x': bg['rho'][(1, 0)].numpy(), 'rho_y': bg['rho'][(0, 1)].numpy(), 'psi_x': bg['psi'][(1, 0)].numpy(), 'psi_y': bg['psi'][(0, 1)].numpy()}
    return r, theta, base, bgf, bg['meta']

def dyadic(F2w, r):
    edges = [0.02, 0.5, 1, 2, 4, 8, 16, 32, 64, 128, 300, 1000, 1e4]; tot = F2w.sum(); out = {}
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (r >= lo) & (r < hi); out[f'[{lo:g},{hi:g})'] = float(F2w[m].sum()/tot)
    return out

def main():
    phip, bgp, outp = sys.argv[1], sys.argv[2], sys.argv[3]; runnpy = sys.argv[4] if len(sys.argv) > 4 else None
    P = json.load(open(phip)); atoms = P['atoms']
    r, theta, base, bgf, meta = load_bg(bgp)
    print(f'{len(atoms)} atoms; mesh {len(r)} x {len(theta)} from {os.path.basename(bgp)}; longdouble eps {np.finfo(LD).eps:.2e}', flush=True)
    T0 = time.time(); rad64, absrad = accumulate(atoms, r, np.float64, with_abs=True, log=True); t64 = time.time()-T0; print(f'binary64 pass {t64:.0f} s', flush=True)
    T0 = time.time(); radld, _ = accumulate(atoms, r, LD, log=True); tld = time.time()-T0; print(f'longdouble pass {tld:.0f} s', flush=True)
    f64 = assemble(rad64, theta, np.float64); fld = assemble(radld, theta, LD); fabs = assemble(absrad, theta, np.float64, absolute=True)
    F64 = fstar(f64, bgf, np.float64); FLD = fstar(fld, bgf, LD); FLD64 = FLD.astype(np.float64); NB = noise_bound(fabs, bgf)
    diff = F64-FLD64
    n64 = math.sqrt(float((base*F64**2).sum())); nld = math.sqrt(float((base*FLD64**2).sum())); nd = math.sqrt(float((base*diff**2).sum())); nb = math.sqrt(float((base*NB**2).sum()))
    print(f'||F_*||_2: binary64 {n64:.6e}  longdouble {nld:.6e}  (difference field {nd:.3e}; eps64 bound field {nb:.3e})', flush=True)
    rows = []
    for rv in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 20.0, 50.0, 150.0, 300.0, 1000.0]:
        i = int(np.argmin(np.abs(r-rv))); rms = lambda a: float(math.sqrt(np.mean(a[i].astype(np.float64)**2)))
        rows.append({'r': float(r[i]), 'rms_f64': rms(F64), 'rms_ld': rms(FLD64), 'rms_diff': rms(diff), 'rms_bound': rms(NB), 'max_abs_diff': float(np.max(np.abs(diff[i])))})
        print(f"r = {r[i]:9.4f}: rms F_* binary64 {rows[-1]['rms_f64']:.4e}  longdouble {rows[-1]['rms_ld']:.4e}  diff {rows[-1]['rms_diff']:.3e} ({100*rows[-1]['rms_diff']/max(rows[-1]['rms_f64'], 1e-300):.1f} percent of the binary64 rms)  eps64 bound {rows[-1]['rms_bound']:.3e}", flush=True)
    out = {'label': 'FLOAT (longdouble honest residual against binary64, same code); no rounding control', 'phi_json': os.path.relpath(phip), 'phi_sha256': __import__('hashlib').sha256(open(phip, 'rb').read()).hexdigest(),
           'background_pt': os.path.relpath(bgp), 'bg_meta': {k: v for k, v in meta.items() if k in ('mid', 'ang', 'Nr', 'Nt', 'cand_sha256', 'rcut', 'rmax')},
           'n_atoms': len(atoms), 'L2_binary64': n64, 'L2_longdouble': nld, 'L2_difference_field': nd, 'L2_eps64_bound_field': nb,
           'dyadic_shares_longdouble': dyadic((base*FLD64**2).sum(1), r), 'dyadic_shares_binary64': dyadic((base*F64**2).sum(1), r), 'dyadic_shares_difference': dyadic((base*diff**2).sum(1), r),
           'sup_F_longdouble': float(np.max(np.abs(FLD64))), 'sup_F_binary64': float(np.max(np.abs(F64))), 'rows': rows, 'time_s': {'binary64': t64, 'longdouble': tld},
           'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if runnpy and os.path.exists(runnpy):
        Frun = np.load(runnpy)
        if Frun.shape == F64.shape:
            d2 = Frun-FLD64; nr = math.sqrt(float((base*Frun**2).sum())); nd2 = math.sqrt(float((base*d2**2).sum()))
            out['run_npy'] = {'path': os.path.relpath(runnpy), 'L2_run': nr, 'L2_run_minus_longdouble': nd2, 'rows': [{'r': float(r[int(np.argmin(np.abs(r-rw['r'])))]), 'rms_run': float(math.sqrt(np.mean(Frun[int(np.argmin(np.abs(r-rw['r'])))]**2))), 'rms_run_minus_ld': float(math.sqrt(np.mean(d2[int(np.argmin(np.abs(r-rw['r'])))]**2)))} for rw in rows]}
            print(f'saved torch run: ||F_*||_2 {nr:.6e}; run minus longdouble field {nd2:.3e}', flush=True)
        else: print('run npy shape mismatch', Frun.shape, F64.shape)
    np.save(outp.replace('.json', '_Fld.npy'), FLD64)
    json.dump(out, open(outp, 'w'), indent=1); print('written', outp, flush=True)

if __name__ == '__main__': main()
