# CONVENTIONS.md: conventions for the S2 (case 1, x^2 y-leading, X3 branch) theory run

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

Version 1, 2026-10-28T00:34Z (theory author). Every item is DERIVED by the theory author and must be checked independently by the
verifier; item numbers (S0.1, S3.2, ...) are the references for VERIFICATION_RECORD.md. Later versions append or mark
corrections; item numbers are never reused.

Research copies: the theory work used full copies of the case 1 data (72 MB, no symbolic links, checked identical
with the originals at 00:21Z) and of the earlier analysis; the originals were never written.

## S0. Background state

S0.1 Accepted numerical state: the published candidate X3 of case 1, `IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz`,
md5 15f8095f7e79dbfa0c50d75e5fe8997a (checked). The follow-up of case 1 (report section 6) produced no newer accepted
state: its collocation solves (`IPM_Setting_I.followup.artifacts/numerics/data/dn*.npz`) stagnated at 2-norm residual
about 2e-4 and are diagnostics, not candidates. X3 is a P_2 state: its centre factor a = rho/(x^2 y) is continuous with
a(0) = 1 but not smooth (it carries the saddle mode |x|^{p_3} y^3, p_3 = 6 + 2/A; case 1 report 6.3).
Held constants (exact): k = 1615536043799051/2^53 = 0.17936053129375418..., c_l = 1/k = 5.575362610641546...,
A = 2 c_l - 1 = 10.150725221283093..., D = 4 c_l - 1 = 2A + 1 = 21.301450442566185..., length scale
L = 7.651424601381517 (exact dyadic, stored).

S0.2 X3 is not exactly normalized: with c = psi[X3]_xy(0), 3/k - 1 - c lies in [1.03009e-8, 1.03014e-8] (Analysis I,
certified there; to be recomputed by our verifier before we use it). Consequence (S4.4): with the normalized exponent
c_l[rho] = (1 + c[rho])/3 built into F, F(X3) contains (c_l[X3] - 1/k) X.grad X3, which grows like r^k at infinity.

S0.3 Rigorous background. Every rigorous statement must name its background rho_bar and must use one with
3 c_l_bar - c[rho_bar] = 1 EXACTLY (c_l_bar := (1 + c[rho_bar])/3). Admissible choices: (i) the exactly joined and
exactly normalized modal trial rho~ of Analysis I (`numerics/data/trial_v2_h0.008.npz`, exact export
`verification/data_exact/modal_v2.json.xz`, SHA-256 of the json 57f67a53...a6), for which c_l = 1/k and the far
residual is eps~ = r^{2k-1} Eps(theta) + o(r^{2k-1}) (decaying, in L^2(<r>^{-2 beta}) iff beta > 2k, not in L^2);
(ii) a background built by the numerics team with an exact normalization (state how). X3 is the numerical reference.
Every certified number must state which background it refers to.

Notation: r = |X|, theta polar angle, t = log r, <r> = (1 + r^2)^{1/2}, k = 1/c_l, A = 2c_l - 1, D = 4c_l - 1.

## S1. Equation and symmetry class

S1.1 F(rho) := (c_l X + U[rho]).grad rho - rho, U = (-psi_y, psi_x), -Lap psi = d_x rho on R^2.
S1.2 Parity class P: rho even in x, odd in y. Then d_x rho is odd-odd, psi odd-odd, U_1 = -psi_y is odd in x and even
in y, U_2 = psi_x is even in x and odd in y. U = 0 on the origin; U_1 = 0 on {x = 0}; U_2 = 0 on {y = 0}; both axes
are invariant for every field c X + U.
S1.3 S2 branch: rho = x^2 y a(X) near 0 with a continuous, a(0) = 1.
S1.4 y-axis vanishing (lemma, to verify): if rho in P solves F(rho) = 0, is C^1 near the y-axis, rho = O(r^3) at 0 and
V_2(0, y) = D y + O(y^3) with V_2(0, y) != 0 for y != 0, then rho(0, y) = 0 for all y. Proof: G(y) = rho(0, y)
satisfies V_2(0,y) G' = G (the coupling vanishes since U_1(0, y) = 0 and d_x rho(0, y) = 0 by evenness), so
G = C exp(int dy/V_2) ~ C |y|^{1/D} at 0; O(r^3) forces C = 0. Hence rho = x^2 G_2(y) + O(x^4) near the y-axis, and the
same holds for every correction h = rho - rho_bar when rho_bar has this property.

## S2. Canonical inverse and Riesz conventions

