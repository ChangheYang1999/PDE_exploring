# Check: the first-moment identity of 3.56 holds for every solution of the leading equations
# V_n=(A x d_x+y d_y-1)H_n, Delta V_n=a0 d_xx H_n (no sign condition, no global input).
import sympy as sp, random
x,y,th=sp.symbols('x y th'); random.seed(1)
def mom(P):  # int_0^{2pi} P(cos,sin) dth for a polynomial P, exactly
    return sp.integrate(sp.expand(P.subs({x:sp.cos(th),y:sp.sin(th)})),(th,0,2*sp.pi))
ok=0
for n in [3,5,7,9]:
  for trial in range(3):
    A=sp.Rational(random.randint(11,90),10); a=sp.Rational(random.randint(-90,190),10)
    cs=sp.symbols('c0:%d'%(n//2+1))
    H=sum(cs[i]*x**(2*i)*y**(n-2*i) for i in range(n//2+1))
    V=sp.expand(A*x*sp.diff(H,x)+y*sp.diff(H,y)-H)
    eq=sp.Poly(sp.expand(sp.diff(V,x,2)+sp.diff(V,y,2)-a*sp.diff(H,x,2)),x,y).coeffs()
    M=sp.Matrix([[sp.diff(e,c) for c in cs] for e in eq]); K=M.nullspace()
    assert len(K)==1
    Hs=H.subs(dict(zip(cs,K[0]))); Vs=V.subs(dict(zip(cs,K[0])))
    C=mom(Hs*y); T=mom(Hs*y*x**2)/C
    E=sp.simplify((a-(n-1)*(A-1))*((n+3)*T-1)-(n-1)**2)
    E1=sp.simplify(mom(Vs*y)/C-a/(n-1)*((n+3)*T-1))
    E2=sp.simplify(mom(Vs*y)/C-(n-A+(n+3)*(A-1)*T))
    print(n,A,a,'T=',T,'E=',E,E1,E2); ok+= (E==0 and E1==0 and E2==0)
print('pass',ok)
