"""Exact reconstruction of the X3 trial density from the published coefficient file (float64, vectorized).

Formula (checked against a_generator/stationary.py and d_evaluator/code/gen_shape.py of the published artifacts):
  u = r/L, s = u^2/(1+u^2), q = 1 - (1+u^2)^(-(1-k)/2), chi = u^2/(u^2 + r0^2) (r0 = origin_radius, in units of L),
  H(r,theta) = (k-3)/2 log(1+u^2) + sum_{m=0}^{M} chi^{max(m-1,0)} b_m(q) cos(2 m theta)
             + s^{p3/2} T(2q-1) |cos theta|^{p3-2} sin^2 theta,
  b_m(q) = sum_{j=0}^{374} z[1+m*375+j] B_{j+1}(q)  (order-7 B-splines on the stored knots, first one omitted),
  T(t) = sum_{j<6} z[1+201*375+j] T_j(t) (Chebyshev), p3 = 6 + 2k/(2-k) = 6 + 2/(2c_l-1), k = z[0] = 1/c_l,
  rho = x^2 y exp(H) = r^3 cos^2 theta sin theta exp(H).
This module evaluates H, H_r (d/dr), H_theta, and rho with its polar and Cartesian gradient.
"""
import os
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial.chebyshev import chebval, chebder

# The published coefficient file (IPM Setting I artifacts, a_coefficients/c6g_shape.npz, md5 15f8095f7e79dbfa0c50d75e5fe8997a) is not redistributed here;
# set X3_COEFF_PATH to its location (default: the repository clone used in the run).
DEFAULT = os.environ.get("X3_COEFF_PATH", "PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz")


class X3:
    def __init__(self, path=DEFAULT):
        d = np.load(path, allow_pickle=True)
        z = np.asarray(d["z"], float)
        self.k = float(z[0]); self.coef = z[1:]
        self.L = float(d["L"]); self.deg = int(d["degree"]); self.M = int(d["angular"]); self.sing = int(d["singular"])
        self.order = int(d["spline_order"]); self.r0 = float(d["origin_radius"])
        assert str(d["compact"]) == "matched" and str(d["radial_basis"]) == "spline" and int(d["angular_cap"]) == 0
        self.knots = np.asarray(d["spline_knots"], float)
        assert len(self.knots) == self.deg + self.order + 2
        assert len(self.coef) == (self.M + 1) * self.deg + self.sing
        self.c_l = 1.0 / self.k
        self.p3 = 6.0 + 2.0 * self.k / (2.0 - self.k)
        self.B = BSpline(self.knots, np.eye(self.deg + 1), self.order, extrapolate=False)
        self.cm = self.coef[:(self.M + 1) * self.deg].reshape(self.M + 1, self.deg)   # (M+1, deg)
        self.tcheb = self.coef[(self.M + 1) * self.deg:]                               # (6,)
        self.tcheb_d = chebder(self.tcheb)
        self.m = np.arange(self.M + 1)
        self.jpow = np.maximum(self.m - 1, 0)
        self.stored = dict(c_l=float(d["c_l"]), c=float(d["c"]), L=self.L, k=self.k, R_shape=float(d["R_shape"]))

    # radial profiles ------------------------------------------------------------------------------------------
    def radial(self, r):
        """Return dict of radial quantities at the 1-D array r: b_m(q) chi^j and d/dr of it, the singular radial factor
        and its d/dr, the base term and its d/dr."""
        r = np.asarray(r, float)
        u = r / self.L; u2 = u * u
        s = u2 / (1.0 + u2)
        l1 = np.log1p(u2)
        q = -np.expm1(-(1.0 - self.k) / 2.0 * l1)
        dq_dr = (1.0 - self.k) * (u / self.L) * np.exp(-(3.0 - self.k) / 2.0 * l1)      # (1-k) u/L (1+u^2)^(-(3-k)/2)
        Bv = self.B(q)[:, 1:]                    # (N, deg)
        Bd = self.B(q, nu=1)[:, 1:] * dq_dr[:, None]
        prof = Bv @ self.cm.T                    # (N, M+1)   b_m(q)
        prof_r = Bd @ self.cm.T
        chi = u2 / (u2 + self.r0 ** 2)
        dchi_dr = (2.0 * u / self.L) * self.r0 ** 2 / (u2 + self.r0 ** 2) ** 2
        mult = chi[:, None] ** self.jpow[None, :]                      # chi^j
        mult_r = np.where(self.jpow[None, :] > 0,
                          self.jpow[None, :] * chi[:, None] ** np.maximum(self.jpow[None, :] - 1, 0) * dchi_dr[:, None], 0.0)
        bm = prof * mult
        bm_r = prof_r * mult + prof * mult_r
        # singular radial factor  s^(p3/2) T(2q-1)
        t = 2.0 * q - 1.0
        T = chebval(t, self.tcheb); Td = chebval(t, self.tcheb_d) * 2.0 * dq_dr
        ds_dr = (2.0 * u / self.L) / (1.0 + u2) ** 2
        sp = s ** (self.p3 / 2.0)
        sp_r = (self.p3 / 2.0) * s ** (self.p3 / 2.0 - 1.0) * ds_dr
        sing = sp * T; sing_r = sp_r * T + sp * Td
        base = (self.k - 3.0) / 2.0 * l1
        base_r = (self.k - 3.0) / 2.0 * (2.0 * u / self.L) / (1.0 + u2)
        return dict(r=r, u=u, s=s, q=q, bm=bm, bm_r=bm_r, sing=sing, sing_r=sing_r, base=base, base_r=base_r)

    def angular(self, th):
        th = np.asarray(th, float)
        cos2m = np.cos(2.0 * self.m[:, None] * th[None, :])            # (M+1, Nt)
        dcos2m = -2.0 * self.m[:, None] * np.sin(2.0 * self.m[:, None] * th[None, :])
        ct, st = np.cos(th), np.sin(th)
        act = np.abs(ct)
        e = self.p3 - 2.0
        ang = act ** e * st ** 2
        # d/dtheta of |cos|^e sin^2 = -e sign(cos)|cos|^(e-1) sin^3 + 2 |cos|^e sin cos ; sign(cos)|cos|^(e-1) = cos|cos|^(e-2)
        dang = -e * ct * act ** (e - 2.0) * st ** 3 + 2.0 * act ** e * st * ct
        return dict(th=th, cos2m=cos2m, dcos2m=dcos2m, ct=ct, st=st, ang=ang, dang=dang)

    def H(self, r, th, derivs=True):
        """H and its derivatives on the tensor grid r x th. Returns H, H_r, H_t (arrays (Nr, Nt))."""
        R = self.radial(r); A = self.angular(th)
        H = R["base"][:, None] + R["bm"] @ A["cos2m"] + R["sing"][:, None] * A["ang"][None, :]
        if not derivs:
            return H
        H_r = R["base_r"][:, None] + R["bm_r"] @ A["cos2m"] + R["sing_r"][:, None] * A["ang"][None, :]
        H_t = R["bm"] @ A["dcos2m"] + R["sing"][:, None] * A["dang"][None, :]
        return H, H_r, H_t

    def rho(self, r, th, derivs=True):
        """rho, rho_r, rho_theta on the tensor grid; also the Cartesian gradient (rho_x, rho_y)."""
        r = np.asarray(r, float); th = np.asarray(th, float)
        ct, st = np.cos(th), np.sin(th)
        fac_ang = ct ** 2 * st
        fac_ang_t = -2.0 * ct * st ** 2 + ct ** 3
        if not derivs:
            H = self.H(r, th, derivs=False)
            return (r ** 3)[:, None] * fac_ang[None, :] * np.exp(H)
        H, H_r, H_t = self.H(r, th)
        eH = np.exp(H)
        rho = (r ** 3)[:, None] * fac_ang[None, :] * eH
        rho_r = (3.0 * r ** 2)[:, None] * fac_ang[None, :] * eH + rho * H_r
        rho_t = (r ** 3)[:, None] * (fac_ang_t[None, :] + fac_ang[None, :] * H_t) * eH
        rho_x = rho_r * ct[None, :] - rho_t * st[None, :] / r[:, None]
        rho_y = rho_r * st[None, :] + rho_t * ct[None, :] / r[:, None]
        return dict(rho=rho, rho_r=rho_r, rho_t=rho_t, rho_x=rho_x, rho_y=rho_y, H=H, H_r=H_r, H_t=H_t)


