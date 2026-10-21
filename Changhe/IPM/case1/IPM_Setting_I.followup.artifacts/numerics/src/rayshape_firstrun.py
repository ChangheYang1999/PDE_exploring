"""Scattered-point evaluator (torch, float64) of the lead's global trial formula (SPEC / lead stationary.py Shape, spline radial basis,
compact = 'matched'; the closed formula is the one re-derived in the verifier's code/gen_shape.py):
  rr = r/L, s = rr^2/(1+rr^2), q = 1 - (1+rr^2)^(-(1-k)/2), chi = rr^2/(rr^2 + r_or^2), p3 = 6 + 2k/(2-k),
  H = (k-3)/2 log(1+rr^2) + sum_{m=0}^{M} prof_m(q) chi^(m-1)[m>1] cos(2 m t) + sum_{j<sing} g_j s^(p3/2) T_j(2q-1) |cos t|^(p3-2) sin^2 t,
  prof_m(q) = sum_{i=1}^{deg} z[1 + m deg + i - 1] B_i(q)   (B_i: order-7 B-splines on the stored knots, the first one omitted),
  rho = x^2 y e^H  (even in x, odd in y).
Provides rho and f = d_x rho (analytic) at arbitrary points of the plane. B-splines by the Cox-de Boor recursion on the GPU; tested
against scipy.interpolate.BSpline (tests/test_rayshape.py).
"""
import numpy as np
import torch

DT = torch.float64


def load_shape(path):
    d = np.load(path, allow_pickle=True)
    z = np.asarray(d['z'], float)
    P = dict(k=float(z[0]), L=float(d['L']), deg=int(d['degree']), ang=int(d['angular']), sing=int(d['singular']),
             order=int(d['spline_order']), r_or=float(d['origin_radius']), knots=np.asarray(d['spline_knots'], float),
             c_l=float(d['c_l']))
    assert str(d['compact']) == 'matched' and str(d['radial_basis']) == 'spline' and int(d['angular_cap']) == 0
    coef = z[1:]
    assert len(coef) == (P['ang'] + 1) * P['deg'] + P['sing']
    C = np.zeros((P['ang'] + 1, P['deg'] + 1))
    C[:, 1:] = coef[:(P['ang'] + 1) * P['deg']].reshape(P['ang'] + 1, P['deg'])   # first basis function omitted (coefficient 0)
    P['C'] = C
    P['gs'] = coef[(P['ang'] + 1) * P['deg']:]
    P['p3'] = 6 + 2 * P['k'] / (2 - P['k'])
    return P


