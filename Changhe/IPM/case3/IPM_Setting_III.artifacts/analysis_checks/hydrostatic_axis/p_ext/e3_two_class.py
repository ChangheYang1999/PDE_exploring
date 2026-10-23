# e = 3, two weight classes of two nodes each: (A_0; al/2, al/2, be/2, be/2), m = A_0 + 2 al + 2 be (lead, 2026-10-21).
# Method of the external m = 13 proof: (X) and g(u_*) = 0 give U'/U(r) = -T/((al - be) r), V'/V(r) = T/((al - be) r),
# T = A_0 D - m; M_1 = 0 is linear; M_2 = 0 is then a quadratic in p (necessary conditions only).
import sympy as sp, sys
n,p,h,q,j,r,X=sp.symbols('n p h q j r X')
for spec in sys.argv[1:]:
    A0,al,be=[int(x) for x in spec.split(',')]
    m=A0+2*al+2*be; D=2*n+m; rr=D/(D-1); T=A0*D-m
    U=X**2-p*X+q; V=X**2-h*X+j
    qs=sp.solve(sp.Eq((al-be)*sp.diff(U,X).subs(X,r)*r,-T*U.subs(X,r)),q)[0]
    js=sp.solve(sp.Eq((al-be)*sp.diff(V,X).subs(X,r)*r,T*V.subs(X,r)),j)[0]
    # check (X) and g(u_*) = 0 hold identically with these
    LU=(sp.diff(U,X)/U).subs(X,r).subs(q,qs); LV=(sp.diff(V,X)/V).subs(X,r).subs(j,js)
    assert sp.simplify((LU+LV).subs(r,rr))==0
    assert sp.simplify((A0/(r-1)+al*LU+be*LV-m/r).subs(r,rr))==0
    hs=sp.solve(A0+al*p+be*h,h)[0]
    M2=A0+al*(p**2-2*qs)+be*(hs**2-2*js.subs(h,hs))
    E=sp.factor(sp.numer(sp.together(M2.subs(r,rr))))
    Pp=sp.Poly(E,p); disc=sp.factor(sp.discriminant(Pp.as_expr(),p))
    print('pattern A0=%d weights (%d,%d,%d,%d) m=%d'%(A0,al,al,be,be,m)); print('  M2 numerator',E)
    print('  deg_p',Pp.degree(),'lead',sp.factor(Pp.LC()),'disc',disc)
    for f,k in sp.factor_list(disc)[1]:
        if sp.Poly(f,n).degree()>0:
            c=sp.Poly(f,n).all_coeffs()
            print('  factor',f,'all coeffs same sign' if all(x>0 for x in c) or all(x<0 for x in c) else '',
                  'real roots',[float(x) for x in sp.real_roots(sp.Poly(f,n))])
