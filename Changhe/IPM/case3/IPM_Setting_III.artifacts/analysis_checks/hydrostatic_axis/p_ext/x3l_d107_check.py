# hand-check of the external d = 107 certificate (x3l answer, 18:07Z) (lead)
import sympy as sp
n,v=sp.symbols('n v')
f=749*n**4+88168*n**3+2994312*n**2+22061260*n-25153453
z=(107+2*n)/(106+2*n); r=z*(1-sp.Rational(13)/n)
s=-(1+18*r)/44; p=(1+18*r**2+44*s**2)/88
pi=(v-r)*(v**2-s*v+p)
M1=1+18*r+44*s; M2=1+18*r**2+44*(s**2-2*p); M3=1+18*r**3+44*(s**3-3*s*p)
dz=sp.diff(pi,v).subs(v,z)
print('M1',sp.simplify(M1),'M2',sp.simplify(M2))
print('pi_prime(z) - 9f/(3872 n^2 (n+53)^2):',sp.simplify(dz-9*f/(3872*n**2*(n+53)**2)))
print('A7 identity:',sp.simplify(M3*z-107*r*p-11*(2*n+107)/(n+53)**2*dz))
print('f(1)',f.subs(n,1),'f(1001/1000)',f.subs(n,sp.Rational(1001,1000)))
print('f_prime coeffs',sp.Poly(sp.diff(f,n),n).all_coeffs())
n0=sp.nsolve(f,n,1.0003); print('n0',n0,'r',r.subs(n,n0),'disc s^2-4p',(s**2-4*p).subs(n,n0))
