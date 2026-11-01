# Lead check of verifier topic 123: inf_{k>=2}|sigma_k(b)| = -sigma_4(b), attained only at k=4, at both real roots of P6.
# Uses the lead's own symbolic responses (sigma_check.json). For k>=7: sigma_4(b)*den(k) - num(k,b) has positive
# t-coefficients (k=t+7) on the isolating interval, so sigma_k < sigma_4 < 0.
import json, sympy as sp
b,k,t=sp.symbols('b k t')
d=json.load(open('sigma_check.json'))
num=sp.sympify(d['generic_sigma_numerator']); den=sp.sympify(d['generic_sigma_denominator'])
P6=176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936
roots=sp.Poly(P6,b).intervals(eps=sp.Rational(1,10**40))
def bound(poly_b,lo,hi,low=True):
    P=sp.Poly(sp.expand(poly_b),b); s=0
    for (e,),c in P.terms():
        s+=(min if low else max)(c*lo**e,c*hi**e)
    return s
small={int(kk):sp.sympify(v) for kk,v in d['sigma_small_k'].items()}
for ir,((lo,hi),m) in enumerate(roots):
    assert lo>0
    s4=sp.expand(small[4])
    U4=bound(s4,lo,hi,False); L4=bound(s4,lo,hi,True)
    assert U4<0
    print('root %d: sigma_4 in [%.20e, %.20e]'%(ir+1,float(L4),float(U4)))
    for kk in (2,3,5,6):
        s=sp.expand(small[kk]); L=bound(s,lo,hi); U=bound(s,lo,hi,False)
        gap=(bound(s+s4,lo,hi) if L>0 else bound(s4-s,lo,hi))
        assert (L>0 or U<0) and gap>0
        print('  k=%d sigma in [%.6e, %.6e], |sigma_k|-|sigma_4| >= %.3e'%(kk,float(L),float(U),float(gap)))
    Dt=sp.Poly(sp.expand(den.subs(k,t+7)),t); assert all(c>0 for c in Dt.all_coeffs())
    Pt=sp.Poly(sp.expand((s4*den-num).subs(k,t+7)),t)
    lows=[bound(c,lo,hi) for c in Pt.all_coeffs()]
    print('  k>=7: degree %d, %d coefficients, min lower bound %.4e, all >0: %s'%(Pt.degree(),len(lows),float(min(lows)),all(x>0 for x in lows)))
    assert all(x>0 for x in lows)
print('PASS: inf_k |sigma_k| = -sigma_4 at both roots, attained only at k=4')
