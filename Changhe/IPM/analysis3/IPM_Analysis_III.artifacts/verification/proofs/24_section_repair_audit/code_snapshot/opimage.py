"""Exact operator images (ball arithmetic) for the full linearization at the exact modal trial (s2-num, 2026-10-28).

  L h = (V.grad - 1) h + (U[h] + (c[h]/3) X).grad rho~,   V = c_l X + U[rho~],  c_l = 1/k (exact rational),
  h = x^2 y b(t) cos(2 m theta) = e^{3t} sum_j P_jm b(t) sin((2j+1) theta).
Output: the factor modes G_N(t) := e^{-3t} (L h)_N  of  L h = sum_N (L h)_N(t) sin((2N+1) theta), as exponential polynomials on
integration cells (local variable sigma = t - t_a).  Conventions mirror analysis1 numerics src/lin_fast.py (validated there by
the identity L rho~ = 2 eps~ + rho~ - X.grad rho~/3), re-derived here:
  transport:   G_N += P_Nm [ (3 c_l - 1) b + c_l b' ]                                  (per exponential term: (3c_l-1+c_l e) p + c_l p')
  background velocity on h, n = 1..Nf:  Pe_n = e^{-2t}(A_n+B_n)/2, Qe_n = e^{-2t}(B_n-A_n)/2:
               coef  = -(1/2) Pe_n P_jm (3b + b')  -> sine frequencies 2j+1+2n, 2j+1-2n
               coef2 = +(1/2) Qe_n (2j+1) P_jm b   -> sine frequencies 2n+2j+1, 2n-2j-1
  velocity of h on the background (n in the 5 modes of h), with dR_j = 3 Rhat_j + Rhat_j' and Rhat_j = sum_m P_jm a_m:
               coef  = -(1/2) Pe^h_n dR_j,  coef2 = +(1/2) Qe^h_n (2j+1) Rhat_j, same frequencies
  strain term: G_N += (c[h]/3) dR_N.
  addsin(f, coef): f < 0 -> (-f, -coef); f = 0 dropped; N = (f-1)/2.
Exact cancellation at the origin: for mode n = 1, B^h_1(t) = 2 c[h] e^{2t} + Bt^h_1(t), Bt^h_1 = -e^{2t} int_{-oo}^t f^h_1; the part
2 c[h] e^{2t} together with the strain term equals c[h] M, M = e^{-3t} ((-2x/3, 4y/3).grad rho~) in modes, whose constant term at the
origin vanishes identically ((-2x/3, 4y/3).grad(x^2 y) = 0; verified in exact rational arithmetic in M_leading_check()).
"""
import math, time, sys, os
from fractions import Fraction
from flint import arb, arb_mat, fmpq, fmpq_mat, fmpq_poly, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb, prim_S, moment_left, moment_right, moment_minf, moment_pinf, integrate_ep


def addsin(acc, f, ep):
    """acc: dict N -> ExpPoly; add ep at sine frequency f."""
    if f < 0: f, ep = -f, ep.scale(arb(-1))
    if f == 0: return
    N = (f - 1) // 2
    if N in acc: acc[N] = acc[N] + ep
    else: acc[N] = ep


class Cells:
    """Integration cells: the trial's spline cells, plus finite sub-cells of the inner and outer regions at the given extra
    boundaries, plus the two half-infinite end cells. Each cell: dict(kind, ta (arb), h (arb or None), tq (fmpq left end),
    trial_cell (index or None), shift (fmpq: t_a - t_- for inner sub-cells, t_a - t_+ for outer)."""
    def __init__(self, T, inner_extra, outer_extra):
        """inner_extra: list of positive fmpq offsets d (cells [t_- - d_i, t_- - d_{i-1}]); outer_extra: positive offsets beyond t_+."""
        self.T = T
        cells = []
        din = sorted(set(fmpq(x) for x in inner_extra)); dout = sorted(set(fmpq(x) for x in outer_extra))
        # half-infinite inner cell (-oo, t_- - din[-1]]
        lo_q = T.t_lo_q - (din[-1] if din else fmpq(0))
        cells.append(dict(kind="minf", tq=lo_q, ta=q2arb(lo_q), h=None, trial_cell=None, shift=-(din[-1] if din else fmpq(0))))
        bounds = [T.t_lo_q - d for d in reversed(din)] + [T.t_lo_q]
        for i in range(len(bounds) - 1):
            cells.append(dict(kind="inner", tq=bounds[i], ta=q2arb(bounds[i]), h=q2arb(bounds[i + 1] - bounds[i]), hq=bounds[i + 1] - bounds[i], trial_cell=None, shift=bounds[i] - T.t_lo_q))
        for ci in range(T.nc):
            cells.append(dict(kind="mid", tq=T.tb_q[ci], ta=T.tb[ci], h=q2arb(T.h_q[ci]), hq=T.h_q[ci], trial_cell=ci, shift=fmpq(0)))
        bounds = [T.t_hi_q] + [T.t_hi_q + d for d in dout]
        for i in range(len(bounds) - 1):
            cells.append(dict(kind="outer", tq=bounds[i], ta=q2arb(bounds[i]), h=q2arb(bounds[i + 1] - bounds[i]), hq=bounds[i + 1] - bounds[i], trial_cell=None, shift=bounds[i] - T.t_hi_q))
        hi_q = T.t_hi_q + (dout[-1] if dout else fmpq(0))
        cells.append(dict(kind="pinf", tq=hi_q, ta=q2arb(hi_q), h=None, trial_cell=None, shift=hi_q - T.t_hi_q))
        self.cells = cells
        self.n = len(cells)
        self.tq = [c["tq"] for c in cells]
        # index of the first mid cell and the number of mid cells
        self.first_mid = next(i for i, c in enumerate(cells) if c["kind"] == "mid")
        self.n_mid = T.nc

    def find(self, tq):
        """index of the cell containing t = tq (left-closed)"""
        for i in range(self.n - 1, -1, -1):
            if self.tq[i] <= tq: return i
        return 0


