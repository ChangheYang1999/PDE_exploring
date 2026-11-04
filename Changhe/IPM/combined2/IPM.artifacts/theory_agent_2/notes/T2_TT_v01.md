# T2_TT_v01: the two-tier ball (scoping note) and the answer to theory_v01 T6.4 item 6

Version 1. Owner: the second theory agent (theory agent). Written 2026-11-02T21:45Z.
Requested by the coordinator 20:28Z item 3(a) (two-tier ball first; state the missing linear estimate; relate it to H1, Theorem D
and THR-D; closure function in the form of T2_WGK_v01 section 7, with its source quantity; due X2 = 2026-11-03T02:05Z)
and the coordinator 20:59Z (answer theory_v01 T6.4 item 6 together with this note).
Plain-text mathematics as in T2_WGK_v01. Paths are relative to the combined2 root.

Inputs used (read-only): exchange/theory_requirements/theory_v01.md (T2.1, T3.4, T4.1, T6.4), exchange/numerical_results/numerics_v01.md
(N2, N8), the theory auditor audit items AT-080, AT-081, AT-087, AT-088, theory_agent_2/notes/T2_WGK_v01.md, theory_agent_2/notes/T2_REV_v01.md, an external referee answer
(TAME-LB, TAME-UB). Script: theory_agent_2/research/tt/closure_tt.py (Python, FLOAT; output closure_tt.out in the same directory).

## Summary

| ID (proposed) | statement | label | section |
|---|---|---|---|
| T2-TT-LIP | smallness of A(k) = \|\|k\|\|_inf + \|\|grad k\|\|_inf does not bound DU[k]; tier 1 must be a C^(1,alpha)-level size | CLAIMED | 1 |
| T2-TT-CZ | \|\|Sym DU[k]\|\|_(inf,op) <= (1/2)\|\|grad k\|\|_inf + (2 sqrt2/(pi alpha))[grad k]_alpha + ((8 + B)/(sqrt2 pi))\|\|k\|\|_inf, B = 4(2 sqrt2 - 1)/3 | CLAIMED (constants EXACT) | 3 |
| T2-TT-OR | for S1 k with ell(k) = 0, the solution of A_k z = -G has ell(z) = -G_y(0)/a0 | CLAIMED | 2 |
| T2-TT-H1 | H1 restricted to a small C^(1,alpha) ball implies the target estimate H-L; the converse fails | CLAIMED | 2 |
| T2-TT-CL | Hoelder-tier closure: under H-L and F_y(0) = 0, one linear condition gives a unique solution in the tier-1 ball (Banach, no Schauder) | CONDITIONAL on H-L | 4 |
| T2-TT-NQ | the N tier is optional; its conditions; the M-dependence of C_eps_bar decides whether it is qualitative | HEURISTIC / OPEN | 5 |
| T2-TT-NT | necessary test NT-L for every WG-K (T2-CF) closure: c_4' A(h_0) + q \|\|Sym DU[h_0]\|\|_(inf,op) < beta - eps, h_0 = -L^(-1) F | CLAIMED; FLOAT proxy inconclusive | 6 |
| T2-CW-Q | c_W(q) <= max(c_W(2), c_W(3)) for 2 <= q <= 3 | CLAIMED | 8 |

Main reading.
- The two-tier ball works with tier 1 alone. Under the missing linear estimate H-L (section 2), the small weighted
  C^(1,alpha) ball is invariant under one linear condition on (N_Y(F), ||F||_2), and the fixed-point map is an L^2
  contraction there. No Gagliardo-Nirenberg conversion and no constant that degenerates as q -> 2 enters. The N tier adds
  only regularity.
- The price is the conversion constant D(alpha) of order 1/alpha from C^(1,alpha) to the strain (section 3). With the
  HEURISTIC size eps_L ~ beta_L/(2 C_sig D(alpha)), the uncentered 007 problem fails already because ||F||_2 = 0.377 is
  too large, for every alpha (section 4). So re-centering is still needed. What changes is the norm of the source: S_F, sup norms of 1 + alpha
  + delta derivatives, instead of N_q(F), q derivatives in weighted L^2.
- NT-L (section 6) is a necessary condition for the WG-K criterion that no improvement of C_eps_bar, c_W or the GN
  constants can remove. On the h_N proxy it is undecided, since ||grad h_N||_inf (0.026 to 0.31, depending on the
  cutoff) is of the same size as beta (0.22 to 0.32).
- T6.4 item 6 (section 8): c_4' and c_W do not degenerate as q -> 2. C_eps_bar is expected to degenerate faster than
  any power when the sharp tame constant 1 + delta_0 is used (HEURISTIC). kappa_q >= 1/sqrt2 (AT-081) shows that no bound
  on kappa_q rescues T3.4.

## 0. Notation

- A_k h = W_k.grad h - h + U[h].grad rho_bar, W_k = V + U[k]; L = A_0. The fixed-point map T(k) := z, the L^2 solution of
  A_k z = -F. A fixed point h = T(h) solves L h + U[h].grad h = -F.
- U[-Delta psi] = (-psi_xy, psi_xx); |m| <= 1, div U = 0. ell(k) = d_y U_2[k](0). For S1 k, U[k](0) = 0 and
  DU[k](0) = diag(-ell(k), ell(k)).
