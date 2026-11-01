# Independent check of |sigma_k(b)| >= 1/100000 for k >= 2 at both real roots of P6 (lead review of verifier topic 120).
import json, sympy as sp
b,k,t=sp.symbols('b k t')
d=json.load(open('sigma_check.json'))
num=sp.sympify(d['generic_sigma_numerator']); den=sp.sympify(d['generic_sigma_denominator'])
P6=176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936
roots=sp.Poly(P6,b).intervals(eps=sp.Rational(1,10**30))
print('root intervals', [(float(a),float(c)) for (a,c),m in roots])
def lower(poly_b,lo,hi):
    # lower bound of a polynomial in b>0 on [lo,hi] by termwise monotonicity
    P=sp.Poly(sp.expand(poly_b),b); s=0
    for (e,),c in P.terms():
        s+=min(c*lo**e,c*hi**e)
    return s
def upper(poly_b,lo,hi):
    P=sp.Poly(sp.expand(poly_b),b); s=0
    for (e,),c in P.terms():
        s+=max(c*lo**e,c*hi**e)
    return s
small={int(kk):sp.sympify(v) for kk,v in d['sigma_small_k'].items()}
eps=sp.Rational(1,100000)
for (lo,hi),m in roots:
    assert lo>0
    print('root in',float(lo),float(hi))
    for kk in range(2,7):
        s=small[kk]; nu,de=sp.fraction(sp.together(s))
        L=lower(nu,lo,hi); U=upper(nu,lo,hi); de=sp.nsimplify(de)
        # sigma = nu/de with de a positive rational constant
        assert de.is_number and de>0
        ok = (L/de>=eps) or (U/de<=-eps)
        print(' k=%d sigma in [%.6e, %.6e] ok=%s'%(kk,float(L/de),float(U/de),ok)); assert ok
    # all k>=7: sigma_k = num/den, den>0; check -num - den*eps has nonnegative t-coefficients after k=t+7 (sigma negative)
    expr=sp.expand((-num - eps*den).subs(k,t+7))
    Pt=sp.Poly(expr,t)
    lows=[lower(c,lo,hi) for c in Pt.all_coeffs()]
    print(' k>=7: degree in t',Pt.degree(),' min coefficient lower bound %.4e'%float(min(lows)), ' all >=0:',all(x>=0 for x in lows),' some >0:',any(x>0 for x in lows))
    assert all(x>=0 for x in lows) and any(x>0 for x in lows)
    assert sp.Poly(sp.expand(den.subs(k,t+7)),t).all_coeffs()[0]>0 and all(c>=0 for c in sp.Poly(sp.expand(den.subs(k,t+7)),t).all_coeffs())
print('PASS')
