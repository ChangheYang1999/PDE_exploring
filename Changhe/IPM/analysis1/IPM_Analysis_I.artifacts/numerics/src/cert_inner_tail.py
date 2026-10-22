"""Rigorous bound of W(tau')/m on the inner tail tau' <= -T_in (r <= rmin e^{-T_in}) by termwise majorants of the
exponential-polynomial representation at tau' = -T_in, with the exponent-3 coefficient (the x^2 y coefficient of eps,
proportional to 3 c_l - 1 - c) evaluated exactly in Arb (it is a ball of radius ~1e-24 around 0 by the exactified normalization).
Inner region: a_m(tau') = delta_m0 + sum_j D_mj e^{2j tau'} + e^{bi tau'} sum_i Ei_mi tau'^i (tau' <= 0),
  f_n(e^t) = e^{2 tmin} sum e^{(alpha+2) tau'} F_n(tau'),  A_n(tau') = e^{2 tmin} sum e^{(2+alpha') tau'} S^A(tau')    (int from -oo; lam > 0)
  B_n(tau') = e^{2n tau'} C^B_n - e^{2 tmin} sum e^{(2+alpha') tau'} S^B(tau'),   C^B_n = B_n(tmin) + e^{2 tmin} sum S^B(0)
  R_j = e^{3 tmin} sum e^{(3+alpha) tau'} Rc_j(tau'), dR_j/dt likewise.
For tau' <= -T every term of eps_N has exponent >= 3 (relative to m ~ e^{3 tau'} L^-3 (1+u^2)^{(k-3)/2}: exponent >= 0 after division),
so the termwise majorant at -T bounds the tail (terms with exponent exactly 3 are evaluated exactly, see above; polynomial factors
|tau'|^i e^{(gamma-3) tau'} are increasing on tau' <= -T iff i/T <= gamma - 3 (checked in the code for the correction terms, whose
exponents are >= bi + 2 - 3 with degree <= 6; all other terms have degree 0).
Usage: python3 cert_inner_tail.py trial.npz data/cert_green.npz data/cert_coeffs.json data/cert_inner_green.npz out.json [PREC]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx
from math import factorial
from cert_green import Cert, prim_S, load_ball
from modal_fit import OUTER_JL, NIN, NCOR, NOUT


def prim_coeffs(lam, cf):
    """polynomial coefficients of S with int e^{lam s} p(s) ds = e^{lam tau} S(tau) (lam != 0)."""
    S = [arb(0)] * len(cf)
    for j, c in enumerate(cf):
        for l in range(j + 1):
            S[j - l] += c * (-1) ** l * (arb(factorial(j)) / factorial(j - l)) / lam ** (l + 1)
    return S


def main(trial, green, coeffs, inner, out, prec=256):
    t0_ = time.time()
    C = Cert(trial, prec, 0.0)
    cj = json.load(open(coeffs))
    C.Ei = [[load_ball(x) for x in row] for row in cj["Ei"]]; C.Eo = [[load_ball(x) for x in row] for row in cj["Eo"]]; C.A[0][0] = load_ball(cj["A00"])
    g = np.load(green); gi = np.load(inner)
    T = -arb(float(gi["tau"][0]), float(gi["tau_rad"][0]))          # T_in > 0, tail is tau' <= -T
    B_tmin = [arb(float(m), float(r)) for m, r in zip(g["B_mid"][0], g["B_rad"][0])]
    Nf = C.Nf; M = C.M; k = C.k
    inner_terms = C.inner_terms()
    f_in = C.f_terms(inner_terms, (2 * C.tmin).exp())
    e2 = (2 * C.tmin).exp(); e3 = (3 * C.tmin).exp(); eT = (C.tmin - T).exp(); u = eT / C.L
    m_low = u ** 3 * (1 + u * u) ** ((k - 3) / 2)                 # m at r_T (m increasing: inf over the tail is at r -> 0, so divide termwise: each term/m ~ e^{(gamma-3) tau'} ...)
    # We bound each exponential term e^{gamma tau'} |coef| by its value at -T divided by m_low? No: e^{gamma tau'}/m(tau') ~ e^{(gamma-3) tau'}(1+u^2)^{-(k-3)/2} L^3
    # is increasing for gamma >= 3 (tau' <= 0), so the sup over the tail is at -T: bound = (sum of |terms| at -T) / m(-T) with m(-T) >= m_low.
    tau = -T
    # --- psi_n majorants at -T, with the exponent-2 part of psi_1 (which gives the exponent-3 part of eps with lin) tracked exactly
    Pabs = arb(0); Qabs = arb(0)
    P_exact3 = arb(0); Q_exact3 = arb(0)          # exact exponent-0 coefficient of P~_1 = -psi_1 e^{-2t} and of Q~_1 = psi_1' e^{-t}/2
    for n in range(1, Nf + 1):
        absA = arb(0); absB = arb(0); transientB = B_tmin[n - 1]
        exact2_psi = arb(0)        # exact coefficient of e^{2 tau'} e^{2 tmin} in psi_n (only n = 1 matters for exponent 3)
        for alpha, fc in f_in:
            lam = 2 * n + 2 + alpha; mu = 2 - 2 * n + alpha
            cf = [fc[q][n - 1] for q in range(len(fc))]
            if all(c == 0 for c in cf): continue
            SA = prim_coeffs(lam, cf)                     # A-part: e^{2 tmin} e^{(2+alpha) tau'} S_A(tau')  (lam > 0, from -oo)
            absA += e2 * ((2 + alpha) * tau).exp() * sum((abs(c) * abs(tau) ** j for j, c in enumerate(SA)), arb(0))
            if abs(mu) * T >= arb(1) / 2:
                SB = prim_coeffs(mu, cf)                  # B-part: int_{tau'}^0 e^{mu s} p = e^{0} S_B(0) - e^{mu tau'} S_B(tau')
                transientB += e2 * SB[0]                      # S_B(0) = SB[0]
                # B(tau') = e^{2n tau'} [B(tmin) + e^{2 tmin} sum S_B(0)] - e^{2 tmin} sum e^{(2+alpha) tau'} S_B(tau')   [e^{2n tau'} e^{mu tau'} = e^{(2+alpha) tau'}]
                absB += e2 * ((2 + alpha) * tau).exp() * sum((abs(c) * abs(tau) ** j for j, c in enumerate(SB)), arb(0))
            else:
                # |mu| T small (incl. mu = 0 exactly): int_{tau'}^0 e^{mu s} p(s) ds = [P(0) - P(tau')] + int (e^{mu s} - 1) p, P the polynomial
                # primitive; |e^{mu s} - 1| <= |mu| |s| e^{|mu| |s|}. Majorant of the B-part at tau' = -T: e^{2 tmin} e^{2n tau'} [ |P|(T) + |mu| T e^{|mu| T} sum |c_j| T^{j+1}/(j+1) ].
                Pp = [arb(0)] + [cf[j] / (j + 1) for j in range(len(cf))]
                corr = abs(mu) * T * (abs(mu) * T).exp() * sum((abs(cf[j]) * T ** (j + 1) / (j + 1) for j in range(len(cf))), arb(0))
                absB += e2 * ((2 * n) * tau).exp() * (sum((abs(c) * abs(tau) ** j for j, c in enumerate(Pp)), arb(0)) + corr)
        absB += abs(transientB) * (2 * n * tau).exp()
        psi_abs = (absA + absB) / (4 * n); dpsi_abs = (absA + absB) / (2 * eT)
        Pabs += n * psi_abs / (eT * eT); Qabs += dpsi_abs / (2 * eT)
    # --- R, Rt majorants and the lin term; exponent-3 part (alpha = 0 term: the constant a_0 = 1) handled exactly together with
    # the exponent-3 part of the convolution: eps_N^{(3)} = (3 c_l - 1) R^{(0)}_N - [c-part], which equals (3 c_l - 1 - c) * x^2y coefficient.
    # Rather than isolating it, we note: eps's exponent-3 coefficient is exactly (3 c_l - 1 - c) * (1/4 for N=0,1) (the x^2 y mode), and
    # c = c_green is a ball around 3 c_l - 1 of radius ~1e-24. So the exponent-3 contribution to W/m is bounded by |3 c_l - 1 - c| * (1/2) * L^3 * (1+u^2)^{(3-k)/2}.
    cdef = abs(3 * C.c_l - 1 - arb(float(g["c_mid"]), float(g["c_rad"])))
    # monotonicity precondition for the polynomial (degree <= 6) correction terms: i/T <= gamma - 3 with gamma >= bi - 1 (the smallest
    # exponent of any correction product: bi + 2 - 2n ... conservatively bi - 1 + ... we use the weakest: gamma_min = bi + 2 - 3 for lin terms)
    # Degree-sensitive monotonicity (referee round 2): a majorant monomial |tau'|^i e^{beta tau'} divided by r^5 (or by m) is increasing on
    # tau' <= -T iff beta - 5 - i/T >= 0. Degree-0 terms have beta >= 5 (after the exact cubic cancellation). Positive-degree terms come
    # from the correction e^{bi tau'} tau'^i (i <= 6) and, in the tiny-|mu| branch, from the error group (exponent 2n - |mu| >= bi - 1 + ...,
    # degree <= 8). Sufficient: 8/T <= bi + 2 - 5 - 2*0 ... we require the conservative 8/T <= bi - 5.
    if not (arb(8) / T <= C.bi - 5):
        raise SystemExit("inner tail majorant: degree condition 8/T <= bi - 5 fails; no bound emitted")
    Rabs = arb(0); Rtabs = arb(0); Rhatabs = arb(0); linabs = arb(0)
    for alpha, c in inner_terms:
        deg = len(c) - 1
        Rc = [C.R_from_a(c[q]) for q in range(deg + 1)]
        dRc = [[(3 + alpha) * Rc[q][j] + (Rc[q + 1][j] * (q + 1) if q + 1 <= deg else arb(0)) for j in range(M + 1)] for q in range(deg + 1)]
        ea = e3 * ((3 + alpha) * tau).exp()
        for j in range(M + 1):
            R_T = sum((abs(Rc[q][j]) * abs(tau) ** q for q in range(deg + 1)), arb(0)) * ea
            Rt_T = sum((abs(dRc[q][j]) * abs(tau) ** q for q in range(deg + 1)), arb(0)) * ea
            Rabs += R_T; Rtabs += Rt_T; Rhatabs += (2 * j + 1) * R_T
            if alpha != 0:        # exponent > 3 terms of lin; the alpha = 0 (constant) term is the exponent-3 part handled via cdef
                linabs += sum((abs(C.c_l * dRc[q][j] - Rc[q][j]) * abs(tau) ** q for q in range(deg + 1)), arb(0)) * ea
    # convolution majorant: this includes the exponent-3 cross terms of n = 1 with the constant part of R (which cancel against lin's
    # exponent-3 part); we keep them in the majorant (over-estimate), and add the exact cancellation defect cdef separately. The
    # majorant is therefore valid but not tight at exponent 3: to recover tightness, the exponent-3 part of the convolution is removed:
    # the psi_1 exponent-2 coefficient is exactly e^{2 tmin} c/2 (c = c_green), giving P~_1^{(0)} = -c/2 and Q~_1^{(0)} = c/2 ... these
    # multiply R^{(0)}_j = e^{3t}/4 (j = 0, 1) and R^_j^{(0)} = (2j+1) e^{3t}/4. We subtract those exact products from the majorant.
    c_arb = arb(float(g["c_mid"]), float(g["c_rad"]))
    e3T = e3 * (3 * tau).exp()
    P1_0 = c_arb / 2 / (eT * eT) * (eT * eT)       # |P~_1^{(0)} Rt^{(0)}| summed: P~_1^{(0)} = -(1/2) 2 psi_1 e^{-2t} -> -c/2 ; Rt^{(0)}_j = 3 e^{3t}/4 (j=0,1)
    # exponent-3 cross terms (n = 1 with the constant part a_0 = 1), each placed in two frequencies by the sine products:
    # P-part: |P~_1^{(0)}| |Rt_j^{(0)}| = (|c|/2)(3 e^{3T}/4) for j = 0, 1, two placements each -> 3|c| e^{3T}/2;
    # Q-part: |Q~_1^{(0)}| (2j+1) |R_j^{(0)}| = (|c|/2)(2j+1) e^{3T}/4 for j = 0, 1, two placements each -> |c| e^{3T}.
    conv3 = abs(c_arb) * e3T * (arb(3) / 2 + 1)
    total_majorant = linabs + 2 * (Pabs * Rtabs + Qabs * Rhatabs)      # every product term feeds two frequencies of the Wiener sum
    total = total_majorant - conv3 + cdef * e3T / 2
    if total < 0: total = total_majorant
    bound = total / m_low
    # R4: W / r^5 for r <= r_T. The cubic (x^2 y) coefficient of eps~ is (3 c_l - 1 - c)/4 for N = 0, 1 and is EXACTLY zero by the
    # definition of the trial (A_00 solves c = 3/k - 1); the Arb ball cdef only reflects the finite precision. The remaining terms have
    # exponents >= 5 in tau' (>= 0 after division by r^5), so their majorant at -T bounds W/r^5 on the whole tail.
    rest = linabs + 2 * (Pabs * Rtabs + Qabs * Rhatabs) - conv3
    if rest < 0: rest = total_majorant
    bound_r5 = rest / eT ** 5
    res = dict(T_in=float(T.mid()), r_T=float(eT.mid()), bound_W_over_m=bound.str(6), majorant_total=total_majorant.str(6), conv3_removed=conv3.str(6),
               normalization_defect=cdef.str(6), bound_W_over_r5=bound_r5.str(6), time=time.time() - t0_,
               note="valid for all r <= r_T: every term has exponent >= 3 in tau' (>= 0 after division by m), hence maximal at -T; exponent-3 part replaced by its exact value proportional to |3 c_l - 1 - c|")
    print(json.dumps(res, indent=1)); json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], a[3], a[4], a[5], int(a[6]) if len(a) > 6 else 256)
