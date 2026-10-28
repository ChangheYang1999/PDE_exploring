# S1 closure: the conditional a posteriori existence theorem and the quantified gap

Status: FINAL (end of the run, 2026-10-28T17:48Z). A complete conditional a posteriori existence theorem is proved
for every reference profile satisfying explicit hypotheses (Theorem D); its best version needs a residual of fractional
norm at most 1/1572864 (about 6.3578e-7). It is not yet applicable. There is an explicit reference (a potential-level
tail repair of the checkpoint) for which every hypothesis except the smallness of the residual is proved, and its
residual is far too large. Exact finite rational references whose residual lies in the space (algebraic tail repairs)
also exist; nine of the ten explicit variants fail the energy-matrix hypothesis (B1), and all ten have a certified
residual size N_s(F) > 11.48, far above the threshold. No reference is known that satisfies all hypotheses. For the
checkpoint (states 88 and 131) and the early refits m4, m5, m10, m12 and m14, a necessary condition (Theorem E) shows
that no exact solution exists in the corresponding affine class of unweighted corrections at all, of any size and for
any value of the exponent. It does not apply to the tail repairs or the later exactly admissible refits, whose
residuals lie in the space; nonexistence in their affine classes is open. A second conditional
theorem (Theorem D_w, section 7a), in a weighted space that admits residuals growing like r^q with q < 1/5, applies to
the checkpoint itself: every hypothesis on the reference and the membership of its residual hold, but the smallness
hypothesis fails: its residual size exceeds its
first-version threshold (2^-35) by a factor of more than 2^119 for every weight radius R >= 2^31 (N^w_s(F) > 3.53e25 by the
exterior transfer of an annular witness; 2^128 for R >= 2^35). Its matrix hypothesis can be weakened from (19/5) I to (5/2) I on r <= R. A
second version of Theorem D_w (section 7a, smooth commutator) has threshold 2^-30 at s = 3 * 2^-21; the checkpoint
misses it by more than 2^114. Nine exactly admissible references from least-squares fitting (all forbidden residual
sectors cancelled exactly; eight with six stationary branches, one with seven) have residuals in both spaces but miss
the weighted thresholds by factors of more than 2^37 over 2^-35 and 2^32 over 2^-30 for every R >= 1 (all nine), and
for R >= 2^31 by more than 2^65 (Mpen2, d2), 2^59 (A2, A3) and 2^42 (the other five) over 2^-35; each of the nine
violates a derivative bound of (W3) at a certified point (Mpen2 and d2 off-axis; they pass at the eight points
audited first) (section 9). Necessary local tests exclude every exact solution within N^w_s-distance 2^-14 of the
checkpoint and 2^-9 of Mpen2 and d2 for every admissible s and R >= 1, and within 2^57 of the checkpoint and 2^21 of
Mpen2 and d2 for R >= 2^31, so the balls of both versions of Theorem D_w around them contain no exact solution. For
the refit d2 every hypothesis on the reference of the parametric logarithmic theorem (section 11 (vii)) is proved,
with Astar = 2^189 and tau = 2^-210, and its residual lies in the space; only the smallness of the residual fails,
by a factor of more than 2^243 (P95, P91, P105). For
each fixed radial degree of the six-branch family the weighted residual norm has a positive lower bound uniform in s
and R (section 11), which is not evaluated. For Theorem D a uniform bound
holds over the whole generator family of these fits: no choice of coefficients brings N_s(F) within a factor of 22986
of the threshold, and with any radial degree up to 3675 in place of 75 N_s(F) still exceeds it (section 11). This file states the theorems, every hypothesis they use, which hypotheses are proved for
which reference, and the size of the remaining gap.

Labels. THEOREM: proof checked by an independent verification, with independent recomputation of every certified number.
PROPOSED: a complete written argument exists but its independent check is not finished; never used as a proved
conclusion. OPEN: no complete argument. FLOAT: a floating-point observation, never a bound.

## 1. Setting

- Unknowns: a density rho(X), X = (x, y) in R^2, even in x and odd in y (the parity class), and the far-field strain
  coefficient c_l > 0. The profile equation is
  F(rho; c_l) = (c_l X + U[rho]).grad rho - rho = 0,
  U[rho] = (-psi_y, psi_x), -Delta psi = d_x rho, with the canonical inverse (psi odd in x and y, psi = o(r^2));
  equivalently U[h] = (-R_1 R_2 h, R_1^2 h) with the Riesz transforms R_j = d_j (-Delta)^(-1/2).
- Strain functional: for h in C^(1,a) near 0 with sublinear growth,
  c[h] = d_y U_2[h](0) = -h_y(0)/4 + (1/pi) PV int sin(3 theta) h(X) r^-3 dX (THEOREM).
- Fixed-c formulation. Fix c_l and a reference density rho_tilde. Write Ubar = U[rho_tilde], V = c_l X + Ubar,
  R_tilde = F(rho_tilde; c_l) and rho = rho_tilde + h. Then F(rho; c_l) = 0 is equivalent to
  L h + U[h].grad h = -R_tilde,  L h = V.grad h - h + U[h].grad rho_tilde.
- Automatic normalization (THEOREM): every solution rho of F(rho; c_l) = 0 in the parity class that is C^1 near 0 with
  Hoelder remainders, with U[rho] differentiable at 0 and d_y rho(0) != 0, satisfies c_l + c[rho] = 1. No strain unknown
  or rank-one correction is needed. (Normalization alone does not remove scaling; see the next items.)
- Center identity (THEOREM): for C^1 functions k, h in the classes below and f = (L + U[k].grad) h,
  f_y(0) = (c_l + c[rho_tilde] - 1 + c[k]) h_y(0) + a_0 c[h], a_0 = d_y rho_tilde(0).
- Scaling rho -> t rho(X/t) maps solutions to solutions and changes a leading far-field profile r^gamma Theta_0 into
  t^(1 - gamma) r^gamma Theta_0. The correction spaces E_2, X and N_s consist of continuous functions tending to 0 at
  infinity (their first derivatives also tend to 0 for X and N_s); the negative-order space H alone does not have this
  property. So if the reference has a nonzero leading profile r^gamma Theta_0, gamma = 1/c_l (hypothesis (B11) below),
  a correction in E_2, X or N_s fixes gamma and Theta_0 and is transverse to the scaling direction. No additional scalar
  phase equation is imposed: the fixed leading profile and the correction class (corrections square-integrable in N_s and of order at most r^(1/5), below the leading order r^gamma, in N^w_s) remove scaling.

## 2. Spaces

Let C be the space of smooth compactly supported functions in the parity class. All spaces are completions of C.
H denotes the homogeneous Hdot^-1 completion, ||h||_H = ||(-Delta)^(-1/2) h||_2. Tensors D^j h carry the Frobenius
norm of all ordered derivatives. Put omega(X) = (1 + 4 r^2)^(2/5), r = |X|.

    E_0(h)^2 = ||h||_2^2 + (20/21) ||h||_H^2,
    E_1(h)^2 = ||grad h||_2^2 + 16 E_0(h)^2,
    E_2(h)^2 = ||omega D^2 h||_2^2 + 2^14 E_1(h)^2,
    E_3(h)^2 = ||omega D^3 h||_2^2 + 2^173 E_2(h)^2,
    X = [E_2, E_3]_(1/32)  (complex interpolation),
    N_s(h) = E_2(J^s h),  J = (1 - Delta)^(1/2),  0 < s <= 1/2.

For vector fields the squares of the component norms are summed. Facts (THEOREM): N_s embeds with norm 1 in H^(2+s);
||grad h||_inf and ||DU[h]||_inf are at most c_s N_s(h) with c_s = [2 (pi s (1 + s))^(1/2)]^-1; ||h||_H <= N_s(h);
||h||_(C^(1/2)) <= N_s(h) (supremum plus seminorm); the ball {N_s(h) <= r, c[h] = 0} is complete in the H metric.

Residual conversion (THEOREM). If E = E_2(f) and Q = ||omega D^3 f||_2 are finite and 0 < s <= 1/2, then

    N_s(f) <= E^(1 - s) (2 Q^2 + 16410 E^2)^(s/2) + 34 s E.

In particular E_3 membership implies N_s membership, and for s = 2^-28 certified upper bounds for E and Q give a
certified upper bound for N_s(f) without evaluating a fractional operator. The four components of E_2 form one square
sum and must be bounded together, including the Hdot^-1 component.

Reverse comparison (THEOREM). For 0 < s < 1/34, N_s(f) >= (1 - 34 s) E_2(f) (S1_PROOFS.md, P8.1, (27)); any partial
square sum of the components of E_2 may replace E_2 on the right. At s = 2^-18 the factor is 0.99987030029296875.

## 3. Hypotheses on the reference (c_l, rho_tilde)

Notation: A = [[rho_tilde_y, -rho_tilde_x/2], [-rho_tilde_x/2, 0]],
N = (1/2) [[rho_tilde_yyy, -rho_tilde_xyy], [-rho_tilde_xyy, rho_tilde_xxy]], v = omega^2,
S = (v_xy rho_tilde_x - v_xx rho_tilde_y - v_x rho_tilde_xy + v_y rho_tilde_xx)/2, <r> = (1 + r^2)^(1/2).
Matrix inequalities hold pointwise on R^2 in the sense of symmetric matrices. Tensor bounds are Frobenius suprema except
in (B9), where ||T||_S is the sum over ordered indices I of ||T_I||_inf. (A Frobenius bound gives the component sum only
with the factor equal to the number of components, not its square root, because the component maxima may occur at
different points.)

- (B0) Structure. 9/5 < c_l < 37/20. rho_tilde is smooth, in the parity class, of sublinear growth, with canonical
  velocity Ubar; a_0 = d_y rho_tilde(0) > 0; the functions D rho_tilde, <r> D^2 rho_tilde, <r>^2 D^3 rho_tilde,
  <r>^2 D^4 rho_tilde, D Ubar, <r> D^2 Ubar and <r> D^3 Ubar are bounded.
- (B0n) Normalization. c_l + c[rho_tilde] = 1.
- (B1) M = (2 c_l + 1) I + sym D Ubar + A >= (19/5) I.
- (B2) A >= -(1/20) I.
- (B3) N <= I.
- (B4) M_1 = I - sym D Ubar + A >= (9/10) I.
- (B5) M_2 = (1 + c_l + V.grad log omega) I - 2 sym DV + A >= (1/2) I.
- (B6) M_3 = (1 + c_l + V.grad log omega) I - 3 sym DV + A >= -(5/4) I.
- (B7) ||D^2 rho_tilde||_inf <= 3, ||omega D^2 rho_tilde||_inf <= 8, ||omega D^3 rho_tilde||_inf <= 10,
  ||omega D^2 Ubar||_inf <= 3, ||D(v grad rho_tilde)/omega||_inf <= 28, ||S||_inf <= 40.
- (B8) ||D^2 Ubar||_inf <= 35, ||D^2 rho_tilde||_inf <= 77, ||<r> D^3 Ubar||_inf <= 2^14,
  ||<r> D^3 rho_tilde||_inf <= 2^14, ||<r>^2 D^4 rho_tilde||_inf <= 2^84.
- (B9) M* = |c_l| + ||D Ubar||_S + ||omega D^2 Ubar||_S + ||omega D^3 Ubar||_S + ||D rho_tilde||_S
        + sum_(j=2..4) ||omega D^j rho_tilde||_S <= 4096.
- (B9c) Component form of (B9): |c_l| <= 2, ||D Ubar||_S <= 6, ||omega D^2 Ubar||_S <= 24, ||omega D^3 Ubar||_S <= 160,
  ||D rho_tilde||_S <= 22, ||omega D^2 rho_tilde||_S <= 32, ||omega D^3 rho_tilde||_S <= 80,
  ||omega D^4 rho_tilde||_S <= 2048. (It implies (B9) with M* <= 2374.)
- (B10m) Membership: R_tilde = F(rho_tilde; c_l) lies in the N_s space (for instance R_tilde in the E_3 completion).
- (B10s) Smallness: N_s(R_tilde) <= eta, where (s, eta) = (2^-28, 2^-27/20 = 3.7252902984619140625e-10) for Theorem D(a) and
  (s, eta) = (2^-18, 2^-16/24 = 1/1572864 = 6.3578287760416...e-7) for Theorem D(b).
  (B10) denotes (B10m) and (B10s) together.
- (B11) Leading profile (used only for the statements about Theta_0 and scaling). rho_tilde - r^gamma Theta_0(theta)
  tends to 0 relative to r^gamma, uniformly in theta, for some nonzero Theta_0.

