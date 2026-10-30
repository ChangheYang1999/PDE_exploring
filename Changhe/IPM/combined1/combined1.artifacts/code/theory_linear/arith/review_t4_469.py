"""Independent check of c1-t4 T4-469 (research/divergence_free_negative_norm_upper: PROOF.md and its supplement
ERRATA_v01.md, TEAM_NOTE_v246/v247): the divergence-free correction of the angular Hardy upper bound of
H(F) = sup |int F phi| / ||grad phi||_2.

No c1-t4 code is executed; code/check.py is not imported. Read only: PROOF.md, ERRATA_v01.md, data/parameters.json,
data/manifest.json, verification/result.json, verification/positive_pole_scope.json (sha256 asserted).

Parts.
  A  input hashes and the hashes the T4-469 files cite for each other.
  B  symbolic (sympy) identities behind PROOF.md (1)-(11): div A_F = F; the explicit components of
     Z = A_(Delta psi) - grad psi for psi = u(r) sin(n theta), Z = -(v'/r) sin e_r - (v''/(n r)) cos e_theta with
     v(y) = u(e^y); div Z = 0 (polar, generic n and u; Cartesian, n = 1, 2, 3); the theta integrals giving (7) and (8)
     directly from Z (no integration by parts), and the boundary terms by which (6) differs from them; the operator
     D_b of (9) with symbolic b; the changes of variable behind (10) and (11); the beta moment formula.
  C  the two manufactured fixtures of data/parameters.json, by an independent exact r-route (Laurent polynomials in
     r and S = sqrt(1 + r^2), int_0^oo r^m S^(-2 sigma) dr = (1/2) B((m+1)/2, sigma - (m+1)/2) in Fractions, both (6)
     and (7)/(8) forms) and by the t-route of (10)/(11); the combined, one-test and mixed-trial values of
     verification/result.json; a two-exponent trial for the cross terms of (10).
  D  sources that are not manufactured from the test: F = -Delta(r (1+r^2)^-2 sin theta) with the mode-1 fixture
     test (exact H(F)^2, strict inequalities of (3) and (4), (11) against (8), the supplement's energy identity, its
     t = 1 reading and the triangle bound); a two-mode source with a 2x2 same-mode Gram test plus a mode-3 test, (5).
  E  the supplement's positive-pole case: a source mode r w^(5/2) t(1-2t)/(1+3w)^2, b by (11) in t and by (8) in r
     (mpmath, 40 digits, a numerical observation), and the exact closed form of this pole moment (sympy), which
     contains sqrt(3) pi.

Run from artifacts/:  python3 -B -u arith/review_t4_469.py
Takes no arguments. Needs sympy and mpmath. Output: stdout (logs/review_t4_469.log by the README command),
data/review_t4_469_results.json.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as Fr
from math import factorial
from pathlib import Path

import mpmath as mp
import sympy as sp

if len(sys.argv) != 1:
    sys.exit("usage: review_t4_469.py (no arguments)")
T0 = time.time()
HERE_ = Path(__file__).resolve().parents[1]
SRC = HERE_.parent.parent / "c1-t4/research/divergence_free_negative_norm_upper"
SH = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
FAILS, N = [], [0]
OUT = {}


def check(msg, ok):
    N[0] += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


def zero(e):
    return sp.simplify(e) == 0


# ---------------------------------------------------------------- A: inputs
PIN = {"PROOF.md": "efabe956aa103859e42f8240f270217a1738a732d590d0dd1f01be11377c2cbf",
       "ERRATA_v01.md": "45e743dd2ef7ac929a5a4f8b5ec89c8e0dfb0c480e8ae164f909ae8c10840037",
       "data/parameters.json": "0c5abd318d8f6c55b924c12a04021e4204fe351ab0c1181ec2f5bb0a647d03ad",
       "data/manifest.json": "9fabbf16784e6d2e91edc4a12b6cfff7fbe7a393787d57ff71a9fa19cb9f79b4",
       "verification/result.json": "144fd3c25a57d48302e5aa4f94012ae64204752d402c6dfdf6adddc7dafe595c",
       "verification/positive_pole_scope.json": "4fb3ee80cb79cc87a76ba6e1b6600c985ce955b80eacb1a46340df2a345c3e30",
       "code/check.py": "869ddaf2340145223d5ad0030308f5feba571ffc3f6b03268c981b7d5fc9c95c"}
print("A. inputs")
for k, h in PIN.items():
    check("sha256 of %s is %s...%s" % (k, h[:8], h[-8:]), SH(SRC / k) == h)
PAR = json.loads((SRC / "data/parameters.json").read_text())
RES = json.loads((SRC / "verification/result.json").read_text())
POLE = json.loads((SRC / "verification/positive_pole_scope.json").read_text())
MAN = json.loads((SRC / "data/manifest.json").read_text())
ERR = (SRC / "ERRATA_v01.md").read_text()
check("result.json cites PROOF.md, code/check.py and data/manifest.json by their current sha256, %d checks"
      % RES["check_count"], RES["proof_sha256"] == PIN["PROOF.md"] and RES["checker_sha256"] == PIN["code/check.py"]
      and RES["manifest_sha256"] == PIN["data/manifest.json"] and RES["check_count"] == len(RES["checks"]) == 75)
check("positive_pole_scope.json cites PROOF.md and ERRATA_v01.md by their sha256; ERRATA_v01.md cites PROOF.md",
      POLE["proof_sha256"] == PIN["PROOF.md"] and POLE["supplement_sha256"] == PIN["ERRATA_v01.md"]
      and PIN["PROOF.md"] in ERR)
check("manifest rows for PROOF.md and data/parameters.json carry the pinned sha256",
      {m["local"]: m["sha256"] for m in MAN}.get("PROOF.md") == PIN["PROOF.md"]
      and {m["local"]: m["sha256"] for m in MAN}.get("data/parameters.json") == PIN["data/parameters.json"])
OUT["A"] = {"inputs": {"c1-t4/research/divergence_free_negative_norm_upper/" + k: h for k, h in PIN.items()}}

# ---------------------------------------------------------------- B: symbolic identities
print("B. symbolic identities")
r, th, Y = sp.symbols("r theta y", positive=True)
n = sp.symbols("n", positive=True, integer=True)
f, u = sp.Function("f")(r), sp.Function("u")(r)


def pdiv(Zr, Zt):
    """polar divergence of Zr e_r + Zt e_theta"""
    return sp.diff(r * Zr, r) / r + sp.diff(Zt, th) / r


AF = (0, -r * f * sp.cos(n * th) / n)
check("(1) div A_F = f_n sin(n theta) for A_F = -e_theta r f_n cos(n theta)/n (generic n, f_n)",
      zero(pdiv(*AF) - f * sp.sin(n * th)))
lap = sp.diff(u, r, 2) + sp.diff(u, r) / r - n ** 2 * u / r ** 2          # (Delta psi)_n for psi = u sin(n theta)
gpsi = (sp.diff(u, r) * sp.sin(n * th), n * u * sp.cos(n * th) / r)
check("polar Laplacian of psi = u sin(n theta): div grad psi = (u'' + u'/r - n^2 u/r^2) sin(n theta)",
      zero(pdiv(*gpsi) - lap * sp.sin(n * th)))
AL = (0, -r * lap * sp.cos(n * th) / n)
Z = (AL[0] - gpsi[0], AL[1] - gpsi[1])
v1 = r * sp.diff(u, r)                                                     # v'(y) at y = log r
v2 = r * sp.diff(v1, r)                                                    # v''(y) = r^2 u'' + r u'
check("Z = A_(Delta psi) - grad psi = -(v'/r) sin(n theta) e_r - (v''/(n r)) cos(n theta) e_theta, generic n and u",
      zero(Z[0] + v1 / r * sp.sin(n * th)) and zero(Z[1] + v2 / (n * r) * sp.cos(n * th)))
check("div Z = 0 (polar, generic n and u)", zero(pdiv(*Z)))
check("div A_(Delta psi) = Delta psi (polar, generic n and u)", zero(pdiv(*AL) - lap * sp.sin(n * th)))

# Cartesian check of the polar formulas for concrete n and a concrete radial profile
x_, y_ = sp.symbols("x y", real=True)
rho = sp.sqrt(x_ ** 2 + y_ ** 2)
okc = True
for nn in (1, 2, 3):
    uu = lambda s: s ** 3 / (1 + s ** 2) ** sp.Rational(5, 2) if nn > 1 else s / (1 + s ** 2) ** sp.Rational(3, 2)
    sn, cn = sp.im(sp.expand((x_ + sp.I * y_) ** nn)) / rho ** nn, sp.re(sp.expand((x_ + sp.I * y_) ** nn)) / rho ** nn
    psi = uu(rho) * sn
    s_ = sp.symbols("s", positive=True)
    us = uu(s_)
    vp = s_ * sp.diff(us, s_)
    vpp = s_ * sp.diff(vp, s_)
    Zr_, Zt_ = (-vp / s_).subs(s_, rho) * sn, (-vpp / (nn * s_)).subs(s_, rho) * cn
    Zx, Zy = Zr_ * x_ / rho - Zt_ * y_ / rho, Zr_ * y_ / rho + Zt_ * x_ / rho
    lapc = sp.diff(psi, x_, 2) + sp.diff(psi, y_, 2)
    lapp = (sp.diff(us, s_, 2) + sp.diff(us, s_) / s_ - nn ** 2 * us / s_ ** 2).subs(s_, rho) * sn
    # A_(Delta psi) in Cartesian components, then Z = A - grad psi componentwise
    At = (-s_ * (sp.diff(us, s_, 2) + sp.diff(us, s_) / s_ - nn ** 2 * us / s_ ** 2) / nn).subs(s_, rho) * cn
    Zx2, Zy2 = -At * y_ / rho - sp.diff(psi, x_), At * x_ / rho - sp.diff(psi, y_)
    pts = [(sp.Rational(3, 7), sp.Rational(-5, 11)), (sp.Rational(2), sp.Rational(1, 3)), (sp.Rational(-1, 5), 3)]
    for p_ in pts:
        sub = {x_: p_[0], y_: p_[1]}
        e1 = sp.N((lapc - lapp).subs(sub), 60)
        e2 = sp.N((sp.diff(Zx, x_) + sp.diff(Zy, y_)).subs(sub), 60)
        e3 = sp.N(((Zx - Zx2) ** 2 + (Zy - Zy2) ** 2).subs(sub), 60)
        okc = okc and abs(e1) < 1e-50 and abs(e2) < 1e-50 and abs(e3) < 1e-50
check("Cartesian cross-check (n = 1, 2, 3, concrete profiles, 3 rational points each, 60 digits, residuals < 1e-50):"
      " Laplacian, Z components and div Z = 0", okc)

okt = True
for nn in range(1, 7):
    for mm in range(1, 7):
        ss = sp.integrate(sp.sin(nn * th) * sp.sin(mm * th), (th, 0, 2 * sp.pi))
        cc = sp.integrate(sp.cos(nn * th) * sp.cos(mm * th), (th, 0, 2 * sp.pi))
        sc = sp.integrate(sp.sin(nn * th) * sp.cos(mm * th), (th, 0, 2 * sp.pi))
        okt = okt and ss == cc == (sp.pi if nn == mm else 0) and sc == 0
check("theta orthogonality for n, m = 1..6: int sin sin = int cos cos = pi delta_nm, int sin cos = 0", okt)
# theta integrals per mode (int sin^2 = int cos^2 = pi), times r from dx = r dr dtheta, against dy = dr/r
Zsq_r = sp.pi * (v1 ** 2 / r ** 2 + v2 ** 2 / (n ** 2 * r ** 2)) * r
check("(7) directly from Z: int |Z|^2 dtheta r dr = pi (v'^2 + v''^2/n^2) dy, no integration by parts",
      zero(Zsq_r * r - sp.pi * (v1 ** 2 + v2 ** 2 / n ** 2)))
AFZ_r = sp.pi * (-r * f / n) * (-v2 / (n * r)) * r
check("(8) directly from Z: int A_F.Z dtheta r dr = (pi/n^2) r f_n (r^2 u'' + r u') dr, only the n-th mode of F",
      zero(AFZ_r - sp.pi / n ** 2 * r * f * (r ** 2 * sp.diff(u, r, 2) + r * sp.diff(u, r))))
V = sp.Function("v")(Y)
Vp, Vpp = sp.diff(V, Y), sp.diff(V, Y, 2)
d_y = sp.pi * (Vp ** 2 + n ** 2 * V ** 2)
AL2_y = sp.pi / n ** 2 * (Vpp - n ** 2 * V) ** 2
a7_y = sp.pi / n ** 2 * Vpp ** 2 + sp.pi * Vp ** 2
check("d = pi int (v'^2 + n^2 v^2) dy and ||A_(Delta psi)||^2 = (pi/n^2) int (v'' - n^2 v)^2 dy (theta integrals)",
      zero(sp.pi * (sp.diff(u, r) ** 2 + n ** 2 * u ** 2 / r ** 2) * r * r - sp.pi * (v1 ** 2 + n ** 2 * u ** 2))
      and zero(sp.pi / n ** 2 * r ** 3 * lap ** 2 * r - sp.pi / n ** 2 * (v2 - n ** 2 * u) ** 2))
check("(6) a = ||A_(Delta psi)||^2 - d differs from (7) by the boundary term -2 pi [v v']: integrands differ by "
      "-2 pi (v v')'", zero(AL2_y - d_y - a7_y + 2 * sp.pi * sp.diff(V * Vp, Y)))
check("<A_(Delta psi), grad psi> = d up to the boundary term: integrands differ by -pi (v v')'",
      zero(-sp.pi * (Vpp - n ** 2 * V) * V - d_y + sp.pi * sp.diff(V * Vp, Y)))
check("<A_F, grad psi> = -p exactly per r (theta integration only): -pi r f_n u = -(pi r f_n u)",
      zero(sp.pi * (-r * f / n) * (n * u / r) * r + sp.pi * r * f * u))
check("(6) b = <A_F, A_(Delta psi)> + p equals the (8) integrand exactly per r (no integration by parts)",
      zero(sp.pi * (-r * f / n) * (-r * lap / n) * r + sp.pi * f * u * r - AFZ_r))

t, bb, cB = sp.symbols("t b c", positive=True)
cs = sp.symbols("c0:6")
Pg = sum(cs[i] * t ** i for i in range(6))


def Dop(b_, P_):
    return sp.expand((1 - 2 * b_ * t) * P_ + 2 * t * (1 - t) * sp.diff(P_, t))


tr = r ** 2 / (1 + r ** 2)
check("dt/dy = r dt/dr = 2 t (1 - t) and r^2 = t/w for t = r^2/(1 + r^2), w = 1 - t",
      zero(r * sp.diff(tr, r) - 2 * tr * (1 - tr)) and zero(r ** 2 - tr / (1 - tr)))
U_ = r * (1 - tr) ** bb * Pg.subs(t, tr)
U1 = r * sp.diff(U_, r)
U2 = r * sp.diff(U1, r)
check("(9) u_y = r w^b D_b P and u_yy = r w^b D_b(D_b P), symbolic b > 0, generic degree-5 P",
      zero(U1 - (r * (1 - t) ** bb * Dop(bb, Pg)).subs(t, tr))
      and zero(U2 - (r * (1 - t) ** bb * Dop(bb, Dop(bb, Pg))).subs(t, tr)))
X1, X2, Aa = sp.symbols("X1 X2 A")
rt = sp.sqrt(t / (1 - t))
jac = 1 / (2 * t * (1 - t))                                                # dy/dt
check("(10) change of variable: (r w^b X1)(r w^c X2) dy = (1/2) w^(b+c-2) X1 X2 dt",
      zero((rt * (1 - t) ** bb * X1) * (rt * (1 - t) ** cB * X2) * jac - (1 - t) ** (bb + cB - 2) * X1 * X2 / 2))
ee = sp.symbols("e", positive=True)
check("(11) change of variable: r (r w^e A)(r w^b X1) dr = (1/2) t w^(e+b-3) A X1 dt (dr = r dy)",
      zero(rt * (rt * (1 - t) ** ee * Aa) * (rt * (1 - t) ** bb * X1) * rt * jac
           - t * (1 - t) ** (ee + bb - 3) * Aa * X1 / 2))


def mom(j, q):
    """int_0^1 t^j (1-t)^q dt = j! / prod_{i=1}^{j+1} (q+i), q > -1"""
    assert q > -1
    v = Fr(factorial(j))
    for i in range(1, j + 2):
        v /= q + i
    return v


okb = True
for j in range(8):
    for q in map(Fr, ["-1/2", "-1/3", "0", "1/3", "1", "3/2", "7/4", "5/2"]):
        g = sp.gammasimp(sp.gamma(j + 1) * sp.gamma(sp.Rational(q.numerator, q.denominator) + 1)
                         / sp.gamma(sp.Rational(q.numerator, q.denominator) + j + 2))
        okb = okb and sp.Rational(mom(j, q).numerator, mom(j, q).denominator) == g
check("beta moment formula = Gamma(j+1) Gamma(q+1)/Gamma(q+j+2) for j = 0..7 and 8 values of q in (-1, 5/2]", okb)

# ---------------------------------------------------------------- exact r-route and t-route machinery
S = sp.symbols("S", positive=True)                                         # S = sqrt(1 + r^2)


def Dr(E):
    return sp.diff(E, r) + sp.diff(E, S) * r / S


def zeroS(e):
    """zero after S = sqrt(1 + r^2) (Laurent polynomials in r, S are equal only modulo S^2 = 1 + r^2)"""
    return zero(e.subs(S, sp.sqrt(1 + r ** 2)))


def rint(E):
    """exact int_0^oo E dr for a Laurent polynomial E in r and S, termwise; asserts termwise convergence"""
    tot = Fr(0)
    for term in sp.Add.make_args(sp.expand(E)):
        c, rest = term.as_coeff_Mul()
        pw = rest.as_powers_dict() if rest != 1 else {}
        assert set(pw) <= {r, S} and c.is_Rational, term
        m, e = int(pw.get(r, 0)), sp.Rational(pw.get(S, 0))
        k, sig = (m + 1) // 2, Fr(int(-e.p), int(e.q)) / 2
        assert m % 2 == 1 and m >= 1 and sig - k > 0, term
        z, val = sig - k, Fr(factorial(k - 1), 2)
        for i in range(k):
            val /= z + i
        tot += Fr(int(c.p), int(c.q)) * val
    return tot


def rtrial(terms):
    """u = sum x r^3 (1+r^2)^(-beta) t^k as a Laurent polynomial in r, S; terms = [(x, beta, k)]"""
    return sum(sp.Rational(x) * r ** 3 * S ** (-2 * sp.Rational(beta)) * (r ** 2 / S ** 2) ** k for x, beta, k in terms)


def radial(u_, nn):
    """v', v'', (Delta psi)_n for psi = u sin(n theta)"""
    u1, u2 = Dr(u_), Dr(Dr(u_))
    return r * u1, r * Dr(r * u1), u2 + u1 / r - nn ** 2 * u_ / r ** 2


