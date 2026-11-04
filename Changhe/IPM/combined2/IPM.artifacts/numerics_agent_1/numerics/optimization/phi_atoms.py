"""phi_atoms.py (lane numerics_agent_1): fields of the exact odd-potential correction class (numerical_audit AT-119, research/correction_potential/PROOF.md) on the product mesh.
Atom: phi = A * H_n(X) s^h (1+s)^b (t+s)^(-d), H_n = Im (x+iy)^n = r^n sin(n theta) (n odd), s = r^2.  Radial factor G(r) = r^(n+2h) (1+r^2)^b (t+r^2)^(-d),
so phi = G(r) sin(n theta).  Fields (numerical_audit PROOF.md): h = -Delta phi (density correction), v = U[h] = (-phi_xy, phi_xx) (velocity correction).
Cartesian derivatives by the ipm_polar algebra on the sine series {(0,0,n,'s'): 1} (exact rational coefficients) with radial derivatives G^(a)(r) by autograd.
Returns per atom a dict of slots key -> list of (typ, N, radial tensor) with keys ('h',(i,j)) for i+j <= dmax_h and ('v1',(i,j)), ('v2',(i,j)) for i+j <= dmax_h-1,
in the slot convention of ipm_opt2.  Self-test: -Delta phi from the series against a finite-difference Laplacian of phi (relative 1e-6 expected)."""
import math, sys, os
from fractions import Fraction
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import ipm_polar as PL
DT = torch.float64

def atom_radial_derivs(n, h, b, t, d, mesh, order=5, k=0):
    """G^(a)(r), a <= order, for G = r^(n+2h) (1+r^2)^b (t+r^2)^(-d) P_k(2 ts - 1), ts = r^2/(t + r^2) (b, t floats here; exactness lives in the JSON).
    P_k(2 ts - 1) is the shifted Legendre polynomial (recurrence, numerically stable); its exact expansion in ts is in phi_fit.shifted_legendre_coeffs."""
    def Gfun(r):
        r2 = r*r
        G = torch.exp((n+2*h)*torch.log(r)+b*torch.log1p(r2)-d*torch.log(t+r2))
        if k > 0: G = G*EV.legendre_torch(k, 2*r2/(t+r2)-1)
        return G
    return EV.autograd_radial(Gfun, mesh.r, order)

# ---------------------------------------------------------------- truncated power series (jets) in eps around every mesh radius: fast exact-order radial derivatives
class Jet:
    """J[a, i] = coefficient of eps^a of f(r_i + eps), a <= order; G^(a)(r_i) = a! J[a, i]"""
    def __init__(self, arr): self.c = arr
    @property
    def order(self): return self.c.shape[0]-1
    def __add__(self, o): return Jet(self.c+o.c) if isinstance(o, Jet) else Jet(torch.cat([self.c[:1]+o, self.c[1:]], 0))
    __radd__ = __add__
    def __sub__(self, o): return Jet(self.c-o.c) if isinstance(o, Jet) else Jet(torch.cat([self.c[:1]-o, self.c[1:]], 0))
    def __rsub__(self, o): return Jet(torch.cat([o-self.c[:1], -self.c[1:]], 0))
    def __mul__(self, o):
        if not isinstance(o, Jet): return Jet(self.c*o)
        A, B = self.c, o.c; m = A.shape[0]; out = torch.zeros_like(A)
        for a in range(m):
            out[a] = sum(A[i]*B[a-i] for i in range(a+1))
        return Jet(out)
    __rmul__ = __mul__
    def __truediv__(self, o):
        if not isinstance(o, Jet): return Jet(self.c/o)
        A, B = self.c, o.c; m = A.shape[0]; out = torch.zeros_like(A)
        for a in range(m):
            out[a] = (A[a]-sum(out[i]*B[a-i] for i in range(a)))/B[0]
        return Jet(out)
    def log(self):
        A = self.c; m = A.shape[0]; u = Jet(torch.cat([torch.zeros_like(A[:1]), A[1:]/A[0]], 0))      # A = A0 (1 + u)
        out = torch.zeros_like(A); out[0] = torch.log(A[0]); term = u
        for k in range(1, m):
            out = out+((-1)**(k+1)/k)*term.c; term = term*u
        return Jet(out)
    def exp(self):
        A = self.c; m = A.shape[0]; u = Jet(torch.cat([torch.zeros_like(A[:1]), A[1:]], 0))
        out = torch.zeros_like(A); out[0] = 1.0; term = Jet(torch.zeros_like(A)); term.c[0] = 1.0; fact = 1.0
        for k in range(1, m):
            term = term*u; fact *= k; out = out+term.c/fact
        out = out*torch.exp(A[0])[None, :]
        return Jet(out)
    def derivs(self):
        f = 1.0; out = []
        for a in range(self.order+1):
            if a > 0: f *= a
            out.append(self.c[a]*f)
        return out