class Background:
    """Per-cell exponential-polynomial data of the trial: Rhat_j, dR_j, Pe_n, Qe_n (computed on demand, cached per cell)."""
    def __init__(self, T, cells, nmax=None, full_cells=()):
        self.T = T; self.cells = cells
        self.nmax = nmax; self.full_cells = set(full_cells)
        if not hasattr(T, "A"): T.build_green()
        self.cache = {}
        self.a_in = T.a_inner(); self.a_out = T.a_outer()
        self.Rhat_in = T.Rhat_from_a(self.a_in); self.Rhat_out = T.Rhat_from_a(self.a_out)
        self.fhat_in = T.fhat_from_Rhat(self.Rhat_in); self.fhat_out = T.fhat_from_Rhat(self.Rhat_out)

    def get(self, ic):
        if ic in self.cache: return self.cache[ic]
        T = self.T; c = self.cells.cells[ic]; kind = c["kind"]; Nf = T.Nf
        if kind == "mid":
            ci = c["trial_cell"]
            Rc = T.cell_a[ci] * T.P.transpose()
            Rhat = [ExpPoly([(fmpq(0), [Rc[r_, j] for r_ in range(T.p + 1)])]) for j in range(T.Mj)]
            fhat = [ExpPoly([(fmpq(0), T.cell_fhat[ci][n - 1])]) for n in range(1, Nf + 1)]
            ta = T.tb[ci]; h = q2arb(T.h_q[ci])
            Abd = T.A[ci]; Bbd = T.B[ci + 1]
            hA, hB = h, h
        else:
            # inner/outer (sub)cells: re-expand the half-infinite formulas about the cell's left end
            s = c["shift"]
            if kind in ("minf", "inner"):
                Rhat = [ep.shift(q2arb(s)) for ep in self.Rhat_in]; fhat = [ep.shift(q2arb(s)) for ep in self.fhat_in]
                # boundary values: A at the left end: A_n(t) = e^{4t} int_{-oo}^{sigma_0} e^{(2n+4)(s' - sigma_0)} fhat_in(s') ds' with t = t_- + sigma_0
                # simpler: A_n(t_a) via closed form on (-oo, t_a]; B_n(t_b) via B(t_-) and the integral over [t_a, t_b]
                ta = c["ta"]; h = c["h"]
                Abd = []; 
                for n in range(1, Nf + 1):
                    # A_n(t_a) = e^{-2n t_a} int_{-oo}^{t_a} e^{(2n+2)s} f_n ds, f_n = e^{2 t_a} e^{2 sigma} fhat(sigma) (fhat re-expanded at t_a)
                    Abd.append((4 * ta).exp() * integrate_ep(fhat[n - 1].mul_exp(fmpq(2 * n + 4)), "minf"))
                if kind == "minf":
                    # B at the right end t_a of the half-infinite cell: B_n(t_a) = e^{-2n (t_- - t_a)} B_n(t_-) + e^{4 t_a} int_0^{hb} e^{(4-2n) s} fhat_a(s) ds
                    hb = q2arb(-s); Bbd = []
                    for n in range(1, Nf + 1):
                        mu = arb(4 - 2 * n); mom = arb(0)
                        for e, cs in fhat[n - 1].terms.items():
                            for p_, cp in enumerate(cs):
                                if cp != 0: mom += cp * moment_right(q2arb(e) + mu, p_, hb)
                        Bbd.append((-2 * n * hb).exp() * T.B[0][n - 1] + (4 * ta).exp() * mom)
                    hB = None; hA = None
                else:
                    # B_n(t_b): if t_b = t_- use T.B[0]; else B_n(t_b) = e^{-2n (t_- - t_b)} B_n(t_-) + e^{2n t_b} int_{t_b}^{t_-} e^{(2-2n)s} f_n ds
                    tbq = c["tq"] + c["hq"]
                    if tbq == T.t_lo_q: Bbd = T.B[0]
                    else:
                        sb = tbq - T.t_lo_q   # negative
                        fh_b = [ep.shift(q2arb(sb)) for ep in self.fhat_in]
                        hb = q2arb(-sb); tb_ = q2arb(tbq)
                        Bbd = []
                        for n in range(1, Nf + 1):
                            # int_{t_b}^{t_-} e^{(2-2n)s} f_n ds = e^{(4-2n) t_b} int_0^{hb} e^{(4-2n) sigma} fhat_b(sigma) dsigma
                            mu = arb(4 - 2 * n)
                            mom = arb(0)
                            for e, cs in fh_b[n - 1].terms.items():
                                for p_, cp in enumerate(cs):
                                    if cp != 0: mom += cp * ((moment_right(q2arb(e) + mu, p_, hb)))
                            Bbd.append((-2 * n * hb).exp() * T.B[0][n - 1] + (4 * tb_).exp() * mom)
                    hA = hB = h
            else:
                Rhat = [ep.shift(q2arb(s)) for ep in self.Rhat_out]; fhat = [ep.shift(q2arb(s)) for ep in self.fhat_out]
                ta = c["ta"]; h = c["h"]
                # A_n(t_a): if t_a = t_+ use T.A[nc]; else A_n(t_a) = e^{-2n (t_a - t_+)} A_n(t_+) + e^{-2n t_a} int_{t_+}^{t_a} e^{(2n+2)s} f_n ds
                if c["tq"] == T.t_hi_q: Abd = T.A[T.nc]
                else:
                    fh0 = self.fhat_out; ha = q2arb(s)
                    Abd = []
                    for n in range(1, Nf + 1):
                        lam = arb(2 * n + 4); mom = arb(0)
                        for e, cs in fh0[n - 1].terms.items():
                            ea = q2arb(e); eeh = (ea * ha).exp()
                            for p_, cp in enumerate(cs):
                                if cp != 0: mom += cp * eeh * moment_left(ea + lam, p_, ha)
                        Abd.append((-2 * n * ha).exp() * T.A[T.nc][n - 1] + (4 * ta).exp() * mom)
                if kind == "pinf":
                    Bbd = None; hA = hB = None
                else:
                    Bbd = []
                    for n in range(1, Nf + 1):
                        # B_n(t_b) = e^{2n t_b} int_{t_b}^oo e^{(2-2n)s} f_n ds, with f re-expanded at t_b
                        sb = c["tq"] + c["hq"] - T.t_hi_q; fh_b = [ep.shift(q2arb(sb)) for ep in self.fhat_out]; tb_ = q2arb(c["tq"] + c["hq"])
                        Bbd.append((4 * tb_).exp() * integrate_ep(fh_b[n - 1].mul_exp(fmpq(4 - 2 * n)), "pinf"))
                    hA = hB = h
        # dR_j = 3 Rhat_j + Rhat_j'
        dR = [Rhat[j].scale(arb(3)) + Rhat[j].deriv() for j in range(T.Mj)]
        # psi data as exp-polys in sigma: A_n(sigma), B_n(sigma)
        Pe = []; Qe = []
        e4a = (4 * ta).exp(); em2a = (-2 * ta).exp()
        nmax = Nf if (self.nmax is None or ic in self.full_cells) else min(Nf, self.nmax)
        for n in range(1, nmax + 1):
            An = green_A_on_cell(fhat[n - 1], n, Abd[n - 1] if Abd is not None else None, e4a, kind)
            if kind == "minf": Bn = green_B_on_cell_minf(fhat[n - 1], n, Bbd[n - 1], e4a)
            else: Bn = green_B_on_cell(fhat[n - 1], n, Bbd[n - 1] if Bbd is not None else None, e4a, hB, kind)
            Pe.append((An + Bn).scale(em2a / 2).mul_exp(fmpq(-2)))
            Qe.append((Bn - An).scale(em2a / 2).mul_exp(fmpq(-2)))
        data = dict(Rhat=Rhat, dR=dR, Pe=Pe, Qe=Qe, fhat=fhat, ta=ta, h=h, kind=kind, e4a=e4a, Abd=Abd, Bbd=Bbd)
        if len(self.cache) > 4: self.cache.pop(next(iter(self.cache)))
        self.cache[ic] = data
        return data


