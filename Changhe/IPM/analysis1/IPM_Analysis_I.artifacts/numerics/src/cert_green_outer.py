"""Arb boundary values on the OUTER region (r > R0) and INNER region (r < rmin) sub-cells, for the Taylor-model certificate.
Outer: tau = t - t0 in [0, T_out], sub-cells of length hsub; a_m(tau) = sum_q A_mq e^{alpha_q tau} + e^{-bo tau} sum_i Eo_mi tau^i
(exactified coefficients from data/cert_coeffs.json).  A_n(tau_a) = e^{-2n tau_a} A_n(t0) + e^{2 t0} int_0^{tau_a} ... ,
B_n(tau_a) = e^{2 t0} sum_terms int_{tau_a}^oo ...  (closed forms, cert_green.integ_scaled).
Also exports, per outer sub-cell, the exponential-polynomial terms of a_m re-centred at the sub-cell start (exponent, coefficients).
Inner: tau' = t - tmin in [-T_in, 0]; a_m = delta_m0 + sum_j D_mj e^{2j tau'} + e^{bi tau'} sum_i Ei_mi tau'^i;
A_n(tau'_a) = e^{2 tmin} sum_terms int_{-oo}^{tau'_a} ..., B_n(tau'_a) = e^{-2n (0 - tau'_a)} B_n(tmin) + e^{2 tmin} sum int_{tau'_a}^0 ...
Usage: python3 cert_green_outer.py trial.npz data/cert_green.npz data/cert_coeffs.json hsub T_out T_in out_prefix [PREC]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx
from math import factorial
from cert_green import Cert, integ_scaled, load_ball
from modal_fit import OUTER_JL, NIN, NCOR, NOUT


def export(rows):
    m = np.array([[float(x.mid()) for x in row] for row in rows]); r = np.array([[float(x.rad()) for x in row] for row in rows])
    r = np.nextafter(np.nextafter(np.nextafter(r, np.inf) + np.nextafter(2.0 ** -53 * np.abs(m), np.inf), np.inf) + 2.0 ** -1074, np.inf)
    return m, r


def recentre(terms, d):
    """exponential-polynomial terms [(alpha, coeffs[q][m])] in tau -> in sigma = tau - d: e^{alpha (d + sigma)} p(d + sigma)."""
    out = []
    for alpha, c in terms:
        deg = len(c) - 1; ea = (alpha * d).exp()
        newc = []
        for q in range(deg + 1):
            row = []
            for m in range(len(c[0])):
                v = arb(0)
                for pp in range(q, deg + 1):
                    v += c[pp][m] * (arb(factorial(pp)) / (factorial(q) * factorial(pp - q))) * d ** (pp - q)
                row.append(v * ea)
            newc.append(row)
        out.append((alpha, newc))
    return out


def main(trial, green, coeffs, hsub, T_out, T_in, out_prefix, prec=256):
    t0_ = time.time()
    C = Cert(trial, prec, hsub)
    cj = json.load(open(coeffs))
    # install the exactified coefficients
    C.Ei = [[load_ball(x) for x in row] for row in cj["Ei"]]; C.Eo = [[load_ball(x) for x in row] for row in cj["Eo"]]; C.A[0][0] = load_ball(cj["A00"])
    g = np.load(green)
    Nf = C.Nf
    A_t0 = [arb(float(m), float(r)) for m, r in zip(g["A_mid"][-1], g["A_rad"][-1])]
    B_tmin = [arb(float(m), float(r)) for m, r in zip(g["B_mid"][0], g["B_rad"][0])]
    n_out = int(np.ceil(T_out / hsub)); n_in = int(np.ceil(T_in / hsub))
    print("outer sub-cells: %d, inner sub-cells: %d" % (n_out, n_in), flush=True)
    # ---- outer
    outer_terms = C.outer_terms()                                     # in tau = t - t0
    f_out = C.f_terms(outer_terms, (2 * C.t0).exp())
    taus = [arb(T_out) * i / n_out for i in range(n_out + 1)]
    Ao = []; Bo = []
    for i, ta in enumerate(taus):
        rowA = []; rowB = []
        for n in range(1, Nf + 1):
            accA = arb(0); accB = arb(0)
            for alpha, fc in f_out:
                lam = 2 * n + 2 + alpha; mu = 2 - 2 * n + alpha
                coeffs_n = [fc[q][n - 1] for q in range(len(fc))]
                if ta != 0: accA += integ_scaled(lam, coeffs_n, arb(0), ta, -2 * n * ta)
                accB += integ_scaled(mu, coeffs_n, ta, np.inf, 2 * n * ta)
            rowA.append((-2 * n * ta).exp() * A_t0[n - 1] + (2 * C.t0).exp() * accA)
            rowB.append((2 * C.t0).exp() * accB)
        Ao.append(rowA); Bo.append(rowB)
        if i % 500 == 0: print("  outer %d/%d (%.0fs)" % (i, n_out, time.time() - t0_), flush=True)
    # ---- inner (tau' from -T_in to 0, cells ordered increasing)
    inner_terms = C.inner_terms()
    f_in = C.f_terms(inner_terms, (2 * C.tmin).exp())
    tausi = [-arb(T_in) + arb(T_in) * i / n_in for i in range(n_in + 1)]
    Ai = []; Bi = []
    for i, ta in enumerate(tausi):
        rowA = []; rowB = []
        for n in range(1, Nf + 1):
            accA = arb(0); accB = arb(0)
            for alpha, fc in f_in:
                lam = 2 * n + 2 + alpha; mu = 2 - 2 * n + alpha
                coeffs_n = [fc[q][n - 1] for q in range(len(fc))]
                accA += integ_scaled(lam, coeffs_n, -np.inf, ta, -2 * n * ta)
                if ta != 0: accB += integ_scaled(mu, coeffs_n, ta, arb(0), 2 * n * ta)
            rowA.append((2 * C.tmin).exp() * accA)
            rowB.append((2 * n * ta).exp() * B_tmin[n - 1] + (2 * C.tmin).exp() * accB)
        Ai.append(rowA); Bi.append(rowB)
        if i % 500 == 0: print("  inner %d/%d (%.0fs)" % (i, n_in, time.time() - t0_), flush=True)
    # export: boundary values and the BASE exponential-polynomial terms (re-centring is done in cert_resid_regions)
    def exp_base(terms):
        nterms = len(terms); degmax = max(len(c) for a, c in terms) - 1; M = len(terms[0][1][0])
        # exponents: exact Arb values (k-3) - j(1-k) - 2l etc.; export the nearest double and an upper bound of |exact - double|
        alphas = np.array([float(a.mid()) for a, c in terms])
        alphas_rad = np.array([float((a - arb(float(a.mid()))).rad() + abs((a - arb(float(a.mid()))).mid())) * (1 + 1e-12) + 1e-300 for a, c in terms])
        cm = np.zeros((nterms, degmax + 1, M)); cr = np.zeros_like(cm)
        for it, (a, c) in enumerate(terms):
            m_, r_ = export(c); cm[it, :len(c), :] = m_; cr[it, :len(c), :] = r_
        return alphas, alphas_rad, cm, cr
    aO, aOr, cOm, cOr = exp_base(outer_terms); aI, aIr, cIm, cIr = exp_base(inner_terms)
    AOm, AOr = export(Ao); BOm, BOr = export(Bo); AIm, AIr = export(Ai); BIm, BIr = export(Bi)
    tauO = export([taus]); tauI = export([tausi])
    np.savez_compressed(out_prefix + "_outer_green.npz", tau=tauO[0][0], tau_rad=tauO[1][0], A_mid=AOm, A_rad=AOr, B_mid=BOm, B_rad=BOr,
                        alphas=aO, alphas_rad=aOr, base_mid=cOm, base_rad=cOr, t0=float(C.t0.mid()), t0_rad=float(C.t0.rad()), hsub=hsub)
    np.savez_compressed(out_prefix + "_inner_green.npz", tau=tauI[0][0], tau_rad=tauI[1][0], A_mid=AIm, A_rad=AIr, B_mid=BIm, B_rad=BIr,
                        alphas=aI, alphas_rad=aIr, base_mid=cIm, base_rad=cIr, tmin=float(C.tmin.mid()), tmin_rad=float(C.tmin.rad()), hsub=hsub)
    print("saved %s_outer_green.npz and _inner_green.npz; total %.0fs" % (out_prefix, time.time() - t0_))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], a[3], float(a[4]), float(a[5]), float(a[6]), a[7], int(a[8]) if len(a) > 8 else 256)
