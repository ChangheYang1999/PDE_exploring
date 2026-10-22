"""Rigorous bound of the weighted residual norm on the far tail tau >= T_out (r >= R0 e^{T_out}) by termwise bounds of the
exponential-polynomial representation at tau = T_out (SPEC item R0, region r > R0 beyond the Taylor-model sub-cells).

On the outer region every modal function is an exponential-polynomial in tau = t - t0 (closed forms, computed in Arb at
PREC bits where the cancellation of the primitive is harmless). For tau >= T:
  A_n(tau) = e^{-2n (tau - T)} C^A_n + e^{2 t0} sum_terms e^{(2+alpha') tau} S^A_{n,term}(tau),   C^A_n = A_n(T) - e^{2 t0} sum e^{(2+alpha') T} S^A(T)
  B_n(tau) = -e^{2 t0} sum_terms e^{(2+alpha') tau} S^B_{n,term}(tau)     (S^A, S^B the primitive polynomial factors with lam = 2n+2+alpha', mu = 2-2n+alpha';
   the minus sign because int_tau^oo e^{mu s} p = -e^{mu tau} S^B(tau) for mu < 0;
                                                                            B has no transient because its boundary condition is at infinity)
  R_j, dR_j/dt = e^{3 t0} sum_terms e^{(3+alpha) tau} (Rc_j, dR_j)(tau).
Every product term in eps_N has a net exponent <= 2k - 1 relative... precisely: the residual eps = (c_l Rt - R) + sum_{n,j} [P~_n Rt_j, Q~_n R^_j]
with P~_n = -n psi_n e^{-2t}, Q~_n = psi_n' e^{-t}/2; all product exponents are <= 2k - 1 < k - delta for delta < 1 - k, and the
exponent-k term of c_l Rt - R has the coefficient (c_l k - 1) A_N0 = 0 exactly (c_l := 1/k).  Hence for tau >= T the weighted
quantity W(tau)(1+u)^delta/m(tau) is bounded by its termwise majorant at tau = T, which is what this module computes:
  tail_bound = [ sum_N |lin_N|^(T) + 2 (sum_n |P~_n|^(T)) (sum_j |Rt_j|^(T)) + 2 (sum_n |Q~_n|^(T)) (sum_j |R^_j|^(T)) ] * (1+u_T)^delta / m_low(T),
  (factor 2: each product term feeds two sine frequencies; refined version below keeps the exact e^{(2k-1) tau} coefficient),
where |.|^(T) denotes the sum of the absolute values of all exponential-polynomial terms evaluated at T (polynomial factors with
absolute coefficients), with the exponent-k term of lin removed by the exact identity. (For the polynomial factors tau^i of the
correction terms the majorant |coef| tau^i e^{(gamma - k + delta) tau} must be decreasing for tau >= T: checked by requiring
i/T <= -(gamma - k + delta) for each such term; the correction exponents are about -120, so this always holds.)
Usage: python3 cert_tail.py trial.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz delta out.json [PREC]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx
from math import factorial
from cert_green import Cert, prim_S, load_ball
from modal_fit import OUTER_JL, NIN, NCOR, NOUT


def abs_poly_at(coeffs, tau):
    return sum((abs(c) * tau ** j for j, c in enumerate(coeffs)), arb(0))


def main(trial, green, coeffs, outer, delta, out, prec=256):
    t0_ = time.time()
    C = Cert(trial, prec, 0.0)
    cj = json.load(open(coeffs))
    C.Ei = [[load_ball(x) for x in row] for row in cj["Ei"]]; C.Eo = [[load_ball(x) for x in row] for row in cj["Eo"]]; C.A[0][0] = load_ball(cj["A00"])
    g = np.load(outer); T = arb(float(g["tau"][-1]), float(g["tau_rad"][-1]))
    A_T = [arb(float(m), float(r)) for m, r in zip(g["A_mid"][-1], g["A_rad"][-1])]
    Nf = C.Nf; M = C.M; k = C.k; delta = arb(delta)
    outer_terms = C.outer_terms()                          # [(alpha, coeffs[q][m])] in tau
    f_out = C.f_terms(outer_terms, (2 * C.t0).exp())       # [(alpha' = alpha+2, fc[q][n])] includes e^{2 t0}
    e2t0 = (2 * C.t0).exp(); e3t0 = (3 * C.t0).exp(); eT = (C.t0 + T).exp(); u_T = eT / C.L
    m_low = u_T ** k * (1 + 1 / (u_T * u_T)) ** ((k - 3) / 2)          # m = u^k (1+u^-2)^((k-3)/2) exactly
    wT = (1 + u_T) ** delta
    # termwise majorants at T of psi_n (via A and B), psi_n' , then P~, Q~
    Pabs = arb(0); Qabs = arb(0)
    for n in range(1, Nf + 1):
        absA = arb(0); transient = A_T[n - 1]
        absB = arb(0)
        for alpha, fc in f_out:
            lam = 2 * n + 2 + alpha; mu = 2 - 2 * n + alpha
            cf = [fc[q][n - 1] for q in range(len(fc))]
            if all(c == 0 for c in cf): continue
            # S^A: primitive polynomial factor for lam (e^{lam tau} S(tau) is the primitive of e^{lam tau} p)
            # A-contribution: e^{2 t0} e^{(2+alpha) tau} [S(tau) - e^{-lam tau} S(0)]... we bound termwise: |e^{2t0} e^{(2+alpha)tau} S(tau)| + transient part
            # exact: A_n(tau) = e^{-2n(tau-T)} [A_n(T) - e^{2t0} e^{(2+alpha)T} S_A(T)] + e^{2t0} e^{(2+alpha) tau} S_A(tau) (summed over terms)
            SA_T = prim_S(lam, cf, T)
            transient -= e2t0 * ((2 + alpha) * T).exp() * SA_T
            # proper majorant: expand S_A as a polynomial with explicit coefficients: S(tau) = sum_j c_j sum_l (-1)^l j!/(j-l)! tau^{j-l}/lam^{l+1}
            SA_coeffs = [arb(0)] * len(cf)
            for j, c in enumerate(cf):
                for l in range(j + 1):
                    SA_coeffs[j - l] += c * (-1) ** l * (arb(factorial(j)) / factorial(j - l)) / lam ** (l + 1)
            absA += e2t0 * ((2 + alpha) * T).exp() * abs_poly_at(SA_coeffs, T)
            # B_n(tau) = -e^{2t0} sum e^{(2+alpha) tau} S_B(tau) with S_B the primitive factor for mu (int_tau^oo = -primitive(tau) since the primitive -> 0 at infinity, mu < 0)
            SB_coeffs = [arb(0)] * len(cf)
            for j, c in enumerate(cf):
                for l in range(j + 1):
                    SB_coeffs[j - l] += c * (-1) ** l * (arb(factorial(j)) / factorial(j - l)) / mu ** (l + 1)
            absB += e2t0 * ((2 + alpha) * T).exp() * abs_poly_at(SB_coeffs, T)
        absA += abs(transient)
        psi_abs = (absA + absB) / (4 * n); dpsi_abs = (absA + absB) / (2 * eT)
        Pabs += n * psi_abs / (eT * eT); Qabs += dpsi_abs / (2 * eT)
    # R_j, Rt_j termwise majorants; lin = c_l Rt - R with the exponent-k term removed
    Rabs = arb(0); Rtabs = arb(0); Rhatabs = arb(0); linabs = arb(0)
    Rc0 = None; Rc1 = None
    for alpha, c in outer_terms:
        deg = len(c) - 1
        Rc = [C.R_from_a(c[q]) for q in range(deg + 1)]
        dRc = [[(3 + alpha) * Rc[q][j] + (Rc[q + 1][j] * (q + 1) if q + 1 <= deg else arb(0)) for j in range(M + 1)] for q in range(deg + 1)]
        ea = e3t0 * ((3 + alpha) * T).exp()
        is_lead = (alpha == C.alpha[0])     # exponent k: c_l dR - R = (c_l k - 1) Rc = 0 exactly (c_l = 1/k): dropped by the identity
        is_sub = (alpha == C.alpha[1])      # exponent 2k - 1: kept EXACTLY (its coefficient enters C_N below)
        if is_lead: Rc0 = Rc[0]
        if is_sub: Rc1 = Rc[0]
        for j in range(M + 1):
            R_T = abs_poly_at([Rc[q][j] for q in range(deg + 1)], T) * ea
            Rt_T = abs_poly_at([dRc[q][j] for q in range(deg + 1)], T) * ea
            Rabs += R_T; Rtabs += Rt_T; Rhatabs += (2 * j + 1) * R_T
            if not (is_lead or is_sub):
                linabs += abs_poly_at([C.c_l * dRc[q][j] - Rc[q][j] for q in range(deg + 1)], T) * ea
    crude_total = linabs + 2 * (Pabs * Rtabs + Qabs * Rhatabs)
    # ---- refined leading order: exact e^{(2k-1) tau} coefficient C_N (linear q = 1 term + leading psi x leading rho products), the
    # corresponding termwise magnitudes removed from the majorant. Leading psi_n term (exponent k+1): A-part a_n = e^{2t0} c_n / lam_n,
    # B-part b_n = -e^{2t0} c_n / mu_n (both positive multiples of c_n), c_n = coefficient of the alpha_0 term of f_n (includes e^{2t0}),
    # lam_n = 2n + k + 1, mu_n = k + 1 - 2n.  P~_n^lead = -(a_n + b_n) e^{-2t0}/4 e^{(k-1)tau}, Q~_n^lead = (b_n - a_n) e^{-2t0}/4 e^{(k-1)tau};
    # R_j^lead = e^{3t0} Rc0_j e^{k tau}, Rt_j^lead = k R_j^lead, R^_j^lead = (2j+1) R_j^lead.
    alpha0 = C.alpha[0]; fc0 = None
    for alpha, fc in f_out:
        if alpha == alpha0 + 2: fc0 = fc[0]
    Nmax = 2 * M + 2; CN = [arb(0)] * (Nmax + 1)
    em2 = (-2 * C.t0).exp()
    for j in range(M + 1):
        CN[j] += (C.c_l * (2 * k - 1) - 1) * e3t0 * Rc1[j]
    lead_mag_P = arb(0); lead_mag_Q = arb(0)
    e2k1T = ((2 * k - 1) * T).exp()
    for n in range(1, Nf + 1):
        cn = fc0[n - 1]
        if cn == 0: continue
        lam_n = 2 * n + k + 1; mu_n = k + 1 - 2 * n
        a_n = e2t0 * cn / lam_n; b_n = -e2t0 * cn / mu_n
        Plead = -(a_n + b_n) * em2 / 4; Qlead = (b_n - a_n) * em2 / 4
        Pmaj = (abs(a_n) + abs(b_n)) * em2 / 4; Qmaj = Pmaj
        for j in range(M + 1):
            Rl = e3t0 * Rc0[j]
            if Rl == 0: continue
            coefP = Plead * k * Rl; coefQ = Qlead * (2 * j + 1) * Rl
            # scatter: P-term to N1 = j + n (+) and N2 (sign +1 if n <= j else -1); Q-term to N1 (+) and N2 (opposite sign)
            N1 = j + n; N2 = (j - n) if n <= j else (n - j - 1); s2 = 1 if n <= j else -1
            if N1 <= Nmax: CN[N1] += coefP + coefQ
            if N2 <= Nmax: CN[N2] += s2 * coefP - s2 * coefQ
            lead_mag_P += Pmaj * abs(k * Rl); lead_mag_Q += Qmaj * (2 * j + 1) * abs(Rl)
    sumC = sum((abs(x) for x in CN), arb(0)) * e2k1T
    rest = linabs + 2 * (Pabs * Rtabs + Qabs * Rhatabs) - 2 * (lead_mag_P + lead_mag_Q) * e2k1T
    if rest < 0: rest = arb(0)
    total = sumC + rest
    # monotonicity precondition of the majorant for tau >= T: for every absolute monomial tau^i e^{beta tau} appearing, beta + i/T + delta - k <= 0.
    # Exponents: lin terms 3 + alpha_q (q >= 1) and 3 - bo (degree <= 6); products: (psi exponents <= k+1 or <= 3 - bo + 4, A-transient -2n) - 2 + (3 + alpha or 3 - bo).
    worst = arb(-100)
    for q in range(1, NOUT):
        worst = max(worst, 3 + C.alpha[q] + delta - k)
    worst = max(worst, 3 - C.bo + arb(6) / T + delta - k)                      # corrections, degree <= 6
    worst = max(worst, (k + 1) - 2 + (3 + C.alpha[0]) + delta - k)              # leading product: (k+1) - 2 + k = 2k - 1
    worst = max(worst, (3 - C.bo + 4) - 2 + 3 + C.alpha[0] + arb(6) / T + delta - k)
    monotone_ok = bool(worst < 0)
    print("monotonicity check: max over terms of beta + i/T + delta - k = %s -> %s" % (worst.str(6), "OK (decreasing)" if monotone_ok else "FAILED"))
    if not monotone_ok:
        raise SystemExit("tail majorant NOT valid for tau >= T: the monotonicity precondition fails; no bound is emitted")
    bound = total * wT / m_low
    res = dict(T_out=float(T.mid()), r_T=float(eT.mid()), delta=float(delta.mid()), tail_bound_weighted=bound.str(6), tail_bound_unweighted=(total / m_low).str(6), monotone_ok=monotone_ok,
               crude_total_diagnostic_only=crude_total.str(6), leading_sumC=sumC.str(6), rest_majorant=rest.str(6), crude_bound_weighted_diagnostic_only=(crude_total * wT / m_low).str(6),
               lin=linabs.str(6), PR_twice=(2 * Pabs * Rtabs).str(6), QR_twice=(2 * Qabs * Rhatabs).str(6), time=time.time() - t0_,
               note="termwise majorant at tau = T of W(1+u)^delta/m; valid for all tau >= T since every term decays relative to m (1+u)^-delta (delta < 1-k)")
    print(json.dumps(res, indent=1)); json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], a[3], a[4], float(a[5]), a[6], int(a[7]) if len(a) > 7 else 256)