def green_A_on_cell(fhat, n, A_ta, e4a, kind):
    """A_n(sigma) on a cell as ExpPoly: A_n(sigma) = e^{-2n sigma} A_n(t_a) + e^{4 t_a} e^{-2n sigma} int_0^sigma e^{(2n+4) s} fhat(s) ds  (sigma >= 0),
    on the half-infinite inner cell (sigma <= 0, A(t_a) at sigma = 0 given):  A_n(sigma) = e^{-2n sigma} [A_n(t_a) - e^{4t_a} int_sigma^0 e^{(2n+4)s} fhat ds]
    = e^{-2n sigma} A_n(t_a) - e^{4t_a} e^{-2n sigma} int_sigma^0 ...  (same closed form, both signs)."""
    out = ExpPoly()
    lam0 = fmpq(2 * n + 4)
    if kind == "minf":
        # canonical inner primitive on the half-line (-oo, t_a]: A_n(sigma) = e^{4 t_a} sum e^{(lam - 2n) sigma} S(sigma); the homogeneous
        # e^{-2n sigma} coefficient A(t_a) - e^{4 t_a} sum S(0) is identically zero (A(t_a) is that integral); it is not represented
        # (a nonzero-radius ball there would grow as sigma -> -oo; verifier V020).
        homo = arb(A_ta) if A_ta is not None else None
        for e, cs in fhat.terms.items():
            lam = lam0 + e; lam_a = q2arb(lam); assert lam_a > 0
            for p_, cp in enumerate(cs):
                if cp == 0: continue
                S = prim_S(lam_a, p_)
                out.add(lam - fmpq(2 * n), [e4a * cp * s_ for s_ in S])
                if homo is not None: homo = homo - e4a * cp * S[0]
        if homo is not None:
            assert homo.contains(arb(0)), ("inner Green consistency", homo.str(5))
        return out
    if A_ta is not None: out.add(fmpq(-2 * n), [A_ta])
    for e, cs in fhat.terms.items():
        lam = lam0 + e; lam_a = q2arb(lam)
        # int_0^sigma e^{lam s} p(s) ds = e^{lam sigma} S(sigma) - S(0)   (lam != 0)
        for p_, cp in enumerate(cs):
            if cp == 0: continue
            if lam_a == 0:
                out.add(fmpq(-2 * n), [arb(0)] * (p_ + 1) + [e4a * cp / (p_ + 1)])
            else:
                S = prim_S(lam_a, p_)
                out.add(lam - fmpq(2 * n), [e4a * cp * s_ for s_ in S])        # e^{(lam-2n) sigma} S(sigma) e^{4t_a}
                out.add(fmpq(-2 * n), [-e4a * cp * S[0]])
    return out