S2.1 Fourier: f^(xi) = int f e^{-i xi.X} dX; R_j = d_j (-Lap)^{-1/2}, symbol i xi_j/|xi| (same convention as the
Hoelder team). R_1^2 = d_xx (-Lap)^{-1}, symbol -xi_1^2/|xi|^2; R_1 R_2 = d_xy (-Lap)^{-1}, symbol -xi_1 xi_2/|xi|^2.
U[h] = (-R_1 R_2 h, R_1^2 h), symbols (xi_1 xi_2/|xi|^2, -xi_1^2/|xi|^2).
S2.2 Kernels. G = -(1/2 pi) log r is the fundamental solution of -Lap, (-Lap)^{-1} f = G * f. As distributions
d_xx G = PV cos(2 theta)/(2 pi r^2) - (1/2) delta and d_xy G = PV sin(2 theta)/(2 pi r^2) (no local term). Hence
R_1^2 h = T_xx h - h/2 and R_1 R_2 h = T_xy h with T_xx, T_xy the PV convolutions with cos(2theta)/(2 pi r^2),
sin(2theta)/(2 pi r^2) (prompt 4.1). Symbol check: -xi_1^2/|xi|^2 has angular mean -1/2.
S2.3 Growth class and canonical velocity: for h in P with |h| <= C <r>^beta, beta < 1, U[h] is defined by the kernels
with the standard subtraction K(X - Y) - K(-Y) for |Y| > 1; the canonical psi is the unique odd-odd solution with
psi = o(r^2) (no harmonic lambda x y term; a difference is an odd-odd harmonic polynomial of degree <= 1, hence 0).
"No additional harmonic velocity" means exactly this.

## S3. Strain functional and normalization identity

S3.1 c[h] := psi[h]_xy(0) = d_y U_2[h](0) = -d_x U_1[h](0); DU[h](0) = diag(-c[h], c[h]) for h in P (U_1 odd in x,
even in y; U_2 even in x, odd in y). NOT divided by 3 (Analysis I convention; the prompt also uses c = psi_xy(0)).
S3.2 Kernel formula: for h in P with |h(X)| <= C r^{1+eps} near 0 (some eps > 0), |h| <= C <r>^beta at infinity
(beta < 1) and h locally Hoelder,
   c[h] = (1/pi) int_{R^2} sin(3 theta) r^{-3} h(X) dX   (absolutely convergent).
Derivation: psi = (d_x G) * h, so psi_xy(0) = int (d_x^2 d_y G)(-Y) h(Y) dY and d_x^2 d_y G = -(1/pi) sin(3 theta)/r^3
(from d_xx G = cos(2theta)/(2 pi r^2) = Re z^{-2}/(2 pi) and d_y z^{-2} = -2 i z^{-3}); at -Y the sign flips.
Check: c[x^2 y chi(r)] = (1/pi) int cos^2 sin sin3 dtheta int chi r^{...} > 0 since int_0^{2pi} cos^2(t) sin(t) sin(3t) dt = pi/4.
WARNING (from the S1 team, item S3.1 of their CONVENTIONS, re-derived here): for h with a nonzero y-jet the canonical
functional has an extra local term, c[h] = (1/pi) PV int sin3theta r^{-3} h - (1/4) d_y h(0) (e.g. c[y e^{-r^2}] = -1/4
while the PV integral is 0). In the S2 class every correction is O(r^{1+eps}) at 0, so the formula S3.2 holds without
the local term; any space containing functions with d_y h(0) != 0 must use the full formula.
S3.3 Normalization identity: if rho = x^2 y a with a in C^0, a(0) = 1, U[rho] in C^{1,alpha} near 0 and F(rho) = 0
(or F(rho) = o(r^3) in a sense that allows division by x^2 y at 0), then 3 c_l - c[rho] = 1. Proof: with
V = c_l X + U[rho] = (c_l - c) x e_1 + (c_l + c) y e_2 + O(r^{1+alpha}), the x^2 y coefficient of F is
2(c_l - c) + (c_l + c) - 1 = 3c_l - c - 1 (for a merely continuous, use the rescaled distributional limit of
Analysis I section 2). Hence c_l = (1 + c[rho])/3 and DV(0) = diag(c_l - c, c_l + c) = diag(-A, D),
A = 2c_l - 1, D = 4c_l - 1 (prompt 3.1 confirmed).

## S4. Formulations, full linearization, nonlinear remainder

