# the second theory agent to the first theory agent: O3 skeleton in the Hoelder framework, the O2 hypothesis, and the k-norm bookkeeping (v02)

Version: v02. Author agent: the second theory agent. Written 2026-11-02, started 2026-11-02T19:32Z (the completion time is in the last line).
Supersedes: theory_agent_2/notes/T2_TO_T1_v01.md, published SHA256 2c41523f04d53ceb6a0fc1cf6a0dc0122a9132290ace95351325c34947d5e097
(v01 stays frozen). Recipients: the first theory agent (theory publisher), the theory auditor (audit), the coordinator (ledger rows L-O2, L-O3).
Answers: the theory audit exchange audit_v13 (AT-017 to AT-021: "Please revise Proposition E and the heuristic coefficient in a new
version, and review the added exact constrained optimizer"), audit_v14 (AT-022), audit_v15 (AT-024: "Make H1's deformation
norm explicitly operator norm ... Review of these transfer bounds is requested"), the coordinator's team notes 19:12Z item 3.
Consulted in addition to the v01 list: theory_audit/research/{tame_closure_audit, decomposition_scope_audit,
frozen_coefficient_audit, velocity_norm_transfer, tame_weight_constants_audit}/PROOF.md, theory_audit/exchange/audit_v13 to
audit_v18, THEORY_NEW_RESULTS.md v1, PROMPT R5 (optional uniqueness) and R10.2. Arithmetic: theory_agent_2/scratch/o3/
o3_constants.py and o3_exact.py with outputs o3_constants.out and o3_exact.out (FLOAT, binary64).
Companion note (Sobolev ball, new): theory_agent_2/notes/T2_O2S_v01.md, frozen at SHA256 3abc3a8f53b327d3f621bc3cd9a43dbc9a46359dfbbf972d6c2fc08242d63f47.

## Change list against v01

Audited snapshots: 0a56001e... (AT-017 to AT-021) and the published 2c41523f... (AT-022, AT-024).
1. Status labels updated: Lemma S and Lemma W PROVED (AT-017, AT-018, carried by AT-022). Theorem D and THR-D
   CONDITIONAL on OPEN H1, implication CONFIRMED (AT-019, AT-022). Lemma S2 (new) CLAIMED.
2. AT-024: eps(k) is now explicitly the operator norm ||DU[k]||_(inf,op); Lambda(k) uses the registered Frobenius
   seminorm. C_eps = C_I C_U^(1 - theta_I) is then valid by scalar projection (section 1). Review of both transfer
   bounds of theory_audit/research/velocity_norm_transfer: section 11.
3. AT-019 exact constrained optimizer reviewed (section 4, "Exact closure region"; agrees). The K = 0 (c_T = 0) case is
   stated separately, as AT-019 asks.
4. Remark D2 softened to the displayed interpolation argument (AT-020 scope note). Remark D4 (new): the R5.4 contraction
   condition evaluated in the Hoelder ball.
5. Section 3: variants H1_beta and H1' (new) and a flag on the Lambda-dependence of C_tube in R10.2 (new).
6. Section 5 rewritten as Proposition E' with all AT-020 repairs: Q_c includes R and covers alpha + delta > 1; the stronger
   premises on h_0 are explicit (P_E1 to P_E3); H2 no longer asks for S1 of each input f_i; the a_z = 0 case is covered
   by Lemma S2; the weighted-gradient constant is max(1, sigma/2). New: a radial split that makes the leading
   coefficient eta_0 small as R -> 0 at fixed strong norms of h_0 (v01 said it was not R-small).
7. AT-021: the heuristic coefficient is now c_F^+ = int_0^infinity u^(b+1) Fhat(0, u) du, with the exact vertical-ray
   identity; the singularity claim and the cap alpha < 0.3838 stay HEURISTIC.
8. Section 8 (Sobolev alternative) replaced by a pointer to T2_O2S_v01. Its v01 claim that the standard Kato-Ponce
   commutator gives a usable tame bound is withdrawn (the first theory agent NR-4 objection; see T2_O2S_v01 section 4), and its v01 claim
   that a Sobolev analog of R5 must be proved is withdrawn (the coordinator 19:13Z: R5 is IMPORTED, only the ball differs).
Sections 6, 7, 10 change only where these items require it.

Status of this note: Lemma S and Lemma W are PROVED (the theory auditor CONFIRMED). Lemma S2 is CLAIMED. Theorem D and Corollary D1
are CONDITIONAL on H1 (OPEN) and on the IMPORTED R1 to R5, with the implication CONFIRMED. Proposition E' is CONDITIONAL
on H2, H3 (OPEN) and the premises P_E; its implication is CLAIMED. Sections 7 and 8 are HEURISTIC unless marked.
No O2 estimate is proved here: H1 remains the open analytical statement in the Hoelder framework (ledger row L-O2).

## 0. Summary

1. The closure inequality (13.1) follows from one k-uniform tame inverse estimate (H1, "UT-H"):
   H(z) <= C_0 [ N_Y(G) + ||z||_2 + c_T Lambda(k) ||grad z||_inf ] for A_k z = -G, uniformly over normalized k with
   eps(k) = ||DU[k]||_(inf,op) <= eps_0, where Lambda(k) = [DU[k]]_(C^alpha) (Frobenius). At k = 0 the tame term
   vanishes and H1 is exactly the O1 estimate, so O1 and O2 stay separate.
2. With H1, R2.2 and the interpolation R4.2, every T(k), k in K_{R,M}, obeys x <= a + b x^(1 - theta_I),
   x = H(T(k)), theta_I = alpha/(2 + alpha). Lemma S turns this into invariance:
   H(T(k)) <= A_F + eta(R, M) M, A_F = C_0 (Sigma_F + R), eta = K (1 + R/M) R^theta_I M^(1 - theta_I),
   K = C_0 c_T C_U C_I c_w^(1 - theta_I). The needed smallness is eps(k) <= C_eps R^theta_I (R + M)^(1 - theta_I) <= eps_0.
3. Corollary D1 (preferred type: only ||F||_2 small, Sigma_F finite): closure whenever
   (||F||_2/beta_0)^(alpha/2) (Sigma_F + ||F||_2/beta_0) <= tau_*^((2 + alpha)/2) / C_0.
   The exact closure region (with the (D2) cap) is the AT-019 optimizer, reviewed in section 4.
4. The R lever is weak at 007: R^(-alpha/2) = 1.52 at alpha = 1/2, and K_max(1, R(007)) = 0.375 (section 7).
5. Proposition E' (decomposition through R8.1 and R7), repaired: H(T(k)) <= A^dec + eta_dec M with every part of eta_dec
   small as R -> 0 at fixed strong norms of h_0, once w_(sigma') grad h_0 is in C^(1,alpha) for some sigma' > 0 and the
   region |X| <= 2 rho is split off. Its powers of R are weaker than those of Theorem D, so the direct route remains the
   better one quantitatively.
6. The Sobolev-ball route (T2_O2S_v01) reduces O2 there to one weighted tame commutator lemma (KP-W, OPEN) and a
   qualitative step (HS0, OPEN), given Lemma WG (CONFIRMED, AT-029), and gives the closure theorem D-S with the same
   "only ||F||_2 small" structure.

## 1. Setting, notation, constants

- A_k h = W_k.grad h - h + U[h].grad rho_bar, W_k = V + U[k], A_0 = L, T(k) = -A_k^(-1) F (R2, R5.2).
- K_{R,M} as in R5.1 and WORKSPACE_CONTRACTS.md A2.2; H(f) := H_{sigma,alpha}(f) = ||w_sigma f||_(C^(1,alpha)) (NORM-H, sum
  convention), w_sigma = <X>^sigma; R = ||F||_2/beta_0.
- theta_I := alpha/(2 + alpha); alpha = 1/4, 1/2, 3/4 give theta_I = 1/9, 1/5, 3/11 and theta_I/(1 - theta_I) = alpha/2.
- C_I = (1 + 2/alpha) A^theta_I (alpha B_alpha/2)^(1 - theta_I), A = 2/sqrt(pi), B_alpha = 16/(pi (1+alpha)(4+alpha)):
  the scalar R4.2 constant, ||grad f||_inf <= C_I ||f||_2^theta_I [grad f]_alpha^(1 - theta_I). FLOAT: C_I = 1.3837,
  1.3488, 1.3003 for alpha = 1/4, 1/2, 3/4 (AT-018 CONFIRMED the optimization).
- k-quantities, with the matrix-norm convention fixed (AT-024):
      eps(k) := sup_X |DU[k](X)|_op,      Lambda(k) := sup_(X != Y) |DU[k](X) - DU[k](Y)|_F / |X - Y|^alpha.
  IMPORTED R4 (prompt statement only, constant not explicit): ||U[k]||_2 <= ||k||_2 and Lambda(k) <= C_U (R + M) for
  k in K_{R,M}, with C_U registered for the Frobenius seminorm (if R4 is read in the operator seminorm, C_U is
  multiplied by sqrt(2), since |A|_F <= sqrt(2) |A|_op for 2 x 2 matrices).
  Scalar projection (AT-024 transfer (1), reviewed in section 11): for unit vectors e, u, the scalar f = e.U[k] has
  ||f||_2 <= ||k||_2 and [grad f]_alpha <= Lambda(k) (|e^T A| <= |A|_op <= |A|_F), so
  |e^T DU[k](X) u| <= ||grad f||_inf <= C_I R^theta_I Lambda(k)^(1 - theta_I). The sup over e, u is the operator norm:
      eps(k) <= C_eps R^theta_I (R + M)^(1 - theta_I),   C_eps := C_I C_U^(1 - theta_I).                     (E)
- c_w := a constant with [grad f]_(C^alpha) <= c_w H(f); c_w1 := a constant with ||grad f||_inf <= c_w1 H(f).
  Lemma W (PROVED, AT-018): with L1 = ||grad(w_sigma^(-1))||_inf and L2 = sup |D^2(w_sigma^(-1))|_op,
      c_w = max{ 1, L1^alpha + 2^(1-alpha) alpha L1, (2 L1)^(1-alpha) L2^alpha + 2^(1-alpha) (1-alpha) L1 },  c_w1 = max{1, L1}.
  FLOAT: sigma = 7/4: c_w = 2.0462, 1.8541, 1.7612 for alpha = 1/4, 1/2, 3/4; c_w1 = 1.
- Weighted gradient (AT-020; theory_audit/research/tame_weight_constants_audit): ||w_sigma grad f||_inf <= max(1, sigma/2) H(f).
  Proof: with g = w_sigma f, w_sigma grad f = grad g - g grad(log w_sigma) and |grad log w_sigma| = sigma |X|/<X>^2
  <= sigma/2. This, not c_w1, is the constant for weighted sups.
- Interpolation for f in X_{sigma,alpha} (R4.2 plus Lemma W):
      ||grad f||_inf <= C_I c_w^(1 - theta_I) ||f||_2^theta_I H(f)^(1 - theta_I).                       (I)
- Sigma_F := N_Y(F), N_Y the source norm of the O1 theorem registered by the first theory agent; default N_Y(G) = ||G||_2 +
  ||w_sigma G||_(C^(1+alpha+delta)), Sigma_F = ||F||_2 + S_F(alpha, delta, sigma) (NORM-SF).

## 2. Sublevel lemmas

Lemma S (PROVED, AT-017; text unchanged from v01 section 2). Let a > 0, b >= 0, 0 < theta < 1 and f(x) = x - a - b x^(1 - theta).
(i) {x >= 0 : f(x) <= 0} = [0, x*], x* > 0 the unique zero of f. (ii) For M > 0: x* <= M iff a + b M^(1 - theta) <= M.
(iii) max{a, b^(1/theta)} <= x* <= max{2a, (2b)^(1/theta)}. Finiteness of x is essential in every use.

Lemma S2 (several powers, a >= 0; CLAIMED). Let a >= 0, b_1, ..., b_n >= 0, theta_1, ..., theta_n in (0, 1), M > 0, and
let x in [0, infinity) satisfy x <= a + Sum_i b_i x^(1 - theta_i). If a + Sum_i b_i M^(1 - theta_i) <= M, then x <= M.
Proof. Put f(x) = x - a - Sum_i b_i x^(1 - theta_i), continuous on [0, infinity), f(0) = -a <= 0, f(M) >= 0, f(x) <= 0.
If all b_i = 0, then x <= a <= M. Otherwise f'' > 0 on (0, infinity), so f is strictly convex on [0, infinity). If x > M,
put t = M/x in (0, 1); strict convexity gives f(M) < (1 - t) f(0) + t f(x) <= 0, a contradiction. QED.
Lemma S2 contains Lemma S(ii) in the direction used, and it covers a = 0, which AT-020 asked to treat separately.

## 3. The O2 hypothesis H1 (UT-H) and its k = 0 case (O1)

FW-C2-O3skel-v1:H1 (UT-H). There are eps_0 > 0, C_0 >= 1, c_T >= 0 such that for every S1 density k with ell(k) = 0,
H(k) < infinity and eps(k) = ||DU[k]||_(inf,op) <= eps_0, and every S1 source G with N_Y(G) < infinity, the unique L^2
solution z of A_k z = -G (R2) satisfies z in X_{sigma,alpha} and
    H(z) <= C_0 [ N_Y(G) + ||z||_2 + c_T Lambda(k) ||grad z||_inf ].                                   (UT-H)
C_0, c_T may depend on eps_0, alpha, delta, sigma, nu, the background and the radii of the proof, not otherwise on k
(in particular not on Lambda(k) or H(k)). Status: OPEN (ledger row L-O2).

The k = 0 case is O1 (Lambda(0) = 0): H(h) <= C_0 [N_Y(G) + ||h||_2] for L h = -G. H1 for k != 0 is O2, separated
from O1 by (a) one constant for all k with eps(k) <= eps_0 and (b) k entering only through the tame term.
The discussion in v01 section 3 (why the tame term is intrinsic, why the tame factor is the unweighted ||grad z||_inf,
the R11 joint-inverse remark, consistency with AT-010 and AT-011) is unchanged and not repeated here.

Variants (each implies the same closure mechanism with the stated change; all OPEN):
- H1(p) (polynomial Lambda-growth; v01): C_0 replaced by C_0 (1 + Lambda(k)/Lambda_*)^p. Remark D3 says what survives.
- H1_beta (new): the smallness hypothesis eps(k) <= eps_0 replaced by ||DU[k]||_(C^beta) <= eps_0 for some
  0 < beta < alpha (a Schauder-type proof may need the deformation small in C^beta, not only in L^inf). This is still
  R-small on K_{R,M}: [DU[k]]_beta <= (2 eps(k))^(1 - beta/alpha) Lambda(k)^(beta/alpha) (minimum of the two bounds
  2 eps(k) and Lambda(k) |X - Y|^alpha on the difference quotient), so (D2) becomes
  C_eps R^theta_I (R+M)^(1-theta_I) + (2 C_eps R^theta_I (R+M)^(1-theta_I))^(1-beta/alpha) (C_U (R+M))^(beta/alpha) <= eps_0,
  whose left side tends to 0 as R -> 0 at fixed M (power R^(theta_I (1 - beta/alpha))).
- H1' (new): an additional term C_0 c'_T ||k||_(C^(1+delta')) H(z) on the right, 0 < delta' < alpha (high norm of z times
  a low norm of k). On K_{R,M}, ||k||_(C^(1+delta')) <= k_inf + k_1 + (2 k_1)^(1-delta'/alpha) (c_w M)^(delta'/alpha)
  (section 5 notation), which tends to 0 as R -> 0; if C_0 c'_T times this bound is at most 1/2, the term is absorbed
  and Theorem D holds with C_0 replaced by 2 C_0. Terms of the form (high norm of k) x (high norm of z) cannot be
  absorbed and are excluded.

Flag on R10 (new). R10.2 states that C_tube "depends on finite flow time, geometric separation and first-order Hoelder
bounds on the velocity, not on D^2 k". For W_k = V + U[k] the first-order Hoelder bound includes [DU[k]]_alpha =
Lambda(k). So an O2 proof that uses R10 with k-dependent velocity in general produces a C_0 that depends on Lambda(k),
that is H1(p) rather than H1. Remark D3 shows that p < 1 is harmless, p = 1 needs C_0 C_U Sigma_F/Lambda_* < 1 and p > 1
needs Sigma_F small. Any such proof must therefore track the Lambda-dependence of C_tube explicitly (HEURISTIC reading
of the prompt statement; R10 is IMPORTED as a prompt statement only).

## 4. The direct route: Theorem D (CONDITIONAL on H1; implication CONFIRMED, AT-019 and AT-022)

Statement and proof are those of v01 section 4, with eps(k) the operator norm and C_eps from (E):
Let R = ||F||_2/beta_0, M > 0, A_F := C_0 (Sigma_F + R), K := C_0 c_T C_U C_I c_w^(1 - theta_I),
eta(R, M) := K (1 + R/M) R^theta_I M^(1 - theta_I). Assume H1, the background hypotheses of R1, R2, (B0n),
Sigma_F < infinity, and
    (D1)  A_F + eta(R, M) M <= M,        (D2)  C_eps R^theta_I (R + M)^(1 - theta_I) <= eps_0.
Then T(K_{R,M}) is contained in K_{R,M} and H(T(k)) <= A_F + eta(R, M) M (13.1); R5 gives a stationary solution.
(The only change in the proof: step (2) uses (E) for the operator norm.)

Exact closure region (review of the AT-019 optimizer in theory_audit/research/tame_closure_audit; it agrees with the
following independent derivation). For M > a := A_F, (D1) is equivalent to K <= G(M), where
    G(M) := (M - a) / ((R + M) R^theta_I M^(1 - theta_I)).
d log G/dM = 1/(M - a) - 1/(R + M) - (1 - theta_I)/M. Multiplying by M (M - a)(R + M) > 0 gives the quadratic
    (1 - theta_I) M^2 - [theta_I R + (2 - theta_I) a] M - (1 - theta_I) a R = 0,
whose only positive root is
    M* = { theta_I R + (2 - theta_I) a + sqrt( (theta_I R + (2 - theta_I) a)^2 + 4 (1 - theta_I)^2 a R ) } / (2 (1 - theta_I)).
The log-derivative is +infinity at a+, negative for large M (it behaves like -(1 - theta_I)/M), and has the single zero
M*, so G increases on (a, M*] and decreases on [M*, infinity). (D2) is M <= B := (eps_0/(C_eps R^theta_I))^(1/(1 - theta_I)) - R.
Hence, for K > 0: some M satisfies (D1) and (D2) if and only if B > a and K <= G(min{M*, B}). For K = 0 (c_T = 0),
(D1) holds for every M >= a, and closure holds if and only if B >= a, that is C_eps R^theta_I (R + A_F)^(1 - theta_I) <= eps_0.
Asymptotics for R << a: M* = a (2 - theta_I)/(1 - theta_I) + O(R) and
G(M*) = (1 - theta_I)^(1 - theta_I) (2 - theta_I)^(-(2 - theta_I)) a^(-(1 - theta_I)) R^(-theta_I) (1 + o(1)), the v01 kappa_theta.
FLOAT check (scratch/o3/o3_exact.out): at alpha = 1/2, R = 0.188142, G(M*) = 1.104942 (M* = 0.5364), 0.941833 (0.6788),
0.609306 (1.247), 0.375061 (2.376), 0.223725 (4.628), 0.110090 (11.38) for a = 0.18815, 0.25, 0.5, 1, 2, 5; these are
the K_max values of the section 7 table.

Corollary D1 (CONDITIONAL on H1; THR-D CONFIRMED as implication). As v01: with
tau_* := min{ [(2 + 1/C_0) 2^(1-theta_I) K]^(-1), eps_0/(C_eps (2 + 1/C_0)^(1-theta_I)) } (first member +infinity if K = 0),
R^theta_I A_F^(1-theta_I) <= tau_* implies (D1), (D2) at M = 2 A_F, and equivalently
    (||F||_2/beta_0)^(alpha/2) (Sigma_F + ||F||_2/beta_0) <= tau_*^((2+alpha)/2) / C_0.                 (THR-D)

Remark D2 (revised). Within the displayed interpolation argument, eta is of order R^theta_I M^(1-theta_I), not R: the tame
factor ||grad h_k||_inf is controlled only through (I), and the exponent of R4.2 is sharp by scaling for general h in the
Hoelder ball. This does not exclude a linear-in-R coefficient obtained from other joint cancellations of the full inverse.

Remark D3 (Lambda-growth, H1(p)). Unchanged from v01: p < 1 keeps the "only ||F||_2 small" structure with a worse
exponent; p = 1 needs C_0 C_U Sigma_F/Lambda_* < 1; p > 1 needs Sigma_F small.

Remark D4 (new; R5 optional uniqueness evaluated). R5.4 (IMPORTED) gives ||T(k) - T(l)||_2 <= ||grad T(l)||_inf ||k - l||_2/beta_0,
and R5 states that a gradient factor below one gives contraction and uniqueness within the set. Under the conclusion of
Theorem D, T(l) is in K_{R,M}, so by (I) ||grad T(l)||_inf <= C_I c_w^(1-theta_I) R^theta_I M^(1-theta_I). The factor is
below one if C_I c_w^(1-theta_I) R^theta_I M^(1-theta_I) < beta_0. FLOAT, sigma = 7/4: C_I c_w^(1-theta_I) = 2.6148, 2.2103,
1.9625 for alpha = 1/4, 1/2, 3/4; with R = 0.188142 and beta_0 = 2.00215 (HISTORICAL) this means M < 0.9126, 1.3418, 1.9232.
Not needed for existence.

## 5. The decomposition route through R8.1 and R7: Proposition E' (repairs of AT-020)

Write h_k = h_0 + z_k, h_0 = -L^(-1) F, A_k z_k = -G_k, G_k := U[k].grad h_0 (R8.1). Exact identity (R7 form), with
[a, U_i] f := a U_i[f] - U_i[a f]:
    G_k = Sum_i U_i[f_i] + G_c,   f_i := k d_i h_0,   G_c := Sum_i [d_i h_0, U_i] k.
Parities (corrected). k and h_0 are S1 (even in x, odd in y). d_1 h_0 is odd in x and odd in y, so f_1 is odd in x and
even in y; d_2 h_0 is even in both, so f_2 is S1. U_1 flips both parities and U_2 preserves them, so U_1[f_1], U_2[f_2]
and G_c are S1. The input f_1 is not S1, and H2 must not require it.

Radial split (new). Fix a smooth radial chi with 0 <= chi <= 1, chi = 1 on |X| <= 1, chi = 0 on |X| >= 2, and put
chi_rho = chi(./rho), rho >= 1. Split f_i = f_i^n + f_i^f, f_i^n := chi_rho f_i, f_i^f := (1 - chi_rho) f_i (same parities).

FW-C2-O3skel-v1:H2 (UT-H-sp, repaired). Under the assumptions of H1, for sources
G = Sum_j U_(i_j)[g_j] + G_reg (finitely many j), where each g_j is in L^2 cap w_sigma^(-1) C^(1,alpha) and has the parity
for which U_(i_j)[g_j] is S1 (odd-x even-y if i_j = 1, S1 if i_j = 2), and G_reg is S1 with N_Y(G_reg) < infinity, the L^2
solution z of A_k z = -G is in X_{sigma,alpha} and
    H(z) <= C_0 [ C_7 Sum_j (||g_j||_2 + H(g_j)) + N_Y(G_reg) + ||z||_2 + c_T Lambda(k) ||grad z||_inf ].
Status: OPEN (the k-uniform full-operator version of R7.1; R7.1 itself is frozen and IMPORTED as a prompt statement).

FW-C2-O3skel-v1:H3 (COMM). For a = d_i h_0 and all k in K_{R,M}:
N_Y([a, U_i] k) <= C_c ||a||_(X_c) (||k||_2 + ||k||_(C^gamma)), gamma := alpha + delta not an integer, for a specified
weighted norm X_c (at least C^(1+alpha+delta) regularity of a). Status: OPEN. A local one-order gain (R7) is not this
global weighted estimate.

Premises on h_0 (explicit, AT-020; stronger than O1 and not supplied by it):
- P_E1: H_0 := H(h_0) < infinity (O1, that is H1 at k = 0).
- P_E2: h_0 in C^(2,alpha)_loc and D_2 := Sum_i ||w_(sigma') d_i h_0||_(C^(1,alpha)) < infinity for some sigma' > 0.
- P_E3: d_i h_0 in X_c, with H3.

Elementary estimates (CLAIMED; k in K_{R,M}):
- Low norms of k (all tend to 0 as R -> 0 at fixed M): ||grad k||_inf <= k_1 := C_I c_w^(1-theta_I) R^theta_I M^(1-theta_I);
  ||k||_inf <= k_inf := 2 pi^(-1/4) R^(1/2) k_1^(1/2); [k]_alpha <= (2 k_inf)^(1-alpha) k_1^alpha;
  q(R, M) := k_inf + (1 + 2^(1-alpha)) k_1 + (2 k_inf)^(1-alpha) k_1^alpha (coefficient 1 on k_inf, AT-022).
- Commutator input (AT-020 repair): ||k||_2 + ||k||_(C^gamma) <= Q_c(R, M), with
      Q_c = R + k_inf + (2 k_inf)^(1-gamma) k_1^gamma                                   if 0 < gamma < 1,
      Q_c = R + k_inf + k_1 + (2 k_1)^(1-beta/alpha) (c_w M)^(beta/alpha), beta = gamma - 1, if 1 < gamma < 1 + alpha.
  (Second case: |grad k(X) - grad k(Y)| <= min{2 k_1, c_w M |X - Y|^alpha}.)
- Product rule: ||k B||_(C^(1,alpha)) <= ||B||_inf [grad k]_alpha + ||B||_(C^(1,alpha)) q(R, M), and the general algebra bound
  ||a b||_(C^(1,alpha)) <= c_P ||a||_(C^(1,alpha)) ||b||_(C^(1,alpha)) with c_P := 2 + 2^(2-alpha). (Expand grad(ab) and the
  Hoelder seminorm of a grad b + b grad a; use [a]_alpha <= 2^(1-alpha) ||a||_inf^(1-alpha) ||grad a||_inf^alpha.)
- Near part: B_i^n := w_sigma chi_rho d_i h_0 is supported in |X| <= 2 rho, so ||B_i^n||_inf <= <2 rho>^sigma ||d_i h_0||_inf,
  and B^n(rho) := Sum_i ||B_i^n||_(C^(1,alpha)) is finite by P_E2. Hence
  H(f_i^n) <= c_w <2 rho>^sigma ||d_i h_0||_inf M + ||B_i^n||_(C^(1,alpha)) q(R, M).
- Far part: w_sigma f_i^f = [(1 - chi_rho) w_(sigma')^(-1)] [w_(sigma') d_i h_0] [w_sigma k], so
  H(f_i^f) <= c_P^2 e_chi(rho) ||w_(sigma') d_i h_0||_(C^(1,alpha)) M, with e_chi(rho) := ||(1 - chi_rho) w_(sigma')^(-1)||_(C^(1,alpha)).
  e_chi(rho) <= C_(chi,sigma') <rho>^(-sigma') (the function and its first two derivatives are O(<rho>^(-sigma')) on its
  support |X| >= rho).
- L^2 parts: ||f_i^n||_2 + ||f_i^f||_2 <= sqrt(2) ||f_i||_2 <= sqrt(2) ||d_i h_0||_inf R (chi^2 + (1 - chi)^2 <= 1).
- ||z_k||_2 <= r_z := ||grad h_0||_inf R/beta_0 (R8.2, IMPORTED). Tame term: c_T Lambda(k) ||grad z_k||_inf <=
  (K/C_0) (R + M) r_z^theta_I H(z_k)^(1-theta_I) by (I).

Proposition E' (CONDITIONAL on H2, H3, P_E1 to P_E3 and (D2); implication CLAIMED). Put nu_inf := Sum_i ||d_i h_0||_inf and
    A^dec := H_0 + C_0 ( sqrt(2) C_7 nu_inf R + r_z ),
    eta_0(rho) := C_0 C_7 [ c_w <2 rho>^sigma nu_inf + c_P^2 e_chi(rho) D_2 ],
    eta_1(rho; R, M) := (C_0/M) [ C_7 q(R, M) B^n(rho) + C_c Q_c(R, M) Sum_i ||d_i h_0||_(X_c) ],
    eta_2(R, M) := K (1 + R/M) r_z^theta_I M^(1-theta_I).
If A^dec + (eta_0 + eta_1 + eta_2) M <= M for some rho >= 1, then for every k in K_{R,M}:
T(k) in K_{R,M} and H(T(k)) <= A^dec + (eta_0 + eta_1 + eta_2) M, so (R5.3) holds.
Proof. Fix k. (D2) gives eps(k) <= eps_0 by (E). Apply H2 to z_k with the four special inputs f_i^n, f_i^f (i = 1, 2)
and G_reg = G_c, and insert the estimates above: x := H(z_k), finite by H2, satisfies x <= a_z + b_z x^(1-theta_I) with
a_z := A^dec - H_0 + (eta_0 + eta_1) M >= 0 and b_z := K (R + M) r_z^theta_I. Put m := M - H_0. The hypothesis is
a_z + b_z M^(1-theta_I) <= m, so m >= 0. If m = 0, then a_z = b_z = 0 (M > 0) and x <= 0. If m > 0, then
a_z + b_z m^(1-theta_I) <= a_z + b_z M^(1-theta_I) <= m, and Lemma S2 (one power; a_z = 0 allowed) gives x <= m. In both cases
H(T(k)) <= H_0 + x <= H_0 + a_z + b_z M^(1-theta_I) = A^dec + (eta_0 + eta_1 + eta_2) M <= M. The L^2 bound (R2.2), S1
(uniqueness) and ell(T(k)) = 0 (R3.6) follow as in Theorem D. QED.

Assessment (HEURISTIC where stated).
- By (I) and ||h_0||_2 <= R, nu_inf <= 2 C_I c_w^(1-theta_I) R^theta_I H_0^(1-theta_I). For fixed rho, eta_1 -> 0 and the first
  part of eta_0 -> 0 as R -> 0 with H_0, D_2 and the X_c norms bounded; e_chi(rho) -> 0 as rho -> infinity. Choosing
  rho = rho(R) -> infinity slowly enough therefore makes eta_0 + eta_1 + eta_2 -> 0. With rho of order R^(-theta_I/(sigma+sigma'))
  the two parts of eta_0 balance at order R^(theta_I sigma'/(sigma+sigma')), a weaker power than R^theta_I in Theorem D.
  This replaces the v01 statement that eta_0 is not R-small; the price is the premise P_E2.
- eta_2 is the direct eta with R^theta_I replaced by r_z^theta_I = (||grad h_0||_inf/beta_0)^theta_I R^theta_I.
- A^dec contains H_0 = H(h_0) at full size, as A_F contains Sigma_F. The route is useful for a posteriori bounds once h_0 is
  computed (the second numerics agent target X3) and as a model near the origin; it is not quantitatively better than Theorem D.
- Regularity needed of h_0: C^(2,alpha)_loc with a weighted tail (P_E2) for the special part, and about C^(2+alpha+delta)
  for H3. Origin heuristic (corrected interval, AT-021): on the vertical Fourier ray the IMPORTED R6.1 formula gives exactly
      v^(b+2) hhat_fr(0, v) = int_0^v u^(b+1) Fhat(0, u) du  ->  c_F^+ := int_0^infinity u^(b+1) Fhat(0, u) du
                                                             = int_(-infinity)^infinity e^(-(b+2) s) Fhat(0, e^(-s)) ds   (v -> infinity)
  for the frozen solution (the v01 interval [0, infinity) in s was wrong; AT-021 gives a smooth S1 source with F_y(0) = 0
  for which the v01 coefficient vanishes and c_F^+ does not). If c_F^+ != 0 and the fixed-angle decay
  |hhat(xi)| ~ |c_F^+| |xi|^(-(b+2)) |sin phi|^(a_0/d - b - 2) holds uniformly on cones (not shown), the frozen solution has a
  degree-b singularity at the origin, is C^b and not better, and H3 then needs 2 + alpha + delta <= b; with
  delta > alpha/(b - 1) this forces alpha < (b - 1)(b - 2)/b = 0.3838 (b = 2.6206). P_E2 needs only 2 + alpha < b,
  that is alpha < 0.6206. Whether c_F^+ != 0 for 007, and whether the full h_0 inherits the frozen singularity, are OPEN;
  the cap is HEURISTIC and is not a theorem hypothesis.

## 6. Which norm of k each estimate uses (AT-010 directive; O1 and O2 separated)

| step | estimate | norm of k used | where it comes from |
|---|---|---|---|
| L^2 bound of T(k) | ||h_k||_2 <= R | none (R1.2 holds for all regular k) | R1.2, R2.2 IMPORTED |
| existence of T(k) | flow of W_k | eps(k) < infinity, U[k] bounded | R2 IMPORTED |
| L^2 bound of z_k | ||z_k||_2 <= ||grad h_0||_inf ||k||_2/beta_0 | ||k||_2 | R8.2 IMPORTED |
| constant of H1 | eps(k) <= eps_0 | eps(k) = ||DU[k]||_(inf,op) <= C_eps R^theta_I (R+M)^(1-theta_I) | (E): R4 IMPORTED, scalar projection |
| constant of H1_beta | ||DU[k]||_(C^beta) <= eps_0 | eps(k) and Lambda(k) (R-small combination) | section 3 |
| tame term of H1 | c_T Lambda(k) ||grad z||_inf | Lambda(k) = [DU[k]]_(alpha,F) <= C_U (R + M): the high norm M | R4 IMPORTED |
| extra term of H1' | c'_T ||k||_(C^(1+delta')) H(z) | low norm of k (R-small) | section 3 |
| special source (route E') | H(f_i^n), H(f_i^f) | [grad k]_alpha <= c_w M (times R-small or rho-small factors), ||k||_inf, ||grad k||_inf, [k]_alpha | section 5 |
| commutator (route E') | N_Y([d_i h_0, U_i] k) | ||k||_2 + ||k||_(C^gamma) <= Q_c (R-small) | H3 |
| contraction (Remark D4) | ||T(k) - T(l)||_2 | ||k - l||_2 (and M through ||grad T(l)||_inf) | R5.4 IMPORTED |
| normalization | ell(h_k) = 0 | ell(k) = 0 | R3.6 IMPORTED |
| O1 (k = 0) | H(h_0) <= C_0 (Sigma_F + R) | none | H1 at k = 0 (the first theory agent) |

No H^q norm of k (q > 1 + alpha) is used in the Hoelder framework. The high norm H(k) enters only the tame term and, in
route E', the special-source term.

## 7. Quantitative evaluation at Candidate 007 (FLOAT arithmetic on symbolic constants)

Unchanged from v01 section 7 (inputs ||F||_2 = 0.3766893247, now also certified by AN-005: 0.37668932470589426194 <
||F||_2 < 0.37668932470589426195; beta_0 > 2.00215453 HISTORICAL until the numerical auditor's theta cover finishes; R(007) <= 0.188142).
The K_max column is the exact G(M*) of section 4; (D2) adds the cap B, which is symbolic until eps_0, C_eps are known.

| alpha | theta_I | R^theta_I | R^(-alpha/2) | K_max(A_F) at R(007) for A_F = 0.188, 0.25, 0.5, 1, 2, 5 | same at R = 1e-2 (A_F = 1) | R = 1e-4 (A_F = 1) |
|---|---|---|---|---|---|---|
| 1/4 | 0.1111 | 0.8306 | 1.232 | 1.010, 0.843, 0.517, 0.300, 0.169, 0.077 | 0.450 | 0.754 |
| 1/2 | 0.2000 | 0.7160 | 1.518 | 1.105, 0.942, 0.609, 0.375, 0.224, 0.110 | 0.726 | 1.832 |
| 3/4 | 0.2727 | 0.6341 | 1.871 | 1.196, 1.037, 0.701, 0.452, 0.283, 0.149 | 1.079 | 3.805 |

Reading (HEURISTIC, as in v01): at alpha = 1/2, sigma = 7/4, closure at 007 needs C_0 c_T C_U <= K_max/2.21, about 0.17
at A_F = 1, so the direct route is not expected to close at 007 itself. The strong lever is A_F (K_max ~ A_F^(-(1-theta_I))).
The coordinator's figure of merit (19:12Z item 5) is the left side of THR-D.

## 8. Sobolev-ball alternative: see T2_O2S_v01

The v01 section 8 proposal is superseded by theory_agent_2/notes/T2_O2S_v01.md. Main points: the energy norm is the first theory agent's
N(f) = ||<D>^q (W f)||; Lemma GN gives explicit interpolation constants (C_GN = 0.5728 at q = 2.5); the split
U[k] = U_lo[k] + U_hi[k] removes the A_2 restriction for the k-terms; the k-uniform estimate UT-S follows from Lemma WG
(CONFIRMED, AT-029), Lemma KP-W (OPEN) and HS0 (OPEN); Theorem D-S and Corollary D1-S close the Sobolev ball under
"only ||F||_2 small, N(F) finite"; R5 is IMPORTED and only the ball differs. Withdrawn from v01 section 8: (i) the claim that
the standard Kato-Ponce commutator gives a tame bound with N_q(k) ||grad h||_inf usable for closure (with u = W h the
standard bound gives ||grad (W h)||_inf, which is not small when ||h||_2 is small); (ii) the claim that a Sobolev analog
of R5 must be proved.

## 9. Proposed ledger wording and registry entries (for the first theory agent and the coordinator)

- L-O2 (OPEN): FW-C2-O3skel-v1:H1 (UT-H), with eps(k) = ||DU[k]||_(inf,op) and Lambda(k) = [DU[k]]_(alpha,F), explicit
  (eps_0, C_0, c_T), C_0 independent of Lambda(k) and H(k) (or H1(p) with p < 1; or H1_beta, H1'). Alternative L-O2'
  (OPEN): H2 (repaired) plus H3, with P_E1 to P_E3, for route E'. Sobolev form: FW-C2-Hq-v1:HS1 (T2_O2S_v01).
- L-O3 (CONDITIONAL on L-O1, L-O2; Theorem D CONFIRMED as implication): (D1) C_0 (Sigma_F + R) + K (R + M) R^theta_I M^(1-theta_I) <= M
  and (D2) C_eps R^theta_I (R + M)^(1-theta_I) <= eps_0 for some M > 0; exact test: B > a and K <= G(min{M*, B}) (section 4);
  sufficient: THR-D.
- Constants block: theta_I, C_I, c_w, c_w1 (Lemma W), max(1, sigma/2) (weighted gradient), C_U (R4, Frobenius,
  symbolic), C_eps = C_I C_U^(1-theta_I) (operator norm), C_0, c_T, eps_0 (symbolic), K, M*, B, K_max table, c_P = 2 + 2^(2-alpha).
- Hypothesis registry: H4 := (B0n) and Sigma_F < infinity; P_E1 to P_E3 for route E'.

## 10. Source status (for EXISTING_PROOFS_REFERENCE.md)

As v01 section 10, plus: R5 optional uniqueness (Remark D4) and R10.2 (flag in section 3) are used as prompt statements.
C_U of R4 still has no explicit value; it must be derived before any Hoelder threshold becomes numerical.

## 11. Reviews requested by the theory auditor

- AT-019 exact constrained optimizer (tame_closure_audit): agrees with the independent derivation in section 4 (same
  quadratic, same root, monotonicity, cap B, K = 0 case). No correction.
- AT-024 transfer bounds (velocity_norm_transfer): (1) operator norm by scalar projection: correct; it needs only
  ||e.U[k]||_2 <= ||k||_2 and [grad(e.U[k])]_alpha <= Lambda(k), both valid in either seminorm convention since
  |e^T A| <= |A|_op <= |A|_F. (2) Frobenius sup norm: applying the scalar bound to the two rows and using
  L_1^(2 theta) + L_2^(2 theta) <= 2^(1-theta) (L_1^2 + L_2^2)^theta (concavity of t -> t^theta) gives the factor
  2^((1-theta)/2): correct. Whether the factor can be removed is not decided by this argument. In the Fourier-L^1 route of
  T2_O2S_v01 the question does not arise, since each Fourier mode of DU[k] is a rank-one matrix whose operator and
  Frobenius norms agree.
- AT-003, AT-010/011 and AT-016 (earlier self-audits offered for Opus review): not yet reviewed; planned for the next cycle.

## 12. Next steps of the second theory agent

1. Complete proofs of Lemma KP-W and HS0 (T2_O2S_v01), so that UT-S becomes CLAIMED; then Theorem D-S closes given
   O1-Hq data. An independent referee answer on KP-W is pending (the external referee t2-kpw1).
2. Toward H1 near the origin (R7 angular zero, R11 triangular form), with the R10.2 Lambda-dependence tracked.
3. Explicit C_U (R4) and c_W (multiplier norm of W^(-1) on H^q), so that the thresholds become numerical.
4. Reviews of AT-003, AT-010/011, AT-016.

Completed: 2026-11-02T19:32Z (numbers checked against scratch/o3/o3_constants.out and o3_exact.out).
