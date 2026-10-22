"""Verifier's own evaluator of the X3 trial density (written from the formula in PROMPT.md + the stored npz fields).

No code of the team or of the earlier runs is imported. B-splines by an own Cox-de Boor recursion (float64 numpy or
torch), derivatives analytic.

Formula (u = r/L, s = u^2/(1+u^2), q = 1-(1+u^2)^(-(1-k)/2), chi = u^2/(u^2+r0^2)):
  H = (k-3)/2 log(1+u^2) + sum_m chi^max(m-1,0) b_m(q) cos(2 m th) + s^(p3/2) |cos th|^(p3-2) sin^2 th T(2q-1)
  b_m(q) = sum_{j=1..deg} C[m, j-1] B_j(q)  (B_0 omitted so b_m(0) = 0), T = sum_j S_j T_j (Chebyshev)
  rho = x^2 y exp(H) = L^3 u^3 cos^2 th sin th exp(H).
"""
import numpy as np

NPZ = 'PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz'


class Trial:
    def __init__(self, path=NPZ):
        d = np.load(path, allow_pickle=True)
        self.z = np.asarray(d['z'], float)
        self.k = float(self.z[0])
        self.L = float(d['L'])
        self.cl_stored = float(d['c_l'])
        self.deg = int(d['degree']); self.ang = int(d['angular']); self.sing = int(d['singular'])
        self.order = int(d['spline_order']); self.r0 = float(d['origin_radius'])
        assert str(d['compact']) == 'matched' and str(d['radial_basis']) == 'spline'
        self.knots = np.asarray(d['spline_knots'], float)
        assert len(self.knots) == self.deg + self.order + 2
        co = self.z[1:]
        self.C = co[:(self.ang + 1) * self.deg].reshape(self.ang + 1, self.deg)
        self.S = co[(self.ang + 1) * self.deg:]
        assert len(self.S) == self.sing
        self.p3 = 6 + 2 * self.k / (2 - self.k)

    # ---------------------------------------------------------------- B-splines (own Cox-de Boor)
    def bspline(self, q, nu=0):
        """values (nu=0) or first derivatives (nu=1) of all B_0..B_deg at points q (1-d array); returns (len(q), deg+1).
        Right end q = 1 is included in the last interval (clamped)."""
        t = self.knots; p = self.order
        nb = len(t) - p - 1                      # = deg + 1
        q = np.asarray(q, float)
        # interval index i with t[i] <= q < t[i+1], restricted to p <= i <= nb-1
        i = np.searchsorted(t, q, side='right') - 1
        i = np.clip(i, p, nb - 1)
        # de Boor triangular table of the p+1 nonzero basis functions of degree p (and lower degrees for derivs)
        N = np.zeros((len(q), p + 1)); N[:, 0] = 1.0
        tables = [N[:, :1].copy()]
        for j in range(1, p + 1):
            Nn = np.zeros((len(q), j + 1))
            for rr in range(j):
                left = t[i + rr + 1 - j]; right = t[i + rr + 1]
                den = right - left
                w = np.where(den > 0, (q - left) / np.where(den > 0, den, 1), 0.0)
                Nn[:, rr] += (1 - w) * tables[-1][:, rr]
                Nn[:, rr + 1] += w * tables[-1][:, rr]
            tables.append(Nn)
        # tables[j][:, rr] is B_{i-j+rr, j}
        def lower_to_full(vals, j):
            out = np.zeros((len(q), nb))
            for rr in range(j + 1):
                idx = i - j + rr
                np.add.at(out, (np.arange(len(q)), idx), vals[:, rr])
            return out
        if nu == 0:
            return lower_to_full(tables[p], p)
        # derivative formula: B'_{a,p} = p [B_{a,p-1}/(t_{a+p}-t_a) - B_{a+1,p-1}/(t_{a+p+1}-t_{a+1})]
        def deriv_coeffs(level_vals, j):
            # given B_{.,j-1} on the (j) nonzero entries, return derivative-of-degree-j combination weights
            out = np.zeros((len(q), j + 1))
            for rr in range(j):            # B_{i-(j-1)+rr, j-1}
                a = i - (j - 1) + rr
                # contributes +j/(t_{a+j}-t_a) to B'_{a,j} and -j/(t_{a+j+1}-t_{a+1}) to B'_{a-1,j}
                d1 = t[a + j] - t[a]
                c1 = np.where(d1 > 0, j / np.where(d1 > 0, d1, 1), 0.0)
                out[:, rr + 1] += c1 * level_vals[:, rr]        # B_{a,j} is index rr+1 in degree-j table (a = i-j+(rr+1))
                out[:, rr] -= c1 * level_vals[:, rr]            # B_{a-1,j}: derivative term -j B_{a,j-1}/(t_{a+j}-t_a)
            return out
        if nu == 1:
            return lower_to_full(deriv_coeffs(tables[p - 1], p), p)
        raise ValueError

    # ---------------------------------------------------------------- radial profiles
    def radial(self, u):
        """returns dict with q, dq/du, chi, dchi/du, b (deg-contracted, shape (len(u), ang+1)), b_u."""
        u = np.asarray(u, float)
        k = self.k
        lg = np.log1p(u * u)
        tau = np.exp(-(1 - k) / 2 * lg)               # 1 - q
        q = -np.expm1(-(1 - k) / 2 * lg)
        dq = (1 - k) * u * tau / (1 + u * u)
        Bv = self.bspline(q, 0)[:, 1:]
        Bd = self.bspline(q, 1)[:, 1:]
        b = Bv @ self.C.T                              # (n, ang+1)
        bq = Bd @ self.C.T
        chi = u * u / (u * u + self.r0 ** 2)
        dchi = 2 * u * self.r0 ** 2 / (u * u + self.r0 ** 2) ** 2
        m = np.arange(self.ang + 1)
        j = np.maximum(m - 1, 0)
        mult = chi[:, None] ** j[None, :]
        dmult = np.where(j[None, :] > 0, j[None, :] * chi[:, None] ** np.maximum(j[None, :] - 1, 0) * dchi[:, None], 0.0)
        bm = b * mult
        bm_u = bq * dq[:, None] * mult + b * dmult
        s = u * u / (1 + u * u)
        ds = 2 * u / (1 + u * u) ** 2
        zc = 2 * q - 1
        T = np.polynomial.chebyshev.chebval(zc, self.S)
        Tz = np.polynomial.chebyshev.chebval(zc, np.polynomial.chebyshev.chebder(self.S))
        sp3 = s ** (self.p3 / 2)
        sg = sp3 * T
        sg_u = (self.p3 / 2) * s ** (self.p3 / 2 - 1) * ds * T + sp3 * Tz * 2 * dq
        base = (k - 3) / 2 * lg
        base_u = (k - 3) * u / (1 + u * u)
        return dict(q=q, dq=dq, bm=bm, bm_u=bm_u, sg=sg, sg_u=sg_u, base=base, base_u=base_u)

    def H(self, u, th):
        """H, H_u, H_th on the tensor grid u (n,) x th (m,). th in [0, pi/2] or general (uses |cos|)."""
        R = self.radial(u)
        m = np.arange(self.ang + 1)
        cosm = np.cos(2 * np.outer(m, th)); sinm = np.sin(2 * np.outer(m, th))
        ct = np.abs(np.cos(th)); st = np.sin(th)
        A = ct ** (self.p3 - 2) * st ** 2
        # d/dth of |cos|^(p3-2) sin^2 (valid for cos != 0; at cos = 0 the value is 0 since p3-3 > 0)
        sgn = np.sign(np.cos(th))
        A_th = -(self.p3 - 2) * ct ** (self.p3 - 3) * sgn * st ** 3 + 2 * ct ** (self.p3 - 2) * st * np.cos(th)
        Hv = R['base'][:, None] + R['bm'] @ cosm + R['sg'][:, None] * A[None, :]
        Hu = R['base_u'][:, None] + R['bm_u'] @ cosm + R['sg_u'][:, None] * A[None, :]
        Hth = R['bm'] @ (-2 * m[:, None] * sinm) + R['sg'][:, None] * A_th[None, :]
        return Hv, Hu, Hth

    def fields(self, r, th):
        """rho, rho_x, rho_y on the tensor grid (physical r)."""
        L = self.L
        u = np.asarray(r, float) / L
        Hv, Hu, Hth = self.H(u, th)
        rr = np.asarray(r, float)[:, None]
        c = np.cos(th)[None, :]; s = np.sin(th)[None, :]
        x = rr * c; y = rr * s
        E = np.exp(Hv)
        Hr = Hu / L
        Hx = c * Hr - s * Hth / rr
        Hy = s * Hr + c * Hth / rr
        rho = x * x * y * E
        rho_x = E * (2 * x * y + x * x * y * Hx)
        rho_y = E * (x * x + x * x * y * Hy)
        return dict(rho=rho, rho_x=rho_x, rho_y=rho_y, H=Hv, Hr=Hr, Hth=Hth, x=x, y=y)


