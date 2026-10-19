# Symbolic checks of signs, kernels and the compatibility identity for IPM Setting I.
import sympy as sp
x,y,r,t,cl,c=sp.symbols('x y r theta c_l c',real=True)
G=-sp.log(sp.sqrt(x**2+y**2))/(2*sp.pi)
# psi = d_x G * rho ; U = (-psi_y, psi_x)  =>  kernels of U are (-d_x d_y G, d_x^2 G)
K1=sp.simplify(-sp.diff(G,x,y)); K2=sp.simplify(sp.diff(G,x,2))
print('K1 =',K1,'  K2 (PV part) =',K2)
# third derivative kernel for psi_xy(0)
K3=sp.simplify(sp.diff(G,x,2,y))
print('d_x^2 d_y G =',sp.factor(K3))
# polar: y(3x^2-y^2)=r^3 sin 3theta
print(sp.simplify((y*(3*x**2-y**2)).subs({x:r*sp.cos(t),y:r*sp.sin(t)})-r**3*sp.sin(3*t)))
# leading-order compatibility: rho=x^2 y, U=(-c x, c y)
rho=x**2*y; W=(cl*x-c*x, cl*y+c*y)
print('transport of x^2y:',sp.factor(W[0]*sp.diff(rho,x)+W[1]*sp.diff(rho,y)))
# x^2 y in polar
print(sp.simplify(sp.expand_trig((x**2*y).subs({x:r*sp.cos(t),y:r*sp.sin(t)})-r**3*(sp.sin(t)+sp.sin(3*t))/4)))
# exponents at the saddle: rho ~ y^j |x|^p with lambda1 p + lambda2 j = 1
l1=1-2*cl; l2=4*cl-1
for j in [1,3,5]:
    print('j=',j,' p_j =',sp.simplify((1-l2*j)/l1))
# int_0^pi cos^2 sin * sin3 dtheta
print(sp.integrate(sp.cos(t)**2*sp.sin(t)*sp.sin(3*t),(t,0,sp.pi)))
