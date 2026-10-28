Lemma Emb (embeddings of the high full spaces; DERIVED, submitted for checking). Notation: sigma = 25/4, delta = 9/5,
gamma = -1/2, b = e^((3+delta)t) far left and e^(gamma t) far right, a = e^(-3t) b, p(theta) = cos^2(theta) sin(theta),
E beta = x^2 y beta(log r) = r^3 p(theta) beta(t). B_H = {J chi_0 + a v : v in H^(29/4)(R)}, Gamma_H = a H^sigma(R),
X_s = {h : v = h/b in H^(s(.)), u_X = chi h/(b p) in H^sigma, zero vertical trace}, s_min = 41/20, H_full = B_H (+) X_s,
Y_full = Gamma_H (+) X_s. Low spaces as in the moving-tail iteration: w = |x|^(-17/2) max(1, r)^(29/4), R = L^2_P(w dX),
G = L^2(e^(-t/2) dt on t < 0, e^(27t/4) dt on t > 0), B = {J chi_0 + w_0 : w_0, w_0' in G}, X0 = E B (+) R, Y = E G (+) R.
H_high^sigma = H_base^sigma + Q is the high space of the low/high product theorem (exponents 1/4 < delta < 2, gamma < -3/8,
sigma > 6, s > 2).
Claims. The following inclusions are continuous:
 (a) Gamma_H in G and B_H in B, hence Y_full in Y;
 (b) X_s in R, and for every coefficient perturbation B of the uniform high theory, X_s in the maximal low domain
     D_L = {u in R : (T + B.grad) u in R}; hence H_full in X0 and in the low graph domain of each perturbed operator;
 (c) H_full in H_high^(25/4), with the bulk order s = 41/20 in Q.
Proof. (a) For f = a phi: integral over t < 0 of |a phi|^2 e^(-t/2) = integral e^((2 delta - 1/2) t) |phi|^2, with
2 delta - 1/2 = 31/10 > 0; over t > 0 the weight is e^(-7t) e^(27t/4) = e^(-t/4). For beta = J chi_0 + a v, w_0 = a v and
w_0' = a (v' + (a'/a) v) with a'/a bounded, so ||w_0||_G + ||w_0'||_G <= C ||v||_(H^1).
(b) dX = r^2 dt dtheta. For h = b v: |h|^2 w dX = |v|^2 b^2 r^(-13/2) max(1, r)^(29/4) |cos(theta)|^(-17/2) dt dtheta. The radial
factor is e^((6 + 2 delta - 13/2) t) = e^(31t/10) on the left and e^(-t - 13t/2 + 29t/4) = e^(-t/4) on the right. The angular
factor is bounded off the vertical sector. On the sector h = b p u_X, and u_X is even about the vertical axis with zero
trace there, so u_X = cos^2(theta) u~ with sup_theta |u~(t, .)| <= C ||u_X(t, .)||_(H^3_theta); then |h|^2 |cos|^(-17/2) =
b^2 |cos|^(-1/2) sin^2 |u~|^2, integrable in theta, and integral dt ||u_X(t, .)||^2_(H^3_theta) <= ||u_X||^2_(H^sigma).
For the domain: T_0 h = b P_v v on the bulk and b p P_u u_X on the sector (the conjugated operators of the high theory),
with P_v v in H^(s(.) - 1) in L^2 and P_u u_X in H^(sigma - 1) = H^(21/4) in C^2 uniformly in t. The background field is
tangent to the vertical axis, so P_u u_X has zero trace there (u_X = 0 and d_t u_X = 0 on the axis, vartheta = 0 there), and
it is even; the same computation gives T_0 h in R. For a perturbation B the extra term is b p (B.grad u_X + d_u u_X),
d_u = beta B_t + (p'/p) B_theta, which is again even, has zero vertical trace (B_theta = O(cos theta), u_X = d_t u_X = 0),
and lies in H^(sigma - 1) by the sector bounds of the velocity theorem (chi Z and chi Z_theta/cos(theta) in H^sigma); the
bulk part is bounded in L^2 by ||B||_(C^1) ||v||_(H^1). Hence X_s in D_L, with norm bounds uniform on the ball.
(c) Choose a fixed angular cutoff chi' with chi' chi = chi' (supported where the cofactor is defined) and 1 - chi' supported
in |cos(theta)| >= epsilon. Then
     h = p_phys [a (chi' u_X)] + b [(1 - chi') v],   p_phys = x^2 y = r^3 p(theta), so p_phys a = p(theta) b.
The first term is in H_base^sigma with u = chi' u_X in H^sigma(R x S^1), even under both reflections (h and p have the same
parity); the second is in Q with s = 41/20 > 2 (Q carries no radial restriction and its b is our b; 1/4 < 9/5 < 2,
-1/2 < -3/8). For the scalar part, E(J chi_0 + a v) = p_phys [J chi + a (v + J (chi_0 - chi)/a)]; (chi_0 - chi)/a is smooth
with compact support in t, and v in H^(29/4)(R), viewed as a function on R x S^1, is in H^sigma. QED.
Consequences. With H = H_full, the low/high product theorem gives ||W[d].grad g||_Y <= C_B ||d||_X0 ||g||_H and
||DW[g]||_inf + |c[g]| <= C_V ||g||_H, and therefore the difference bound (4) of the moving-tail iteration,
||(A_h1 - A_h0) g||_Y <= C ||h1 - h0||_X0 ||g||_H for h0, h1 in the H ball, holds for H = H_full: (A_h1 - A_h0) g =
W[d].grad g + W[z].grad g + U[g].grad z + c[g] (m(ell_1) - m(ell_0)) with d = h1 - h0, z = z_ell1 - z_ell0, and
|ell_1 - ell_0| <= ||c||_(X0*) ||d||_X0 / 3 by n' >= 3; the z terms are bounded by C |ell_1 - ell_0| ||g||_H by the tail
velocity bounds and the coupling-change bound C_z : X0 -> Y of the moving-tail uniform theorem, and the last term by the
smoothness of m into Y.

Theorem E (conditional existence of the self-similar profile; DERIVED, submitted for checking as a CONDITIONAL THEOREM).
Setting: the exact moving-tail family rho_ell = rho_0 + chi_inf(r) (r^(1/ell) - r^k) Theta(theta), ell in a fixed interval I
with max(k, 1/ell) < q_* < 1/4, the scalar map n(ell) = 3 ell - 1 - c[rho_ell] (n(ell_0) = 0, n' >= 3), ell(h) defined by
n(ell(h)) = c[h], the operators A_h of the moving-tail family, and f0 = F_ell0(rho_0) (the residual of the normalized
modal density, in Y_full by the moving-tail residual analysis). Hypotheses:
 (I) (base low injectivity) the base operator A_0 : B (+) D_R -> Y is injective;
 (S) (smallness) with r_* the radius, K_H the uniform high inverse bound (B_H (+) D_H(v) -> Y_full) and K_L the uniform
     low inverse bound (into X0) that the moving-tail uniform theorem provides under (I), C the constant of the
     difference bound above, and eta0 = ||f0||_(Y_full), there is r <= r_* with
          K_H eta0 <= r,   K_L C K_H eta0 < 1.
Conclusion. There are ell in I and h in H_full with ||h||_(H_full) <= K_H eta0 and F_ell(rho_ell + h) = 0 in Y; h is the
X0-limit of h_(j+1) = -A_(h_j)^(-1) f0, h_0 = 0. The density rho = rho_ell + h has the parity of the problem, is C^1 off the
origin (s_min > 2), has cubic jet (1 + J(h)) x^2 y at the origin and far field r^(1/ell) Theta(theta) + o(r^(1/ell)) with
q = 1/ell in (0, 1/4), and solves the profile equation pointwise off the origin. If moreover |J(h)| < 1,
rho_norm(X) = lambda rho(X/lambda), lambda = (1 + J(h))^(1/2), is a solution with unit cubic coefficient (leading term
exactly x^2 y), the same ell and c, and tail amplitude lambda^(1 - q). It is unique in the closed r ball if K_L C r < 1.
Proof. Under (I) the moving-tail uniform theorem gives, for ||v||_(H_full) <= r_*, an isomorphism A_v : B_H (+) D_H(v) ->
Y_full with ||A_v^(-1) f||_(H_full) <= K_H ||f||_(Y_full), and the low isomorphism A_v : B (+) D_L(v) -> Y with
||g||_X0 <= K_L ||A_v g||_Y; by Lemma Emb (b), H_full lies in B (+) D_L(v), so the low bound holds on H_full. This is
hypothesis (16) of the conditional iteration theorem with H = H_full (a Hilbert space, hence reflexive), Y_H = Y_full
(continuously embedded in Y by Lemma Emb (a)) and R_v = A_v^(-1). Its hypothesis (4) is the difference bound above, and
(17) is (S). The iteration theorem gives h and the equation f0 + A_h h = 0 in Y, which is F_ell(h)(rho_ell(h) + h) = 0 by the
exact identity F_ell(h)(rho_ell(h) + h) = f0 + A_h h. The regularity and the jet follow from h in H_full: the scalar
component has beta(-inf) = J(h) and rho_ell = rho_0 = x^2 y + O(r^5) near the origin; the far-field statement uses
h = b v with v in H^(s(.)) in C^1 of the cylinder, so h = O(r^(-1/2)) pointwise at infinity, and rho_ell - r^q Theta =
O(r^(2k - 1)) there, both below r^q. The normalization is the scaling identity
F_ell(rho_norm)(X) = lambda F_ell(rho)(X/lambda) of the iteration theorem. QED.
Status of the hypotheses. (I) is OPEN (the computer-assisted route needs O(1e4) low modes with the present rigorous
tools; finite sections are NUMERICAL evidence only). (S) cannot be checked: r_*, K_H, K_L and C are qualitative constants
(compactness arguments), and the only certified residual size is a low norm (6049.11 < ||F||_Y < 8601.42 in the original
low space, ||F||_(Y_a) < 485.632 in the decoupled family), which is not the high norm eta0 and is in any case not
comparable with unknown constants. Hence Theorem E is not an existence theorem; it states exactly what remains.
