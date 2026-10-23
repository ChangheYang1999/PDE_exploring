# N = 3 analogue of A.3.63: modes 1,3,5 inside, E1 = E3 = E5 = 0; linearization at Y0 and order-j matrices
import sympy as sp
c,a,H,z=sp.symbols('c a H z',positive=True)
lam=sp.symbols('lam')
D=c-1; M=a/4-D
# order-j coefficient system from the dot-form equations (dot = 2 z d/dz, so dot z^j = lam z^j, lam = 2j)
f1,g1,k1=sp.symbols('f_j g_j k_j')
def lin(lam):
    # first-order variations at Y0 of f,g,k with z^j dependence; moments: T_j = -g/lam, S_j = -k/(lam-2), J_j = f/(lam+4),
    # K_j = g/(lam+6), L_j = k/(lam+8)
    f0,g0,k0,T0,S0,J0,K0,L0=a,0,M,0,a/4,0,0,0
    e=sp.symbols('e')
    f=f0+e*f1; g=e*g1; k=e*k1; T=M+e*(-g1/lam); S=e*(-k1/(lam-2)); J=a/4+e*f1/(lam+4); K=e*g1/(lam+6); L=e*k1/(lam+8)
    fd=e*lam*f1; gd=e*lam*g1; kd=e*lam*k1
    u=(T-J)/2; B=-u-K+S; C=K-sp.Rational(3,2)*L-S
    F1=(D+T)*f-f**2/4+f*g/2+(-J+2*K+4*S-2*T)*g+(-4*K+6*L-6*S)*k+g*k/2
    F3=(J+2*S)*f-f**2/4-f*g/2+(D+3*L)*g+(-2*J-3*T+f+g/2)*k
    E1=(c+u)*fd+B*gd+C*kd+F1
    E3=B*fd+(c-sp.Rational(3,2)*L)*gd-u*kd+F3
    E5=c*kd+D*k+C*fd-u*gd+(2*J+T)*g+2*K*f-f*g-f*k/2-sp.Rational(3,4)*g**2
    rows=[sp.expand(sp.diff(E,e).subs(e,0)) for E in (E1,E3,E5)]
    A=sp.Matrix([[sp.simplify(r.coeff(v)) for v in (f1,g1,k1)] for r in rows])
    return A
A=lin(lam)
print('A_3(lam) ='); sp.pprint(A.applyfunc(sp.factor))
d=sp.factor(sp.simplify(A.det()))
print('det A_3 =',d)
I=a**2-4*((c+2)*lam-D)*a+4*(c**2+4*c-1)*lam**2-8*D*(c-3)*lam
print('det A_3 / I =',sp.factor(sp.simplify(d/I*16)))
Mat3=sp.Matrix([[c-D/2,D/2,0],[D/2,c,D/2],[0,D/2,c]])
print('det Mat3 =',sp.factor(sp.expand(Mat3.det())), ' in D:',sp.expand((Mat3.det()*8).subs(c,sp.Symbol('Dd')+1)))