Reference independence (THEOREM; S1_PROOFS.md, P8.2). The proofs of the Route U theory (Theorem A), of Theorem C and
of Theorem D use the reference only through these hypotheses and exact identities of the operator; no finite-potential
representation enters. This does not extend to the weighted alternative realization of section 9 (S1_PROOFS.md, P6.11),
which is proved for the checkpoint only. Precisely: (B0) to (B5) and (B7) give the E_0, E_1, E_2 theory;
adding (B6) and (B8) gives the E_3 and X theory (the auxiliary third-level estimate uses the (B7) constants 28 and 40
directly); (B0n) is needed for the normalized range statements; the low theory uses (B1) for its numerical constant and
(B0) for its realization; Theorem C and Theorem D(a) use in addition (B9), the sharper rate in
Theorem C and Theorem D(b) use (B9c), and Theorem D uses (B10m) and (B10s). The hypotheses do not transfer from one reference to
another: each new reference needs its own certificates.

Status for the checkpoint state 131 (the latest accepted state of the case 4 run, reconstructed exactly as a finite
potential with rational coefficients): (B0) to (B9), (B9c) and (B11) are THEOREMS, by exact identities and exact
compactified Bernstein certificates with independent 384-bit recomputation (S1_NUMERICAL_CERTIFICATES.md). The
component sums of (B9c) come from the Frobenius bounds of (B7) and omega |D^3 Ubar|_F <= 10, omega |D^4 rho_tilde|_F <=
128 (certified), multiplied by the number of ordered components
(8 for D^2 Ubar, 16 for D^3 Ubar, 4, 8 and 16 for D^2, D^3 and D^4 rho_tilde) and from sum sup |D_j Ubar_i| <= 6 and
sup |rho_x|, sup |rho_y| <= 11; their total is M* <= 2374. (B10m) is false: the residual of state 131 contains a
non-stationary far-field sector of exponent 2 gamma - 1 = 0.1048 and is not in L^2 or in H.

Status for the tail repair of state 131 (THEOREM). Let chi_0 be the exact potential of state 131 (rho = -d_y Delta chi,
stream function d_xy chi) and chi_inf = sum_(n=1..6) r^(p_n + 3) C_n(theta) the exact homogeneous potentials of the six
stationary far-field sectors (finite even cosine polynomials C_n, obtained by an exact triangular inversion; C_1 is the
original leading potential). With a fixed smooth radial cutoff eta_R (0 for r <= R, 1 for r >= 2R), put
chi_R = chi_0 + eta_R (chi_inf - chi_0) and rho_R = -d_y Delta chi_R. Then rho_R and its canonical velocity coincide with
those of state 131 on r < R (so every center jet, a_0, c[rho_R] and (B0n) are preserved), and on r > 2R they are exactly
the six stationary homogeneous sums, so the residual has symbol order p_7 < -2 there and F(rho_R) lies in E_3 and in
N_s. For R = 2^1024 every hypothesis (B0) to (B9), (B9c), (B10m) and (B11) holds: on r >= R all fields obey
|D^j rho_R|_F + |D^j u_R|_F <= 2^206 r^(gamma - j), j <= 7, which gives the weighted tensor bounds of (B7) to (B9) at
most 3/1024 there (7/1024 for D(v grad rho_tilde)/omega, 24/1024 for S), M >= (19/5) I,
M_1 >= (9/10) I, M_2 >= (4082593/6579200) I and M_3 >= -(1011919/822400) I on the exterior,
while the original certificates apply on the unchanged interior; hence (B9c) and M* <= 2374 hold globally. (B10s) fails
quantitatively: the residual of rho_R equals that of state 131 on r < R, whose leading sector has angular L^2 norm at
least r^(p_2)/16 on R/2 <= r <= R, so ||F(rho_R)||_2 >= R/32 and N_s(F(rho_R)) >= 512 ||F(rho_R)||_2 >= 2^1028 for every
s. More generally ||F(rho_R)||_2 grows like R^(p_2 + 1) for this splice,
because the checkpoint residual itself grows. This removes membership and coefficient compatibility as obstacles of
principle; what remains is smallness, (B10s), achieved simultaneously with the coefficient hypotheses.

For the early exact refits m4, m5, m10, m12 and m14 (finite potentials with exactly stationary first far-field
sector), (B0n) and (B11) hold by construction and (B1) is certified for m5; the other hypotheses are not certified, and
their residuals are not in the space (section 9). The later exactly admissible refits have residuals in the space; for
d2 every reference hypothesis of the parametric logarithmic theorem holds and only residual smallness fails (sections 9
and 11).

Status for the algebraic tail repairs (THEOREM; S1_PROOFS.md, P14). Let chi_old be the exact potential of state 131 or of
the refit m10, written in the canonical generators G_(j,m,k) = r^(2k)(1 + r^2)^(a_j - k) cos(2m theta),
a_j = (3 + gamma - j(1 - gamma))/2, k >= m, and let L_(j,m) = sum_k a_(j,m,k) and D_(j,m) = sum_k (a_j - k) a_(j,m,k) be
its leading and first-descendant potential moments in branch j and mode m. Fix an integer K >= 3 and put k = m + K. For
j = 2, ..., 5 add A G_(j,m,k) with A = C_(j+1)(m) - L_(j,m); for j = 0, 1 add alpha G_(j,m,k) + beta G_(j,m,k+1) with
beta = (a_j - k) A + D_(j,m) and alpha = A - beta, which solves alpha + beta = A and
(a_j - k) alpha + (a_j - k - 1) beta = -D_(j,m) (determinant -1). The result chi_new is a finite rational combination of
canonical generators. Every Taylor coefficient of the potential of degree below 2K is unchanged, so a_0, c[rho] and (B0n) hold exactly.
The leading potential of branch j is exactly the stationary C_(j+1), j = 0, ..., 5, and the first descendants of branches
0 and 1 vanish. Consequently all eight residual sectors of exponent >= -2 vanish (section 10), the first nonzero sector is
r^(p_7) with full-circle angular L^2 norm in [3081.27440111579, 3081.27440111580], |D^d F| <= C_d r^(p_7 - d) for
r >= 2, and F(rho_new) lies in E_3 and in N_s for 0 < s <= 1/2: (B10m) holds. Ten variants (bases state 131 and m10,
K = 4, 8, 16, 256, 4096) are constructed and independently audited in exact arithmetic. They show that membership is achievable within finite
rational potentials of the canonical form, without a cutoff function. They are not usable references (THEOREM;
S1_PROOFS.md, P14): two independent 640-bit evaluators (Cartesian potential jets and polar differentiation) agree at
eight rational points for each of four variants, and at X = (1, 1) the least eigenvalue of M lies in
[-395.204, -395.203] (state 131, K = 4), [-315.676, -315.675] (m10, K = 4), [-167.090, -167.089] (state 131, K = 16)
and [-9.156, -9.155] (m10, K = 16), so (B1) fails; with ||f||_inf <= N_s(f) the residual point values give
N_s(F) >= 4564, 11919, 2386 and 289 respectively, for every 0 < s <= 1/2. A scan of all ten variants on a 73 x 65 polar grid, with every minimizing
point re-evaluated by both evaluators (THEOREM for the point values; S1_PROOFS.md, P14), certifies a negative
eigenvalue of M for every variant with K <= 256, and least eigenvalue below 3.417 < 19/5 at r = 2^4.75, theta = 0 for
state 131 with K = 4096, so (B1) fails for nine variants. The residual values at the same points give N_s(F) > 9281,
13448, 7618, 4575, 4825, 1305, 605 and 208 for state 131 and m10 with K = 4, 8, 16 and 256. For m10 with K = 4096 no sampled point fails (no positivity
proof), and the certified point value |F(30, 40)| > 11.48 gives N_s(F) > 11.48 (state 131, K = 4096: > 25.44). For m10
with K = 8 the whole-plane Hessian residual is ||omega D^2 F||_2 in [863401.8215612798, 863401.8215612799] (THEOREM;
1024-bit ball arithmetic), so E_2(F) > 8.6e5. Certified whole-plane norms of all residual components of the m10
variants with K = 8 and 16 (S1_PROOFS.md, P14.2 section 5) give, with the residual conversion, the reverse comparison
and ||F||_Hdot^-1 <= ||r F||_2, 7344656 < N_s(F) < 19372856 and 3600047 < N_s(F) < 16301199 at s = 2^-18 (THEOREM). These are statements about these explicit variants only, not about all
tail repairs.

## 4. Theorem A: the fixed-background inverse (THEOREM)

Assume (B0) to (B8). On the respective generator domains:

1. L is bijective on E_0, E_1, E_2 with semigroup decay rates 11/4, 1/2 and 1/10, inverse bounds 4/11, 2 and 10. The
   E_2 statement contains the inequality -Re <L h, h>_(E_2) >= (1/10) E_2(h)^2 on the generator domain.
2. The E_3 semigroup grows at most like exp(3t/2). On X the semigroup decays like exp(-t/20), and L is bijective from
   its generator domain onto X with ||L^-1||_(X -> X) <= 20.
3. ||grad h||_inf, ||DU[h]||_inf <= 2 ||h||_X; [grad h]_(C^(1/64)), [DU[h]]_(C^(1/64)) <= 5 ||h||_X; with alpha = 1/64
   and M_loc(h) = [int_(r<1) r^-260 |h - h_y(0) y|^256 dX]^(1/256),
   ||h||_H + ||h||_(C^alpha) + M_loc(h) + |c[h]| <= 240 ||L h||_X.
4. Under (B0n), for h in the generator domain in X, f = L h satisfies f_y(0) = a_0 c[h], so L^-1 maps
   {f in X : f_y(0) = 0} bijectively onto {c[h] = 0}. (The point value f_y(0) is a continuous functional on X and on
   N_s with s > 0, not on E_0, E_1 or E_2, so the statement is made only there.) Without (B0n) the identity carries the
   extra term (c_l + c[rho_tilde] - 1) h_y(0).
5. Low level under a frozen velocity: if W is a C^1, globally Lipschitz, divergence-free parity field with W(0) = 0 and
   d = ||sym DW||_inf < 19/5, then L + W.grad is bijective on H with ||(L + W.grad)^-1||_(H -> H) <= 1/(19/5 - d).
   Bilinear bound: ||U[z].grad g||_H <= ||z||_H ||grad g||_inf.
6. Weighted Riesz bound (a property of U alone): for |beta| < a, on L^2(r^(2 beta)) the Beurling transform has norm
   (a + |beta|)/(a - |beta|), a = 1 in general and a = 2 on centrally odd functions (the formula is restricted to
   |beta| < a). For the weight omega,
   ||omega U[f]||_2 <= (9/5) ||omega f||_2 for centrally odd f and <= (16/3) ||omega f||_2 in general (some energy
   proofs use the weaker earlier constant 256, which is also valid).

## 5. Theorem B: the two-norm fixed-point theorem (THEOREM, abstract)

Let X_H embed continuously and injectively in X_L, let B be a ball {k : ||k||_H <= r} (possibly intersected with a
closed affine constraint) that is complete in the X_L metric, and let Y_H embed in Y_L. Assume, for k, k_1, k_2 in B:

- (H1) A_k g = -R has a unique solution g = T(k) in X_H with ||g||_H <= K_H ||R||_(Y_H), and T(k) satisfies the
  constraint;
- (H2) ||g||_L <= K_L ||A_k g||_(Y_L) for differences g of elements of X_H;
- (H3) A_(k_1) - A_(k_2) = C(k_1 - k_2, .) with ||C(k_1 - k_2, g)||_(Y_L) <= C_B ||k_1 - k_2||_L ||g||_H.

Put eta = ||R||_(Y_H) and m = K_H eta. If m <= r and q = K_L C_B m < 1, then T has a unique fixed point h in B; it
solves A_h h = -R, satisfies ||h||_H <= m, and for any h_0 in B the iterates h_(n+1) = T(h_n) obey
||h_n - h||_L <= q^n ||h_1 - h_0||_L/(1 - q). If 0 is in B (as for the constraint c[k] = 0 used below) one may take
h_0 = 0. The proof is the contraction mapping principle for T on B with the X_L metric.

Application: A_k g = (V + U[k]).grad g - g + U[g].grad rho_tilde and C(z, g) = U[z].grad g, so h = T(h) solves
F(rho_tilde + h; c_l) = 0.

## 6. Theorem C: high solvability under a rough frozen velocity (THEOREM)

Let the reference satisfy (B0) and (B0n) (smooth sublinear parity reference with canonical velocity, bounded first
derivatives, a_0 != 0, exact center normalization) and the conclusions of Theorem A item 1 (E_2 decay 1/10) and item 5
(low decay 19/5) for the consistent transport realizations, for instance through (B1) to (B5) and (B7), and let M* be
finite. Let 0 < s <= 1/2, let k be real, in the parity class,
with N_s(k) finite, and W = U[k]. The maximal distributional realization of A_k = L + W.grad in the N_s space generates a
strongly continuous semigroup with

    ||exp(t A_k)||_(N_s -> N_s) <= exp[-t beta],  beta = 1/10 - 1024 s M* - 128 N_s(k)/s^(1/2).