class BSplineBasis:
    """Cox-de Boor evaluation of all nonzero B-splines of order p (degree p) and their first derivatives at points q in [0,1]."""

    def __init__(self, knots, p, device):
        self.t = torch.tensor(knots, dtype=DT, device=device)
        self.p = p
        self.n = len(knots) - p - 1          # number of basis functions
        self.device = device

    def __call__(self, q):
        t, p = self.t, self.p
        q = q.clamp(min=float(t[0]), max=float(t[-1]))
        # interval index mu with t[mu] <= q < t[mu+1], restricted to [p, n-1]
        mu = torch.searchsorted(t, q, right=True) - 1
        mu = mu.clamp(min=p, max=self.n - 1)
        N = torch.ones(q.shape[0], 1, dtype=DT, device=self.device)   # degree-0 basis on the interval
        Nprev = None
        for d in range(1, p + 1):
            # left[j] = q - t[mu+1-j], right[j] = t[mu+j] - q, j = 1..d
            j = torch.arange(1, d + 1, device=self.device)
            left = q[:, None] - t[mu[:, None] + 1 - j[None, :]]
            right = t[mu[:, None] + j[None, :]] - q[:, None]
            Nnew = torch.zeros(q.shape[0], d + 1, dtype=DT, device=self.device)
            saved = torch.zeros(q.shape[0], dtype=DT, device=self.device)
            for r in range(d):
                denom = right[:, r] + left[:, d - 1 - r]
                temp = N[:, r] / denom
                Nnew[:, r] = saved + right[:, r] * temp
                saved = left[:, d - 1 - r] * temp
            Nnew[:, d] = saved
            if d == p:
                Nprev = N
            N = Nnew
        # derivative: B'_{i,p} = p (B_{i,p-1}/(t_{i+p}-t_i) - B_{i+1,p-1}/(t_{i+p+1}-t_{i+1})), i = mu-p..mu
        i = mu[:, None] - p + torch.arange(p + 1, device=self.device)[None, :]          # (N, p+1) global indices
        # B_{i,p-1} nonzero for i = mu-p+1..mu -> Nprev columns 0..p-1 correspond to i = mu-p+1..mu
        Bm1 = torch.zeros(q.shape[0], p + 2, dtype=DT, device=self.device)                # index shift: column c <-> i = mu-p+c-1 ... build explicitly
        # columns of Bm1: i = mu-p .. mu+1 ; nonzero for i = mu-p+1..mu
        Bm1[:, 1:p + 1] = Nprev
        den1 = t[i + p] - t[i]
        den2 = t[i + p + 1] - t[i + 1]
        term1 = torch.where(den1 > 0, Bm1[:, 0:p + 1] / torch.where(den1 > 0, den1, torch.ones_like(den1)), torch.zeros_like(den1))
        term2 = torch.where(den2 > 0, Bm1[:, 1:p + 2] / torch.where(den2 > 0, den2, torch.ones_like(den2)), torch.zeros_like(den2))
        dN = p * (term1 - term2)
        return N, dN, i


