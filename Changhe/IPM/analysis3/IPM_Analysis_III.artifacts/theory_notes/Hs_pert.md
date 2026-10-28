Lemma K (tame coefficient commutator for the single variable-order operator; DERIVED, submitted for checking).
Notation of Proposition Hs. C = R x S^1, s smooth with bounded derivatives and 2 < s_0 <= s(X) <= s_+, Lambda smooth
and bounded with bounded derivatives, N >= 0, A = Op(a), a(X, xi) = e^(N Lambda(X)) <xi>^(s(X)) (uniform left
quantization). Delta_m (m >= 0) is a smooth inhomogeneous Littlewood-Paley partition with sum_m Delta_m = I,
S_k = sum_(m <= k) Delta_m (S_k = 0 for k < 0), Delta~_m a fattened block (Delta~_m Delta_m = Delta_m), and
w_m(X) = e^(N Lambda(X)) 2^(m s(X)). ||v||^2_{H^(s(.))} is equivalent to sum_m ||w_m Delta_m v||^2 (dyadic norm of the
verifier's proof 123; e^(N Lambda) is bounded above and below). Let B = c E + Z, where c is a real number, E is a fixed
smooth bounded vector field with all derivatives bounded, and Z is in H^(s(.)) and in C_b^(1,alpha), 0 < alpha < 1. Put
     K_B v := sum_l [A, B_l] d_l v.
Claim. For 0 < eps <= eps_K := min(alpha/2, (s_0 - 2)/2) and v in H^(s(.)),
     ||K_B v||_2 <= C (|c| + ||DZ||_inf) ||v||_{H^(s(.))} + C (|c| + ||Z||_{H^(s(.))} + ||Z||_{C^(1,alpha)}) ||v||_{H^(s(.) - eps)},
C depending only on s, Lambda, N, E, alpha and eps. The same holds at the constant order sigma for
A_u = e^(N Lambda) <D>^sigma.
K_B does not contain the logarithmic term: A(B.grad v) = B.grad(A v) - N (B.grad Lambda) A v - (B.grad s) Op(a log<xi>) v
+ K_B v exactly (left quantization, since d_(X_l) a = a (N d_l Lambda + (d_l s) log<xi>) and d_l Lambda, d_l s depend on X
only), so the claim is consistent with V153, which REFUTES the corresponding bound for [A, B.grad].
Facts used (the kernel facts are those of the verifier's proof 156, proofs (5) to (9)).
 (F1) Moderate weights: w_m(X)/w_m(Y) <= C (1 + 2^m d(X, Y))^M, and for k >= m - C_0,
      w_m(X)/w_k(Y) <= C 2^(-(k - m) s_0) (1 + 2^m d(X, Y))^M.
 (F2) Kernel and Bernstein bounds: the kernel of A Delta~_m is bounded by C_L w_m(X) 2^(2m) (1 + 2^m d(X, Y))^(-L) (the
      xi-derivatives of a carry no logarithm), so ||A f||_2 <= C ||w_m f||_2 for f with Fourier support in the annulus of
      Delta~_m, and ||w_m d Delta_m v||_2 <= C 2^m ||w_m Delta~_m v||_2.
 (F3) Frequency localization: a is in S^(s_+)_(1,delta) for every delta > 0 (X-derivatives cost powers of log<xi>), so
      ||Delta_j A Delta_m||_(L^2 -> L^2) <= C_R 2^(-R max(j, m)) for |j - m| > C_1 and every R.
 (F4) Hoelder blocks: ||Delta_k F||_inf <= C 2^(-k(1 + alpha)) ||F||_{C^(1,alpha)} for k >= 1, ||Delta_0 F||_inf <= C ||F||_inf.
 (F5) High-coefficient paraproduct (proof 156, the two high-coefficient types, with Q_j = Delta_j): for F in H^(s(.)) and
      G in L^inf, ||sum_k Delta_k F . S_(k + C_0) G||_{H^(s(.))} <= C ||F||_{H^(s(.))} ||G||_inf (by (F1), Schur and Young's
      inequality for the sequence 2^(-n s_0), n >= -C_0; s_0 > 0 is used).
Proof. For v smooth with compact support (then by density), B_l d_l v = sum_(k,m) Delta_k B_l Delta_m d_l v and
A d_l v = sum_m A Delta_m d_l v, so K_B v = sum_l sum_(k,m) [A, Delta_k B_l] Delta_m d_l v = I + II + III with
     I   = sum_l sum_m [A, S_(m - C_0 - 1) B_l] Delta_m d_l v                     (k < m - C_0, low coefficient),
     II  = sum_l A( sum_k Delta_k B_l . S_(k + C_0) d_l v )                         (k >= m - C_0, coefficient high, A outside),
     III = - sum_l sum_k Delta_k B_l . A S_(k + C_0) d_l v                          (k >= m - C_0, coefficient high, A inside).
I. Put b_m = S_(m - C_0 - 1) B_l and F_m = [A, b_m] Delta_m d_l v. The kernel of F_m is the kernel of A Delta~_m times
(b_m(Y) - b_m(X)), and |b_m(Y) - b_m(X)| <= ||D B||_inf d(X, Y), which gains 2^(-m); with (F1), (F2) and Schur,
||F_m||_2 <= C ||DB||_inf ||w_m Delta~_m v||_2 (proof 156 (8)). Both A(b_m Delta_m d_l v) and b_m A Delta_m d_l v have their
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
Remarks. (1) III is the only place where the single operator differs from the square function of proof 156: the sum
over k has no output orthogonality, and it is controlled by the Hoelder decay of the coefficient blocks (alpha > 0), not by
the H^(s(.)) norm of B. With alpha = 0 the bound of III would fail logarithmically; this is a different logarithm from the one
of V153, which is outside K_B. (2) The Hoelder norm is available for the IPM perturbation: by V156, B_norm[g] = c[g] E_0 + Z[g]
with E_0 = chi_0(t) B_0(theta) + (1, 0)/3, B_0 = (-cos 2theta, sin 2theta), and |c[g]| + ||Z[g]||_{H^(s(.))} +
||B_norm[g]||_{C_b^(1,alpha)} <= C_alpha ||g||_G for every alpha < 1/20. Hence ||K_B v||_2 <= C ||g||_G ||v||_{H^(s(.))}, and the
coefficient of the top norm is C (|c| + ||DZ||_inf) <= C ||g||_G.

Lemma P (variable-order products; DERIVED, same facts). Let d = c d_E + d_Z with d_E smooth and bounded with bounded
derivatives and d_Z in H^(r(.)) and L^inf, where r(.) is s(.) or s(.) - 1 (so r(.) >= s_0 - 1 > 0), and let A_r be the
operator of Lemma K of order r(.). Then for f in H^(r(.)) and L^inf,
     ||A_r (d f)||_2 <= C ||d||_inf ||f||_{H^(r(.))} + C (|c| + ||d_Z||_{H^(r(.))}) ||f||_inf + C |c| ||f||_2.
Proof. d f = T_d f + (T_f d + R(d, f)); the first part has its Fourier mass in the annuli of f and is bounded by (F1), (F2)
and (F3) by C ||d||_inf ||f||_{H^(r(.))}; the second part is (F5) for d_Z (with r_- = s_0 - 1 > 0 in Young's inequality) and the
fast decay of the blocks of d_E. QED.
Applications: ||A_v(d_v v)|| <= C ||d_v||_inf ||v||_{H^(s(.))} + C_r ||v||_{H^(s(.) - eps)} for the zeroth-order coefficients of
V156, and, with r = s - 1 and f = d_l v, ||B.grad v + d v||_{H^(s(.) - 1)} <= C (||B||_inf + ||d||_inf) ||v||_{H^(s(.))} +
C_r ||v||_{H^(s(.) - eps)} (C_r bounded for ||g||_G <= r).

Proposition Hs-pert (the high estimate uniformly on a ball of transport perturbations; DERIVED, submitted for checking).
Setting. For g in the space G_s of V156 with ||g||_G <= r, let B = B_norm[g] = c[g] E_0 + Z[g] (V156 (5)) and
     S_g := S + B.grad + d[g],   d_v = beta(t) B_t (bulk, for v = h/b),   d_u = beta(t) B_t + (p'/p) B_theta (cofactor),
which are the conjugations (1/b) B.grad (b v) = B.grad v + d_v v and (1/(b p)) B.grad (b p u) = B.grad u + d_u u; an
additional zeroth-order modulation term c[g] m_0 with m_0 smooth and bounded is covered by the same proof. By V156,
B_theta = 0 on both axes, chi B_theta/cos(theta) is in H^sigma, B is in C_b^(1,alpha) for alpha < 1/20, and the explicit
smooth parts of d_v, d_u are multiples of c[g]. The maximal domain is D_s(g) := {h in X_s : (T + B.grad) h in X_s}.
Fix alpha = 1/40 and eps := min(1/32, alpha/64) = 1/2560 (V155 bounds the logarithmic form below by the H^(-alpha/64)
norm). By V154, (W~ + B).grad s >= 0 when ||B||_inf <= kappa_s/2, so r is taken with C_alpha r <= kappa_s/2.
Claim. There are r_0 > 0 and C_s' such that, with the compact operator K of Proposition Hs (the same operator),
     ||h||_{X_s} <= C_s' (||(S_g - lambda) h||_{X_s} + ||h||_{X_(s - eps)} + ||K h||_{X_s})
for every g with ||g||_G <= r_0, h in D_s(g) and 0 <= lambda <= lambda_*.
Proof. Write theta(r) for constants of the form C r (C independent of g, eta, a) and C_r for constants bounded on the ball.
Step 0 (conjugated identity of the perturbation). For v in H^(s(.)), with w = A_v v,
     A_v (B.grad v + d_v v) = B.grad w - N (B.grad Lambda) w - (B.grad s) log<D> w + G_B v,
     G_B v := K_B v - (B.grad s) (Op(a log<xi>) - log<D> A_v) v + A_v (d_v v),
exactly on test functions and, by continuity of every term from H^(s(.)) into H^(-1), for all v in H^(s(.)). The composition
log<D> Op(a) = Op(a log<xi>) + Op(r_1), with r_1 of order s(.) - 1 times a power of log<xi>, so by Lemmas K and P
     ||G_B v||_2 <= theta(r) ||v||_{H^(s(.))} + C_r ||v||_{H^(s(.) - eps)}.
Step 1 (bulk, maximal domain). Let v = h/b, so v and P_(v,g) v := (P_v + B.grad + d_v) v are in H^(s(.)) for h in D_s(g). By
V149 and V150 (the proof 148 form of the identity), A_v P_v v = W~.grad w - (W~.grad s) log<D> w + Q w + E v, Q L^2-bounded
(the scalar c - N W~.grad Lambda and the order-zero principal operator), ||E v|| <= C ||v||_{H^(s(.) - eps)}, and the quadratic
form identity -Re <Q w, w> + (1/2) <(div W~) w, w> - Re <E v, w> = <M_W R w, R w> + E'(v), |E'(v)| <= eta ||v||^2 +
C_eta ||v||_{s - eps} ||v||_s, holds on all of H^(s(.)) (V149; this part does not involve the domain). Adding Step 0,
     A_v P_(v,g) v = F + Q w + E v + (G_B v - N (B.grad Lambda) w),   F := (W~ + B).grad w - ell_g log<D> w,
with ell_g = (W~ + B).grad s >= 0 (V154) and ell_g in C_b^(1,alpha). Every term except F is in L^2, so F is in L^2.
Regularize with a Fourier-multiplier mollifier J_n, which commutes with log<D>, as in V150: [J_n, (W~ + B).grad] w -> 0 in
L^2 (Friedrichs; Lipschitz field), and [J_n, ell_g] log<D> w -> 0 in L^2 (ell_g Lipschitz, log<D> w in H^(-1)). Then
     -Re <F, w> = lim -Re <J_n F, J_n w> >= (1/2) <div(W~ + B) w, w> - C ||w||^2_{H^(-alpha/64)}
by V155 applied to J_n w before the limit. Hence, with ||div B||_inf + N ||B.grad Lambda||_inf <= theta(r),
     -Re <A_v P_(v,g) v, w> >= <M_W R w, R w> - (eta + theta(r)) ||v||^2_{H^(s(.))} - C_(eta, r) ||v||_{s - eps} ||v||_s,
where M_W = (kappa_v + N W~.grad Lambda) I - s sym DW~ = M_v + P - L_0 W~ W~^T is the matrix of (Q1) with field W~ in
Proposition Hs (the perturbation does not change it; the identity is the proof 147 form of V149, which holds on H^(s(.)) since
both sides are continuous there).
Step 2 (cofactor). The same at the constant order sigma for u = chi h/(b p) with d_u: there is no logarithmic term, Lemma K
and Lemma P hold at order sigma with the H^sigma bounds of V156 for chi Z, chi Z_theta/cos(theta) and the cofactor coefficient,
and the cutoff term (W~ + B).grad chi . v/p is supported where p is bounded below and s = sigma, with
||A_u((W~ + B).grad chi . v/p)|| <= (C_chi + theta(r)) ||v||_{H^(s(.))}.
Step 3 (penalty). The bound (Q5') of V148 is derived from the bulk and cofactor equations W~.grad v = f/b + (1 + lambda -
beta q) v - C_R h/b and their cofactor analogue. For h in D_s(g) the equations carry the extra source -(B.grad v + d_v v)
(and its cofactor analogue), and the proof of (Q5') sees a source only through ||<D>^(-1) A_v (source)||_2 <= C ||source||_{H^(s(.) - 1)}.
By the application of Lemma P at order s(.) - 1, the extra source costs theta(r) ||h||_{X_s} + C_r ||h||_{X_(s - eps)}, so
     ||W~.R w|| + ||W~.R z|| <= C_5 ||f||_{X_s} + (a + theta(r)) ||h||_{X_s} + C_(a, r) ||h||_{X_(s - eps)},   f = (S_g - lambda) h.
(This is the one input whose proof must be rerun rather than quoted: V148 is stated for h in D_H with f in X_s, while here
(S - lambda) h is only in X_(s - 1).)
Step 4 (assembly). The coupling bound (Q2) of V147 and the norm facts (Q0) of V146 do not involve the transport and hold
unchanged. Steps 1 to 4 of Proposition Hs then go through with e replaced by
     e(r) := 3 L_0 (a + theta(r))^2 + 2 eta + 2 theta + theta(r),
and C_4 does not depend on g, a, eta, theta. Choose a, eta, theta and then r_0 so that C_4 e(r_0) <= 1/2. QED.

Corollary Hs-pert (consequences; DERIVED, conditional on Proposition Hs-pert, Lemma K and Proposition H2-pert below).
(i) Uniform (H3). The proof of Proposition H3-red goes through with the same choices: the N_0 energy identity of Lemma B for
T_R + B.grad + d has the additional density [CORRECTED, V162: the sign as first written is wrong; for the physical
perturbation B.grad the change is (1/2) div_C B - beta B_t + 4 tan(theta) B_theta] (1/2) div_C B + (1/2) B.grad log omega, bounded by theta(r) because
B.grad log omega = -2 beta B_t + 8 tan(theta) B_theta and tan(theta) B_theta = sin(theta) (B_theta/cos(theta)) is bounded (V156);
the axis boundary term vanishes since B_theta = O(cos theta); the extension to D_s(g) is again a Friedrichs argument. So Lemma C
holds with c_0 - theta(r), Lemma D is unchanged, and
     ||h||_{X_s} <= C_1' ||(S_g - lambda) h||_{X_s} + ||K' h||_W,   h in D_s(g), 0 <= lambda <= lambda_*, ||g||_G <= r_0,
with C_1' and the compact operator K' independent of g.
(ii) Proposition H2-pert (resolvent for large lambda). In the dyadic norm of V129 (proof 126), w_j Delta_j (B.grad v) =
B.grad(w_j Delta_j v) - (N B.grad Lambda + j log(2) B.grad s) w_j Delta_j v + w_j sum_l [Delta_j, B_l] d_l v, and the logarithmic
density j log(2) ell_g |w_j Delta_j v|^2 is pointwise nonnegative for the total field (V154), so it is discarded exactly as in
V129 (7). The square function of the commutators is bounded by C ||g||_G ||v||_{H^(s(.))} (proof 156 (2) and (4)), and the
background part is V129. Hence Re <(S_g - lambda) h, h>_D <= -(lambda - lambda_0(r)) ||h||^2_D on D_s(g) (Friedrichs for the
maximal domain), and existence for lambda > lambda_0(r) follows by smooth approximation of B with uniform bounds and a weak
limit (B_n.grad h_n -> B.grad h in distributions). So S_g - lambda : D_s(g) -> X_s is bijective for lambda > lambda_0(r).
(iii) Index 0. Lemma H-spec with (H1) (unchanged), (ii) and (i) on [0, lambda_0(r) + 1] gives: S_g - lambda : D_s(g) -> X_s is
Fredholm of index 0 for every lambda >= 0 and ||g||_G <= r_0.
(iv) Uniform inverse under low injectivity. If S : D_s -> X_s is injective (by V152 this is the low injectivity question),
there are r_1 in (0, r_0] and C_inv with ||h||_{X_s} <= C_inv ||S_g h||_{X_s} for h in D_s(g), ||g||_G <= r_1, and S_g is
bijective. Proof: otherwise there are g_n with ||g_n||_G -> 0 and h_n in D_s(g_n), ||h_n||_{X_s} = 1, ||S_(g_n) h_n|| -> 0.
By (i), 1 <= C_1' ||S_(g_n) h_n|| + ||K' h_n||_W; a subsequence converges weakly in X_s to h, and K' h_n -> K' h, so
||K' h||_W >= 1 and h != 0. S h_n = S_(g_n) h_n - (B_n.grad + d_n) h_n -> 0 in distributions (||B_n||_inf + ||d_n||_inf
<= C ||g_n||_G -> 0, grad h_n bounded in L^2_loc), and S h_n -> S h in distributions, so S h = 0, T h = -C_R h is in X_s,
h is in D_s and h = 0, a contradiction. Bijectivity follows from (iii).
Remarks. (1) No constant is computed: r_0, r_1, C_s', C_1' and C_inv come from the qualitative constants of V146 to V150 and
from a compactness argument, so they cannot be compared with the size of the residual. (1a) In the moving-tail form the
background also moves with the dilation rate, rho_ell with ell = ell(g) and |ell - ell_0| <= C |c[g]|, so the coupling
coefficient changes by grad(rho_ell - rho_ell0). If ell -> rho_ell is Lipschitz into the coefficient space of V147, this change
is a bounded operator on X_s of norm O(|c[g]|) and is absorbed in e(r); this Lipschitz property is not proved here (OPEN).
(2) The bordered operators L_ren and
L_red (jet row, axis row and the moving-tail vector) need the same statement on B_H (+) D_s(g); the perturbation of the axis
row and of the jet column is not treated here (OPEN). (3) What a nonlinear existence argument would still need, given (iv):
the bordered version of (iv); the exact quasilinear form of the profile equation, S_g g = F + N_2(g) with N_2 free of
derivative loss (the IPM nonlinearity U[g].grad g is the transport term B_norm[g].grad g up to the modulation terms); and a
fixed point, for example g -> S_g^(-1)(F + N_2(g)) on the closed ball of radius r_1 of the high space with its weak topology
(convex, weakly compact and metrizable; weak continuity from the linearity and boundedness of g -> (c[g], Z[g]) into
C_b^(1,alpha) and Arzela-Ascoli on bounded sets), which needs C_inv ||F + N_2(g)|| <= r_1. Without computed constants this
smallness condition cannot be checked (OPEN), and low injectivity itself is OPEN.
