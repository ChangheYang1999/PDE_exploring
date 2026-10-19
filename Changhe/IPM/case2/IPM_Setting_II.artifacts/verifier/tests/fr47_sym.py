"""Report Section 4.7(iii) (version of 21:23Z): for A = cos^2 th, Psi_p[A] = -(3p+2)/(4p(p+2)) cos th - cos 3th/(4(p+4)) solves
Psi'' + (p+1)^2 Psi = (sin th A)' - (p+1) cos th A; B_p = J_p[A]/(l-1) = p J_p/(1-p) with J_p = (p+1) Psi A' - p Psi' A equals
sin th cos^2 th [2(p+1) + p(2-p) cos^2 th]/((1-p)(p+4)); the sin 2th coefficient of Psi_{2p-1}[B_p] times (1-p)^2 equals
p(-5p^2+25p+18)/(64 (p+1)(p+4)) -> 19/320 at p = 1 (degree q = 2p-1: Psi'' + (q+1)^2 Psi = (sin th B)' - (q+1) cos th B)."""
import sympy as sp
t, p = sp.symbols('theta p', positive=True)
A = sp.cos(t)**2
Psi = -(3*p + 2)/(4*p*(p + 2))*sp.cos(t) - sp.cos(3*t)/(4*(p + 4))
r1 = sp.simplify(sp.expand_trig(sp.diff(Psi, t, 2) + (p + 1)**2*Psi - (sp.diff(sp.sin(t)*A, t) - (p + 1)*sp.cos(t)*A)))
print('Psi_p ODE residual:', r1)
J = (p + 1)*Psi*sp.diff(A, t) - p*sp.diff(Psi, t)*A
B = sp.simplify(p*J/(1 - p))
Bc = sp.sin(t)*sp.cos(t)**2*(2*(p + 1) + p*(2 - p)*sp.cos(t)**2)/((1 - p)*(p + 4))
print('B_p - claim:', sp.simplify(sp.expand_trig(B - Bc)))
q = 2*p - 1
# solve Psi2'' + (q+1)^2 Psi2 = (sin B)' - (q+1) cos B by Fourier projection on modes 0..6
rhs = sp.expand(sp.expand_trig(sp.diff(sp.sin(t)*Bc, t) - (q + 1)*sp.cos(t)*Bc))
rhs = sp.fu(rhs) if False else rhs
coef = {}
for k in range(0, 7):
    for f in (sp.cos, sp.sin):
        if f is sp.sin and k == 0: continue
        ck = sp.simplify(sp.integrate(rhs*f(k*t), (t, 0, 2*sp.pi))/(sp.pi*(2 if k == 0 else 1)))
        if ck != 0:
            coef[(f.__name__, k)] = sp.simplify(ck/((q + 1)**2 - k**2))
s2 = coef.get(('sin', 2), 0)
print('sin 2th coeff of Psi_{2p-1}[B_p]:', sp.factor(s2))
print('(1-p)^2 * coeff - claim:', sp.simplify((1 - p)**2*s2 - p*(-5*p**2 + 25*p + 18)/(64*(1 - p)**2*(p + 1)*(p + 4))*(1 - p)**2))
print('limit p->1 of (1-p)^2 coeff:', sp.limit((1 - p)**2*s2, p, 1))