def green_B_on_cell(fhat, n, B_tb, e4a, h, kind):
    """B_n(sigma) = e^{2n sigma} e^{-2n h} B_n(t_b) + e^{4 t_a} e^{2n sigma} int_sigma^h e^{(4-2n) s} fhat(s) ds  (finite cell);
    outer half-infinite cell: B_n(sigma) = e^{4 t_a} e^{2n sigma} int_sigma^oo e^{(4-2n)s} fhat ds (all exponents of the integrand negative)."""
    out = ExpPoly()
    mu0 = fmpq(4 - 2 * n)
    const = arb(0)
    if B_tb is not None: const += (-2 * n * h).exp() * B_tb
    for e, cs in fhat.terms.items():
        mu = mu0 + e; mu_a = q2arb(mu)
        for p_, cp in enumerate(cs):
            if cp == 0: continue
            if kind == "pinf":
                assert mu_a < 0
                # int_sigma^oo e^{mu s} s^p ds = -e^{mu sigma} S(sigma)   (S the primitive factor; e^{mu s} S -> 0 at oo)
                S = prim_S(mu_a, p_)
                out.add(mu + fmpq(2 * n), [-e4a * cp * s_ for s_ in S])
            else:
                if mu_a == 0:
                    # int_sigma^h s^p ds = h^{p+1}/(p+1) - sigma^{p+1}/(p+1)
                    const += e4a * cp * h ** (p_ + 1) / (p_ + 1)
                    out.add(fmpq(2 * n), [arb(0)] * (p_ + 1) + [-e4a * cp / (p_ + 1)])
                else:
                    S = prim_S(mu_a, p_)
                    const += e4a * cp * (mu_a * h).exp() * sum((S[q_] * h ** q_ for q_ in range(len(S))), arb(0))
                    out.add(mu + fmpq(2 * n), [-e4a * cp * s_ for s_ in S])
    if kind != "pinf" or const != 0: out.add(fmpq(2 * n), [const])
    return out


