"""Certificate of the residual of the explicit modal trial on the middle region (SPEC v1 item R0), by Taylor models.

Input: data/cert_green.npz (Arb, exported as enclosing mid/rad doubles): sub-cell boundaries tb (7810), A_n(tb), B_n(tb)
for n = 1..Nf, Taylor coefficients T[ci][q][m] of a_m at every sub-cell start (degree 7), and the trial file (k, L).
On every sub-cell [t_a, t_a + h] (h <= hsub, 2 n h <= 1 for all n), with tau = t - t_a, every modal function is enclosed by a
Taylor model (polynomial of degree Q in tau with mid-rad coefficients + remainder bound):
  R_j(tau)   = e^{3 t_a} e^{3 tau} T_j[a](tau),  dR_j/dt = e^{3 t_a} e^{3 tau} (3 T_j[a] + T_j[a'])(tau)       (exact polynomial x TM(exp))
  g_n(tau)   = e^{2t} f_n(e^t) = e^{4 t_a} e^{4 tau} F_n(tau),  F_n the degree-7 f-polynomial from T (d_x of the sine modes)
  A_n' = -2n A_n + g_n,  B_n' = 2n B_n - g_n: Taylor coefficients by the recursion from the certified A_n(t_a), B_n(t_a);
     remainders from |A_n^{(Q+1)}| <= (2n)^{Q+1} |A_n|_oo + sum_i (2n)^{Q-i} |g_n^{(i)}|_oo, |A_n|_oo <= |A_n(t_a)| + h |g_n|_oo
     (and |B_n|_oo <= e^{2nh} (|B_n(t_a)| + h |g_n|_oo)), all derivative bounds of g from its exponential-polynomial form.
  psi_n = (A_n + B_n)/(4n), psi_n' = (B_n - A_n) e^{-t_a} e^{-tau} / 2,
  eps_N = c_l dR_N/dt - R_N - (1/2) sum_{n,j} 2n psi_n dR_j/dt e^{-2t} [sin((2j+1+2n)th) + sin((2j+1-2n)th)]
                          + (1/2) sum_{n,j} psi_n' (2j+1) R_j e^{-t} [sin((2n+2j+1)th) + sin((2n-2j-1)th)].
Sup over the sub-cell of |eps_N| <= max of the Bernstein coefficients of the degree-Q polynomial on [0, h] + remainder;
W(sub-cell) = sum_N sup |eps_N| >= sup_{r in sub-cell} sup_theta |eps~|.  Reported: sup over sub-cells of W/m, m = u^3 (1+u^2)^{(k-3)/2}
(monotone increasing in r, so inf over the sub-cell = m at its left end), by region.
All arithmetic: src/midrad.py (rigorous float64 mid-rad with outward rounding); transcendental constants (e^{t_a} etc.) in Arb.
Usage: python3 cert_resid.py data/cert_green.npz data/trial_v2_h0.008.npz out.json [Q=12] [ci_start ci_end]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial, comb
from midrad import MR, mr_matmul, succ, U, ETA
from flint import arb, ctx


def mag(x):      # upper bound of |x| for an MR
    return x.mag()


class TMArr:
    """Taylor models for an array of functions (shape S) on [0, h]: coefficients MR of shape S + (Q+1,), remainder float array S."""
    def __init__(self, coef, rem):
        self.c = coef; self.r = np.asarray(rem, float)

    @property
    def Q(self):
        return self.c.m.shape[-1] - 1

    def sup(self, hpow):
        """upper bound of sup_{[0,h]} |f|: sum_i |c_i| h^i + rem  (hpow: array of h^i upper bounds)."""
        return succ(succ(succ((mag(self.c) * hpow[None, :self.Q + 1]).sum(-1) * succ(1 + (self.Q + 2) * U)) + (self.Q + 2) * ETA) + self.r)

    def __add__(self, other):
        return TMArr(self.c + other.c, succ(self.r + other.r))

    def __sub__(self, other):
        return TMArr(self.c - other.c, succ(self.r + other.r))

    def scale(self, s):
        """multiply by an MR scalar or MR array broadcast over the leading axes (no tau dependence)."""
        if not isinstance(s, MR): s = MR.exact(s)
        sm = s if s.m.ndim == 0 else MR(s.m[..., None], s.r[..., None])
        return TMArr(self.c * sm, succ(succ(self.r * mag(s if s.m.ndim == 0 else s)) * succ(1 + 2 * U)))

    def mul_poly(self, poly, hpow):
        """multiply by an exact-degree polynomial (MR array of shape S + (d+1,)), truncate at Q; poly has no remainder."""
        Q = self.Q; d = poly.m.shape[-1] - 1
        S = self.c.m.shape[:-1]
        cm = np.zeros(S + (Q + 1,)); cr = np.zeros(S + (Q + 1,)); trunc = np.zeros(S); absacc = np.zeros(S + (Q + 1,))
        A = self.c; B = poly
        for i in range(Q + 1):
            for k in range(d + 1):
                prod = A[..., i] * B[..., k]
                if i + k <= Q:
                    cm[..., i + k] += prod.m; cr[..., i + k] = succ(cr[..., i + k] + prod.r); absacc[..., i + k] = succ(absacc[..., i + k] + np.abs(prod.m))
                else:
                    trunc = succ(trunc + succ(mag(prod) * hpow[i + k]) + ETA)          # + eta: the h-weighted product may underflow
        # rounding of the midpoint sums (at most d+1 terms per output coefficient, any order): gamma_d * sum |summands|, plus underflow
        gam = succ(d * U / (1 - d * U)) if d >= 1 else 0.0
        cr = succ(succ(cr + succ(gam * absacc)) + (d + 2) * ETA)
        polysup = succ(succ((mag(B) * hpow[None, :d + 1]).sum(-1) * succ(1 + (d + 2) * U)) + (d + 2) * ETA)      # underflow allowance (referee round 2)
        rem = succ(succ(self.r * polysup) + trunc)
        return TMArr(MR(cm, cr), rem)


def tm_exp(gamma, h_up, Q):
    """TM of e^{gamma tau} on [0, h] (gamma exact float, |gamma| h <= 1): coefficients gamma^i/i!, remainder (1+x+x^2) x^{Q+1}/(Q+1)!,
    x = |gamma| h (e^x <= 1 + x + x^2 on [0,1])."""
    g = gamma if isinstance(gamma, MR) else MR.exact(float(gamma))
    coeffs = [MR.exact(1.0)]
    for i in range(1, Q + 1):
        coeffs.append(coeffs[-1] * g * MR(1.0 / i, succ(U / i)))
    x = succ(float(g.mag()) * h_up); assert x <= 1.0 + 1e-12, "exponent too large for the cell"
    rem = succ(succ(1 + x + x * x) * succ(x ** (Q + 1) / factorial(Q + 1)) * succ(1 + 4 * (Q + 2) * U))
    cm = np.array([c.m for c in coeffs]); cr = np.array([c.r for c in coeffs])
    return MR(cm, cr), rem


def bernstein_matrix(Q):
    """MR matrix B with B[k,i] = C(k,i)/C(Q,i) (ratio of integers; the double division is rounded, radius u|B|), such that for
    p(h x) = sum_i a_i h^i x^i the Bernstein coefficients on [0,1] are b_k = sum_i B[k,i] (a_i h^i)."""
    Bm = np.zeros((Q + 1, Q + 1)); Br = np.zeros((Q + 1, Q + 1))
    for k in range(Q + 1):
        for i in range(k + 1):
            Bm[k, i] = comb(k, i) / comb(Q, i); Br[k, i] = succ(U * Bm[k, i])      # the double division may be inexact: always a radius
    return MR(Bm, Br)


class Certifier:
    def __init__(self, green_path, trial_path, Q=12):
        d = np.load(green_path); self.d = d
        self.tb = MR(d["tb"], d["tb_rad"]); self.nc = len(d["tb"]) - 1
        self.A = MR(d["A_mid"], d["A_rad"]); self.B = MR(d["B_mid"], d["B_rad"])        # (nc+1, Nf)
        self.T = MR(d["T_mid"], d["T_rad"])                                           # (nc, 8, M)
        self.Nf = self.A.m.shape[1]; self.M = self.T.m.shape[2]; self.p = self.T.m.shape[1] - 1
        tr = np.load(trial_path); self.k = float(tr["k"]); self.L = float(tr["L"])
        self.c_l = MR(1.0 / self.k, succ(U * abs(1.0 / self.k)))                    # 1/k rounded
        self.Q = Q
        self.n = np.arange(1, self.Nf + 1)
        self.Bern = bernstein_matrix(Q)
        # Arb constants per boundary: e^{t_a}, m(r_a) = u^3 (1+u^2)^((k-3)/2), (1+u)^0.5
        ctx.prec = 128
        et = []; mm = []; wf = []
        k = arb(self.k); L = arb(self.L)
        for i in range(self.nc + 1):
            ta = arb(float(d["tb"][i]), float(d["tb_rad"][i]))
            e = ta.exp(); u = e / L
            et.append(e); mm.append(u ** 3 * (1 + u * u) ** ((k - 3) / 2)); wf.append((1 + u).sqrt())
        self.e_ta = MR.from_arb(et); self.m_ta = MR.from_arb(mm); self.wfar_ta = MR.from_arb(wf)
        # frequency bookkeeping for the scatter: term1 N = j + n ; term2: n <= j -> N = j - n (+), n > j -> N = n - j - 1 (-)
        nn = self.n[:, None]; jj = np.arange(self.M + 1)[None, :]
        self.N1 = (jj + nn); self.N2 = np.where(nn <= jj, jj - nn, nn - jj - 1); self.S2 = np.where(nn <= jj, 1.0, -1.0)
        self.Nmax = 2 * self.M + 2

    # ---------- modal algebra on MR arrays (last axis = mode) ----------
    def R_from_a(self, a):
        """a: MR (..., M) -> (..., M+1)  (sin((2j+1)theta) coefficients of cos^2 sin * sum a_m cos 2m theta)."""
        M = self.M; S = a.m.shape[:-1]
        Rm = np.zeros(S + (M + 1,)); Rr = np.zeros(S + (M + 1,))
        def add(freq, coef_m, coef_r):
            if freq < 0: freq, coef_m = -freq, -coef_m
            if freq == 0: return
            j = (freq - 1) // 2
            if j <= M: Rm[..., j] += coef_m; Rr[..., j] = succ(Rr[..., j] + coef_r)
        for m in range(M):
            am = a.m[..., m] / 8.0; ar = succ(a.r[..., m] / 8.0 + U * np.abs(am))
            add(2 * m + 1, am, ar); add(-(2 * m - 1), am, ar); add(2 * m + 3, am, ar); add(-(2 * m - 3), am, ar)
        Rr = succ(Rr + 4 * U * np.abs(Rm))        # at most 4 terms summed per entry
        return MR(Rm, Rr)

    def f_terms_from_a(self, a_terms):
        """a_terms: list of (alpha, Tpoly) with Tpoly an MR (deg+1, M) of ascending coefficients in the local variable sigma:
        a_m(sigma) = sum_terms e^{alpha sigma} Tpoly[:, m](sigma).  Returns
          f_terms: list of (alpha, F (Nf, deg+1)) with f_n(e^t) = e^{2 t_a} sum e^{(alpha+2) sigma} F_n(sigma)   [exponent alpha+2 NOT yet added]
          R_terms: list of (alpha, Rc (deg+1, M+1), dR (deg+1, M+1)) with R_j = e^{3 t_a} sum e^{(3+alpha) sigma} Rc_j(sigma),
                   dR_j/dt = e^{3 t_a} sum e^{(3+alpha) sigma} dR_j(sigma),  dR = (3+alpha) Rc + Rc'."""
        P_ = None; f_terms = []; R_terms = []
        for alpha, T in a_terms:
            alpha = alpha if isinstance(alpha, MR) else MR.exact(float(alpha))      # exponent as an enclosing ball
            deg = T.m.shape[0] - 1
            Rc = self.R_from_a(T)                                  # (deg+1, M+1)
            dR = Rc * (alpha + MR.exact(3.0))                      # (3+alpha) Rc  (MR scalar x MR array)
            if deg >= 1:
                sh = MR(np.zeros_like(Rc.m), np.zeros_like(Rc.r))
                sh.m[:-1] = Rc.m[1:] * np.arange(1, deg + 1)[:, None]; sh.r[:-1] = succ(Rc.r[1:] * np.arange(1, deg + 1)[:, None] * (1 + 2 * U))
                dR = dR + sh
            Fm = np.zeros((deg + 1, self.Nf)); Fr = np.zeros((deg + 1, self.Nf))
            for j in range(self.M + 1):
                twoj1 = 2 * j + 1
                up_m = 0.5 * (dR.m[:, j] - twoj1 * Rc.m[:, j]); up_r = succ(0.5 * succ(dR.r[:, j] + twoj1 * Rc.r[:, j]) + 2 * U * np.abs(up_m))
                dn_m = 0.5 * (dR.m[:, j] + twoj1 * Rc.m[:, j]); dn_r = succ(0.5 * succ(dR.r[:, j] + twoj1 * Rc.r[:, j]) + 2 * U * np.abs(dn_m))
                if j + 1 <= self.Nf: Fm[:, j] += up_m; Fr[:, j] = succ(Fr[:, j] + up_r)
                if j >= 1: Fm[:, j - 1] += dn_m; Fr[:, j - 1] = succ(Fr[:, j - 1] + dn_r)
            Fr = succ(Fr + 2 * U * np.abs(Fm))
            f_terms.append((alpha, MR(Fm.T, Fr.T)))
            R_terms.append((alpha, Rc, dR))
        return f_terms, R_terms

    def poly_derivative_sups(self, P, hpow):
        """For polynomials P (MR (..., d+1)), upper bounds of sup_{[0,h]} |P^{(i)}| for i = 0..d: sum_{j>=i} |c_j| j!/(j-i)! h^{j-i}."""
        d = P.m.shape[-1] - 1; out = np.zeros(P.m.shape[:-1] + (d + 1,))
        mg = mag(P)
        for i in range(d + 1):
            s = np.zeros(P.m.shape[:-1])
            for j in range(i, d + 1):
                s = succ(s + succ(mg[..., j] * (factorial(j) / factorial(j - i)) * hpow[j - i]))
            out[..., i] = succ(s * (1 + 2 * (d + 1) * U))
        return out

    def ode_tm(self, x0, g, gsup_der, lam, h_up, gsign=1.0):
        """TM of y with y' = lam y + gsign*g on [0,h], y(0) = x0 (MR arrays over modes), lam array (per mode, exact), g a TMArr whose
        polynomial coefficients g_0..g_{Q-1} MUST be enclosures of the exact Taylor coefficients of g (true for the exponential-
        polynomial construction used here: g = e^{4 t_a} sum e^{(4+alpha) sigma} F(sigma), tm_exp coefficients x exact polynomial F); (its
        polynomial part used for the recursion; its remainder is folded into the derivative bounds), gsup_der[..., i] >= sup |g^{(i)}|.
        Remainder: h^{Q+1}/(Q+1)! [ |lam|^{Q+1} Y + sum_i |lam|^{Q-i} gsup_der_i ],  Y >= sup |y| = e^{max(lam,0) h} (|x0| + h sup|g|)."""
        Q = self.Q; lamM = MR.exact(lam)
        coef = [x0]
        for i in range(Q):
            gi = g.c[..., i] if i <= g.Q else MR(np.zeros_like(x0.m))
            coef.append((lamM * coef[-1] + gi * MR.exact(gsign)) * MR(1.0 / (i + 1), succ(U / (i + 1))))
        cm = np.stack([c.m for c in coef], -1); cr = np.stack([c.r for c in coef], -1)
        gsup = gsup_der[..., 0]
        x = succ(np.maximum(lam, 0.0) * h_up); ex = succ(1 + x + x * x)
        Y = succ(ex * succ(mag(x0) + succ(h_up * gsup)))
        al = np.abs(lam)
        bound = succ(al ** (Q + 1) * Y)
        for i in range(Q + 1):
            gi = gsup_der[..., i] if i < gsup_der.shape[-1] else 0.0
            bound = succ(bound + succ(al ** (Q - i) * gi))
        rem = succ(bound * succ(h_up ** (Q + 1) / factorial(Q + 1)) * succ(1 + 4 * (Q + 3) * U))
        return TMArr(MR(cm, cr), rem)

    def conv_scatter(self, Pn, Rj, hpow, h_up, flip2=False):
        """eps contribution  sum_{n,j} Pn_n(tau) Rj_j(tau)  scattered to frequencies N1 (sign +) and N2 (sign S2, or -S2 if flip2).
        Pn: TMArr over n (Nf), Rj: TMArr over j (M+1). Returns TMArr over N (Nmax+1).
        Polynomial products by tensordot over the degree index: prod[n, j, d] = sum_{i+k=d} a[n,i] b[j,k]  (d <= Q), and the
        truncated degrees d > Q bounded by  (sum_i |a_i| h^i)(sum_k |b_k| h^k) - sum_{i+k<=Q} |a_i| h^i |b_k| h^k ."""
        Q = self.Q; Nf = self.Nf; Mj = self.M + 1
        a = Pn.c; b = Rj.c
        # shifted copies of b: Bsh[i, j, d] = b[j, d - i] for d >= i else 0  -> prod[n, j, d] = sum_i a[n, i] Bsh[i, j, d]
        def shifted(arr):
            out = np.zeros((Q + 1, Mj, Q + 1))
            for i in range(Q + 1):
                out[i, :, i:] = arr[:, :Q + 1 - i]
            return out
        Bsh_m = shifted(b.m); Bsh_r = shifted(b.r)
        gam = succ((Q + 1) * U / (1 - (Q + 1) * U))           # rounding of the (Q+1)-term sums (any order)
        cm = np.tensordot(a.m, Bsh_m, axes=([1], [0]))                                   # (Nf, Mj, Q+1)
        absprod = np.tensordot(np.abs(a.m), np.abs(Bsh_m), axes=([1], [0]))
        cr = np.tensordot(np.abs(a.m), Bsh_r, axes=([1], [0])) + np.tensordot(a.r, np.abs(Bsh_m), axes=([1], [0])) + np.tensordot(a.r, Bsh_r, axes=([1], [0]))
        cr = succ(succ(succ(cr * succ(1 + 3 * gam)) + succ(gam * absprod)) + 4 * (Q + 2) * ETA)      # products and sums may underflow: eta/2 each
        # truncation: full product of the h-weighted magnitude sums minus the kept part (degrees <= Q)
        ah = mag(a) * hpow[None, :Q + 1]; bh = mag(b) * hpow[None, :Q + 1]
        full = succ(ah.sum(1)[:, None] * bh.sum(1)[None, :] * succ(1 + 2 * (Q + 2) * U))
        Bsh_h = shifted(bh)
        kept = np.tensordot(ah, Bsh_h, axes=([1], [0])).sum(2)                            # sum over d <= Q of sum_{i+k=d}
        # underflow of the h-weighted magnitudes (|a_i| h^i or |b_k| h^k rounded to zero) is amplified by the other factor: allowance
        # (Q+2) eta (sum_i |a_i| h^i + sum_k |b_k| h^k) per pair, plus the product/sum allowances
        amp = succ((Q + 2) * ETA * succ(ah.sum(1)[:, None] + bh.sum(1)[None, :]) * (1 + 4 * U))
        trunc = succ(succ(succ(np.maximum(full - kept * (1 - 2 * (Q + 2) * U), 0.0) + succ(full * 4 * (Q + 2) * U)) + 2 * (Q + 2) ** 2 * ETA) + amp)
        supP = Pn.sup(hpow); supR = Rj.sup(hpow)
        rem = succ(succ(succ(supP[:, None] * Rj.r[None, :]) + succ(supR[None, :] * Pn.r[:, None])) + succ(Pn.r[:, None] * Rj.r[None, :]))
        rem = succ(rem + trunc)
        # scatter to frequencies
        Nmax = self.Nmax; out_m = np.zeros((Nmax + 1, Q + 1)); out_r = np.zeros((Nmax + 1, Q + 1))
        idx1 = self.N1.ravel(); idx2 = self.N2.ravel(); s2 = (-self.S2 if flip2 else self.S2).ravel()   # term 2: sin(2n-2j-1): + for n > j, - for n <= j
        cnt = np.bincount(idx1, minlength=Nmax + 1) + np.bincount(idx2, minlength=Nmax + 1)
        gamc = succ(cnt * U / (1 - cnt * U))
        for q in range(Q + 1):
            v = cm[..., q].ravel(); vr = cr[..., q].ravel()
            out_m[:, q] = np.bincount(idx1, weights=v, minlength=Nmax + 1) + np.bincount(idx2, weights=s2 * v, minlength=Nmax + 1)
            absum = np.bincount(idx1, weights=np.abs(v), minlength=Nmax + 1) + np.bincount(idx2, weights=np.abs(v), minlength=Nmax + 1)
            rsum = np.bincount(idx1, weights=vr, minlength=Nmax + 1) + np.bincount(idx2, weights=vr, minlength=Nmax + 1)
            out_r[:, q] = succ(succ(rsum * succ(1 + cnt * U)) + succ(gamc * absum * succ(1 + cnt * U)))
        rr = rem.ravel()
        out_rem = succ((np.bincount(idx1, weights=rr, minlength=Nmax + 1) + np.bincount(idx2, weights=rr, minlength=Nmax + 1)) * succ(1 + cnt * U))
        return TMArr(MR(out_m, out_r), out_rem)

    def cell(self, ci):
        """Spline sub-cell ci: a_m = exact polynomial (one term, alpha = 0)."""
        h = self.tb[ci + 1] - self.tb[ci]; h_up = h.mag()
        res = self.cell_core(h_up, self.e_ta[ci], [(0.0, self.T[ci])], self.A[ci], self.B[ci], self.m_ta[ci], self.wfar_ta[ci])
        res.update(ci=ci, t_a=float(self.tb.m[ci]), h=float(h_up))
        return res

    @staticmethod
    def mr_powers(h_up, Q):
        """MR enclosures of h_up^i, i = 0..Q (h_up an exact double), for signed polynomial transformations."""
        hp = MR.exact(h_up); out = [MR.exact(1.0)]
        for i in range(1, Q + 1): out.append(out[-1] * hp)
        return MR(np.array([o.m for o in out]), np.array([o.r for o in out]))

    def cell_core(self, h_up, e_ta, a_terms, A0, B0, m_ta, wfar_ta):
        """Taylor-model bounds on one sub-cell [0, h] (local sigma): a_terms = [(alpha, Tpoly (deg+1, M))] exact exponential-
        polynomial representation of a_m; A0, B0 = A_n, B_n at the cell start (MR (Nf,)); e_ta = e^{t_a}; m_ta, wfar_ta =
        m(r_a), (1+u_a)^0.5 (MR scalars).  Returns the dict of bounds (W = sum_N sup|eps_N| over the cell, etc.)."""
        Q = self.Q; n = self.n
        hpow = np.array([1.0] + [succ(h_up ** i * (1 + 2 * i * U)) for i in range(1, 2 * Q + 3)])
        f_terms, R_terms = self.f_terms_from_a(a_terms)
        e2 = e_ta * e_ta; e3 = e2 * e_ta; e4 = e2 * e2
        inv_e = MR(1.0 / e_ta.m, succ(e_ta.r / (e_ta.mig() ** 2) + U * abs(1.0 / e_ta.m)))
        inv_e2 = inv_e * inv_e
        def bc(c, r, S):
            return TMArr(MR(np.broadcast_to(c.m, (S, Q + 1)).copy(), np.broadcast_to(c.r, (S, Q + 1)).copy()), np.full(S, r))
        def zero_tm(S):
            return TMArr(MR(np.zeros((S, Q + 1)), np.zeros((S, Q + 1))), np.zeros(S))
        # g_n(sigma) = e^{2t} f_n(e^t) = e^{4 t_a} sum_terms e^{(4+alpha) sigma} F_n(sigma); derivative sups by the exponential-polynomial form
        g = zero_tm(self.Nf); gsup = np.zeros((self.Nf, Q + 1))
        for alpha, F in f_terms:
            gam = alpha + MR.exact(4.0); gabs = float(gam.mag())
            Ec, Er = tm_exp(gam, h_up, Q)
            g = g + bc(Ec, Er, self.Nf).mul_poly(F, hpow)
            Fsup = self.poly_derivative_sups(F, hpow)                                      # (Nf, deg+1)
            x = succ(gabs * h_up); assert x <= 1.0, "exponent too large for the cell"; egh = succ(1 + x + x * x)
            degF = F.m.shape[1] - 1
            for i in range(Q + 1):
                s_ = np.zeros(self.Nf)
                for kk in range(min(i, degF) + 1):
                    s_ = succ(s_ + succ(comb(i, kk) * succ(gabs ** (i - kk) * (1 + 2 * (i - kk) * U)) * Fsup[:, kk]))
                gsup[:, i] = succ(gsup[:, i] + succ(s_ * egh * (1 + 4 * (Q + 1) * U)))
        g = g.scale(e4); gsup = succ(gsup * mag(e4) * (1 + 4 * U))
        A = self.ode_tm(A0, g, gsup, -2.0 * n, h_up)
        B = self.ode_tm(B0, g, gsup, 2.0 * n, h_up, gsign=-1.0)       # B' = 2n B - g
        inv4n = MR(1.0 / (4 * n), succ(U / (4 * n)))
        psi = (A + B).scale(inv4n)
        Em1c, Em1r = tm_exp(-1.0, h_up, Q); Em2c, Em2r = tm_exp(-2.0, h_up, Q)
        Em1 = bc(Em1c, Em1r, self.Nf); Em2 = bc(Em2c, Em2r, self.Nf)
        def tm_mul(X, Y):
            Z = X.mul_poly(Y.c, hpow); supX = X.sup(hpow)
            return TMArr(Z.c, succ(Z.r + succ(supX * Y.r)))
        dpsi = tm_mul((B - A).scale(inv_e * MR.exact(0.5)), Em1)                           # psi_n'
        Pn = tm_mul(psi.scale(MR(-1.0 * n, 0.0) * inv_e2), Em2)                           # -(1/2) 2n psi_n e^{-2t}
        Qn = tm_mul(dpsi.scale(MR.exact(0.5) * inv_e), Em1)                               # (1/2) psi_n' e^{-t}
        # R_j, dR_j/dt as TMs: sum_terms e^{3 t_a} e^{(3+alpha) sigma} (Rc_j, dR_j)
        Rj = zero_tm(self.M + 1); Rtj = zero_tm(self.M + 1)
        for alpha, Rc, dR in R_terms:
            Ec, Er = tm_exp(alpha + MR.exact(3.0), h_up, Q); E = bc(Ec, Er, self.M + 1)
            Rj = Rj + E.mul_poly(MR(Rc.m.T, Rc.r.T), hpow)
            Rtj = Rtj + E.mul_poly(MR(dR.m.T, dR.r.T), hpow)
        Rj = Rj.scale(e3); Rtj = Rtj.scale(e3)
        twoj1 = 2.0 * np.arange(self.M + 1) + 1.0
        Rhat = TMArr(Rj.c * MR(twoj1[:, None], 0.0), succ(Rj.r * twoj1))                   # (2j+1) R_j
        eps_m = np.zeros((self.Nmax + 1, Q + 1)); eps_r = np.zeros((self.Nmax + 1, Q + 1)); eps_rem = np.zeros(self.Nmax + 1)
        lin = Rtj.scale(self.c_l) - Rj
        eps_m[:self.M + 1] = lin.c.m; eps_r[:self.M + 1] = lin.c.r; eps_rem[:self.M + 1] = lin.r
        E1 = self.conv_scatter(Pn, Rtj, hpow, h_up)
        E2 = self.conv_scatter(Qn, Rhat, hpow, h_up, flip2=True)
        tot = TMArr(MR(eps_m, eps_r), eps_rem) + E1 + E2
        self._last_tms = dict(A=A, B=B, psi=psi, dpsi=dpsi, Rj=Rj, Rtj=Rtj, eps=tot, hpow=hpow, h_up=h_up, e_ta=e_ta, inv_e=inv_e)
        supN, W, W1, W2 = self.bernstein_sup_sub(tot, hpow, h_up, K=4)      # sub-interval Bernstein bounds (tighter sum of suprema)
        self._last_supN = supN
        m_inf = np.nextafter(m_ta.m - m_ta.r, -np.inf)                                   # m increasing in r: inf over the cell at its left end
        wf_sup = succ((wfar_ta.m + wfar_ta.r) * succ(1 + 0.5 * h_up + 0.5 * h_up * h_up))   # (1+u)^0.5 <= (1+u_a)^0.5 e^{h/2} (u e^h >= u)
        # R2 piece: int_cell |eps/m|^2 dX/(1+u^2) <= pi sum_N sup_N^2 * h * max_cell r^2/(m^2 (1+u^2)), the max at the left end (decreasing)
        r2m2 = succ((e_ta.m + e_ta.r) ** 2 / (m_inf ** 2 * (1 + ((e_ta.m - e_ta.r) / self.L) ** 2)) * (1 + 8 * U))
        L2piece = succ(np.pi * 1.0000000001 * succ((supN ** 2).sum() * (1 + (self.Nmax + 2) * U)) * h_up * r2m2)
        return dict(W=float(W), W1=float(W1), W2=float(W2), m_inf=float(m_inf), W_over_m=float(succ(W / m_inf)), W_over_m_far=float(succ(succ(W / m_inf) * wf_sup)),
                    L2piece=float(L2piece), sup_lin=float(lin.sup(hpow).max()), remA=float(A.r.max()), remB=float(B.r.max()),
                    rem_eps=float(tot.r.max()), sup_eps_max=float(supN.max()), N_at_max=int(np.argmax(supN)))


