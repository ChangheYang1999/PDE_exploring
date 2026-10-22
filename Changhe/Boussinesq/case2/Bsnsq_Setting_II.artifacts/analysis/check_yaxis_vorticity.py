# Symbolic checks for the y-axis temperature/vorticity traces (the y-axis trace lemma of the analysis).
import sympy as sp

b, y, t, nu, d = sp.symbols('beta y t nu d', real=True)
L = 3*b + 2          # lam_y
c = 2*b + 1          # vorticity coefficient
v = sp.Function('v')(y)
E = sp.Function('E')(y)
K = sp.Function('K')(y)

# 1. s = K/E satisfies v s' + (v' - beta - 1) s = 2 given the two trace equations.
Ep = (2*sp.diff(v, y) - L)*E/v
Kp = (2*E - (c - sp.diff(v, y))*K)/v
s = K/E
sp_ = Kp/E - K*Ep/E**2
print('s-ODE residual:', sp.simplify(v*sp_ + (sp.diff(v, y) - b - 1)*s - 2))

# 2. Negative simple zero nu: if ord K = ord E = p = 2 - L/nu, then K/E -> 2/(c + (p-1) nu) = 2/(nu - (beta+1)).
p = 2 - L/nu
print('r = p limit check:', sp.simplify(2/(c + (p - 1)*nu) - 2/(nu - (b + 1))))
# 3. n = L/|nu|, ell = c/|nu|: 2n - 3 ell = 1/|nu|  (nu < 0, |nu| = -nu)
n = L/(-nu); ell = c/(-nu)
print('2n - 3 ell - 1/|nu|:', sp.simplify(2*n - 3*ell - 1/(-nu)))
# 4. With nu = -1/d: p - r = n + 2 - (ell + 1) = (beta + 1) d + 1
pr = (n + 2 - (ell + 1)).subs(nu, -1/d)
print('p - r - ((beta+1) d + 1):', sp.simplify(pr - ((b + 1)*d + 1)))
# 5. Positive zeros: nu2 = L/2 (p = 0): K/E -> 2/(c - nu2) = 4/beta; nu2 = L (p = 1): K/E -> 2/c.
print('nu2 = L/2:', sp.simplify(2/(c - L/2) - 4/b), ' nu2 = L:', sp.simplify(2/(c + 0*L) - 2/c))
# homogeneous K exponents at these positive zeros: 1 - c/nu2, must be non-integer (here negative or in (0,1))
print('hom. exponents at nu2 = L/2, L:', sp.simplify(1 - c/(L/2)), sp.simplify(1 - c/L))

# 6. Integral identity: with t' = 1/v, v d/dy [ s v exp(-(beta+1) t(y)) ] = 2 v exp(-(beta+1) t)
T = sp.Function('T')(y)  # flow time on the axis, T' = 1/v
S = sp.Function('S')(y)
expr = v*sp.diff(S*v*sp.exp(-(b + 1)*T), y)
expr = expr.subs(sp.Derivative(T, y), 1/v)
expr = expr.subs(sp.Derivative(S, y), (2 - (sp.diff(v, y) - b - 1)*S)/v)
print('integral identity residual:', sp.simplify(expr - 2*v*sp.exp(-(b + 1)*T)))

# 7. Far field with v = beta y exactly: s = -2 + C y^(1/beta) solves the s-ODE.
C = sp.symbols('C')
sf = -2 + C*y**(1/b)
print('far-field s check:', sp.simplify(b*y*sp.diff(sf, y) + (b - b - 1)*sf - 2))

# 8. D = Omega + Theta_x: W.grad D + D + (d_x U).grad Theta = R_V + d_x R_T (exact identity).
x = sp.symbols('x', real=True)
Y = sp.symbols('Y', real=True)
U1 = sp.Function('U1')(x, Y); U2 = sp.Function('U2')(x, Y)
Th = sp.Function('Th')(x, Y); Om = sp.Function('Om')(x, Y)
W1 = b*x + U1; W2 = b*Y + U2
kap = b - 2
RT = W1*sp.diff(Th, x) + W2*sp.diff(Th, Y) - kap*Th
RV = W1*sp.diff(Om, x) + W2*sp.diff(Om, Y) + Om - sp.diff(Th, x)
D = Om + sp.diff(Th, x)
lhs = W1*sp.diff(D, x) + W2*sp.diff(D, Y) + D + sp.diff(U1, x)*sp.diff(Th, x) + sp.diff(U2, x)*sp.diff(Th, Y)
print('D identity residual:', sp.simplify(sp.expand(lhs - RV - sp.diff(RT, x))))

# 9. J_1 transport on the axis: with X1' = A0 X1, A0 = 2 beta - v', d/dsigma [e^sigma K X1] = 2 e^sigma E X1
sig = sp.symbols('sigma')
# along the axis orbit d/dsigma = v d/dy
A0 = 2*b - sp.diff(v, y)
X1 = sp.Function('X1')(y)  # as a function of y along the orbit, v X1' = A0 X1
e = sp.Function('e')(y)    # e^sigma along the orbit, v e' = e
expr = v*sp.diff(e*K*X1, y)
expr = expr.subs({sp.Derivative(X1, y): A0*X1/v, sp.Derivative(e, y): e/v, sp.Derivative(K, y): Kp})
print('J_1 transport residual:', sp.simplify(expr - 2*e*E*X1))