def q_pair(ua, ub, nn):
    """r-route values /pi for two profiles of one mode n: <grad psi_a, grad psi_b>, <Z_a, Z_b> (7 form),
    <A_(Delta a), A_(Delta b)>"""
    a1, a2, la = radial(ua, nn)
    b1, b2, lb = radial(ub, nn)
    return {"G": rint((a1 * b1 + nn ** 2 * ua * ub) / r), "Z": rint((a1 * b1 + a2 * b2 / nn ** 2) / r),
            "AL": rint(r ** 3 * la * lb) / nn ** 2}


def src_vals(fn, ua, nn):
    """r-route values /pi for source mode f_n and test profile u: M2 part, b by (8), b by (6), p"""
    a1, a2, la = radial(ua, nn)
    return {"M2": rint(r ** 3 * fn ** 2) / nn ** 2, "b8": rint(r * fn * a2) / nn ** 2,
            "b6": rint(r ** 3 * fn * la) / nn ** 2 + rint(r * fn * ua), "p": rint(r * fn * ua)}


def tint(q, poly):
    """exact int_0^1 (1-t)^q poly(t) dt"""
    q = Fr(int(q.p), int(q.q)) if isinstance(q, sp.Basic) else Fr(q)
    cf = sp.Poly(sp.expand(poly), t).all_coeffs()[::-1] if sp.expand(poly) != 0 else []
    return sum((Fr(int(c.p), int(c.q)) * mom(j, q) for j, c in enumerate(cf)), Fr(0))


