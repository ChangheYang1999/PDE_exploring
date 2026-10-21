# Lead check of the verifier's result (compact canonical extension): local identities and the separable density formula.
import sympy as sp
x, y, s, A = sp.symbols('x y s A', positive=True)
k = sp.sqrt(2/A); cl = (A+1)/2
h = cl*x + (A/k)*sp.sin(k*x); w = -(A/k)*sp.sin(k*x); g = A*(1-sp.cos(k*x))
psi = h*y; rho = g*y
print('elliptic', sp.simplify(-(sp.diff(psi,x,2)+sp.diff(psi,y,2)) - sp.diff(rho,x)))
U = (-sp.diff(psi,y), sp.diff(psi,x)); W = (cl*x+U[0], cl*y+U[1])
print('transport', sp.simplify(W[0]*sp.diff(rho,x)+W[1]*sp.diff(rho,y)-rho))
print('psi_xy(0) - (3cl-1)', sp.simplify(sp.diff(psi,x,y).subs(x,0)-(3*cl-1)))
print('rho series', sp.series(g, x, 0, 5))
print('local rho from definition', sp.simplify(-sp.integrate(sp.diff(h,s if False else x,2).subs(x,s)*y, (s,0,x)) - (sp.diff(h,x).subs(x,0)-sp.diff(h,x))*y))
# separable formula with generic functions: psi = hb(x) J''(y) + q(x) (H0 J - I J'')
hb, q, J = sp.Function('hb'), sp.Function('q'), sp.Function('J')
H0, I = sp.symbols('H0 I')
f = sp.diff(J(y),y,2); j = H0*J(y) - I*f
P = hb(x)*f + q(x)*j
lap = sp.diff(P,x,2)+sp.diff(P,y,2)
# rho = -int_0^x lap ds; claimed: [H0(1-Q)-hb'+I q']J'' + [I Q - H]J'''' - H0 q' J, with H'=hb, Q'=q, H(0)=Q(0)=0,
# using hb'(0)=H0, q'(0)=0.  Check d/dx of the claim equals -lap and value at x=0 is 0.
H, Q = sp.Function('H'), sp.Function('Q')
claim = (H0*(1-Q(x)) - sp.diff(hb(x),x) + I*sp.diff(q(x),x))*sp.diff(J(y),y,2) + (I*Q(x)-H(x))*sp.diff(J(y),y,4) - H0*sp.diff(q(x),x)*J(y)
dclaim = sp.diff(claim, x).subs({sp.Derivative(Q(x),x): q(x), sp.Derivative(H(x),x): hb(x)})
print('d/dx claim + lap', sp.simplify(dclaim + lap))
at0 = claim.subs(x,0).subs({Q(0):0, H(0):0}).subs({sp.Subs(sp.Derivative(hb(x),x),x,0): H0, sp.Subs(sp.Derivative(q(x),x),x,0): 0})
print('claim at x=0', sp.simplify(at0))
