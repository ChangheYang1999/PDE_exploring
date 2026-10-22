"""Rigorous (Arb ball arithmetic, python-flint) point/box enclosures of the X3 trial: H, H_r, H_theta, rho, rho_r, rho_theta.
The coefficient file's float64 numbers are taken as exact (they define the trial). Inputs r, theta may be arb balls
(boxes). Every operation is a ball operation, so the outputs are rigorous enclosures of the exact formula values.
B-splines: de Boor recursion (Cox-de Boor) on the stored knots, in ball arithmetic. For a box in q straddling knots the
recursion is still valid (each piece is evaluated as the same polynomial formula; the B-spline recursion with the
standard convention 0/0 = 0 is exact on each knot interval and we evaluate it with the index range determined by the
knot interval(s) covered: for a straddling box we split at the knots and take the union).
"""
import os, sys, time
import numpy as np
from flint import arb, ctx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x3 import X3, DEFAULT


class X3Arb:
    def __init__(self, path=DEFAULT, prec=100):
        ctx.prec = prec
        self.X = X3(path)
        X = self.X
        self.k = arb(X.k); self.L = arb(X.L); self.r0 = arb(X.r0)
        self.knots = [arb(float(t)) for t in X.knots]
        self.knots_f = X.knots.copy()
        self.deg = X.deg; self.order = X.order; self.M = X.M
        self.cm = [[arb(float(v)) for v in row] for row in X.cm]      # (M+1) x deg
        self.tcheb = [arb(float(v)) for v in X.tcheb]
        self.p3 = arb(6) + 2 * self.k / (2 - self.k)
        self.one = arb(1)

    # ---- B-splines of order p on knots t at q: values of all B_{i,p} nonzero on the knot interval containing q
    def bspline_values(self, q, nu=0):
        """Return list of (index i, B_i(q), B_i'(q)) for the order-7 B-splines nonzero on the knot interval(s) covered by q.
        q is an arb ball. If q straddles interior knots, evaluate on each knot interval and take unions."""
        kf = self.knots_f; p = self.order
        lo, hi = float(q.lower()), float(q.upper())
        # closed-span selection (outward): every nondegenerate span [kf[j], kf[j+1]] that intersects the closed interval
        # [lo, hi] (verifier audit 2026-10-20T13:33Z: a box at an exact knot must include both adjacent spans)
        lo_ = np.nextafter(lo, -np.inf); hi_ = np.nextafter(hi, np.inf)
        js = [j for j in range(p, len(kf) - p - 1) if kf[j + 1] > kf[j] and kf[j + 1] >= lo_ and kf[j] <= hi_]
        if not js:
            js = [len(kf) - p - 2] if lo >= kf[-1] else [p]
        results = {}
        for j in js:
            vals, ders = self._deboor(q, j)
            for a in range(p + 1):
                i = j - p + a
                if i in results:
                    v0, d0 = results[i]; results[i] = (v0.union(vals[a]), d0.union(ders[a]))
                else:
                    results[i] = (vals[a], ders[a])
        return results

    def _deboor(self, q, j):
        """Cox-de Boor on knot interval j (kf[j] <= q < kf[j+1]) for B-splines i = j-p..j of order p; returns values and
        first derivatives (lists of length p+1)."""
        t = self.knots; p = self.order
        # N^0: only B_{j,0} = 1
        N = [arb(0)] * (p + 1); N[p] = arb(1)          # N[a] corresponds to i = j - p + a, at degree 0 only i = j nonzero
        # build up degrees d = 1..p ; keep degree p-1 values for the derivative
        Nprev = None
        for d in range(1, p + 1):
            Nn = [arb(0)] * (p + 1)
            for a in range(p + 1):
                i = j - p + a
                if i + d < j or i > j:        # B_{i,d} nonzero only for j-d <= i <= j
                    continue
                v = arb(0)
                den1 = t[i + d] - t[i]
                if den1 != 0 and a <= p:
                    v += (q - t[i]) / den1 * N[a]
                den2 = t[i + d + 1] - t[i + 1]
                if den2 != 0 and a + 1 <= p:
                    v += (t[i + d + 1] - q) / den2 * N[a + 1]
                Nn[a] = v
            if d == p:
                Nprev = N
            N = Nn
        # derivative: B_{i,p}' = p [ B_{i,p-1}/(t_{i+p}-t_i) - B_{i+1,p-1}/(t_{i+p+1}-t_{i+1}) ]
        D = [arb(0)] * (p + 1)
        for a in range(p + 1):
            i = j - p + a
            v = arb(0)
            den1 = t[i + p] - t[i]
            if den1 != 0: v += Nprev[a] / den1
            den2 = t[i + p + 1] - t[i + 1]
            if den2 != 0 and a + 1 <= p: v -= Nprev[a + 1] / den2
            D[a] = p * v
        return N, D

    def H(self, r, th):
        """Enclosures of H, H_r, H_theta at (r, th) (arb balls). Returns (H, H_r, H_t)."""
        k, L, r0 = self.k, self.L, self.r0
        u = r / L; u2 = u * u
        l1 = u2.log1p()
        s = u2 / (1 + u2)
        q = -(-(1 - k) / 2 * l1).expm1()
        dq_dr = (1 - k) * (u / L) * (-(3 - k) / 2 * l1).exp()
        B = self.bspline_values(q)
        # b_m(q) and d/dr for every m
        bm = [arb(0)] * (self.M + 1); bmr = [arb(0)] * (self.M + 1)
        for i, (v, d) in B.items():
            j = i - 1                              # coefficient index (first spline omitted)
            if j < 0 or j >= self.deg: continue
            for m in range(self.M + 1):
                c = self.cm[m][j]
                if c != 0:
                    bm[m] += c * v; bmr[m] += c * d * dq_dr
        chi = u2 / (u2 + r0 * r0)
        dchi = (2 * u / L) * r0 * r0 / ((u2 + r0 * r0) ** 2)
        # angular: cos(2 m th) via recurrence
        c1 = (2 * th).cos(); s1 = (2 * th).sin()
        Hv = (k - 3) / 2 * l1; Hr = (k - 3) / 2 * (2 * u / L) / (1 + u2); Ht = arb(0)
        cm_, sm_ = arb(1), arb(0)                  # cos(0), sin(0)
        chipow = arb(1); chipow_prev = arb(1)
        for m in range(self.M + 1):
            if m >= 1:
                sm_, cm_ = (2 * m * th).sin_cos()                        # direct (box-safe): sin(2m th), cos(2m th)
            jp = max(m - 1, 0)
            if m == 2: chipow = chi
            elif m > 2: chipow = chipow * chi
            if jp == 0:
                mult, mult_r = arb(1), arb(0)
            else:
                mult = chipow
                chipow_m1 = arb(1) if jp == 1 else chipow_prev
                mult_r = jp * chipow_m1 * dchi                # chi^{jp-1} kept separately (no division: r = 0 safe)
            chipow_prev = chipow if jp >= 1 else arb(1)
            Hv += bm[m] * mult * cm_
            Hr += (bmr[m] * mult + bm[m] * mult_r) * cm_
            Ht += bm[m] * mult * (-2 * m * sm_)
        # singular term s^{p3/2} T(2q-1) |cos th|^{p3-2} sin^2 th
        tt = 2 * q - 1
        T = arb(0); Td = arb(0)
        # Chebyshev via recurrence T_j and T_j'
        T0, T1 = arb(1), tt; U0, U1 = arb(0), arb(1)   # T_j' = j U_{j-1}
        Tj = [T0, T1]; Uj = [U0, U1]
        for j in range(2, 6):
            Tj.append(2 * tt * Tj[-1] - Tj[-2]); Uj.append(2 * tt * Uj[-1] - Uj[-2])
        for j in range(6):
            T += self.tcheb[j] * Tj[j]
            if j >= 1: Td += self.tcheb[j] * j * Uj[j]          # T_j' = j U_{j-1}; Uj[j] holds U_{j-1} (list starts U_{-1}=0, U_0=1)
        Td = Td * 2 * dq_dr
        ds_dr = (2 * u / L) / ((1 + u2) ** 2)
        sp = s ** (self.p3 / 2); sp_r = (self.p3 / 2) * s ** (self.p3 / 2 - 1) * ds_dr
        sing = sp * T; sing_r = sp_r * T + sp * Td
        ct, st = th.cos(), th.sin(); act = abs(ct)
        e = self.p3 - 2
        ang = act ** e * st * st
        dang = -e * ct * act ** (e - 2) * st ** 3 + 2 * act ** e * st * ct
        Hv += sing * ang; Hr += sing_r * ang; Ht += sing * dang
        return Hv, Hr, Ht

    def rho(self, r, th):
        Hv, Hr, Ht = self.H(r, th)
        ct, st = th.cos(), th.sin()
        fac = ct * ct * st; fac_t = -2 * ct * st * st + ct ** 3
        eH = Hv.exp()
        rho = r ** 3 * fac * eH
        rho_r = 3 * r * r * fac * eH + rho * Hr
        rho_t = r ** 3 * (fac_t + fac * Ht) * eH
        return dict(rho=rho, rho_r=rho_r, rho_t=rho_t, H=Hv, H_r=Hr, H_t=Ht)


