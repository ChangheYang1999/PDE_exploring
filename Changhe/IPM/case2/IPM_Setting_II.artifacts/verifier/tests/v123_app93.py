# sympy checks for the FR 9.3 draft (FR_app9_3_draft.md, sha cf606fe4528052b6)
import sympy as sp
r,th,p,t,s,a,be,l,lam=sp.symbols('r theta p t s a beta l lambda',positive=True)
A=sp.Function('A')(th); Ps=sp.Function('Psi')(th)
x=r*sp.cos(th); y=r*sp.sin(th)
er=sp.Matrix([sp.cos(th),sp.sin(th)]); et=sp.Matrix([-sp.sin(th),sp.cos(th)])
def polar_div(vr,vt): return sp.diff(r*vr,r)/r+sp.diff(vt,th)/r
def polar_curl(vr,vt): return sp.diff(r*vt,r)/r-sp.diff(vr,th)/r
F=r**p*A
Hr=-r**p*sp.diff(Ps,th); Ht=(p+1)*r**p*Ps
print('div H =',sp.simplify(polar_div(Hr,Ht)))
dxF=sp.cos(th)*sp.diff(F,r)-sp.sin(th)/r*sp.diff(F,th)
ang=sp.diff(Ps,th,2)+(p+1)**2*Ps-((sp.sin(th)*A).diff(th)-(p+1)*sp.cos(th)*A)
print('curl H + d_x F - r^(p-1)*angular_eq =',sp.simplify(polar_curl(Hr,Ht)+dxF-r**(p-1)*ang))
# Q system: Q = Psi' - sin A ; Q' = -lam^2 Psi - lam cos A when the angular eq holds, lam=p+1
Q=sp.diff(Ps,th)-sp.sin(th)*A
Qp=sp.diff(Q,th).subs(sp.Derivative(Ps,(th,2)),-(p+1)**2*Ps+(sp.sin(th)*A).diff(th)-(p+1)*sp.cos(th)*A)
print('Q\' + (p+1)^2 Psi + (p+1) cos A =',sp.simplify(Qp+(p+1)**2*Ps+(p+1)*sp.cos(th)*A))
J=(p+1)*Ps*sp.diff(A,th)-p*sp.diff(Ps,th)*A
print('div(F H) - r^(2p-1) J =',sp.simplify(polar_div(F*Hr,F*Ht)-r**(2*p-1)*J))
print('distributional form - J =',sp.simplify((p+1)*sp.diff(Ps*A,th)-(2*p+1)*sp.diff(Ps,th)*A-J))
kap=(p+1)/p
print('(Psi A^-k)\' + A^(-k-1) J/p =',sp.simplify(sp.diff(Ps*A**(-kap),th)+A**(-kap-1)*J/p))
gradF_H=sp.diff(F,r)*Hr+sp.diff(F,th)/r*Ht
print('gradF.H - r^(2p-1) J =',sp.simplify(gradF_H-r**(2*p-1)*J))
# Step 2: f_t = e^{-pt} rho(e^t X); residual identity
X1,X2=sp.symbols('X1 X2',real=True)
rho=sp.Function('rho'); W1=sp.Function('W1'); W2=sp.Function('W2')
Z1,Z2=sp.exp(t)*X1,sp.exp(t)*X2
f=sp.exp(-p*t)*rho(Z1,Z2)
w1=sp.exp(-p*t)*W1(Z1,Z2); w2=sp.exp(-p*t)*W2(Z1,Z2)
u1,u2=sp.symbols('u1 u2')
g=lambda U1,U2:(1/p*U1+W1(U1,U2))*sp.diff(rho(U1,U2),U1)+(1/p*U2+W2(U1,U2))*sp.diff(rho(U1,U2),U2)-rho(U1,U2)
lhs=sp.diff(f,t)+p*sp.exp(-(1-p)*t)*(w1*sp.diff(f,X1)+w2*sp.diff(f,X2))
res=sp.exp(-p*t)*p*g(u1,u2)
res=res.subs({u1:Z1,u2:Z2})
print('Step 2: d_t f + p e^{-(1-p)t} w.grad f - p e^{-pt} (V.grad rho - rho)(e^t X) =',sp.simplify(sp.expand(lhs-res.doit())))
print('Step 4: p/(1-p) - 1/(l-1) at p=1/l:',sp.simplify((1/l)/(1-1/l)-1/(l-1)))
# Step 5 expansions
q1=2*a*sp.sin(be)*s; q2=a*(2-p)*sp.cos(be)*s**2
P1=sp.integrate(sp.sin(lam*(t-s))*q1/lam,(s,0,t)); P2=sp.integrate(sp.sin(lam*(t-s))*q2/lam,(s,0,t))
print('Psi leading (sin beta != 0):',sp.series(P1,t,0,5).removeO().as_leading_term(t))
print('Psi leading (sin beta = 0):',sp.series(P2,t,0,6).removeO().as_leading_term(t))
At=a*t**2; Ap=2*a*t
qq=sp.sin(be+t)*Ap-p*sp.cos(be+t)*At
print('q expansion:',sp.series(qq,t,0,3))
print('q at sin beta=0 (beta=0):',sp.series(qq.subs(be,0),t,0,3), ' (beta=pi):',sp.series(qq.subs(be,sp.pi),t,0,3))
# Step 6 exponents and Step 7 annular constant
q=sp.symbols('q',positive=True)
print('Step 6 exponent 2+q(2p-1) at q=2:',sp.expand(2+2*(2*p-1)))
print('Step 7 int_1^2 r^(4p-2) r dr =',sp.simplify(sp.integrate(r**(4*p-1),(r,1,2))))