If beta > 0, A_k is bijective from its domain onto the N_s space with ||A_k^-1|| <= 1/beta, and if moreover c[k] = 0,
A_k^-1 maps the forcing hyperplane {f_y(0) = 0} onto the solution hyperplane {c[h] = 0}.

Sharper rate. If in addition (B9c) holds and 0 < s <= 1/1024, the same conclusions hold with

    beta = 1/10 - 4800 s - 5 N_s(k)/s^(1/2).

(Proof: keep the four components e = (P, 128 a, 512 b, 512 (20/21)^(1/2) H) of E_2, with P = ||omega D^2 h||_2,
a = ||grad h||_2, b = ||h||_2, H = ||h||_H, separate. Each background coefficient then acts only at its own derivative
level; the commutator energy is bounded by s e^T K e with an explicit upper triangular 4 x 4 matrix K whose symmetric
part has row sums 19053/4, 17925/4, 4324 and 240 under (B9c), all below 4800. The rough transport cost, kept per
component, is at most (n/s^(1/2)) [A_s x^2 + B_s x + (13/10)(1 - x^2)] E^2 with x = P/E in [0, 1], n = N_s(k),
A_s = 127/50 + (653/5) s and B_s = (9/5)(1 + 44 s); this is increasing in x, with maximum 217/50 + (1049/5) s < 5.)

Structure of the proof (complete proof in S1_PROOFS.md):
- Kernel: J^s f = f + int kappa_s(z) (f(x) - f(x - z)) dz with
  kappa_s(z) = s/(2 Gamma(1 - s/2)) int_0^inf e^-t (4 pi t)^-1 e^(-|z|^2/(4t)) t^(-1 - s/2) dt and
  int |z|^2 kappa_s = 2s; with m(z) = (1 + 2|z|)^(4/5) >= omega(x)/omega(x - z),
  int |z| m kappa_s <= 17 s and int |z|^2 m |D kappa_s| <= 54 s.
- Background: [J^s, X.grad] J^-s = s (I - J^-2); a Taylor expansion of the coefficient gives
  ||omega [J^s, d.grad] J^-s h||_2 <= s (28 ||Dd||_S + 132 ||D^2 d||_S) ||omega h||_2; the divergence form
  T g = div([J^s, u] g) handles the Hdot^-1 component. With full ordered-derivative bookkeeping,
  ||[J^s, L] J^-s h||_(E_2) <= 1024 s M* E_2(h).
- Rough transport: a weighted Kato-Ponce type bound for [J^s, W.grad], the product bound
  ||omega J^s(v f)||_2 <= (1 + 44 s) s^(-1/2) ||v||_(H^(1+s)) ||omega J^s f||_2 and Theorem A item 6 for the top term give
  |Re (J^s(W.grad g), J^s g)_(E_2)| <= 128 N_s(k) N_s(g)^2/s^(1/2). No third derivative of W is used.
- Realization: mollify k, use bounded-perturbation semigroups for smooth k_n, prove convergence in C_t L^2 with uniform
  N_s bounds, identify the limit generator with the maximal distributional operator, and obtain the inverse as
  -int_0^inf exp(t A_k) dt.

## 7. Theorem D: conditional a posteriori existence (THEOREM)

Assume (B0), (B0n), (B1) to (B5) and (B7) for (c_l, rho_tilde), and one of

    (a) (B9), (B10m) and (B10s) with s = 2^-28, r = 2^-27, eta = r/20 = 2^-27/20 = 3.7252902984619140625e-10;
    (b) (B9c), (B10m) and (B10s) with s = 2^-18, r = 2^-16, eta = r/24 = 1/1572864 = 6.3578287760416...e-7.

Then there is exactly one h with

    N_s(h) <= r,  c[h] = 0,  F(rho_tilde + h; c_l) = 0.

Moreover:
1. h is in H^(2+s), hence C^1, U[h] is C^1, and the equation holds pointwise. ||grad h||_inf and ||DU[h]||_inf are at
   most d = c_s r, with d < 2^-13 in case (a) and d < 1/400 (d = 0.0022039...) in case (b). d_y(rho_tilde + h)(0) > 0 and c_l + c[rho_tilde + h] = 1. (For every admissible reference,
   parity and (B0n) give D Ubar(0) = diag(c_l - 1, 1 - c_l), A(0) = diag(a_0, 0), M_1(0) = diag(2 - c_l + a_0, c_l), so
   (B4) gives a_0 >= c_l - 11/10 > 7/10, and |h_y(0)| <= d < 7/10 keeps the slope positive.)
2. h is in L^2 and H, and h, grad h tend to 0 at infinity. Under (B11), rho_tilde + h has the exponent gamma = 1/c_l and
   the leading angular profile Theta_0 of rho_tilde, and the solution is not a rescaling of another solution in the same
   class.
3. Direct Hoelder, moment and strain control: with delta = s/2, p = 4/delta, kappa = p + 4 and
   M_loc(h) = [int_(r<1) r^-kappa |h - h_y(0) y|^p dX]^(1/p),
   ||h||_H + ||h||_(C^(1/2)) + M_loc(h) + |c[h]| <= (2 + 3 s^(-1/2)) N_s(h) <= (2 + 3 s^(-1/2)) K_H N_s(R_tilde),
   that is at most 2^16 * 20 N_s(R_tilde) in case (a) (p = 2^31) and 2^11 * 24 N_s(R_tilde) in case (b) (p = 2^21).
4. The Picard iterates h_0 = 0, h_(n+1) = -A_(h_n)^-1 R_tilde converge to h in H with ratio below 2^-13 in case (a)
   and below 1/1000 in case (b).

Proof. Case (a): by Theorem C with N_s(k) <= r, the background loss is at most 2^22 s = 1/64 and the rough loss is
128 r/s^(1/2) = 1/64, so beta >= 11/160 > 1/20 and K_H <= 20. Case (b): by the sharper rate,
beta >= 1/10 - 4800/2^18 - 5/128 = 873/20480 > 1/24, so K_H <= 24. In both cases K_H eta = r. (B0n) and the center identity give R_tilde_y(0) = 0 and
c[T(k)] = 0 whenever c[k] = 0. By Theorem A item 5 with ||sym DU[k]||_inf <= d,
K_L <= (19/5 - d)^-1 < 1, and C_B = c_s by the bilinear bound and ||grad g||_inf <= c_s N_s(g). Then
m = K_H N_s(R_tilde) <= r and q = K_L c_s m <= d/(19/5 - d), below 2^-13 in case (a) and below 1/1000 in case (b), and
Theorem B applies on B = {N_s(k) <= r, c[k] = 0} with
the H metric. Conversely every solution in B is a fixed point, which gives uniqueness. The remaining statements follow
from the embeddings of section 2 and the automatic normalization of section 1. The scalar constants were recomputed in
rational and 384-bit arithmetic. (An external referee of the case (a) proof confirmed every constant and asked for one
step to be written out: the construction of the low-space semigroup on H and its agreement with the L^2 realization on
H cap L^2, which is what allows K_L to be applied to differences T(k) - T(l). That step is now part of the verified proof
(S1_PROOFS.md, P8, section 5): the low semigroup is the extension by density of the high semigroup to H, the density is
simultaneous in H and L^2, and the L^2 Duhamel identity places every contraction difference in the low generator
domain, without assuming that an arbitrary H solution lies in L^2. The constants of both cases are unchanged.)

Remarks.
- Optimizing s and the radius (elementary arithmetic from Theorems B and C). With mu = 1/10 - C_bg s and
  C_W = c_U/s^(1/2), the condition K_H(r) eta <= r with K_H(r) = 1/(mu - C_W r) is satisfiable exactly when
  eta <= mu^2/(4 C_W), at r = mu/(2 C_W); this is largest at s = (1/10)/(5 C_bg). With the constants of case (b)
  (C_bg = 4800, c_U = 5) the optimum is s = 1/240000, r = s^(1/2)/125, eta = s^(1/2)/3125 = 6.5319726...e-7 (THEOREM,
  recomputed in 384-bit arithmetic), only 3 percent above case (b). With the constants of case (a) it gives 8.6e-10
  (M* <= 4096) or 1.1e-9 (M* <= 2374).
- An unnormalized reference (c_l + c[rho_tilde] != 1) would require dropping the constraint c[k] = 0 and redoing the
  center bookkeeping; not used (OPEN in that form).

## 7a. Theorem D_w: conditional existence in a weighted space (THEOREM)

This is a second conditional theorem, proved independently of (B1) to (B10m), in a space whose weights admit slowly
growing residuals. Its proof (weighted fractional energy, a rough weighted inverse without a third derivative of the
rough velocity, direct weighted negative-order commutators, and the nonlinear closure) is part P17 of S1_PROOFS.md,
with the weighted derivative estimates P6.12 to P6.16; the smaller radius below is part P18.

Weights and norms. <r> = (1 + r^2)^(1/2), R = 2^35, w = (1 + r^2/R^2)^(-11/10), omega_1 = <r>^(-1/5),
omega_2 = (1 + 4 r^2)^(2/5), P_1(g) = ||omega_1 D g||_2, P_2(g) = ||omega_2 D^2 g||_2, L(g) = ||w g||_Hdot^-1,
E^w(g)^2 = P_2(g)^2 + 2^22 P_1(g)^2 + 2^53 L(g)^2, N^w_s(g) = E^w(J^s g), J = (1 - Delta)^(1/2). The space is the
completion of the compactly supported smooth functions of the parity class (even in x, odd in y).

Hypotheses on the reference rho (all pointwise and global; Euclidean norms of the ordered derivative tensors;
V = cX + u, u = U[rho] canonical, A = [[rho_y, -rho_x/2], [-rho_x/2, 0]]):
(W0) rho smooth, even in x, odd in y, sublinear, with canonical sublinear velocity; 9/5 < c < 37/20;
     a_0 = d_y rho(0) >= 1.
(Wn) c + c[rho] = 1 exactly (with the local term of the strain formula).
(W1) M = (2c + 1) I + sym Du + A >= (19/5) I, and with the decay exponent d = 2/5: sup r^d (|D rho| + r |D^2 rho|)
     <= 152, sup r^(d - 1) |u| <= 18, sup r^d |Du| <= 18, sup r^(1 + d) |D^2 u| <= 45 (d is not delta = 1 - gamma).
(W2) M_k = (1 + c + V.D log omega_k) I - k sym DV + A >= I/2 for k = 1, 2 (weighted principal matrices; for k = 1 this
     is not the unweighted first-derivative matrix).
(W3) |Du| <= 14/5, |D rho| <= 16, <r>|D^2 u| <= 3, <r>|D^3 u| <= 16, |D^2 rho| <= 3, <r>|D^2 rho| <= 8,
     <r>^2 |D^3 rho| <= 32, <r>^2 |D^4 rho| <= 512.
(Wm) F(rho; c) belongs to N^w_s.  (Ws) N^w_s(F(rho; c)) <= eta: 2^-46 at s = 2^-30 with the constants below, or 2^-35
     at s = 3 * 2^-31 with the sharper constants at the end of this section.
(Wt) (for the tail and scaling conclusions only) r^(-gamma) rho -> Theta_0 != 0 uniformly, gamma = 1/c.
(W0)-(W3) imply the low semigroup decay 1/5 (proved margin above 0.2288 at R = 2^35) and the E^w decay 1/20, with
their generator realizations and inverses; these are conclusions, not further hypotheses. Of the list (B0)-(B11) of
section 3, (B1) and (B5) are used directly; (B2), (B3), (B6), (B9) and (B9c) are not needed, and (B4) does not replace
(W2). No finite-potential representation is used once (W0)-(Ws) are verified. For state 131 every condition except
(Ws) is certified.

Conclusion. For 0 < s <= 2^-12 and every k with N^w_s(k) finite, the maximal realization of A_k = L_fix + U[k].grad
generates a semigroup on N^w_s with ||exp(t A_k)|| <= exp[-t (1/20 - 2^23 s - 2^19 N^w_s(k)/s^(1/2))]; when the rate
is positive A_k is bijective with inverse bounded by the reciprocal rate. Let s = 2^-30, r_0 = 2^-41,
eta = 2^-46 (= 1.4210854715...e-14). If F(rho; c) belongs to N^w_s and N^w_s(F(rho; c)) <= eta, there is exactly one h
with N^w_s(h) <= r_0 and c[h] = 0 such that F(rho + h; c) = 0. On the ball the high rate is at least 11/320 > 1/32
(inverse at most 32), the low inverse is at most 6 and the contraction factor in the low metric is 3/1024. The low
norm L(h), an adapted Hoelder norm, the center moment and |c[h]| are together at most 2^23 s^(-3/2) N^w_s(F) = 2^68
N^w_s(F). Since |h(X)| <= 2^13 max(1, r)^(1/5) N^w_s(h) and gamma > 1/5, rho + h has the leading profile of rho.