def main(green, trial, out, Q=12, c0=0, c1=None):
    C = Certifier(green, trial, Q)
    c1 = C.nc if c1 is None else min(c1, C.nc)
    t0 = time.time(); rows = []; sups = []
    for ci in range(c0, c1):
        rows.append(C.cell(ci)); sups.append(np.nextafter(C._last_supN, np.inf))
        if (ci - c0) % 50 == 0:
            r = rows[-1]
            print("cell %d/%d t_a=%.4f r=%.4g  W=%.3e  W/m=%.3e  remA=%.1e remB=%.1e rem_eps=%.1e  (%.0fs)" % (
                ci, C.nc, r["t_a"], np.exp(r["t_a"]), r["W"], r["W_over_m"], r["remA"], r["remB"], r["rem_eps"], time.time() - t0), flush=True)
            json.dump(dict(rows=rows, Q=Q, done=False), open(out, "w"))
    json.dump(dict(rows=rows, Q=Q, done=True, time=time.time() - t0), open(out, "w"))
    np.savez_compressed(out.replace(".json", "_supN.npz"), supN=np.array(sups), t_a=np.array([r_["t_a"] for r_ in rows]), h=np.array([r_["h"] for r_ in rows]))
    Wm = np.array([r["W_over_m"] for r in rows]); ra = np.exp(np.array([r["t_a"] for r in rows])); L2 = sum(r["L2piece"] for r in rows)
    print("done %d cells in %.0fs; max W/m = %.4e at r = %.4g ; sum of L2 pieces (middle region) = %.4e" % (len(rows), time.time() - t0, Wm.max(), ra[np.argmax(Wm)], L2))