def sq(x):
    return sp.Rational(x.numerator, x.denominator)


# ---------------------------------------------------------------- C: fixtures
print("C. manufactured fixtures (data/parameters.json)")
OUT["C"] = {}
fx = {}
for case in PAR["cases"]:
    nn, b_, P_ = case["n"], sp.Rational(case["b"]), sum(sp.Rational(c) * t ** i for i, c in enumerate(case["P"]))
    # r-route: P_b(t) = sum x t^(k+1) and b = beta - 1, so a term x t^j becomes (x, b + 1, j - 1)
    cf = sp.Poly(P_, t).all_coeffs()[::-1]
    terms = [(c, b_ + 1, j - 1) for j, c in enumerate(cf) if c != 0]
    ua = rtrial(terms)
    check("%s: u_r-route = r w^b P_b(t) (S = sqrt(1+r^2)) and the origin rule 3 + 2k >= n, 3 + 2k - n even"
          % case["name"], zeroS((ua - r * S ** (-2 * b_) * P_.subs(t, r ** 2 / S ** 2)))
          and all(3 + 2 * k >= nn and (3 + 2 * k - nn) % 2 == 0 for _, _, k in terms) and b_ > sp.Rational(1, 2))
    qq = q_pair(ua, ua, nn)
    v1a, v2a, la = radial(ua, nn)
    fn = -la                                                               # F = -Delta psi
    sv = src_vals(fn, ua, nn)
    # t-route
    DP, D2P = Dop(b_, P_), Dop(b_, Dop(b_, P_))
    q2 = Fr(int((2 * b_ - 2).p), int((2 * b_ - 2).q))
    Apoly = sp.cancel((nn ** 2 * P_ - D2P) / t)                            # f_n = r w^(b+1) A(t)
    check("%s: f_n = -(Delta psi)_n = r w^(b+1) A(t) with A = (n^2 P - D_b^2 P)/t a polynomial" % case["name"],
          sp.denom(sp.together(Apoly)) == 1
          and zeroS(fn - (r * S ** (-2 * b_ - 2) * Apoly.subs(t, r ** 2 / S ** 2))))
    tv = {"d": tint(q2, (DP ** 2 + nn ** 2 * P_ ** 2) / 2),
          "a": tint(q2, (D2P ** 2 / nn ** 2 + DP ** 2) / 2),
          "M2": tint(2 * (b_ + 1) - 4, t ** 2 * Apoly ** 2) / (2 * nn ** 2),
          "b": tint((b_ + 1) + b_ - 3, t * Apoly * D2P) / (2 * nn ** 2),
          "p": tint((b_ + 1) + b_ - 3, t * Apoly * P_) / 2}
    rv = {"d": qq["G"], "a": qq["Z"], "a6": qq["AL"] - qq["G"], "M2": sv["M2"], "b": sv["b8"], "b6": sv["b6"],
          "p": sv["p"]}
    check("%s: r-route d/pi = %s, a/pi by (7) = %s = by (6) %s, M2/pi = %s, b/pi by (8) = %s = by (6) %s, p/pi = %s"
          % (case["name"], rv["d"], rv["a"], rv["a6"], rv["M2"], rv["b"], rv["b6"], rv["p"]),
          rv["a"] == rv["a6"] and rv["b"] == rv["b6"])
    check("%s: t-route (10)/(11) equals the r-route for d, a, M2, b, p" % case["name"],
          all(tv[k] == rv[k] for k in tv))
    check("%s: equals parameters.json d/pi %s, M2/pi %s, a/pi %s, b/pi %s" % (case["name"], case["d_over_pi"],
          case["M2_over_pi"], case["a_over_pi"], case["b_over_pi"]),
          all(rv[k] == Fr(case[k + "_over_pi"]) for k in ("d", "M2", "a", "b")))
    check("%s: manufactured identities b = -a, M2 = d + a, p = d, M2 - b^2/a = d" % case["name"],
          rv["b"] == -rv["a"] and rv["M2"] == rv["d"] + rv["a"] and rv["p"] == rv["d"]
          and rv["M2"] - rv["b"] ** 2 / rv["a"] == rv["d"])
    fx[case["name"]] = dict(rv, u=ua, n=nn, b_exp=b_, P=P_)
    OUT["C"][case["name"]] = {k: str(v) for k, v in rv.items()}