Status for state 131. Every hypothesis on the reference holds. The residual belongs to N^w_s: |D^j F| <= C_j
<r>^(q - j) with q = 2 gamma - 1 = 0.1048 < 1/5, so the obstruction of Theorem E (which concerns N_s) does not apply.
But the residual is large in N^w_s (THEOREM, annular duality). The low component 2^(53/2) L amplifies a far-field
sector r^q E(theta), -2 < q < 1/5, by a factor of order 2^(53/2) R^(q+2) (the Hdot^-1 norm of a profile of size T^q on
the annulus r ~ T is of order T^(q+2) in two dimensions). Rigorously: L(J^-s g) <= 6 L(g) (0 < s <= 2^-12) gives
N^w_s(F) >= 2^(53/2) L(J^s F) >= (2^(53/2)/6) L(F), and L(F) >= <w F, phi>/||D phi||_2 for every phi in Hdot^1. Take
  phi = chi(r/R) sum_(m = 1, 3, ..., 39) (e_m/d_m) sin(m theta),  chi(t) = (t - 1)^2 (2 - t)^2 on [1, 2], 0 elsewhere,
  d_m = 1/35 + m^2/630,
where e_m are the exact sin(m theta) coefficients of the leading residual sector r^q E_1. This phi is C^1, compactly
supported in R <= r <= 2R, even in x and odd in y; int chi = 1/30, int chi^2 = 1/630, int t chi'(t)^2 dt = 1/35, so
||D phi||_2^2 <= pi sum_m e_m^2/d_m, and w >= 5^(-11/10) on its support. On r >= R the residual is the exact finite
sector expansion from the first two binomial orders of the four potential branches (powers gamma - j delta - 2a, the
leading one q with angular data E_1, all others below q) plus an error bounded uniformly by C_tail r^q with
C_tail < 1.762e-18 (geometric majorant of the omitted binomial orders of the potential and its third and fourth
derivatives). Hence every sin(m theta) coefficient of F, m = 1, ..., 39 odd, has the sign of e_m and modulus at least
b_m r^q with explicit b_m = |e_m| - (lower sectors at r = R) - 2 C_tail > 0, and
  L(F) >= sqrt(pi) R^(q+2) 5^(-11/10) (sum_m |e_m| b_m/d_m) / (30 (sum_m e_m^2/d_m)^(1/2)) > 4.4839e19,
  N^w_s(F) > 7.0925e26 > 2^89  for every 0 < s <= 2^-12,
so N^w_s(F)/eta > 2^135 (about 5.0e40) at the choice s = 2^-30 above (768-bit certificate; the 860 coefficients are
reconstructed independently from the original checkpoint; three full Cartesian-jet evaluations at r = R and 2R agree
with the truncated sectors within the proved error). A floating-point evaluation of the whole far field (all radii,
mode-wise radial Green functions) gives L(F) of about 8.8e20 and 2^(53/2) L(F) of about 8.4e28 (FLOAT), so the
annular bound is within a factor of about 120 of the true size. The earlier certified bound N^w_s(F) > 2^-18 (from F(0, 1000) > 1/8 and
|g(X)| <= 2^13 max(1, r)^(1/5) N^w_s(g)) is superseded. The theorem is a sufficient condition; this does not exclude a
profile near state 131, and gives no existence result. The bound concerns state 131 only: the algebraic repairs of
section 3 cancel every residual sector above r^-2, so this growing-sector bound does not transfer to them.

Smaller radius (THEOREM). The theorem also holds with R = 2^32 in w and in every norm, with the same s, r_0, eta and
constants (32, 6, 3/1024, 2^68), when the decay bounds of (W1) are taken with d = 4/9 instead of 2/5:
sup r^d (|D rho| + r |D^2 rho|) <= 190, sup r^(d - 1)|u| <= 23, sup r^d |Du| <= 23,
sup r^(1 + d)|D^2 u| <= 56. This needs 4/9 < 1 - gamma (true for state 131: 1 - gamma = 0.4476). The radial
commutator factor is then 4 sigma M_d/(3 - sigma - d) < 14.573 (sigma = 11/5, d = 4/9, M_d = (d/2)((2 - d)/d)^(1 - d/2)),
and the low energy margin is mu = 2/5 - R^-d [23 + 16 * 190 + (11/5)(9 * 23 + 2 * 23 + 56/sqrt 2)] > 0.2060571
(rational check: 19000^9 < 2^128 and 1/sqrt 2 < 5/7 give mu > 9731/47500 > 1/5). The derivative weights, the
interpolation inequality (proved for all R >= 1), the low commutator estimate (uniform in R >= 1) and the velocity
bound 13/2 do not depend on R, so the rest of the proof is unchanged. For state 131 the four bounds are certified from
the original checkpoint (interior r <= 100 from the global bounds of (W3), times 100^(4/9) < 7.75; exterior by exact
sectors with negative radial exponents d - delta - j delta - 2q). The annular bound at R = 2^32 gives
L(F) > 5.6305e17 and N^w_s(F) > 8.906e24 > 2^82, a gap of more than 2^128 over eta. The smaller radius lowers the
norm of a growing residual by a factor of about 2^(3(q + 2)) (about 80), far from what the gap requires.

Sharper constants (THEOREM). The norm gives the two lower derivative components the coefficients 2^-11:
P_0(H) = ||<r>^(-6/5) H||_2 and P_1(H) are at most E^w(H)/2048 (for P_0 from the interpolation inequality
P_0^2 <= P_1^2 + 26 L^2). Keeping these coefficients in the localization step, instead of bounding P_0 and P_1 by
E^w, replaces the localization constant 548 by 2595/2048 and improves every later constant, with the same space, the
same hypotheses (W0)-(Wt) (with (W1) at R = 2^35 or its d = 4/9 version at R = 2^32) and the same domain and
consistency arguments: ||D g||_inf <= 4 N^w_s(g)/s^(1/2), Hoelder constant 8, |g(X)| <= 16 max(1, r)^(1/5) N^w_s(g),
weighted derivative multiplier 32, rough loss 1964/5 < 400 times N^w_s(k)/s^(1/2) (instead of 2^19), low bilinear
constant 1820 < 2^11 (using the exact Hausdorff-Young constant of the embedding H^1 into L^(4/s), at most s^(-1/2)).
So for 0 < s <= 2^-12 the decay rate of A_k is 1/20 - 2^23 s - 400 N^w_s(k)/s^(1/2). Take s = 3 * 2^-31,
r_0 = 5 * 2^-32, eta = 2^-35 (= 2.9103830456...e-11). On the ball the rate is at least 6283/245760 > 1/40 (high
inverse at most 40, and 40 eta = r_0), the low inverse is at most 6, the low contraction factor is
6 * 2^11 r_0/s^(1/2) = 15/(16 sqrt 6) < 2/5, and the slope changes by at most 4 r_0/s^(1/2) < 2^-12. If
N^w_s(F(rho; c)) <= 2^-35, there is exactly one h with N^w_s(h) <= r_0 and c[h] = 0 such that F(rho + h; c) = 0, and
L(h) + C_ad(h) + M(h) + |c[h]| <= 2^8 s^(-3/2) N^w_s(h) <= 2^58 N^w_s(F); bounding c[h] = d_y U_2[h](0) directly as
a trace of the velocity gradient (its multiplier has modulus at most (2/(3 sqrt 3)) |xi|) gives |c[h]| <= N^w_s(h)/s^(1/2)
and the sharper L(h) + C_ad(h) + M(h) + |c[h]| <= 146 N^w_s(h)/s^(1/2) <= 2^28 N^w_s(F) (THEOREM; S1_PROOFS.md, P37),
with the threshold, the radius and the contraction factor unchanged. This improves the threshold by a factor
2048. For state 131 the gaps over 2^-35 are more than 2^124 at R = 2^35 and more than 2^117 at R = 2^32 (the annular
bounds hold for every 0 < s <= 2^-12, and 3 * 2^-31 < 2^-12). The proof is part P19 of S1_PROOFS.md.

Second version: smooth commutator (THEOREM; S1_PROOFS.md, P43). For R >= 2^31 and 0 < s <= 2^-12, under
|c| <= 2, |Du| <= 14/5, |D^2 u| <= 3, <r>|D^3 u| <= 16, |D^2 rho| <= 3, <r>^2 |D^3 rho| <= 32 and
<r>^2 |D^4 rho| <= 512 (all contained in (W0)-(W3)), the commutator of J^s with the frozen operator satisfies
E^w([J^s, L_0] J^-s H) <= (9325421/1200) s E^w(H) <= 2^13 s E^w(H) (Bessel and heat-subordination kernels with
explicit moments, the exact linear term -s Du : D^2 J^-2, the low component factored through q = D(-Delta)^-1(w h)).
The decay rate of A_k becomes 1/20 - 2^13 s - 400 N^w_s(k)/s^(1/2). At s = 3 * 2^-21, r_0 = 5 * 2^-27,
eta = 2^-30 (= 9.3132257461...e-10) the ratios 2^13 s and r_0/s^(1/2) equal those of the previous paragraph, so with
the same hypotheses (at R = 2^31, 2^32 or 2^35): if N^w_s(F(rho; c)) <= 2^-30, there is exactly one h with
N^w_s(h) <= r_0 and c[h] = 0 such that F(rho + h; c) = 0 (high inverse 40, low inverse 6, contraction factor
15/(16 sqrt 6) < 2/5), and L(h) + C_ad(h) + M(h) + |c[h]| <= 40 * 146 s^(-1/2) N^w_s(F) <= 2^23 N^w_s(F). For state
131 the gaps over 2^-30 are more than 2^112, 2^114 and 2^120 at R = 2^31, 2^32 and 2^35. A consolidated audit of this theorem (maximal distributional domains and their identification with the generator domains, consistency of the low and high inverses on the nonlinear differences, the exact normalized range N_0 = {f : d_y f(0) = 0} and domain D(A_k) cap ker c, completeness of the normalized ball in the low metric) found no defect and rechecked every constant (S1_PROOFS.md, P63).

Smallest radius (THEOREM). For real densities the angular input modes n and -n have equal energy. With
B = (d_x - i d_y)^2 (-Delta)^-1 one has U_2 + i U_1 = (B - I)h/2; B maps mode n >= 3 to n - 2 with norm at most
A_n = n(n - 2 + sigma)/((n - 2)(n - sigma)), mode -n to -n - 2 with norm at most D_n = 1 + sigma/(n + 2), and mode 1 to
-1 as minus the identity, in the conjugated weighted space. Keeping the cross term of ||(B - I)h/2||^2 gives a
nonnegative three-diagonal comparison matrix (J_11 = 5/8 + D_1^2/8, J_nn = 1/4 + (A_n^2 + D_n^2)/8,
J_(n,n-2) = (A_n + D_(n-2))/8), and the weighted Schur test with weights 1/10, 1, 1/20, 1/20, ... bounds it by 75/4.
Hence the canonical velocity satisfies ||w U[h]||_Hdot^-1 <= sqrt(75/4) ||w h||_Hdot^-1 < (13/3) ||w h||_Hdot^-1 for
every R > 0 and 0 <= sigma <= 11/5 (instead of 13/2). The same pairing bounds the real radial commutator coefficient by
sqrt((P^2 + D^2)/2) < 10.339 < 21/2, with P = (99/4) M_d and D = (132/65) M_d (instead of P < 14.573). With
the decay bounds of the smaller-radius version tightened to (186, 22, 22, 56) (certified for state 131 by the same
enclosures), the low margin at R = 2^31 is 2/5 - R^-d [22 + (1 + 21/2) 186 + (11/5)(9 * 22 + 2 * 22 + 56/sqrt 2)]
> 14093/70000 > 1/5 (14000^9 < 2^124). Every other estimate is uniform in R >= 1, so the theorem of the previous
paragraph (s = 3 * 2^-31, r_0 = 5 * 2^-32, eta = 2^-35, inverses 40 and 6, output bound 2^28) holds at R = 2^31; the
low bilinear constant becomes 3640/3. For state 131 the annular bound at R = 2^31 gives L(F) > 1.3084e17 and
N^w_s(F) > 2.0697e24 > 2^80, a gap of more than 2^115. The proofs are part P21 of S1_PROOFS.md.

