# check: for homogeneous H of degree n (odd in y, even in x), int_circle H_xx sin = (n+1)((n+3)M - C)
import sympy as sp
x,y,t=sp.symbols('x y t',real=True)
ok=0
for n in [3,5,7,9]:
    for k in range(1,n+1,2):
        H=x**(n-k)*y**k
        f=H.subs({x:sp.cos(t),y:sp.sin(t)})
        C=sp.integrate(sp.expand(f*sp.sin(t)),(t,0,2*sp.pi))
        M=sp.integrate(sp.expand(f*sp.cos(t)**2*sp.sin(t)),(t,0,2*sp.pi))
        Hxx=sp.diff(H,x,2).subs({x:sp.cos(t),y:sp.sin(t)})
        I=sp.integrate(sp.expand(Hxx*sp.sin(t)),(t,0,2*sp.pi))
        assert sp.simplify(I-(n+1)*((n+3)*M-C))==0,(n,k)
        ok+=1
print('pass',ok)
