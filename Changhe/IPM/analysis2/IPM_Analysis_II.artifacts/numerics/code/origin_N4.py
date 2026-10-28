"""Near-origin Taylor constants (N4) on disks r <= r0 from the exact origin Taylor polynomials (state 88, phi to degree 34):
  sup |rho_y - a_0| / r^2,  sup |rho_x| / r^2,  sup |DU - DU(0)| / r^2 (max entry),  sup |U - DU(0) X| / r^3,
each as sum over degrees d of (rigorous sup_theta of the homogeneous part) r0^(d - power), plus a Cauchy remainder for the degrees beyond
the exact range: the fields are analytic on the polydisc |x|,|y| <= P; |coefficient of degree d| <= M_field/P^d (sum over the d+1 monomials
of |x|^a |y|^b <= r^d ... we use the standard bound sum_{|beta|=d} |c_beta| x^a y^b <= (d+1) M r^d / P^d) so the tail from degree d0 is
<= M sum_{d>=d0} (d+1) (r0/P)^d.  M from fcert2.FCert2.polydisc_field_bounds (crude, termwise).
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import numpy as np
from flint import arb, ctx
from fcert2 import FCert2
from boxenc3 import FIELDS

def homog_sups(poly, dmax, M=40000):
    """poly: dict (a,b)->Fraction; returns {d: rigorous sup_theta |sum_{a+b=d} c x^a y^b| on the unit circle} for d <= dmax."""
    th = np.linspace(0, 2*math.pi, M, endpoint=False); out = {}
    for d in range(dmax+1):
        terms = [(a, b, float(c)) for (a, b), c in poly.items() if a + b == d]
        if not terms: out[d] = arb(0); continue
        vals = np.zeros_like(th)
        for a, b, c in terms: vals += c*np.cos(th)**a*np.sin(th)**b
        out[d] = arb(float(np.abs(vals).max()))*(1 + arb(2)**-30)/(1 - arb(math.pi)*d/M)
    return out

def pdx(P): return {(a-1, b): a*v for (a, b), v in P.items() if a > 0}
def pdy(P): return {(a, b-1): b*v for (a, b), v in P.items() if b > 0}

if __name__ == '__main__':
    ctx.prec = 128
    T = json.load(open(sys.argv[1])); DEG = T['DEG']
    phi = {tuple(int(v) for v in k.split(',')): Fr(s) for k, s in T['phi'].items()}
    cl = Fr(T['cl']); a0 = Fr(T['a0'])
    psi = pdy(pdx(phi)); lap = {}
    for P in (pdx(pdx(phi)), pdy(pdy(phi))):
        for k, v in P.items(): lap[k] = lap.get(k, 0) + v
    rho = {k: -v for k, v in pdy(lap).items()}
    rho_x = pdx(rho); rho_y = pdy(rho)
    U1 = {k: -v for k, v in pdy(psi).items()}; U2 = pdx(psi)
    DU11 = pdx(U1); DU12 = pdy(U1); DU21 = pdx(U2); DU22 = pdy(U2)
    # exact degrees: phi to DEG; rho to DEG-3; grad rho, DU to DEG-4; U to DEG-3
    dmax_4 = DEG - 4; dmax_3 = DEG - 3
    fields = {'rho_y - a0': ({k: v for k, v in rho_y.items() if sum(k) >= 1}, 2, dmax_4, FIELDS['rho_y']),
              'rho_x': (rho_x, 2, dmax_4, FIELDS['rho_x']),
              'DU11 - (cl-1)': ({k: v for k, v in DU11.items() if sum(k) >= 1}, 2, dmax_4, FIELDS['DU11']),
              'DU12': (DU12, 2, dmax_4, FIELDS['DU12']), 'DU21': (DU21, 2, dmax_4, FIELDS['DU21']),
              'DU22 - (1-cl)': ({k: v for k, v in DU22.items() if sum(k) >= 1}, 2, dmax_4, FIELDS['DU22']),
              'U1 - (cl-1)x': ({k: v for k, v in U1.items() if sum(k) >= 2}, 3, dmax_3, FIELDS['U1']),
              'U2 - (1-cl)y': ({k: v for k, v in U2.items() if sum(k) >= 2}, 3, dmax_3, FIELDS['U2'])}
    # sanity: constant/linear parts
    print('rho_y(0) - a0 =', float(rho_y.get((0, 0), 0) - a0), '; DU11(0) - (cl-1) =', float(DU11.get((0, 0), 0) - (cl - 1)), '; U1 linear coef - (cl-1) =', float(U1.get((1, 0), 0) - (cl - 1)))
    S = FCert2(sys.argv[2], sys.argv[3], prec=256)
    Pdisc = Fr(1, 5)       # polydisc radius 0.2 (series converge for r < about 0.25)
    B = S.polydisc_field_bounds('base', 0, 0, Pdisc, Pdisc, 4)
    def Mcrude(comb): return sum((abs(c)*B[(a, b)] for (a, b), c in comb.items()), arb(0))
    out = {}
    for name, (poly, power, dmax, comb) in fields.items():
        sups = homog_sups(poly, dmax)
        M = Mcrude(comb)
        row = {}
        for r0 in (0.01, 0.02, 0.05, 0.1):
            s = sum((sups[d]*arb(r0)**(d-power) for d in range(power, dmax+1)), arb(0))
            x = arb(r0)/arb(Pdisc.numerator)*Pdisc.denominator
            d0 = dmax + 1
            tail = M*sum(((d+1)*x**d for d in range(d0, d0+200)), arb(0))/(1 - x) if x < 1 else arb('inf')     # crude geometric closure (x<1): sum_{d>=d0}(d+1)x^d <= [explicit 200 terms] + remainder < explicit/(1-x) ... conservative
            total = s + tail/arb(r0)**power
            row[r0] = (float(total.upper()), float(s.upper()), float((tail/arb(r0)**power).upper()))
            print('%-14s r0=%.2f: sup/r^%d <= %.6g  (polynomial part %.6g, remainder %.2e; M_crude=%.3g)' % (name, r0, power, float(total.upper()), float(s.upper()), float((tail/arb(r0)**power).upper()), float(M)))
        out[name] = {str(k): v for k, v in row.items()}
    json.dump(out, open(os.environ.get('ORIGIN_N4_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'origin_N4_088.json')), 'w'), indent=1)