Weaker matrix hypothesis (THEOREM; S1_PROOFS.md, P24). In the hypotheses of Theorem D_w at R = 2^31 the low matrix
condition M = (2c + 1) I + sym Du + A >= (19/5) I of (W1) can be replaced by M >= (5/2) I on r <= R (outside R the
baseline argument gives a margin above 853/2000 without any matrix floor), or by the position-dependent floor
M >= 2/5 + (11/5) c r^2/(R^2 + r^2) on r <= R. Every other hypothesis (the decay-coefficient bounds of (W1), (W2),
(W3)), the low margin 14093/70000 > 1/5 and every later constant are unchanged. The floor 19/5 entered only as a
baseline in the low-energy identity, where 5/2 - (11/10)(37/20) = 93/200 suffices. For a reference with other decay
coefficients the radius beyond which the position-dependent floor is implied must be recomputed.

Necessary residual scales (THEOREM; S1_PROOFS.md, P30, P44 and P47). Since L(J^-s g) <= (11/10) L(g) and
|g(X)| <= (1/12) max(1, |X|)^(1/5) N^w_s(g) for every R >= 1 and 0 < s <= 2^-12 (first proved with the constants 6
and 16), the threshold N^w_s(F) <= 2^-35 requires L(F) = ||w F||_Hdot^-1 <= (11/10) 2^(-123/2) < 2^-61 and
|F(X)| < 2^-38 max(1, |X|)^(1/5) at every point (2^-56 and 2^-33 for the threshold 2^-30). The weighted amplitude and
L^2 bounds w |g| <= N^w_s(g)/1000 and ||w g||_2 <= N^w_s(g)/190000 (S1_PROOFS.md, P48 and P49) sharpen the pointwise
condition to |F(X)| < 2^-44 (1 + |X|^2/R^2)^(11/10) (2^-39 for 2^-30) and add ||w F||_2 < 2^-52 (2^-47). These are necessary
conditions, not sufficient ones. Conversely, a certified point value |F(X)| gives
N^w_s(F) >= 12 |F(X)|/max(1, |X|)^(1/5) for every 0 < s <= 2^-12; the point gaps of section 9 were first computed
with the factor 1/16 and are restated with 12 in section 11.

Necessary local distance (THEOREM; S1_PROOFS.md, P38 to P47). If rho_bar has the leading profile of the checkpoint,
every exact solution rho_bar + h with h in the space has the exponent of rho_bar (exponent rigidity), and pairing the
difference equation with compact tests bounds the residual pairing by A n + Q n^2, n = N^w_s(h). Certified tests
exclude, for every 0 < s <= 2^-12 and R >= 1, every exact solution with N^w_s(h) <= 2^-14 around state 131 (annular
test at T = 2^31), 2^-9 around Mpen2 and d2 (square tests with the weighted amplitudes of P48), and for R >= 2^31
2^57 around state 131 and 2^21 around Mpen2 and d2 (annular tests with the weighted L^2 bounds, P49 and P52); at
s = 3 * 2^-31 point tests exclude 2^-11, 2^-13, 2^-18, 2^-21, 2^-21, 2^-21 and 2^-16 around A2, A3, A4, A5, Mpen,
A6dpen and b6. All radii exceed r_0 = 5 * 2^-32 and 5 * 2^-27. These are local statements.

Independent recomputation of the gap at R = 2^35. A separately written program of the numerical work (single mode
sin(theta), smooth log-radial bump on 2^34 <= r <= 2^36, own exact sectors, rigorous adaptive integration) gives a lower
bound for L(F), and an independent audit with freshly reconstructed sectors confirms L(F) > 1.1221e19 and
N^w_s(F) > 1.77498e26 > 2^87, a gap of more than 2^122 over 2^-35 (S1_PROOFS.md, P11.2). The same program also evaluates the combined test (all
leading modes) with exact integration of the radial weight; an independent audit (fresh reconstruction of the 860
coefficients, its own exterior sectors and remainder, 384-bit log-coordinate quadrature) confirms L(F) > 3.7247e17,
1.6026e18, 1.2761e20 and N^w_s(F) > 5.8916e24, 2.5351e25, 2.0186e27 at R = 2^31, 2^32, 2^35, gaps of more than 2^117,
2^119 and 2^125 over 2^-35 (THEOREM; S1_PROOFS.md, P11.4). These exceed the twenty-mode bounds above because the
radial weight and the test energy are integrated exactly.

Earlier version. The first proof of this theorem (same space) bounded the low-order commutator through the weighted
L^2 component, at a cost of a factor 2^42; its rate was 1/20 - 2^92 s - 2^19 N^w_s(k)/s^(1/2), with s = 2^-104,
r_0 = 2^-78 and eta = r_0/24 (about 1.3786e-25). The direct factorization h = -div(w^-1 q) - (D log w).(w^-1 q),
q = D(-Delta)^-1(w h), which applies the parity Hardy inequality ||f||_Hdot^-1 <= ||r f||_2 (for centrally odd f) only
to the weight-derivative remainders, removes that factor.

## 8. Arithmetic: the admissible residual

The script scripts/closure_arithmetic.py evaluates the threshold in interval arithmetic. All constants in the table are
proved: mu_0 = 1/10 always; C_bg = 1024 M* (at most 2^22) and c_U = 128 for 0 < s <= 1/2 under (B9); C_bg = 4800 and
c_U = 5 for 0 < s <= 1/1024 under (B9c).

| scenario | s | eta_0 |
|---|---|---|
| Theorem D(a) as stated (r = 2^-27, eta = r/20) | 2^-28 = 3.7e-9 | 3.7e-10 |
| constants of (a), M* <= 4096, s = 2^-28, best radius | 3.7e-9 | 8.4e-10 |
| constants of (a), M* <= 4096, optimal s | 4.8e-9 | 8.6e-10 |
| constants of (a), M* <= 2374, optimal s | 8.2e-9 | 1.1e-9 |
| Theorem D(b) as stated (r = 2^-16, eta = r/24) | 2^-18 = 3.8e-6 | 6.357e-7 |
| constants of (b), s = 2^-18, best radius | 3.8e-6 | 6.51e-7 |
| constants of (b), optimal s | 1/240000 = 4.2e-6 | 6.53e-7 |

eta_0 = mu^2 s^(1/2)/(4 c_U) with mu = mu_0 - C_bg s, so it scales like mu_0^(5/2) C_bg^(-1/2) c_U^(-1) at the optimal
s. In every row c_s r < 1/400, so the slope and contraction conditions hold with a wide margin. Case (b) gains a factor
of about 1700 over case (a), mostly from the rough constant (5 instead of 128) and from charging each background
coefficient only at the derivative level where it acts.

Composition of the residual norm.

    E_2(R_tilde)^2 = ||omega D^2 R_tilde||_2^2 + 2^14 ||grad R_tilde||_2^2 + 2^18 ||R_tilde||_2^2
                     + 2^18 (20/21) ||R_tilde||_H^2,

and N_s(R_tilde) is bounded by the residual conversion of section 2: N_s(f) <= E (2 (Q/E)^2 + 16410)^(s/2) + 34 s E.
At s = 2^-18 this is at most 1.0003 E whenever Q <= e^25 E (at s = 2^-28, at most 1.0001 E whenever Q/E <= exp(10^4)).
So in case (b) it suffices that E_2(R_tilde) <= 6.355e-7 and Q <= e^25 E_2(R_tilde). Since the four components form one
square sum, each one alone must satisfy ||omega D^2 R_tilde||_2 <= 6.4e-7, ||grad R_tilde||_2 <= 5.0e-9,
||R_tilde||_2 <= 1.24e-9 and ||R_tilde||_H <= 1.27e-9; the low-order components carry the factors 2^7 and 2^9.

## 9. Status for the available references

| reference | (B0)-(B9) | (B10m): residual in the space | residual size ((B10s)) | exact solution in rho + N_s |
|---|---|---|---|---|
| state 131 (checkpoint) | all THEOREM | no: sector exponent 0.1048, not in L^2 or H | ||omega D^2 R||_2 = 25.18922..., ||omega D^3 R||_2 = 2.50428... (THEOREM); lower components infinite | none (Theorem E) |
| exact refit m5: E_1 = 0, monomial mid field (1020 generators) | (B1) THEOREM; rest not certified | no: E_(2,0) != 0 (THEOREM), so not in H | ||<r>^0.7 D^2 F||_2 = 3.61 (FLOAT) | none (Theorem E) |
| exact refit m10: E_1 = 0, Legendre mid-field blocks (1200 generators) | not certified | no: E_(2,0) != 0 at exponent p_3 = -0.343 (THEOREM), so not in L^2 or H | ||grad F||_2 = 0.344473..., ||omega D^2 F||_2 = 5.00992..., ||omega D^3 F||_2 = 12.3311... (THEOREM); ||F||_2 infinite | none (Theorem E) |
| tail repair of state 131 at R = 2^1024 | all THEOREM | yes (THEOREM) | N_s(F) >= 2^1028 (THEOREM) | not excluded; Theorem D not applicable |
| projected refits A2 and A3 (2342 generators, all eight sectors cancelled exactly) | (B1) false (THEOREM: least eigenvalue of M 2.2225 and 3.1352 at (0, 1), below 19/5 at four of eight certified points; A2 also violates the constant weakened floor 5/2 of section 7a there); (W3) false (THEOREM: rho_yy(0, 1/10) > 4.717 and > 10.899 against |D^2 rho| <= 3); rest not certified | yes (THEOREM): residual starts at r^(p_7), in N_s and N^w_s | N^w_s(F) > 20014377 (A2) and > 20013535 (A3) at R = 2^31, more than 2^59 times 2^-35 (THEOREM: annular duality test with the exact leading sector r^(p_7) and a certified remainder) | not excluded; Theorems D and D_w not applicable |
| projected refit A4 (exactly admissible, THEOREM) | (B1) false at (0, 1/10) (THEOREM; the weakened floor 5/2 is not violated at the certified points); (W3) false (THEOREM: |D^2 rho| > 3.050 and <r>^2 |D^4 rho| > 2001.1 at (0, 1/10), <r> |D^3 u| > 35.57 and <r>^2 |D^3 rho| > 49.64 at (0, 1/5)) | yes (THEOREM) | N^w_s(F) > 9/100 from F(3, 4) = -2.06597... (THEOREM, point value), more than 2^31 times 2^-35 | not excluded; Theorems D and D_w not applicable |
| projected refits A5 and Mpen (Mpen fitted with a penalty for (B1); exactly admissible, THEOREM) | (W3) false (THEOREM: <r>^2 |D^4 rho| > 692.78 (A5) and > 678.83 (Mpen) at (0, 4/5), against 512); M >= (19/5) I and M_1, M_2 >= I/2 at the eight certified points (point values only, no proof on the plane) | yes (THEOREM) | N^w_s(F) > 0.02036 (A5) and > 0.01781 (Mpen) from the certified values F(6, 8) = -0.51641... and -0.45171... (THEOREM), more than 2^29 times 2^-35 | not excluded; Theorems D and D_w not applicable |
| projected refit A6dpen (fitted with a penalty for the descendant sector (2, 1); exactly admissible, THEOREM) | (W3) false (THEOREM: <r>^2 |D^4 rho| > 551.52 at (0, 1/5) and > 631.67 at (0, 4/5)); (W2) holds at the eight certified points only | yes (THEOREM) | N^w_s(F) > 0.00732 from F(6, 8) = -0.18570... (THEOREM), more than 2^27 times 2^-35 | not excluded; Theorems D and D_w not applicable |
| projected refit Mpen2 (fitted with both penalties; exactly admissible, THEOREM) | M >= (19/5) I, M_1, M_2 >= I/2 and every bound of (W3) hold at the eight certified points; (W3) false off-axis (THEOREM: <r>|D^3 u(19/64, 7/16)| > 16.12 > 16, <r>^2 |D^3 rho(19/64, 7/16)| > 39.23 > 32, <r>^2 |D^4 rho(1/4, 15/32)| > 1333 > 512) | yes (THEOREM) | N^w_s(F) > 0.0048729 from F(6, 8) = -0.12357... (THEOREM), more than 2^27 times 2^-35 (N^w_s(F) > 12.66 for every R >= 1 and > 1.759e9 for R >= 2^31, P48 and P52) | none with N^w_s(h) <= 2^-9, for every s and R (2^21 for R >= 2^31) (THEOREM); Theorem D_w not applicable (residual too large) |
| exactly admissible seven-branch refit b6 (2902 generators, first seven branches stationary, nine sectors vanish exactly) | (W2) false (THEOREM: M_2(3, 4) < 0.46618 < 1/2); (W3) false (THEOREM: |D^2 rho(0, 1/5)| > 10.33 > 3 and <r>^2 |D^4 rho(3, 4)| > 27670 > 512) | yes (THEOREM) | N^w_s(F) > 59.586 (THEOREM, point values, uniform in s and R), more than 2^35 times 2^-30 | none with N^w_s(h) <= 2^-16 at s = 3 * 2^-31 (THEOREM); Theorem D_w not applicable |
| six-branch refit d2 (2382 generators; nine sectors vanish exactly, including the first descendants of branches 0, 1 and 2) | (W1) to (W3) hold at the eight certified points; the matrix part M >= (19/5) I of (W1) and the matrices M_1, M_2 >= I/2 of (W2) hold on the whole plane (THEOREM, P95: complete covers with 41, 79 and 119 leaves, each rechecked independently); so do the decay bounds of (W1) in the form at R = 2^31 (decay exponent d = 4/9; 186, 22, 22, 56) and the five bounds of (W3) not left free by the parametric theorem (THEOREM, P95: covers with 36, 121, 314 and 23 leaves, rechecked independently), and with the caps of P91 every reference hypothesis of the parametric logarithmic theorem holds (THEOREM, P105); (W3) false off-axis (THEOREM: <r>^2 |D^4 rho(7/16, 7/64)| > 592 > 512) | yes (THEOREM) | N^w_s(F) > 5.479 (THEOREM, point values, uniform in s and R >= 1), more than 2^32 times 2^-30; > 1.759e9 for R >= 2^31 (P52) | none with N^w_s(h) <= 2^-9, for every s and R (2^21 for R >= 2^31) (THEOREM); Theorem D_w not applicable ((W3) and residual smallness fail); the parametric logarithmic theorem fails only residual smallness, Mstar(F)/eta > 2^243 (THEOREM, P105) |
| every coefficient choice in the generator family of the refits (j <= 5, m <= 59, k <= 75; six leading branches and two descendants prescribed) | not applicable (a family) | yes, for every member (THEOREM) | N_s(F) > 0.01461 at s = 2^-18 for every member (THEOREM; section 11), more than 22986 times the threshold of Theorem D(b), and above the threshold for every radial degree k <= K, K <= 3675; in the weighted space, for each fixed radial degree a positive lower bound uniform in the coefficients, 0 < s <= 2^-12 and R >= 1 is proved (P56, P57; evaluated only in the weak form of P62), but no weighted bound above the weighted thresholds and none uniform in the radial degree | Theorem D(b) applies to no member |
| algebraic repairs of state 131 and m10, K = 4, 8, 16, 256, 4096 | (B1) false for every K <= 256 (THEOREM: certified negative eigenvalue of M, for example between -395.21 and -9.155 at (1, 1) for K = 4, 16) and for state 131 K = 4096 (least eigenvalue < 3.417 at r = 2^4.75); m10 K = 4096 not certified (no sampled failure) | yes (THEOREM): residual starts at r^(p_7) | N_s(F) > 1305 for K = 4, 8, 16, > 605 and > 208 for K = 256, > 25.44 and > 11.48 for K = 4096 (THEOREM, point values); ||omega D^2 F||_2 = 863401.8... for m10 K = 8; 7344656 < N_s(F) < 19372856 (K = 8) and 3600047 < N_s(F) < 16301199 (K = 16) for m10 at s = 2^-18 (THEOREM) | not excluded; Theorem D not applicable |