x1, x3 = fx["mode1"], fx["mode3"]
M = x1["M2"] + x3["M2"]
ex = x1["d"] + x3["d"]
both = M - x1["b"] ** 2 / x1["a"] - x3["b"] ** 2 / x3["a"]
one = M - x1["b"] ** 2 / x1["a"]
check("combined F = -Delta(psi1 + psi3): H^2/pi = %s = both-test bound (5); one-test bound %s; gap %s (parameters.json"
      " %s, %s, %s)" % (ex, one, one - ex, PAR["combined_exact_H2_over_pi"], PAR["one_test_upper_over_pi"],
                        PAR["omitted_mode_gap_over_pi"]),
      ex == both == Fr(PAR["combined_exact_H2_over_pi"]) and one == Fr(PAR["one_test_upper_over_pi"])
      and one - ex == Fr(PAR["omitted_mode_gap_over_pi"]) == x3["a"])
am, bm = x1["a"] + 4 * x3["a"], x1["b"] + 2 * x3["b"]
cmb = RES["combined"]
tq = Fr(PAR["rational_test_coefficient"])
check("mixed trial psi1 + 2 psi3: a/pi = %s, b/pi = %s, M2 - b^2/a = %s > H^2 (result.json %s, %s, %s); at t = 3/4 the"
      " quadratic minus H^2 is (1-t)^2 a1 + (1-2t)^2 a3" % (am, bm, M - bm * bm / am, cmb["mixed_trial_a_over_pi"],
                                                              cmb["mixed_trial_b_over_pi"],
                                                              cmb["mixed_optimal_upper_over_pi"]),
      am == Fr(cmb["mixed_trial_a_over_pi"]) and bm == Fr(cmb["mixed_trial_b_over_pi"])
      and M - bm * bm / am == Fr(cmb["mixed_optimal_upper_over_pi"]) > ex
      and M + 2 * tq * bm + tq * tq * am - ex == (1 - tq) ** 2 * x1["a"] + (1 - 2 * tq) ** 2 * x3["a"]
      and Fr(cmb["M2_over_pi"]) == M)
