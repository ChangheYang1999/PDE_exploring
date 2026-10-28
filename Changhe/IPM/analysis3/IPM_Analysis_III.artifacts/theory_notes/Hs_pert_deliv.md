Theorem Hs-pert (uniform high estimate, generation, index 0 and a conditional uniform inverse for small rough transport
perturbations with frozen coupling; THEOREM, V157 to V160, constants qualitative). Notation of Proposition Hs; the order s
is the explicit repeller-block order of V130 (s = 25/4 on a neighbourhood of the vertical sector), and W~.grad s >=
kappa_s |grad s| with kappa_s > 0 (V154). G_s is the coefficient space of V156: g = J x^2 y chi_0 + b v_g, v_g in H^(s(.)),
chi_1 v_g/p in H^sigma, same parity, no trace condition, ||g||_G = |J| + ||v_g||_{H^(s(.))} + ||chi_1 v_g/p||_{H^sigma}. For g in G_s
     B_g := (U[g].e_r/r, U[g].e_theta/r) + (c[g]/3, 0),   T_g h := (V + U[g] + c[g] X/3).grad h - h,   S_g := T_g + C_R,
     D_g := {h in X_s : T_g h in X_s in distributions},
with the fixed remainder coupling C_R of the background (the coupling is frozen; T_0, S_0, D_0 are T_R, S, D_s). By V156,
B_g = c[g] E_0 + Z_g with E_0 = chi_0 (-cos 2theta, sin 2theta) + (1, 0)/3 smooth and |c[g]| + ||Z_g||_{H^(s(.))} + ||B_g||_{C_b^(1,alpha)}
+ ||chi_2 Z_g||_{H^sigma} + ||chi_2 Z_(g,theta)/cos(theta)||_{H^sigma} <= C_alpha ||g||_G for alpha < 1/20.
(i) (V157) Square-function commutator. With A_j = Op(e^(N Lambda) <xi>^(s(X)) psi_j(xi)), sum_j psi_j^2 = 1,
     (sum_j ||sum_l [A_j, B_l] d_l v||_2^2)^(1/2) <= C [||DB||_inf ||v||_{H^(s(.))} + ||B||_{H^(s(.))} ||Dv||_inf]
for B in H^(s(.)) with bounded first derivatives, and with C_E |c| ||v||_{H^(s(.))} in place of the B-terms for the smooth part
c E; for B = B_g the right side is at most C ||g||_G ||v||_{H^(s(.))}. This is not the bound for [A, B.grad] refuted in V153.
(ii) (V158) Dyadic energy. sum_j ||A_j v||^2 is equivalent to ||v||^2_{H^(s(.))} modulo the H^(s(.) - eps) norm, and for the
background transport P_0 = W~.grad + c_0
     - Re sum_j <A_j P_0 v, A_j v> = sum_j <M_0 R A_j v, R A_j v> + Re sum_j <(W~.grad s) log<D> A_j v, A_j v> + E(v),
