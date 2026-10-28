Lemma H2-ord (existence of the order function; DERIVED, submitted for checking). There is a real function s on the
cylinder C = R_t x S^1 with every derivative bounded, invariant under both coordinate reflections, with
41/20 = s_0 <= s <= sigma = 25/4, such that
  (a) s = sigma on {|cos theta| < eps_2} for some eps_2 > 0, and on {t >= T_inf} for some finite T_inf;
  (b) s = s_0 on a set N_0 that contains a uniform neighbourhood of the closed x-axis segments and of the sources:
      N_0 contains {|sin theta| <= beta_0, t <= t_c} and the discs {|X -+ P| <= rho_1/2}, where t_c < log x_P and
      e^(t_c) > x_P - rho_1, for some beta_0 > 0, rho_1 = 1/4;
  (c) W.grad s >= 0 everywhere, W = (q, vartheta) the cylindrical transport field.
So the order hypothesis of V126 and V129 holds, and s is at most 41/20 at S_x, along the x-axis segment and at +-P, as
the frozen thresholds of 6.5 require (2.0809 at S_x in the cylinder norm, 2.334 along the segment, 3.5785 at P).
Inputs (all verified for the actual field). (I1) W is in W^(2,infinity) and C^1 on C, tangent to the axes and
compatible with the reflections (V129, hypothesis 1). (I2) Origin end: q -> q_0 = -A cos^2 theta + D sin^2 theta, vartheta -> vartheta_0 = Sigma sin theta cos theta and
d_theta vartheta -> Sigma cos 2theta uniformly in theta as t -> -infinity. (d_theta vartheta = e_theta.DV e_theta - V.e_r/r, so
this follows from V = diag(-A, D) X + O(r^3) and DV = diag(-A, D) + O(r^2), V055.) (I3) V_1(x, 0) < 0 for
0 < x < x_P (Lemma H1 (ii) and (Z), V063, V080: no zero on the open segment, and V_1 ~ -A x near 0). (I4) On the
rectangle Q of V070 the symmetric part of DV exceeds 0.1801 I, so V.(X - P) >= 0.1801 |X - P|^2 there (V070).
No global property of the flow beyond (I3) is used.
Proof. All distances, normals and derivatives are taken in the coordinates (t, theta). Work in the first quadrant
near theta = 0 and extend everything by the two reflections.
Step 1 (a repeller block B). Since vartheta is odd in theta, vartheta(t, theta) = theta int_0^1 d_theta vartheta(t, u theta) du.
By (I2) choose t_1 with |d_theta vartheta - Sigma cos 2theta| <= Sigma/4 and q(t, theta) < 0 for t <= t_1, |theta| <= pi/8
(q_0 < 0 for tan^2 theta < A/D). Then vartheta(t, theta) >= 0.4 Sigma theta there. On [t_1, t_c], with
x_c := e^(t_c) = x_P - rho_1/2, (I3) and compactness give q(t, 0) <= -2 q_m < 0, and W in C^1 gives
|vartheta(t, theta) - theta a(t)| <= C_2 theta^2 and |q(t, theta) - q(t, 0)| <= C_1 theta, a(t) := d_theta vartheta(t, 0). Put
M := 2(||a||_inf + 1)/q_m, take psi smooth, nondecreasing, psi = 0 on (-infinity, t_1 - 1], psi' = 1 on [t_1, infinity),
0 <= psi' <= 1, and beta(t) := beta_* exp(M psi(t)), where beta_* > 0 is so small that beta <= min(pi/8, q_m/C_1, 1/(2 C_2))
on (-infinity, t_c], x_c beta(t_c) <= rho_1/4 and x_P (1 + 2M) beta(t_c)^2 < rho_1. Here C_1 = ||d_theta q||_inf and
C_2 = ||d_theta^2 vartheta||_inf/2. Let B_T := {t <= t_c, |theta| <= beta(t)} and B_P := {|X - P| <= rho_1}
(B_P lies in Q since x_P lies in the V017 bracket [p_-, p_+]). The outward normal of B_T on theta = beta(t)
is proportional to (-beta', 1), and W.(-beta', 1) = vartheta - beta' q.
- For t <= t_1: q < 0 and beta' >= 0, so W.(-beta', 1) >= vartheta(t, beta) >= 0.4 Sigma beta_*.
- For t_1 <= t <= t_c: beta' = M beta and q(t, beta) <= -q_m, so
  W.(-beta', 1) >= beta (a(t) - C_2 beta + M q_m) >= beta (a(t) + 2||a||_inf + 3/2) >= beta_*.
On the circle |X - P| = rho_1, W.(X - P)/rho_1 >= 0.1801 rho_1 by (I4) (in the plane; the cylinder normal has the same
sign). The end cap {t = t_c, |theta| <= beta(t_c)} lies in the interior of B_P (|X - P|^2 <= (rho_1/2)^2 + x_c x_P beta^2 <
rho_1^2), and along the lateral boundary |X - P|^2 is strictly decreasing in x on [x_P - rho_1, x_c] (its x-derivative
is at most -rho_1 + x_P (1 + 2M) beta^2 < 0), so each lateral boundary curve crosses the circle exactly once, near its
leftmost point, where the circle is nearly vertical and the curve nearly horizontal: the crossing is transversal. Round the two reentrant corners of B_T union B_P by fillets whose normals are
convex combinations of the two adjacent normals; W.n > 0 is convex in n, so it persists. Reflect. The result B is a
closed reflection-invariant set with C^2 boundary, n.W >= kappa_B > 0 on its boundary (uniformly, the t -> -infinity
part included), contained in {|theta| <= pi/8 or |theta - pi| <= pi/8} intersected with {t <= log(x_P + rho_1)}.
Step 2 (B is backward invariant; the exit time). Because W points strictly outward on the C^1 boundary, no backward
orbit leaves B, and a forward orbit starting outside B never enters B. For X not in B let
tau_B(X) := inf{tau >= 0 : Phi_(-tau)(X) in B} in [0, infinity]. Then tau_B(Phi_u X) = tau_B(X) + u for u >= 0, so
W.grad tau_B = 1 where tau_B is finite; {tau_B > c} is open for every c (B closed, [0, c] compact); on {tau_B < infinity}
tau_B is C^1 by the implicit function theorem at the transversal exit point, with
|grad tau_B(X)| <= exp(tau_B(X) ||DW||_inf)/kappa_B. Also tau_B(X) >= dist(X, B)/||W||_inf.
Step 3 (a C^1 Lyapunov function). Fix 0 < tau_1 < tau_2 < tau_3 < tau_4 and G smooth, nondecreasing, G = 0 on
(-infinity, tau_1], G = 1 on [tau_4, infinity], G(tau_2) <= 1/4, G(tau_3) >= 3/4, G' >= kappa_1 > 0 on [tau_2, tau_3].
Put g := G(tau_B) off B, g := 0 on B, g := 1 where tau_B = infinity. Then g is C^1 on C (it is constant near B and
on the open set {tau_B > tau_4}), reflection invariant, 0 <= g <= 1, ||grad g||_inf <= ||G'||_inf exp(tau_4 ||DW||_inf)/kappa_B,
W.grad g = G'(tau_B) >= 0, and W.grad g >= kappa_1 on the open set {1/4 < g < 3/4}, which lies in {tau_2 < tau_B < tau_3}.
g = 1 at distance >= d_4 := tau_4 ||W||_inf from B.
Step 4 (smoothing). Let g_e := g * rho_e with a reflection-invariant mollifier of radius e on C. Then g_e has all
derivatives bounded and is reflection invariant. Take e with e ||grad g||_inf < 1/24. If 1/3 <= g_e(X) <= 2/3, then
|g(Y) - g_e(X)| <= |g(Y) - g(X)| + |g(X) - g_e(X)| <= 2 e ||grad g||_inf < 1/12 on the e-ball around X, so 1/4 < g < 3/4
there, and
  W.grad g_e(X) = int [W(Y).grad g(Y) + (W(X) - W(Y)).grad g(Y)] rho_e(X - Y) dY >= kappa_1 - e ||DW||_inf ||grad g||_inf > 0
for e small. Let F be smooth and nondecreasing, F = 0 on (-infinity, 1/3], F = 1 on [2/3, infinity), and
  s := s_0 + (sigma - s_0) F(g_e).
Then W.grad s = (sigma - s_0) F'(g_e) W.grad g_e >= 0, since F' vanishes off {1/3 < g_e < 2/3}. s = sigma wherever g = 1
on the e-ball, in particular at distance >= d_4 + e from B; take tau_4 and e so small that d_4 + e < pi/24. This contains
{t >= log(x_P + rho_1) + pi/24} and the sector {|cos theta| < 1/2}, whose distance from B is at least pi/3 - pi/8 = 5pi/24
(so eps_2 = 1/2). s = s_0
on the points of B at distance >= e from its boundary, which contain the sets of (b) with beta_0 = beta_*/2 once e < beta_*/2
and e < rho_1/(2(x_P + rho_1)) (the cylinder distance from {|X - P| <= rho_1/2} to the circle is at least this). QED.
Remarks. (1) The order function is sigma on all of C except a thin neighbourhood of the closed x-axis segments and the
sources; the transition lies in the thin shell {tau_1 <= tau_B <= tau_4} just outside B, where every orbit exits once.
The only dynamical input is the block B, that is, the facts that the segment flows to 0, that the origin rates are
those of diag(-A, D) and that P is a source. (2) For t <= t_1 - 2, s(t, theta) = s_0 for |theta| <= beta_*/2 and
s = sigma for |theta| >= beta_* + pi/24 (B is the strip |theta| <= beta_* there, up to reflection, and the shell has width
below pi/24); this is the angular profile used in the normal family of Lemma H3-var, item 2. If s(t, .) converges in C^1
as t -> -infinity (expected from (I2) and Step 2, not needed here), the limit is nondecreasing in |theta| on [0, pi/2],
because vartheta_0 > 0 there.
(3) With V126 and V129 the lemma gives (H1) and (H2) of Lemma H-spec on X_s for this s; (H3) and low injectivity on
X_s remain OPEN.