def jet_radial_derivs(n, h, b, t, d, mesh, order=5, k=0):
    """G^(a)(r), a <= order, for G = r^(n+2h) (1+r^2)^b (t+r^2)^(-d) P_k(2 ts - 1) by jet arithmetic (no autograd)"""
    r = mesh.r; z = torch.zeros(order+1, len(r), dtype=DT, device=r.device); z[0] = r; z[1] = 1.0; x = Jet(z)
    x2 = x*x
    G = ((n+2*h)*x.log()+b*(x2+1.0).log()-d*(x2+t).log()).exp()
    if k > 0:
        y = (x2-t)/(x2+t)
        P0 = Jet(torch.zeros_like(z)); P0.c[0] = 1.0; P1 = y
        for kk in range(1, k):
            P0, P1 = P1, (y*P1*(2*kk+1)-P0*kk)/(kk+1)
        G = G*(P1 if k >= 1 else P0)
    return G.derivs()

_SERIES = {}
def atom_series(n, omax=5):
    """PolarSeries dicts for phi = G(r) sin(n theta) and its Cartesian derivatives up to total order omax: key (i,j) -> series (exact rational coefficients)"""
    if (n, omax) in _SERIES: return _SERIES[(n, omax)]
    base = {(0, 0, n, 's'): Fraction(1)}
    out = {(0, 0): base}
    for tot in range(1, omax+1):
        for i in range(tot+1):
            j = tot-i
            if i > 0: out[(i, j)] = PL.d_x(out[(i-1, j)])
            else: out[(i, j)] = PL.d_y(out[(i, j-1)])
    _SERIES[(n, omax)] = out
    return out

def atom_slots(n, h, b, t, d, mesh, dmax_h=3, k=0):
    """slots for h = -(phi_xx + phi_yy) and its derivatives (i+j <= dmax_h), v1 = -phi_xy, v2 = phi_xx and their derivatives (i+j <= dmax_h-1)"""
    G = (jet_radial_derivs if os.environ.get('PHI_JETS', '1') == '1' else atom_radial_derivs)(n, h, float(b), float(t), d, mesh, order=dmax_h+2, k=k)
    S = atom_series(n, omax=dmax_h+2)
    slots = {}
    for i in range(dmax_h+1):
        for j in range(dmax_h+1-i):
            lap = PL.add(S[(i+2, j)], S[(i, j+2)])
            slots[('h', (i, j))] = PL.series_slots({k: -v for k, v in lap.items()}, G, mesh)
    for i in range(dmax_h):
        for j in range(dmax_h-i):
            slots[('v1', (i, j))] = PL.series_slots({k: -v for k, v in S[(i+1, j+1)].items()}, G, mesh)
            slots[('v2', (i, j))] = PL.series_slots(S[(i+2, j)], G, mesh)
    return slots

def slots_to_field(slots_list, tabs, mesh):
    """sum of slot lists (already scaled by coefficients) -> (Nr, Nt) field"""
    tot = torch.zeros(mesh.Nr, mesh.Nt, dtype=DT, device=mesh.device)
    for typ, N, arr in slots_list: tot += arr[:, None]*tabs.tab[typ][N][None, :]
    return tot