|E(v)| <= eta ||v||^2_{H^(s(.))} + C_eta ||v||_{H^(s(.) - eps)} ||v||_{H^(s(.))}, with the matrix M_0 of (Q1). The extra term from
differentiating the cutoffs psi_j cancels pointwise because sum_j psi_j d_xi psi_j = 0. The coupling form (Q2), the penalty
(Q5') and the sector bounds of (Q0) hold in the square-summed form. On a maximal domain the sums are taken through a
finite index, the logarithmic forms are bounded below before the limit, and no graph-dense core is used.
(iii) (V159) Uniform compact-error estimate. Let eps = 1/5120 and L >= 0. There are r_* > 0, C, a Hilbert space W_* and a
compact K : X_s -> W_*, independent of g and lambda, with
     ||h||_{X_s} <= C ||(S_g - lambda) h||_{X_s} + ||K h||_{W_*},   h in D_g, ||g||_G <= r_*, 0 <= lambda <= L.
Proof outline: A_j (B_g.grad v) = B_g.grad w_j - N (B_g.grad Lambda) w_j - (B_g.grad s) A_j log<D> v + sum_l [A_j, B_(g,l)] d_l v
exactly; the logarithmic coefficient of the sum is (W~ + B_g).grad s >= 0 for small g (V154) and its form is bounded below
by V155 (alpha = 1/40); the commutators are (i); the zeroth-order and divergence terms are O(||g||_G); the penalty gets the
extra source B_g.grad v, bounded in H^(s(.) - 1) by C ||g||_G ||v||_{H^(s(.))}; the cofactor cutoff forcing stays triangular; the
absorption of Proposition Hs is repeated with a replaced by a + C_2 ||g||_G, and r_* is chosen last. The N_0 end energy of
Proposition H3-red changes by (1/2) div B_g - beta B_(g,r) + 4 tan(theta) B_(g,theta), which is O(||g||_G) (divided angular bound),
and the radial cutoff commutator has the bounded coefficient q + B_(g,r), so K is independent of g.
(iv) (V160) Generation, index 0, conditional uniform inverse. For ||g||_G <= r_* (after decreasing r_*): T_g with domain D_g
generates a strongly continuous semigroup on X_s with a growth bound uniform on the ball (positive dyadic Hilbert energy,
smooth approximation of g, flow representation, weak limits plus norm convergence); its generator domain is exactly D_g;
S_g - lambda : D_g -> X_s is Fredholm of index 0 for every lambda >= 0; and if S : D_s -> X_s is injective, then after
decreasing r_* every S_g is bijective and
     ||h||_{X_s} + ||T_g h||_{X_s} <= C ||S_g h||_{X_s},   h in D_g,
with C independent of g. By V152 the injectivity of S on D_s is the low injectivity question.
Scope. The theorem concerns the remainder block with the coupling of the fixed background. It does not include the
bordered block (jet column and axis row of L_ren and L_red under the perturbation), the moving background rho_ell of the
moving-tail formulation (V062), the low inverse for the perturbed operators, or any constant; these are the remaining
analytic inputs of the conditional existence theorem V062 besides low injectivity and the smallness conditions.
Regularity remark: the divided cofactor coefficient (p'/p) vartheta contains vartheta/cos(theta), which is W^(6,inf) and in
H^(6 + delta)_loc for delta < 1/2, not W^(7,inf); this covers the order 25/4 used in the flow argument.

Lemma K (tame coefficient commutator for the single variable-order operator; THEOREM, V161, an alternative to the square-function route of V157, not used by Theorem Hs-pert).
Notation of Proposition Hs. C = R x S^1, s smooth with bounded derivatives and 2 < s_0 <= s(X) <= s_+, Lambda smooth
and bounded with bounded derivatives, N >= 0, A = Op(a), a(X, xi) = e^(N Lambda(X)) <xi>^(s(X)) (uniform left
quantization). Delta_m (m >= 0) is a smooth inhomogeneous Littlewood-Paley partition with sum_m Delta_m = I,
S_k = sum_(m <= k) Delta_m (S_k = 0 for k < 0), Delta~_m a fattened block (Delta~_m Delta_m = Delta_m), and
w_m(X) = e^(N Lambda(X)) 2^(m s(X)). ||v||^2_{H^(s(.))} is equivalent to sum_m ||w_m Delta_m v||^2 (dyadic norm of
V126; e^(N Lambda) is bounded above and below). Let B = c E + Z, where c is a real number, E is a fixed
smooth bounded vector field with all derivatives bounded, and Z is in H^(s(.)) and in C_b^(1,alpha), 0 < alpha < 1. Put
     K_B v := sum_l [A, B_l] d_l v.
Claim. For 0 < eps <= eps_K := min(alpha/2, (s_0 - 2)/2) and v in H^(s(.)),
     ||K_B v||_2 <= C (|c| + ||DZ||_inf) ||v||_{H^(s(.))} + C (|c| + ||Z||_{H^(s(.))} + ||Z||_{C^(1,alpha)}) ||v||_{H^(s(.) - eps)},
C depending only on s, Lambda, N, E, alpha and eps. The same holds at the constant order sigma for
A_u = e^(N Lambda) <D>^sigma.
K_B does not contain the logarithmic term: A(B.grad v) = B.grad(A v) - N (B.grad Lambda) A v - (B.grad s) Op(a log<xi>) v
+ K_B v exactly (left quantization, since d_(X_l) a = a (N d_l Lambda + (d_l s) log<xi>) and d_l Lambda, d_l s depend on X
only), so the claim is consistent with V153, which REFUTES the corresponding bound for [A, B.grad].
Facts used (the kernel facts are those of the proof of V157: moderate weights, annular kernel bounds and the two
high-coefficient paraproduct types).
 (F1) Moderate weights: w_m(X)/w_m(Y) <= C (1 + 2^m d(X, Y))^M, and for k >= m - C_0,
      w_m(X)/w_k(Y) <= C 2^(-(k - m) s_0) (1 + 2^m d(X, Y))^M.
 (F2) Kernel and Bernstein bounds: the kernel of A Delta~_m is bounded by C_L w_m(X) 2^(2m) (1 + 2^m d(X, Y))^(-L) (the
      xi-derivatives of a carry no logarithm), so ||A f||_2 <= C ||w_m f||_2 for f with Fourier support in the annulus of
      Delta~_m, and ||w_m d Delta_m v||_2 <= C 2^m ||w_m Delta~_m v||_2.
 (F3) Frequency localization: a is in S^(s_+)_(1,delta) for every delta > 0 (X-derivatives cost powers of log<xi>), so
      ||Delta_j A Delta_m||_(L^2 -> L^2) <= C_R 2^(-R max(j, m)) for |j - m| > C_1 and every R.
 (F4) Hoelder blocks: ||Delta_k F||_inf <= C 2^(-k(1 + alpha)) ||F||_{C^(1,alpha)} for k >= 1, ||Delta_0 F||_inf <= C ||F||_inf.
 (F5) High-coefficient paraproduct (the two high-coefficient types of V157, with Q_j = Delta_j): for F in H^(s(.)) and
      G in L^inf, ||sum_k Delta_k F . S_(k + C_0) G||_{H^(s(.))} <= C ||F||_{H^(s(.))} ||G||_inf (by (F1), Schur and Young's
      inequality for the sequence 2^(-n s_0), n >= -C_0; s_0 > 0 is used).
Proof. For v smooth with compact support (then by density), B_l d_l v = sum_(k,m) Delta_k B_l Delta_m d_l v and
A d_l v = sum_m A Delta_m d_l v, so K_B v = sum_l sum_(k,m) [A, Delta_k B_l] Delta_m d_l v = I + II + III with
     I   = sum_l sum_m [A, S_(m - C_0 - 1) B_l] Delta_m d_l v                     (k < m - C_0, low coefficient),
     II  = sum_l A( sum_k Delta_k B_l . S_(k + C_0) d_l v )                         (k >= m - C_0, coefficient high, A outside),
     III = - sum_l sum_k Delta_k B_l . A S_(k + C_0) d_l v                          (k >= m - C_0, coefficient high, A inside).
I. Put b_m = S_(m - C_0 - 1) B_l and F_m = [A, b_m] Delta_m d_l v. The kernel of F_m is the kernel of A Delta~_m times
(b_m(Y) - b_m(X)), and |b_m(Y) - b_m(X)| <= ||D B||_inf d(X, Y), which gains 2^(-m); with (F1), (F2) and Schur,
||F_m||_2 <= C ||DB||_inf ||w_m Delta~_m v||_2 (the low-coefficient kernel bound of V157). Both A(b_m Delta_m d_l v) and b_m A Delta_m d_l v have their
Fourier mass in the m-th annulus up to the tails of (F3) (C_0 large), so ||Delta_j F_m||_2 <= C_R 2^(-R max(j, m)) 2^m
||B||_inf ||Delta~_m v||_2 for |j - m| > C_1 + 2, and almost orthogonality gives
     ||I||_2 <= C ||DB||_inf ||v||_{H^(s(.))} + C ||B||_inf ||v||_2,   ||DB||_inf <= |c| ||DE||_inf + ||DZ||_inf.
II. For the part with Z, ||A F||_2 <= C ||F||_{H^(s(.))} ((Q0), V146) and (F5) with G = d_l v give ||II_Z||_2 <= C ||Z||_{H^(s(.))} ||Dv||_inf. For the part with c E,
the blocks Delta_k E, k >= 1, are bounded in W^(R, inf) by C_R 2^(-kR), and the block k = 0 gives a product with Fourier
support in a fixed ball; hence ||II_E||_2 <= C |c| ||v||_2. Finally ||Dv||_inf <= C ||v||_{H^(s_0 - eps)} <= C ||v||_{H^(s(.) - eps)},
since s_0 - eps > 2 (two dimensions) and s(.) >= s_0.
III. By (F2), ||A S_(k + C_0) d_l v||_2 <= sum_(m <= k + C_0) ||A Delta_m d_l v||_2 <= C sum_(m <= k + C_0) 2^m a_m with
a_m = ||w_m Delta~_m v||_2 (a_0 <= C ||v||_2). By (F4), with ||B||_{C^(1,alpha)} <= |c| ||E||_{C^(1,alpha)} + ||Z||_{C^(1,alpha)},
     ||III||_2 <= C ||B||_{C^(1,alpha)} sum_k 2^(-k(1 + alpha)) sum_(m <= k + C_0) 2^m a_m <= C' ||B||_{C^(1,alpha)} sum_m 2^(-m alpha) a_m
              <= C'' ||B||_{C^(1,alpha)} ||v||_{H^(s(.) - alpha/2)},
by the Cauchy-Schwarz inequality, sum_m 2^(-m alpha) a_m <= (sum_m 2^(-m alpha))^(1/2) (sum_m 2^(-m alpha) a_m^2)^(1/2). Adding
I, II and III proves the claim. The constant-order case is the same computation with s = sigma. QED.
Remarks. (1) III is the only place where the single operator differs from the square function of Theorem Hs-pert (i): the sum
over k has no output orthogonality, and it is controlled by the Hoelder decay of the coefficient blocks (alpha > 0), not by
the H^(s(.)) norm of B. With alpha = 0 the bound of III would fail logarithmically; this is a different logarithm from the one
of V153, which is outside K_B. (2) The Hoelder norm is available for the IPM perturbation: by V156, B_norm[g] = c[g] E_0 + Z[g]
with E_0 = chi_0(t) B_0(theta) + (1, 0)/3, B_0 = (-cos 2theta, sin 2theta), and |c[g]| + ||Z[g]||_{H^(s(.))} +
||B_norm[g]||_{C_b^(1,alpha)} <= C_alpha ||g||_G for every alpha < 1/20. Hence ||K_B v||_2 <= C ||g||_G ||v||_{H^(s(.))}, and the
coefficient of the top norm is C (|c| + ||DZ||_inf) <= C ||g||_G. (3) With Lemma K the uniform estimate can be run with the
single operators A_v, A_u of Proposition Hs instead of the dyadic energy of Theorem Hs-pert (ii). This second route (a
work file of the accompanying artifacts) is CONFIRMED (V163) after one correction (V162): the change of the N_0 energy
coefficient under the perturbation is (1/2) div B - beta B_r + 4 tan(theta) B_theta (the formula of Theorem Hs-pert
(iii)); the literal formula -(1/2) div B - (1/2) B.grad log omega + d first written for it has the opposite sign and is
REFUTED (V162; a constant radial field B = (b_0, 0) on the outer end, beta = -1/2, gives b_0/2, not -b_0/2). The error
does not affect the estimate, which uses only the bound |change| <= C ||g||_G. (4) Lemma P (variable-order products,
||A_r (d f)||_2 <= C ||d||_inf ||f||_{H^(r(.))} + C (|c| + ||d_Z||_{H^(r(.))}) ||f||_inf + C |c| ||f||_2 for r(.) = s(.) and
s(.) - 1) is also a THEOREM (V161).