- beta_0: the L^2 rate of A_k, uniform in k because U[k].grad is skew (AT-060 check). For 007, beta_0 = 2.0021 (AN-010).
  R = ||F||_2/beta_0; G0 = ||F||_2.
- h(k) := ||k||_inf + ||grad k||_inf + [grad k]_alpha, with [grad k]_alpha := max_j [d_j k]_alpha (unweighted).
  H(k) := H_(sigma_L,alpha)(k) = ||w||_inf + ||grad w||_inf + [grad w]_alpha with w = <X>^(sigma_L) k (NORM-H, sum form).
- N_Y(G) = ||G||_2 + S_F(alpha, delta, sigma_L), S_F = ||<X>^(sigma_L) G||_(C^(1+alpha+delta)) (NORM-SF, sum form). Note
  N_Y(G) >= ||G||_2.
- a0 = d_y rho_bar(0) = 10.3119... (EXACT); F_y(0) = 0 for 007 (EXACT, AN-001, AT-005).

## 1. Tier 1 must be at the C^(1,alpha) level [T2-TT-LIP, CLAIMED]

The T2.1 target uses the ball A(k) = ||k||_inf + ||grad k||_inf <= eps_L. This is too weak: smallness of A(k) does not make
W_k Lipschitz, and ell(k) need not exist.

Example.
- Let g = chi(X) cos(2 theta), with chi a smooth radial cutoff equal to 1 near 0; g is even in x and in y. Put
  k := chi_2(X) int_0^y g(x, t) dt with a second cutoff chi_2 equal to 1 on the support of chi. Then k is S1 and compactly
  supported.
- d_x cos(2 theta) = 4 x y^2/r^4, and int_0^y 4 x t^2/(x^2 + t^2)^2 dt = int_0^(y/x) 4 s^2/(1 + s^2)^2 ds <= pi. So
  ||grad k||_inf and ||k||_inf are finite, and A(lambda k) = lambda A(k) is as small as we like.
- But d_y U_2[k] = -Q11(d_y k), Q11 = (1 + P)/2, where P has symbol cos(2 phi) and kernel -(1/pi) cos(2 theta)/|Y|^2
  (principal value). Near 0, d_y k = g, and for |X| << |Y| < 1 we have g(X - Y) ~ cos(2 theta_Y). So
  P g(X) = -(1/pi) int cos^2(2 theta) dtheta int_|X|^1 dr/r + O(1) = -log(1/|X|) + O(1).
  Hence d_y U_2[lambda k] is unbounded near the origin for every lambda > 0.
- W_k is then not Lipschitz, the transport A_k is outside the Lipschitz theory, and ell(k) is undefined.

Correction proposed for T2.1: tier 1 must bound a Hoelder modulus of grad k. Either use H(k) <= eps_L (the same norm as
the output of the estimate, which is what invariance needs anyway), or use eps(k) + Lambda(k) <= eps_L with
eps(k) = ||DU[k]||_inf and Lambda(k) = [DU[k]]_alpha, as in H1.

## 2. The missing linear estimate H-L, the origin identity, and the relation to H1

Hypothesis H-L(alpha, sigma_L; beta_L, C_L, eps_L). Fix 0 < alpha < 1, sigma_L >= 0 and
delta with alpha/(2c - 2) < delta < 1 (the frozen-origin range of AT-087). There are beta_L > 0, C_L < infinity and
eps_L > 0 such that: for every S1 k with ||k||_2 < infinity, ell(k) = 0 and H(k) <= eps_L, and every S1 G with
N_Y(G) < infinity, the L^2 solution z of A_k z = -G satisfies

    H(z) <= beta_L^(-1) N_Y(G) + C_L ||z||_2.                                                       (H-L)

Remarks.
- The L^2 solution exists and is unique, with ||z||_2 <= ||G||_2/beta_0. W_k is Lipschitz on this ball by section 3.
- Since ||z||_2 <= ||G||_2/beta_0, (H-L) is equivalent to H(z) <= beta_L^(-1) S_F(G) + C'_L ||G||_2 with
  C'_L = beta_L^(-1) + C_L/beta_0. It would help to state the estimate with S_F alone in the beta_L term, so that the
  L^2 part of the source carries only the remainder constant (section 4).