class ShapeEval:
    def __init__(self, P, device):
        self.P = P
        self.dev = device
        self.basis = BSplineBasis(P['knots'], P['order'], device)
        self.C = torch.tensor(P['C'], dtype=DT, device=device)                       # (M+1, deg+1)
        self.m = torch.arange(P['ang'] + 1, dtype=DT, device=device)
        self.chipow = torch.clamp(self.m - 1, min=0)                                 # chi^(m-1) for m > 1, else chi^0
        self.gs = torch.tensor(P['gs'], dtype=DT, device=device)

    def _H(self, r, t):
        """H, dH/dr, dH/dt at first-quadrant polar points (r > 0, t in [0, pi/2])."""
        P = self.P
        k, L, r_or, p3 = P['k'], P['L'], P['r_or'], P['p3']
        rr = r / L
        rr2 = rr * rr
        lg = torch.log1p(rr2)
        s_ = rr2 / (1 + rr2)
        q = -torch.expm1(-(1 - k) / 2 * lg)
        q_r = (1 - k) * rr * torch.exp(-(3 - k) / 2 * lg) / L
        s_r = 2 * rr / (L * (1 + rr2) ** 2)
        N, dN, idx = self.basis(q)                                                   # (n, p+1)
        # prof_m = sum_c C[m, idx_c] N_c ; prof_m' = sum_c C[m, idx_c] dN_c
        Cg = self.C[:, idx]                                                          # (M+1, n, p+1)
        prof = torch.einsum('mnc,nc->mn', Cg, N)
        dprof = torch.einsum('mnc,nc->mn', Cg, dN)
        del Cg
        if r_or > 0:
            chi = rr2 / (rr2 + r_or ** 2)
            chi_r = 2 * rr * r_or ** 2 / (L * (rr2 + r_or ** 2) ** 2)
            cp = chi[None, :] ** self.chipow[:, None]                                # chi^(m-1)
            # d/dr chi^(m-1) = (m-1) chi^(m-2) chi_r for m > 1 (0 for m <= 1)
            cpr = torch.where(self.chipow[:, None] > 0,
                              self.chipow[:, None] * chi[None, :] ** torch.clamp(self.chipow[:, None] - 1, min=0) * chi_r[None, :],
                              torch.zeros_like(cp))
        else:
            cp = torch.ones_like(prof)
            cpr = torch.zeros_like(prof)
        mt = 2 * self.m[:, None] * t[None, :]
        cos_ = torch.cos(mt)
        sin_ = torch.sin(mt)
        H = (k - 3) / 2 * lg + torch.einsum('mn,mn,mn->n', prof, cp, cos_)
        H_r = (k - 3) * rr / (L * (1 + rr2)) + torch.einsum('mn,mn->n', dprof * q_r[None, :] * cp + prof * cpr, cos_)
        H_t = torch.einsum('mn,mn,mn->n', prof * cp, -2 * self.m[:, None] * torch.ones_like(prof), sin_)
        if P['sing'] > 0:
            ct, st = torch.cos(t), torch.sin(t)
            ang = ct ** (p3 - 2) * st ** 2
            ang_t = -(p3 - 2) * ct ** (p3 - 3) * st ** 3 + 2 * ct ** (p3 - 1) * st
            x = 2 * q - 1
            # Chebyshev T_j(x) and T_j'(x) by recursion
            T0, T1 = torch.ones_like(x), x
            dT0, dT1 = torch.zeros_like(x), torch.ones_like(x)
            rad = torch.zeros_like(x)
            rad_r = torch.zeros_like(x)
            sp = s_ ** (p3 / 2)
            sp_r = (p3 / 2) * s_ ** (p3 / 2 - 1) * s_r
            for j in range(P['sing']):
                if j == 0:
                    T, dT = T0, dT0
                elif j == 1:
                    T, dT = T1, dT1
                else:
                    T = 2 * x * T1 - T0
                    dT = 2 * T1 + 2 * x * dT1 - dT0
                    T0, T1, dT0, dT1 = T1, T, dT1, dT
                rad = rad + self.gs[j] * sp * T
                rad_r = rad_r + self.gs[j] * (sp_r * T + sp * dT * 2 * q_r)
            H = H + rad * ang
            H_r = H_r + rad_r * ang
            H_t = H_t + rad * ang_t
        return H, H_r, H_t

    def rho_f(self, x, y, chunk=300000, want_y=False):
        """rho and f = d_x rho at arbitrary points (torch tensors on the device). Parity: rho even in x, odd in y; f odd in both.
        With want_y=True also returns rho_y (even in x, even in y)."""
        out_rho = torch.empty_like(x)
        out_f = torch.empty_like(x)
        out_fy = torch.empty_like(x) if want_y else None
        for i0 in range(0, x.shape[0], chunk):
            xs = x[i0:i0 + chunk]
            ys = y[i0:i0 + chunk]
            xa, ya = xs.abs(), ys.abs()
            r = torch.hypot(xa, ya)
            t = torch.atan2(ya, xa)
            rpos = torch.where(r > 0, r, torch.ones_like(r))
            H, H_r, H_t = self._H(rpos, t)
            eH = torch.exp(H)
            ct, st = torch.cos(t), torch.sin(t)
            H_x = ct * H_r - st * H_t / rpos
            rho = xa * xa * ya * eH
            f = (2 * xa * ya + xa * xa * ya * H_x) * eH
            rho = torch.where(r > 0, rho, torch.zeros_like(rho)) * torch.sign(ys)
            f = torch.where(r > 0, f, torch.zeros_like(f)) * torch.sign(xs) * torch.sign(ys)
            out_rho[i0:i0 + chunk] = rho
            out_f[i0:i0 + chunk] = f
            if want_y:
                H_y = st * H_r + ct * H_t / rpos
                fy = (xa * xa + xa * xa * ya * H_y) * eH          # d_y (x^2 y e^H) in the first quadrant; even in x and in y
                out_fy[i0:i0 + chunk] = torch.where(r > 0, fy, torch.zeros_like(fy))
        if want_y:
            return out_rho, out_f, out_fy
        return out_rho, out_f