def bernstein_sup_sub(self, tot, hpow, h_up, K=4):
    """sup over [0,h] of sum_N |p_N| (Wiener sum) and per-N sups, from the TM 'tot' (coefficients (S, Q+1), remainders),
    using K equal sub-intervals: on each, re-centre the polynomial (exact binomial shift in mid-rad arithmetic), Bernstein
    bound with length h/K; W_bound = max over sub-intervals of sum_N sup_sub|p_N| (+ remainders); supN = max over sub-intervals."""
    from math import comb as _comb
    Q = self.Q; S = tot.c.m.shape[0]; hk = succ(h_up / K)          # sub-interval length (upper bound: the Bernstein bound on a longer interval is valid)
    hkP = self.mr_powers(hk, Q)                                      # MR enclosures of hk^i for the signed transformation
    supN_all = np.zeros(S); W_best = 0.0; W1_best = 0.0; W2_best = 0.0
    twoN1 = 2.0 * np.arange(S) + 1.0
    for kk in range(K):
        a = kk * hk                                     # sub-interval start (exact multiple of hk up to rounding, covered by using hk upper bound)
        # re-centre: q_j = sum_{i>=j} C(i,j) c_i a^{i-j}
        cm = np.zeros_like(tot.c.m); cr = np.zeros_like(tot.c.r)
        apow = [MR.exact(1.0)]
        for i in range(1, Q + 1): apow.append(apow[-1] * MR(a, succ(U * a)))
        for j in range(Q + 1):
            acc = MR(np.zeros(S), np.zeros(S))
            for i in range(j, Q + 1):
                acc = acc + tot.c[..., i] * MR.exact(float(_comb(i, j))) * apow[i - j]
            cm[:, j] = acc.m; cr[:, j] = acc.r
        ah = MR(cm, cr) * MR(hkP.m[None, :], hkP.r[None, :])
        b = mr_matmul(ah, MR(self.Bern.m.T, self.Bern.r.T))
        supN = succ(mag(b).max(-1) + tot.r)
        supN_all = np.maximum(supN_all, supN)
        W_best = max(W_best, succ(supN.sum() * succ(1 + (S + 1) * U)))
        W1_best = max(W1_best, succ((supN * twoN1).sum() * succ(1 + (S + 2) * U)))
        W2_best = max(W2_best, succ((supN * twoN1 ** 2).sum() * succ(1 + (S + 3) * U)))
    return supN_all, W_best, W1_best, W2_best


