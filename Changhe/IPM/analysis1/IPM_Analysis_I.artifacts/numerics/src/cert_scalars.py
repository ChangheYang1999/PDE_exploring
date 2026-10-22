"""Rigorous scalars of the explicit modal trial (SPEC v1 item S1), Arb ball arithmetic from the certified Green data.

Inputs: data/cert_green.npz (A_n, B_n at sub-cell boundaries as enclosing mid/rad doubles; Taylor coefficients of a_m per
sub-cell), trial file, data/cert_coeffs.json (exactified coefficients; not needed inside the middle region).
At a point t in sub-cell ci (tau = t - t_a): exact closed forms (cert_green.integ_scaled) give A_n(t), B_n(t) from the
boundary values; a_m(t) and a_m'(t) from the Taylor polynomial; then on the x-axis (theta = 0):
  V_1(x, 0) = c_l x + U_1(x, 0),  U_1(x,0) = U_r(r, 0) = -psi_theta/r = -(1/r) sum_n 2n psi_n(r)
  mu(x) := d_y V_2(x, 0) = c_l + psi_xy(x, 0) = c_l + sum_n 2n (psi_n'(x)/x - psi_n(x)/x^2)       (so d_x V_1 = 2 c_l - mu)
  g(x) := rho_y(x, 0) = (1/r) rho_theta = (1/x) sum_j (2j+1) R_j(x),   R_j = e^{3t} T_j[a].
x_* by interval Newton on V_1(x, 0) (derivative 2 c_l - mu on the interval), then mu(x_*) - 1, g_* = g(x_*), A = 2 c_l - 1.
Usage: python3 cert_scalars.py data/cert_green.npz data/trial_v2_h0.008.npz out.json
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx
from cert_green import integ_scaled
from midrad import U


class ScalarCert:
    def __init__(self, green, trial, prec=200):
        ctx.prec = prec
        d = np.load(green); self.d = d
        self.tb = [arb(float(m), float(r)) for m, r in zip(d["tb"], d["tb_rad"])]
        self.tbf = d["tb"]; self.nc = len(self.tb) - 1
        self.Am, self.Ar, self.Bm, self.Br = d["A_mid"], d["A_rad"], d["B_mid"], d["B_rad"]
        self.Tm, self.Tr = d["T_mid"], d["T_rad"]
        self.Nf = self.Am.shape[1]; self.M = self.Tm.shape[2]; self.p = self.Tm.shape[1] - 1
        tr = np.load(trial); self.k = arb(float(tr["k"])); self.c_l = 1 / self.k

    def R_from_a(self, a):
        M = self.M; R = [arb(0)] * (M + 1)
        def add(freq, coef):
            if freq < 0: freq, coef = -freq, -coef
            if freq == 0: return
            j = (freq - 1) // 2
            if j <= M: R[j] += coef
        for m in range(M):
            am = a[m] / 8
            add(2 * m + 1, am); add(-(2 * m - 1), am); add(2 * m + 3, am); add(-(2 * m - 3), am)
        return R

    def cell_of(self, t):
        tf = float(t.mid()); ci = int(np.searchsorted(self.tbf, tf, side="right") - 1)
        ci = min(max(ci, 0), self.nc - 1)
        assert self.tb[ci] <= t and t <= self.tb[ci + 1] or (abs(tf - self.tbf[ci]) < 1e-12 or abs(tf - self.tbf[ci + 1]) < 1e-12), "t outside cell"
        return ci

    def modes_at(self, t):
        """(a_m, a_m') polynomials evaluated at t (lists of arb), R_j, dR_j/dt (lists), psi_n, psi_n' (lists) at t (arb ball)."""
        ci = self.cell_of(t); ta = self.tb[ci]; tau = t - ta
        T = [[arb(float(self.Tm[ci, q, m]), float(self.Tr[ci, q, m])) for m in range(self.M)] for q in range(self.p + 1)]
        a = [sum((T[q][m] * tau ** q for q in range(self.p + 1)), arb(0)) for m in range(self.M)]
        ad = [sum((T[q][m] * q * tau ** (q - 1) for q in range(1, self.p + 1)), arb(0)) for m in range(self.M)]
        e3 = (3 * t).exp()
        R = [e3 * x for x in self.R_from_a(a)]
        Rt = [e3 * (3 * x + y) for x, y in zip(self.R_from_a(a), self.R_from_a(ad))]
        # f-polynomial on the cell (in tau): F_n with f_n(e^t) = e^{2 t_a} e^{2 tau} F_n(tau)  -> f-terms alpha' = 2, coefficients e^{2 ta} F
        Rc = [self.R_from_a(T[q]) for q in range(self.p + 1)]
        dRc = [[(3 * Rc[q][j] + (Rc[q + 1][j] * (q + 1) if q + 1 <= self.p else arb(0))) for j in range(self.M + 1)] for q in range(self.p + 1)]
        F = [[arb(0)] * self.Nf for _ in range(self.p + 1)]
        for q in range(self.p + 1):
            for j in range(self.M + 1):
                up = (dRc[q][j] - (2 * j + 1) * Rc[q][j]) / 2; dn = (dRc[q][j] + (2 * j + 1) * Rc[q][j]) / 2
                if j + 1 <= self.Nf: F[q][j] += up
                if j >= 1: F[q][j - 1] += dn
        e2ta = (2 * ta).exp(); h = self.tb[ci + 1] - ta
        psi = []; dpsi = []; r = t.exp()
        for n in range(1, self.Nf + 1):
            coeffs = [F[q][n - 1] * e2ta for q in range(self.p + 1)]
            lam = 2 * n + 2 + 2; mu = 2 - 2 * n + 2
            A0 = arb(float(self.Am[ci, n - 1]), float(self.Ar[ci, n - 1])); B1 = arb(float(self.Bm[ci + 1, n - 1]), float(self.Br[ci + 1, n - 1]))
            An = (-2 * n * tau).exp() * A0 + e2ta * integ_scaled(arb(lam), coeffs, arb(0), tau, -2 * n * tau)
            Bn = (-2 * n * (h - tau)).exp() * B1 + e2ta * integ_scaled(arb(mu), coeffs, tau, h, 2 * n * tau)
            psi.append((An + Bn) / (4 * n)); dpsi.append((Bn - An) / (2 * r))
        return dict(a=a, R=R, Rt=Rt, psi=psi, dpsi=dpsi, r=r, ci=ci)

    def axis(self, t):
        """V_1(x,0), mu(x) = d_y V_2(x,0), g(x) = rho_y(x,0), rho(x, small) data at x = e^t."""
        md = self.modes_at(t); x = md["r"]
        U1 = -sum((2 * n * md["psi"][n - 1] for n in range(1, self.Nf + 1)), arb(0)) / x
        V1 = self.c_l * x + U1
        mu = self.c_l + sum((2 * n * (md["dpsi"][n - 1] / x - md["psi"][n - 1] / (x * x)) for n in range(1, self.Nf + 1)), arb(0))
        g = sum(((2 * j + 1) * md["R"][j] for j in range(self.M + 1)), arb(0)) / x
        return V1, mu, g

    def find_xstar(self, x_guess=8.600063803, iters=6):
        """Interval Newton: start from a float Newton refinement, then verify contraction on an interval."""
        t = arb(np.log(x_guess))
        for _ in range(4):                       # float-level Newton (midpoints)
            V1, mu, g = self.axis(arb(float(t.mid())))
            t = arb(float(t.mid())) - V1 / ((2 * self.c_l - mu) * t.exp())      # dV1/dt = x dV1/dx = x (2 c_l - mu)
        # interval Newton on t-interval of radius eps
        for eps in (1e-9, 1e-11, 1e-13):
            T = arb(float(t.mid()), eps)
            V1m, _, _ = self.axis(arb(float(T.mid())))
            _, muT, _ = self.axis(T)
            Nt = arb(float(T.mid())) - V1m / ((2 * self.c_l - muT) * T.exp())
            if T.contains_interior(Nt) if hasattr(T, "contains_interior") else (Nt.lower() > T.lower() and Nt.upper() < T.upper()):
                tstar = Nt
                return tstar, True
        return t, False


def main(green, trial, out):
    t0 = time.time(); S = ScalarCert(green, trial)
    tstar, ok = S.find_xstar()
    xstar = tstar.exp()
    V1, mu, g = S.axis(tstar)
    A = 2 * S.c_l - 1
    res = dict(x_star=xstar.str(20), x_star_rad=float(xstar.rad()), newton_contracted=ok, V1_at_xstar=V1.str(5), mu_minus_1=(mu - 1).str(8),
               g_star=g.str(20), A=A.str(20), c_l=S.c_l.str(25), time=time.time() - t0)
    print(json.dumps(res, indent=1)); json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
