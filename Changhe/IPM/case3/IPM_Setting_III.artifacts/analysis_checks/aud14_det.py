# check of the claim det(j Id - DPhi_Y(0,Y0)) = j (j+2)(j+3) I(a,2j) / (16 (c^2+4c-1))
import sympy as sp
c,a,z,H,j=sp.symbols('c a z H j')
f,g,T,J,K=sp.symbols('f g T J K')
D=c-1; M=a/4-D; S=H*z; L=0; k=0
u=(T-J)/2; B=-u-K+S
F1=(D+T)*f-f**2/4+f*g/2+(-J+2*K+4*S-2*T)*g+(-4*K+6*L-6*S)*k+g*k/2
F3=(J+2*S)*f-f**2/4-f*g/2+(D+3*L)*g+(-2*J-3*T+f+g/2)*k
Mat=sp.Matrix([[c+u,B],[B,c]])
fg=-sp.Rational(1,2)*Mat.inv()*sp.Matrix([F1,F3])
Phi=sp.Matrix([fg[0],fg[1],-g/2,(f-4*J)/2,(g-6*K)/2])
Y=[f,g,T,J,K]; Y0={f:a,g:0,T:M,J:a/4,K:0,z:0}
assert all(sp.simplify(x.subs(Y0))==0 for x in Phi)
Mlin=Phi.jacobian(Y).subs(Y0).applyfunc(sp.simplify)
d=sp.factor(sp.simplify((j*sp.eye(5)-Mlin).det()))
lam=2*j
I=a**2-4*((c+2)*lam-D)*a+4*(c**2+4*c-1)*lam**2-8*D*(c-3)*lam
print(d)
print('identity:',sp.simplify(d-j*(j+2)*(j+3)*I/(16*(c**2+4*c-1)))==0)
