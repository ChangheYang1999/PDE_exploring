import sympy as sp
th,a,eta=sp.symbols('theta a eta',real=True)
p=sp.Rational(1,2); D=1/p-1
coef={1:a,5:eta}
Theta=sum(c*sp.sin(j*th) for j,c in coef.items())
Psi=0
for m in range(2,12,2):
    am1=coef.get(m-1,0); ap1=coef.get(m+1,0)
    Psi+=(-am1/(2*(m+p+1))+ap1/(2*(m-p-1)))*sp.sin(m*th)
corr=(-p*sp.diff(Psi,th)*Theta+(p+1)*Psi*sp.diff(Theta,th))/D
c3=sp.simplify(sp.integrate(corr*sp.sin(3*th),(th,0,2*sp.pi))/sp.pi)
print('coef sin3:',sp.expand(c3), ' expected', -a**2/28+sp.Rational(67,70)*a*eta)
print('zero at eta =',sp.solve(c3,eta))
# n=1 A_1 check
pp,n=sp.symbols('p n',positive=True)
Dd=1/pp-1
c00=sp.Rational(1,4)*(1-2*(n+1)/((n+pp)+2))
print('A1/a^2 (n=1):',sp.simplify((c00/Dd).subs(n,1)), ' expected', -pp/(4*(pp+3)))
# also check first correction against the recurrence for Theta=a sin(theta): coefficient of sin 3theta
coef1={1:a}
Theta1=a*sp.sin(th); Psi1=-a/(2*(2+pp+1))*sp.sin(2*th)
corr1=(-pp*sp.diff(Psi1,th)*Theta1+(pp+1)*Psi1*sp.diff(Theta1,th))/Dd
c3b=sp.simplify(sp.integrate(sp.expand(sp.expand_trig(corr1))*sp.sin(3*th),(th,0,2*sp.pi))/sp.pi)
print('first correction sin3 coefficient /a^2:',sp.simplify(c3b/a**2))
