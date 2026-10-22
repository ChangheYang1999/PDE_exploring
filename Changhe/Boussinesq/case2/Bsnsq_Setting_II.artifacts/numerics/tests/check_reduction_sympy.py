"""Independent symbolic checks of:
 (1) the A2 symmetry reduction (A2-red) from (P),
 (2) the Taylor identities c = 2 beta + 2 and (2 beta + 1) b0 = 2 a0,
 (3) the desingularized forms used by the solver:
     R_Theta = x^2 y R_a,  R_a = W.grad a + (2 w1 + w2 - beta + 2) a,
     R_Omega = x y R_G,    R_G = W.grad G + (w1 + w2 + 1) G - 2 a - x a_x,
     with Theta = x^2 y a(s,t), Omega = x y G(s,t), Psi = x y H(s,t), s = x^2, t = y^2,
     W1 = x w1, W2 = y w2, w1 = beta - H - 2 t H_t = A, w2 = beta + H + 2 s H_s = B.
"""
import sympy as sp
x, y, beta = sp.symbols('x y beta', real=True)
s, t = sp.symbols('s t', positive=True)
a = sp.Function('a'); G = sp.Function('G'); H = sp.Function('H')
S, T = x**2, y**2
Theta = x**2*y*a(S, T)
Omega = x*y*G(S, T)
Psi = x*y*H(S, T)
U1 = -sp.diff(Psi, y); U2 = sp.diff(Psi, x)
W1 = beta*x + U1; W2 = beta*y + U2
R_Theta = W1*sp.diff(Theta, x) + W2*sp.diff(Theta, y) - (beta-2)*Theta
R_Omega = W1*sp.diff(Omega, x) + W2*sp.diff(Omega, y) + Omega - sp.diff(Theta, x)
E = -(sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2)) - Omega

# (3) desingularized forms
w1 = sp.simplify(W1/x); w2 = sp.simplify(W2/y)
A_ = beta - H(S, T) - 2*T*sp.Derivative(H(S, T), T) if False else None
# express A,B directly with Subs-free derivatives
Hs = sp.diff(H(S, T), x)/(2*x)   # = H_s
Ht = sp.diff(H(S, T), y)/(2*y)   # = H_t
A = beta - H(S, T) - 2*T*Ht
B = beta + H(S, T) + 2*S*Hs
print('w1 == A :', sp.simplify(w1 - A) == 0)
print('w2 == B :', sp.simplify(w2 - B) == 0)
ax = sp.diff(a(S, T), x); ay = sp.diff(a(S, T), y)
R_a = W1*ax + W2*ay + (2*w1 + w2 - beta + 2)*a(S, T)
print('R_Theta == x^2 y R_a :', sp.simplify(R_Theta - x**2*y*R_a) == 0)
Gx = sp.diff(G(S, T), x); Gy = sp.diff(G(S, T), y)
R_G = W1*Gx + W2*Gy + (w1 + w2 + 1)*G(S, T) - 2*a(S, T) - x*ax
print('R_Omega == x y R_G :', sp.simplify(R_Omega - x*y*R_G) == 0)

# (1) A2-red in (s,t): F = s a; use generic F
F = sp.Function('F')
Theta2 = y*F(S, T)
R_Theta2 = W1*sp.diff(Theta2, x) + W2*sp.diff(Theta2, y) - (beta-2)*Theta2
Fs = sp.diff(F(S, T), x)/(2*x); Ft = sp.diff(F(S, T), y)/(2*y)
red1 = 2*S*A*Fs + 2*T*B*Ft + (B - beta + 2)*F(S, T)
print('(A2-red) eq1: R_Theta/y == 2sAF_s+2tBF_t+(B-beta+2)F :', sp.simplify(R_Theta2/y - red1) == 0)
R_Omega2 = W1*sp.diff(Omega, x) + W2*sp.diff(Omega, y) + Omega - sp.diff(Theta2, x)
Gs = Gx/(2*x); Gt = Gy/(2*y)
red2 = 2*S*A*Gs + 2*T*B*Gt + (A + B + 1)*G(S, T) - 2*Fs
print('(A2-red) eq2: R_Omega/(xy) == 2sAG_s+2tBG_t+(A+B+1)G-2F_s :', sp.simplify(R_Omega2/(x*y) - red2) == 0)
Hss = sp.diff(Hs, x)/(2*x); Htt = sp.diff(Ht, y)/(2*y)
red3 = 4*S*Hss + 6*Hs + 4*T*Htt + 6*Ht + G(S, T)
print('(A2-red) eq3: -E/(xy) == 4sH_ss+6H_s+4tH_tt+6H_t+G :', sp.simplify(-E/(x*y) - red3) == 0)

# (2) Taylor identities with polynomial jets
a0, b0, c = sp.symbols('a0 b0 c')
# generic even-even jets to degree 2 in (s,t)
a1, a2, g1, g2, h1, h2 = sp.symbols('a1 a2 g1 g2 h1 h2')
aj = a0 + a1*s + a2*t; Gj = b0 + g1*s + g2*t; Hj = c + h1*s + h2*t
sub = {a(S, T): aj.subs({s: S, t: T}), G(S, T): Gj.subs({s: S, t: T}), H(S, T): Hj.subs({s: S, t: T})}
Theta_j = x**2*y*aj.subs({s: S, t: T}); Omega_j = x*y*Gj.subs({s: S, t: T}); Psi_j = x*y*Hj.subs({s: S, t: T})
U1j = -sp.diff(Psi_j, y); U2j = sp.diff(Psi_j, x)
W1j = beta*x + U1j; W2j = beta*y + U2j
RT = sp.expand(W1j*sp.diff(Theta_j, x) + W2j*sp.diff(Theta_j, y) - (beta-2)*Theta_j)
RO = sp.expand(W1j*sp.diff(Omega_j, x) + W2j*sp.diff(Omega_j, y) + Omega_j - sp.diff(Theta_j, x))
print('R_Theta coefficient of x^2 y :', sp.factor(RT.coeff(x, 2).coeff(y, 1)))
print('R_Omega coefficient of x y   :', sp.factor(RO.coeff(x, 1).coeff(y, 1)))
# Poisson at origin for the jet: -Delta(xy(c + h1 x^2 + h2 y^2)) = -(6 h1 + 6 h2) x y ... check
print('-Delta Psi_j - Omega_j, coeff xy :', sp.expand(-(sp.diff(Psi_j, x, 2) + sp.diff(Psi_j, y, 2)) - Omega_j).coeff(x, 1).coeff(y, 1))
# origin strain identity: c = H(0) = (1/2) int_0^inf b2(s)/s ds for Omega = b2(r) sin 2 theta
r, th, sa = sp.symbols('r theta sigma', positive=True)
# check Green formula for mode k: h_k = (1/2k)[r^-k int_0^r s^{k+1} b ds + r^k int_r^inf s^{1-k} b ds] solves -(h''+h'/r-k^2 h/r^2) = b
k = sp.symbols('k', positive=True)
bfun = sp.Function('b')
ss = sp.symbols('ss', positive=True)
Iin = sp.Integral(ss**(k+1)*bfun(ss), (ss, 0, r)); Iout = sp.Integral(ss**(1-k)*bfun(ss), (ss, r, sp.oo))
h = (r**(-k)*Iin + r**k*Iout)/(2*k)
lhs = -(sp.diff(h, r, 2) + sp.diff(h, r)/r - k**2*h/r**2)
print('Green mode formula: -(h\'\'+h\'/r-k^2h/r^2) - b =', sp.simplify(lhs - bfun(r)))
