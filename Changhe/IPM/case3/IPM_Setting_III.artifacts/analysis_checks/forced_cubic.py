# Cubic jet of the forced problem W.grad rho - rho = mu y phi(r), phi = (1 + r^2/L^2)^-2 (num lane's forcing).
import sympy as sp
x,y,cl,c,a0,b,e,q1,q2,mu,L,H=sp.symbols('x y c_l c a0 b e q1 q2 mu L H')
rho=a0*y+b*x**2*y+e*y**3
psi=c*x*y+q1*x**3*y+q2*x*y**3
U1=-sp.diff(psi,y); U2=sp.diff(psi,x)
R=(cl*x+U1)*sp.diff(rho,x)+(cl*y+U2)*sp.diff(rho,y)-rho
F=mu*y*sp.series((1+(x**2+y**2)/L**2)**-2,x,0,4).removeO()
F=sp.expand(sp.series(F,y,0,4).removeO())
E=sp.Poly(sp.expand(R-F),x,y)
eqs={m:E.coeff_monomial(m) for m in [y, x**2*y, y**3]}
for k,v in eqs.items(): print(k,':',sp.factor(v))
# Delta = c_l + c - 1 = mu/a0 from linear order; Poisson q1+q2=-b/3; H = q1-q2
D=sp.symbols('Delta')
sol=sp.solve([eqs[x**2*y].subs({c:1+D-cl}), q1+q2+b/3, q1-q2-H],[b,q1,q2],dict=True)[0]
A=2*cl-1
print('b =',sp.factor(sol[b]))
print('check against (3 a0 H + 4 mu/L^2)/(a0 - 4A + 2 Delta):',
      sp.simplify(sol[b]-(3*a0*H+4*mu/L**2)/(a0-4*A+2*D)))
