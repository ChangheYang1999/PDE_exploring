"""Rigorous tail bounds for the trial velocity quantities (N1', complement of src/cert_flow.py): for r >= R_T = R0 e^{T_out} and for
r <= r_T = rmin e^{-T_in}, enclosures of s = X.V/r^2, V_2/y, V_1/x and an upper bound of T_0, from the exponential-polynomial
representations of the stream modes (Arb, same construction as cert_tail.py / cert_inner_tail.py).
Outer: |s - c_l| <= DEV_s := sum_n 2n |psi_n|^(T)/R_T^2, |V_2/y - c_l|, |V_1/x - c_l| <= DEV_s + DEV_V, DEV_V := sum_n 2n |psi_r,n|^(T)/R_T,
where |.|^(T) are the termwise majorants at tau = T (every term decreasing for tau >= T: power-law exponents alpha_q + 2 <= k - 1 < 0,
correction terms e^{-bo tau} tau^i with i/T <= bo, transients e^{-2n(tau-T)} <= 1). T_0 <= -(1+c_l) + mu(R_T) c_l + S DEV + (S - mu(R_T)) DEV_s.
Inner: the leading (a_0 = 1) part gives exactly 2 psi_1 e^{-2t} -> c and psi_r,1 e^{-t} -> c (c = psi_xy(0) ball), hence
s = c_l - c cos 2theta + rest, V_2/y = 4c_l - 1 + rest, V_1/x = 1 - 2c_l + rest, |rest| <= DEV_in (termwise majorants at tau' = -T_in of all
other terms, which decrease as r -> 0: exponents >= 2 after division by r^2).
Usage: python3 cert_flow_tails.py trial.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz data/cert_inner_green.npz out.json [PREC]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx
from math import factorial
from cert_green import Cert, load_ball
from cert_inner_tail import prim_coeffs
from cert_flow import PAR


def abs_poly_at(coeffs, tau):
    return sum((abs(c) * abs(tau) ** j for j, c in enumerate(coeffs)), arb(0))


def outer_dev(C, g):
    T = arb(float(g["tau"][-1]), float(g["tau_rad"][-1]))
    A_T = [arb(float(m), float(r)) for m, r in zip(g["A_mid"][-1], g["A_rad"][-1])]
    outer_terms = C.outer_terms(); f_out = C.f_terms(outer_terms, (2 * C.t0).exp())
    e2t0 = (2 * C.t0).exp(); eT = (C.t0 + T).exp()
    DEV_s = arb(0); DEV_V = arb(0); mono_ok = True
    for n in range(1, C.Nf + 1):
        absA = arb(0); absB = arb(0); transient = A_T[n - 1]
        for alpha, fc in f_out:
            lam = 2 * n + 2 + alpha; mu = 2 - 2 * n + alpha
            cf = [fc[q][n - 1] for q in range(len(fc))]
            if all(c == 0 for c in cf): continue
            if not (alpha < 0): mono_ok = False                     # normalized exponent of every particular term must be negative
            if not (lam != 0 and mu != 0): mono_ok = False           # primitive nonresonance
            SA = prim_coeffs(lam, cf); SB = prim_coeffs(mu, cf)
            transient -= e2t0 * ((2 + alpha) * T).exp() * sum((SA[j] * T ** j for j in range(len(SA))), arb(0))
            absA += e2t0 * ((2 + alpha) * T).exp() * abs_poly_at(SA, T)
            absB += e2t0 * ((2 + alpha) * T).exp() * abs_poly_at(SB, T)
            # monotonicity of e^{(2+alpha) tau} tau^i / r^2 ~ e^{alpha tau} tau^i for tau >= T: need i/T <= -alpha (alpha < 0)
            deg = len(cf) - 1
            if deg >= 1 and not (arb(deg) / T <= -alpha): mono_ok = False
        absA += abs(transient)
        psi_abs = (absA + absB) / (4 * n); dpsi_abs = (absA + absB) / (2 * eT)        # |psi_n|, |psi_r,n| majorants at T
        DEV_s += 2 * n * psi_abs / (eT * eT); DEV_V += 2 * n * dpsi_abs / eT
    return DEV_s, DEV_V, eT, mono_ok


def inner_dev(C, g, gi):
    T = -arb(float(gi["tau"][0]), float(gi["tau_rad"][0]))          # T_in > 0; tail is tau' <= -T
    B_tmin = [arb(float(m), float(r)) for m, r in zip(g["B_mid"][0], g["B_rad"][0])]
    inner_terms = C.inner_terms(); f_in = C.f_terms(inner_terms, (2 * C.tmin).exp())
    e2 = (2 * C.tmin).exp(); eT = (C.tmin - T).exp(); tau = -T
    DEV = arb(0); c_lead = None; mono_fail = []
    for n in range(1, C.Nf + 1):
        absA = arb(0); absB = arb(0); transientB = B_tmin[n - 1]
        for alpha, fc in f_in:
            lam = 2 * n + 2 + alpha; mu = 2 - 2 * n + alpha
            cf = [fc[q][n - 1] for q in range(len(fc))]
            if all(c == 0 for c in cf): continue
            SA = prim_coeffs(lam, cf)
            # A-part: e^{2 tmin} e^{(2+beta) tau'} S_A(tau'), beta = alpha here (f-term exponent, >= 2): after division by r^2 the exponent is
            # beta >= 2 > 0, decreasing as tau' -> -inf provided deg/T <= beta (checked). The exact exponent-2 coefficient of psi_1 comes
            # entirely from the B transient C_B,1 = B_1(tmin) + e^{2tmin} sum S_B(0) (referee flow1): c = e^{-2 tmin} C_B,1 / 2.
            degA = len(SA) - 1
            if degA >= 1 and not (arb(degA) / T <= alpha): mono_fail.append(("A", n, float(alpha.mid()), degA))
            absA += e2 * ((2 + alpha) * tau).exp() * abs_poly_at(SA, tau)
            degB = len(cf) - 1
            if abs(mu) * T >= arb(1) / 2:
                SB = prim_coeffs(mu, cf); transientB += e2 * SB[0]
                absB += e2 * ((2 + alpha) * tau).exp() * abs_poly_at(SB, tau)
                if degB >= 1 and not (arb(degB) / T <= alpha): mono_fail.append(("B", n, float(alpha.mid()), degB))
            else:
                if n == 1: raise SystemExit("near-resonant branch reached for n = 1: the homogeneous coefficient would not be extracted")
                Pp = [arb(0)] + [cf[j] / (j + 1) for j in range(len(cf))]
                corr = abs(mu) * T * (abs(mu) * T).exp() * sum((abs(cf[j]) * T ** (j + 1) / (j + 1) for j in range(len(cf))), arb(0))
                absB += e2 * ((2 * n) * tau).exp() * (abs_poly_at(Pp, tau) + corr)
                # normalized majorants x^{d+1} e^{-(2n-2) x} and |mu| x^{d+2} e^{-(2n-2-|mu|) x} must decrease for x >= T
                if not (arb(degB + 1) / T <= 2 * n - 2): mono_fail.append(("Bres1", n, float(alpha.mid()), degB))
                if not (arb(degB + 2) / T <= 2 * n - 2 - abs(mu)): mono_fail.append(("Bres2", n, float(alpha.mid()), degB))
        if n == 1:
            c_lead = transientB * (-2 * C.tmin).exp() / 2          # exact exponent-2 coefficient: 2 psi_1 e^{-2t} -> c
            absB_rest = absB
        else:
            absB_rest = absB + abs(transientB) * (2 * n * tau).exp()
        rest = (absA + absB_rest)
        DEV += 2 * n * rest / (4 * n) / (eT * eT) + 2 * n * rest / (2 * eT) / eT      # 2n|psi_rest|/r^2 + 2n |psi_r,rest|/r at r_T
    return DEV, c_lead, eT, mono_fail


def main(trial, green, coeffs, outer, inner, out, prec=256):
    ctx.prec = prec; t0_ = time.time()
    C = Cert(trial, prec, 0.0)
    cj = json.load(open(coeffs))
    C.Ei = [[load_ball(x) for x in row] for row in cj["Ei"]]; C.Eo = [[load_ball(x) for x in row] for row in cj["Eo"]]; C.A[0][0] = load_ball(cj["A00"])
    g = np.load(green); go = np.load(outer); gi = np.load(inner)
    A_ = arb(PAR["a"][0]) / PAR["a"][1]; B_ = arb(PAR["b"][0]) / PAR["b"][1]; GP = arb(PAR["gp"][0]) / PAR["gp"][1]; Rm = arb(PAR["Rm"]); p = PAR["p"]; S = A_ + B_
    cl = C.c_l                                                       # c_l := 1/k (the trial's exponent), as in the whole certificate
    # outer
    DEV_s, DEV_V, RT, mono = outer_dev(C, go)
    muRT = GP + (S - GP) / (1 + (RT / Rm) ** p)
    T0_out = -(1 + cl) + muRT * cl + S * (DEV_s + DEV_V) + (S - muRT) * DEV_s
    def upf(x): return float(np.nextafter(float(x.upper()), np.inf))
    def lof(x): return float(np.nextafter(float(x.lower()), -np.inf))
    if not mono:
        raise SystemExit("outer tail: a hypothesis (negative normalized exponents, nonresonance, correction monotonicity) failed; no bound emitted")
    res = dict(outer=dict(R_T_lo=lof(RT), R_T_hi=upf(RT), DEV_s=upf(DEV_s), DEV_V=upf(DEV_V), monotone_ok=bool(mono),
               s_min=lof(cl - DEV_s), v2y_min=lof(cl - DEV_s - DEV_V), v1x_min=lof(cl - DEV_s - DEV_V), T0_max=upf(T0_out)))
    print("outer tail r >= %.6e (valid for all r >= R_T_hi): |s - c_l| <= %.3e, |V2/y - c_l|, |V1/x - c_l| <= %.3e; s >= %.6f, V2/y >= %.6f, T0 <= %.6f (limit -(1+c_l) + gamma' c_l = %.6f)" % (
        res["outer"]["R_T_hi"], res["outer"]["DEV_s"], res["outer"]["DEV_s"] + res["outer"]["DEV_V"], res["outer"]["s_min"], res["outer"]["v2y_min"], res["outer"]["T0_max"], float((-(1 + cl) + GP * cl).mid())), flush=True)
    # inner
    DEV, c_lead, rT, mono_fail = inner_dev(C, g, gi)
    if mono_fail:
        raise SystemExit("inner tail: monotonicity conditions failed: %s" % mono_fail[:5])
    c_green = arb(float(g["c_mid"]), float(g["c_rad"]))
    v2y_lo = lof(cl + c_lead - DEV); v1x_hi = upf(cl - c_lead + DEV)
    mu_rT = GP + (S - GP) / (1 + (rT / Rm) ** p)
    # T0 <= -(1+c_l) + a (c_l - c + DEV) + b (c_l + c + DEV) + max(0, (mu(r_T) - S) (c_l - |c| - DEV))   [(mu - S) <= 0, s >= c_l - |c| - DEV]
    Ls = cl - abs(c_lead) - DEV
    extra = (mu_rT - S) * Ls
    extra_up = extra.upper() if extra.upper() > 0 else arb(0)
    T0_in = -(1 + cl) + A_ * (cl - c_lead + DEV) + B_ * (cl + c_lead + DEV) + extra_up
    res["inner"] = dict(r_T_lo=lof(rT), r_T_hi=upf(rT), DEV=upf(DEV), c_lead=[lof(c_lead), upf(c_lead)], c_green=[lof(c_green), upf(c_green)],
                        v2y_min=v2y_lo, v1x_max=v1x_hi, T0_max=upf(T0_in), note="valid for all r <= r_T_lo; c_lead = e^{-2 tmin} C_B,1 / 2 from the B transient (a_0 = 1 term)")
    print("inner tail r <= %.6e (valid for r <= r_T_lo): rest <= %.3e; c_lead = [%.12f, %.12f] (c_green [%.12f, %.12f]); V2/y >= %.6f (4c_l - 1 = %.6f), V1/x <= %.6f (1 - 2c_l = %.6f), T0 <= %.6f" % (
        res["inner"]["r_T_lo"], res["inner"]["DEV"], res["inner"]["c_lead"][0], res["inner"]["c_lead"][1], res["inner"]["c_green"][0], res["inner"]["c_green"][1], v2y_lo, float((4 * cl - 1).mid()), v1x_hi, float((1 - 2 * cl).mid()), res["inner"]["T0_max"]), flush=True)
    res["time"] = time.time() - t0_; res["constants"] = dict(a="129/20", b="307/100", gamma_prime="1129/1000", R_m=PAR["Rm"], p=PAR["p"], c_l="1/k of the trial")
    json.dump(res, open(out, "w"), indent=1); print("saved", out)


if __name__ == "__main__":
    a = sys.argv; main(a[1], a[2], a[3], a[4], a[5], a[6], int(a[7]) if len(a) > 7 else 256)