Certifier.bernstein_sup_sub = bernstein_sup_sub


# =====================================================================================================================
# Derivative Taylor models (SPEC v2 items R1, R3, R5): TMs of d_t^i eps_N for i <= nder on a sub-cell, by the exact
# identities A' = -2n A + g, B' = 2n B - g (g, R exponential-polynomials differentiated exactly) and Leibniz rules.
# =====================================================================================================================
def _cell_core_deriv(self, h_up, e_ta, a_terms, A0, B0, m_ta, wfar_ta, nder=2):
    from math import comb as _comb
    Q = self.Q; n = self.n
    hpow = np.array([1.0] + [succ(h_up ** i * (1 + 2 * i * U)) for i in range(1, 2 * Q + 3)])
    f_terms, R_terms = self.f_terms_from_a(a_terms)
    e2 = e_ta * e_ta; e3 = e2 * e_ta; e4 = e2 * e2
    inv_e = MR(1.0 / e_ta.m, succ(e_ta.r / (e_ta.mig() ** 2) + U * abs(1.0 / e_ta.m))); inv_e2 = inv_e * inv_e

    def bc(c, r, S):
        return TMArr(MR(np.broadcast_to(c.m, (S, Q + 1)).copy(), np.broadcast_to(c.r, (S, Q + 1)).copy()), np.full(S, r))

    def zero_tm(S):
        return TMArr(MR(np.zeros((S, Q + 1)), np.zeros((S, Q + 1))), np.zeros(S))

    def tm_mul(X, Y):
        Z = X.mul_poly(Y.c, hpow); supX = X.sup(hpow)
        return TMArr(Z.c, succ(Z.r + succ(supX * Y.r)))

    def poly_deriv(P):          # MR polynomial (deg+1, S) ascending in sigma -> derivative
        dm = np.zeros_like(P.m); dr = np.zeros_like(P.r)
        if P.m.shape[0] > 1:
            dm[:-1] = P.m[1:] * np.arange(1, P.m.shape[0])[:, None]; dr[:-1] = succ(P.r[1:] * np.arange(1, P.m.shape[0])[:, None] + U * np.abs(dm[:-1]))
        return MR(dm, dr)

    # --- g and its t-derivatives (exact exponential-polynomials): g^{(i)} = e^{4 t_a} sum e^{(4+alpha) sigma} F_i, F_{i+1} = (4+alpha) F_i + F_i'
    g_list = [zero_tm(self.Nf) for _ in range(nder + 1)]; gsup = np.zeros((self.Nf, Q + 1))
    for alpha, F in f_terms:
        gam = alpha + MR.exact(4.0); gabs = float(gam.mag()); Ec, Er = tm_exp(gam, h_up, Q); E = bc(Ec, Er, self.Nf)
        Fi = MR(F.m.T, F.r.T)                                            # (deg+1, Nf)
        Fsup = self.poly_derivative_sups(F, hpow); degF = F.m.shape[1] - 1
        x = succ(gabs * h_up); assert x <= 1.0; egh = succ(1 + x + x * x)
        for i in range(Q + 1):
            s_ = np.zeros(self.Nf)
            for kk in range(min(i, degF) + 1):
                s_ = succ(s_ + succ(_comb(i, kk) * succ(gabs ** (i - kk) * (1 + 2 * (i - kk) * U)) * Fsup[:, kk]))
            gsup[:, i] = succ(gsup[:, i] + succ(s_ * egh * (1 + 4 * (Q + 1) * U)))
        for i in range(nder + 1):
            g_list[i] = g_list[i] + E.mul_poly(MR(Fi.m.T, Fi.r.T), hpow)
            Fi = Fi * gam + poly_deriv(Fi)
    g_list = [gi.scale(e4) for gi in g_list]; gsup = succ(gsup * mag(e4) * (1 + 4 * U))
    # --- A, B and derivatives
    A = [self.ode_tm(A0, g_list[0], gsup, -2.0 * n, h_up)]; B = [self.ode_tm(B0, g_list[0], gsup, 2.0 * n, h_up, gsign=-1.0)]
    m2n = MR(-2.0 * n, 0.0); p2n = MR(2.0 * n, 0.0)
    for i in range(nder):
        A.append(A[-1].scale(m2n) + g_list[i]); B.append(B[-1].scale(p2n) - g_list[i])
    inv4n = MR(1.0 / (4 * n), succ(U / (4 * n)))
    psi = [(A[i] + B[i]).scale(inv4n) for i in range(nder + 1)]
    BmA = [(B[i] - A[i]) for i in range(nder + 1)]
    Em2c, Em2r = tm_exp(-2.0, h_up, Q); Em2 = bc(Em2c, Em2r, self.Nf)
    # P~^{(i)} = -n e^{-2 t_a} sum_l C(i,l) psi^{(l)} (-2)^{i-l} e^{-2 sigma};  Q~^{(i)} = (1/4) e^{-2 t_a} sum_l C(i,l) (B-A)^{(l)} (-2)^{i-l} e^{-2 sigma}
    Pt = []; Qt = []
    for i in range(nder + 1):
        accP = zero_tm(self.Nf); accQ = zero_tm(self.Nf)
        for l in range(i + 1):
            cst = _comb(i, l) * (-2.0) ** (i - l)
            accP = accP + psi[l].scale(MR.exact(cst)); accQ = accQ + BmA[l].scale(MR.exact(cst))
        Pt.append(tm_mul(accP.scale(MR(-1.0 * n, 0.0) * inv_e2), Em2))
        Qt.append(tm_mul(accQ.scale(MR.exact(0.25) * inv_e2), Em2))
    # --- R_j^{(i)}: exact exponential-polynomials; R^{(i)} = e^{3 t_a} sum e^{(3+alpha) sigma} Rc_i, Rc_{i+1} = (3+alpha) Rc_i + Rc_i'
    Rd = [zero_tm(self.M + 1) for _ in range(nder + 2)]
    for alpha, Rc, dR in R_terms:
        a3 = alpha + MR.exact(3.0); Ec, Er = tm_exp(a3, h_up, Q); E = bc(Ec, Er, self.M + 1)
        Ri = Rc
        for i in range(nder + 2):
            Rd[i] = Rd[i] + E.mul_poly(MR(Ri.m.T, Ri.r.T), hpow)
            Ri = Ri * a3 + poly_deriv(Ri)
    Rd = [r_.scale(e3) for r_ in Rd]
    twoj1 = 2.0 * np.arange(self.M + 1) + 1.0
    Rhat = [TMArr(Rd[i].c * MR(twoj1[:, None], 0.0), succ(Rd[i].r * twoj1)) for i in range(nder + 1)]
    # --- eps^{(i)} = c_l R^{(i+1)} - R^{(i)} + sum_l C(i,l) [P~^{(l)} * Rt^{(i-l)} + Q~^{(l)} * R^^{(i-l)}]
    eps = []
    for i in range(nder + 1):
        lin = Rd[i + 1].scale(self.c_l) - Rd[i]
        em = np.zeros((self.Nmax + 1, Q + 1)); er = np.zeros((self.Nmax + 1, Q + 1)); erem = np.zeros(self.Nmax + 1)
        em[:self.M + 1] = lin.c.m; er[:self.M + 1] = lin.c.r; erem[:self.M + 1] = lin.r
        tot = TMArr(MR(em, er), erem)
        for l in range(i + 1):
            cst = MR.exact(float(_comb(i, l)))
            E1 = self.conv_scatter(Pt[l].scale(cst), Rd[1 + i - l], hpow, h_up)
            E2 = self.conv_scatter(Qt[l].scale(cst), Rhat[i - l], hpow, h_up, flip2=True)
            tot = tot + E1 + E2
        eps.append(tot)
    self._last_eps = eps          # stash of the per-mode TMs of d_t^i eps_N (used by cert_forcing.py; added shift 4, arithmetic unchanged)
    # --- bounds: sup_N |eps^{(i)}_N| by Bernstein; Wiener sums with angular factors (2N+1)^j
    twoN1 = 2.0 * np.arange(self.Nmax + 1) + 1.0
    out = dict(remA=float(A[0].r.max()), remB=float(B[0].r.max()))
    supNs = []
    for i in range(nder + 1):
        tot = eps[i]
        supN, Wb0, Wb1, Wb2 = self.bernstein_sup_sub(tot, hpow, h_up, K=4); supNs.append(supN)
        Wb = [Wb0, Wb1, Wb2]
        for j in range(nder + 1 - i):
            out["W_%d_%d" % (i, j)] = float(Wb[j]) if j <= 2 else float(succ((supN * twoN1 ** j).sum() * succ(1 + (self.Nmax + 2 + j) * U)))
        out["rem_eps_%d" % i] = float(tot.r.max())
    # R5: eps - d_t eps (Wiener), K~ = rho~ - d_t rho~ modes R - R^{(1)} (Wiener), and d_t K~
    if nder >= 1:
        d = eps[0] - eps[1]
        hP = self.mr_powers(h_up, Q); ah = d.c * MR(hP.m[None, :], hP.r[None, :])
        b = mr_matmul(ah, MR(self.Bern.m.T, self.Bern.r.T)); s_ = succ(mag(b).max(-1) + d.r)
        out["W_eps_minus_dteps"] = float(succ(s_.sum() * (1 + (self.Nmax + 2) * U)))
        Kt = Rd[0] - Rd[1]
        for name, tm in (("K", Kt), ("dtK", Rd[1] - Rd[2])):
            ah = tm.c * MR(hP.m[None, :], hP.r[None, :])
            b = mr_matmul(ah, MR(self.Bern.m.T, self.Bern.r.T)); s_ = succ(mag(b).max(-1) + tm.r)
            out["W_" + name] = float(succ(s_.sum() * (1 + (self.M + 2) * U))); out["W1_" + name] = float(succ((s_ * (2.0 * np.arange(self.M + 1) + 1.0)).sum() * (1 + (self.M + 3) * U)))
    m_inf = np.nextafter(m_ta.m - m_ta.r, -np.inf)
    wf_sup = succ((wfar_ta.m + wfar_ta.r) * succ(1 + 0.5 * h_up + 0.5 * h_up * h_up))
    out.update(m_inf=float(m_inf), wf_sup=float(wf_sup), W=out["W_0_0"], W_over_m=float(succ(out["W_0_0"] / m_inf)))
    self._last_supNs = supNs
    return out


Certifier.cell_core_deriv = _cell_core_deriv


def cell_deriv(self, ci, nder=2):
    h = self.tb[ci + 1] - self.tb[ci]; h_up = h.mag()
    res = self.cell_core_deriv(h_up, self.e_ta[ci], [(0.0, self.T[ci])], self.A[ci], self.B[ci], self.m_ta[ci], self.wfar_ta[ci], nder)
    res.update(ci=ci, t_a=float(self.tb.m[ci]), h=float(h_up))
    return res


Certifier.cell_deriv = cell_deriv


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], a[3], int(a[4]) if len(a) > 4 else 12, int(a[5]) if len(a) > 5 else 0, int(a[6]) if len(a) > 6 else None)