# two-exponent trial, n = 3: cross terms of (10)
P15, P20 = t - 2 * t ** 2, t / 2 + t ** 3
u2e = rtrial([(1, sp.Rational(5, 2), 0), (-2, sp.Rational(5, 2), 1), (sp.Rational(1, 2), 3, 0), (1, 3, 2)])
check("two-exponent trial n = 3: u = r [w^(3/2)(t - 2t^2) + w^2 (t/2 + t^3)] in the r-route",
      zeroS(u2e - r * (S ** -3 * P15 + S ** -4 * P20).subs(t, r ** 2 / S ** 2)))
q2e = q_pair(u2e, u2e, 3)
a10 = Fr(0)
for bx, Px in ((sp.Rational(3, 2), P15), (sp.Integer(2), P20)):
    for cx, Pc in ((sp.Rational(3, 2), P15), (sp.Integer(2), P20)):
        ex_ = Fr(int((bx + cx - 2).p), int((bx + cx - 2).q))
        a10 += tint(ex_, (Dop(bx, Dop(bx, Px)) * Dop(cx, Dop(cx, Pc)) / 9 + Dop(bx, Px) * Dop(cx, Pc)) / 2)
check("two-exponent trial: a/pi by (10) with cross terms = %s = r-route (7) %s = r-route (6) %s > 0"
      % (a10, q2e["Z"], q2e["AL"] - q2e["G"]), a10 == q2e["Z"] == q2e["AL"] - q2e["G"] and a10 > 0)