- Compactness. If the remainder comes from a compactness argument, ||z||_2 is a natural remainder only when the weighted
  C^(1,alpha) ball embeds compactly into L^2, that is for sigma_L > 1 (<X>^(-sigma_L) in L^2). For sigma_L <= 1, a
  weighted sup remainder ||<X>^(sigma') z||_inf with sigma' < sigma_L is the natural replacement (HEURISTIC).
- The gap. At the Lipschitz level the perturbation k enters the rate through Sym DU[k] with a coefficient of order 1
  (1 for ||grad z||_inf, 1 + alpha for [grad z]_alpha; not q) and through the weight term sigma_L U[k].X/<X>^2. So the
  loss is of order (D_sym + sigma_L D_full) h(k) <= (D_sym + sigma_L D_full) C_sig H(k) (section 3).
  HEURISTIC scale: eps_L ~ beta_L/(C_sig (D_sym + sigma_L D_full)). This is used only in the HEURISTIC tables.
- The background coupling grad(U[z].grad rho_bar) contains DU[z]^T grad rho_bar. Its C^alpha size is up to
  D(alpha) |grad rho_bar| ~ 9 x 10.3 at alpha = 1/10 near the origin. So BG-L cannot be obtained by treating the coupling
  as a perturbation of a pointwise sup-norm matrix; it must be kept in the operator exactly (the joint inverse of R11).
  This is a remark for the first theory agent's scoping of BG-L.

Lemma T2-TT-OR (origin identity; CLAIMED). Let k be S1 with ell(k) = 0 and W_k Lipschitz, and let z be an S1 solution of
A_k z = -G that is C^1 near 0, with G C^1 near 0. Then a0 ell(z) = -G_y(0).
Proof. Differentiate in y at X = 0. W_k(0) = 0; DW_k(0) = diag(b, 1) + diag(-ell(k), ell(k)) = diag(b, 1). So
d_y(W_k.grad z)(0) = (d_y W_k)(0).grad z(0) = z_y(0), since z_x(0) = 0 for z even in x. The term -z gives -z_y(0). In
d_y(U[z].grad rho_bar)(0), U[z](0) = 0, d_x rho_bar(0) = 0 and d_y U_1[z](0) d_x rho_bar(0) = 0, so only
d_y U_2[z](0) d_y rho_bar(0) = a0 ell(z) remains. Summing, z_y(0) - z_y(0) + a0 ell(z) = -G_y(0). QED.
Consequences.
- T preserves {ell = 0} exactly when F_y(0) = 0. This holds for 007 (EXACT).
- z_y(0) is not determined at this order. This is the neutral jet of AT-080, which (H-L) must control through the
  frozen-origin conditions (R6.3, R6.4) and the source condition delta > alpha/(2c - 2).
- For a re-centered problem with S1 center h_*: F_* = F + L h_* + U[h_*].grad h_* has
  d_y F_*(0) = ell(h_*)(a0 + d_y h_*(0)), by the same computation with k = 0 and the product term. The re-centered
  operator adds U[d].grad h_*, so its identity reads (a0 + d_y h_*(0)) ell(d) = -d_y F_*(0) when ell(h_*) = ell(k) = 0.
  So the center must satisfy ell(h_*) = 0 exactly (the alternative d_y h_*(0) = -a0 is far from any small center).

Lemma T2-TT-H1 (H1 implies H-L; CLAIMED). Suppose H1 holds:
H(z) <= C_0[N_Y(G) + ||z||_2 + c_T Lambda(k) ||grad z||_inf] whenever eps(k) <= eps_0. Let C_CZ(alpha) be the norm of the
zero-order operators in DU on C^alpha (finite for 0 < alpha < 1; standard, not evaluated), so that
Lambda(k) <= C_CZ(alpha) [grad k]_alpha <= C_CZ(alpha) C_sig H(k).
Then H-L holds with beta_L^(-1) = C_L = 2 C_0 and
eps_L = min{ eps_0/(D_full C_sig), 1/(2 C_0 c_T C_CZ(alpha) C_sig c_grad) }.
Proof. ||grad z||_inf <= c_grad H(z) with c_grad = max(1, sigma_L), and eps(k) <= D_full h(k) <= D_full C_sig H(k)
(section 3). On H(k) <= eps_L the tame term is at most H(z)/2; absorb it. QED.
- The converse fails: H-L says nothing about large Lambda(k).
- Relation to Theorem D. Theorem D (D1) (A_F + eta M <= M, eta = K(1 + R/M) R^(theta_I) M^(1 - theta_I)) closes a Hoelder
  ball of size M under the full H1 and needs THR-D, R^(alpha/2)(Sigma_F + R) <= tau_*^((2+alpha)/2)/C_0. Under H-L
  alone, only the small-ball case is available, and there the closure is linear in (Sigma_F, R) (section 4). The
  favourable factor R^(alpha/2) of THR-D is lost. In exchange, the tame term never appears, because the ball is small
  in the same norm in which the output is measured.
- T1.2 gives Hoelder output by embedding from H^q (H(h0) <= c_mu C_S(q, alpha) [N(F)/beta_1 + C_1 ||F||_2]). An H-L
  obtained in this way would require N(F) small and gain nothing over T2-CF. H-L must have a sup-norm source
  quantity N_Y.

## 3. Conversion constants [T2-TT-CZ, CLAIMED; constants EXACT]

Sym DU[k] in terms of k. With Q_ij the multipliers xi_i xi_j/|xi|^2 and P = Q11 - Q22 (symbol cos 2 phi):
- Sym_11 = Q11(d_y k) = d_y k/2 + P(d_y k)/2;
- Sym_12 = -P(d_x k)/2;
- Sym_22 = -Sym_11.
- The antisymmetric part of DU[k] is local: (d_y U_1 - d_x U_2)/2 = d_x k/2.
Hence ||Sym DU[k]||_op <= |d_y k|/2 + (1/sqrt2) max_j |P d_j k| pointwise, and ||DU[k]||_op <= ||Sym DU[k]||_op + |d_x k|/2.

Lemma. For g = d_j k with k bounded and g in C^alpha:
    ||P g||_inf <= (4/(pi alpha)) r^alpha [g]_alpha + ((8 + B)/(pi r)) ||k||_inf    for every r > 0,
with B = int_0^(2 pi) |cos 2t cos t| dt = 4(2 sqrt2 - 1)/3 = 2.437903 (EXACT; quadrature agrees to 12 digits).
Proof.
- Inner part: the kernel has mean zero on circles, so int_(|Y|<r) kappa(Y)(g(X - Y) - g(X)) dY is at most
  (1/pi) int |cos 2t| dt int_0^r rho^(alpha - 1) d rho [g]_alpha = (4/(pi alpha)) r^alpha [g]_alpha.
- Outer part: integrate by parts in Y_j. Here grad kappa = (2/pi)(cos 3t, sin 3t)/r^3, so
  int_(|Y|>r) |d_j kappa| = 8/(pi r). The boundary term is at most (1/(pi r)) int |cos 2t| |cos t| dt ||k||_inf = B ||k||_inf/(pi r).
QED.
- At r = 1: ||P d_j k||_inf <= (4/(pi alpha)) [d_j k]_alpha + ((8 + B)/pi) ||k||_inf.
- The optimum over r is (1 + alpha) a^(1/(1+alpha)) (b/alpha)^(alpha/(1+alpha)) with a = 4[g]_alpha/(pi alpha) and
  b = (8 + B)||k||_inf/pi. It is in the script.

Consequence: ||Sym DU[k]||_(inf,op) <= a1 ||grad k||_inf + a2 [grad k]_alpha + a3 ||k||_inf, with
a1 = 1/2 (1 for the full DU), a2 = 2 sqrt2/(pi alpha), a3 = (8 + B)/(sqrt2 pi) = 2.349. So D_sym(alpha) := max(a1, a2, a3)
bounds ||Sym DU[k]||_(inf,op)/h(k); D_full is the same with a1 = 1.

| alpha | a2 | D_sym = D_full |
|---|---|---|
| 0.05 | 18.006 | 18.006 |
| 0.10 | 9.003 | 9.003 |
| 0.20 | 4.502 | 4.502 |
| 0.30 | 3.001 | 3.001 |
| 0.50 | 1.801 | 2.349 |

- Order 1/alpha (HEURISTIC sharpness). If d_y k = |X|^alpha cos(2 theta) near 0 (even in x and y; k S1 as in section
  1), then P(d_y k)(0) = -(1/pi) int cos^2(2t) dt int_0^1 rho^(alpha - 1) d rho + O(1) = -1/alpha + O(1), with
  [d_y k]_alpha bounded uniformly in alpha (about 2). So D_sym(alpha) >= c/alpha. Compare the strain constant of the
  Sobolev route, which grows like (q - 2)^(-1/2).
- Weights (FLOAT, script section 2): h(k) <= C_sig H_(sigma_L,alpha)(k) with C_sig = 2.87 (sigma_L = 1, alpha = 1/10),
  3.43 (sigma_L = 7/5, alpha = 1/10), 2.76 (sigma_L = 1, alpha = 3/10). Also ||grad z||_inf <= c_grad H(z) with
  c_grad = max(1, sigma_L), since |grad <X>^(-sigma)| <= sigma <X>^(-sigma-1).
- Besov alternative (HEURISTIC; not checked). In a B^1_(inf,1)-type tier the zero-order operators in DU are bounded on
  every dyadic block with absolute constants. That would remove the 1/alpha. The frozen-origin conditions of Part II are
  stated in C^(1,alpha), so this would need its own origin analysis.

## 4. The Hoelder-tier closure [T2-TT-CL, CONDITIONAL on H-L]

Theorem. Assume H-L(alpha, sigma_L; beta_L, C_L, eps_L), F_y(0) = 0 and N_Y(F) < infinity. Put R = G0/beta_0, and let
c_grad = max(1, sigma_L). If eps satisfies

    beta_L^(-1) N_Y(F) + C_L R <= eps <= eps_L   and   c_grad eps < beta_0,                         (CF-H)

then K^H_(R,eps) := {k S1 : ell(k) = 0, ||k||_2 <= R, H(k) <= eps} contains exactly one h with T(h) = h, that is,
L h + U[h].grad h = -F.
Proof.
- Invariance. Let k be in K^H and z = T(k). Then ||z||_2 <= ||F||_2/beta_0 = R. By (H-L),
  H(z) <= beta_L^(-1) N_Y(F) + C_L R <= eps. By Lemma T2-TT-OR, ell(z) = -F_y(0)/a0 = 0. S1 is preserved.
- Contraction in L^2. For k, k' in K^H with z = T(k), z' = T(k'): A_k (z - z') = -U[k - k'].grad z'. The L^2 rate gives
  beta_0 ||z - z'||_2 <= ||U[k - k']||_2 ||grad z'||_inf <= ||k - k'||_2 c_grad eps, using |m| <= 1.
- Closedness. K^H is closed in L^2.
  - If k_n -> k in L^2 with H(k_n) <= eps, a subsequence converges in C^1_loc (Arzela-Ascoli), and the sup and Hoelder
    bounds pass to the limit.
  - ell is continuous along such sequences: ell(k) = -(1/2) d_y k(0) - (1/2) P(d_y k)(0). The inner part converges by
    the C^alpha bounds. The outer part is int d_j kappa k + boundary, and converges by dominated convergence, since
    |d_j kappa| is integrable on |Y| > r and the k_n are uniformly bounded.
- Banach's fixed-point theorem applies on the complete metric space K^H. QED.
- No Schauder argument and no N tier is needed.
- The solution has H(h) <= eps. Its H^q_W regularity is a separate qualitative question (section 5).

Closure function (in the form of T2_WGK_v01 section 7). closure_H(G0, NY, beta_L, C_L, eps_L, beta0, sigma_L) in
research/tt/closure_tt.py returns the interval of admissible eps, or None. Source quantity: N_Y(F) = ||F||_2 + S_F(alpha, delta, sigma_L)
with alpha/(2c - 2) < delta < 1. For P-S1 (q = 21/10), c = 1.81032, so at alpha = 1/10 delta must exceed 0.0617.
Closure requires N_Y(F) <= beta_L (eps_L - C_L R). Since N_Y(F) >= G0, it requires in particular
G0 (beta_L^(-1) + C_L/beta_0) <= eps_L.

HEURISTIC table. The unknown constants are chosen: eps_L = beta_L/(C_sig (D_sym + sigma_L D_full)), the Lipschitz-level
loss of section 2 expressed in H; sigma_L = 1; beta_0 = 2.00215. Entry: largest N_Y(F) that closes. A star marks entries
below G0, where no F with that G0 closes; "none" means that no F closes.

| alpha | beta_L | C_L | eps_L | G0 = 0.377 | 0.0521 | 0.01 | 1e-3 |
|---|---|---|---|---|---|---|---|
| 1/10 | 0.1 | 0 | 0.0019 | 1.9e-4 * | 1.9e-4 * | 1.9e-4 * | 1.9e-4 * |
| 1/10 | 0.3 | 0 | 0.0058 | 1.7e-3 * | 1.7e-3 * | 1.7e-3 * | 1.7e-3 |
| 1/10 | 0.6 | 0 | 0.0116 | 7.0e-3 * | 7.0e-3 * | 7.0e-3 * | 7.0e-3 |
| 1/10 | 0.6 | 0.1 | 0.0116 | none | 5.4e-3 * | 6.7e-3 * | 6.9e-3 |
| 1/10 | 0.6 | 1 | 0.0116 | none | none | 4.0e-3 * | 6.7e-3 |
| 3/10 | 0.3 | 0 | 0.0181 | 5.4e-3 * | 5.4e-3 * | 5.4e-3 * | 5.4e-3 |
| 3/10 | 0.6 | 0 | 0.0363 | 0.022 * | 0.022 * | 0.022 | 0.022 |
| 3/10 | 0.6 | 0.1 | 0.0363 | 0.011 * | 0.020 * | 0.022 | 0.022 |
| 3/10 | 0.6 | 1 | 0.0363 | none | 6.2e-3 * | 0.019 | 0.022 |

The full table, including beta_L = 0.1 and C_L = 0.1 rows, is in closure_tt.out.

Reading (HEURISTIC).
- The uncentered 007 problem (G0 = 0.377) fails for every row and every alpha. It needs G0 <= beta_L eps_L, and
  beta_L eps_L <= beta_L^2/((1 + sigma_L) D(alpha)) <= 0.36/(2 x 2.349) = 0.077 for beta_L <= 0.6 and sigma_L = 1, since
  C_sig >= 1 and D(alpha) >= a3 = 2.349 for every alpha.
- With re-centering (||F_*||_2 <= 0.01) the requirement becomes N_Y(F_*) <~ 0.007 at alpha = 1/10, or <~ 0.022 at
  alpha = 3/10 (beta_L = 0.6, C_L = 0).
- Comparison on one residual, E6a (G0 = 0.0254; numerics_v01 N2). At P-H = (1/2, 2/5, 7/4): S_F in [51.7, 64.2], with
  S0 = 0.627, S1 = 1.792 and S2 = 84.8 (sup norms of g, grad g and D^2 g, g = <X>^(7/4) F). The interpolation
  [grad g]_gamma <= (2 S1)^(1 - gamma) S2^gamma gives, at the P-H weight:
  - alpha = 1/10, delta = 7/100 (gamma = 0.17): [grad g]_0.17 <= 6.1, so N_Y <~ 8.5, about 1.2e3 times the 0.007 allowed;
  - alpha = 3/10, delta = 19/100 (gamma = 0.49; delta must exceed 0.185): [grad g]_0.49 <= 16.9, so N_Y <~ 19.3, about
    9e2 times the 0.022 allowed.
  E6a also fails on G0 alone, since 0.0254 exceeds both allowed values.
  In T2-CF with the same optimistic choices (T2_REV_v01 section 6, v2 constants, C_eps_bar = 0, c_4' = 1, c_W = 1), the
  largest N(F) at G0 = 0.0254 is 0.0218 at P-Q2 and 0.0192 at P-Q1, against N_q(E6a) = 475 and 3028: factors 2.2e4 and
  1.6e5. So the Hoelder tier is 20 to 180 times closer for E6a. This is the gain from dropping GN. It is not a closure.
- The scale of the requirement is fixed by beta_L, C_sig and D(alpha); q does not enter.

## 5. The N tier [T2-TT-NQ, HEURISTIC / OPEN]

Two-tier ball K^TT_(R,eps,M) := K^H_(R,eps) intersected with {N(k) <= M}. With UT-K in the form
b N(z) <= N(F) + c_4' N(k) A(z) + (b C_eps_bar)^(1/2) ||z||_2, evaluated on this class:
- (N1) b := beta - eps_g - q D_sym C_sig eps - sigma D_full C_sig eps > 0 (gap, with the strain bounded by tier 1 instead
  of GN; eps_g is the slack of Lemma WG-K; sigma is the weight exponent of N);
- (N2) c_4' c_A eps < b (tame term bounded by tier 1: A(z) <= c_A H(z), with c_A = c_grad for A = ||grad z||_inf and
  c_A = 1 + sup |grad <X>^(-sigma_L)| (1.385 for sigma_L = 1) for A = ||grad z||_inf + ||z||_inf);
- (N3) M >= [N(F) + (b C_eps_bar)^(1/2) R]/(b - c_4' c_A eps).
(N1) and (N2) do not involve M. (N3) is qualitative, that is, it holds for all large M, if and only if
C_eps_bar(class)^(1/2) = o(M). This is the open point.
Example (HEURISTIC, closure_tt.out; A = ||grad z||_inf, c_A = 1): beta = 0.6, q = 21/10, sigma = 1, eps = eps_L/2 of the
beta_L = 0.6 row. Then
b = 0.135 at alpha = 1/10 and at alpha = 3/10. With N(F) = 1, C_eps_bar = 1 and R = 0.188, M_min = 8.3 (c_4' = 1) and 13.9
(c_4' = 10) at alpha = 1/10. At alpha = 3/10, M_min = 9.1 for c_4' = 1, and c_4' = 10 violates (N2).
- With the sharp tame constant c_4' = 1 + delta_0 (TAME-UB, the external referee t2-tame1 (1), (33)), C_eps_bar depends on M through the
  frequency cut Lambda_1 with C M Lambda_1^(-(q-2)/4) <= delta_0. So the dependence is at least polynomial in
  M^(4/(q-2)) unless C_eps_bar is independent of Lambda. In that version, (N3) is not qualitative.
- On the two-tier class, the small-coefficient terms of KP-W (c_1 eps(k), c_3 ||a||_inf) can be bounded by the tier-1
  radius instead of by a frequency cut. Only c_2 ||e_Lambda||_2 <= C Lambda^(-q) M needs Lambda, with exponent 1/q
  (HEURISTIC). The tame constant is then the KP-W constant c_4 (not 1 + delta_0), and (N2) requires c_4 c_A eps < b,
  which is affordable because eps is small.
- The N tier is not needed for existence (section 4). Its role is the H^q_W regularity of the fixed point. That can
  also be obtained a posteriori for the single coefficient k = h (HEURISTIC).
Recommendation: treat tier 1 as the closure and the N tier as a regularity statement. Do not let T2-CF-type constants
enter the tier-1 closure.

Sobolev two-tier variant (HEURISTIC). Two Sobolev tiers q1 < q:
- For q1 > 2 the closure is the one-tier T2-CF at q1, and the upper tier adds regularity. So the choice of q already
  covers it.
- For q1 <= 2 the tier is below the Lipschitz threshold, and the transport A_k is outside the Lipschitz theory.
So the Lipschitz-level tier must be a Hoelder or Besov tier, as in section 3.

## 6. Necessary test NT-L [T2-TT-NT, CLAIMED; FLOAT proxy]

Proposition. Suppose (D1-K) and (D2-K) of T2-CF (T2_WGK_v01 section 7, T2_REV_v01 section 6) hold for some M, with
constants (eps, C_eps_bar, c_4', c_W) and the tame quantity A of the chosen version. Let h_0 := T(0) = -L^(-1) F. Then

    c_4' A(h_0) + q ||Sym DU[h_0]||_(inf,op) < beta - eps.                                          (NT-L)

Proof.
- (D1-K) reads N(F)/b + (C_eps_bar/b)^(1/2) R + (c_4'/b) M A_sup <= M with
  A_sup = C_GN c_W^(1-theta) R^theta M^(1-theta) + C_inf c_W^(1-theta_0) R^(theta_0) M^(1-theta_0). Since N(F) > 0,
  c_4' A_sup < b.
- The criterion gives T(K_(R,M)) contained in K_(R,M) and 0 is in K_(R,M), so h_0 is in K_(R,M). The GN bounds behind
  A_sup and Lemma SYM apply to h_0. Hence A(h_0) <= A_sup and q ||Sym DU[h_0]|| <= q C*_sym R^theta (c_W M)^(1-theta),
  which is the first term of tau_bar.
- So c_4' A(h_0) < b = beta - eps - tau_bar <= beta - eps - q ||Sym DU[h_0]||. QED.

Remarks.
- (NT-L) does not depend on C_eps_bar, on the value of c_W or on the GN constants. Improving those cannot rescue a case
  where (NT-L) fails.
- On c_4'. The best value available is c_4' = 1 + delta_0 with A = ||grad h||_inf (TAME-UB; the external referee t2-tame1 (33)
  supports this under the uniform compact-remainder hypothesis (34)). TAME-LB (c_4 >= 1) is a statement about the KP-E
  form, which has no gap term. For the UT-K form with slack eps > 0, the same packet construction gives c_4' >= 1 only
  when the packets can be placed where the slack of the pointwise gap vanishes (HEURISTIC). So c_4' < 1 in UT-K is not
  excluded by this note.
- Re-centered version: c_4' A(d_0) + q ||Sym DU[d_0]|| < beta_* - eps with d_0 = -L_*^(-1) F_*. It is small when F_* is
  small. This is why re-centering is the way for this route.
- Hoelder-tier version: (CF-H) gives H(h_0) <= eps <= eps_L, so ||grad h_0||_inf <= c_grad eps_L.

FLOAT proxy with h_N (numerics_v01 N8). h_N is not h_0: the L^2 distance bound ||h_N - h_0||_2 <= 0.1255 there exceeds
||h_N||_2 = 0.0354. beta(h_N) is the BG-q value with q Sym D(V + U[h_N]) in the frozen matrix, so it already contains the
strain of h_N pointwise.

| cutoff | 1e-4 | 1e-6 | 1e-8 | 1e-10 | 1e-12 | 1e-14 |
|---|---|---|---|---|---|---|
| \|\|grad h_N\|\|_inf | 0.0261 | 0.0432 | 0.0405 | 0.1205 | 0.1808 | 0.3085 |
| \|\|DU[h_N]\|\|_(op,inf) | 0.0168 | 0.0233 | 0.0253 | 0.0458 | 0.1623 | 0.2092 |

| tuple | beta(0) FLOAT | beta(h_N, 1e-14) | ratio \|\|grad h_N\|\|_inf/beta(0) at 1e-14 | at 1e-12 |
|---|---|---|---|---|
| (13/5, 7/5, 1/4) (P-BG1; certified beta = 1/10) | 0.2184 | 0.2077 | 1.41 | 0.83 |
| (12/5, 1, 1/4) | 0.2441 | 0.2441 | 1.26 | 0.74 |
| (5/2, 7/5, 1/2) (P-BG2; certified 1/4) | 0.3117 | 0.2373 | 0.99 | 0.58 |
| (5/2, 7/5, 1/4) | 0.3185 | 0.3088 | 0.97 | 0.57 |

Reading.
- With c_4' = 1 and the Sym DU term dropped, the 1e-14 proxy fails (NT-L) at (13/5, 7/5, 1/4) and (12/5, 1, 1/4), and
  is marginal at the two q = 5/2 tuples. Including q ||Sym DU[h_N]||_(inf,op) (not reported; at most q x 0.2092) can only
  make it worse.
- With the certified gaps (1/10 at P-BG1, 1/4 at P-BG2), the proxy fails at P-BG1 for the cutoffs 1e-10, 1e-12 and
  1e-14, and at P-BG2 for the cutoff 1e-14.
- The Galerkin correction is not converged in Lipschitz norms (a factor of 12 across cutoffs). So the test is undecided
  for h_0, but the sizes are comparable. An uncentered WG-K ball has at best an O(1) margin in (NT-L), whatever the
  constants.
- At P-S1 (beta target 3/5; origin margin 0.71) the term ||grad h_N||_inf alone passes at every cutoff. With
  q ||Sym DU[h_N]||_(inf,op) (at most 2.1 x 0.209 = 0.44 at 1e-14) the test is again undecided. beta(h_N) at P-S1 is not
  yet reported.

## 7. Scaling remark (HEURISTIC)

- R^theta N^(1-theta) scales like a Lipschitz norm, l^(-1) under X -> X/l.
- S_F scales like l^(-1-alpha-delta), the same as N_(q1) with q1 = 2 + alpha + delta.
- So the gain of a sup-norm tier is not a scaling gain. It is the removal of the GN step from L^2-based sizes to the
  Lipschitz-level quantities that enter the gap. Which source norm is smaller for an actual residual is a numerical
  question.
- Diagnostics that would decide which tier norm is smaller for actual candidates: S_F(alpha, delta, sigma_L) and
  N_(q1)(F) at matching order (q1 = 2 + alpha + delta), with the same weight.

## 8. Answer to theory_v01 T6.4 item 6 (q -> 2)

Question: does any constant that is not explicit (c_4', c_W, C_eps_bar) degenerate as q -> 2 faster than (q-2)^(-1/2)?
Is there a usable bound on kappa_q (AT-071)?

- c_4' (tame constant of UT-K): no. TAME-UB gives c_4' = 1 + delta_0 for every delta_0 > 0 and every q in (2, 3), with
  tame quantity ||grad h||_inf (CLAIMED). the external referee t2-tame1 confirms the argument with one repair (Lemma CU: differentiate
  the fixed-z representation, not the singular kernel), under a uniform low-frequency hypothesis (the external referee (32); (34) is
  one sufficient form) that remains an assumption. TAME-LB gives c_4 >= 1 in KP-E form for every q. The leading
  value 1 does not depend on q. The KP-W constant c_4 = C_q G C_W (1 + L + M_ell) (research/kpw/PROOF.md (iv)) is finite
  for each q. Its behaviour as q -> 2 is not evaluated, but none of the displayed dyadic sums has the ratio 2^(-(q-2))
  (HEURISTIC).
- c_W: no. Lemma T2-CW-Q (CLAIMED): c_W(q) = ||W^(-1)||_(H^q -> H^q) satisfies
  c_W(q) <= c_W(2)^(3-q) c_W(3)^(q-2) <= max(c_W(2), c_W(3)) for 2 <= q <= 3.
  Proof: H^s = [H^2, H^3]_(s-2) is an exact complex interpolation scale (norms ||J^s f||, J positive self-adjoint), and
  W^(-1) is a fixed operator; the S1 subspace is invariant under J and W^(-1). QED.
  The homogeneous constant of T2-CF (||k||_(Hdot^q) <= c_W^hom N(k)) satisfies c_W^hom <= c_W(q), so it is bounded in the
  same way.
  The integer-order norms are explicit. research/explicit/cw_ub.py uses exactly this interpolation, with explicit
  bounds M2 and M3 for the H^2 and H^3 norms: c_W <= 7.41, 4.95, 12.88 at P-Q2, P-BG2, P-Q1.
  FLOAT values on the S1 subspace (research/explicit/cw_power.out): 1.33, 1.28, 1.74; at q = 2.2 (sigma 7/5, r0 1/4):
  1.26. Homogeneous version (cw_hom.out): 1.30, 1.23, 1.71.
- C_eps_bar: yes, expected (HEURISTIC), in the version with c_4' = 1 + delta_0.
  - The remainder of TAME-UB decays like C M Lambda^(-(q-2)/4) (the external referee t2-tame1 (1)). Any such rate is at best
    Lambda^(-c(q-2)), since a function with N(k) bounded has strain only in C^(q-2).
  - So the frequency cut is Lambda_1 >= (C M/delta_0)^(1/(c(q-2))), and C_eps_bar, which is obtained by compactness
    (the external referee (34), not explicit), is at least a function of this Lambda_1.
  - Unless C_eps_bar is independent of Lambda, it grows faster than any power of (q - 2)^(-1); a growth like
    exp(C/(q-2)) is plausible. At q = 21/10 the exponent 4/(q-2) of the external referee (1) is 40.
  - C_eps_bar enters T2-CF only through (C_eps_bar/b)^(1/2) R. Through its M-dependence it also decides whether (D1-K)
    can be met at large M.
  - Consequence for T4.1 (P-S1, q = 21/10): a closure at q = 21/10 should not use c_4' = 1 + delta_0 together with an
    M-independent C_eps_bar. Either keep the KP-W constant c_4 (the T2_WGK_v01 c_4' = c_4(1 + C_chi)), whose remainder
    does not need the cut Lambda_1, or prefer a larger q. The explicit GN constants C*_sym, C_GN, C_DU grow like
    (q - 2)^(-1/2); the value constants (B_0, C_value, C_inf^U) stay finite (AT-080 correction).
  - In the two-tier route of sections 4 and 5, none of these constants enters the tier-1 closure. q does not enter at
    all; the alpha-dependence D(alpha) ~ 1/alpha replaces the q-dependence.
- kappa_q: AT-081 gives C_sym/sqrt2 <= C_norm(q) <= kappa_q C_sym, hence kappa_q >= 1/sqrt2. By T3.4 (i), the failure
  of (D1-K), (D2-K) for 007 persists for every strain coefficient kappa q C*_sym with kappa >= kappa_min, and
  kappa_min <= 0.1560 at all eight AN-023 tuples. Since 1/sqrt2 = 0.707 > 0.156, no bound on kappa_q can rescue the
  criterion at these tuples. The usable bound is the lower bound, and it settles the question negatively. It also
  limits any sharpening of the strain coefficient on the normalized ball to a factor of at most sqrt2.

## 9. Requests

- The first theory agent (T2.1 scoping, due X2):
  - (a) Replace the hypothesis A(k) <= eps_L by H(k) <= eps_L (section 1).
  - (b) State the estimate as H(z) <= beta_L^(-1) S_F(G) + C_L ||z||_2 (or with a weighted sup remainder for
    sigma_L <= 1), so that G0 enters only through C_L.
  - (c) Treat the coupling DU[z]^T grad rho_bar exactly: it is of size D(alpha) a0 in C^alpha (section 2).
  - (d) Use Lemma T2-TT-OR for the ell normalization: T preserves ell = 0 when F_y(0) = 0, and z_y(0) is the remaining
    neutral jet.
  - (e) If T2.1 is out of reach, the Besov B^1_(inf,1) tier is the alternative to scope.
- numerics (the first numerics agent, the second numerics agent):
  - (a) For h_0 (the H0_PLAN solve) and for h_N at every cutoff: ||grad h||_inf, ||h||_inf, ||Sym DU[h]||_(inf,op),
    H_(sigma_L,alpha)(h) at (sigma_L, alpha) = (1, 1/10), and beta(h) at P-S1, P-BG1, P-BG2 (NT-L, section 6).
  - (b) S_F(1/10, 7/100, sigma_L) and S_F(3/10, 19/100, sigma_L) for sigma_L in {1, 7/5}, with S0, S1 and
    [grad g]_(alpha + delta), for every candidate and for any F_*. Also N_(q1)(F) with q1 = 2 + alpha + delta and the
    same weight, for the comparison of section 7.
  - (c) Any re-centering center must satisfy ell(h_*) = 0 exactly (Lemma T2-TT-OR); report d_y F_*(0).
- The theory auditor (audit): T2-TT-LIP, T2-TT-CZ (the constants a2, a3 and B), T2-TT-OR, T2-TT-H1, the proof of T2-TT-CL given H-L,
  T2-TT-NT and T2-CW-Q.
- The coordinator: the two-tier ball is scoped. Tier 1 is the closure; its single missing input is H-L, which is T2.1 with
  corrections (a) and (b). The N tier is a regularity statement. The quantitative T4.1 consequence is in section 8.

## 10. Files

- research/tt/closure_tt.py, closure_tt.out (this note; FLOAT).
- research/explicit/cw_power.py, cw_power_big.py, cw_ub.py, cw_hom.py with .out files (c_W; to be written up in T2_EXP_v01).
- an external referee answer, PROOF.md, VERIFICATION.md (TAME-LB, TAME-UB referee route).