S4.1 Formulation N (primary): unknown rho only, c_l[rho] := (1 + c[rho])/3, F_N(rho) := (c_l[rho] X + U[rho]).grad rho
- rho. Formulation P (parametric): unknowns (rho, c_l), F(rho; c_l) = 0 and 3 c_l - c[rho] = 1. Same solutions in the
S2 class.
S4.2 Full linearization at any background with 3 c_l_bar - c[rho_bar] = 1 (no stationarity used):
   L h = V.grad h - h + W[h].grad rho_bar,   V = c_l_bar X + U[rho_bar],   W[h] = U[h] + (c[h]/3) X.
Fixed-c_l linearization L_fix h = V.grad h - h + U[h].grad rho_bar, so L = L_fix + (c[h]/3) G_bar with
G_bar = X.grad rho_bar (rank one; G_bar ~ k r^k Theta_0 at infinity, not decaying). Any use of L_fix must say so.
S4.3 Exact expansion: F_N(rho_bar + h) = F_N(rho_bar) + L h + N(h), N(h) = W[h].grad h EXACTLY (no cubic terms,
because c_l[.] is affine and U is linear).
S4.4 With a background whose held exponent differs from c_l[rho_bar] (X3), F_N(rho_bar) = F_held(rho_bar) +
(c_l[rho_bar] - c_l^held) G_bar; the second term grows like r^k.
S4.5 Leading cancellation (prompt 5.3): write U[h] = DU[h](0) X + U^(2)[h] with DU[h](0) X = c[h](-x, y). Then
   W[h] = c[h](-2x/3, 4y/3) + U^(2)[h],   (c[h](-2x/3, 4y/3)).grad(x^2 y) = 0  exactly.
Hence, for rho_bar = x^2 y a_bar: W[h].grad rho_bar = U^(2)[h].grad rho_bar + c[h] x^2 y (-(2/3) x d_x + (4/3) y d_y) a_bar.
By parity U^(2)[h] has no Taylor term of degree 0 or 2 at 0 (U_1 odd-even, U_2 even-odd); if U[h] is C^3 near 0 then
U^(2)[h] = O(r^3). In the factor variable, the c[h] term is c[h] x^2 y (-(2/3) x a_x + (4/3) y a_y) = o(x^2 y).
S4.6 x^2 y coefficient of the range: for h = J x^2 y + o(r^3) with U[h] in C^{1,alpha} near 0, the x^2 y coefficient of
L h is J(3c_l_bar - c[rho_bar] - 1) + 0 = 0. So L maps the S2 class into forcings with vanishing x^2 y coefficient,
and J(h) is NOT determined by the x^2 y coefficient of L h (it is the scaling freedom, S5).

## S5. Scaling direction and the normalization J

S5.1 rho_lambda(X) = lambda rho(X/lambda): U[rho_lambda](X) = lambda U[rho](X/lambda), c[rho_lambda] = c[rho],
F_N(rho_lambda)(X) = lambda F_N(rho)(X/lambda). For rho = x^2 y a: rho_lambda = lambda^{-2} x^2 y a(X/lambda).
S5.2 K := d/dlambda rho_lambda at lambda = 1 = rho - X.grad rho. J(K) = 1 - 3 = -2 when X.grad a -> 0 at 0
(J(h) := lim_{X->0} h/(x^2 y)). Residual identity (exact, any background): L K_bar = F_N(rho_bar) - X.grad F_N(rho_bar).
So L K_bar = 0 only at an exact profile. At infinity K_bar ~ (1 - k) r^k Theta_0.
S5.3 Closedness of J = 0 (prompt 1). J must be a continuous functional on the correction space, otherwise {J = 0} is
dense and removes nothing. Examples: (a) in the diagnostic norm X of Analysis I (weight r^{-6} on f^2 + r^2|grad f|^2)
h_eps = x^2 y chi(r/eps) has ||h_eps||_X = O(eps) and J = 1: J is unbounded, {J = 0} is dense (not closed);
(b) on factor spaces with a continuous at 0 (sup norm of a, or H^s of a with s > 1 locally) J = a(0) is continuous;
(c) jet-plus-remainder: h = J x^2 y chi_0(r) + h_rem with h_rem in a space whose elements are o(r^3) in a norm sense
(for example sup r^{-3-eps}|h_rem| near 0, or L^2(r^{-2 beta}) with beta > 4 near 0 together with enough derivatives
to embed into o(r^3)); then J is a coordinate and is continuous. Required: every proposed space states which of these
holds.

## S6. Frozen operators

