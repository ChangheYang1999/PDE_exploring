# Lead check of the verifier's positive polar formula (1) for ||D^k f||^2 on an annulus.
import sympy as sp, mpmath as mp
x,y,t,z=sp.symbols('x y t z',real=True)
r=sp.sqrt(x**2+y**2)
def P(k,j,n,zz):
    e=1
    for i in range(j): e*=(zz+1-n-2*i)
    for h in range(k-j): e*=(zz+1+n-2*h)
    return e
def check(dfun,k,a,b):
    # f = r sum d_n(t) sin(n th), d_n given as functions of t (sympy)
    th=sp.atan2(y,x)
    f=0
    for n,d in dfun.items():
        f+= r*d.subs(t,sp.log(r))*sp.sin(n*th)
    f=sp.simplify(sp.expand_trig(f)) if False else f
    tot=0
    for j in range(k+1):
        der=sp.diff(f,x,j,y,k-j) if j>0 and k-j>0 else (sp.diff(f,x,k) if j==k else sp.diff(f,y,k))
        tot+=sp.binomial(k,j)*der**2
    F=sp.lambdify((x,y),tot,'mpmath')
    mp.mp.dps=20
    lhs=mp.quad(lambda rr,ph: F(rr*mp.cos(ph),rr*mp.sin(ph))*rr,[a,b],[0,2*mp.pi])
    # rhs
    s=0
    for n,d in dfun.items():
        for j in range(k+1):
            # P(E) d with E = d/dt
            Pz=sp.Poly(sp.expand(P(k,j,n,z)),z)
            expr=sum(c*sp.diff(d,t,m) for (m,),c in Pz.terms())
            s+=sp.binomial(k,j)*expr**2
    G=sp.lambdify(t,sp.exp((4-2*k)*t)*s,'mpmath')
    rhs=mp.pi/2**k*mp.quad(G,[mp.log(a),mp.log(b)])
    return lhs,rhs
d={1:2+sp.exp(2*t)/(1+sp.exp(2*t)), 3:sp.exp(2*t)*sp.cos(t), 4:sp.exp(t)/3}
for k in (1,2,3):
    l,rr=check(d,k,0.5,1.7); print(k,l,rr,abs(l-rr)/abs(l))
