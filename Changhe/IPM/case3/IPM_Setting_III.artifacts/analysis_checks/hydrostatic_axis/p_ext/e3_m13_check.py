# check of the external e = 3, m = 13, (A_0, mu) = (1, (2, 2, 1, 1)) exclusion (lead hand-check)
import sympy as sp
n,p,h,q,j,r,X=sp.symbols('n p h q j r X')
D=2*n+13; rr=D/(D-1)
assert sp.simplify(13/rr-1/(rr-1)+2*n/rr)==0
U=X**2-p*X+q; V=X**2-h*X+j
# U'/U = -n/r and V'/V = n/r at X = r solved for q and j
qs=sp.solve(sp.Eq(sp.diff(U,X).subs(X,r)*r,-n*U.subs(X,r)),q)[0]
js=sp.solve(sp.Eq(sp.diff(V,X).subs(X,r)*r,n*V.subs(X,r)),j)[0]
print(sp.simplify(qs-((n+1)*p*r-(n+2)*r**2)/n), sp.simplify(js-((2-n)*r**2+(n-1)*h*r)/n))
# (Z): 1/(r-1) + 4 U'/U + 2 V'/V = 13/r holds with these
Z=1/(r-1)+4*(-n/r)+2*(n/r)-13/r
print(sp.simplify(Z.subs(r,rr)))
hs=-2*p-sp.Rational(1,2)
M2=1+4*(p**2-2*qs)+2*(hs**2-2*js.subs(h,hs))
E=sp.factor(sp.together(M2.subs(r,rr)*2*n*(n+6)**2))
print(E)
target=24*n*(n+6)**2*p**2+(8*n**3+64*n**2-112*n-1248)*p+31*n**3+410*n**2+1436*n+520
print(sp.simplify(sp.together(M2.subs(r,rr))*2*n*(n+6)**2-target))
disc=sp.factor(sp.discriminant(target,p)); print(disc)
print(sp.expand(disc+32*(n+6)**2*(91*n**4+1222*n**3+4404*n**2+1768*n-1352)))
