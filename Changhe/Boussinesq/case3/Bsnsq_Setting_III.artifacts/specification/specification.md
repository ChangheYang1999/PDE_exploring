# Specification (Setting B2): admissible class, inverse, normalization, identities

Version 94, 2026-10-22T11:43Z (lead). The numerical work and the independent verification follow this file. Changes are logged at the end.

## 1. Equations (rederived by the lead; verifier please rederive independently)

Physical system: w_t + u.grad w = d_{z1} theta, theta_t + u.grad theta = 0, u = (-psi_{z2}, psi_{z1}), -Lap psi = w.
Remark: with this convention w = -curl u (curl u = d1 u2 - d2 u1 = Lap psi). It is the standard Boussinesq
system after theta -> -theta; we keep the prompt's convention throughout.

Ansatz: tau = T - t, X = (z - z_c(t))/tau^beta, w = tau^{-1} Omega(X), theta = tau^{beta-2} Theta(X),
u = tau^{beta-1} U(X), psi = tau^{2beta-1} Psi(X), z_c' = u(t, z_c) = tau^{beta-1} U(0).
Substitution gives exactly (lead check, line by line):
  dt X = tau^{-1} (beta X - U(0)),
  theta-eq: tau^{beta-3} [ (beta X + U - U(0)).grad Theta - (beta-2) Theta ] = 0,
  w-eq:     tau^{-2}     [ (beta X + U - U(0)).grad Omega + Omega - Theta_x ] = 0.
So (B2-P):
  W.grad Omega + Omega = Theta_x,   W.grad Theta = (beta-2) Theta,   W = beta X + U(X) - U(0),
  -Lap Psi = Omega,  U = (-Psi_y, Psi_x).
z_c(t) = z_* - U(0) tau^beta / beta.

Reduced variables s = x^2: Theta = x^2 F(s,y), Omega = x G(s,y), Psi = x H(s,y):
  U1 = -x H_y, U2 = H + 2 s H_s, A = beta - H_y, B = beta y + H + 2 s H_s - H(0,0), W = (x A, B),
  2A(F + sF_s) + B F_y = (beta-2) F,
  A(G + 2sG_s) + B G_y + G = 2(F + sF_s),
  4 s H_ss + 6 H_s + H_yy = -G.
(These are (B2-red) of the prompt; the lead has checked them. Verifier: rederive.)

Center identities: W(0) = 0; DW(0) = diag(beta - c, beta + c), c = Psi_xy(0) = H_y(0,0);
Theta-jet: 2(beta - c) = beta - 2, so c = 1 + beta/2, DW(0) = diag((beta-2)/2, 1 + 3beta/2);
Omega-jet: (beta - c + 1) b0 = 2 a0, so b0 = G(0,0) = 4 a0/beta.

## 2. Admissible class (class A)

(A1) beta > 0 real, unknown.
(A2) Theta in C^infty(R^2) (the regularity each theorem actually uses is stated theorem by theorem in FINAL_REPORT;
     flat-jet and Sard arguments at beta = 2 need C^infty, so do NOT assume C^3 suffices in general), even in x, Theta(0,y) = 0, Theta = a0 x^2 + O(|X|^3)
     near 0 with a0 != 0. Polynomial growth: |Theta(X)| <= C (1+|X|)^m for some m.
(A3) Omega in C^infty(R^2), odd in x, with |Omega(X)| <= C (1+|X|)^{-delta} for some delta > 0 (polynomial tail).
(A4) Velocity law (canonical inverse). U is a C^1 divergence-free field with -curl U = Omega and U(X) = o(|X|).
     By Liouville, U is then unique up to an additive constant vector, so the RELATIVE velocity
        U_rel(X) := U(X) - U(0)
     is canonical. Under (A3) it is given by the absolutely convergent once-subtracted Biot-Savart integral
        U_rel(X) = int_{R^2} [K(X-Y) - K(-Y)] Omega(Y) dY,   K(Z) = (1/(2 pi)) (Z_2, -Z_1)/|Z|^2,
     equivalently U_rel = (-Psi_rel_y, Psi_rel_x) with the twice-subtracted stream function
        Psi_rel(X) = -(1/(2 pi)) int [ log|X-Y| - log|Y| + X.Y/|Y|^2 ] Omega(Y) dY,
     which satisfies -Lap Psi_rel = Omega, Psi_rel(0) = 0, grad Psi_rel(0) = 0, Psi_rel odd in x,
     Psi_rel = x H_rel with H_rel(0,0) = 0, and U_rel = O(|X|^{1-delta}) (delta < 1).
     W = beta X + U_rel. Nothing else (no strain, no harmonic correction, no wall, no fitted drift) is allowed.
(A5) What the canonical inverse fixes, and what it does not. B2-P involves only U_rel, which is canonical.
     The center drift v0 = U(0) = (0, (1/(2pi)) int Y_1 Omega(Y)/|Y|^2 dY) is canonically defined only when this
     integral converges, e.g. when int |Omega| (1+|Y|)^{-1} dY < infinity. In every nontrivial class A solution
     this integral fails to converge absolutely: by Theorem 4.11 [V], int |Y_1 Omega|/|Y|^2 diverges. Theorem A
     excludes beta<2. The positive part of (sign a0) Omega on the right half-ball contributes at least c
     R^(1-1/beta) to the absolute component integral; this is not a bound on the full signed truncation. By
     Theorem D (4.12), signed circular truncations satisfy v0(R)=B R^(1-1/beta)+o(R^(1-1/beta)), where B=[2 pi
     (1-1/beta)]^(-1) int_0^(2pi) cos(theta) a(theta) dtheta. They diverge if B!=0; when B=0 this leading
     asymptotic does not decide convergence. If a0>0 and Omega>=0 on x>0, then B>0 and v0(R) is asymptotic to B
     R^(1-1/beta). The absolute-divergence theorem does not select a finite observer drift.
     So v0 is an observer gauge, fixed only by a declared convention. Exact statement (verifier research/07): if (theta, w, u, p) solves the physical
     system and a(t) is a C^2 path, then theta(t, z - a(t)), w(t, z - a(t)), u(t, z - a(t)) + a'(t),
     p(t, z - a(t)) - a''(t).z is again a solution (the scalars are TRANSLATED too). With a(t) = -v tau^beta/beta the
     profile (Theta, Omega, U_rel) is unchanged, U(0) -> v0 + v, z_c -> z_c + a. Equivalently, a moving-center profile
     is a translated fixed-center profile: Y = X - v0/beta, W(X) = beta Y + U(Y + v0/beta).
     B2-P and every statement in this file are independent of v0. Numerics: report the circularly truncated value v0(R)
     and its R-dependence; never fit it.
     SELECTED CONVENTION (lead, 16:13Z). The canonical object is (Theta, Omega, U_rel, beta); v0 is a free observer
     parameter. For physical reconstruction we use the representative v0 = 0 (observer in which the material center is
     at rest, z_c = z_*, u = tau^{beta-1} U_rel(X)); any other v0 is obtained by the exact observer change above. In
     class A, "U(0) = 0" (B1) therefore has no gauge-invariant meaning: no absolutely convergent integral defines U(0)
     (4.11), and the constant is invisible at the blow-up time (tau^{beta-1} v0 -> 0). A candidate report must state
     U_rel (subtracted kernel), v0(R) for diagnostics, and that v0 = 0 was used for reconstruction.
(A6) Scaling gauge. Theta_l = l Theta(X/l), Omega_l = Omega(X/l), U_l = l U(X/l) is an exact symmetry for every real
     l != 0 (l < 0 includes the y-reflection (x,y) -> (x,-y), Theta -> -Theta o R, Omega -> -Omega o R). It maps
     a0 -> a0/l. NORMALIZATION: a0 = 1 (Theta_xx(0) = 2). This fixes the full scaling group (including the sign),
     and excludes no branch. Then c = 1 + beta/2, G(0,0) = 4/beta.

## 3. Proved restrictions (status per item; items marked [V] are verifier-CONFIRMED and referee-audited, in FINAL_REPORT)

Let W be locally Lipschitz on R^2 with W(X).X > 0 for |X| >= R0 (true under (A4): W.X = beta|X|^2 + U_rel.X).
Then every backward W-orbit stays in the closed ball of radius max(|Y|, R0) for all backward time.

THEOREM A [V] (no profile with beta < 2). If 0 < beta < 2 and Theta in C^1 solves W.grad Theta = (beta-2) Theta, then
Theta = 0. Proof: along the backward orbit X(t) = phi_{-t}(Y), Theta(X(t)) = e^{(2-beta)t} Theta(Y); the orbit stays in
a compact ball on which |Theta| <= M, so |Theta(Y)| <= M e^{-(2-beta)t} -> 0.
(No use is made of the vorticity equation, of Biot-Savart, of parity or of tails of Theta. Only |U_rel| < beta|X| for
large |X| is used.)

PROPOSITION B [V] (beta > 2; the global size of R(0) is NOT claimed). Let K = {Y : forward orbit bounded}. Then Theta = 0 on K (forward analogue of A);
Theta bounded implies Theta = 0; along every escaping orbit Theta(phi_t Y) = e^{(beta-2)t} Theta(Y), so
|Theta| grows like |X|^{1-2/beta} along every escaping orbit with Theta(Y) != 0. The origin is a hyperbolic source
(eigenvalues (beta-2)/2 < 1 + 3beta/2). On its basin of repulsion R(0) (an open invariant set containing 0),
Theta = a0 xi^2 where xi is the unique C^1 solution of W.grad xi = ((beta-2)/2) xi with xi = x + o(|X|): a C^{2,e}
solution is determined by its 2-jet, and the 2-jet is a0 x^2. Consequently Theta has the sign of a0 on R(0),
vanishes there exactly on the y-axis, and Theta(0,y) = 0 is automatic on R(0).

PROPOSITION C [V] (beta = 2). Theta is constant along W-orbits, hence bounded. DW(0) = diag(0, 4). By the implicit
function theorem on W_2 = 0 and Theta_x != 0 off the axis, W vanishes on a C^1 arc through 0 tangent to the x-axis.
(Necessary condition; not an exclusion.)

COROLLARY. Every nontrivial profile of class A has beta >= 2; bounded nontrivial Theta forces beta = 2;
beta > 2 forces |Theta| ~ |X|^{1-2/beta} growth.

THEOREM E [V] (restricted class). beta >= 2, U = o(|X|), (D) sup_{|Y|>=R} int_0^infty |DU_rel(phi_t Y)| dt -> 0
(implied by (H1) |U_rel| <= C|X|^{1-delta}, |DU_rel| <= C|X|^{-delta}; (D) version verifier research/23 + auditJ VALID
15:28Z; (D) is not implied by smoothness + sublinearity + parity + center data, shear example). If int |Omega|(1+|X|)^{-gamma} < infinity for some
gamma <= 2 - 2/beta, or Omega in L^p for some 0 < p <= beta, then Theta = 0 for beta > 2 (no axis condition needed) and
Theta = const for beta = 2. The two-term expansion Omega(phi_t Y) = e^{-t}A - e^{-2t}(g + o(1)) holds ALONG TRAJECTORIES;
a fixed-angle expansion is not established.

THEOREM 4.7 [V] (beta = 2). U real analytic near {W = 0} is impossible. If U, Theta are C^infty, some accumulation zero
p of W has a flat Theta jet (all derivatives of order >= 1 vanish), so Theta is not real analytic.