The THEOREM norms are whole-plane values with omega = (1 + 4 r^2)^(2/5), computed by exact rational integration of the
exact residual polynomials in the compactified variables (only pi and a rigorously enclosed weight series are not
rational; no quadrature), with an independent recomputation at 640 bits (S1_PROOFS.md, P12). The enclosing intervals are
[25.1892236171285365, 25.1892236171285379] and [2.5042775321848363, 2.5042775321848366] for state 131, and
[0.3444735104934888, 0.3444735104934889], [5.0099247071386049, 5.0099247071386053] and
[12.3311345810175309, 12.3311345810175319] for the refit m10.

Since (1 + 4 r^2)^(2/5) >= (1 + r^2)^(7/20) everywhere, the FLOAT value for the refit m5 indicates (heuristically: FLOAT, no
error enclosure) a lower estimate for the omega-weighted Hessian norm that enters E_2.

A second realization with bottom weight (1 + r^2/R^2)^(-11/10), R = 2^179 (S1_PROOFS.md) contains the original
checkpoint residual and has a proved inverse of norm 40, but its low-order weights make the residual norm far larger
than any admissible threshold. It is not used for closure.

## 10. Theorem E: a necessary condition in the affine class (THEOREM)

Theorem D is a sufficient condition. The following theorem shows that its membership requirement (B10m) is not an
artifact of the method: a residual sector that is too large at infinity excludes every exact solution in the affine class
rho_tilde + N_s, of any size (S1_PROOFS.md, P13.2).

Theorem E. Let rho_bar be a smooth density of the parity class (even in x, odd in y) with bounded gradient and canonical
velocity u = U[rho_bar]. Suppose that for some C > 0, R_0 >= 1 and 0 < gamma < 1

    |u(X)| <= C |X|^gamma,   |Du(X)| <= C |X|^(gamma - 1)   for |X| >= R_0.

Fix c and put F_bar = (cX + u).grad rho_bar - rho_bar. Let h be C^1 with bounded gradient, h in H, with canonical velocity
W = U[h], and suppose rho_bar + h is stationary with the same c (distributionally suffices). Let phi be smooth with
support in 1 < |X| < 2, put R_j = 3^j R_0 and m_j = integral of F_bar(X) phi(X/R_j) dX. With A = ||D phi||_2,
B = ||D(X.D phi)||_2, D_2 = ||D^2 phi||_2 and K = |c| B + |2c + 1| A + C R_0^(gamma - 1)(A + 2^gamma D_2),

    (sum_j m_j^2)^(1/2) <= [K + A (||D rho_bar||_inf + ||Dh||_inf)] ||h||_H.

Consequently, if F_bar(r, theta) = r^q E(theta) + o(r^q) uniformly in theta, with E continuous and not identically zero
and q >= -2, no such h exists. The same holds for a leading term r^-2 (log r)^(-beta) E(theta) with beta <= 1/2.
Every h in N_s, s > 0, satisfies the hypotheses on h (N_s embeds in H^(2+s) and in H).

Proof idea. Subtracting the reference equation and testing with phi(X/R_j) gives m_j = <h, chi_j> - <G, phi_j> with
chi_j = cX.D phi_j + (2c + 1) phi_j + u.D phi_j and G = W.grad(rho_bar + h). In two dimensions ||D f(./R)||_2 does not
depend on R, so ||D chi_j||_2 <= K, and the supports of the chi_j are disjoint, which gives the l^2 bound by duality
between H and the homogeneous H^1. The nonlinear term is in H because W.grad v = -div(psi D^perp v) with
psi = partial_x (-Delta)^-1 h, ||psi||_2 <= ||h||_H. A sector r^q E gives m_j of exact order R_j^(q + 2).

Corollary E1 (THEOREM). Fix c = c_l. There is no h in N_s, for any s > 0 and of any norm, with
F(rho_bar + h; c_l) = 0, when rho_bar is state 131 or state 88 (leading residual exponent p_2 = 2 gamma - 1 = 0.1048 for state 131 and
0.1059 for state 88, whose gamma is 0.55293) or
one of the exact refits m4, m5, m10, m12 (E_(1,0) = 0 exactly, leading exponent p_3 = 3 gamma - 2 = -0.3428, E_(2,0) not
zero) or the exact refit m14 (sectors (0,0) to (3,0) zero, leading sector (4,0) of exponent p_5 = -1.2381 not zero). For a reference given by a finite potential of the canonical generator form, every residual sector has an
exponent gamma - h(1 - gamma) - 2q (h, q >= 0 integers), the expansion converges uniformly for r >= 2, and an exact
solution in rho_bar + N_s can exist only if all sectors with exponent >= -2 vanish: (h, 0) for h <= 5 (exponents p_1
to p_6) and the radial descendants (0, 1) and (1, 1) (exponents gamma - 2 = -1.448 and 2 gamma - 3 = -1.895); the sector
(0, 0) vanishes automatically at c = 1/gamma, so there are seven genuine conditions. There are no other sectors with
exponent >= -2 (at q = 0 one needs h <= (2 + gamma)/(1 - gamma) = 5.70, at q = 1 h <= gamma/(1 - gamma) = 1.23, and none at
q >= 2). The vanishing of these eight sectors is necessary and sufficient for F to lie in N_s, 0 < s <= 1/2 (if one of
them is nonzero, F is not even in H; if all vanish, F = O(r^(p_7)) with all derivatives), so (B10m) is exactly this test,
and by Theorem E it is also necessary for an exact solution in rho_bar + N_s.

Corollary E2 (THEOREM; exponent rigidity). Suppose rho_bar = r^gamma Theta_0 + O(r^(gamma - delta)) and
X.D rho_bar = gamma r^gamma Theta_0 + O(r^(gamma - delta)) uniformly, with Theta_0 not zero and delta > 0, and
F_(c_0)(rho_bar) = o(r^gamma), c_0 = 1/gamma; this holds for every finite potential considered here. Then for every
c != c_0 there is no h as in Theorem E with F(rho_bar + h; c) = 0. Indeed F_c(rho_bar) = F_(c_0)(rho_bar) +
(c - c_0) X.D rho_bar has the nonzero leading sector (c - c_0) gamma r^gamma Theta_0, of exponent gamma > -2, and the
constant K of Theorem E is valid for every real c. So Corollary E1 holds for every value of the exponent, and an exact
solution in rho_bar + N_s for an admissible reference must have c = c_0; if its center slope is nonzero, the origin
identity then gives c[h] = 0.

A companion result (S1_PROOFS.md, P13.1; THEOREM) describes the forced correction. If in addition |D rho_bar| <=
C r^(gamma - 1), u is globally Lipschitz, F_bar = r^q E + o(r^q) with gamma - 1 < q and cq < 1, and h is a bounded C^1
stationary correction with bounded Lipschitz W, then h = r^q E(theta)/(1 - cq) + o(r^q) uniformly (proof by integrating
along the outward characteristics of cX + u + W). For the refits m4, m5, m10 and m12 (q = 3 gamma - 2), 1 - c q = 2(c - 1) > 0 and the forced correction is a
nonzero r^(3 gamma - 2) tail (angular quarter-circle norm 0.184 for m10), which is not in L^2. For m14
(q = p_5 = -1.238 < gamma - 1) the hypothesis gamma - 1 < q fails and P13.1 does not apply; Theorem E still excludes
it, since q >= -2.

Scope. Theorem E concerns one fixed affine class at fixed c. It does not exclude solutions in weighted correction spaces
or in spaces augmented by explicit tail coordinates, and it does not apply to the tail repairs of section 3, whose residuals start at r^(p_7), p_7 = -2.133 < -2. It is not a nonexistence theorem for the profile.

## 11. The gap

For Theorem D_w (section 7a) only one requirement remains for the checkpoint: smallness, N^w_s(F) <= 2^-35 for the
first version, against the certified N^w_s(F) > 5.89e24 > 2^82 at R = 2^31 (a factor of more than 2^117; the
twenty-mode bound alone gives 2^115), 2.53e25 at R = 2^32 and 2.01e27 at R = 2^35. By the consequences stated in
section 7a, smallness needs ||w F||_Hdot^-1 < 2^-58 and |F| <= 2^-31 max(1, |X|^(1/5)) at every point. The exactly
admissible projected refits remove the growing sector, but their certified residual values lie between 0.12 and 27 at
radii 2 to 10, each violates a derivative bound of (W3) at a certified point (off-axis for Mpen2 and d2), and their certified gaps
over 2^-35 are more than 2^59 (A2, A3), 2^31 (A4), 2^29 (A5, Mpen) and 2^27 (A6dpen, Mpen2) with the amplitude factor
1/16 (section 9). With the factor 12 of section 7a the point values give N^w_s(F) > 277.09, 143.71, 17.968, 3.910,
3.420, 1.406, 0.9356, 59.586 and 0.14095 for A2, A3, A4, A5, Mpen, A6dpen, Mpen2, b6 and d2, more than 2^27 times
the threshold 2^-30 of the second version in every case (THEOREM; S1_PROOFS.md, P45). With the weighted amplitude
bound N^w_s(F) >= 1000 w |F| (P48) the same points give, uniformly in s and R >= 1, N^w_s(F) > 5195.0, 2850.1, 309.38,
40.58, 39.61, 19.21, 12.66, 1380.0 and 5.479 (more than 2^37 times 2^-35), and for R >= 2^31 more than 26524, 14449,
2308.4, 516.4, 451.7, 185.7, 123.5, 5849.1 and 16.71; annular tests give N^w_s(F) > 1.759e9 for Mpen2 and d2 and
N^w_s(F) > 3.53e25 for the checkpoint for every R >= 2^31 (P51, P52). All nine refits violate (W3) at a certified point
(P54, P58 for d2 and Mpen2).