if __name__ == '__main__':
    import sys, time
    sys.path.insert(0, 'PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/d_evaluator/code')
    from gen_shape import shape_rho          # comparison only
    T = Trial()
    rng = np.random.default_rng(1)
    r = np.exp(rng.uniform(np.log(1e-3), np.log(1e7), 400))
    th = rng.uniform(0, np.pi / 2, 50)
    t0 = time.time(); F = T.fields(r, th); t1 = time.time()
    d = np.load(NPZ, allow_pickle=True)
    rho2, H2, info = shape_rho(d, r, th)
    print('own eval %.2fs' % (t1 - t0), 'max |H - H_ref| =', np.abs(F['H'] - H2).max(),
          ' max rel rho err', np.max(np.abs(F['rho'] - rho2) / np.maximum(np.abs(rho2), 1e-300)))
    # derivative check by finite differences in r and theta
    h = 1e-6
    Fp = T.fields(r * (1 + h), th); Fm = T.fields(r * (1 - h), th)
    Hr_fd = (Fp['H'] - Fm['H']) / (2 * h * r[:, None])
    print('max rel err H_r vs FD', np.max(np.abs(Hr_fd - F['Hr']) / (np.abs(F['Hr']) + 1e-8 / r[:, None])))
    Fp = T.fields(r, th + h); Fm = T.fields(r, th - h)
    print('max abs err H_th vs FD', np.max(np.abs((Fp['H'] - Fm['H']) / (2 * h) - F['Hth'])))