OUT["C"]["combined"] = {"H2": str(ex), "one_test": str(one), "gap": str(one - ex), "mixed_a": str(am),
                        "mixed_b": str(bm), "mixed_opt": str(M - bm * bm / am)}
OUT["C"]["two_exponent_a_over_pi"] = str(a10)

# ---------------------------------------------------------------- D: sources not manufactured from the test
print("D. sources not manufactured from the test")
uF = r * S ** -4                                                           # r (1+r^2)^-2, b = 2, P = 1, n = 1
v1F, v2F, lF = radial(uF, 1)
fF = -lF
u1 = x1["u"]
H2 = q_pair(uF, uF, 1)["G"]                                                # H(F)^2 = ||grad psi_F||^2 (Riesz)
sv = src_vals(fF, u1, 1)
a1 = x1["a"]
AF_ = sp.cancel((1 * 1 - Dop(2, Dop(2, sp.Integer(1)))) / t)
b11 = tint(Fr(3) + Fr(3, 2) - 3, t * AF_ * Dop(sp.Rational(3, 2), Dop(sp.Rational(3, 2), sp.Integer(1)))) / 2
check("F = -Delta(r(1+r^2)^-2 sin theta), test psi1: f_1 = r w^3 A with A = %s; b/pi by (11) = %s = (8) %s = (6) %s"
      % (sp.expand(AF_), b11, sv["b8"], sv["b6"]),
      zeroS(fF - r * S ** -6 * AF_.subs(t, r ** 2 / S ** 2)) and b11 == sv["b8"] == sv["b6"])
