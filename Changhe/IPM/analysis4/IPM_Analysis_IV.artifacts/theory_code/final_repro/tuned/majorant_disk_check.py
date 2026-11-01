# Independent check of the explicit majorant disk of verifier topic 120 (lead review), exact rational arithmetic.
import sympy as sp
z,W,U,V,E=sp.symbols('z W U V E')
a=sp.Integer(2); kap=sp.Integer(10); sig=sp.Rational(1,100000)
d=sp.Rational(3,2)*kap*a**2; e=3*kap*a*d
P=a*z+d*z**2+e*z**3
h=sp.Rational(3,2)
Phi=[h*kap*(d**2+2*a*e+2*d*e*z+e**2*z**2)+3*kap*P*W+h*kap*z**4*W**2+kap*E*(P+z**4*W),
     h*kap*(2*d*e+e**2*z)+3*kap*sp.expand(P/z)*W+h*kap*z**3*W**2+kap*z**3*E*W,
     h*kap*(e**2+2*(d+e*z)*W+z**2*W**2)+kap*z**2*E*W+3*kap*a*U,
     (kap/sig)*(3*e*W+h*z*W**2+z*E*W+3*a*V+3*d*U)]
Phi=[sp.expand(f) for f in Phi]
Y=[W,U,V,E]
c=sp.Matrix([f.subs({z:0,W:0,U:0,V:0,E:0}) for f in Phi])
J=sp.Matrix([[sp.diff(f,y).subs({z:0,W:0,U:0,V:0,E:0}) for y in Y] for f in Phi])
# Phi(0,Y) must be affine in Y
for f in Phi:
    f0=f.subs(z,0); assert sp.expand(f0-(f0.subs({W:0,U:0,V:0,E:0})+sum(sp.diff(f0,y).subs({W:0,U:0,V:0,E:0})*y for y in Y)))==0
print('d,e',d,e); print('c',list(c)); print('J',J.tolist())
assert J**4==sp.zeros(4,4)
Q=sp.eye(4)+J+J**2+J**3
Y0=Q*c; print('Y0',list(Y0))
Psi=[sp.expand((Phi[i]-c[i]-sum(J[i,j]*Y[j] for j in range(4)))/z) for i in range(4)]
for p in Psi:
    for coef in sp.Poly(p,z,W,U,V,E).coeffs(): assert coef>=0
M=sp.Integer(2)**55; z0=sp.Integer(2)**-120
PsiVal=sp.Matrix([p.subs({z:1,W:2*M,U:2*M,V:2*M,E:2*M}) for p in Psi])
QP=Q*PsiVal
print('max Y0 <= M:',max(Y0)<=M, float(max(Y0)/M))
print('log2 max QPsi:',float(sp.log(max(QP),2)),' need <= 175:',max(QP)<=M*2**120)
# best z0 with this M: z0*max(QP) <= M
print('log2 of largest admissible z0 for M=2^55:', float(sp.log(M/max(QP),2)))