class Column:
    """A single-angular-mode radial column h = x^2 y b(t) cos(2 m theta): b given as dict ic -> ExpPoly on the cells where it is nonzero.
    Green data of the column: A^h_n(t_a), Bt^h_n(t_b) (Bt = B - 2 c e^{2t} for n = 1) at the boundaries of its cells, c[h].
    Multi-mode variant: coef = {m: arb} gives h = x^2 y b(t) sum_m coef_m cos(2m theta) (one radial function, many modes); then
    Rhat^h_j = b * sum_m P_jm coef_m for every j and the velocity modes n run over all 1..Nf."""
    def __init__(self, m, pieces, T, cells, label="", coef=None):
        self.m = m; self.pieces = pieces; self.T = T; self.cells = cells; self.label = label
        self.coef = coef
        if coef is None:
            self.hmodes = [n for n in range(max(1, m - 2), m + 3) if n <= T.Nf]      # velocity modes of h: n in m-2..m+2
            self.Pcol = {j: q2arb(T.P_q[j, m]) for j in range(T.Mj) if T.P_q[j, m] != 0}
        else:
            self.Pcol = {}
            for j in range(T.Mj):
                v = arb(0); nz = False
                for mm, cm in coef.items():
                    pq = T.P_q[j, mm]
                    if pq != 0 and cm != 0: v += q2arb(pq) * cm; nz = True
                if nz: self.Pcol[j] = v
            js = sorted(self.Pcol)
            self.hmodes = sorted(set(n for j in js for n in (j, j + 1) if 1 <= n <= T.Nf))
        self._green()

    def Rhat_h(self, b):
        """Rhat^h_j = (sum_m P_jm coef_m) b; returns dict j -> ExpPoly"""
        return {j: b.scale(pj) for j, pj in self.Pcol.items()}

    def fhat_h(self, b):
        """f^h_n = e^{2t} fhat^h_n;  fhat^h_n = (1/2)[(3 - (2n-1)) Rh_{n-1} + Rh_{n-1}' + (3 + (2n+1)) Rh_n + Rh_n']"""
        Rh = self.Rhat_h(b); out = {}
        for n in self.hmodes:
            ep = ExpPoly()
            if (n - 1) in Rh: ep = ep + Rh[n - 1].scale(arb(3 - (2 * n - 1))) + Rh[n - 1].deriv()
            if n in Rh: ep = ep + Rh[n].scale(arb(3 + (2 * n + 1))) + Rh[n].deriv()
            if ep.terms: out[n] = ep.scale(arb(1) / 2)
        return out

    def _green(self):
        """boundary values along the cells: A^h_n(t_a of each cell), B^h_n(t_b of each cell) for n in hmodes; c[h]."""
        cells = self.cells; T = self.T
        idx = sorted(self.pieces.keys())
        self.fh = {ic: self.fhat_h(self.pieces[ic]) for ic in idx}
        # c[h] = (1/2) int_R f_1 dt = (1/2) sum_cells e^{2 t_a} int e^{2 sigma} fhat_1
        c = arb(0)
        for ic in idx:
            fh = self.fh[ic]
            if 1 not in fh: continue
            cl = cells.cells[ic]; e2a = (2 * cl["ta"]).exp()
            if cl["kind"] == "minf": c += e2a * integrate_ep(fh[1].mul_exp(fmpq(2)), "minf")
            elif cl["kind"] == "pinf": c += e2a * integrate_ep(fh[1].mul_exp(fmpq(2)), "pinf")
            else: c += e2a * integrate_ep(fh[1].mul_exp(fmpq(2)), "cell", cl["h"])
        self.c = c / 2
        # A^h_n at the left end of every cell of the support and beyond: A^h_n(t) for t right of the support = e^{-2n(t - t_end)} A_end
        # store A at left ends of support cells (list aligned with idx) and A_end (value at the right end of the support)
        self.A_left = {}; self.B_right = {}
        Acur = {n: arb(0) for n in self.hmodes}
        for ic in idx:
            cl = cells.cells[ic]; fh = self.fh[ic]
            self.A_left[ic] = dict(Acur)
            if cl["kind"] == "minf":
                # A at the right end t_a (= the cell's reference point): e^{4 t_a} int_{-oo}^0 e^{(2n+4) s} fhat
                for n in self.hmodes:
                    Acur[n] = (4 * cl["ta"]).exp() * (integrate_ep(fh[n].mul_exp(fmpq(2 * n + 4)), "minf") if n in fh else arb(0))
            elif cl["kind"] == "pinf":
                pass
            else:
                h = cl["h"]; e4b = (4 * (cl["ta"] + h)).exp()
                for n in self.hmodes:
                    inc = arb(0)
                    if n in fh:
                        for e, cs in fh[n].terms.items():
                            ea = q2arb(e); lam = ea + (2 * n + 4); eeh = (ea * h).exp()
                            # A(t_b) = e^{-2nh} A(t_a) + e^{4 t_a} e^{(4+e) h} int_0^h e^{lam (sigma - h)} p(sigma) dsigma
                            for p_, cp in enumerate(cs):
                                if cp != 0: inc += cp * eeh * moment_left(lam, p_, h)
                    Acur[n] = (-2 * n * h).exp() * Acur[n] + e4b * inc
        self.A_end = dict(Acur); self.t_end_q = cells.tq[idx[-1]] + (cells.cells[idx[-1]]["hq"] if cells.cells[idx[-1]]["kind"] not in ("minf", "pinf") else fmpq(0))
        # B^h_n at the right end of every support cell, going backward; B beyond the left end = e^{2n (t - t_start)} B_start
        Bcur = {n: arb(0) for n in self.hmodes}
        for ic in reversed(idx):
            cl = cells.cells[ic]; fh = self.fh[ic]
            self.B_right[ic] = dict(Bcur)
            if cl["kind"] == "pinf":
                for n in self.hmodes:
                    Bcur[n] = (4 * cl["ta"]).exp() * (integrate_ep(fh[n].mul_exp(fmpq(4 - 2 * n)), "pinf") if n in fh else arb(0))
                self.B_right[ic] = {n: None for n in self.hmodes}
            elif cl["kind"] == "minf":
                pass
            else:
                h = cl["h"]; e4a = (4 * cl["ta"]).exp()
                for n in self.hmodes:
                    inc = arb(0)
                    if n in fh:
                        for e, cs in fh[n].terms.items():
                            mu = q2arb(e) + (4 - 2 * n)
                            for p_, cp in enumerate(cs):
                                if cp != 0: inc += cp * moment_right(mu, p_, h)
                    Bcur[n] = (-2 * n * h).exp() * Bcur[n] + e4a * inc
        self.B_start = dict(Bcur); self.t_start_q = cells.tq[idx[0]]
        # consistency: B_1(start) e^{-2 t_start} should equal 2 c (for columns whose support does not include the minf cell)
        self.idx = idx

    def green_on_cell(self, ic):
        """A^h_n(sigma), Bt^h_n(sigma) (n in hmodes) as ExpPoly on cell ic (anywhere), with Bt_1 = B_1 - 2 c e^{2t}."""
        cells = self.cells; cl = cells.cells[ic]; T = self.T
        ta = cl["ta"]; e4a = (4 * ta).exp(); kind = cl["kind"]; h = cl["h"]
        out_A = {}; out_B = {}
        in_support = ic in self.pieces
        for n in self.hmodes:
            if in_support:
                fh = self.fh[ic].get(n, ExpPoly())
                if kind == "minf":
                    # A(sigma) for sigma <= 0 with A(0) = A_end[n] known: A(sigma) = e^{-2n sigma}[A(0) - e^{4ta} int_sigma^0 e^{(2n+4)s} fhat] -> same closed form as finite with A_ta := A(0)
                    An = green_A_on_cell(fh, n, self.A_end[n] if ic == self.idx[-1] else self._A_at_right_of(ic, n), e4a, kind)
                    # B on the half-infinite inner cell: B(sigma) = e^{2n sigma} B(0) + e^{4ta} e^{2n sigma} int_sigma^0 e^{(4-2n)s} fhat ds
                    Bn = green_B_on_cell_minf(fh, n, self.B_right[ic][n], e4a)
                elif kind == "pinf":
                    An = green_A_on_cell(fh, n, self.A_left[ic][n], e4a, kind)
                    Bn = green_B_on_cell(fh, n, None, e4a, None, kind)
                else:
                    An = green_A_on_cell(fh, n, self.A_left[ic][n], e4a, kind)
                    Bn = green_B_on_cell(fh, n, self.B_right[ic][n], e4a, h, kind)
            else:
                An = ExpPoly(); Bn = ExpPoly()
                tq = cl["tq"]
                if tq >= self.t_end_q:       # right of the support: A = e^{-2n (t - t_end)} A_end, B = 0
                    An.add(fmpq(-2 * n), [(-2 * n * (ta - q2arb(self.t_end_q))).exp() * self.A_end[n]])
                else:                        # left of the support: B = e^{2n (t - t_start)} B_start, A = 0
                    Bn.add(fmpq(2 * n), [(2 * n * (ta - q2arb(self.t_start_q))).exp() * self.B_start[n]])
            if n == 1:
                Bn = Bn - ExpPoly([(fmpq(2), [2 * self.c * (2 * ta).exp()])])      # Bt_1 = B_1 - 2 c e^{2t}
            out_A[n] = An; out_B[n] = Bn
        return out_A, out_B

    def _A_at_right_of(self, ic, n):
        j = self.idx.index(ic)
        return self.A_left[self.idx[j + 1]][n] if j + 1 < len(self.idx) else self.A_end[n]