low = sv["M2"] - sv["b8"] ** 2 / a1
check("H(F)^2/pi = %s < M2 - b^2/a = %s < M2/pi = %s (strict: the test is not the Riesz representative)"
      % (H2, low, sv["M2"]), H2 < low < sv["M2"])
okq = True
for tt_ in list(map(Fr, ["-1", "0", "1/2", "3/4", "1", "2"])) + [-sv["b8"] / a1]:
    qv = sv["M2"] + 2 * tt_ * sv["b8"] + tt_ * tt_ * a1
    okq = okq and qv >= low and qv > H2 and qv - low == a1 * (tt_ + sv["b8"] / a1) ** 2
check("(3) at t = -1, 0, 1/2, 3/4, 1, 2, -b/a: M2 + 2tb + t^2 a = (M2 - b^2/a) + a (t + b/a)^2 > H^2", okq)
p_, d1 = sv["p"], x1["d"]
pG = q_pair(uF, u1, 1)["G"]
gH2 = q_pair(uF - u1, uF - u1, 1)["G"]                                     # H(g)^2, g = F + Delta psi = -Delta(psi_F - psi)
check("p = int F psi = <grad psi_F, grad psi> = %s (two r-routes)" % p_, p_ == pG)
check("supplement energy identity H(F)^2 = 2p - d + H(g)^2, g = F + Delta psi: %s = 2 %s - %s + %s"
      % (H2, p_, d1, gH2), H2 == 2 * p_ - d1 + gH2)
_, _, l1 = radial(u1, 1)
Ag2 = rint(r ** 3 * (fF + l1) ** 2)                                        # ||A_g||^2/pi, A_g = A_F + A_(Delta psi)
t1 = sv["M2"] + 2 * sv["b8"] + a1
check("t = 1 reading: M2 + 2b + a = %s = 2p - d + ||A_g||^2 = %s (A_g = A_F + A_(Delta psi), linear in the source)"
      % (t1, 2 * p_ - d1 + Ag2), t1 == 2 * p_ - d1 + Ag2 and Ag2 >= gH2)
# triangle bound (sqrt(d) + sqrt(M_g2))^2 >= 2p - d + M_g2  <=>  sqrt(d) sqrt(M_g2) >= p - d, checked by squares
check("triangle bound: (sqrt d + ||A_g||)^2 >= 2p - d + ||A_g||^2 (p - d = %s; d ||A_g||^2 >= (p - d)^2 if p > d)"
      % (p_ - d1), (p_ - d1 <= 0) or d1 * Ag2 >= (p_ - d1) ** 2)
# the same source with the half test psi1/2, where p > d and the triangle bound is not trivial
uh = u1 / 2
svh = src_vals(fF, uh, 1)
dh, ah = q_pair(uh, uh, 1)["G"], q_pair(uh, uh, 1)["Z"]
gh2 = q_pair(uF - uh, uF - uh, 1)["G"]
_, _, lh = radial(uh, 1)
Agh = rint(r ** 3 * (fF + lh) ** 2)
check("half test psi1/2: p - d = %s > 0; H^2 = 2p - d + H(g)^2; t = 1 value %s = 2p - d + ||A_g||^2 <= (sqrt d + "
      "||A_g||)^2 (checked as d ||A_g||^2 >= (p - d)^2)" % (svh["p"] - dh, svh["M2"] + 2 * svh["b8"] + ah),
      svh["p"] > dh and H2 == 2 * svh["p"] - dh + gh2 and svh["M2"] + 2 * svh["b8"] + ah == 2 * svh["p"] - dh + Agh
      and dh * Agh >= (svh["p"] - dh) ** 2)


