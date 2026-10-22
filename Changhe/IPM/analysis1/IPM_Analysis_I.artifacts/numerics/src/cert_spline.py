"""Arb (python-flint) exact per-cell Taylor coefficients of the trial's B-spline part, and exactification of the
dependent coefficients (join corrections Ei, Eo and the normalization coefficient).

B-spline derivatives at a cell start t_a^+ (right limit) for all active basis functions, by the recursion
  B_{i,p}^{(nu)} = p [ B_{i,p-1}^{(nu-1)} / (t_{i+p} - t_i)  -  B_{i+1,p-1}^{(nu-1)} / (t_{i+p+1} - t_{i+1}) ]
down to degree p - nu, where the degree-(p-nu) B-splines are evaluated by Cox-de Boor on the knot interval of the cell.
All knots and coefficients are exact doubles, so every quantity here is an exact rational enclosed in an arb ball.
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, arb_mat, ctx
from math import factorial


def deboor_values(knots, p, j, q):
    """Values of B_{i,p}(q) for i = j-p..j (nonzero on [t_j, t_{j+1})), knots: list of arb. Returns list of p+1 arb."""
    N = [arb(0)] * (p + 1); N[p] = arb(1)
    for d in range(1, p + 1):
        Nn = [arb(0)] * (p + 1)
        for a in range(p + 1):
            i = j - p + a
            if i + d < j or i > j: continue
            v = arb(0)
            den1 = knots[i + d] - knots[i]
            if den1 != 0: v += (q - knots[i]) / den1 * N[a]
            den2 = knots[i + d + 1] - knots[i + 1]
            if den2 != 0 and a + 1 <= p: v += (knots[i + d + 1] - q) / den2 * N[a + 1]
            Nn[a] = v
        N = Nn
    return N


def deboor_derivs(knots, p, j, q, nu_max):
    """B_{i,p}^{(nu)}(q) for i = j-p..j and nu = 0..nu_max (q in [t_j, t_{j+1})).  Returns list over nu of lists (p+1)."""
    # derivative order nu: combination of degree p-nu B-splines B_{l, p-nu}, l = i..i+nu, with coefficients from the
    # recursion; compute iteratively: start with the vector e_i (coefficient of B_{i,p}), apply the derivative map nu times
    out = []
    for nu in range(nu_max + 1):
        d = p - nu
        if d < 0: break
        vals_d = deboor_values(knots, d, j, q) if d >= 0 else None      # B_{l,d}(q), l = j-d..j
        res = []
        for a in range(p + 1):
            i = j - p + a
            # coefficient vector over l of B_{i,p}^{(nu)} in terms of B_{l,d}: computed by the recursion
            coef = {i: arb(1)}
            deg = p
            for _ in range(nu):
                newc = {}
                for l, c in coef.items():
                    den1 = knots[l + deg] - knots[l]
                    if den1 != 0: newc[l] = newc.get(l, arb(0)) + deg * c / den1
                    den2 = knots[l + deg + 1] - knots[l + 1]
                    if den2 != 0: newc[l + 1] = newc.get(l + 1, arb(0)) - deg * c / den2
                coef = newc; deg -= 1
            v = arb(0)
            for l, c in coef.items():
                idx = l - (j - d)
                if 0 <= idx <= d: v += c * vals_d[idx]
            res.append(v)
        out.append(res)
    return out


class SplineCells:
    def __init__(self, knots_f, p, S_f):
        """knots_f: full knot vector (floats), p degree, S_f: coefficients (M, nb) floats (modes x basis)."""
        self.p = p; self.knots_f = np.asarray(knots_f, float)
        self.knots = [arb(float(x)) for x in self.knots_f]
        self.S = [[arb(float(x)) for x in row] for row in S_f]       # M x nb
        self.M = len(S_f); self.nb = len(S_f[0])
        # cells: nondegenerate knot intervals [t_j, t_{j+1}) for j = p .. len-p-2
        self.cell_j = [j for j in range(p, len(self.knots_f) - p - 1) if self.knots_f[j + 1] > self.knots_f[j]]

    def cell_taylor(self, ci):
        """Taylor coefficients (arb) at the cell start of a_m on cell ci, for all modes: list over nu of list over m."""
        j = self.cell_j[ci]; p = self.p
        D = deboor_derivs(self.knots, p, j, self.knots[j], p)          # [nu][a]
        T = []
        for nu in range(p + 1):
            inv = arb(1) / factorial(nu)
            row = []
            for m in range(self.M):
                v = arb(0)
                for a in range(p + 1):
                    i = j - p + a
                    c = self.S[m][i]
                    if c != 0: v += c * D[nu][a]
                row.append(v * inv)
            T.append(row)
        return T


def _test():
    from scipy.interpolate import BSpline
    ctx.prec = 200
    d = np.load(sys.argv[1] if len(sys.argv) > 1 else "data/trial_v2_h0.008.npz")
    knots = d["knots"]; S = d["S"][:5]; p = int(d["p"])
    sc = SplineCells(knots, p, S)
    spl = BSpline(knots, S.T, p, extrapolate=True)
    t0 = time.time()
    worst = 0.0
    for ci in (0, 1, 100, 700, len(sc.cell_j) - 1):
        T = sc.cell_taylor(ci); ta = sc.knots_f[sc.cell_j[ci]]
        for nu in range(p + 1):
            ref = spl(np.array([ta]), nu=nu)[0] / factorial(nu)
            for m in range(5):
                a = T[nu][m]
                worst = max(worst, abs(float(a.mid()) - ref[m]) / (1 + abs(ref[m])))
        # polynomial reproduces the spline inside the cell?
        tm = 0.5 * (sc.knots_f[sc.cell_j[ci]] + sc.knots_f[sc.cell_j[ci] + 1]); tau = tm - ta
        val = sum(float(T[nu][0].mid()) * tau ** nu for nu in range(p + 1))
        print("cell %d: Taylor poly at midpoint %.15e vs spline %.15e (diff %.1e), rad of c0 %.1e" % (ci, val, spl(np.array([tm]))[0, 0], abs(val - spl(np.array([tm]))[0, 0]), float(T[0][0].rad())))
    print("max |arb mid - scipy| / (1+|ref|) over tested cells/orders/modes: %.2e ; time %.1fs for 5 cells x 5 modes" % (worst, time.time() - t0))


if __name__ == "__main__":
    _test()
