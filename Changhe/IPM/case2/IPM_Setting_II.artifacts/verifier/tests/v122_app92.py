# sympy checks for the FR 9.2 draft (FR_app9_2_draft.md, sha a68f2867380e56fb)
import sympy as sp
a,b,c,om,ph,l,s,L,Th,R,Vr,Vt,a0=sp.symbols('a b c omega phi l s L Theta R V_r V_t a0',real=True)
# Step 2: traceless DW with curl omega is determined by DW E and omega, linear map of norm <= C
D=sp.Matrix([[a,b],[b+om,-a]]); E=sp.Matrix([sp.cos(ph),sp.sin(ph)])
w=D*E; sol=sp.solve([w[0]-sp.Symbol('w0'),w[1]-sp.Symbol('w1')],[a,b],dict=True)[0]
print('step2 solvable for all phi:', sp.simplify(sp.Matrix([[sp.cos(ph),sp.sin(ph)],[-sp.sin(ph),sp.cos(ph)]]).det())==1, sol)
# Step 4: det(lF,F') with F=L e_Theta(a), and det(V, R J e_a) = R V_r
La=sp.Function('L')(a0); Ta=sp.Function('T')(a0)
F=sp.Matrix([La*sp.cos(Ta),La*sp.sin(Ta)]); Fp=F.diff(a0)
print('step4 det(lF,Fp)-l L^2 Theta\' =', sp.simplify(sp.Matrix.hstack(l*F,Fp).det()-l*La**2*Ta.diff(a0)))
ea=sp.Matrix([sp.cos(a0),sp.sin(a0)]); Jea=sp.Matrix([-sp.sin(a0),sp.cos(a0)])
V=Vr*ea+Vt*Jea
print('step4 det(V,R J e_a)-R V_r =', sp.simplify(sp.Matrix.hstack(V,R*Jea).det()-R*Vr))
# exponents: p=1/l, lambda=l-1
p=1/l
print('(1-p)l-lambda:', sp.simplify((1-p)*l-(l-1)))
print('step5 grad: (1-l)s vs (p-1)ls:', sp.simplify((1-l)-(p-1)*l))
print('step6 e^s = e^{pls}:', sp.simplify(p*l-1))
print('step7 D2rho exponent (1-2l)/l vs p-2:', sp.simplify((1-2*l)/l-(p-2)))
print('step7 forcing e^{ls} r^{p-2} -> exponent l+(p-2)l vs -lambda:', sp.simplify(l+(p-2)*l+(l-1)))
# Step 7: f=e^{-s}rho(e^{ls}Z) with profile eq => d_tau f + u.grad f = 0, tau'(s)=e^{-lambda s}
tau=(1-sp.exp(-(l-1)*s))/(l-1)
print('dtau/ds - e^{-lambda s}:', sp.simplify(sp.diff(tau,s)-sp.exp(-(l-1)*s)))
# Step 2 iteration: sum_n 4^{-n} 2^{n+2} finite
n=sp.symbols('n',integer=True,nonnegative=True)
print('sum 4^-n 2^(n+2) =', sp.summation(sp.Rational(1,4)**n*2**(n+2),(n,0,sp.oo)))