S6.1 Origin: V = A_c X + V^(3), A_c = diag(-A, D), where by parity V^(3) has no Taylor terms of degree 0 or 2
(V_1 odd-even, V_2 even-odd), so V^(3) = O(r^3) if U[rho_bar] is C^3 and O(r^{2+alpha}) if it is C^{2,alpha}
(X3 is not smooth at 0, S0.1). Frozen transport T_0 = -A x d_x + D y d_y - 1. Coupling: by S4.5 and
grad rho_bar = (2xy, x^2) + o(r^2), the coupling is U^(2)[h].grad rho_bar + o(|c[h]| r^3): it carries no O(r)
factor of h; in a weighted space at degree d it is formally smaller by r^2 than h. Factor form:
T_0(x^2 y B) = x^2 y (-A x B_x + D y B_y): pure transport, no damping, for the factor.
S6.2 Homogeneous solutions of T_0: |x|^p sgn(y)|y|^q with -A p + D q = 1; at degree d = p + q:
p(d) = (D d - 1)/(A + D), q(d) = (A d + 1)/(A + D). d = 3 gives (p, q) = (2, 1) (x^2 y); d = 2 gives
p = 1.3227352, q = 0.6772648 (the Analysis I quasimode). Integer resonances x^i y^j (i even, j odd): -A i + D j = 1
with D = 2A + 1 is A(2j - i) = 1 - j, i.e. i = 2j + (j - 1)/A. With c_l = 1/k exactly, A = M/n,
n = 1615536043799051, M = 2^54 - n = 16398862465682933, gcd(M, n) = 1, so (j - 1)/A is an integer only if
M | (j - 1): the only resonance with j < 1 + M is (2, 1). The first non-smooth saddle mode in the x^2 y class
beyond x^2 y is |x|^{p_3} y^3, p_3 = (3D - 1)/A = 6 + 2/A = 6.1970303.
S6.3 Source P = (x_P, 0) (X3: x_P ~ 8.600064): V(P) = 0, DV(P) = diag(A_P, mu_P) by parity, A_P + mu_P = div V = 2 c_l.
At an exact solution with g = rho_y(P) != 0: mu_P = 1 (grad rho(P) is a left eigenvector of DV(P) with eigenvalue 1),
hence A_P = 2c_l - 1 = A. Frozen coupled operator (s = x - x_P):
   L_P h = A s h_s + mu y h_y - h - g M h + (c[h]/3) G_bar,   M = -R_1^2 (symbol xi_1^2/|xi|^2),
G_bar = X.grad rho_bar = (g + x_P rho_bar_xy(P)) y + O(|s y| + |y|^3) near P; the last term is the rank-one strain
term (nonlocal through c[h]; absent in the frozen model of Analysis I). The term U_1[h] rho_bar_x vanishes at P. X3/trial: A ~ 10.15,
mu ~ 1 (trial: |mu - 1| ~ 2.3e-8), g ~ 29.75.
S6.4 Infinity: V = c_l X + O(r^k); homogeneous far solutions r^k Theta(theta) for every Theta (infinite-dimensional
outflow data); (c_l r d_r - 1)(r^k log r) = c_l r^k, so the c_l variation produces r^k log r terms.

## S7. Energy identity at the origin (prompt 3.1)

S7.1 For h = -Lap Phi with Phi in P, grad Phi in L^2 and enough decay:
   -<L_fix h, Phi> = int grad Phi^T M_Phi grad Phi dX,  M_Phi = (1 + 2c_l) I + S(U_bar) + [[rho_y, -rho_x/2], [-rho_x/2, 0]],
S(U) the symmetric part of DU. (Re-derived by the theory author: -int (V.grad h) Phi = 2c_l ||grad Phi||^2 + int grad Phi^T S(V)
grad Phi - c_l ||grad Phi||^2 and -int (U[h].grad rho) Phi = int (rho_y Phi_x^2 - rho_x Phi_x Phi_y).)
S7.2 M_Phi(0) = diag(2 - c_l, 5 c_l) (S(U_bar)(0) = diag(-c, c), c = 3c_l - 1, grad rho(0) = 0). For X3 about
diag(-3.5754, 27.877). With the strain term, -<L h, Phi> = int grad Phi^T M_Phi grad Phi - (c[h]/3)<G_bar, Phi>.
What it rules out: the pointwise positivity inf lambda_min(M_Phi) > 0, and every estimate
delta ||grad Phi||^2 <= -<L h, Phi> (delta > 0) on any class containing x-oscillatory potentials localized near a
point off the axes close to 0 (with c[h] = 0 arranged by a remote bump); it does not rule out invertibility of L.
S7.3 Weighted local L^p energies (theory author, Avenue III; derivation in S2_C_FUNCTIONAL.md): for the frozen saddle and the
weight w = |x|^{-a p}|y|^{-b p}, int (T_0 h)|h|^{p-2} h w = -kappa_0 int |h|^p w + (1/p) boundary flux, with
kappa_0 = (D - A)/p + 1 + A a - D b. For p = 2 this is -delta of Analysis I 5(e) (b_0 = (A + 3)/2 = c_l + 1).
For radial weights r^{-beta p} the multiplier is (D - A)/p + 1 - beta(-A cos^2 theta + D sin^2 theta); it is
negative on the y-axis iff beta > (D - A + p)/(p D) (about 0.31 for p = 2). Every isotropic weight that can see the
x^2 y jet (r^3 critical or subcritical: beta near 3 + 2/p) therefore gives an indefinite multiplier: isotropic
weights of the relevant strength cannot be coercive at the saddle.

