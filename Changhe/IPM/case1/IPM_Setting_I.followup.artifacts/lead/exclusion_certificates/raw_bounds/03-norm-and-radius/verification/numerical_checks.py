"""Numerical evidence, separate from rational_certificate.py.

Checks the rational-family value in two formulas, and computes exact-linearized
polynomial responses by finite-part beta moments. No trial-data fitting enters
these calculations. All output files stay beside this script.
"""
import resource
resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))
import json
import math
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
ROOT = Path(__file__).resolve().parent
u = sp.Symbol("u", positive=True)


def B_beta(A, e):
    be = 2/A
    return (16-be)/(3*A*(4+be))*mp.beta(2-be/2,be)*(
        1-6*A*(4*A-3)/(8*A-1)*e)


def B_integral(A,e):
    be = 2/A
    # Integration by parts after subtracting the divergent polynomial:
    # 1/(3A) integral [5(1-6Ae)u^4+3(1+2Ae)u^2] ((1-u^2)/u)^(be-1) du.
    # y=(1-u^2)^be removes the source singularity exactly.
    def fun(y):
        t = 1-y**(1/be)
        if t <= 0:
            return mp.mpf(0)
        return (5*(1-6*A*e)*t**(2-be/2)
                +3*(1+2*A*e)*t**(1-be/2))/(6*A*be)
    return mp.quad(fun, [0,mp.mpf(".5"),1])


def bernstein_bound(coeff, a, b):
    """Exact upper bound of |polynomial| on [a,b] using Bernstein coefficients."""
    n = len(coeff)-1
    c = [sum(coeff[j]*math.comb(j,k)*a**(j-k)*(b-a)**k
             for j in range(k,n+1)) for k in range(n+1)]
    bs = [sum(c[k]*F(math.comb(i,k),math.comb(n,k)) for k in range(i+1))
          for i in range(n+1)]
    return max(map(abs,bs))


def polynomial_bound(poly, a, b, pieces=32):
    pp = sp.Poly(sp.expand(poly),u)
    coeff = [F(pp.nth(i)) for i in range(pp.degree()+1)]
    return max(bernstein_bound(coeff,a+(b-a)*F(i,pieces),a+(b-a)*F(i+1,pieces))
               for i in range(pieces))


def response(A,e,j):
    As, es = sp.Rational(str(A)), sp.Rational(str(e))
    be = 2/A
    w = -As*u*(1-u*u)/(1+u*u)
    g = u*u/(1+u*u)
    k = 2/(u*(1+u*u))
    v = u**j+sp.Rational(j-11,2)*u**9+sp.Rational(9-j,2)*u**11
    av = sp.cancel((sp.diff(v,u)-k*v)/w)
    eta = sp.integrate(sp.expand(av),(u,0,u))
    assert sp.denom(sp.cancel(av)) == As.q or sp.Poly(av,u) is not None
    Q = sp.cancel((sp.diff(g,u)-es*sp.diff(w,u,2))/(2*g**3))
    dq = sp.cancel(av/(2*g**2)-es*sp.diff(v,u,2)/(2*g**3)
                   +(k/(2*g**2)-3*Q)*eta)
    vm = sp.cancel(v/w-eta)
    # Keep beta symbolic; the reference A,e are exact decimals here.
    bs = sp.Symbol("b")
    integrand = sp.expand(sp.cancel(sp.diff(dq,u)+(bs-1)*sp.diff(Q,u)*vm))
    value = mp.mpf(0)
    for term in sp.Add.make_args(integrand):
        power = term.as_powers_dict().get(u,sp.Integer(0))
        cc = sp.cancel(term/u**power)
        cv = mp.mpf(str(sp.N(cc.subs(bs,sp.Rational(str(be))),70)))
        value += cv*mp.beta((mp.mpf(int(power))+2-be)/2,be)/(6*A)
    # A second derivative formula: differentiate the endpoint-subtracted form.
    # Individual beta moments also use a finite part at 1, but their source
    # divergences cancel because the bracket vanishes at 1.
    source_subtracted = sp.expand(sp.cancel((1+u*u)*(
        dq-dq.subs(u,1)+(Q-Q.subs(u,1))*((bs-2)*vm-eta))))
    value_sub = mp.mpf(0)
    for term in sp.Add.make_args(source_subtracted):
        power = term.as_powers_dict().get(u,sp.Integer(0))
        cc = sp.cancel(term/u**power)
        cv = mp.mpf(str(sp.N(cc.subs(bs,sp.Rational(str(be))),70)))
        value_sub += cv*mp.beta((mp.mpf(int(power))+1-be)/2,be-1)*(be-1)/(6*A)
    assert abs(value-value_sub) < mp.mpf("1e-55")
    rem = v-u**j
    origin = polynomial_bound(sp.cancel(sp.diff(rem,u,2)/u**6),F(0),F(1,2))
    tail2 = polynomial_bound(sp.diff(v,u,2),F(1,2),F(1))
    # H_theta(v'') <= sup|v'''| for theta=.9 and interval length<=1.
    tailH = polynomial_bound(sp.diff(v,u,3),F(1,2),F(1))
    normupper = 1+origin+tail2+tailH
    return {"j":j,"DB_phi":mp.nstr(value,40),
            "DB_source_subtracted":mp.nstr(value_sub,40),
            "derivative_formula_difference":mp.nstr(value-value_sub,8),
            "N_phi_rational_upper":str(normupper),
            "N_phi_upper_decimal":float(normupper),
            "tested_dual_lower_numerical":mp.nstr(abs(value)/(
                mp.mpf(normupper.numerator)/normupper.denominator),30),
            "eta_polynomial":str(eta)}