THEOREM 4.8 [V] (mass bound). beta >= 2, |U_rel| <= C(1+|X|)^{1-eps} (automatic in class A): M(R) = int_{B_R}|Omega|
>= c R^{2-2/beta}. Hence no uniform o(r^{-2/beta}) decay, no weighted L^1 with gamma <= 2-2/beta, Omega not in L^p for
1 <= p <= beta. Identity: div[W Omega f(Theta) - g(Theta) e_x] = [(2beta-1) f + (beta-2) Theta f'] Omega, g' = f.
[V] the same L^p exclusion under ONLY U = o(r) (verifier research/09 Sec. 5-7; referee VALID).
[V] referee F: r^{-(1-2/beta)} Theta(r e^{i phi}) -> A(phi) uniformly under the power bound (verifier research/14).
(The conditional sign claim under |Omega| <= C r^{-2/beta} is now vacuous: that tail class is empty by 4.9.)

THEOREM 4.9 [V] (circulation, notes/circulation_mass.md; verifier research/17; referee VALID with fixes).
beta >= 2, U_rel = o(r). For the small (xi, y) rectangle D at the center, J(t) = int_{phi_t D} Omega satisfies
J' = (2beta-1)J + B, B = oint Theta dy, and J e^{-(2beta-1)t} -> A_D = int_D Omega - oint_{dD} H dTheta, a0 A_D > 0,
H = int_0^infty e^{-(beta+1)s}(phi_s X)_2 ds. Hence int_{B_R cap {x>0}} ((sign a0)Omega)_+ >= c R^{2-1/beta} (power bound),
>= c_eta R^{(2beta-1)/(beta+eta)} (U = o(r)). Omega not in L^p for 1 <= p <= 2 beta (U = o(r) only); no uniform
o(r^{-1/beta}) decay; the critical tail r^{-2/beta} is EXCLUDED. No pointwise trajectory limit is claimed.

THEOREM 4.11 [V] (sector circulation; verifier research/18, C1/C2 confirmed 15:07Z; external referee auditI VALID 15:06Z).
beta >= 2, power bound on U_rel. A fixed sector-annulus K = {a <= r <= b, x >= eps0 r} has
int_{RK} ((sign a0) Omega)_+ >= c R^{2-1/beta}. Hence int |x| r^{-gamma-1} ((sign a0)Omega)_+ = infinity for
gamma <= 2 - 1/beta; gamma = 1: the drift component integral diverges absolutely (>= c R^{1-1/beta}). Under (H1) the
trajectory coefficient A in Omega(phi_t Y) = e^{-t} A(Y) + O(e^{-2t}) is not identically zero. beta = 2 via a Sard
regular level of Theta (lines, simple repelling zeros, escape). Also [V]: Omega is flat at the flat-Theta zero of 4.7(ii).

THEOREM D = FINAL_REPORT 4.12 [V] (verifier research/33 CONFIRMED 16:02Z, two proofs; external referee auditK VALID WITH FIXES
16:06Z). Every class A profile: delta <= 1/beta (from 4.9); |DU_rel| <= C r^{-1/beta}, |U_rel| <= C r^{1-1/beta},
|grad Theta| <= C r^{-2/beta}; (D) holds with eps(R) <= C R^{-1/beta}; Omega = r^{-1/beta}(a(theta) + o(1)) UNIFORMLY in
theta, a continuous, a(pi - theta) = -a(theta), a not identically 0. With 4.10: Theta = r^{1-2/beta}(A(theta) + o(1)).
Not a nonexistence result: the leading pair (a, A) is unconstrained at leading order.
CLASS REDUCTION = FINAL_REPORT 4.15 [V] (verifier research/39 CONFIRMED 16:27-16:31Z; external referee auditL VALID WITH FIXES
16:18Z): beta >= 2, U = o(r), and (i) Omega -> 0, or (ii) Omega bounded, or (iii) beta = 2 with no vorticity
assumption, imply |Omega| <= C_eta r^{-1/(beta + eta)}, |Theta| <= C r^p (p < 1), canonical inverse. So class A =
{smooth B2 profiles with U = o(r) and bounded Omega}; at beta = 2 = {smooth B2 profiles with U = o(r)}.
POLYNOMIAL VORTICITY = FINAL_REPORT 4.15(iii) [V] (verifier research/40 CONFIRMED 16:37Z; external referee audit40 VALID 16:47Z,
one wording fix: only V = U - U(0) is the canonical integral): polynomially bounded Omega (|Omega| <= C r^k) with
U = o(r) (uniform) implies class A (local strain bound |DV| <= C[M + A/r] log(2 + M), exponent iteration
k -> max(0, k - 1/beta)). So CLASS A = THE PROMPT'S BROAD TARGET (sublinear velocity, polynomially bounded vorticity);
FINAL_REPORT section 1 and section 3 say so. A NO for class A would be a full NO.
SECOND FAR-FIELD TERMS = FINAL_REPORT 4.16 [V] (verifier research/35, 36; external referee audit35 VALID 16:37Z): a, A smooth;
Omega = r^{-s} a + r^{-2s} b + o_{C^j}(r^{-2s}), Theta = r^m A + r^{m-s} d + o_{C^j}(r^{m-s}), s = 1/beta,
b = u0t a' - s u0r a - d_x theta0(e), d = u0t A' + m u0r A (u0 = canonical inverse of r^{-s} a). Numerics: use these
as the far-field model beyond the leading order (section 5). Velocity second term (research/38): verifier CONFIRMED,
not yet audited.
SIGN 4.12(f) [V]: (sign a0) a > 0 on an open arc with cos theta > eps0 (sector of 4.11(i)).
BETA = 2 ARC = FINAL_REPORT 4.7(iii)-(iv) [V] (verifier 45 + auditN): the zero component through 0 is a compact smooth
x-symmetric arc meeting the axis only at 0; Theta - L and Omega are flat at BOTH endpoints; DW = 4 n (x) n there; no
profile if Theta is analytic near the arc. Each endpoint is (a) accumulating (other zeros of W accumulate from beyond),
(b) outgoing (open invariant O with backward limit p, Theta = L, Omega = 0, U harmonic on O, O reaches infinity, and
a = 0, A = L on an open arc of angles) or (c) incoming (no conclusion).
CRITICAL IDENTITY = FINAL_REPORT 4.12(g) [V] (verifier 44 + auditN), every class A profile, every beta >= 2:
int |Omega|^{2 beta - 2} Omega Theta_x = (1/2) int |a|^{2 beta} d theta > 0 (numerical diagnostic: report it).
DIVIDED FIELDS = FINAL_REPORT 4.17 [V] (verifier 50 + auditO H), class A, beta > 2: P = Theta/x^2, Q = Omega/x,
v = V_1/x, S = 2P + x P_x obey |P| + |S| <= C(1+r)^{-1-2/beta}, |Q| <= C(1+r)^{-1-1/beta}, |v| <= C(1+r)^{-1/beta};
|A(theta)| <= C cos^2 theta, |a(theta)| <= C|cos theta|; int_{x>0}(1+v)P^2 = 0, int_{x>0}(1+v)Q^2 = int_{x>0} Q S,
int v|P|^k = [beta/k - (beta+2)/2] int |P|^k (k > 2beta/(beta+2)), and
beta int a cos^{-alpha} = alpha int_{x>0} x^{1-alpha}(P - vQ), alpha = 2 - 1/beta. Numerics: the representation
F = Theta/x^2-type quotients must decay like r^{-1-2/beta} and r^{-1-1/beta} (already in section 5); diagnostics 9.
GLOBAL SOURCE = FINAL_REPORT 4.18 [V] (verifier 48-49 + auditO A-D): if W has no zero but 0, Theta = a0 xi^2 >= 0 with
smooth area-preserving coordinates (xi, eta) in which W = lambda1 xi d_xi + (lambda2 eta + kappa xi^k) d_eta, where the
even resonant triangular term kappa xi^k (k = lambda2/lambda1 an even integer) is possible (4.18(b)); a global C^1 linear
conjugacy is available, a smooth one only if kappa = 0; no Omega = x g(x^2 + (y - y0)^2); a horizontal reflection of Omega about y0
forces b(y0)^2 q''(y0) = 4(beta+1)^2(beta+2) q(y0)/(beta - 1) > 0. Not an exclusion of the subclass.
ZEROS OFF THE CENTER = FINAL_REPORT 4.19 [V] (beta > 2): zeros are hyperbolic sources (a zero with grad Theta != 0 is a
source; the converse fails), hyperbolic saddles or degenerate (eigenvalues 0, 2 beta; Theta, Omega flat there); backward orbits converge to single zeros;
Theta = grad Theta = Omega = 0 on saddle unstable manifolds and on basin boundaries of sources; if b = W_2(0, .) has no
zero but 0 the profile is in G; for beta irrational or P/Q with P, Q odd the nearest axis zero is degenerate.
WEAK SIGN (Omega >= 0 on {x > 0}, sign of a0) = FINAL_REPORT 4.7(viii)-(x), 4.20 [V]: no forward-escaping orbit in
{x > 0} is (eventually) horizontal (beta >= 2); at beta = 2 critical directions of the angular temperature h are
degenerate, of odd order at a non-saddle backward limit, flat at extrema; for beta >= 2 a critical point of Theta on an
escaping orbit in {x > 0} forces grad Theta = D^2 Theta = Omega = grad Omega = 0 on the orbit (Theta = 0 if beta > 2),
and odd order / flat extrema at a non-saddle backward limit. Numerics: a candidate with a weak sign must not show an
escaping orbit in {x > 0} through a physical critical point with nonzero Hessian of Theta (diagnostic, not a test).
AXIS TAILS = FINAL_REPORT 4.21 [V] (beta >= 2): on a half-axis with no zero of b = W_2(0, .) (both half-axes in G),
Theta_xx(0, y) = P |y|^{-1-2/beta}(1 + O(|y|^{-1/beta})), Omega_x(0, y) = Q |y|^{-1-1/beta}(1 + O(|y|^{-1/beta})), P, Q > 0, and
h''(+-pi/2) = P, a'(pi/2) = -Q_+, a'(-pi/2) = Q_- (a/cos theta -> Q, h/cos^2 theta -> P/2 at the vertical direction). In G,
Theta_x >= 0 on {x > 0} implies Omega > 0 there and a > 0 on the open right semicircle. Numerics: diagnostic 10 (only a
verified failure is informative; a basis with these powers built in satisfies it without solving the equations).
TEMPERATURE TAIL IN G = FINAL_REPORT 4.22 [V]: Theta(Y) = |Phi(Y)|^{1-2/beta} h(arg Phi(Y)); h > 0 off the vertical
directions; h/cos^2 theta is smooth and positive; c(1 + r)^{-1-2/beta} <= Theta/x^2 <= C(1 + r)^{-1-2/beta}. On each level
curve Theta = T > 0: x_T(y) = (2T/P_+-)^{1/2} |y|^{1/2+1/beta}(1 + o(1)), Omega = Q_+- (2T/P_+-)^{1/2} |y|^{-1/2}(1 + o(1)).
kappa = 0: (xi, eta) o Phi^{-1}(r e) = (r^alpha q, r^gamma g), alpha q g' - gamma q' g = 1, one simple zero of g per open
semicircle. This geometry alone does not give Theta_x >= 0 (explicit map). Numerics: for a G candidate, Theta/x^2 must be
positive with the two-sided rate (diagnostic, not a test).
HOMOGENEOUS WEIGHTS = FINAL_REPORT 4.23 [V], beta >= 2 (construction beta > 2), d = 1/beta, k0 = 2 - d, kT = 2 - 2d:
for f_k = r^{-k} phi(theta) odd in x and g_k = d_x f_k, beta (k - k0) int f_k Omega = int Omega V.grad f_k - int Theta g_k
(k0 < Re k < 3) and beta (k - kT) int g_k Theta = int Theta V.grad g_k (kT < Re k < 3); the full family is equivalent to
(V), (T). Strain identity (k = 2, f = K_c = x y/|X|^4): pi (1 + beta/2) = int Omega V.grad K_c - (1/2) int Theta
V.grad(d_x K_c), invariant under signed scaling, no sign (blob pairs give both signs; smooth nonsolutions satisfy it with
all parity, center, sign and decay conditions). Residue at k0: beta int phi a = int Omega V.grad f_{k0} - int Theta
V.grad g_{k0}. Exclusions: Omega(x, y) <= Omega(x, -y) on x, y > 0; (beta > 2) L_x^{1/(beta+1)} A_x^{beta/(beta+1)} <
3 pi (beta + 2)/(8 (beta + 1)), L_x = sup |Omega/x|, A_x = sup |X|^{1+d} |Omega/x|. Numerics: diagnostic 11.
FINITE ANGULAR SUPPORT = FINAL_REPORT 4.24 [V], beta >= 2: no class A profile has Omega, or Psi (Psi(0) = 0), with
finitely many angular Fourier modes. Numerics: a pure finite-mode ansatz cannot be exact.
NONSTATIONARY LIMIT = 4.25 [V], beta >= 2: b and d of 4.16 do not both vanish; the homogeneous limit (u0, omega0,
theta0) is not a steady solution; no class A profile is exactly homogeneous outside a ball.
THIRD TERMS = 4.26 [V], beta > 2: explicit omega2, theta2; for 2 < beta < 3 a constant vertical velocity C = (0, C2),
C2 = -(1/(2 pi)) int (y1/|y|^2) eta, enters V at order r^0 and shifts Omega, Theta by (C.grad omega0)/beta,
(C.grad theta0)/beta. (c): a representation whose Omega is a finite sum of r^{-s-js-2n} c_jn(theta) outside a ball (the
radial representation with basis exponent = beta) forces C = 0, so such a state with C != 0 cannot be exact.
BETA = 3 RESONANCE = 4.27 [V]: V contains -(alpha/2)(log r)(0, 1), alpha = first cosine coefficient of r omega2; the
fourth terms of Omega, Theta contain -(alpha/6)(log r) d_y omega0, d_y theta0. (c): a log-free power representation
with basis exponent 3 forces alpha = 0. (d): the leading data alone do not fix alpha or its sign.
CENTER TAYLOR CONDITIONS = FINAL_REPORT 4.28 [V], beta > 2: the formal center equations of (V) are triangular,
(R_Omega)_n = (A X.grad + 1) Omega_n + N_n, and leave the harmonic coefficients of Psi free; (b) realizes R_Omega flat
at 0 with (T) on R^2, positivity, canonical inverse, slow tail and whole-plane basin (configuration, not a profile).
AXIS AND DISK REALIZATIONS = FINAL_REPORT 4.29 [V], beta > 2: d_x R_Omega(0, y) = b q' + (M - b') q - 2a; the exact
polynomial P = l x + c x y - (q0/6) x^3, Theta = a0 x^2, Omega = q0 x (not a profile); configurations with (V) exact on
a small disk, all axis jets of R_Omega zero on a finite segment, or d_x R_Omega = 0 on the whole axis (strip exterior).
Compact modifications of the example of 4.13 fail (V) far down the axis.
WHOLE AXIS / LARGE DISKS / ANALYTIC EXTERIORS = 4.30, 4.31(a), (b), 4.32 [V] (entered 05:15, 05:20): all derivatives of R_Omega
zero on the whole axis with (V) exact on a small disk (strip exterior); (V) and (T) exact on any prescribed disk, with
the anisotropic exterior Psi_L = -B x (L^2 + x^2 + eta (y - h)^2)^p; both together (4.31(b): any prescribed disk plus
all axis jets, exterior Psi_L off a narrow cone around the axis); and no C^2 temperature solves (T), (V) on any open
set for the relative velocity and vorticity of the example or of Psi_L (no-division elimination E = 0, [x^2 y]E > 0),
so all these configurations are non-profiles.
HORIZONTAL PRIMITIVE / EXTERIOR EXACTNESS / AXIS SUBSYSTEM = 4.33, 4.34, 4.35 [V]: 4.33 (T) and (V) in terms of
Theta = int_0^x F; 4.34 for every R0 > 0 a configuration with (V) exact on B_R0 and on |X| > R1, R_Omega a nonzero smooth
function supported in the closed annulus R0 <= |X| <= R1 (whole-axis flatness not asserted); 4.35 the axis subsystem in
the normalized coordinates of 4.18(b) and positive canonical vorticity compatible with it (no exclusion, no profile).
COMPATIBILITY SUMMARY = FINAL_REPORT, paragraph at the end of 4.31 (beta > 2): each of (i) every Taylor condition of (V)
at the center, (ii) (V) exactly on any prescribed disk plus every derivative of R_Omega zero on the whole axis, (iii) (V)
exactly on any prescribed disk and outside a larger disk, is satisfied by a configuration that also satisfies (T) on
R^2, parity, positivity, the center data, the canonical inverse and the slow tail. None is a profile (4.32). An exclusion
must use more, e.g. (V) on the connecting annulus as well, (V) on an open neighbourhood of the whole axis, or a global
argument.
CONVERSE OF THE COMPATIBILITY IDENTITY = 4.32(d) [V], entered 07:25: for Psi odd with Psi_xy(0) = c and the normalized
primitive Theta = int_0^x F, t = W.grad Theta - k Theta: E_comp = J^2 t_y - J W_2 t_xy + (W_2 J_y + J (k - d_y W_2)) t_x;
E_comp = 0 near 0 and Psi_xxx(0) != 0 give (T), (V) near 0 (no analyticity; any beta > 0); for beta > 2 and analytic Psi on R^2
with sublinear velocity, E_comp = 0 on R^2 iff (T), (V) on R^2 (beta = 2 OPEN). Psi_xxx(0) is not fixed by the center data. HORIZONTAL OFFSETS =
4.33(e) [V]: lim_L int_0^L (F(x, y) - F(x, 0)) dx = 0 for a profile with Theta(0, .) = 0 (diagnostic for numerics).
COMPACT MODIFICATIONS OF 4.34 = FINAL_REPORT 6.3 [V], beta > 2: (a) conjugation by the area-preserving flow of
grad^perp(eps eta), eta odd in two mirror disks of the polynomial disk, keeps (T), parity, center data, canonical inverse,
positivity (small eps), basin and the exterior, with Omega_eps recomputed from W_eps; int (x y/r^4) R_Omega changes (first
variation int eta A p0, A p0(x, 0) = -3 q0 (17 beta + 28)/(2 x^3)). (b) INVARIANT: if two configurations with exact (T)
have W and Theta equal outside a compact set (relative chi, tau compact), int delta R_Omega = int y delta R_Omega = 0,
int x delta R_Omega = int tau, int delta R_Theta = -(3 beta - 2) int tau, so int tau = 0 and int x R_Omega is invariant;
a repair of 4.34 keeping the exterior W, Theta requires int x R_Omega = 0 (necessary only).
(c) LARGE R [V, P145 + audit]: fixed reference, A = lim r^{-m} Theta_* >= 0, 0 <= rho <= 1: int x R_Omega =
R^{3-2s}[C_rho m1 + O(R^{-s})], C_rho = int_0^8 (1 - rho) r^{2-2s} dr > 0, m1 = int [1 - (3 - 2s) cos^2] A dtheta; m1 not
computed for any 4.34 reference. (d) 4.36 [V, P149 + A90; in report 09:02]: beta > 2 not in Z_crit = {M/d > 2,
gcd = 1, d <= 3}, (T) on R^2, R_Omega = 0 outside a ball, exterior expansion (stream 2 - Ks - n, temperature 1 - Ls - n,
remainders o(r^{-1}), o(r^{-2}), o(r^{-3}), o(r^{-2})): int x R_Omega = 2 pi (1 - 3 beta) D, D = coefficient of x/|X|^2;
profiles have D = 0; positivity gives no sign of D. (e) FINITE EXTERIOR EXPANSION [V, 4.37 in FINAL_REPORT; P150 CONFIRMED 09:23,
referee audit150 VALID WITH FIXES]: symbol bounds Omega in S^{-s}, V in S^{1-s}, Theta in S^m plus (T), (V) outside
a ball give P, H with remainders S^{2-mu}, S^{1-s-mu} for every mu in (3, 4) not in E = {Ks + n}; class A satisfies
the symbol bounds (rescaled local regularity of 4.16), so D = 0 for EVERY class A profile, beta > 2 not in Z_crit
(necessary only). (f) RENORMALIZED ENERGY [V, 4.38 in FINAL_REPORT; P151 CONFIRMED 09:47, audit437 VALID WITH FIXES]: for beta not in
Z_E = {M/N > 2, N <= 4}, depth 4 - s < mu < 4: (4 beta - 2) f.p. int (|V|^2/2 + y Theta) = -2 pi beta C D = 0 for
profiles (with compact R_Omega the right side gains - int Psi R_Omega); no sign (radial-dipole family with D = 0,
both signs, violating (V)). (g) [V, P147/P148/P152 + audit152; in report 6.3 10:18]: 4.34(iii) now includes
|D^k Theta| <= C_k (1 + |X|)^{m-k} for every k (P135), so 4.37 applies to the 4.34 configurations without an added
hypothesis; signed glued configurations with int R_Omega = int y R_Omega = int x R_Omega = 0 exist for every beta > 2
(nonprofiles; D = 0 outside Z_crit); compact conjugacies in a polynomial disk with Theta = a0 x^2, Omega = q0 x,
R_Omega = 0 keep these and the exterior and change f.p. energy at rate -4 a0 (5 - 1/beta) int x eta, so f.p. energy = 0
(4.38(c), beta not in Z_E) is not implied among nonprofiles. (h) [V, P154 + P155 + audit154/audit155 VALID; in report 6.3
10:46-10:48, re-read E368]: on these nonprofiles (both vorticity signs) the f.p. energy takes EVERY real value (twists in the
core: a_tw eps^2 + O(1 + |eps|), a_tw > 0; far annuli: -> -infinity; intermediate value theorem), with all affine residual
moments 0 and D = 0 outside Z_crit. So the energy condition 4.38(c) carries no information beyond being necessary.
BETA = 2 LOCAL REALIZATION [P156 CONFIRMED by VER 10:49; P158 (VER own proof of the outgoing endpoints, 11:01); audit156 VALID WITH FIXES 11:02; draft CONFIRMED E379 11:05; ENTERED 6.3, Summary, Table 8.1, 11:06]: a smooth nonprofile with the center
data, (T) on R^2, the canonical inverse, U = O(1/r), Theta >= 0 zero exactly on the axis, (V) on a prescribed disk and on a
neighbourhood of the open zero arc, flat endpoints as in 4.7(iii); lead claim (under VER check): endpoints of outgoing type (b),
with Omega != 0 on O, so (V) fails on O. Any beta = 2 exclusion must use (V) on O or farther out.
NONANALYTIC ENDPOINT GERM [P159 CONFIRMED by VER 11:23; audit159 (A102) VALID WITH FIXES 11:37; ENTERED 6.3, Summary, Table 8.1,
11:39]: a further compact area-preserving map, flat at the endpoints, makes the strong unstable curves non-analytic (as 4.7(vi)
requires) and keeps all other properties; (V) still fails (not identically zero) on an open invariant set at each endpoint.
P161 [CONFIRMED by VER 11:47; audit161 (A104) VALID WITH FIXES 12:09; ENTERED 6.3, Summary, Table 8.1, 12:14]: with a temperature plateau Theta = M on a subarc ending at
each endpoint, Omega = 0 and Theta = M on the local outgoing side and on the nonanalytic strong unstable curve; (V) still
fails in every endpoint neighbourhood.
4.7(xii) [lead; P162 CONFIRMED by VER 11:56, drafts E401 CONFIRMED 11:58; audit161 (A104) VALID 12:09; ENTERED 4.7, Summary, Q1, Table 8.1, 12:14]: for a smooth profile, (a) U is not
real analytic (in particular Omega is not identically 0) on any neighbourhood of an endpoint of gamma; (b) at an outgoing
endpoint Theta - L is not identically 0 on any neighbourhood (no plateau of Theta on a subarc ending at p). So an exclusion
at beta = 2 would follow from Omega = 0 on some endpoint neighbourhood; Theta = L on a neighbourhood of an OUTGOING endpoint
excludes only profiles having that outgoing endpoint (incoming and accumulating endpoints need a separate argument; under
Z = gamma both endpoints are outgoing by 4.7(v)). [repaired v41 after VER E446] The remaining local question: (T) and (V) on a whole endpoint neighbourhood (external referee endpoint1:
neither germ nor obstruction found; exact Lagrangian reduction det(X_a, X_t) = e^{4t}, K_t - 3K = G'(a) y_t, Omega = e^{-4t} K).
4.7(xii)(c) [P164 (polynomial case) CONFIRMED 12:18, P166 CONFIRMED 12:35 with only the value trace analytic; audit166 (A106)
VALID 12:36 (Neumann trace redundant); ENTERED 4.7, Summary, section 5, 6.3, Table 8.1, 12:44]: at an outgoing endpoint, in the
orthonormal (s, z) of 4.7(iv), there is no delta > 0 with z -> U(0, z) real analytic on (-delta, delta) and z -> Omega(s, z)
real analytic on (-delta, delta) for every s in (0, delta). Proof: wedge N gives Omega(s, .) = 0 on an open subinterval,
identity theorem gives W harmonic on (0, delta') x (-delta, delta), Schwarz reflection of W - A (A from the analytic value
trace) gives an analytic extension W^an through p, analytic reduced field f^an = f flat at 0, so f = 0 beyond p: contradiction.
Not derived from (T), (V): the transverse analyticity is a hypothesis. external referee endpoint2 (A105): again neither germ nor
obstruction (regular chart X(a, r), det = 1, W = 4 r X_r, compatibility Q = G'(a) int_0^1 y_r(a, r t^4) dt).
4.7(xii)(d) [external referee endlocal3 (A130) 18:47-19:03; audit_xiid (A131) VALID with fixes 19:16, all adopted; VER P199
CONFIRMED 19:24 (v2 sha 8f83b20a...); ENTERED 4.7(xii), Scope, Summary, Q1, 6.3, Table 8.1, 19:27]: at an outgoing endpoint
there is no finite separated representation W = sum_{j<=N} a_j(s) B_j(z) on S_+ = {|z| < eps, max(0, sigma(z)) < s < eps}
(a_j continuous on [0, eps), C^1 on (0, eps); B_j arbitrary). Proof: finitely many basin slices W(s_i, .) are real analytic
(W = grad H on D_+); their span gives V = W on S_+ with div V = 4, curl V = 0 on a half-rectangle (identity theorem in z);
K = V_s - i V_z + 4 i z holomorphic with analytic trace at s = 0; Morera gives an analytic W^an with the jets of W at p;
f^an flat hence 0; the analytic nullcline lies in S_+, contradiction with f > 0. Contains the polynomial case of (c) on
the basin side only; also for U. VER proved the version with arbitrary a_j (not entered). Common core of (c) and (d)
(lead remark, not entered; endlocal4 Q1): W restricted to an open subset of the basin side that accumulates at p and
contains the nullcline beyond p has no real analytic extension to a neighbourhood of p.
Type (endlocal3 D1, ENTERED 6.3 19:27, P199, A131): with X_r = rho e, alpha = X_a.X_r/rho^2, the arc-side system is, for
r != 0, rho_a = alpha rho_r - rho^{-1} phi_r + alpha rho/r - omega/(4 r rho), phi_a = alpha phi_r + rho^{-3} rho_r,
alpha_r = alpha/r - 2 rho^{-2} phi_r - omega/(4 r rho^2): an elliptic pair (speeds alpha +- i rho^{-2}) and a constraint;
full principal determinant eta((xi - alpha eta)^2 + rho^{-4} eta^2), characteristic on C = {a = 0}; at r = 0,
alpha rho^2 = omega/4. Solvability of the Cauchy problem from C not decided.
P168 [CONFIRMED by VER 12:59; audit168 (A109) VALID with fixes 13:26; ENTERED Scope of 4.7(xii), 6.3, Table 8.1, 13:27]:
in the P161 configuration (not a profile), on a small half-disk s >= 0 at either endpoint W = (Re g, 4z - Im g),
g = exp(-w^{-1/2}), w = s + i z, Omega = 0 there, while W_s(0, z) = exp(-a) cos a, a = (2|z|)^{-1/2}, is flat and nonzero
arbitrarily close to 0: the analytic value-trace hypothesis of (xii)(c) is NOT implied by the Omega hypothesis plus the
local structure (zero set, endpoint type, flatness, div W = 4). The full trace U(0, z) is not flat (normal slope 2).
4.7(xiii) [external referee incoming1 13:52 (A110, research) + lead; audit_inc1 (A113), audit_sigma (A112), audit_xiii_text
(A114) VALID with fixes, all adopted; VER P174 and P175 CONFIRMED 14:27; ENTERED 14:37]: (a) at every endpoint type, all derivatives of Theta - L and Omega vanish on the strong unstable
curve C of p (transport and the Duhamel formula along backward orbits converging exponentially to p); (b) C = {s = sigma(z)}
with sigma_{2j+3} = (-1)^j kappa^(2j+1)(0)/((2j+3)(2j+3)!) at the least odd order with kappa^(2j+1)(0) != 0 (kappa = curvature
of gamma in arclength; jets of W and C determined by the jet of gamma via formal Cauchy-Kovalevskaya; SymPy work/xiii);
(c) if C meets {s > 0} in every neighbourhood of p, (xii)(c) holds at p for every type (Omega(s, .) flat at C n {s = const}, analytic => 0);
(d) arc index (eps_- + eps_+)/2; incoming endpoints => degree 2 of W off gamma; with isolated exterior zeros an off-axis
source q, Theta = Theta(q) and Omega = 0 near q. Unresolved: incoming/accumulating endpoints with every odd derivative of
kappa zero at p, and the full class.
4.7(xiv) [external referee incoming2 (A115) + lead; audit_xiv (A116) VALID with fixes; VER P177, P178 CONFIRMED; ENTERED 15:26;
Scope example P180 ENTERED 16:00]: incoming endpoints with isolated zeros off gamma: finitely many zeros, every backward
orbit converges to a zero, K a finite tree, Theta(R^2) = Theta(gamma); both sectors beyond p near p lie in open basins
(source or index-0 zero), so Theta = L, Omega = 0 there; (c) Theta - L not constant near p; (d) (xii)(c) at p without the
condition on C; (e) C not analytic at p; (f) all-nondegenerate: no axis zero other than 0.
4.7(xv) [lead; audit_xv (A117) VALID with fixes; VER P179 CONFIRMED 15:39; ENTERED 15:46]: at outgoing endpoints (and incoming
ones with isolated zeros off gamma) neither Theta - L nor Omega vanishes identically on a neighbourhood of any point of
C^ (p and its two strong unstable orbits); U not harmonic near any such point; for Z = gamma, O_+- are components of
int{Omega = 0} and of int{Theta = L} with boundary in C^_+ u C^_-.
4.7(xvi) [lead; audit_xvi (A118), audit_xvid (A119) VALID with fixes; VER P182 CONFIRMED 16:17 (wording fix adopted);
ENTERED 16:19]: for Z = gamma, C^_+ is a smooth properly embedded line in {x > 0} (both orbits escape), C^_- = S C^_+
disjoint from it; F, O_+, O_- are the three simply connected components of R^2 minus (C^_+ u C^_-), boundaries C^_+,
C^_-, C^_+ u C^_-; F = S F contains the axis; Theta = L, Omega = 0 off F, U harmonic on O_+-; every boundary point of F
is a limit of points of F with Theta != L and with Omega != 0; directions of O_+ = int I_+, of the two C^_+ orbits = the
endpoints of I_+. (Lead heuristic, not a theorem: an exclusion in Z = gamma has to use (V) and the inverse on F.)
4.7(xvii) [lead; audit_xvii (A122) VALID with fixes, v2 text consultations/audit_xvii_text_v2.md; VER P185
CONFIRMED 16:57; ENTERED 17:00]: quasianalytic Denjoy-Carleman classes C{m} (m_0 = 1, log-convex, D_m finite, sum
m_{k-1}/m_k = infinity): Theta not in C{m}(R^2) (setting (ii)); near each endpoint Omega and U in no C{m}; Theta in
no C{m} on a connected open set containing gamma; likewise near points of C^ under the (xv) hypotheses. So a beta = 2
profile needs non-quasianalytic regularity (e.g. Gevrey s > 1 or worse) at its endpoints.
4.7(xvii)(d) [VER P186 CONFIRMED 17:09; audit_xviid (A124) VALID with wording fixes; ENTERED 17:19; summary
quantifiers repaired 17:24]: for each C{m} and each family of parallel lines transverse to a smooth open arc A of C^,
outside a meager set of lines, Theta - L and Omega restrict to flat nonzero germs and Theta, Omega, U (vector) are not
in C{m}; the scalar exceptional set does not depend on m, that of U does (countably many classes at once).
4.7(xviii) [external referee endlocal1 (A123) + lead checks; audit_xviii (A125) VALID 17:34; VER P188 CONFIRMED 17:55 with two
Scope repairs (oriented chart sense of 'outgoing'; regular analytic image germ of c), adopted in v3 sha 2d613940...;
ENTERED 17:59; VER re-read 18:02 CONFIRMED, label 'Neumann problem' replaced by 'one-sided potential Cauchy problem with
the full gradient trace' 18:06]: exact local reduction at an outgoing endpoint p: on the arc side coordinates
X(a, r), X(a, 0) = gamma(a), W o X = 4 r X_r, det(X_a, X_r) = 1, Theta o X = theta(a),
Omega o X = (theta'/4) int_0^1 u^{-3/4} y_r(a, u r) du, one curl equation
4 d_r(r X_a.X_r) - 4 r d_a |X_r|^2 = Omega o X (with converse); basin side W = grad H, Lap H = 4, d_nu H = 0 on C,
grad H(c(r)) = 4 r c'(r); gluing when theta - L is flat at p; formal normal jets along gamma unobstructed
(multiplier d_m = 4m + 1 - tau_y theta'/(4(m + 1)) > 0 for |theta'| < 4). Neither a local solution nor a local
obstruction is known.
4.7(xix) [external referee endlocal4 (A132) 19:23-19:36 + lead checks; audit_xix (A133) VALID with fixes (Scope and wording) 19:58, all
adopted in v2 sha c7972a01...; VER P203 CONFIRMED 20:04 (v2 sha c7972a01...); ENTERED 4.7, Scope of (xvii) and (xviii),
Summary, Q1, 6.3, Table 8.1, 20:09]: at an outgoing endpoint p, with O = {s > sigma(z)} the basin side, K = W_s - i W_z + 4
i z (d_wbar K = i Omega/2), S = w - K/2, R = conj S, W_s + i W_z = 2 (w - R): (a) no real analytic V equals W on a subset of
O of positive area in every disk about p; (b) no bounds |d_e^n W| <= c A^n (n!)^2 on O n B_eps in one direction e (a tangent
disk {s > L(s^2 + z^2)} in O suffices); proof: E = R o R - w = S* o S - w is holomorphic on the tangent disk D_M, flat at p,
E(s + i k(s)) = -f(s)(1 + O(s)) != 0, Gevrey-2 bounds give exp(-c/|w|) decay, half plane uniqueness after zeta = 1/w; (c)
the same for Omega on a neighbourhood of p (Gevrey-2 cutoff, Cauchy transform); (d) if tau_x(p) != 0, Omega(X(a, r)) =
theta'(a) mu(a, r), mu(0, 0) = tau_x(p), {Omega != 0} is a union of whole fibres a in J, J accumulates at 0, accumulation
directions = closed half circle {v_s <= 0}. Gevrey orders <= 2 of U or Omega near an outgoing endpoint excluded; > 2,
smoothness, sectors and lines not.
4.7(xix)(e) [lead derivation from the proofs of (xix)(a)-(c) and (xiv)(b); audit_xixe (A134) VALID with fixes (Scope clause
on profiles without an outgoing endpoint deleted), adopted in v3 sha 8b473871...; VER P204 20:29 CONFIRMED v3; ENTERED
20:35]: at an incoming endpoint with every zero of W off gamma isolated, (xix)(a)-(c) hold with O replaced by O' = {s >
sigma(z)} (Omega = 0 there by (xiv)(b)); with f < 0 the segment [kappa(s), kappa(s) + |f(s)|/2] lies in {Re w >= s}. (d) is
not extended.
4.7(xx) [external referee endacc1 (A135) 20:27, center-phase proof; lead barrier proof (strong unstable curve C_1 of a nearby zero q_1,
constructed in the original coordinates); audit_xx (A136) VALID; VER P206 20:55 CONFIRMED v3 sha bebc94b3...; ENTERED
20:56]: at an accumulating endpoint p, (a) Theta - L vanishes on no neighbourhood of p (no hypothesis). If F = {s in (0,
eps): f(s) = 0} has empty interior (no arc of zeros of W off gamma near p): (b) Theta = L, Omega = 0 on N n (C u O'), O' =
{s > sigma(z)}, U harmonic on N n O', zeros of f in F isolated; (c) Theta not constant on any subarc of gamma ending at p,
(xiv)(d), (e) hold; (d) (xix)(a)-(c) hold with O replaced by O'. Barrier R = {0 < u < sigma_1(v), |v| < rho_1} is backward
invariant; alpha-limits are single zeros; g d_u Theta(u, 0) = 0 gives Theta(u, 0) = L. Open: accumulating endpoints with
arcs of zeros, incoming endpoints with nonisolated zeros (for the subarc form).
4.7(xxi) [lead derivation; audit_xxi (A137) VALID WITH FIXES (also a corollary of (vii): E open dense, Theta = h(arg Phi) on
E, det D Phi = 1); audit_xxi2 (A138) VALID; VER P207 21:14 CONFIRMED v2 sha 49379c35...; ENTERED 21:17]: if Theta is
constant on a nonempty open set D, the union V of the orbits through D is open and invariant, Theta is constant on V, Omega
= 0 on V, U harmonic on V. Proof: complete flow, Theta_x = 0 on V, Omega(Y) = e^{-T} Omega(phi_{-T} Y), backward orbits
bounded (W.X >= |X|^2 for |X| >= R). Consequence with (xii)(a): Theta - L vanishes on no neighbourhood of any endpoint, of
any type. Fails for local solutions (W = (-x/2, 9y/2 - x^3/3), Omega = x^2, Theta = 0). Open: the subarc form of (xii)(b) at
incoming endpoints with nonisolated zeros and at accumulating endpoints with arcs of zeros; open sets with Theta = L whose
closure contains an endpoint.
Local families at beta = 2 [external referee endlocal2 (A128) 18:39 + lead check; audit_int1 (A129) VALID with fixes 18:44;
VER P195 CONFIRMED 18:58; ENTERED 6.3, 18:59]: for every smooth h, W = (0, 4y - h(x)), Theta = L + h(x), Omega = h'(x) satisfy
div W = 4, Omega = -curl W, (T), (V) on R^2 with zero set y = h(x)/4; W = (4x, 0), Omega = 0, Theta = t(y) for every
smooth t (also t in no Gevrey class). Hence the local equations force no analyticity or Gevrey regularity of gamma or of
the temperature trace at interior points of the arc; these are not profiles. endlocal2 found neither a local solution
nor an obstruction at an outgoing endpoint. With W = (0, 4z) + grad^perp phi near gamma: phi_s = 4k, phi_z = 0 on gamma
(phi not constant there); K = W_s - i W_z + 4 i z = 4 i k(s) on gamma.
OPEN: beta > 2 slow tail (the main gap; within it G); beta = 2 arc with two flat endpoints (non-quasianalytic at the
endpoints by (xvii)); local solvability at an outgoing flat endpoint (reduced to the system of (xviii); restricted exclusions (xii)(c), (d) and (xix)(b), (c): Gevrey orders <= 2 excluded at outgoing endpoints and, by (xix)(e), at incoming endpoints with isolated zeros off gamma, and, by (xx)(d), at accumulating endpoints without arcs of zeros off gamma nearby).

## 4. Consequences for the numerical search

- Search ONLY beta >= 2 for the free-beta problem. Any candidate with beta < 2 is an artifact of a finite box or of
  a non-canonical inverse; if one appears, check W.X at the outer radius and the inverse closure.
- beta = 2 (bounded Theta) is a separate, highly constrained branch: test it as a fixed-beta run and report whether
  W develops a curve of zeros through 0 tangent to the x-axis.
- beta > 2: Theta grows like r^{1-2/beta} Theta_hat(phi); on the basin of the origin Theta >= 0 (a0 = 1), zero only on
  the y-axis. Use this as a diagnostic (not an imposed constraint).
- Fixed-beta scans should include several beta in (2, 4], e.g. 2.25, 2.5, 2.9, 3.5, plus free beta.
- Every candidate must have the slow tail: int_{B_R cap {x>0}} (Omega)_+ >= c R^{2-1/beta} (4.9, a0 = 1). A basis whose
  vorticity decays faster than r^{-1/beta} uniformly (including r^{-2/beta}) can only produce artifacts. With G = Omega/x,
  G must decay like r^{-1-1/beta} (not faster). Diagnostic: the material circulation of the small center rectangle grows
  like e^{(2beta-1)t} with A_D > 0; equivalently, the right half-ball positive vorticity mass grows like R^{2-1/beta},
  and this mass lies in a fixed sector away from the y-axis (4.11), so check the ray exponent -1/beta at angles
  strictly inside x > 0 (e.g. theta = 0, pi/4), not only near the axis.
- Mechanism (lead pilot): with a0 = 1, the buoyancy-generated vorticity in the flow of a rising dipole above the center
  has center strain of the wrong sign (c_self ~ -0.10 vs external 2.5): passive feedback is negative, which explains the
  collapse of time-marching runs. Correction (verifier 18:54Z): the signed spatial scaling U_l(X) = l U(X/l) leaves the
  center strain unchanged (DU_l(0) = DU(0)) for every real l != 0, so it cannot turn c_self < 0 into c_ext > 0. At eps = 0
  the passive problem is linear in (Theta, Omega), so one may first multiply them by k = c_ext/c_self (then c_self = c_ext)
  and afterwards apply the scaling l = k to restore a0 = 1 (this moves and rescales the external dipole). These are two
  operations; the amplitude multiplication is NOT a symmetry of the nonlinear self-consistent (B2-P). Forcing homotopy: W_eps = beta X + U_rel[eps Omega + (1-eps) Omega_ext], eps: 0 -> 1.

## 5. Far-field model (derived from the PDE for W = beta X + O(r^{1-delta}))

Along escaping orbits |phi_t Y| ~ C e^{beta t}. Leading terms (phi = polar angle from the x-axis):
  Theta ~ r^{1 - 2/beta} Theta_hat(phi),
  Omega ~ r^{-1/beta} Omega_hat(phi) + r^{-2/beta}(...)   [homogeneous solution of W.grad + 1 dominates the
          particular part -Theta_x; its coefficient I(Y) = int_R e^s Theta_x(phi_s Y) ds is generically nonzero],
  Psi_rel ~ r^{2 - 1/beta} P_hat(phi),  P_hat'' + (2 - 1/beta)^2 P_hat = -Omega_hat,
  U_rel ~ r^{1 - 1/beta}, sublinear (consistent with A4).
RIGOROUS (4.12 [V]): Omega = r^{-1/beta}(a(theta) + o(1)) uniformly, a continuous, not identically 0; Theta =
  r^{1-2/beta}(A(theta) + o(1)) uniformly (4.10 [V]); ALONG ESCAPING ORBITS Omega = e^{-t} A - e^{-2t} g + ... (4.6).
FORMAL NEXT ORDER (lead notes/farfield_expansion.md; agrees with verifier packet 35; signs VALID by external referee auditL): nu = 1/beta, m = 1 - 2 nu,
  Psi_rel = r^{2-nu} psi0 + ..., psi0'' + (2 - nu)^2 psi0 = -a (unique for beta >= 2), v_r = -psi0', v_theta = (2-nu) psi0,
  Theta = r^m A + r^{m-nu} F1 + ...,  F1 = m v_r A + v_theta A',
  Omega = r^{-nu} a + r^{-2nu} a1 + ...,  a1 = -nu v_r a + v_theta a' - m cos(theta) A + sin(theta) A'.
  Restricted recursion (auditL (18)-(20)): degree-k transport multipliers are -k, logs only from the elliptic inversion
  (rational beta necessary, not sufficient). NOT exhaustive: a constant velocity term c at infinity (not removed by the
  normalization at 0) induces degrees m - 1 and -nu - 1 with coefficients (1/beta) c.grad(r^m A), (1/beta) c.grad(r^{-nu} a);
  decaying harmonic exterior velocity terms induce further powers. A finite-box closure
  should impose these two leading tails with FREE angular profiles (a, A) and the algebraic next-order terms.
Older heuristic (kept for reference): the fixed-angle
  form Omega ~ r^{-1/beta} A_hat + r^{-2/beta} (-d_1 Theta~) + ... (Theta~ = Theta o Phi^{-1}, homogeneous of
  degree 1-2/beta) omits the velocity part of a1;
  g = d_1 Theta~ is never identically zero for a nontrivial profile (Theorem E); A_hat is free (fixed by the core).
Next corrections are relative O(r^{-1/beta}) (from U_rel/(beta r)); expect expansions in powers of r^{-1/beta}.
Exponents are functions of the unknown beta derived from the PDE; they are not fitted constants.
Angular content: Omega odd under phi -> pi - phi, so its Fourier modes are cos(n phi), n odd, and sin(n phi), n even.

## 6. Canonical inverse in practice

Option 1 (polar, modal Green formula; recommended for the verifier). For an angular mode n of Omega (omega_n(r)),
  n >= 2: psi_n(r) = (1/(2n)) [ r^{-n} int_0^r rho^{n+1} omega_n drho + r^n int_r^infty rho^{1-n} omega_n drho ],
  n = 1 (cos phi mode; twice subtracted): psi_1(r) = (1/2) [ r^{-1} int_0^r rho^2 omega_1 drho - r int_0^r omega_1 drho ].
  For n >= 2 the tail integral converges for Omega ~ r^{-1/beta}; the part beyond the computational radius R must be
  supplied by the far-field model of section 5 (and its error reported), not set to zero.
Option 2 (Cartesian/quadrature): the once-subtracted kernel of (A4), with an analytic far-field tail beyond the box.
Forbidden: Dirichlet/Neumann/periodic box inverses presented as the physical inverse; upper-half-plane inverses;
any condition at y = 0.
Option 3 (transport-exact mixed-chart generating function; lead pilot, optional, G_+ only). Valid only in G_+ (W has
no zero but the center, Theta_x > 0 on x > 0, a0 > 0). Unknown S(xi, y), odd in xi, with x = S_y, eta = S_xi,
J = S_{xi y} > 0, where xi, eta are the global linearizing coordinates (Theta = a0 xi^2). Then the temperature
equation holds identically, V = (q S_xi - p xi S_{xi xi})/J, W1 = J p xi + S_yy V, Psi = beta (2 - E) S with
E = a xi d_xi + y d_y, a = 1/2 - 1/beta, p = beta/2 - 1, q = 3 beta/2 + 1, and the only equation left is the vorticity
residual R = p xi Omega_xi + V Omega_y + Omega - 2 a0 xi/J (Omega = -Lap Psi in (x, y)); use the divided form
R/xi = (p+1) H + p xi H_xi + V H_y - 2 a0/J, H = Omega/xi. Normalization S_xi(0,0) = 0, S_{xi y}(0,0) = 1, a0 = 1,
beta free. Audited (external referee genfn1): identities valid; resonances of the linearization beta = 2 + 8/(n-3), n >= 4 even;
J > 0 alone does not give completeness of (xi, y) -> (x, eta) (S = xi arctan y); the far-field expansion of S is
conditional (degree-one term, logarithms, nondegeneracy) and no index count is established. Center constraint
beta q P_vv(1,0) + 8 P_t(1,0) = 4 a0 for S = xi R^{2-a} P(t, v). A state from this route still needs the full prompt
diagnostics (section 7) with an independent whole-plane inverse; the generating function itself is not a proof of
anything.
Verifier packet 100 (01:13Z) CONFIRMED the mixed-chart formulas, including the correction for the resonant term
kappa xi^k of 4.18(b); a smooth global linear chart (as assumed by this option) exists only when kappa = 0, which is
automatic for nonresonant beta (beta != 2 + 8/(k - 3), k >= 4 even) but not otherwise; J > 0 without properness is
insufficient. Pilot outcome (01:37Z, notes/genfn_formulation.md): no candidate; lam = 0 states have 15-30 percent RMS
normalized residual and Omega < 0 on part of {x > 0}; pilot closed.
Option 4 (dynamic rescaling, lead pilot, closed). Polar mapped Chebyshev (r = L tan(pi rho/2)) times Fourier with the
B2 parities, stable modal Green recurrences (Option 1 evaluated by forward/backward interval recurrences; the direct
r^{+-n} form overflows), normalization Theta_xx(0) and Omega_x(0) frozen, so c_l = 2 Theta_xx(0)/Omega_x(0),
c_w = c_l/2 - c and a steady state with c_w < 0 is a profile with beta = -c_l/c_w. Outcome (notes/dr_pilot.md): time
stepping from more than 21 initial data sets loses the center strain c within tau of 0.5 to 2 (c_w turns positive);
steady Newton and Newton homotopies give no candidate (loss of Omega > 0 and Theta_x > 0 on x > 0, residuals of order
one). Pilot only; nothing from it is a claim.
Verifier packet 110: the modal inverse is not accurate on slow tails (strain 1.516 to 1.566 instead of 1.5 for
Omega = 2xy(1 + r^2)^{-7/6}; the interpolated source does not vanish at the compactified endpoint). A tail-aware
source representation is required before any reuse. Option 5 (separate stream-function trial space with exact
canonical inverse, verifier packet 108): sixteen least-squares fits at beta 2.25 to 4.25, no candidate; closed.

## 7. Identities and diagnostics to report

1. c = Psi_rel_xy(0) = (1/pi) int x y Omega / r^4 dX (absolutely convergent) must equal 1 + beta/2 (a0 = 1).
2. G(0,0) = 4/beta; F(0,0) = 1; H_rel(0,0) = 0.
3. Residuals R_Omega = W.grad Omega + Omega - Theta_x, R_Theta = W.grad Theta - (beta-2)Theta, E = -Lap Psi - Omega,
   with the prompt's pointwise normalizations N_Omega, N_Theta (state how zeros of N are handled; no large floors);
   desingularized residuals R_F, R_G, R_H of (B2-red), including their limits on the y-axis (s = 0) and at the center.
4. beta, DW(0) eigenvalues, stagnation points of W (locations, DW there), sign of W.X on large circles.
5. Far field: fitted exponents of Theta, Omega, U_rel versus 1-2/beta, -1/beta, 1-1/beta; truncation error of the
   inverse versus outer radius R; v0(R).
6. Theta >= 0 on the basin of the origin (beta > 2); the zero set of Theta; the curve of zeros of W (beta = 2).
7. Axis: zeros of b = W_2(0,y) with b' there (compare with the resonance list of section 3), the third-order center
   condition defects a'(0) - 4 b''(0) a0/Lambda and (2 beta + 1) q'(0) - b''(0)(q(0) + 8 a0/Lambda), where
   Lambda = 3 beta + 2 = 2(beta + c) and b''(0) is the second derivative (b = (Lambda/2) y + (b''(0)/2) y^2 + ...).
   These coincide with the numerics lane's D1, D2 written with Lam = beta + c = Lambda/2 and h02 = b''(0)/2.
8. Critical flux: int_{B_R} |Omega|^{2 beta - 2} Omega Theta_x versus (1/2) int |a|^{2 beta} d theta, a from the fitted
   tail r^{1/beta} Omega; at finite R the exact disk identity is
   2 beta int_{B_R} |Omega|^{2 beta - 2} Omega Theta_x = int_{|X| = R} |Omega|^{2 beta} W.e R d theta.
9. Quotient identities (beta > 2, FINAL_REPORT 4.17): normalized defects of int_{x>0}(1+v)P^2 = 0 and
   int_{x>0}(1+v)Q^2 = int_{x>0} Q(2P + x P_x), with v = V_1/x from the state's own whole-plane inverse; on a disk the
   exact versions keep the outer flux int_{|X| = R, x > 0} W.e P^2 R d theta (and the same with Q^2).
10. Axis tails (FINAL_REPORT 4.21): on each half-axis without a zero of b, report |y|^{1+2/beta} Theta_xx(0, y) and
   |y|^{1+1/beta} Omega_x(0, y) for |y| from 10 to the largest resolved radius (limits P, Q > 0 required), and compare
   Q with -a'(pi/2) (upper) or a'(-pi/2) (lower) and P with h''(+-pi/2), a and h from the fitted angular tails.
11. Strain identity and residue (FINAL_REPORT 4.23): with V from the state's own whole-plane inverse, report the
   normalized defect of pi (1 + beta/2) = int Omega V.grad K_c - (1/2) int Theta V.grad(d_x K_c) (grouped kernel or
   disk truncation with the outer boundary terms of 4.23 proof (a), which are O(R^{-d}) and O(R^{-2d})), and of the
   k0 residue identity for phi = cos theta and phi = sin 2 theta (both odd in x). These are necessary conditions only: a
   smooth field satisfying (S) need not solve (V), (T) (4.23(c)), so only a verified failure is informative.
12. Representation constants (FINAL_REPORT 6.1, notation b_rep, s_rep = 1/b_rep, C_rep, alpha_rep): for a state stored
   with b_rep = beta, report C_rep (2 < beta < 3, closed form of 6.1; 3 < beta < 4, the three-term formula of 6.1, packet 111; other
   noninteger beta > 3 by 4.26(d) with N = floor(beta) subtracted terms) and, at
   b_rep = beta = 3, alpha_rep = L^2 S''(1)/2. A nonzero value excludes that stored field as an exact profile. Along a
   continuation path it is a representation diagnostic only: without uniform tail control a sequence can converge in
   compact or weighted norms, or in normalized residuals, while C_rep stays away from 0 (verifier packets 94, 96).
13. Axis slope (verifier packet 107): on a zero-free half-axis Q_+ is a functional of b = W_2(0, .) alone, increasing
   in b; the axis system gives no a priori bound on it, so Q_+ is a consistency diagnostic, not a target.
   The axis subsystem is moreover compatible with positive canonical vorticity, the slow tail and the center strain
   (FINAL_REPORT 6.2, packet 106, external referee audit106); it supplies no Theta and no off-axis transport.

## Change log
- v1 2026-10-20 13:03Z: first version.
- v2 2026-10-20 13:17Z: added Theorem E (restricted-class exclusion, integrable vorticity tails) and the precise
  two-term far-field structure of Omega.
- v3 2026-10-20 14:10Z: A5 observer change corrected (theta, omega translated); verification status of section 3;
  Theorem E as audited ((H1'), trajectory-only expansion); 4.7 beta = 2 analytic/flat jet; 4.8 mass bound; translation
  eigenmode (research/10 wording); numerics notes (tail requirement, negative passive feedback, forcing homotopy).
- v4 2026-10-20 14:42Z: Theorem 4.9 (circulation mass bound, verified): critical r^{-2/beta} tail excluded, slow tail
  r^{-1/beta} required (positive part, right half-ball); L^p exclusion 1 <= p <= 2 beta under U = o(r); 4.8 L^p
  extension and referee F angular Theta limit marked verified.
- v5 2026-10-20T15:09Z: Theorem 4.11 (sector circulation, drift integral absolutely divergent in class A, A not identically 0
  under (H1), flat Omega at the beta = 2 flat zero), A5 updated accordingly; A2 regularity wording corrected
  (verifier note 15:02Z).
- v6 2026-10-20T15:30Z: Theorem E with (D) (orbit-integral) replacing (H1); axis structure block (pending verifier);
  third-order center condition and axis diagnostics (section 7 items 7).
- v8 2026-10-20T16:26Z: auditL result; D'' and beta = 2 class extensions (pending verifier); beta2c research.
- v7 2026-10-20T16:13Z: Theorem D (4.12, verified): automatic (D), sharp slow polar tail in class A; Theorem D'
  (pending); rigorous far field and formal next order in section 5; observer convention selected in (A5).
- v9 2026-10-20T16:48Z: class reduction 4.15 and second far-field terms 4.16 verified and entered; sign 4.12(f); packet 40
  (polynomial vorticity) pending audit40; beta = 2 arc structure and critical identity (pending).
- v10 2026-10-20T16:55Z: audit40 VALID; polynomial vorticity entered as 4.15(iii); class A = broad target. FINAL_REPORT
  section 6 now has the numerical residual tables (verifier audits), strategies ruled out and main obstacles.
- v11 2026-10-20T17:08Z: beta = 2 arc 4.7(iii)-(iv) and critical identity 4.12(g) verified and entered; diagnostic 8.
- v12 2026-10-20T17:46Z: 4.17 (divided fields, quadratic identities) and 4.18 (global source) verified and entered;
  diagnostic 9.
- v13 2026-10-20T19:01Z: verifier 18:54Z convention audit adopted: global-source coordinates may contain the even resonant
  term (C^1 linear conjugacy only), and the signed-scaling remark in section 4 corrected (scaling does not change strain).
- v14 2026-10-20T19:19Z: section 3 summary lines for 4.19 (zeros off the center) and the weak-sign results
  4.7(viii)-(x), 4.20 (4.20 entered 19:19Z after verifier packet 60 and external referee auditY).
- v15 2026-10-20T20:00Z: section 3 summary line for 4.21 (axis tails and vertical slopes; entered 20:00Z after external referee
  audit421, verifier packet 65 and external referee audit421b) and diagnostic 10.
- v16 2026-10-20T20:06Z: section 3 summary line for 4.22 (temperature tail in G; entered 20:06Z after verifier packet 66,
  verifier re-read 20:00Z and external referee audit66).
- v17 2026-10-20T21:07Z: section 3 summary line for 4.23 (homogeneous weights, strain identity, residue, restricted
  exclusions; entered 21:06Z after external referee strain1, verifier 20:46Z and 20:59Z, external referee audit423 and audit423b) and
  diagnostic 11.
- v20 2026-10-21T02:21Z: section 6 Option 4 (dynamic-rescaling pilot, closed, no candidate).
- v21 2026-10-21T02:39Z: section 7 diagnostics 12 (representation constants; diagnostic only along paths) and 13 (axis slope).
- v22 2026-10-21T02:58Z: diagnostic 12 extended to 3 < beta < 4 (packet 111 formula, four native lambda-path constants
  entered in FINAL_REPORT 6.1 at 02:55Z); diagnostic 13: axis-subsystem compatibility (6.2 bullet entered 02:55Z);
  section 6 Option 4 packet-110 caveat and Option 5 (packet 108, closed).
- v19 2026-10-21T01:38Z: section 6 Option 3: packet 100 caveat (kappa = 0 needed for a smooth chart), pilot closed.
- v18 2026-10-21T01:14Z: section 3 summary lines for 4.24-4.27 (entered in FINAL_REPORT 23:01Z-00:23Z after verifier
  confirmation and external referee audits); section 6 Option 3 (mixed-chart generating function, G_+ only, audited caveats from
  external referee genfn1).
- v23 2026-10-21T05:07Z: section 3 summary lines for 4.28, 4.29 (entered) and 4.30 to 4.32 (entry pending).
- v24 2026-10-21T05:25Z: 4.30, 4.31(a), 4.31(b) (prescribed disk plus whole axis), 4.32 entered; summary line updated.
- v25 2026-10-21T07:20Z: section 3: stale 'bounded set exclude nothing / (V) on unbounded open sets' sentence replaced by the
  compatibility summary of FINAL_REPORT (end of 4.31) and summary lines for 4.33 to 4.35 (verifier 07:12Z request).
- v26 2026-10-21T07:27Z: section 3: 4.32(d) (converse of the compatibility identity) and 4.33(e) (horizontal offsets).
- v27 2026-10-21T07:46Z: section 3: beta > 2 stated for the global analytic converse of 4.32(d), beta = 2 marked OPEN
  (verifier 07:38Z precision note); the local smooth part holds for every beta > 0.
- v28 2026-10-21T08:17Z: section 3: compact modifications of 4.34 (6.3): the compact conjugacy and the invariant
  x-moment of the vorticity residual (packets 140, 142; audits A84, A87).
- v29 2026-10-21T08:42Z: COMPACT MODIFICATIONS (c) large-R x-moment of the 4.34 residual (verified, in report 6.3);
  (d) draft 4.36 renormalized impulse (under verification).
- v30 2026-10-21T09:04Z: COMPACT MODIFICATIONS (d): 4.36 verified and entered (first formula [rho^0 (log rho)^0] F_rho for
  all beta > 2; dipole form outside Z_crit; x R_Omega in L^1 suffices).
- v31 2026-10-21T09:22Z: 4.36 as entered re-read and CONFIRMED by VER (09:14). Section 4: the beta-parameterized K 32 run
  (beta 3.024 to 3.062, lambda 0.9400 to 0.9317 by shrinking steps, forced ratios growing to 0.068/0.11) is in the report
  (6.1) as under-resolved; the K 40 checkpoint decides whether the levelling of lambda survives resolution. Under study
  (external referee energy437, not verified): renormalized energy f.p. int (|V|^2/2 + y Theta) from int Psi R_Omega.
- v32 2026-10-21T09:41Z: section 3 COMPACT MODIFICATIONS (e) finite exterior expansion (P150 CONFIRMED by VER; D = 0 for
  all class A profiles outside Z_crit once entered) and (f) renormalized energy draft (under verification and audit).
- v33 2026-10-21T09:58Z: section 3 (e), (f) entered as 4.37, 4.38 (verified and audited); P152 noted.
- v34 2026-10-21T10:26Z: section 3 (g) (4.34(iii) temperature derivative bounds; zero-moment signed configurations; non-invariance
  of the f.p. energy) entered in 6.3; numerics (report 6.1): lineage 2 stage lambda 0.98 failed (none of seven reported states met the
  center-strain condition; the saved one at beta 3.0415 VER-checked, E354); no fold or root exclusion established.
- v35 2026-10-21T10:53Z: section 3 (h) every real f.p. energy on the zero-moment nonprofiles (P154, P155; in report 6.3); BETA = 2 LOCAL
  REALIZATION (P156) noted, under audit, not entered; numerics: K40 beta 3.0315 checkpoint rejected by VER (E365: forced F/G
  0.00240/0.00559 vs K32 0.00957/0.0181, self 0.736/0.449; exact tail gives an infinite absolute thermal residual).
- v36 (2026-10-21T11:07Z): P156/P158 entered (6.3 beta = 2 bullet, Summary open core, Table 8.1 row 4.7(iii)-(iv)); endpoints outgoing, (V) fails on a nonempty open invariant set at each endpoint; strong unstable curve straight, so 4.7(vi) not met by the construction.
- v37 (2026-10-21T11:40Z): P159 entered (6.3 beta = 2 bullet, Summary open core, Table 8.1); P161 noted under VER check; endpoint1 result recorded.
- v38 (2026-10-21T11:56Z): P161 CONFIRMED by VER (not entered, audit161 running); draft 4.7(xii) (no harmonic and no isothermal endpoint neighbourhood) under check.
- v39 (2026-10-21T12:14Z): 4.7(xii) and the P161 6.3 paragraph entered (audit161 = A104: (a), (b), equivalence, construction VALID; the exception '(V) not asserted to fail on O' removed); VER 12:08 repairs to the P147/P148 summary in 6.3 adopted. Remaining beta = 2 local question unchanged: (T) and (V) on a whole endpoint neighbourhood with Theta - L flat and not identically 0.
- v40 (2026-10-21T12:45Z): 4.7(xii)(c) entered (P164, P166, A106): analytic value trace on the normal line through an outgoing endpoint plus analytic Omega on the parallel lines beyond it is impossible. 6.3 records that two local consultations (A101, A105) found neither a local solution nor an obstruction.
- v41 (2026-10-21T13:33Z): P168 entered (Scope of 4.7(xii), 6.3; A109 VALID with fixes); 4.7(xii) summary in section 3
  repaired (Theta = L premise excludes only outgoing endpoints; VER E446); numerics: beta = 3.25 entered (state 12 of the
  second path, center thermal limit 0.606 > 3/5), beta = 3.3 no accepted state (clipped evaluations not roots); K32 states at
  beta = 3.0925, 3.085 entered (E447, E448: center limits 0.635, 0.637 > 3/5; lambda at 3.0925 inherited from K24); P169: the
  stored spline fields are not C^5 at interior knots (representation property only).
- v42 (2026-10-21T14:03Z): candidate 4.7(xiii) recorded (not entered); K32 beta = 3.1, 3.11 and referee13 adopted in the report.
- v43 (2026-10-21T14:37Z): 4.7(xiii) entered (P174, P175 CONFIRMED; A112 to A114 VALID with fixes); external referee incoming2 (backward
  basins at an incoming endpoint) running.
- v44 (2026-10-21T14:57Z): external referee incoming2 answered (A115): under incoming endpoints and isolated zeros off gamma, both exterior
  sectors at each endpoint lie in open basins (Theta = L, Omega = 0 beyond C), with the (xii)(b), (xii)(c), (vi)
  analogues and the hyperbolic axis corollary; candidate 4.7(xiv) drafted (work/enter_xiv), audit_xiv asked, VER
  packet P177 in progress; not entered. Numerical searches: no change to the admissible class or the inverse.
- v45 (2026-10-21T15:22Z): audit_xiv (A116) VALID with fixes, adopted in the (xiv) draft; VER P177 CONFIRMED the (xiv)(b)
  conclusion, (d) and (e); the rest of (xiv) waits for VER 178. New candidate 4.7(xv) (beta = 2; outgoing endpoints,
  or incoming with isolated zeros off gamma): Theta - L and Omega do not vanish identically near any point of the
  strong unstable orbits C^; for Z = gamma the endpoint basins are components of int{Omega = 0} and int{Theta = L}.
  Audit asked; not entered. No change to the admissible class, the inverse or the normalization.
- v46 (2026-10-21T15:27Z): 4.7(xiv)(a) to (f) entered in the report 15:26 (VER P177, P178 CONFIRMED; A115, A116); its Scope example (planar field with four sources and two saddles) held back until verified. Last four K24 left states (beta 3.05 to 3.0) entered 15:24 (E485, E493). No change to the admissible class, inverse or normalization.
- v47 (2026-10-21T15:48Z): 4.7(xv) entered in the report 15:46 (VER P179 CONFIRMED 15:39; A117 fixes adopted). New candidate
  4.7(xvi) (Z = gamma: C^_+ is a properly embedded line in {x > 0}; F, O_+, O_- are the three simply connected
  components of the complement of C^_+ u C^_-, with boundaries C^_+, C^_-, C^_+ u C^_-; axis in F; Theta = L and
  Omega = 0 off F): audit_xvi asked 15:48, VER packet requested; not entered. No change to the admissible class, the
  inverse or the normalization.
- v48 (2026-10-21T16:20Z): 4.7(xvi) entered in the report 16:19 (VER P182 CONFIRMED 16:17 with a wording fix; A118, A119
  fixes adopted); section 3 now lists 4.7(xiv), (xv), (xvi). Research consultation zgamma1 (global restrictions under
  Z = gamma) running. No change to the admissible class, the inverse or the normalization.
- v49 (2026-10-21T16:57Z): referee14 adopted in the report 16:50 (open parts O_+- of the basins distinguished from the
  full basins; notation in the Summary); candidate 4.7(xvii) recorded in section 3 (audited, VER pending, not entered);
  endlocal1 asked. No change to the admissible class, the inverse or the normalization.
- v50 (2026-10-21T17:05Z): 4.7(xvii) ENTERED 17:00 (VER P185 CONFIRMED 16:57); K40 beta = 3.062 (E530) entered 17:03 in
  section 6.1 of the report (fourth 32/40 comparison: lambda agrees to 2.4e-8, C2 differs by 2.4 percent). No change
  to the admissible class, the inverse or the normalization.
- v51 (2026-10-21T17:25Z): 4.7(xvii)(d) ENTERED 17:19 (VER P186, A124) with the 17:24 quantifier repair in section 5 and
  the timeline of the report; candidate 4.7(xviii) (exact local reduction at an outgoing endpoint, from endlocal1)
  recorded in section 3 (audit and VER pending, not entered). No change to the admissible class, the inverse or the
  normalization.
- v52 (2026-10-21T18:07Z): 4.7(xviii) v3 ENTERED 17:59 (VER P188, A125), basin-problem label repaired 18:06 after the
  VER re-read; K40 state at beta = 3.092 (E557) entered in 6.1 at 18:00. No change to the admissible class, the inverse
  or the normalization.
- v53 (2026-10-21T18:43Z): referee16 (A127) items 1-4 adopted in the report 18:38; 4.14(j) sentence on arXiv:2201.06780v3
  (reported beta = 2.917 +- 0.002, half plane with wall) entered 18:42 (VER P192, A127); endlocal2 local families
  recorded in section 3 (not entered). No change to the admissible class, the inverse or the normalization.
- v54 (2026-10-21T19:28Z): 4.7(xii)(d) and the 6.3 type statement entered 19:27 (A130, A131, P199); local families of
  endlocal2 recorded as entered (18:59, P195, A129); registry kinds of A91, A96, A100, A103, A107 repaired (targeted
  review). No change to the admissible class, the inverse or the normalization.
- v55 (2026-10-21T20:10Z): 4.7(xix) (continuation, Gevrey-2 exclusion and vorticity support at an outgoing endpoint) entered
  20:09 (A132, A133, P203). No change to the admissible class, the inverse or the normalization.
- v56 (2026-10-21T20:35Z): 4.7(xix)(e) ((xix)(a)-(c) at incoming endpoints with isolated zeros off gamma) entered 20:35
  (A134, P204). No change to the admissible class, the inverse or the normalization.
- v57 (2026-10-21T20:56Z): 4.7(xx) (accumulating endpoints) entered 20:56 (A135, A136, P206). No change to the admissible
  class, the inverse or the normalization.
- v58 (2026-10-21T21:17Z): 4.7(xxi) (open sets on which Theta is constant) entered 21:17 (A137, A138, P207), with the Q1
  sentence on the scattering identities corrected ((vii) holds without Z = gamma). No change to the admissible class, the
  inverse or the normalization.
- v59 (2026-10-21T21:36Z): referee17 wording items entered 21:35 (P209); no change to the admissible class, the inverse or
  the normalization. Research consultation subarc1 (second form of (xii)(b) at incoming endpoints with nonisolated zeros
  off gamma and at accumulating endpoints with arcs of zeros) asked 21:30.
- v60 (2026-10-21T22:05Z): finite-difference Jacobian diagnostics (P208, P211) entered 22:05 in 6.1, Table 6.1c and
  section 7; no change to the admissible class, the inverse or the normalization. Candidate 4.7(xxii) (restricted
  results of subarc1) under audit and verification (P214).
- v61 (2026-10-21T22:18Z): 4.7(xxii) entered 22:18 (P214 v2, A141); no change to the admissible class, the inverse or the
  normalization.
- v62 (2026-10-21T22:50Z): equal-count comparison at lambda = 0.95 (P215, P219) entered 22:49 in 6.1, Table 6.1c and
  section 7; no change to the admissible class, the inverse or the normalization. VER theorem P218 (no profile-type
  field with Theta = H(x/a(y)), a > 0 of class C2 on R, H'(k_j) != 0 for some k_j -> +infinity) is a candidate
  restricted exclusion, pending an analytic audit and an entry check.
- v63 (2026-10-21T23:09Z): the referee18 adoptions (P221) entered 23:08 (Summary and 6.1 qualifiers, identifiers,
  section 7); no change to the admissible class, the inverse or the normalization. P218 drafted as 4.7(xxiii) with a
  part (b) from the audit (nonconstant H, rho bounded above on a half-line, W = 2X + o(|X|)); text under audit and VER P222.
- v64 (2026-10-21T23:33Z): 4.7(xxiii) entered 23:32 (P222 23:02 to 23:31, A143 and A144 adopted); a candidate exclusion of the
  whole family H(x/rho(y)) under (V) (work/sepV/NOTES.md, lead derivation, unverified) sent to verification and audit.
- v65 (2026-10-22T00:02Z): 4.7(xxiv) entered 00:01 (P227 23:40 to 23:59, A145 and A146 adopted); no change to the
  admissible class, the inverse or the normalization. Candidate 4.39 (P226, P228: restricted temperature representations) under audit.
- v66 (2026-10-22T00:26Z): 4.39 entered 00:25 (P228 (a), P226 (b), A147 VALID, P232 00:17 to 00:23); no change to the
  admissible class, the inverse or the normalization. Candidates 4.40 (P229, A148 VALID) and 4.41 (P230, P231: finite axis jets) next.
- v67 (2026-10-22T00:34Z): 4.40 entered 00:34 (P229, A148 VALID, P233 00:24 to 00:33); no change to the
  admissible class, the inverse or the normalization. Candidate 4.41 (P230 (a), P231 (b); A149, A150 VALID) next.
- v68 (2026-10-22T00:45Z): 4.41 entered 00:44 (P230 (a), P231 (b), A149 and A150 VALID, P235 00:35 to 00:37); no change
  to the admissible class, the inverse or the normalization. Lead candidate: 4.41 on the axis component J of
  {Theta_xx(0, .) != 0} containing 0 (work/z441/NOTES.md), under audit.
- v69 (2026-10-22T01:40Z): 4.42 entered 01:40 (P237, A151 VALID, P243 01:26 to 01:31); no change to the
  admissible class, the inverse or the normalization. Candidate 4.43 (beta > 2: I_2 and I_3 not both constant on J,
  no bounds at infinity; work/z442/NOTES.md, A152 VALID) awaits P242.
- v70 (2026-10-22T02:09Z): 4.43 entered 02:09 (A152 VALID; P242 CONFIRMED 01:52; P246 01:43 to 02:00); no change to the
  admissible class, the inverse or the normalization.
- v71 (2026-10-22T02:27Z): referee consistency corrections to 4.39 to 4.43, the Summary and the Q1 bullet entered
  02:27 (P250 CONFIRMED 02:14 to 02:18); no change to the admissible class, the inverse or the normalization.
- v72 (2026-10-22T03:13Z): the numerics integration of shift 7 entered 03:12 (P256 02:42 to 03:03, v2 with the two spread bounds
  1.5e-7) and 4.44 entered 03:12 (P257 CONFIRMED 02:51, A153 VALID WITH FIXES adopted, P260 03:04 to 03:10); no change
  to the admissible class, the inverse or the normalization. Candidate 4.45 (tail restrictions for I_2: P258 (A1),
  (A2) and the lead's one-sided power bound z445, work/z445/NOTES.md) under audit.
- v73 (2026-10-22T03:51Z): 4.45 entered 03:51 (P258, P261, P263 CONFIRMED; A154 VALID WITH FIXES adopted; P265 03:36 to 03:49, v3
  with the range beta >= 2 stated in the opening); no change to the admissible class, the inverse or the normalization.
  Candidate 4.46 (the exponent of 4.45 is optimal for the axis relations: P264, A155, A156, and the lead's concave
  variant, work/z446/NOTES.md) under verification.
- v74 (2026-10-22T04:01Z): 4.46 entered 04:01 (P264, P268, P269 CONFIRMED; A155, A156 VALID; v2 text 31b48fbb); no
  change to the admissible class, the inverse or the normalization. Candidate 4.47 (log-enhanced critical tails, P266
  CONFIRMED; referee audit z447_log asked 03:54) next.
- v75 (2026-10-22T04:38Z): 4.47 entered 04:36 (P266, P270, P271 CONFIRMED; A157 VALID, A158 VALID WITH FIXES, A159 VALID;
  P274 CONFIRMED 04:29 to 04:31, v2 text 60e5178d, approved placeholders); no change to the admissible class, the inverse
  or the normalization. Candidate 4.48 (critical limits of the axis ratios; P272 CONFIRMED, A160 VALID WITH FIXES) next.
- v76 (2026-10-22T04:53Z): 4.48 entered 04:53 (P272, P275 CONFIRMED; A160 VALID WITH FIXES, A158 VALID WITH FIXES;
  P276 CONFIRMED 04:44 to 04:47 after the exact p_n notation correction, text v4 917f3056, approved placeholders); no
  change to the admissible class, the inverse or the normalization. Next: numerics integration num_s8 (48 angular modes on
  both paths, y* acceptance flags) under verification.
- v77 (2026-10-22T05:16Z): numerics integration num_s8 entered 05:15 (48 angular modes on both paths, diagnostics of the
  40-mode state at beta = 3.085, y* flags; P279 numerical values CONFIRMED 05:07 to 05:13, 307 of 309 controls, with the
  three exact wordings on the fit-growth multiplier 1e9 adopted; text v2, apply_v2); no change to the admissible class,
  the inverse or the normalization. Next: 4.49 (P273 + P278) and num_s9 (P277, P280).
- v78 (2026-10-22T05:38Z): 4.49 entered 05:37 (a bounded axis component is consistent with all axis equations; P273, P278
  CONFIRMED; A161 VALID WITH FIXES, A162 correct with fixes; P282 CONFIRMED 05:32 to 05:35, 223 controls, with its two
  exact wording corrections adopted; text v3, approved placeholders); no change to the admissible class, the inverse or
  the normalization. Next: num_s9 (P277, P280) under verification; candidate 4.50 (A162 D4: exact (T) on R^2 with all
  axis jets and a bounded J) after P283 and the referee audit z450_d4.
- v79 (2026-10-22T05:52Z): numerics integration num_s9 entered 05:51 (48-mode states of the second 48-mode run of the
  first path at beta = 3.076 and 3.062; P277, P280 CONFIRMED as finite diagnostics, both fields REFUTED as profiles;
  P284 CONFIRMED 05:44 to 05:45, 206 controls, text unchanged, approved placeholders); no change to the admissible class,
  the inverse or the normalization. Next: 4.50 (P283 CONFIRMED, A164 valid with clarifications) under verification.
- v80 (2026-10-22T06:22Z): 4.50 entered 06:21 (exact temperature transport is consistent with a bounded axis
  component, every beta >= 2; P283 CONFIRMED, A162, A164 valid with clarifications; P290 CONFIRMED 06:02 to 06:04, 165
  controls, text unchanged, approved placeholders); no change to the admissible class, the inverse or the normalization.
  Next: 4.51 (P286, A166; P292 under way with two scope repairs), 4.52 (P289, A165), num_s10 (P287, P291).
- v81 (2026-10-22T06:32Z): 4.51 and 4.52 entered 06:31 (finite-order ends of the axis component: D/T is asymptotic to
  -(3 d0/beta) p (p - 1) s^-2, s the distance to the end, and A I_2 tends to -infinity when A/T > 0; infinitely flat
  ends: the four axis relations force no sign of A I_2; P286, P289 CONFIRMED; A166 VALID with its precision adopted, A165 VALID; P292 CONFIRMED 06:20 to 06:27, 152
  controls, with its scope repairs and two clarifications adopted, text v3; P293 CONFIRMED 06:23 to 06:28, 158 controls,
  with its local scope correction adopted, text v3; approved placeholders); P295 confirmed the actual entry of 4.50. No
  change to the admissible class, the inverse or the normalization. Next: numerics integration num_s10 (P287, P291).
- v82 (2026-10-22T06:59Z): numerics integration num_s10 entered 06:59 (restarts of six stored stages with 48 Gauss
  points per radial quadrature cell and the runtime velocity norms at 12 and 48 points: finite diagnostics, all six
  fields refuted as profiles; P287, P291 CONFIRMED; P298 CONFIRMED 06:41 to 06:56, 468 controls, VER approved text
  9e583dec, word-identical to the approved preview). No change to the admissible class, the inverse or the
  normalization. Next: 4.53 (simple ends of the axis component; P296, external referee audit z453_simple VALID), P294 (tight
  secant roots) as num_s11.
- v83 (2026-10-22T07:27Z): 4.53 entered 07:27 (ends of the axis component at which the axis velocity has a simple zero: I_2 has an
  extended real limit; if b''(y_*) != 0, A I_2 -> -sgn(y_* b''(y_*)) infinity; local solutions of the four axis
  relations attain every finite limit and both infinite limits, at beta = 2 with the signs and integrality of 4.13;
  P296, P299, P303 CONFIRMED; A167 VALID, A169 VALID with scope corrections; P304 CONFIRMED 07:11 to 07:21, 167
  controls, with its seven wording corrections adopted; seven lead precision edits checked 07:24 to 07:26 (P304); approved
  placeholders). No change to the admissible class, the inverse or the normalization. Next: the adoption of the
  whole-report review A168 (ref19) and numerics integration num_s11 (P294).
- v84 (2026-10-22T07:33Z): adoption of the fourteenth whole-report review (A168) entered 07:33: R1 to R4 (the word "earlier" in the
  entry on the 48-mode states of the second path, the finite ends of J in the Q1 bullet, the Scope of 4.50, the split
  of the Summary bullet on temperature and the axis) and the section 7 entry R5 with the wall-clock cap reading of the
  run instructions; P307 CONFIRMED 07:22 to 07:30, 81 controls, one duration correction. End of the run: the run
  instructions cap the wall-clock run at 48 h from T0 = 2026-10-20T12:44:11Z; the report is completed shortly before
  2026-10-22T12:44:11Z and records the elapsed time, the gaps between sessions and the active time separately. No
  change to the admissible class, the inverse or the normalization. Next: numerics integration num_s11 (P294, P305).
- v85 (2026-10-22T07:50Z): numerics integration num_s11 entered 07:50 (6.1 paragraph, Summary bullet, Tables 6.1c, 6.1e with the
  rows root12K32_beta3.062 and root48K32_beta3.062, 97 states, Table 8.2 row, section 7 entry): two redeterminations
  of lambda for the 32-mode stage of the first path at beta = 3.062 with 12 and 48 quadrature points, 1.76e-8 apart,
  without establishing exact discrete roots or a difference between them; both fields REFUTED as profiles (P294);
  P305 CONFIRMED 07:26 to 07:38, 342 controls, six wording corrections. No change to the admissible class, the
  inverse or the normalization. Next: 4.54 (the next vorticity relation at a simple end, P306 and the lead extension).
- v86 (2026-10-22T08:20Z): 4.54 entered 08:19 (the next vorticity relation (V_1) at a simple end of the axis component,
  beta = 2: (a) in the family of 4.53 (e) a smooth gamma exists if and only if H = -k^7/231, which forces A k < 0; (b)
  local analytic solutions of the five relations with both infinite limits of A I_2; (c) the polynomials and analytic
  solutions of 4.53 (d) satisfy (V_1)), with the Summary and Q1 bullets, the Scope of 4.53, the notation paragraph,
  the proof notes, the Table 8.1 row and the section 7 entry; P306 and P311 CONFIRMED, P312 CONFIRMED 08:08 to 08:16,
  242 controls, three wording corrections (proof (4) right side D + 2 eta eta', the open question on additional
  restrictions of the limit, the scalar residue reading of the further relations); A170 VALID with three corrections.
  No change to the admissible class, the inverse or the normalization. Next: 4.55 (the relations (T_3) and (V_2) in
  the family of 4.54 (a), P308, A171).
- v87 (2026-10-22T08:51Z): 4.55 entered 08:50 (two further axis relations in the family of 4.54 (a), beta = 2: (T_3) and (V_2)
  have smooth solutions near y_* for exactly one choice of the two free constants of D and gamma; residue matrix
  entries 12 C k/25, 0, -9 k^8/1925, -9 C k/20, determinant -27 C^2 k^2/125), with the Q1 bullet, the Scope of 4.54,
  the notation paragraph, the proof notes, the Table 8.1 row and the section 7 entry; P308 CONFIRMED (256 exact and
  23 symbolic controls), P320 (adjudication of A171, 34 controls), P319 CONFIRMED 08:42 to 08:49 (complete entry, 129
  controls, five wording corrections); A171 VALID. No change to the admissible class, the inverse or the
  normalization. Next: 4.56 candidate (P321: the axis relations of every order in the same family, as formal series
  in x with analytic coefficients; audit z456_p321 running, lead check work/z456/check_allorder.py n = 2 to 8 PASS).
- v88 (2026-10-22T09:26Z): 4.56 entered 09:26 (the axis relations of every order in the family of 4.54 (a), beta = 2: (T_n),
  (V_n) and the curl relation of 4.49 (2) of every order have solutions, real analytic on the one interval
  |y - y_*| < R_*, R_* = min(1, 1/(4|k|), (65/|Ck|)^{1/12}), for exactly one choice of the two free constants at each
  order; determinant -54 C^2 k^2/(25 n (2 n + 1)); formal in x, no convergence, no profile), with the Summary and Q1
  bullets, the Scopes of 4.55 and 4.54, the last sentence of the statement of 4.54, the notation paragraph, the proof
  notes, the Table 8.1 row and the section 7 entry; P321 CONFIRMED (192 controls), P326 CONFIRMED (common interval,
  88 controls), P325 CONFIRMED 09:13 to 09:22 (complete entry, 611 controls, two wording corrections: "all further
  conditions beyond H = -k^7/231" in the statement of 4.54, the value of D fixed in 4.55 in the letters of 4.56);
  A173 VALID, A174 VALID. No change to the admissible class, the inverse or the normalization. Next: 4.57 candidate
  (P328: the part of total degree 11 of Theta in (x^2, y_* - y) is (C/2) x^2 (u - k x^2/11)^10; audit z457_p328
  running, lead check work/z457/check_p328.py).
- v89 (2026-10-22T09:57Z): 4.57 entered 09:57 (the leading part of the temperature series at the end in the family of
  4.54 (a), beta = 2: Theta in (x^2, u = y_* - y) has no term of total degree below 11, its part of degree 11 is
  (C/2) x^2 (u - k x^2/11)^10; formal; uses (T_1) to (T_11) only). P328 CONFIRMED (156 controls), P332 CONFIRMED 09:35
  to 09:49 (complete entry, 1983 controls, one Scope correction: the whole series vanishes on x = 0, so the leading
  part gives no zero curve and no sign); A175 VALID for the proof. No change to the admissible class, the inverse or
  the normalization. Next: 4.58 (P331: Theta = (C/2) x^2 Z^10 in the formal ring, Z = (u - h(x^2)) times a unit,
  odd formal first integral I = x Z^5; A176 VALID; complete-entry check P336).
- v90 (2026-10-22T10:17Z): 4.58 entered 10:16 (a factorization of the temperature series at the end in the family of
  4.54 (a): in the formal ring, Theta = (C/2) x^2 Z^10 with Z = (u - h(x^2)) times a formal unit, h_1 = k/11, and
  Theta = (C/2) I^2 for the odd formal first integral I = x Z^5; formal, no convergence, no off-axis zero curve, no
  sign). P331 CONFIRMED (184 controls); P336 CONFIRMED 10:02 to 10:15 (complete entry, 1107 controls, four wording
  repairs W1 to W4); A176 VALID. No change to the admissible class, the inverse or the normalization. Next: 4.59
  (P337 and P338: actual smooth factorization at a simple end of J for every beta > 0, Theta = (C_u/2) x^2 Z^n,
  Z = (u - H(x)) L, L > 0; A177 VALID with two fixes, adopted).
- v91 (2026-10-22T10:34Z): 4.59 entered 10:33 (the temperature near a simple end of the axis component, necessary conditions,
  every beta > 0: near (0, y_*), Theta = (C_u/2) x^2 Z^n with Z = (u - H(x)) L, L > 0 smooth, u = H(x) the smooth
  unstable curve of W, H = k x^2/(4 beta + 3 kappa) + O(x^4); zero set the axis and this curve; the sign of C off them
  for even n, a sign change across the curve off the axis for odd n). P334 CONFIRMED (53), P337 CONFIRMED (74), P338
  CONFIRMED 10:14 to 10:33 (complete entry, 271 controls, repairs W1 Scope dependencies and W2 timeline off-axis);
  A177 VALID with two fixes, adopted. No change to the admissible class, the inverse or the normalization. Next: 4.60
  (P339: Omega = E_u x Z^m Y at the same end, beta >= 2, m = 1 + (2 beta + 1)/kappa, x Omega Theta > 0 off the two
  curves; A178 VALID; A179 text audit running; complete-entry check P342).
- v92 (2026-10-22T10:43Z): 4.60 entered 10:43 (the vorticity near a simple end of the axis component, necessary conditions,
  beta >= 2: near (0, y_*), Omega = E_u x Z^m Y with Y > 0 smooth, Z and u = H(x) as in 4.59, m = 1 + (2 beta + 1)/kappa,
  E the incoming coefficient of eta, E/C > 0; zero set the axis and the same curve as Theta, order m off the axis;
  x Omega Theta > 0 off the two curves, using the parity of n - m in 4.13 (ii)). P339 CONFIRMED (183), P342 CONFIRMED
  10:27 to 10:42 (complete entry, 533 controls, one clarification W1: E/C is preserved by the reflection of 4.8); A178 and
  A179 VALID, no corrections (plus-sign transcription errata recorded in their directories). No change to the admissible
  class, the inverse or the normalization. No further entries are planned before finalization.
- v93 (2026-10-22T11:00Z): Summary (bullet "Axis ratios") and section 5 (bullet "Restricted temperature representations")
  sentences on 4.57 to 4.60 entered 10:59, with a section 7 entry: the formal factorization of the temperature series at
  beta = 2 (4.57, 4.58) and, for a profile near a simple end of J, Theta = c_1 x^2 phi^n, Omega = c_2 x phi^m Y with c_1, c_2
  of the same sign, n - m even, zero sets the axis and the local unstable manifold, x Omega Theta > 0 off them (4.59, 4.60).
  A180 VALID (no corrections; its optional notation note adopted); P345 CONFIRMED 10:55 to 10:57 (246 controls, two
  wording clarifications). Restatements only; no change to the admissible class, the inverse or the normalization.
- v94 (2026-10-22T11:43Z): (A5) wording and citation clarification adopted verbatim from VER P351 (94 controls;
  research/351_spec_absolute_and_signed_drift/verification/approved_A5_replacement.md): "NEVER happens" now means
  absolute convergence (4.11); the positive-part bound concerns the absolute component integral, not the signed
  truncation; signed truncations follow Theorem D (4.12), v0(R) = B R^(1-1/beta) + o(R^(1-1/beta)), undecided when
  B = 0, B > 0 if a0 > 0 and Omega >= 0 on x > 0. No change to the admissible class, the inverse, the normalization
  or the report.
