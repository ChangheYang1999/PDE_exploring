"""Independent symbolic check of the moving-center reduction (PROMPT sections 1-2).
Independent verifier. Uses sympy only."""
import sympy as sp

t = sp.symbols('t')
z1, z2 = sp.symbols('z1 z2', real=True)
Cr = sp.Function('Cr')(t); Cl = sp.Function('Cl')(t)
Z1s = sp.Function('Z1s')(t); Z2s = sp.Function('Z2s')(t)
x, y = sp.symbols('x y', real=True)
rho = sp.Function('rho'); psi = sp.Function('psi')

X = Cl*(z1 - Z1s); Y = Cl*(z2 - Z2s)
vr = Cr*rho(X, Y)
Psi = Cr/Cl*psi(X, Y)
u1 = -sp.diff(Psi, z2); u2 = sp.diff(Psi, z1)
transport = sp.diff(vr, t) + u1*sp.diff(vr, z1) + u2*sp.diff(vr, z2)
poisson = -(sp.diff(Psi, z1, 2) + sp.diff(Psi, z2, 2)) - sp.diff(vr, z1)

# substitute ODEs: Cr' = -Cr^2 Cl ; Cl' = c_l Cr Cl^2 ; Z*' = Cr U(0)
cl = sp.symbols('c_l')
U0x, U0y = sp.symbols('U0x U0y')
subs = {sp.Derivative(Cr, t): -Cr**2*Cl, sp.Derivative(Cl, t): cl*Cr*Cl**2,
        sp.Derivative(Z1s, t): Cr*U0x, sp.Derivative(Z2s, t): Cr*U0y}
tr = transport.doit().subs(subs)
# express in profile variables: replace z1 -> Z1s + x/Cl etc.
tr = tr.subs({z1: Z1s + x/Cl, z2: Z2s + y/Cl})
tr = sp.simplify(tr/(Cr**2*Cl))
po = sp.simplify(poisson.doit().subs({z1: Z1s + x/Cl, z2: Z2s + y/Cl})/(Cr*Cl))
print('transport / (Cr^2 Cl) =', tr)
print('poisson / (Cr Cl) =', po)

# expected profile operator
r = rho(x, y); p = psi(x, y)
Ux = -sp.diff(p, y); Uy = sp.diff(p, x)
expected = (cl*x + Ux - U0x)*sp.diff(r, x) + (cl*y + Uy - U0y)*sp.diff(r, y) - r
print('transport + (expected) simplifies to:', sp.simplify(tr.doit() + expected))  # note sign: tr = -R ?
print('transport - (expected) simplifies to:', sp.simplify(tr.doit() - expected))
