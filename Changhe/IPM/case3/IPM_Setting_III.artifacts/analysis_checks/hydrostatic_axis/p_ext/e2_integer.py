# e=2, A0=1 (forced by the single-exceptional-node lemma): real node a (weight 2nu), conjugate pair (weight 2mu each).
# For integers n, nu, mu: r = D/(D-1), D = m + 2n, m = 1 + 2nu + 4mu; a = r(1 - (mu-nu)/n);
# M1, M2 give S = sum of pair, T' = product of pair; condition pi'(r) = 0.
import sympy as sp
n,nu,mu=sp.symbols('n nu mu',positive=True)
m=1+2*nu+4*mu; D=m+2*n; r=D/(D-1)
a=r*(1-(mu-nu)/n)
S=-(1+2*nu*a)/(2*mu)
Tp=(1+2*nu*a**2+2*mu*S**2)/(4*mu)
pp=3*r**2-2*(S+a)*r+Tp+a*S
num,den=sp.fraction(sp.together(sp.simplify(pp)))
num=sp.factor(num); print('num =',num); print('den =',sp.factor(den))
