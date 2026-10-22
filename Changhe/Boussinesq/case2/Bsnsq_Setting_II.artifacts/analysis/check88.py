# Symbolic checks for Theorem 88 (energy flux identity with pressure). Single-threaded sympy.
import sympy as sp
x,y,b=sp.symbols('x y beta',real=True)
Psi=sp.Function('Psi')(x,y); Th=sp.Function('Theta')(x,y); Pi=sp.Function('Pi')(x,y)
U=sp.Matrix([-sp.diff(Psi,y),sp.diff(Psi,x)]); X=sp.Matrix([x,y]); W=b*X+U
Om=-(sp.diff(Psi,x,2)+sp.diff(Psi,y,2))
g=lambda f: sp.Matrix([sp.diff(f,x),sp.diff(f,y)])
adv=lambda V,f: V[0]*sp.diff(f,x)+V[1]*sp.diff(f,y)
rcurl=lambda V: sp.diff(V[0],y)-sp.diff(V[1],x)
div=lambda V: sp.diff(V[0],x)+sp.diff(V[1],y)
ok=0
# 1. rcurl U = Omega; rcurl(A + Theta e2) = W.grad Omega + Omega - Theta_x  (A = W.grad U + (1-beta) U)
assert sp.simplify(rcurl(U)-Om)==0; ok+=1
A=sp.Matrix([adv(W,U[0]),adv(W,U[1])])+(1-b)*U
assert sp.expand(rcurl(A+sp.Matrix([0,Th]))-(adv(W,Om)+Om-sp.diff(Th,x)))==0; ok+=1
# 2. div(W e + Pi U) - (4 beta - 2) e = U.M + y T  for arbitrary Psi, Theta, Pi, where
#    M = W.grad U + (1-beta) U + grad Pi + Theta e2 (residual of (88.2)), T = W.grad Theta - (beta-2) Theta (residual of (T))
e=(U[0]**2+U[1]**2)/2+y*Th
M=A+g(Pi)+sp.Matrix([0,Th]); T=adv(W,Th)-(b-2)*Th
lhs=div(W*e+Pi*U)-(4*b-2)*e
assert sp.expand(lhs-(U.dot(M)+y*T))==0; ok+=1
# 3. local expansions at O: Psi = c x y + quartic odd-odd terms, Theta = a0 x^2 y + quintic, c = 2 beta + 2
c=2*b+2; p1,p2,a0,t1,t2,t3=sp.symbols('p1 p2 a0 t1 t2 t3',real=True)
Psi0=c*x*y+p1*x**3*y+p2*x*y**3; Th0=a0*x**2*y+t1*x**4*y+t2*x**2*y**3+t3*y**5*0
U0=sp.Matrix([-sp.diff(Psi0,y),sp.diff(Psi0,x)]); W0=b*X+U0
A0=sp.Matrix([adv(W0,U0[0]),adv(W0,U0[1])])+(1-b)*U0
G=-(A0+sp.Matrix([0,Th0]))   # = grad Pi; keep terms of degree 1
G1=[sp.Poly(sp.expand(G[i]),x,y) for i in range(2)]
lin=[sum(cf*x**m[0]*y**m[1] for m,cf in G1[i].terms() if sum(m)==1) for i in range(2)]
assert sp.expand(lin[0]+(c**2-c)*x)==0 and sp.expand(lin[1]+(c**2+c)*y)==0; ok+=1
Pi2=-((c**2-c)*x**2+(c**2+c)*y**2)/2
r,ph,R=sp.symbols('r phi R',positive=True)
pol={x:r*sp.cos(ph),y:r*sp.sin(ph)}
e2=sp.expand(((U0[0]**2+U0[1]**2)/2).subs({p1:0,p2:0}))   # quadratic part of e
Ur=sp.expand((U0[0]*sp.cos(ph)+U0[1]*sp.sin(ph)).subs({p1:0,p2:0}).subs(pol))
F4=sp.integrate(sp.integrate(e2.subs(pol)*r,(ph,0,sp.pi/2)),(r,0,R))
assert sp.simplify(F4-sp.pi*c**2*R**4/16)==0; ok+=1
Q4=sp.integrate(sp.expand((e2+Pi2).subs(pol)*Ur).subs(r,R)*R,(ph,0,sp.pi/2))
assert sp.simplify(Q4+sp.pi*c**2*R**4/8)==0; ok+=1
assert sp.simplify(sp.expand((e2+Pi2).subs(pol))-c*r**2*sp.cos(2*ph)/2)==0; ok+=1
# 4. 4 beta - 2 = beta n with n = 4 - 2/beta
assert sp.simplify(4*b-2-b*(4-2/b))==0; ok+=1
print('PASS',ok)
