# lead hand-check (2026-10-21T18:34Z) of the d = 15 cases (i), (ii) of the checker's result 267, in A.3.80 notation
import sympy as sp
n,p,A,lam,z=sp.symbols('n p A lambda z',positive=True)
# case (i): d = 15, e = 2, A_0 = 1, weights 2 (node a, real) and 6 (pair v^2 - h v + j)
d=15; zz=(2*n+d)/(2*n+d-1); T=2*n
a=zz*(1+sp.Rational(2-6)/T)      # v_1 = z (1 + (A_1 - b)/T)
h=-(1+2*a)/6                     # M_1 = 1 + 2 a + 6 h = 0
j=(1+2*a**2+6*h**2)/12           # M_2 = 1 + 2 a^2 + 6 (h^2 - 2 j) = 0
v=sp.symbols('v'); pi=(v-a)*(v**2-h*v+j)
dp=sp.factor(sp.simplify(sp.diff(pi,v).subs(v,zz)))
print('case (i) pi\'(z) =',dp)
print(sp.simplify(dp-(15*n**4+250*n**3+1227*n**2+1440*n-200)/(8*n**2*(n+7)**2)))
# case (ii) general: A_0 = A, two weight-4 nodes U = v^2 - p v + q, two weight-2 nodes W = v^2 - h v + j, d = A + 12
for Aval,dd in [(1,13),(3,15)]:
    zz=sp.Rational(1)*(2*n+dd)/(2*n+dd-1); T=Aval*(2*n+dd)-dd
    # (alpha - beta) z U'(z) + T U(z) = 0 with alpha - beta = 2; 2 z V'(z) - T V(z) = 0
    q=sp.symbols('q'); jj=sp.symbols('jj')
    hh=-sp.Rational(Aval,2)-2*p          # M_1 = A + 4 p + 2 h = 0
    qs=sp.solve(2*zz*(2*zz-p)+T*(zz**2-p*zz+q),q)[0]
    js=sp.solve(2*zz*(2*zz-hh)-T*(zz**2-hh*zz+jj),jj)[0]
    M2=Aval+4*(p**2-2*qs)+2*(hh**2-2*js)
    num=sp.numer(sp.together(M2)); P_=sp.Poly(sp.expand(num),p)
    disc=sp.factor(P_.discriminant())
    print('A =',Aval,'d =',dd,'deg',P_.degree(),'disc =',disc)