if __name__ == "__main__":
    A = X3Arb(prec=100)
    X = A.X
    rng = np.random.default_rng(3)
    pts = [(float(np.exp(rng.uniform(np.log(1e-3), np.log(1e5)))), float(rng.uniform(0.01, np.pi / 2 - 0.01))) for _ in range(12)]
    pts += [(8.6, 0.0), (1.0, np.pi / 2), (0.153, 0.7)]
    t0 = time.time()
    worst = 0
    for (rr, tt) in pts:
        out = A.rho(arb(rr), arb(tt))
        F = X.rho(np.array([rr]), np.array([tt]))
        for key in ("H", "H_r", "H_t", "rho", "rho_r", "rho_t"):
            a = out[key]; f = float(F[key][0, 0])
            ok = a.contains(arb(f)) or abs(float(a.mid()) - f) <= 1e-12 * (1 + abs(f))
            worst = max(worst, abs(float(a.mid()) - f) / (1 + abs(f)))
            if not ok and abs(float(a.mid()) - f) > 1e-10 * (1 + abs(f)):
                print("MISMATCH", rr, tt, key, a, f)
        print("r=%.4g th=%.4f  rho=%s  rad(H)=%.1e" % (rr, tt, out["rho"].str(12), float(out["H"].rad())))
    dt = (time.time() - t0) / len(pts)
    print("per point %.3fs ; worst |mid - float64| / (1+|f|) = %.2e" % (dt, worst))
    # box evaluation test: r in [8.5, 8.7], th in [0, 0.05]
    t0 = time.time()
    out = A.rho(arb(8.6, 0.1), arb(0.025, 0.025))
    print("box: rho =", out["rho"], " H =", out["H"], " time %.3fs" % (time.time() - t0))