def selftest(device='cuda'):
    dev = torch.device(device)
    mesh = build_mesh(16, 180, 0.02, 1e3, dev)
    n, h, b, t, d = 3, 0, -2.0, 1.0, 0            # the AN-045 normalizer phi_b = H_3/(6 (1+r^2)^2) up to the factor 1/6
    sl = atom_slots(n, h, b, t, d, mesh)
    Nmax = max(N for key in sl for (_, N, _) in sl[key])+1
    tabs = PL.Tables(mesh, Nmax)
    hfield = slots_to_field(sl[('h', (0, 0))], tabs, mesh)
    print('h slots (typ, N):', [(typ, N) for typ, N, _ in sl[('h', (0, 0))]], ' h_x slots:', [(typ, N) for typ, N, _ in sl[('h', (1, 0))]])
    def phi_xy(x, y):
        r = math.hypot(x, y); th = math.atan2(y, x)
        return r**(n+2*h)*(1+r*r)**b*(t+r*r)**(-d)*math.sin(n*th)
    worst = 0.0
    for (i, jj) in [(60, 50), (90, 120), (120, 30), (150, 170)]:
        r = float(mesh.r[i]); th = float(mesh.theta[jj]); x, y = r*math.cos(th), r*math.sin(th); eps = 1e-4*max(r, 1e-2)
        lap = (phi_xy(x+eps, y)+phi_xy(x-eps, y)+phi_xy(x, y+eps)+phi_xy(x, y-eps)-4*phi_xy(x, y))/eps**2
        hv = float(hfield[i, jj]); rel = abs(hv+lap)/max(abs(lap), 1e-30); worst = max(worst, rel)
        print(f'  r {r:.4f} theta {th:.3f}: series -Delta phi {hv:.8e}  FD -Delta phi {-lap:.8e}  rel {rel:.2e}')
    print('selftest worst relative difference', worst, 'OK' if worst < 1e-5 else 'FAIL')
    # origin identities (PROOF.md (2)): h_y(0) = -8A, ell = phi_xxy(0) = 2A + 6B; for the normalizer atom A = 0, B = 1 (unit coefficient)
    v2y = slots_to_field(sl[('v2', (0, 1))], tabs, mesh)      # d_y phi_xx
    hy = slots_to_field(sl[('h', (0, 1))], tabs, mesh)
    print(f'  normalizer atom: phi_xxy near origin {float(v2y[0, 0]):.6f} (expect 6 = 2A+6B with A=0,B=1), h_y near origin {float(hy[0, 0]):.3e} (expect 0 = -8A)')
    # a mode-1 atom with h=0, b=-1, t=1, d=0: A = b - d/t = -1 -> h_y(0) = 8, ell = 2A = -2
    sl1 = atom_slots(1, 0, -1.0, 1.0, 0, mesh); tabs1 = PL.Tables(mesh, 8)
    print(f'  mode-1 atom (b=-1): phi_xxy near origin {float(slots_to_field(sl1[("v2", (0, 1))], tabs1, mesh)[0, 0]):.6f} (expect -2), h_y {float(slots_to_field(sl1[("h", (0, 1))], tabs1, mesh)[0, 0]):.6f} (expect 8)')

def jet_test(device='cuda'):
    dev = torch.device(device); mesh = build_mesh(8, 60, 0.02, 1e3, dev)
    import time
    for (n, h, b, t, d, k) in [(3, 0, -2.0, 1.0, 0, 0), (21, 2, -9.0, 0.04, 14, 0), (7, 0, 1.6, 9.0, 4, 5), (41, 0, -18.5, 0.125, 21, 24), (1, 0, -0.9, 1.0, 0, 0)]:
        t0 = time.time(); A = atom_radial_derivs(n, h, b, t, d, mesh, 5, k); ta = time.time()-t0
        t0 = time.time(); J = jet_radial_derivs(n, h, b, t, d, mesh, 5, k); tj = time.time()-t0
        rel = [float((J[a]-A[a]).abs().max()/A[a].abs().max().clamp(min=1e-300)) for a in range(6)]
        print(f'  atom n{n} h{h} b{b} t{t} d{d} k{k}: max relative difference per order {["%.1e" % v for v in rel]}  autograd {ta:.3f}s jets {tj:.3f}s')

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'jets': jet_test(sys.argv[1])
    else: selftest(sys.argv[1] if len(sys.argv) > 1 else 'cuda')
