# Lead hand-check of referee flat1s Sections 6-8 (jet recurrence, Theorem 2, quintic classification).
import sympy as sp
x,y,a,A,t,chi=sp.symbols('x y a A t chi',real=True)
ok=[]
def rec_ok(n,cs,aval,Aval):
    K=(n-1)//2; N=n-1
    H=sum(cs[j]*x**(2*j)*y**(n-2*j) for j in range(K+1))
    V=sp.expand(Aval*x*sp.diff(H,x)+y*sp.diff(H,y)-H)
    # phi = int_0^x V ; check Delta phi = a H_x
    phi=sp.integrate(V,(x,0,x))
    return sp.expand(sp.diff(phi,x,2)+sp.diff(phi,y,2)-aval*sp.diff(H,x))==0
def rec_solution(n,aval,Aval):
    K=(n-1)//2; N=n-1; b=Aval-1
    e=[N+2*b*j for j in range(K+1)]
    c=[None]*(K+1); c[K]=sp.Integer(1)
    for j in range(K-1,-1,-1):
        c[j]=sp.simplify(-(2*j+2)*(2*j+1)*(e[j+1]-aval)*c[j+1]/((n-2*j)*(n-2*j-1)*e[j]))
    return c,e
# (6.2) solutions satisfy the full leading elliptic equation
for n in (3,5,7,9):
    for (aval,Aval) in [(sp.Rational(7,3),sp.Rational(5,2)),(-3,4),(sp.Rational(40),3)]:
        c,e=rec_solution(n,aval,Aval)
        ok.append(('rec',n,aval,Aval,rec_ok(n,c,aval,Aval)))
# (7.5) F_chi spans: compare ratios with recurrence for symbolic a, A
def poch(z,j): return sp.prod([z+i for i in range(j)]) if j>0 else sp.Integer(1)
for n in (3,5,7,9,11):
    K=(n-1)//2; N=n-1; b=A-1; eta=sp.Integer(K)/b; ch=1+(N-a)/(2*b)
    F=[(-1)**j*sp.binomial(2*K+1,2*j)*poch(eta,j)*poch(ch+j,K-j) for j in range(K+1)]
    e=[N+2*b*j for j in range(K+1)]
    good=all(sp.simplify((n-2*j)*(n-2*j-1)*e[j]*F[j]+(2*j+2)*(2*j+1)*(e[j+1]-a)*F[j+1])==0 for j in range(K))
    ok.append(('F_chi',n,good))
    # (7.7) expectation identity: sum (-1)^j C(K,j)(chi+j)_{K-j}(chi+J)_j = 0 for J<K
    for J in range(K):
        s=sum((-1)**j*sp.binomial(K,j)*poch(chi+j,K-j)*poch(chi+J,j) for j in range(K+1))
        ok.append(('7.7',n,J,sp.expand(s)==0))
    # binomial identity
    ok.append(('binom',n,all(sp.simplify(sp.binomial(2*K+1,2*j)-poch(-K,j)*poch(-K-sp.Rational(1,2),j)/(poch(sp.Rational(1,2),j)*sp.factorial(j)))==0 for j in range(K+1))))
# numeric check of (7.6) moments and E F(T0 S0)=0 for a sample
import mpmath as mp; mp.mp.dps=30
for (n,Aval,aval) in [(5,3,5.0),(7,2.5,-4.0),(9,6,30.0)]:
    K=(n-1)//2; N=n-1; b=Aval-1; eta=K/b; ch=1+(N-aval)/(2*b)
    J=next(j for j in range(K) if ch+j>0); u=ch+J
    ET=[mp.quad(lambda s: s**(u-1+j)*(1+s)**(-u-K-1.5),[0,1,mp.inf])/mp.quad(lambda s: s**(u-1)*(1+s)**(-u-K-1.5),[0,1,mp.inf]) for j in range(K+1)]
    if eta>0.5:
        ES=[mp.quad(lambda s: s**(j-0.5)*(1-s)**(eta-1.5),[0,1])/mp.quad(lambda s: s**(-0.5)*(1-s)**(eta-1.5),[0,1]) for j in range(K+1)]
    else: ES=[1]*(K+1)
    F=[(-1)**j*mp.binomial(2*K+1,2*j)*mp.rf(eta,j)*mp.rf(ch+j,K-j) for j in range(K+1)]
    val=sum(F[j]*ET[j]*ES[j] for j in range(K+1)); scale=sum(abs(F[j]*ET[j]*ES[j]) for j in range(K+1))
    ok.append(('EF=0 numeric',n,Aval,aval,float(val/scale)))
# quintic (8.1)-(8.4)
c,e=rec_solution(5,a,A)
P=sp.expand(sum(c[j]*t**j for j in range(3)))
e1=2*A+2;e2=4*A
ok.append(('8.1',sp.simplify(P-(t**2+2*(a-e2)/e1*t+(a-e1)*(a-e2)/(20*e1)))==0))
disc=sp.factor(sp.discriminant(P,t))
ok.append(('8.2',sp.simplify(disc-(a-e2)/(5*e1**2)*((20-e1)*a+e1**2-20*e2))==0))
astar=2*(A**2-18*A+1)/(A-9)
ok.append(('8.3 root',sp.simplify(((20-e1)*a+e1**2-20*e2).subs(a,astar))==0))
ok.append(('astar-e1',sp.simplify(astar-e1+20*(e2-e1)/(e1-20))==0))
ok.append(('astar(11)',astar.subs(A,11)))
# example (8.5)
H5=y*(y**2-x**2/5)**2
V5=sp.expand(11*x*sp.diff(H5,x)+y*sp.diff(H5,y)-H5)
phi6=4*x*y**5-sp.Rational(16,5)*x**3*y**3+sp.Rational(44,125)*x**5*y
ok.append(('8.5 V',sp.expand(V5-(4*y**5-sp.Rational(48,5)*x**2*y**3+sp.Rational(44,25)*x**4*y))==0))
ok.append(('8.5 phi',sp.expand(sp.diff(phi6,x)-V5)==0, sp.expand(sp.diff(phi6,x,2)+sp.diff(phi6,y,2)+76*sp.diff(H5,x))==0))
H6=y**5-sp.Rational(10,31)*x**2*y**3+sp.Rational(5,186)*x**4*y
V6=sp.expand(11*x*sp.diff(H6,x)+y*sp.diff(H6,y)-H6); ph=sp.integrate(V6,(x,0,x))
ok.append(('8.6',sp.expand(sp.diff(ph,x,2)+sp.diff(ph,y,2)+100*sp.diff(H6,x))==0, sp.discriminant(sp.Rational(5,186)*t**2-sp.Rational(10,31)*t+1,t)))
for o in ok: print(o)