def dround(x, digits, up):
    """x rounded to `digits` decimals, up or down, exactly"""
    q = x * 10 ** digits
    k = -((-q.numerator) // q.denominator) if up else q.numerator // q.denominator
    return Fr(k, 10 ** digits)


Ud, Ad, Bd = dround(sv["M2"], 6, True), dround(a1, 6, True), dround(abs(sv["b8"]), 6, False)
check("directed use (PROOF.md 'Directed use'): U = %s >= M2, A = %s >= a, 0 <= B = %s <= |b| give U - B^2/A = %s >= "
      "M2 - b^2/a >= H^2 (six-decimal displays of the exact values, rounded outward)" % (Ud, Ad, Bd, Ud - Bd ** 2 / Ad),
      Ud >= sv["M2"] and Ad >= a1 and 0 <= Bd <= abs(sv["b8"]) and Ud - Bd ** 2 / Ad >= low >= H2)
OUT["D"] = {"single": {"H2": str(H2), "M2": str(sv["M2"]), "b": str(sv["b8"]), "a": str(a1), "bound4": str(low),
                       "p": str(p_), "Hg2": str(gH2), "Ag2": str(Ag2), "t1_value": str(t1)}}
# two-mode source with a same-mode Gram test and a mode-3 test
uG = rtrial([(1, sp.Rational(7, 2), 0)])                                   # r^3 (1+r^2)^-7/2 sin(3 theta)
_, _, lG = radial(uG, 3)
fG = -lG
H2two = H2 + q_pair(uG, uG, 3)["G"]
u1b = r * S ** -6                                                          # r (1+r^2)^-3, n = 1
g11, g12, g22 = q_pair(u1, u1, 1)["Z"], q_pair(u1, u1b, 1)["Z"], q_pair(u1b, u1b, 1)["Z"]
s1, s2 = src_vals(fF, u1, 1)["b8"], src_vals(fF, u1b, 1)["b8"]
det = g11 * g22 - g12 ** 2
corr = (g22 * s1 ** 2 - 2 * g12 * s1 * s2 + g11 * s2 ** 2) / det           # b^T G^-1 b
svG = src_vals(fG, x3["u"], 3)
Mtwo = sv["M2"] + svG["M2"]
bnd5 = Mtwo - corr - svG["b8"] ** 2 / x3["a"]
check("two-mode source F = -Delta(r(1+r^2)^-2 sin theta + r^3(1+r^2)^-7/2 sin 3theta): Gram of psi1, r(1+r^2)^-3 sin"
      " theta positive definite (det/pi^2 = %s)" % det, g11 > 0 and det > 0)
check("(5) with the Gram block: H^2/pi = %s < M2 - b^T G^-1 b - b3^2/a3 = %s < M2 - b1^2/a1 - b3^2/a3 = %s < M2 = %s"
      % (H2two, bnd5, Mtwo - s1 ** 2 / g11 - svG["b8"] ** 2 / x3["a"], Mtwo),
      H2two < bnd5 < Mtwo - s1 ** 2 / g11 - svG["b8"] ** 2 / x3["a"] < Mtwo)
OUT["D"]["two_mode"] = {"H2": str(H2two), "bound_gram": str(bnd5), "M2": str(Mtwo), "gram_det": str(det)}

# ---------------------------------------------------------------- E: positive pole (supplement)
print("E. positive-pole source mode (ERRATA_v01), FLOAT cross-check and exact closed form")
mp.mp.dps = 40
Ntp = t * (1 - 2 * t)
D2u3 = Dop(2, Dop(2, t))                                                   # mode-3 fixture P = t, b = 2
check("D_2^2 t = 9t - 48t^2 + 48t^3 (mode-3 fixture)", zero(D2u3 - (9 * t - 48 * t ** 2 + 48 * t ** 3)))
integ_t = sp.lambdify(t, (1 - t) ** sp.Rational(3, 2) * t * Ntp / (1 + 3 * (1 - t)) ** 2 * D2u3, "mpmath")
b11E = mp.quad(integ_t, [0, 0.5, 1]) / (2 * 9)
rr = sp.symbols("rr", positive=True)
ww = 1 / (1 + rr ** 2)
fE = rr * ww ** sp.Rational(5, 2) * Ntp.subs(t, 1 - ww) / (1 + 3 * ww) ** 2
_, v2_3, _ = radial(x3["u"], 3)
integ_r = sp.lambdify(rr, rr * fE * v2_3.subs({r: rr, S: sp.sqrt(1 + rr ** 2)}), "mpmath")
b8E = mp.quad(integ_r, [0, 0.5, 1, 4, 30, mp.inf]) / 9
check("b/pi by (11) in t = %s and by (8) in r = %s agree to 1e-30 relative (FLOAT observation)"
      % (mp.nstr(b11E, 25), mp.nstr(b8E, 25)), abs(b11E - b8E) < 1e-30 * abs(b8E))
s_ = sp.symbols("s", positive=True)
expr = (s_ ** 3 * (1 - s_ ** 2) * Ntp.subs(t, 1 - s_ ** 2) / (1 + 3 * s_ ** 2) ** 2
        * D2u3.subs(t, 1 - s_ ** 2) * 2 * s_)                              # w = s^2, dt = 2 s ds on [0, 1]
cl = sp.simplify(sp.integrate(sp.expand(expr), (s_, 0, 1)) / 18)
ra, rb = cl.as_independent(sp.pi)
check("exact closed form b/pi = %s (contains a nonzero rational multiple of sqrt(3) pi, so it is irrational) and its "
      "40-digit value matches (8)" % cl, sp.simplify(rb / (sp.sqrt(3) * sp.pi)).is_Rational and rb != 0
      and ra.is_Rational and abs(mp.mpf(str(sp.N(cl, 45))) - b8E) < 1e-30 * abs(b8E))
OUT["E"] = {"source": "f_3 = r w^(5/2) t (1-2t)/(1+3w)^2, test u3 = r^3 (1+r^2)^-3", "b_over_pi_closed_form": str(cl),
            "b_over_pi_11": mp.nstr(b11E, 30), "b_over_pi_8": mp.nstr(b8E, 30)}

OUT.update(checks=N[0], fails=FAILS, elapsed_s=round(time.time() - T0, 3))
(HERE_ / "data/review_t4_469_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("%d checks, %d FAIL, %.2f s" % (N[0], len(FAILS), time.time() - T0))
sys.exit(1 if FAILS else 0)