Positive floors for fixed families (THEOREM; S1_PROOFS.md, P56, P57 and P59). For each fixed radial degree K of the
six-branch family (six leading branches and two descendants prescribed), N^w_s(F) over all real coefficients has a
positive lower bound delta_K uniform in 0 < s <= 2^-12 and R >= 1, because the quadratic transport is proper on
finite-dimensional L^2 density spaces (div(v U[v]) = 0 forces v = 0). The bound has an explicit formula in Gram, tail
and remainder constants (the velocity constant is the sharp sin^2(pi/242) for this angular band), which is not
evaluated; so it does not decide the thresholds. The same holds for each fixed radial degree of the seven-branch
family with the descendant (2, 1) free (P60): the signed radial test b_0(t)(c_* - t) annihilates the free sector
r^(-2.343) exactly and pairs with the fixed sector r^(p_8), p_8 = -2.581, with radial factor J_* > 1/67200, so the free
sector cannot cancel the fixed one in the weighted norm; again no value is computed. A weaker floor of the same
kind is evaluated exactly (P62): N^w_s(F) >= 2045 E_J D/sqrt(2) with E_J the angular norm of the fixed sector and D an
explicit finite Muntz product over the powers of the exact radial representation; its values (above 6e-55 for six branches
at radial degree 75, above 3.46e-75 for seven at degree 69) are far below both thresholds.

Endpoint spaces (THEOREM; S1_PROOFS.md, P61, P64 and P65). These results explain why N_s and N^w_s use a strictly
subcritical far-field weight. In the critical space L^2(<r>^(-2-2 gamma) dX), and in the critical weighted
Sobolev spaces with norm sum_(j <= m) ||<r>^(j-1-gamma) D^j h||_2 for every m >= 3 (where the canonical velocity is
bounded and the strain c[h] is a continuous functional), slowly cut-off copies of r^gamma sin(5 theta) on logarithmic
annuli have zero strain, satisfy any finite list of exact linear constraints and are approximate null vectors.
Hence no closed realization of the normalized linearization, with a compact perturbation and finitely many added
parameters and equations, is upper semi-Fredholm. With the growth exponent b in place of gamma (-3 < b < 1) the
whole line Re z = c_l b - 1 lies in the spectrum, so an inverse at zero in that space has norm at least
1/|1 - c_l b| (5/(5 - c_l) = 1.5676... at b = 1/5). This is a necessary bound in that Sobolev space; it is not
compared with the sufficient constant 40 of the different norm N_s. The obstruction persists under logarithmic
modifications (1 + log <r>)^kappa of the critical weights and for closed block operators with arbitrary Banach spaces
of tail coordinates that act on the constrained compact core of the unchanged remainder as (h, 0) -> (B h + K h, Q h)
with K and Q compact (P68).

Strain regularization (THEOREM; S1_PROOFS.md, P69). The fractional surplus s > 0 in N_s and N^w_s cannot be removed
without losing the strain. On real S1 functions in H^(2+s), b[h] = h_y(0) and c[h] have the Gram matrix
[1/(8 pi s (s + 1))] [[1, -1/4], [-1/4, 1/8]] in the dual space. Hence ||c|| = 1/[8 (pi s (s + 1))^(1/2)], and on
{b = 0} it is 1/[8 (2 pi s (s + 1))^(1/2)]; the renormalized strain c + b/4 is a pure angular harmonic 3. In the weighted
norm N_(s,R), with its coefficients 2^22 and 2^53, s^(1/2) C_R(s) -> 1/(8 pi^(1/2)) and
s^(1/2) C_R^0(s) -> 1/(8 (2 pi)^(1/2)), uniformly in R >= 1. At s = 0, c is unbounded on the compact core even when
b = 0. So the s^(-1/2) factor of every strain bound by N_(s,R) is intrinsic. The theorem gives no finite-s upper
constant and does not change any inverse, threshold or residual bound. A logarithmic gain suffices for the trace
(P70): with Q_beta = (1 + log(1 - Delta))^beta in place of J^s, c is continuous on H_beta = ||J^2 Q_beta h||_2 and on
the weighted completion of E_R(Q_beta h) exactly when beta > 1/2. In H_beta its norm is D_beta^(1/2)/(8 pi^(1/2)),
D_beta = 1/(2 beta - 1) - e Gamma(1 - 2 beta, 1) (below 1/18 at beta = 1). In the weighted norm,
(2 beta - 1)^(1/2) C_R^log(beta) -> 1/(8 pi^(1/2)) uniformly in R >= 1. At beta <= 1/2, c is unbounded even with
b = 0. The space controls no positive gradient Hoelder exponent. The inverse and the nonlinear theorem have since
been transferred to it (next paragraph). The low residual obstruction does transfer (P71): for 0 < beta <= 1,
L_R(Q_beta^(-1) g) <= (1 + D_R) L_R(g) with D_R = 41/(5R) + 34/R^2 + 218/R^3 + 3696/(5R^4) + 1584/R^5 < 2^-27 for
R >= 2^31, so N^log_(beta,R)(h) >= 2^(53/2) L_R(h)/(1 + D_R). With the annular witnesses of P51 and P52 the residual
of state 131 has logarithmic norm above 35350194988431047182367358 for R >= 2^31 (152106025684049937879446804 for
R >= 2^32, 12111707931248526899493046278 for R >= 2^35), and the refits Mpen2 and d2 above 1935892101 and
1936535199 for R >= 2^31, uniformly in 0 < beta <= 1. These bounds are extended-norm statements and do not assume
membership of the residuals in the completion.

Logarithmic conditional theorem (THEOREM; S1_PROOFS.md, P72 to P87). Fix R = 2^31, 1/2 < beta <= 1,
epsilon = 2 beta - 1, and for tau > 0 put Q_tau = (1 + tau log(1 - Delta))^beta. The circular cutoff of the strain at
radius eps equals the average of the field C h = d_y U_2[h] + (1/4) d_y h over the disc of radius eps against the
probability density 2(1 - r^2/eps^2)_+/(pi eps^2); since C h(0) = c[h] + h_y(0)/4, the principal value is literal on
the completion (P72); at beta <= 1/2 an explicit
compact C^1 density with Dh(0) = 0 lies in every such space and its circular strain integrals diverge like
log log log(1/eps) (P74). Under hypotheses (W0) to (W3) of section 7a at R = 2^31, with the decay bounds in their
d = 4/9 version and the position-dependent low floor, written out in P77 and P85 (the matrix bounds M_low >= (2/5 + (11/5) c r^2/(R^2 + r^2)) I on r <= R and M_1, M_2 >= I/2, the
decay bounds with d = 4/9 and constants 186, 22, 22, 56, the eight derivative bounds of Theorem D_w, polynomial
growth of every reference derivative, and a nonzero leading profile: T^(-1/c) rho(TX) -> r^(1/c) Theta(theta)
uniformly on compact annuli as T -> infinity, Theta continuous and not identically zero), the following hold.
(i) Fixed background (P75, P77): for tau = 2^-20 and every 0 < beta <= 1, the maximal realization of
A_fix h = (cX + u).Dh - h + U[h].D rho on N_tau = E^w(Q_tau .) decays at rate 1/29 and has inverse at most 29; N_tau and
N_beta = E^w((1 + log(1 - Delta))^beta .) define the same space with N_tau <= (29/7) N_beta and
N_beta <= (2 tau^-beta + 16) N_tau; for 1/2 <= beta <= 1 the inverse is below 2^(8 + 20 beta) in N_beta; for
beta > 1/2 the normalized operator B h = A_fix h - c[h] X.D rho has domain D(A_fix) intersected with ker c and range
{f_y(0) = 0}. (ii) The quadratic term U[h].Dh is not continuous at 0 from the space into itself, even on
{b = c = 0} (P76), so the nonlinear theorem cannot be a contraction in the high norm. (iii) Native norm (P83, P84):
with tau = 2^-24, omega_0 = <r>^(-6/5), omega_1 = <r>^(-1/5), omega_2 = (1 + 4 r^2)^(2/5), w = (1 + r^2/R^2)^(-11/10),
P_j(g) = ||omega_j D^j g||_2, L(g) = ||w g||_(Hdot^-1) and M(g)^2 = P_2(Q g)^2 + 2^22 P_1(Q g)^2 + 2^53 L(g)^2, the
fixed operator has decay rate 1/25 - 2^16 tau and inverse 28, and the products and the strain are controlled with
C = tau^-beta epsilon^(-1/2) (P78 to P82, P84). (iv) Nonlinear theorem (P85): for M(k) <= r_0 = 2^-20 tau^beta
epsilon^(1/2) the maximal operator A_k h = (cX + u + U[k]).Dh - h + U[h].D rho generates a semigroup with
||exp(t A_k)|| <= e^(-t/32) and M(A_k^-1 f) <= 32 M(f); the normalized operator has domain D(A_k) intersected with
ker c and, if c[k] = 0, range {f_y(0) = 0} with inverse at most 32; if the residual F has M(F) <= eta = r_0/32, there
is exactly one h with M(h) <= r_0 and c[h] = 0 such that rho + h is an exact solution with the same exponent and
leading angular function, every solution in that ball has c[h] = 0, and the fixed-point map contracts with factor 3/16
in the low metric L. eta <= 2^-37 for every beta; its maximum is 2^-37 (24 e log 2)^(-1/2) = 1.08199e-12 < 1.083e-12,
attained at beta = (1 + 1/(24 log 2))/2 = 0.5300.... (v) Outputs (P87): the
strain has the contact form c[h] = -h_y(0)/4 + int_0^1 a_3(r) dr/r^2 + (1/pi) int_(r >= 1) sin(3 theta) h r^-3 dX,
with a_3 the sin(3 theta) coefficient of h on the circle of radius r; H(h) <= 64 M(h) for the adapted C^(1/2) density
norm H; M_3(h) = int_0^1 |a_3| dr/r^2 <= 6 C M(h); |c[h]| <= 4 C M(h); and L + H + M_3 + |c| <= 2^12 C M(A_k h). The
angular projection is taken before the absolute value; the absolute moment of h - h_y(0) y is not claimed finite.
(vi) Exclusions (P86): N_beta <= 2^32 tau^-beta M, so by the logarithmic distances of P73 the closed M balls of radius
2^25 tau^beta about state 131 and 2^-11 tau^beta about Mpen2 and d2 contain no exact solution of any exponent (at
least 2^45 and 512 times r_0; by P111 even the balls of radius 2^77/(2^20 + 7) > 2^56 and 2^41/(2^20 + 7) > 2^20,
see (vii)), and the native residual floors are M(F) > 35350195123413029343106947 (state 131),
1935892108 (Mpen2) and 1936535207 (d2), more than 2^121 and 2^67 times eta. These are lower bounds of finite norms:
by P106 a smooth S1 function whose derivatives of order m <= 4 are bounded by C_m <r>^(q-m) with q < 1/5 lies in the
completed native space, and the three residuals satisfy this (q = 2 gamma - 1 for state 131, q = gamma - 6 delta < 0 for
Mpen2 and d2). The power 1/5 is sharp (P108): an eventual tail r^q (log r)^(-a) Theta with Theta nonzero lies in the
space for q < 1/5, not for q > 1/5, and at q = 1/5 exactly when a > 1/2; the leading profile direction (q = gamma) is
outside. Hypotheses (2) and (3) of P85 are exactly
the numerical contract of Theorem D_w at R = 2^31, so state 131 satisfies them; what fails is the residual size.
Polynomial growth of every derivative of the reference is a separate qualitative hypothesis; a consolidated
dependency and domain audit (P88) confirms the list and the domains, and shows that the third density derivative
enters the top energy directly, through (16/3) B3 P_0 P_2 with B3 = sup <r>^2 |D^3 rho|. The regularity range
beta > 1/2 is sharp and open within this logarithmic scale (no least admissible beta is attained); no universal
minimal correction space is claimed.
(vii) Parametric form (P89 to P91). Retain every hypothesis above except the three bounds replaced here (in
particular the matrix and decay hypotheses, the five bounds |Du| <= 14/5, |D rho| <= 16, <r>|D^2 u| <= 3,
|D^2 rho| <= 3, <r>|D^2 rho| <= 8, polynomial growth and the leading profile), and replace <r>|D^3 u| <= 16,
<r>^2 |D^3 rho| <= 32, <r>^2 |D^4 rho| <= 512 by arbitrary finite U3, B3, B4. With a = 198 + B3/24, G3 = a^2 + 352,
Astar >= 2048 with 7 Astar^2 >= 200 G3, Kstar = max(525, 432 + (272 U3 + 816 B3)/Astar, 312 + (1088/3) B3 +
(2176/(3 Astar)) B4), 0 < tau <= min(2^-20, 1/(768 Kstar)) and Mstar(h)^2 = P_2(Qh)^2 + Astar^2 P_1(Qh)^2 +
Astar^2 2^31 L(h)^2, every conclusion of (iv) holds in Mstar with the same r_0, eta, inverse 32 and contraction 3/16
(P89; Astar = 2048 suffices for B3 <= 4096). For every parameter choice N_beta <= 2^36 tau^-beta Mstar, so the Mstar
balls of radius 2^21 tau^beta (state 131) and 2^-15 tau^beta (Mpen2, d2) contain no exact solution, and the residual
floors exceed (Astar/2048) 2^119 and (Astar/2048) 2^65 times eta < 2^-35 (P90). These balls are not the largest
excluded ones: E_R(h) <= (1 + 7 tau) Mstar(h) for R >= 2^31, Astar >= 2048, 0 < tau <= 2^-20 and 0 <= beta <= 1
(P111, by a positive heat-kernel mixture for Q^-1 with first moment at most pi tau beta), so with the distances
E_R > 2^57 and E_R > 2^21 of P73 the closed Mstar (and M) balls of radius 2^77/(2^20 + 7) > 2^56 about state 131 and
2^41/(2^20 + 7) > 2^20 about Mpen2 and d2 contain no exact solution of any exponent, for every such tau and beta; the
residual floors and thresholds do not change. For a finite potential, exact
rational caps C_6, C_7 give admissible U3 = B3 = 2 C_6, B4 = 2 C_7 and polynomial growth of every derivative (P91):
2^107, 2^107, 2^114 for state 131 and 2^191, 2^191, 2^201 for Mpen2 and d2, whose certified derivative violations are
all of these three kinds, and at these parameters the gaps exceed 2^213 (state 131) and 2^243 (Mpen2, d2). For d2
every other hypothesis on the reference is verified (P105: the source audit gives parity, the finite potential form,
c + c[rho] = 1 and a_0 = 10.2923... > 1; the leading potential is that of state 131; P95 gives M >= (19/5) I, which
implies the low matrix condition since 2/5 + (11/10) c <= 487/200, M_1, M_2 >= I/2, the five fixed bounds and the four
decay bounds; the parameter rule holds exactly, 768 Kstar tau = 0.53125...), so d2 fails only the smallness of its
residual: Mstar(F) > 2^178 * 1936535207 and Mstar(F)/eta > 2^243, and the closed Mstar ball of radius
2^-15 tau^beta about d2 contains no exact solution of any exponent. For Mpen2 the other global hypotheses are not
verified.
(viii) The matrix hypothesis for state 131 now has four certificates: the original 244-leaf Bernstein partition
(M >= 3.80064 I), an independent 48-leaf recomputation (M >= 3.8103 I, P92), a Taylor-box covering of 58640 polar
cells with an origin square and a far-field bound (M >= 3.810156 I, independently audited, P93), and the sharp bound
M >= (c_l + 2) I with lambda_min(M) = c_l + 2 = 3.8103192... only at the origin (P94). Further directed covers
with independent rechecks and no floating-point trigonometric bound give A >= -(1/20) I and
rho_y >= (1 + r^2)^(-delta/2) > 0 on the whole plane, the exterior bounds M >= 4.595633 I and, for the matrices of (B4) to (B6) (not the
weighted principal matrices of (W2)), M_1 >= 0.990775 I, M_2 >= 0.620899 I, M_3 >= -1.194644 I for r >= 10^4 (P99), the decay bounds sup r^(2/5)|D rho| <= 19.94465,
sup r^(2/5)|Du| <= 1.85619, sup r^(-3/5)|u| <= 0.97743 (P104), and the exterior residual bound
|F(X)| <= (48707/200000) |X|^(2 gamma - 1) for |X| >= 300 (P101; an upper bound on a growing residual).
(ix) The auxiliary hypotheses (B4) to (B6) and ||sym DU|| <= 17/20 for state 131 have a second, independent
full-plane certificate from the exact original potential: M_1 >= 0.972875 I, M_2 >= 0.587238 I, M_3 >= -1.230876 I and
||sym DU|| <= 0.810792 (99, 144, 164 and 49 Bernstein leaves at 384 bits, rechecked at 448 bits; P96). In the
logarithmic class the projection onto the third harmonic in the singular moment of (iv) is necessary: the full
absolute moment int_(r<1) r^-3 |h - h_y(0) y| dX is bounded on the scale ||(1 - Delta)(1 + log(1 - Delta))^beta h||_2
exactly for beta > 3/2, and one compactly supported C^1 function with zero jet, strain and third harmonic lies in
these spaces for every beta <= 3/2 and in the native spaces of (iv) but has infinite absolute moment (P97).
(x) Near the center, the exact original state 131 has explicit remainder bounds: on the closed disk r <= 1/10,
|rho_y - a_0| <= 3.04 r^2, |rho_x| <= 1.24 r^2, |Du11 - (c_l - 1)| = |Du22 - (1 - c_l)| <= 0.65 r^2, |Du12| <= 0.59 r^2,
|Du21| <= 0.66 r^2, |u1 - (c_l - 1) x| <= 0.285 r^3 and |u2 - (1 - c_l) y| <= 0.293 r^3, together with the 32 constants of the
numerical work at radii 1/100, 1/50, 1/20 and 1/10 and seven of its rounded displays (exact Taylor division with a rational tail bound,
complete covers at 384 bits rechecked at 448 bits; P98). These local bounds are not used by the conditional theorems.

