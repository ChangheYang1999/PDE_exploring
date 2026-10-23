# Lead checks for draft 3.75: bottom recursion n=1,2 and conjugation; triangular structure n=1,2; frozen symbol.
import sympy as sp
x,y,c,A=sp.symbols('xi y c A',positive=True)
k=sp.Function('k')(x)
zeta=sp.Function('zeta')(x)  # zeta' = 1/k
a0=(2*c-1)*k*zeta
def D(e): return sp.diff(e,x).subs(sp.Derivative(zeta,x),1/k)
# bottom recursion: g = k y + g3 y^3 + g5 y^5, h = h0 + h2 y^2 + h4 y^4, b = b1 y + b3 y^3 + b5 y^5
g3=sp.Function('g3')(x); g5=sp.Function('g5')(x)
h0=a0-c*x
g=k*y+g3*y**3+g5*y**5
h2=sp.diff(k,x)/2; h4=sp.diff(g3,x)/4
h=h0+h2*y**2+h4*y**4
b1=c-D(h0); b3=-sp.diff(h2,x)/3; b5=-sp.diff(h4,x)/5
b=b1*y+b3*y**3+b5*y**5
gx=sp.diff(g,x).subs(sp.Derivative(zeta,x),1/k)
hx=D(h)
res=sp.expand((c*x+h)*gx+b*sp.diff(g,y)-g)
r1=sp.simplify(res.coeff(y,1)); print('y^1 coeff (should be 0 iff boundary law):',sp.simplify(r1))
r3=res.coeff(y,3)
F1=-sp.diff(k,x)**2/2+k*sp.diff(k,x,2)/6
lhs3=a0*sp.diff(g3,x)+(3*b1-1)*g3
print('n=1 recursion residual:',sp.simplify(sp.expand(r3-(lhs3-F1))))
print('b1 - (1 - a0 k\'/k):',sp.simplify(b1-(1-a0*sp.diff(k,x)/k)))
# conjugation u = k^(2n+1) w(zeta): (A zeta d_zeta + 2n) w = F/k^(2n+1)
n=sp.Symbol('n',positive=True,integer=True)
w=sp.Function('w')
u=k**(2*n+1)*w(zeta)
lhs=a0*D(u)+((2*n+1)*b1-1)*u
target=k**(2*n+1)*((2*c-1)*zeta*sp.Subs(sp.diff(w(sp.Symbol('t')),sp.Symbol('t')),sp.Symbol('t'),zeta).doit()+2*n*w(zeta))
print('conjugation residual:',sp.simplify(sp.expand(lhs-target)))
# triangular structure: from axis data G
Y=sp.Symbol('y'); G=sp.Function('G')(Y)
v=G/sp.diff(G,Y); Q=G/sp.diff(G,Y)**2
g2=-sp.diff(v,Y,2)/2
b2=((4*c-1-2*sp.diff(v,Y))*sp.diff(v,Y,2)+v*sp.diff(v,Y,3))/(2*sp.diff(G,Y))
g4=-sp.diff(b2,Y,2)/12
d3=sp.Derivative(G,(Y,3)); d6=sp.Derivative(G,(Y,6))
print('g2 top coeff - Q/2:',sp.simplify(sp.diff(g2,d3)-Q/2), ' order:',max([d.derivative_count for d in g2.atoms(sp.Derivative)]))
print('g4 top coeff - Q^2/24:',sp.simplify(sp.diff(g4,d6)-Q**2/24), ' order:',max([d.derivative_count for d in g4.atoms(sp.Derivative)]))
# frozen symbol on axis
lam,eta,vv,Gp=sp.symbols('lambda eta v Gp',positive=True)
poly=vv*lam**3-lam**2+Gp*eta**2
import mpmath as mp
for et in [1e3,1e5]:
    rts=sp.Poly(poly.subs({vv:2,Gp:sp.Rational(1,3),eta:et}),lam).nroots()
    print(et,[complex(r)/ ( (1/6)**(1/3)*et**(2/3)) for r in rts])
