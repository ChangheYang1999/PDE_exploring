"""Third computation for verification topic 72 (circular strain cutoffs are positive local averages).

Written from the statement of topic 72 only; no verifier code is imported. The routes differ from the verifier's audit
(Gaussian-potential test):

1. Exact identities (sympy): H_eps of (11) solves -Delta H = P_eps inside the disk and is harmonic outside; value and
   first two radial derivatives match at r = eps; d_xxy H + (1/4) d_y P = 0 inside and = -sin(3 theta)/(pi r^3) outside
   (Cartesian differentiation); unit mass and second moment of P_1; ||d_x P_1||_1 = 16/(3 pi); the symbol of C is
   -(i r/4) sin(3 theta); the dual-norm factor (2 pi)^-2 int (sin(3 theta)/4)^2 = 1/(64 pi); the Peetre bound
   <X> <= <Y>(1 + |X - Y|) behind (13) and (1 + 2 M_1 + M_2) <= (1 + 2 sqrt(beta))^2.
2. Exact test of (2) on Schwartz functions h = Delta psi, for which U_2 = R_1^2 h = -d_xx psi, so that
   C h = -d_xxy psi + (1/4) d_y Delta psi is explicit with no Fourier integral:
   psi = x^2 y exp(-r^2) (harmonics 1 and 3, b[h] != 0) and psi = (x^2 y + y^3/3) exp(-2 r^2) (another mix). Both sides
   of (2) are computed with exact angular integrals and 40-digit radial quadrature at three eps at the origin, and by
   FLOAT quadrature at an off-center point; C h(0) = c + b/4 is exact; the
   contact term is shown to be necessary (c[h] != lim T_eps h(0) when b[h] != 0). For the pure harmonic-1 function
   psi = y exp(-r^2), T_eps h(0) = 0 for all eps, C h has zero angular mean and C h(0) = 0, so c = -b/4: the case
   that fixes the coefficient 1/4.
3. FLOAT: A(z) = 8 J_2(z)/z^2 against direct quadrature of the Fourier integral of P_1 at several z, the bounds (5) on a
   grid, and the asymptotics (8) to (10) for beta = 1, 0, 1/2 at eps = 2^-k.

Every number stored in the output is exact unless its name contains FLOAT.

Usage: python3 check_p72.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from pathlib import Path
import sympy as sp
import mpmath
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
out = {}
chk = {}
log = lambda m: print(f'[{time.monotonic() - t0:7.1f}s] {m}', file=sys.stderr, flush=True)
x, y = sp.symbols('x y', real=True)
r, e, th, z = sp.symbols('r epsilon theta z', positive=True)
pi = sp.pi

# 1. exact identities
Pin = 2 / (pi * e ** 2) * (1 - r ** 2 / e ** 2)
Hin = -r ** 2 / (2 * pi * e ** 2) + r ** 4 / (8 * pi * e ** 4) - sp.log(e) / (2 * pi) + sp.Rational(3, 8) / pi
Hout = -sp.log(r) / (2 * pi)
radlap = lambda f: sp.diff(f, r, 2) + sp.diff(f, r) / r
chk['-Delta H_in = P_eps'] = sp.simplify(-radlap(Hin) - Pin) == 0
chk['H_out harmonic'] = sp.simplify(radlap(Hout)) == 0
for k in range(3):
    chk[f'radial derivative {k} matches at r = eps'] = sp.simplify((sp.diff(Hin, r, k) - sp.diff(Hout, r, k)).subs(r, e)) == 0
chk['third radial derivative jumps (no smoother than C2)'] = sp.simplify((sp.diff(Hin, r, 3) - sp.diff(Hout, r, 3)).subs(r, e)) != 0
cart = {r: sp.sqrt(x ** 2 + y ** 2)}
HinC = Hin.subs(cart); HoutC = Hout.subs(cart); PinC = Pin.subs(cart)
s3 = y * (3 * x ** 2 - y ** 2) / (x ** 2 + y ** 2) ** sp.Rational(3, 2)
chk['inside: d_xxy H + d_y P/4 = 0'] = sp.simplify(sp.diff(HinC, x, 2, y) + sp.diff(PinC, y) / 4) == 0
chk['outside: d_xxy H = -sin(3 theta)/(pi r^3)'] = sp.simplify(sp.diff(HoutC, x, 2, y) + s3 / (pi * (x ** 2 + y ** 2) ** sp.Rational(3, 2))) == 0
chk['sin(3 theta) = y(3x^2 - y^2)/r^3'] = sp.simplify(sp.expand_trig(sp.sin(3 * th)) - (s3.subs({x: r * sp.cos(th), y: r * sp.sin(th)}))) == 0
P1 = Pin.subs(e, 1)
chk['int P_1 = 1'] = sp.integrate(P1 * 2 * pi * r, (r, 0, 1)) == 1
chk['int x^2 P_1 = 1/6'] = sp.integrate(sp.integrate(P1 * (r * sp.cos(th)) ** 2 * r, (th, 0, 2 * pi)), (r, 0, 1)) == sp.Rational(1, 6)
dxP1 = sp.diff(P1.subs(cart), x)   # = -4x/pi
chk['||d_x P_1||_1 = 16/(3 pi)'] = sp.simplify(sp.integrate(sp.integrate(sp.Abs(sp.simplify(dxP1.subs({x: r * sp.cos(th), y: r * sp.sin(th)}))) * r,
                                                                           (th, 0, 2 * pi)), (r, 0, 1)) - 16 / (3 * pi)) == 0
# 1 - A <= z^2/12: 1 - cos u <= u^2/2 and the x-moment; A = 8 J_2(z)/z^2 is used only in the FLOAT part
lb = sp.I * r * sp.sin(th); lc = -sp.I * r * sp.sin(th) * sp.cos(th) ** 2
chk['symbol of C = -(i r/4) sin(3 theta)'] = sp.simplify(sp.expand_trig(lc + lb / 4 + sp.I * r / 4 * sp.sin(3 * th))) == 0
chk['(2 pi)^-2 int (sin(3 theta)/4)^2 = 1/(64 pi)'] = sp.simplify(sp.integrate((sp.sin(3 * th) / 4) ** 2, (th, 0, 2 * pi)) / (4 * pi ** 2) - 1 / (64 * pi)) == 0
chk['harmonic 3 orthogonal to sin(theta) (b = 0 on representatives)'] = sp.integrate(sp.sin(3 * th) * sp.sin(th), (th, 0, 2 * pi)) == 0
# Peetre: <X>^2 <= (<Y> + t)^2 <= <Y>^2 (1 + t)^2 because <Y> >= 1; then omega0 ratio <= (1 + t)^(6/5) <= (1 + t)^2
Y, t, bt = sp.symbols('Y t beta', positive=True)
chk['(<Y>(1 + t))^2 - (<Y> + t)^2 = t(<Y> - 1)(<Y>(2 + t) + t) >= 0'] = sp.expand((Y * (1 + t)) ** 2 - (Y + t) ** 2 - t * (Y - 1) * (Y * (2 + t) + t)) == 0
chk['1 + 2 M_1 + M_2 <= (1 + 2 sqrt(beta))^2 with M_1 <= sqrt(M_2), M_2 = 4 beta'] = sp.expand((1 + 2 * sp.sqrt(bt)) ** 2 - (1 + 2 * sp.sqrt(4 * bt) + 4 * bt)) == 0

log('section 1 done')
# 2. exact test of (2)
pol = {x: r * sp.cos(th), y: r * sp.sin(th)}
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)


def both_sides(psi, X0):
    """T_eps h(X0) and (P_eps * C h)(X0) for h = Delta psi, X0 = (x0, 0) on the x-axis (exact in eps)."""
    h = sp.expand(lap(psi))
    Ch = sp.expand(-sp.diff(psi, x, 2, y) + sp.diff(lap(psi), y) / 4)
    x0 = X0
    if x0 == 0:
        # the Gaussian factor is radial: replace it by a symbol before the polar substitution
        E = sp.Symbol('E', positive=True)
        g = [f for f in sp.preorder_traversal(psi) if isinstance(f, sp.exp)][0]
        aa = sp.simplify(-g.args[0] / (x ** 2 + y ** 2))
        def toE(ex):   # sympy may split the Gaussian into exp(-a x^2) exp(-a y^2); recombine termwise
            terms = sp.Add.make_args(sp.expand(ex, power_exp=False))
            return sp.expand(sp.Add(*[sp.powsimp(t_, combine='exp').subs(g, E) for t_ in terms]), power_exp=False)
        hE = toE(lap(psi)); CE = toE(-sp.diff(psi, x, 2, y) + sp.diff(lap(psi), y) / 4)
        assert not hE.has(sp.exp) and not CE.has(sp.exp)
        hp = sp.expand(hE.subs({x: r * sp.cos(th), y: r * sp.sin(th)}, simultaneous=True))
        Cp = sp.expand(CE.subs({x: -r * sp.cos(th), y: -r * sp.sin(th)}, simultaneous=True))
        lhs_ang = sp.integrate(sp.expand(hp * sp.sin(3 * th)), (th, 0, 2 * pi)).subs(E, sp.exp(-aa * r ** 2))
        Cang = sp.integrate(Cp, (th, 0, 2 * pi)).subs(E, sp.exp(-aa * r ** 2))
        fL = sp.lambdify(r, lhs_ang / (pi * r ** 2), 'mpmath')
        fR = sp.lambdify((r, e), Pin * Cang * r, 'mpmath')
        return fL, fR, h, Ch
    # T_eps h(X0) = (1/pi) int_(|Y| > eps) sin(3 theta_Y) h(X0 + Y)/|Y|^3 dY
    hp = sp.expand(h.subs({x: x0 + r * sp.cos(th), y: r * sp.sin(th)}, simultaneous=True))
    # off-center point: FLOAT-free exact evaluation is heavy, so compare at rational eps by mpmath quadrature
    fl = sp.lambdify((r, th), hp * sp.sin(3 * th) / (pi * r ** 2), 'mpmath')
    Cq = sp.lambdify((r, th), sp.expand(Ch.subs({x: x0 - r * sp.cos(th), y: -r * sp.sin(th)}, simultaneous=True)), 'mpmath')
    return fl, Cq, h, Ch


psis = {'x^2 y exp(-r^2)': x ** 2 * y * sp.exp(-(x ** 2 + y ** 2)),
        '(x^2 y + y^3/3) exp(-2 r^2)': (x ** 2 * y + y ** 3 / 3) * sp.exp(-2 * (x ** 2 + y ** 2))}
out['identity_tests'] = {}
for name, psi in psis.items():
    fL, fR, h, Ch = both_sides(psi, 0)
    mpmath.mp.dps = 40
    diffs = {}
    for ev in (mpmath.mpf(1) / 3, mpmath.mpf(7) / 5, mpmath.mpf(3)):
        lhs = mpmath.quad(fL, [ev, 2 * ev, 4, 8, mpmath.inf])
        rhs = mpmath.quad(lambda rr: fR(rr, ev), [0, ev])
        diffs[mpmath.nstr(ev, 5)] = {'T_eps_h_0_FLOAT': float(lhs), 'difference_FLOAT': float(lhs - rhs)}
    chk[f'(2) at the origin, eps = 1/3, 7/5, 3 (40-digit quadrature, FLOAT): {name}'] = all(abs(v['difference_FLOAT']) < 1e-30 for v in diffs.values())
    b0 = sp.diff(h, y).subs({x: 0, y: 0})
    c0 = (-sp.diff(psi, x, 2, y)).subs({x: 0, y: 0})
    Ch0 = Ch.subs({x: 0, y: 0})
    small = mpmath.quad(fL, [mpmath.mpf(2) ** -20, mpmath.mpf(2) ** -10, 1, 4, 8, mpmath.inf])
    chk[f'C h(0) = c + b/4 exactly, and T_eps h(0) -> C h(0) (eps = 2^-20, FLOAT): {name}'] = \
        sp.simplify(Ch0 - c0 - b0 / 4) == 0 and abs(small - mpmath.mpf(sp.N(Ch0, 40))) < 1e-5
    chk[f'contact term needed (b != 0): {name}'] = sp.simplify(b0) != 0
    log(f'origin test {name} done')
    out['identity_tests'][name] = {'b': str(b0), 'c': str(sp.simplify(c0)), 'C_h_0': str(sp.simplify(Ch0)), 'radial_quadrature': diffs,
                                   'T_eps_h_0_at_eps_2^-20_FLOAT': float(small)}
# off-center point X0 = (1/2, 0), eps in {1/4, 1}: FLOAT quadrature of both sides (scipy, the integrands are Gaussian-damped;
# the truncation at |Y| = 12 drops less than exp(-100) relative mass)
import numpy as np
from scipy import integrate as si
offc = {}
for name, psi in psis.items():
    h = sp.expand(lap(psi)); Ch = sp.expand(-sp.diff(psi, x, 2, y) + sp.diff(lap(psi), y) / 4)
    x0 = sp.Rational(1, 2)
    fl = sp.lambdify((r, th), h.subs({x: x0 + r * sp.cos(th), y: r * sp.sin(th)}, simultaneous=True) * sp.sin(3 * th) / (pi * r ** 2), 'numpy')
    Cq = sp.lambdify((r, th), Ch.subs({x: x0 - r * sp.cos(th), y: -r * sp.sin(th)}, simultaneous=True), 'numpy')
    for ev in (0.25, 1.0):
        lhs = si.dblquad(lambda tt, rr: fl(rr, tt), ev, 12.0, 0.0, 2 * np.pi, epsabs=1e-14, epsrel=1e-13)[0]
        rhs = si.dblquad(lambda tt, rr: 2 / (np.pi * ev ** 2) * (1 - rr ** 2 / ev ** 2) * rr * Cq(rr, tt), 0.0, ev, 0.0, 2 * np.pi,
                         epsabs=1e-14, epsrel=1e-13)[0]
        offc[f'{name}, eps = {ev}'] = {'T_eps_FLOAT': float(lhs), 'average_FLOAT': float(rhs), 'difference_FLOAT': float(lhs - rhs)}
log('off-center done')
chk['(2) at X0 = (1/2, 0), eps = 1/4 and 1 (FLOAT quadrature)'] = all(abs(v['difference_FLOAT']) < 1e-10 for v in offc.values())
out['off_center_FLOAT'] = offc
# pure harmonic 1 (psi = y exp(-r^2)): T_eps h(0) = 0 for every eps, so (2) requires a zero disk average of C h at the
# origin; C h itself is not zero (harmonics 2 and 4), and C h(0) = 0 means c[h] = -b[h]/4: the contact coefficient 1/4
psi1 = y * sp.exp(-(x ** 2 + y ** 2))
Ch1 = sp.expand(sp.simplify((-sp.diff(psi1, x, 2, y) + sp.diff(lap(psi1), y) / 4) * sp.exp(x ** 2 + y ** 2)))
h1 = sp.expand(sp.simplify(lap(psi1) * sp.exp(x ** 2 + y ** 2)))
Ch1p = sp.expand(Ch1.subs({x: r * sp.cos(th), y: r * sp.sin(th)}, simultaneous=True))
b1 = sp.diff(h1, y).subs({x: 0, y: 0}); c1 = (-sp.diff(psi1, x, 2, y)).subs({x: 0, y: 0})
chk['pure harmonic 1: C h(0) = 0, c = -b/4 with b != 0'] = Ch1.subs({x: 0, y: 0}) == 0 and sp.simplify(c1 + b1 / 4) == 0 and b1 != 0
chk['pure harmonic 1: angular mean of C h vanishes at every r (disk averages at 0 vanish)'] = sp.simplify(sp.integrate(Ch1p, (th, 0, 2 * pi))) == 0
chk['pure harmonic 1: C h is not identically zero'] = sp.simplify(Ch1) != 0

# 3. FLOAT: A(z), bounds (5), asymptotics (8) to (10)
mpmath.mp.dps = 20
A = lambda zz: mpmath.mpf(1) if zz == 0 else 8 * mpmath.besselj(2, zz) / zz ** 2
dirA = {}
for zz in (0.5, 3.0, 10.0):
    d = mpmath.quad(lambda rr: 2 / mpmath.pi * (1 - rr ** 2) * rr * mpmath.quad(lambda tt: mpmath.cos(zz * rr * mpmath.cos(tt)), [0, mpmath.pi, 2 * mpmath.pi]), [0, 1])
    dirA[zz] = float(d - A(zz))
log('A direct done')
chk['A(z) = 8 J_2(z)/z^2 (FLOAT, direct quadrature)'] = max(abs(v) for v in dirA.values()) < 1e-15
grid = [mpmath.mpf(j) / 50 for j in range(1, 10001)]
viol = [float(zz) for zz in grid if abs(A(zz)) > min(1, 16 / (3 * mpmath.pi * zz)) or not (0 <= 1 - A(zz) <= min(2, zz ** 2 / 12))]
chk['bounds (5) on z = 0.02 ... 200 (FLOAT)'] = not viol
out['A_direct_minus_formula_FLOAT'] = {str(k_): v for k_, v in dirA.items()}


def W(rr, beta):
    return rr ** 3 / (1 + rr ** 2) ** 2 * (1 + mpmath.log(1 + rr ** 2)) ** (-2 * beta)


def norm2(beta, k, err):
    L = mpmath.mpf(2) ** k
    f = (lambda rr: W(rr, beta) * (1 - A(rr / L)) ** 2) if err else (lambda rr: W(rr, beta) * A(rr / L) ** 2)
    pts = [mpmath.mpf(0)] + [mpmath.mpf(2) ** j for j in range(-4, k + 1)] + [L * j for j in range(2, 201, 2)]
    val = mpmath.quad(f, pts)
    Mz = L * 200; vM = 1 + mpmath.log(1 + Mz ** 2)
    if err:   # tail beyond 200 L where |A| < 2e-5: (1/2) int_vM^inf (1 - e^(1-v)) v^(-2 beta) dv
        val += (vM ** (1 - 2 * beta) / (2 * beta - 1) - mpmath.e * mpmath.gammainc(1 - 2 * beta, vM)) / 2
    return val / (64 * mpmath.pi)


asym = {}
for beta, err in ((1, True), (0, False), (mpmath.mpf(1) / 2, False)):
    rows = {}
    for k in (8, 16, 32):
        v = 1 + mpmath.log(1 + mpmath.mpf(4) ** k)
        if err:
            pred = v ** (0.5 - beta) / (8 * mpmath.sqrt(2 * mpmath.pi * (2 * beta - 1)))
        elif beta < 0.5:
            pred = v ** (0.5 - beta) / (8 * mpmath.sqrt(2 * mpmath.pi * (1 - 2 * beta)))
        else:
            pred = mpmath.sqrt(mpmath.log(v)) / (8 * mpmath.sqrt(2 * mpmath.pi))
        log(f'asymptotics beta={beta} k={k}')
        rows[k] = float(mpmath.sqrt(norm2(beta, k, err)) / pred)
    asym[f'beta = {float(beta)}, {"error norm (8)" if err else "cutoff norm (9)/(10)"}'] = rows
out['asymptotic_ratio_norm_over_prediction_FLOAT'] = asym
chk['asymptotic ratios approach 1 (FLOAT)'] = all(abs(rw[32] - 1) < abs(rw[8] - 1) for rw in asym.values()) and \
    all(abs(rw[32] - 1) < 0.35 for rw in asym.values())

out['checks'] = {k_: bool(v_) for k_, v_ in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v_ in chk.items() if not v_]
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