The fixed sector r^(p_7). Every six-branch refit and repair audited has the same leading residual sector r^(p_7),
p_7 = gamma - 6 delta = -2.1333 (delta = 1 - gamma), with full-circle angular norm 3081.2744... In the generator
family of the refits (branches j <= 5) no generator enters this sector linearly: it consists of the quadratic
interactions of the six prescribed leading branches, so it is an invariant of the family (it is the forcing of the
six stationary sectors at the next order). For Theorem D it is an obstruction (THEOREM; S1_PROOFS.md, P27 and P31): for every
real choice of the coefficients, a Muntz-type distance of the power u^(a_0), u = 1/(1 + r^2), from the span of the
other 1851 allowed powers, together with a bound for the derivative on the cylinder s = log r on that span, gives
||F||_Hdot^-1 > 2.6775e-7 and N_s(F) > 1.3376e-4 at s = 2^-18, more than 210 times 1/1572864 (P27, with the dilation
bound C_D = 202394.39). The sharper cylinder bound of P31.2 (||d_s g||^2 <= Q_n ||g||^2, Q_n = (2n(n^2 + 2) + 1)/3
for n powers, from an orthonormal basis of exponentials that keeps the factor 1 - u) gives ||F||_Hdot^-1 > 1.665e-6
and N_s(F) > 8.32e-4, more than 1308 times the threshold. The same argument with radial degree k <= K (n = 12(2K + 5)
- 8 powers) keeps N_s(F) above the threshold for every K <= 779 (270180 coefficient slots before the affine constraints at K = 779); at K = 780 the
bound no longer decides. A recursive bound for the skew part of the dilation on spans of exponentials
(q_n <= n - 1/2 + log(2n - 1)/8 in place of the square root of Q_n; THEOREM, S1_PROOFS.md, P33) improves this to
||F||_Hdot^-1 > 2.925e-5 and N_s(F) > 0.01461, more than 22986 times the threshold, and to every radial degree
K <= 3675 (1312740 coefficient slots); at K = 3676 it no longer decides. For Theorem D_w the
same structure gives no obstruction (THEOREM; S1_PROOFS.md, P29): a smooth parity function with the same coefficient
of r^(p_7), the same eight vanishing sectors and the same finite power structure has N^w_s < 3.461e-13 < 2^-35 for
0 < s <= 1/2 at R = 2^31. That function is not shown to be the residual of any potential, so a uniform weighted
statement for the family would have to use the nonlinear structure of the residual; it is open. A reference for
either theorem should therefore cancel this sector, which needs a seventh branch (generators of the next far-field
order with the leading data of the seventh stationary profile). With seven branches whose leading potentials are the
first seven stationary orders, the sector r^(p_7) vanishes and the sector of exponent p_8 = gamma - 7 delta = -2.581
is E_7 = 7(c - 1) Theta_8, fixed by those seven orders alone (no descendant coefficient changes it; within this
generator architecture only an eighth branch cancels it), with full-circle angular norm 9679.9655801992743519, more than three times 3081.27 (THEOREM;
S1_PROOFS.md, P32, a finite formal statement checked by two exact reconstructions and a 60-digit Cartesian
differentiation). It is the leading sector only if the descendant sector (2, 1), of exponent
gamma - 2 delta - 2 = -2.343, is also cancelled exactly (a penalty only makes it small). Since -2.343 < -2 that
sector lies in the unweighted residual space, and no theorem forces its exact cancellation for the weighted threshold;
cancelling it is a possible next constraint, not a proved necessity. The bounds of P27 and P31 are
for six branches; for seven branches they must be recomputed with the new set of exponents.

For Theorem D, the following two requirements separate the available references.

1. Membership, (B10m), which by Theorem E is also necessary for an exact solution in the affine class. A residual with a
   nonzero pure-power angular sector r^p Theta(theta) is in H only if p < -2, and in
   L^2 only if p < -1 (borderline logarithmic sectors such as r^-2 (log r)^-1 can lie in H and are treated separately). With the
   exponents p_n = 1 - n(1 - gamma) (p_6 = -1.686, p_7 = -2.133) this needs the far-field expansion
   r^(p_1) Theta_0 + ... + r^(p_6) Theta_5 to be exactly stationary (the sector defects E_1, ..., E_5 vanish; E_1 = 0 is
   already achieved), so that the residual starts at r^(p_7), and no binomial descendant above r^-2 (the checkpoint
   carries descendants at -1.4476 and -1.8952). The stationary angular data Theta_1, ..., Theta_5 are uniquely
   determined by an explicit nonresonant recursion (THEOREM), so this is a construction problem, and it is solved by
   the two tail repairs of section 3 (THEOREM). The cutoff splice at radius R preserves the reference exactly on r < R,
   so it helps only if the reference residual is already small there and the reference is already close to the
   stationary tail at r about R; for state 131 the residual grows like R^(p_2 + 1) in L^2. The algebraic repair is a
   finite rational potential of the canonical form whose residual lies in N_s, but it changes the field at every radius
   beyond the center jets, so its background hypotheses and its residual size must be certified from scratch.
   Membership is therefore not an obstruction of principle.
2. Size. Theorem D(b) needs N_s(R_tilde) <= 6.357e-7 (optimizing s gives 6.53e-7; case (a) needs 3.7e-10). For the
   best exact refit so far (m10: 1200 generators, E_1 = 0 exactly) the certified whole-plane norms are
   ||omega D^2 F||_2 = 5.0099 and ||grad F||_2 = 0.34447 (THEOREM, section 9), while ||F||_2 and ||F||_H are infinite
   (the sector at exponent p_3 = -0.343 remains). Since the symbol of J^s is at least 1, the gradient component alone
   gives N_s(F) >= 128 ||grad J^s F||_2 >= 128 ||grad F||_2 > 44.0926 for every s, a factor of about 6.94e7 above the
   threshold, that is about eight orders of magnitude; the gradient component (weight 2^7) binds before the Hessian.
   This is a diagnostic for that one reference, not a lower bound over other references. The omega-weighted
   Hessian residual of that refit lies mostly in 32 < r < 256 (FLOAT); the residual decreased only slowly with the size
   of the refit family (FLOAT).

What remains, in order: a reference with N_s(R_tilde) <= 6.357e-7, for instance a repaired refit whose residual is that
small on r < R, with certified upper bounds of E and Q in the residual conversion over the whole plane (the exact-integration method of
section 9 applies directly to finite rational potentials; a smooth cutoff splice needs a separate bound on its transition
annulus); and the certificates (B0) to (B9c) for that reference (for the cutoff splice of a certified
reference, the interior certificates transfer and only the exterior needs the direct estimates above; for an algebraic
repair or a new refit every certificate must be redone, which the Bernstein method of S1_NUMERICAL_CERTIFICATES.md does
for any finite rational potential of the canonical form). The
near-origin and mid-field residual levels of the floating-point refits are observations of particular fits, not lower
bounds over their families.