## S8. Conventions for reports

Certified number: exact quantity, background (S0.3), input file and hash, method, precision, truncation and
rounding errors, final outward enclosure, independent check. Theorem: exact spaces, constants, hypotheses.
Label every item DERIVED / CONFIRMED (verifier) / REFUTED / OPEN / NUMERICAL (not a bound).

## Version 1.1, 2026-10-28T01:15Z (theory author): corrections after V007 to V009

C1 (S1.4, V008). The axis ODE conclusion rho(0, y) = 0 is CONFIRMED under D > 1/3 and V_2(0, y) != 0 for y != 0. The
subsequent statement rho = x^2 G_2(y) + O(x^4) is OPEN under C^1 alone; it holds if rho is C^4 near the y-axis (Taylor
in x with evenness). Every later use of the x^2-jet structure must assume C^4 near the axis, or carry the jet as an
explicit coordinate in the space (the route of S9 below).
C2 (S4.5 and S4.6, V007). The pointwise statements are REFUTED in the broad class "continuous factor, J = 0, h = o(r^3),
U[h] in C^{1,alpha}": the counterexample h = chi(r) x^2 y r^{1/10} sin(r^{-2/5}) has L h / r^3 unbounded on a ray.
Corrected statements: (i) the last sentence of S4.5 holds when the background factor satisfies
|x a_x| + |y a_y| = o(1) at 0 (true for the exact modal trial); (ii) S4.6 holds when, in addition, the correction
factor B = h/(x^2 y) satisfies x B_x, y B_y -> 0 at 0 (conormal derivative control); then the x^2 y coefficient of
L h is J (3 c_l_bar - c[rho_bar] - 1) = 0. Without such control only the distributional (rescaled-limit) version holds.
C3 (S6.2, V009). "First non-smooth saddle mode" holds only within the odd-integer-y ansatz. In the full continuous-factor
C^{2,alpha} class, |x|^{5 + 3/(2A)} sgn(y) |y|^{5/2} solves T_0 H = 0 with lower degree. By parity the next possible
integer resonance has j = 1 + 2M (V009); the arithmetic j < 1 + M of S6.2 is correct but not sharp.

## S9. Jet-plus-remainder domain at the origin (theory author, DERIVED; definitions for S2_L2_THEORY.md Theorem O)

S9.1 Variables: t = log r; near 0 write h = x^2 y B, B = beta(t) + B_R(t, theta) with beta(t) := B(r, pi/2) (the factor on
the y-axis) and B_R(t, pi/2) = 0. J(h) := lim_{t -> -infinity} beta(t).
S9.2 Frozen identities (exact, D = 2A + 1): T_0(x^2 y beta(log r)) = x^2 y beta'(t)(D sin^2 theta - A cos^2 theta)
= x^2 y (D beta'(t) - (A + D) cos^2 theta beta'(t)); T_0(x^2 y B_R) = x^2 y (-A x d_x + D y d_y) B_R, which again
vanishes on the y-axis. So T_0 is block triangular: jet row D beta', remainder row T_0 on B_R plus the off-diagonal
term -(A + D) x^2 y cos^2(theta) beta'(t).
S9.3 Weights: remainder L^2(w), w = |x|^{-2a} |y|^{-2b}, 5/2 < a < 9/2, 0 <= b < 3/2; kappa_0 = (A + 3)/2 + A a - D b
(S7.3 with p = 2). Jet: int |beta - J|^2 e^{(3 - 2 b2) t} dt with 3/2 < b2 < 7/2 and b2 >= a + b - 5/2 (so that the
off-diagonal term is bounded).
