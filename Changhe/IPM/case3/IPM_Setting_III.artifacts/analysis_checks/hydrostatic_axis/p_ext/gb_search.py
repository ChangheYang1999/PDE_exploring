# Exceptional case of the finite polynomial axis class for P = (m+2)/2 (m odd):
# unknown odd F (deg m) and odd A (deg <= m+2) with A*D = F*Q, D = w F' + m t F, Q = 1 + (2P-1) t^2,
# and w A' + 2 P t A = 0 at t^2 = -1/(2P-1); F(1) != 0 by saturation.
import sympy as sp, sys
t=sp.symbols('t')
for m in [int(a) for a in sys.argv[1:]]:
    P=sp.Rational(m+2,2); w=1-t**2; Q=1+(2*P-1)*t**2
    fs=sp.symbols('f1:%d'%(m+2))[0::2]; as_=sp.symbols('a1:%d'%(m+4))[0::2]
    F=sum(f*t**(2*i+1) for i,f in enumerate(fs)); A=sum(a*t**(2*i+1) for i,a in enumerate(as_))
    D=sp.expand(w*sp.diff(F,t)+m*t*F)
    eqs=sp.Poly(sp.expand(A*D-F*Q),t).coeffs()
    cond=sp.expand(w*sp.diff(A,t)+2*P*t*A).subs(t**2,sp.Symbol('u')) if False else None
    E=sp.expand(w*sp.diff(A,t)+2*P*t*A)  # even polynomial
    u=sp.Symbol('u'); Eu=sp.Poly(E,t); 
    val=sum(c*(-1/(2*P-1))**(mon[0]//2) for mon,c in zip(Eu.monoms(),Eu.coeffs()))
    z=sp.Symbol('z')
    G=sp.groebner(list(eqs)+[sp.expand(val), sp.expand(z*F.subs(t,1)-1)],*( [z]+list(fs)+list(as_)),order='lex')
    print('m',m,'P',P,'groebner:',list(G)[:3] if len(G)<=3 else len(G), flush=True)