def green_B_on_cell_minf(fhat, n, B0, e4a):
    """inner half-infinite cell, sigma <= 0: B_n(sigma) = e^{2n sigma} B_n(0) + e^{4 t_a} e^{2n sigma} int_sigma^0 e^{(4-2n) s} fhat(s) ds."""
    out = ExpPoly(); mu0 = fmpq(4 - 2 * n)
    const = arb(B0)
    for e, cs in fhat.terms.items():
        mu = mu0 + e; mu_a = q2arb(mu)
        for p_, cp in enumerate(cs):
            if cp == 0: continue
            if mu_a == 0:
                # int_sigma^0 s^p ds = -sigma^{p+1}/(p+1)
                out.add(fmpq(2 * n), [arb(0)] * (p_ + 1) + [-e4a * cp / (p_ + 1)])
            else:
                S = prim_S(mu_a, p_)
                # int_sigma^0 e^{mu s} s^p = S(0) - e^{mu sigma} S(sigma)
                const += e4a * cp * S[0]
                out.add(mu + fmpq(2 * n), [-e4a * cp * s_ for s_ in S])
    out.add(fmpq(2 * n), [const])
    return out


class Operator:
    def __init__(self, T, cells, bg, Nmax=None):
        self.T = T; self.cells = cells; self.bg = bg
        self.c_l_q = 1 / T.k_q; self.c_l = q2arb(self.c_l_q)
        self.Nmax = Nmax   # keep output modes N <= Nmax (None: all)
        self._Mcache = {}; self._farcache = {}
        # the constant image term at the origin is removed only for an exactly normalized background (3 c_l - 1 - c[rho~] = 0 exactly);
        # for float fixtures (z = 0, inexact joins) it is kept.
        self.exact_normalized = (T.z != 0) or getattr(T, "exact_normalized", False)

    def M_cached(self, ic):
        if ic not in self._Mcache:
            if len(self._Mcache) > 2: self._Mcache.pop(next(iter(self._Mcache)))
            self._Mcache[ic] = self.M_modes(ic)
        return self._Mcache[ic]

    def far_unit_images(self, ic, nlist):
        """For a column NOT supported on cell ic: its nonlocal image is sum_n [alpha_n * UA_n + beta_n * UB_n] (+ c M) with
        UA_n = image of (A^h_n = e^{-2n sigma}, B^h_n = 0) and UB_n = image of (A = 0, Bt = e^{2n sigma}); returns dict n -> (UA_n, UB_n), each dict N -> ExpPoly."""
        key = (ic, tuple(nlist))
        if key in self._farcache: return self._farcache[key]
        d = self.bg.get(ic); T = self.T; Nmax = self.Nmax
        em2a = (-2 * d["ta"]).exp(); out = {}
        for n in nlist:
            res = []
            for which in ("A", "B"):
                if which == "A":
                    Peh = ExpPoly([(fmpq(-2 * n - 2), [em2a / 2])]); Qeh = ExpPoly([(fmpq(-2 * n - 2), [-em2a / 2])])
                else:
                    Peh = ExpPoly([(fmpq(2 * n - 2), [em2a / 2])]); Qeh = ExpPoly([(fmpq(2 * n - 2), [em2a / 2])])
                acc = {}
                for j in range(T.Mj):
                    if Nmax is not None and min(abs(2 * j + 1 - 2 * n), 2 * j + 1 + 2 * n) > 2 * Nmax + 1: continue
                    co = (Peh * d["dR"][j]).scale(arb(-1) / 2); addsin(acc, 2 * j + 1 + 2 * n, co); addsin(acc, 2 * j + 1 - 2 * n, co)
                    co2 = (Qeh * d["Rhat"][j]).scale(arb(2 * j + 1) / 2); addsin(acc, 2 * n + 2 * j + 1, co2); addsin(acc, 2 * n - 2 * j - 1, co2)
                if Nmax is not None: acc = {N: ep for N, ep in acc.items() if N <= Nmax}
                res.append(acc)
            out[n] = tuple(res)
        if len(self._farcache) > 2: self._farcache.pop(next(iter(self._farcache)))
        self._farcache[key] = out
        return out

    def far_coefficients(self, col, ic):
        """(alpha_n, beta_n) for a column not supported on cell ic: A^h_n = alpha_n e^{-2n sigma}, Bt^h_n = beta_n e^{2n sigma}."""
        cl = self.cells.cells[ic]; ta = cl["ta"]; out = {}
        for n in col.hmodes:
            if cl["tq"] >= col.t_end_q:
                out[n] = ((-2 * n * (ta - q2arb(col.t_end_q))).exp() * col.A_end[n], arb(0) if n != 1 else -2 * col.c * (2 * ta).exp())
            else:
                b = (2 * n * (ta - q2arb(col.t_start_q))).exp() * col.B_start[n]
                if n == 1: b = b - 2 * col.c * (2 * ta).exp()
                out[n] = (arb(0), b)
        return out

    def transport_self(self, b, m, Pcol=None):
        """P_Nm [(3 c_l - 1) b + c_l b'] per exponential term with the exact rational factor (3c_l - 1 + c_l e); Pcol: {j: coefficient} for multi-mode columns."""
        tr = ExpPoly()
        for e, cs in b.terms.items():
            fac = q2arb(3 * self.c_l_q - 1 + self.c_l_q * e)
            d = [fac * x for x in cs]
            for p_ in range(1, len(cs)): d[p_ - 1] += self.c_l * p_ * cs[p_]
            tr.add(e, d)
        out = {}
        if Pcol is None: Pcol = {j: q2arb(self.T.P_q[j, m]) for j in range(self.T.Mj) if self.T.P_q[j, m] != 0}
        for j, pj in Pcol.items(): addsin(out, 2 * j + 1, tr.scale(pj))
        return out

    def M_modes(self, ic):
        """M_N on cell ic: the image e^{-3t} ((-2x/3, 4y/3).grad rho~) = the strain term dR_N/3 plus the n=1 constant-velocity terms with Pe = Qe = 1.
        On the inner cells the exponent-0 term is removed (exactly zero; see M_leading_check)."""
        d = self.bg.get(ic); T = self.T
        acc = {}
        for j in range(T.Mj):
            addsin(acc, 2 * j + 1, d["dR"][j].scale(arb(1) / 3))
            co = d["dR"][j].scale(arb(-1) / 2); addsin(acc, 2 * j + 3, co); addsin(acc, 2 * j - 1, co)
            co2 = d["Rhat"][j].scale(arb(2 * j + 1) / 2); addsin(acc, 2 * j + 3, co2); addsin(acc, 1 - 2 * j, co2)
        if d["kind"] in ("minf", "inner"):
            for N, ep in acc.items():
                if fmpq(0) in ep.terms:
                    c0 = ep.terms[fmpq(0)]
                    assert all(x.contains(arb(0)) and float(x.rad()) < 1e-60 for x in c0), ("M constant term not negligible", N, [x.str(5) for x in c0])
                    del ep.terms[fmpq(0)]
        return acc

    def image(self, col, ic, Nmax=None, parts=False):
        """G_N(sigma) on cell ic for the column: dict N -> ExpPoly.  parts=True: returns (acc_transport, acc_nonlocal)."""
        Nmax = self.Nmax if Nmax is None else Nmax
        d = self.bg.get(ic); T = self.T; m = col.m
        acc = {}
        if ic in col.pieces:
            b = col.pieces[ic]
            for N, ep in self.transport_self(b, m, col.Pcol).items(): addsin(acc, 2 * N + 1, ep)
            Rh = col.Rhat_h(b); Rht = {j: Rh[j].scale(arb(3)) + Rh[j].deriv() for j in Rh}
            jmax = max(Rh) if Rh else -1
            for ni in range(len(d["Pe"])):
                n = ni + 1
                if Nmax is not None and n > Nmax + jmax + 2: break
                Pe = d["Pe"][ni]; Qe = d["Qe"][ni]
                for j in Rh:
                    if Nmax is not None and min(abs(2 * j + 1 - 2 * n), 2 * j + 1 + 2 * n) > 2 * Nmax + 1: continue
                    co = (Pe * Rht[j]).scale(arb(-1) / 2); addsin(acc, 2 * j + 1 + 2 * n, co); addsin(acc, 2 * j + 1 - 2 * n, co)
                    co2 = (Qe * Rh[j]).scale(arb(2 * j + 1) / 2); addsin(acc, 2 * n + 2 * j + 1, co2); addsin(acc, 2 * n - 2 * j - 1, co2)
        if parts: acc_ab = acc; acc = {}
        # velocity of h on the background (all background modes j), with the n=1 constant part moved into c M
        Ah, Bh = col.green_on_cell(ic)
        em2a = (-2 * d["ta"]).exp()
        for n in col.hmodes:
            Peh = (Ah[n] + Bh[n]).scale(em2a / 2).mul_exp(fmpq(-2)); Qeh = (Bh[n] - Ah[n]).scale(em2a / 2).mul_exp(fmpq(-2))
            if not Peh.terms and not Qeh.terms: continue
            for j in range(T.Mj):
                if Nmax is not None and min(abs(2 * j + 1 - 2 * n), 2 * j + 1 + 2 * n) > 2 * Nmax + 1: continue
                co = (Peh * d["dR"][j]).scale(arb(-1) / 2); addsin(acc, 2 * j + 1 + 2 * n, co); addsin(acc, 2 * j + 1 - 2 * n, co)
                co2 = (Qeh * d["Rhat"][j]).scale(arb(2 * j + 1) / 2); addsin(acc, 2 * n + 2 * j + 1, co2); addsin(acc, 2 * n - 2 * j - 1, co2)
        if col.c != 0:
            for N, ep in self.M_cached(ic).items():
                if Nmax is None or N <= Nmax: addsin(acc, 2 * N + 1, ep.scale(col.c))
        if Nmax is not None:
            acc = {N: ep for N, ep in acc.items() if N <= Nmax}
        if d["kind"] in ("minf", "inner") and not parts and getattr(self, "exact_normalized", True):
            # exponent-0 (constant at the origin) terms vanish identically: for the strain/n=1 part by (-2x/3, 4y/3).grad(x^2 y) = 0,
            # for a constant factor (the J column) by the exact normalization 3 c_l - 1 - c[rho~] = 0 of the background.
            for N, ep in acc.items():
                if fmpq(0) in ep.terms:
                    c0 = ep.terms[fmpq(0)]
                    assert all(x.contains(arb(0)) and float(x.rad()) < 1e-30 for x in c0), ("constant image term not negligible", col.label, N, [x.str(5) for x in c0])
                    del ep.terms[fmpq(0)]
        if parts: return acc_ab, acc
        return acc

    def residual_modes(self, ic, Nmax=None):
        """epshat_N = e^{-3t} eps~_N on cell ic (eps~ = (c_l X + U).grad rho~ - rho~)."""
        d = self.bg.get(ic); T = self.T; acc = {}
        for j in range(T.Mj):
            addsin(acc, 2 * j + 1, d["dR"][j].scale(self.c_l) - d["Rhat"][j])
        for ni in range(len(d["Pe"])):
            n = ni + 1
            if Nmax is not None and n > 2 * Nmax + 2: break
            Pe = d["Pe"][ni]; Qe = d["Qe"][ni]
            for j in range(T.Mj):
                if Nmax is not None and min(abs(2 * j + 1 - 2 * n), 2 * j + 1 + 2 * n) > 2 * Nmax + 1: continue
                co = (Pe * d["dR"][j]).scale(arb(-1) / 2); addsin(acc, 2 * j + 1 + 2 * n, co); addsin(acc, 2 * j + 1 - 2 * n, co)
                co2 = (Qe * d["Rhat"][j]).scale(arb(2 * j + 1) / 2); addsin(acc, 2 * n + 2 * j + 1, co2); addsin(acc, 2 * n - 2 * j - 1, co2)
        if Nmax is not None: acc = {N: ep for N, ep in acc.items() if N <= Nmax}
        return acc


def M_leading_check():
    """exact rational check: the constant (origin) term of M vanishes in every mode for rho~ = x^2 y (a_0 = 1)."""
    Rh = {0: Fraction(1, 4), 1: Fraction(1, 4)}; dR = {0: Fraction(3, 4), 1: Fraction(3, 4)}
    acc = {}
    def add(f, v):
        if f < 0: f, v = -f, -v
        if f == 0: return
        acc[(f - 1) // 2] = acc.get((f - 1) // 2, Fraction(0)) + v
    for j in (0, 1):
        add(2 * j + 1, dR[j] / 3); add(2 * j + 3, -dR[j] / 2); add(2 * j - 1, -dR[j] / 2)
        add(2 * j + 3, (2 * j + 1) * Rh[j] / 2); add(1 - 2 * j, (2 * j + 1) * Rh[j] / 2)
    assert all(v == 0 for v in acc.values()), acc
    return True


if __name__ == "__main__":
    M_leading_check(); print("M leading-term cancellation verified in exact rationals")