if __name__ == "__main__":
    results = {}
    for label,As,es in (("computed_e_decimal","10.150725","0.0135206"),
                         ("earlier","4","0.0625")):
        A,e = mp.mpf(As),mp.mpf(es)
        v1,v2 = B_beta(A,e),B_integral(A,e)
        assert abs(v1-v2) < mp.mpf("1e-55")
        results[label] = {
            "B_beta":mp.nstr(v1,50),"B_independent_integral":mp.nstr(v2,50),
            "difference":mp.nstr(v1-v2,8),
            "B_A_fixed_shape":mp.nstr(mp.diff(lambda a:B_beta(a,e),A),40),
            "B_e":mp.nstr(mp.diff(lambda ee:B_beta(A,ee),e),40),
            "B_AA":mp.nstr(mp.diff(lambda a:B_beta(a,e),A,2),40),
            "polynomial_responses":[response(A,e,j) for j in (3,5,7)],
        }
    A=mp.mpf("10.150725")
    results["different_normalizations"] = {
        L:{"e":mp.nstr(1/mp.mpf(L)**2,45),
           "B":mp.nstr(B_beta(A,1/mp.mpf(L)**2),45)}
        for L in ("8.6","8.6000638")
    }
    # Broad lognormal bump. The source cutoff is one throughout its maximizer.
    # v'' is differentiated symbolically for the bump before the remote cutoff.
    L=mp.mpf("8.6")
    a=mp.mpf("10.150725")
    for width in (mp.mpf(".3"),mp.mpf("1")):
        center=1/L
        ww=lambda x:-a*x*(1-x*x)/(1+x*x)
        vv=lambda x:ww(x)*mp.exp(-(mp.log(x/center)/width)**2)
        logs=[mp.log(center)-10+mp.mpf(i)/100 for i in range(1401)]
        vals=[abs(mp.diff(vv,mp.exp(t),2))*mp.exp(-6*t) for t in logs]
        ii=max(range(len(vals)),key=vals.__getitem__)
        # This is a sampled lower bound for N, not a certified maximum.
        results[f"bump_sigma_{width}"]={
            "origin_norm_sampled_lower":mp.nstr(vals[ii],30),
            "u_at_sample":mp.nstr(mp.exp(logs[ii]),20),
            "published_response":"-6.37e4" if width<1 else "-1.31e9",
        }
    (ROOT/"numerical_checks.json").write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps(results,indent=2))