if __name__ == "__main__":
    import sys, time
    sys.path.insert(0, os.environ.get("X3_EVALUATOR_DIR", "PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/d_evaluator/code"))   # published evaluator (gen_shape.py) for the self-test
    import gen_shape
    X = X3()
    print("k", X.k, "c_l", X.c_l, "L", X.L, "p3", X.p3, "stored", X.stored)
    d = np.load(DEFAULT, allow_pickle=True)
    rng = np.random.default_rng(1)
    r = np.exp(rng.uniform(np.log(1e-4), np.log(1e7), 400)); r.sort()
    th = np.linspace(0, np.pi / 2, 257)
    t0 = time.time(); rho_ref, H_ref, info = gen_shape.shape_rho(d, r, th); t1 = time.time()
    out = X.rho(r, th); t2 = time.time()
    print("gen_shape %.2fs, x3 %.2fs" % (t1 - t0, t2 - t1))
    print("max |H - H_ref| =", np.max(np.abs(out["H"] - H_ref)))
    print("max rel |rho - rho_ref| =", np.max(np.abs(out["rho"] - rho_ref) / (np.abs(rho_ref) + 1e-300)))
    # derivative check by central differences in r and theta
    h = 1e-6
    Hp = X.H(r * (1 + h), th, derivs=False); Hm = X.H(r * (1 - h), th, derivs=False)
    fd_r = (Hp - Hm) / (2 * h * r[:, None])
    print("max |H_r - fd| / (1+|H_r|) =", np.max(np.abs(out["H_r"] - fd_r) / (1 + np.abs(out["H_r"]))))
    thi = th[1:-1]
    Hp = X.H(r, thi + h, derivs=False); Hm = X.H(r, thi - h, derivs=False)
    fd_t = (Hp - Hm) / (2 * h)
    print("max |H_t - fd| / (1+|H_t|) =", np.max(np.abs(out["H_t"][:, 1:-1] - fd_t) / (1 + np.abs(out["H_t"][:, 1:-1]))))
    # a(0,0) = lim rho/(x^2 y) = exp(H(0)) must be 1: H(r->0) -> b_0(0)+ ... = 0 since B_0 omitted
    print("H at r=1e-6, several theta:", X.H(np.array([1e-6]), np.array([0.3, 0.9, 1.4]), derivs=False))
