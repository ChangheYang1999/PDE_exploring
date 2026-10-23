# pattern (A_0, (2, 2, 1, 1)), e = 3, m = A_0 + 12: the method of the external m = 13 proof for general odd A_0
import sympy as sp, sys
n,p,h,q,j,r,X=sp.symbols('n p h q j r X')
for A0 in [int(x) for x in sys.argv[1].split(',')]:
    m=A0+12; D=2*n+m; rr=D/(D-1); T=A0*D-m
    assert sp.simplify(m/rr-A0/(rr-1)+T/rr)==0
    # (X): U'/U + V'/V = 0; g(u_*) = 0: A0/(r-1) + 4U'/U + 2V'/V = m/r  =>  U'/U = -T/(2r), V'/V = T/(2r)
    U=X**2-p*X+q; V=X**2-h*X+j
    qs=sp.solve(sp.Eq(2*sp.diff(U,X).subs(X,r)*r,-T*U.subs(X,r)),q)[0]
    js=sp.solve(sp.Eq(2*sp.diff(V,X).subs(X,r)*r,T*V.subs(X,r)),j)[0]
    hs=sp.solve(A0+4*p+2*h,h)[0]
    M2=A0+4*(p**2-2*qs)+2*(hs**2-2*js.subs(h,hs))
    E=sp.factor(sp.numer(sp.together(M2.subs(r,rr))))
    Pp=sp.Poly(E,p); disc=sp.factor(sp.discriminant(Pp.as_expr(),p))
    print('A0',A0,'M2 numerator',E); print('  deg_p',Pp.degree(),'disc',disc)
    # real roots of the discriminant in n
    for f,k in sp.factor_list(disc)[1]:
        if sp.Poly(f,n).degree()>0: print('  factor',f,'real roots',[float(x) for x in sp.real_roots(sp.Poly(f,n))])
