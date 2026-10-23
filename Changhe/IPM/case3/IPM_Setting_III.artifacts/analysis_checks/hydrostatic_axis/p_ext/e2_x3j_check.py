# hand-check of the external identity (1) and expansion (8) for e = 2 (lead)
import sympy as sp
n,nu,mu,k,t=sp.symbols('n nu mu k t')
m=1+2*nu+4*mu; D=m+2*n; r=D/(D-1)
a=r*(1-(mu-nu)/n); S=-(1+2*nu*a)/(2*mu); Tp=(1+2*nu*a**2+2*mu*S**2)/(4*mu)
E=3*r**2-2*(S+a)*r+Tp+a*S
den=8*mu**2*n**2*(2*mu+n+nu)**2
num=sp.expand(sp.cancel(E*den))
A=n**2*(2*nu+2*n+2*k+1); B=4*n*(k**2+3*n*k+2*n*(n+nu))
C=4*(4*n-nu)*k**3+4*n*(14*n+3*nu)*k**2+64*n**2*(n+nu)*k+24*n**2*(n+nu)**2
Q=C+B*t+A*t**2
Dk=6*nu+6*n+4*k+1
print('D check',sp.expand(D.subs(mu,nu+n+k)-Dk))
print('identity (1):',sp.simplify(num.subs(mu,nu+n+k)-Dk**2/4*Q.subs(t,(Dk-1)/Dk)))
Q8=(4*(4*n-nu)*k**3+4*n*(14*n+3*nu+t)*k**2+2*n**2*(32*n+32*nu+t**2+6*t)*k
    +n**2*(24*(n+nu)**2+(2*n+2*nu+1)*t**2+8*(n+nu)*t))
print('expansion (8):',sp.expand(Q-Q8))
