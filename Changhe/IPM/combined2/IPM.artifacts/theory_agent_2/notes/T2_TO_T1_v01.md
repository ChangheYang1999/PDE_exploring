# the second theory agent to the first theory agent: O3 skeleton in the Hoelder framework, the O2 hypothesis, and the k-norm bookkeeping (v01)

Version: v01. Author agent: the second theory agent. Written 2026-11-02, started 18:48Z (the completion time is in the last line).
Recipients: the first theory agent (theory publisher, for theory_v01), the theory auditor (audit), the coordinator (ledger rows L-O2, L-O3).
Answers: the coordinator's team notes 18:16Z item 4 (O3 skeleton with eta explicit in R, M, ||grad U[k]||_inf,
[grad U[k]]_alpha) and 18:29Z item 4 (AT-010: keep O1 and O2 separate, state which norm of k each estimate uses).
Consulted: theory_agent_2/PROMPT.md (R1 to R11, sections 13, 14), WORKSPACE_CONTRACTS.md v02, the coordinator team notes
(18:16Z to 18:29Z), JOINT_CLOSURE_LEDGER.md v00, theory_audit/exchange/audit_v08.md (AT-010) and audit_v09.md
(AT-011), theory_audit/research/sobolev_transport_scope/PROOF.md (statement), theory_audit/research/weighted_sobolev_transport_scope/PROOF.md,
source/IPM/combined1/combined1.report.md (lines 18 to 24, 1360 to 1366, 1460 to 1466), the first theory agent work log (18:22Z
to 18:52Z), the second numerics agent status file (18:44Z), source/c1_full/combined1_theory_agent_4/research/{l2_closure, principal_energy_obstruction,
origin_regularity_obstruction, sharp_kernel_audit}/PROOF.md (combined1 T4-019, T4-047). Arithmetic: theory_agent_2/scratch/o3/o3_constants.py, output
theory_agent_2/scratch/o3/o3_constants.out (FLOAT, binary64, rerun 2026-11-02T18:52Z).
Framework ID proposed for registration by the first theory agent: FW-C2-O3skel-v1 (hypotheses FW-C2-O3skel-v1:H1 to H4 below).

Status of this note: Lemma S and Lemma W are CLAIMED (complete elementary proofs below, audit pending).
Theorem D and Corollary D1 are CONDITIONAL on H1 (UT-H) and on the IMPORTED R1 to R5; their proofs are complete
given H1. Proposition E is CONDITIONAL on H2 (UT-H-sp), H3 (COMM) and O1. Everything in sections 7 and 8 is
HEURISTIC unless marked otherwise. No O2 estimate is proved here: H1 is the precise analytical statement that
remains open (ledger row L-O2).

## 0. Summary

1. The closure inequality (13.1) follows from one k-uniform tame inverse estimate (H1, "UT-H"):
   H(z) <= C_0 [ N_Y(G) + ||z||_2 + c_T Lambda(k) ||grad z||_inf ] for A_k z = -G, uniformly over normalized
   k with eps(k) = ||DU[k]||_inf <= eps_0, where Lambda(k) = [DU[k]]_(C^alpha). At k = 0 the tame term vanishes
   and H1 is exactly the O1 estimate, so O1 and O2 stay separate: O2 is "H1 for k != 0 with C_0 independent of k".
2. With H1, R2.2 and the interpolation R4.2, every T(k), k in K_{R,M}, obeys x <= a + b x^(1 - theta_I) with
   x = H(T(k)), theta_I = alpha/(2 + alpha). A convexity lemma (Lemma S) turns this into invariance. Result:
   H(T(k)) <= A_F + eta(R, M) M with
       A_F = C_0 (Sigma_F + R),   eta(R, M) = K (1 + R/M) R^theta_I M^(1 - theta_I),
       K = C_0 c_T C_U C_I c_w^(1 - theta_I),
   and eta(R, M) -> 0 as R -> 0 for fixed M. The required smallness of ||grad U[k]||_inf (H1) is
   eps(k) <= C_eps R^theta_I (R + M)^(1 - theta_I) <= eps_0.
3. This gives a theorem of the preferred type (only ||F||_2 small, Sigma_F finite): closure holds whenever
   (||F||_2/beta_0)^(alpha/2) (Sigma_F + ||F||_2/beta_0) <= tau_*^((2 + alpha)/2) / C_0  (Corollary D1).
4. Quantitatively the R lever is weak. At R(007) <= 0.18814 and alpha = 1/2 the R-smallness is worth a factor
   R^(-alpha/2) = 1.52 on the admissible A_F, and closure needs K <= K_max(A_F, R) with K_max(1, R(007)) = 0.375
   (table in section 7). K_max grows only like R^(-theta_I) = R^(-1/5). Lowering the strong quantities A_F
   (Sigma_F, H(h_0)) is a stronger lever (K_max ~ A_F^(-(1 - theta_I))).
5. The decomposition route through R8.1 and R7 gives the form asked for in section 13, second objective:
   H(h_k - h_0) <= eta_dec(R, M; F) M + (M-independent terms), with a leading coefficient
   eta_0 = C_0 C_7 c_w sum_i ||w_sigma d_i h_0||_inf that does not vanish as R -> 0 at fixed F. It does not improve
   the structure of the direct route: the tame term of z_k comes back with R replaced by ||grad h_0||_inf R/beta_0.
   It also needs h_0 in C^(2 + alpha + delta) for the commutator part; the frozen resolvent indicates (HEURISTIC)
   that h_0 is no better than C^b near the origin, b = 2 c_l - 1 = 2.6206, which forces alpha < 0.3838 for that part.
6. Which norm of k enters where (AT-010): section 6. No H^q norm of k is used anywhere. AT-010 and AT-011 do not
   touch H1 (a C^(1,alpha)-level statement), but they show that any O2 proof through an H^q energy must change the
   map domain to a Sobolev ball and prove invariance there (section 8).

## 1. Setting, notation, constants

- A_k h = W_k.grad h - h + U[h].grad rho_bar, W_k = V + U[k], A_0 = L, T(k) = -A_k^(-1) F (R2, R5.2).
- K_{R,M} as in R5.1 and WORKSPACE_CONTRACTS.md A2.2; H(f) := H_{sigma,alpha}(f) = ||w_sigma f||_(C^(1,alpha)) (NORM-H, sum
  convention); R = ||F||_2/beta_0.
- theta_I := alpha/(2 + alpha) (exponent of R4.2). It is written theta_I because theta is already the background
  quantity of R1 (proposed addition to the WORKSPACE_CONTRACTS.md notation table). Values: alpha = 1/4, 1/2, 3/4 give
  theta_I = 1/9, 1/5, 3/11 and theta_I/(1 - theta_I) = alpha/2.
- C_I: the R4.2 constant obtained by optimizing r in R4.1 with A = 2/sqrt(pi), B_alpha = 16/(pi (1+alpha)(4+alpha)):
      C_I = (1 + 2/alpha) A^theta_I (alpha B_alpha/2)^(1 - theta_I).
  FLOAT: C_I = 1.3837, 1.3488, 1.3003 for alpha = 1/4, 1/2, 3/4. (IMPORTED R4.1, optimization elementary.)
- k-quantities (the two quantities the coordinator asked for):
      eps(k) := ||DU[k]||_inf,      Lambda(k) := [DU[k]]_(C^alpha(R^2)).
  IMPORTED R4 (prompt statement only, constants not explicit): ||U[k]||_2 <= ||k||_2 and
      Lambda(k) <= C_U (||k||_2 + H(k)) <= C_U (R + M),
  with C_U = C_{alpha,sigma} of R4. Then R4.2 applied to U[k] gives (this is R4.3 with its constant made explicit
  in terms of C_I and C_U)
      eps(k) <= C_eps R^theta_I (R + M)^(1 - theta_I),   C_eps := C_I C_U^(1 - theta_I).
- c_w := a constant with [grad f]_(C^alpha) <= c_w H(f) for all f; c_w1 := a constant with ||grad f||_inf <= c_w1 H(f).
  Lemma W (CLAIMED). With L1 = ||grad(w_sigma^(-1))||_inf and L2 = sup |D^2(w_sigma^(-1))| (operator norm),
      c_w = max{ 1, L1^alpha + 2^(1-alpha) alpha L1, (2 L1)^(1-alpha) L2^alpha + 2^(1-alpha) (1-alpha) L1 },
      c_w1 = max{1, L1},
  with L1 = sigma (sigma+1)^(-1/2) ((sigma+2)/(sigma+1))^(-(sigma+2)/2) and L2 = sigma (both attained; FLOAT check
  in o3_constants.py). Proof: f = w^(-1) g with g = w f, so grad f = w^(-1) grad g + g grad(w^(-1)); apply the
  product rule for Hoelder seminorms, [phi]_alpha <= osc(phi)^(1-alpha) Lip(phi)^alpha with osc(w^(-1)) <= 1,
  osc(grad w^(-1)) <= 2 L1, and [g]_alpha <= (2||g||_inf)^(1-alpha) ||grad g||_inf^alpha
  <= 2^(1-alpha) ((1-alpha)||g||_inf + alpha ||grad g||_inf). FLOAT values: sigma = 7/4: L1 = 0.58995,
  c_w = 2.0462, 1.8541, 1.7612 for alpha = 1/4, 1/2, 3/4; sigma = 5/4: c_w = 1.5691, 1.3948, 1.2931;
  sigma = 9/4: c_w = 2.4763, 2.2812, 2.2123; c_w1 = 1 in all cases (L1 < 1).
- Interpolation for any f in X_{sigma,alpha} (R4.2 plus Lemma W):
      ||grad f||_inf <= C_I c_w^(1 - theta_I) ||f||_2^theta_I H(f)^(1 - theta_I).                       (I)
- Sigma_F := N_Y(F), where N_Y is the source norm of the O1 theorem that the first theory agent registers (FW-C2-main-v1). For the
  default Y_F = L^2 cap w_sigma^(-1) C^(1+alpha+delta) of section 13 take N_Y(G) = ||G||_2 + ||w_sigma G||_(C^(1+alpha+delta)),
  so Sigma_F = ||F||_2 + S_F(alpha, delta, sigma) (NORM-SF). If the frozen part uses the weight nu <= sigma
  (R6.4), ||w_nu G||_(C^s) <= C_{nu,sigma} ||w_sigma G||_(C^s); the conversion constant is part of C_0.

## 2. Lemma S (sublevel lemma). Status: CLAIMED

Let a > 0, b >= 0, 0 < theta < 1 and f(x) = x - a - b x^(1 - theta) on [0, infinity).
(i) {x >= 0 : f(x) <= 0} = [0, x*], where x* > 0 is the unique zero of f.
(ii) For M > 0: x* <= M if and only if f(M) >= 0, that is, a + b M^(1 - theta) <= M.
(iii) max{a, b^(1/theta)} <= x* <= max{2a, (2b)^(1/theta)}.
Proof. If b = 0, f(x) = x - a and all claims are immediate. If b > 0, f is continuous, f(0) = -a < 0,
f(x) -> infinity, and f''(x) = b theta (1 - theta) x^(-1-theta) > 0 on (0, infinity), so f is strictly convex.
A strictly convex function that is negative at 0 has at most one zero on (0, infinity) and is negative before it
and positive after it (if f(x1) = 0 and x2 > x1, convexity on [0, x2] gives f(x1) < max{f(0), f(x2)}, so f(x2) > 0);
the intermediate value theorem gives existence. This is (i), and (ii) follows. For (iii): f(a) = -b a^(1-theta) <= 0
and f(b^(1/theta)) = -a < 0 give the lower bound; if x > 2a and x > (2b)^(1/theta) then a < x/2 and
b x^(1-theta) = b x^(-theta) x < x/2, so f(x) > 0. QED.

Use: if a quantity x with x < infinity satisfies x <= a + b x^(1 - theta), then x <= x*, hence x <= M whenever
a + b M^(1 - theta) <= M. Finiteness of x is essential (the inequality is empty for x = infinity); this is why H1
contains the qualitative statement z in X_{sigma,alpha}.

## 3. The O2 hypothesis H1 (UT-H) and its k = 0 case (O1)

FW-C2-O3skel-v1:H1 (UT-H; uniform tame weighted Hoelder inverse). There are eps_0 > 0, C_0 >= 1, c_T >= 0 such that
for every S1 density k with ell(k) = 0, H(k) < infinity and eps(k) <= eps_0, and every S1 source G with
N_Y(G) < infinity, the unique L^2 solution z of A_k z = -G (R2) satisfies z in X_{sigma,alpha} and
    H(z) <= C_0 [ N_Y(G) + ||z||_2 + c_T Lambda(k) ||grad z||_inf ].                                   (UT-H)
C_0 and c_T may depend on eps_0, alpha, delta, sigma, nu, the background and the radii of the proof, but not on k
otherwise (in particular not on Lambda(k) or H(k)). Status: OPEN (this is ledger row L-O2).

The k = 0 case. Lambda(0) = 0, so H1 at k = 0 reads H(h) <= C_0 [N_Y(G) + ||h||_2] for L h = -G: this is the O1
estimate (the first theory agent). H1 for k != 0 is the O2 statement. The two are separated by exactly two requirements:
(a) the same constant for all k with eps(k) <= eps_0, and (b) the k-dependence enters only through the tame term.

Why the tame term is intrinsic (HEURISTIC; to be made precise in the O2 proof). Differentiating the transport,
d_j(U[k].grad z) = U[k].grad d_j z + (d_j U[k]).grad z. In the C^alpha estimate of grad z the first term is part of
the transport along W_k; the second has [d_j U[k] . grad z]_alpha <= Lambda(k) ||grad z||_inf + eps(k) [grad z]_alpha.
The eps(k) part is absorbed by eps(k) <= eps_0; the Lambda(k) part cannot be absorbed by a constant independent of
H(k), since C^(1,alpha) solutions of a transport equation with a C^(1,alpha) field are bounded by the Hoelder norm of
the field times the Lipschitz size of the solution (standard tame transport estimates). The same tame form
appears when the weak-direction coordinate of R11 is used, because composition with a C^(1,alpha) map Phi obeys
[grad(z o Phi)]_alpha <= ||DPhi||_inf^(1+alpha) [grad z]_alpha + [DPhi]_alpha ||grad z||_inf, and [DPhi]_alpha is
controlled by Lambda(k) (R11 needs only first-order Hoelder control of the velocity).

Why the tame factor is the unweighted ||grad z||_inf. The weighted sup ||w_sigma grad z||_inf is not small when
||z||_2 is small (interpolation (I) controls only unweighted sups). In the exterior |X| > R_ext the k-terms are
subordinate to the dilation of V, with coefficients decaying like <X>^(-sigma) (1 + log<X>) H(k) (R9), so the tame
term is needed only on a bounded region, where the weight is at most <2 R_ext>^sigma; that factor is put into c_T.
If the proof needs R_ext to grow with H(k), the constants acquire Lambda-dependence; see H1(p) below.

H1 is a joint statement about the full inverse A_k^(-1), as R11 requires: R11 records that the angular Fourier norm of
a transformed source need not stay bounded after the nonlinear coordinate change, so H1 cannot be obtained by estimating
transformed source, transport and Riesz terms separately in that norm. Any proof of H1 must keep the cancellations
among the three terms.

Variant H1(p) (polynomial Lambda-growth). Same as H1 with C_0 replaced by C_0 (1 + Lambda(k)/Lambda_*)^p for some
p >= 0 and Lambda_* > 0. Remark D3 shows what survives for each p.

Consistency with AT-010 and AT-011. H1 is a C^(1,alpha)-level statement; no H^q norm (q > 1 + alpha) of the source
U[k].grad h or of U[k] appears. The AT-010 sequences (||k_n||_2 -> 0, ||DU[k_n]||_inf -> 0, H(k_n) = O(1)) have
Lambda(k_n) = O(1), so H1 allows H(z) to stay of order one along them; H1 is neither contradicted nor implied.

## 4. The direct route: Theorem D (CONDITIONAL on H1 and IMPORTED R1 to R5)

Let R = ||F||_2/beta_0 and M > 0, and put
    A_F := C_0 (Sigma_F + R),     K := C_0 c_T C_U C_I c_w^(1 - theta_I),
    eta(R, M) := K (1 + R/M) R^theta_I M^(1 - theta_I).
Assume H1, the background hypotheses of R1, R2 (beta_0 > 0, W_k globally Lipschitz with linear growth), (B0n) so
that F_y(0) = 0, Sigma_F < infinity, and
    (D1)  A_F + eta(R, M) M <= M,
    (D2)  C_eps R^theta_I (R + M)^(1 - theta_I) <= eps_0.
Then for every k in K_{R,M}: T(k) in K_{R,M} and
    H(T(k)) <= A_F + eta(R, M) M.                                                                       (13.1)
Hence (R5.3) holds and R5 gives a stationary solution rho_bar + h with h in K_{R,M}.

Proof. Fix k in K_{R,M}. (1) U[k] is bounded and Lipschitz (eps(k) < infinity by (D2)), so W_k satisfies the
assumption of R2, and h_k := T(k) is the unique L^2 solution with ||h_k||_2 <= ||F||_2/beta_0 = R (R1.2, R2.2; no
smallness of k is needed there). (2) By R4 and (D2), eps(k) <= C_eps R^theta_I (R+M)^(1-theta_I) <= eps_0, so H1
applies with G = F: h_k in X_{sigma,alpha} and H(h_k) <= C_0 [Sigma_F + R + c_T Lambda(k) ||grad h_k||_inf].
(3) Lambda(k) <= C_U (R + M) (R4) and, by (I), ||grad h_k||_inf <= C_I c_w^(1-theta_I) R^theta_I H(h_k)^(1-theta_I).
So x := H(h_k) < infinity satisfies x <= a + b x^(1-theta_I) with a = A_F, b = K (R + M) R^theta_I.
(4) (D1) is a + b M^(1-theta_I) <= M, so Lemma S(ii) gives x <= M, and then x <= a + b M^(1-theta_I) = A_F + eta M.
(5) S1 symmetry of h_k: the operator and F respect S1 and the L^2 solution is unique. Normalization: h_k is C^1 and
ell(k) = 0, F_y(0) = 0, so ell(h_k) = 0 by R3.6. Hence h_k in K_{R,M}. QED.

Exact closure region. For given (A_F, R), some M satisfies (D1) if and only if K <= K_max(A_F, R), where
    K_max(a, R) := sup_{M > a} (M - a) / ((R + M) R^theta_I M^(1 - theta_I)).
For R << a: K_max(a, R) = kappa_theta a^(-(1-theta_I)) R^(-theta_I) (1 + o(1)), kappa_theta = (1-theta_I)^(1-theta_I)/(2-theta_I)^(2-theta_I),
attained near M = a (2 - theta_I)/(1 - theta_I) (kappa_theta = 0.2904 at alpha = 1/2). (D2) must then hold at the
chosen M.

Corollary D1 (only ||F||_2 small; CONDITIONAL on H1). Put
    tau_* := min{ [ (2 + 1/C_0) 2^(1-theta_I) K ]^(-1),  eps_0 / ( C_eps (2 + 1/C_0)^(1-theta_I) ) }.
If R^theta_I A_F^(1-theta_I) <= tau_*, then M = 2 A_F satisfies (D1) and (D2). Equivalently (theta_I/(1-theta_I) = alpha/2,
1/(1-theta_I) = (2+alpha)/2):
    (||F||_2/beta_0)^(alpha/2) (Sigma_F + ||F||_2/beta_0) <= tau_*^((2+alpha)/2) / C_0.                 (THR-D)
For every finite Sigma_F this holds once ||F||_2 is small enough; for example, if ||F||_2/beta_0 <= Sigma_F it suffices
that ||F||_2 <= beta_0 [ tau_*^((2+alpha)/2) / (2 C_0 Sigma_F) ]^(2/alpha). So the admissible ||F||_2 scales like
Sigma_F^(-2/alpha) (Sigma_F^(-4) at alpha = 1/2).
Proof. R <= A_F/C_0, so R + 2A_F <= (2 + 1/C_0) A_F. Then eta(R, 2A_F) 2A_F = K (R + 2A_F) R^theta_I (2A_F)^(1-theta_I)
<= (2 + 1/C_0) 2^(1-theta_I) K R^theta_I A_F^(1-theta_I) A_F <= A_F, which is (D1) at M = 2A_F; and
C_eps R^theta_I (R + 2A_F)^(1-theta_I) <= C_eps (2 + 1/C_0)^(1-theta_I) R^theta_I A_F^(1-theta_I) <= eps_0. QED.

Remark D2 (what the coordinator's "eta linear in R" would need). eta is of order R^theta_I M^(1-theta_I), not R:
the tame factor ||grad h_k||_inf is controlled only through interpolation. A linear-in-R eta would need an
estimate of ||grad h_k||_inf by ||h_k||_2 alone, which fails for general h in the Hoelder ball (the R4.2 exponent
is sharp by scaling). In the decomposition route the L^2 size of z_k is linear in R (R8.2), but its Lipschitz size
is again only interpolated (section 5).

Remark D3 (Lambda-growth of the constants, H1(p)). With C_0 replaced by C_0 (1 + C_U (R+M)/Lambda_*)^p:
- p < 1: Theorem D survives with (D1) replaced by C_0 (1 + C_U(R+M)/Lambda_*)^p [Sigma_F + R + c_T C_U (R+M) C_I c_w^(1-theta_I) R^theta_I M^(1-theta_I)] <= M.
  For fixed Sigma_F choose M >= M_0(Sigma_F) (of order Sigma_F^(1/(1-p))) so that the Sigma_F part is <= M/2, then R
  small; the "only ||F||_2 small" structure survives, with a worse exponent.
- p = 1: closure additionally needs C_0 C_U Sigma_F / Lambda_* < 1, a smallness condition on the strong norm that
  R -> 0 does not remove.
- p > 1: closure needs Sigma_F small (take M of order C_0 Sigma_F) and R small.
So the decisive requirement on an O2 proof, beyond H1's form, is that its constants grow at most sublinearly in the
high norm of k. This is the precise sense in which the prompt's question (R4, "unresolved implication") matters
for closure.

## 5. The decomposition route through R8.1 and R7 (Proposition E, CONDITIONAL)

Write h_k = h_0 + z_k with h_0 = -L^(-1) F and A_k z_k = -G_k, G_k := U[k].grad h_0 (R8.1).

Splitting of the source (exact identity of R7): with a_i := d_i h_0 and [a, U_i] f := a U_i[f] - U_i[a f],
    G_k = sum_i U_i[f_i] + G_c,   f_i := k d_i h_0,   G_c := sum_i [d_i h_0, U_i] k.
Parities: U_1 flips both parities and d_1 h_0 is odd-odd; U_2 preserves parity and d_2 h_0 is even-even; so every
term is S1.

FW-C2-O3skel-v1:H2 (UT-H-sp; special-source extension of H1). Under the assumptions of H1, for sources
G = sum_i U_i[f_i] + G_reg with f_i in L^2 cap w_sigma^(-1) C^(1,alpha) and N_Y(G_reg) < infinity,
    H(z) <= C_0 [ C_7 sum_i (||f_i||_2 + H(f_i)) + N_Y(G_reg) + ||z||_2 + c_T Lambda(k) ||grad z||_inf ].
This is the k-uniform full-operator version of R7.1 (R7.1 itself is frozen, unweighted, and IMPORTED as prompt
statement only). Status: OPEN.

FW-C2-O3skel-v1:H3 (COMM; commutator gain). N_Y([a, U_i] f) <= C_c ||a||_(X_c) (||f||_2 + ||f||_(C^(alpha+delta)))
for a norm X_c that requires a in C^(1+alpha+delta) with a weight to be fixed. R7 states only that "the commutator
gains one order locally". Status: OPEN (standard commutator calculus is expected to give it; weights to be fixed).

Estimates of the pieces (CLAIMED, elementary; B_i := w_sigma d_i h_0):
- ||f_i||_2 <= ||d_i h_0||_inf R.
- H(f_i) = ||k B_i||_(C^(1,alpha)) <= ||B_i||_inf [grad k]_alpha + ||B_i||_(C^(1,alpha)) q(k), with
  q(k) := ||k||_inf + (1 + 2^(1-alpha)) ||grad k||_inf + [k]_alpha, and [grad k]_alpha <= c_w M. (Expand
  grad(k B) = B grad k + k grad B with the Hoelder product rule; the coefficient of ||k||_inf is
  ||B||_inf + ||grad B||_inf + [grad B]_alpha = ||B||_(C^(1,alpha)), and [B]_alpha <= 2^(1-alpha) ||B||_(C^(1,alpha)).)
- Low norms of k (all tend to 0 as R -> 0 at fixed M): ||grad k||_inf <= k_1 := C_I c_w^(1-theta_I) R^theta_I M^(1-theta_I);
  ||k||_inf <= k_inf := 2 pi^(-1/4) R^(1/2) k_1^(1/2) (ball average plus Lipschitz bound, optimized radius);
  [k]_alpha <= (2 k_inf)^(1-alpha) k_1^alpha. So q(k) <= q(R, M) := k_inf + (1 + 2^(1-alpha)) k_1 + (2 k_inf)^(1-alpha) k_1^alpha.
- ||f||_(C^(alpha+delta)) for f = k is bounded in the same way (for alpha + delta < 1: k_inf + (2 k_inf)^(1-alpha-delta) k_1^(alpha+delta));
  call the resulting bound q_c(R, M).
- ||z_k||_2 <= r_z := ||grad h_0||_inf R / beta_0 (R8.2, IMPORTED, uses only ||k||_2 and ||grad h_0||_inf).
- Tame term: c_T Lambda(k) ||grad z_k||_inf <= (K/C_0) (R + M) r_z^theta_I H(z_k)^(1-theta_I) by (I).

Proposition E (CONDITIONAL on O1 for h_0, H2, H3, (D2)). Put
    A_F^dec := H(h_0) + C_0 ( C_7 sum_i ||d_i h_0||_inf R + r_z ),
    eta_0(F) := C_0 C_7 c_w sum_i ||w_sigma d_i h_0||_inf,
    eta_1(R, M; F) := (C_0/M) [ C_7 q(R, M) sum_i ||B_i||_(C^(1,alpha)) + C_c q_c(R, M) sum_i ||d_i h_0||_(X_c) ],
    eta_2(R, M; F) := K (1 + R/M) r_z^theta_I M^(1-theta_I),
    eta_dec := eta_0 + eta_1 + eta_2.
Then for k in K_{R,M}, H(h_k - h_0) <= x*(a_z, b_z) (Lemma S) with a_z = A_F^dec - H(h_0) + (eta_0 + eta_1) M and
b_z = K (R + M) r_z^theta_I, and if A_F^dec + eta_dec M <= M then H(T(k)) <= A_F^dec + eta_dec(R, M; F) M, so (R5.3) holds.
Proof: as Theorem D, applied to z_k with G = G_k, using the estimates above and H(T(k)) <= H(h_0) + H(z_k); for the
last step put m = M - H(h_0) and note that a_z + b_z M^(1-theta_I) <= m implies a_z + b_z m^(1-theta_I) <= m. QED.

Assessment of the decomposition route (HEURISTIC where stated).
- eta_0 is independent of R and M: it is small only if h_0 is small in the weighted Lipschitz norm,
  sum_i ||w_sigma d_i h_0||_inf < 1/(C_0 C_7 c_w). By O1, ||w_sigma grad h_0||_inf <= c_w1 H(h_0) <= c_w1 C_0 (Sigma_F + R),
  so this is a smallness condition on the strong norm Sigma_F, not removed by R -> 0. (If h_0 has weighted bounds
  with a stronger weight sigma' in (sigma, 5 - 4/c_l], splitting |X| <= rho and |X| > rho makes eta_0 small as R -> 0
  for fixed Sigma_F; HEURISTIC, to be written if this route is pursued.)
- eta_2 has the same form as the direct eta with R^theta_I replaced by r_z^theta_I = (||grad h_0||_inf/beta_0)^theta_I R^theta_I:
  a gain only if ||grad h_0||_inf < beta_0 (about 2 for 007), and only by the power theta_I = 1/5.
- Regularity needed of h_0: w_sigma grad h_0 in C^(1,alpha) (h_0 weighted C^(2,alpha)) for the special part, and
  grad h_0 in C^(1+alpha+delta) (h_0 in C^(2+alpha+delta)) for H3.
  HEURISTIC regularity limit: in R6.1, for |xi| large in a non-horizontal direction the integrand is concentrated at
  t >= log|xi_2|, which gives |hat h(xi)| ~ c_F |xi|^(-(b+2)) |sin phi|^(a_0/d - b - 2) with
  c_F = int_0^infinity e^(-(b+2)s) hat F(0, e^(-s)) ds, generically nonzero (phi the angle from the xi_1 axis;
  a_0/d - b - 2 = 1.742 > 0 for 007). This is a degree-b singularity at the origin: the frozen solution is C^b and
  not better (consistent with H^s only for s < b + 1 = 2 c_l). If the full h_0 has the same origin singularity, H3
  needs 2 + alpha + delta <= b, and with delta > kappa_ang = alpha/(b - 1) this forces
      alpha < (b - 1)(b - 2)/b = 0.3838.
  The direct route and O1 (1 + alpha < b) are not affected. Side remark for O5: the same computation suggests that
  the exact profile is C^b but not C^infinity at the origin unless c_F vanishes; HEURISTIC, not checked.
- Conclusion: the decomposition gives the exact form "H(h_k - h_0) <= eta(R, M; F) M + ..." of section 13, with an
  explicit F-dependence through h_0, but its leading coefficient eta_0 is not R-small. The direct route (Theorem D)
  is structurally better. The decomposition is worth keeping for two uses: a posteriori bounds once h_0 is computed
  (the second numerics agent target X3), and as the model for proving H1 near the origin, where the source U[k].grad h_0 has the R7
  angular zero.

## 6. Which norm of k each estimate uses (AT-010 directive; O1 and O2 separated)

| step | estimate | norm of k used | where it comes from |
|---|---|---|---|
| L^2 bound of T(k) | ||h_k||_2 <= R | none (R1.2 holds for all regular k) | R1.2, R2.2 IMPORTED |
| existence of T(k) | flow of W_k | eps(k) < infinity, U[k] bounded | R2 IMPORTED |
| L^2 bound of z_k | ||z_k||_2 <= ||grad h_0||_inf ||k||_2/beta_0 | ||k||_2 | R8.2 IMPORTED |
| constant of H1 | eps(k) <= eps_0 | eps(k) = ||DU[k]||_inf <= C_eps R^theta_I (R+M)^(1-theta_I) | R4.3 IMPORTED |
| tame term of H1 | c_T Lambda(k) ||grad z||_inf | Lambda(k) = [DU[k]]_alpha <= C_U (R + M): the high norm M | R4 IMPORTED |
| special source (route E) | H(k d_i h_0) | H(k) <= M (leading), plus ||k||_inf, ||grad k||_inf, [k]_alpha (R-small) | R7 form, Lemma W |
| commutator (route E) | N_Y([d_i h_0, U_i] k) | ||k||_2, ||k||_(C^(alpha+delta)) (R-small) | H3 |
| normalization | ell(h_k) = 0 | ell(k) = 0 | R3.6 IMPORTED |
| O1 (k = 0) | H(h_0) <= C_0 (Sigma_F + R) | none | H1 at k = 0 (the first theory agent) |

No H^q norm of k (q > 1 + alpha) is used. The only place where the high norm H(k) enters is the tame term
(and, in route E, the special-source term). This is unavoidable by AT-010 for any estimate of the source in a
norm stronger than C^(1,alpha), and Remark D2 explains why it cannot be replaced by ||k||_2 in the Hoelder setting.

## 7. Quantitative evaluation at Candidate 007 (FLOAT arithmetic on symbolic constants)

Inputs: ||F||_2 = 0.3766893247 (HISTORICAL, combined1 numerical audit 139), beta_0 > 2.00215453 (HISTORICAL), so
R(007) <= 0.188142. Script: scratch/o3/o3_constants.py.

| alpha | theta_I | R^theta_I | R^(-alpha/2) | K_max(A_F) at R(007) for A_F = 0.188, 0.25, 0.5, 1, 2, 5 | same at R = 1e-2 (A_F = 1) | R = 1e-4 (A_F = 1) |
|---|---|---|---|---|---|---|
| 1/4 | 0.1111 | 0.8306 | 1.232 | 1.010, 0.843, 0.517, 0.300, 0.169, 0.077 | 0.450 | 0.754 |
| 1/2 | 0.2000 | 0.7160 | 1.518 | 1.105, 0.942, 0.609, 0.375, 0.224, 0.110 | 0.726 | 1.832 |
| 3/4 | 0.2727 | 0.6341 | 1.871 | 1.196, 1.037, 0.701, 0.452, 0.283, 0.149 | 1.079 | 3.805 |

Reading. Theorem D closes at 007 if and only if K = C_0 c_T C_U C_I c_w^(1-theta_I) <= K_max(A_F, R(007)) (and (D2)).
At alpha = 1/2, sigma = 7/4: C_I c_w^(0.8) = 1.349 x 1.854^0.8 = 2.21, so the inverse and Riesz constants must
satisfy C_0 c_T C_U <= K_max/2.21, about 0.17 at A_F = 1 and 0.50 at the smallest possible A_F = C_0 R (if C_0 = 1).
Since A_F >= C_0 R(007) = 0.188 C_0 and C_U, c_T are not expected below 1, the direct route is not expected to close
at 007 itself (HEURISTIC; it depends on constants not yet derived). The R lever is weak: K_max scales like R^(-theta_I),
so a factor 10 in K_max needs R smaller by 10^(1/theta_I) (10^5 at alpha = 1/2, 10^3.7 at alpha = 3/4). The strong
lever is A_F (K_max ~ A_F^(-(1-theta_I))) and the constants themselves. Larger alpha helps slightly (larger theta_I).
For comparison, the second numerics agent (status file 18:44Z, FLOAT, not audited, runs in progress) reports G0 = ||F||_2 below 0.12 after
basis expansion (E2b, E2c). If beta_0 stays above 2 for those candidates (their (B-L2) screen is logged but not yet
reported), R is about 0.06 and R^theta_I improves from 0.716 to 0.57 at alpha = 1/2: K_max rises by the factor 1.26 at
fixed A_F.

Consequences for the numerical team (ranked; for the first theory agent's T6 section):
1. Most informative single numbers: h_0 = -L^(-1) F for 007 and for the best new candidate (the second numerics agent target X3):
   ||h_0||_2, ||grad h_0||_inf, ||w_sigma grad h_0||_inf, H_{sigma,alpha}(h_0), ||D^2 h_0||_inf and the local behaviour
   of D^2 h_0 near the origin (to test the C^b prediction of section 5). H(h_0) is a lower bound for any M that can
   close, and it decides whether A_F is of order 0.1 or of order 10.
2. S_F components (NORM-SF) at the parameter grid already planned; Sigma_F enters A_F linearly.
3. ||F||_2 (and beta_0) only through R^theta_I: a large relative reduction is needed to matter.
4. A posteriori Newton refinement: replacing rho_bar by rho_bar + h_N (h_N a computed approximation of the correction)
   lowers both ||F||_2 and the strong norm of the new residual, which is the lever that matters most here; it requires
   the new background to keep c_l, (B0n), the exact sector cancellations and the R1/R2 background screens.

## 8. Alternative framework compatible with AT-010: Sobolev map domain (proposal; HEURISTIC/OPEN)

AT-010/AT-011 rule out bounding the H^q energy of U[k].grad h over the Hoelder ball. They do not rule out a framework
whose map domain is a Sobolev ball: K^S_{R,M_q} = {S1, ell(k) = 0, ||k||_2 <= R, N_q(k) <= M_q}, N_q a (weighted)
H^q seminorm with q = 2 + s, alpha <= s < c_l - 1 = 0.8103 (HISTORICAL: combined1 theory audits 060, 091 and 140
restrict contractive H^q energies and semigroup bounds to rate beta <= c_l + 1 - q, conditional on their coefficient
hypotheses; combined1.report.md lines 1362 to 1364, 1462 to 1465). Structure: the Kato-Ponce commutator gives
|<[|D|^q, U[k].grad] h, |D|^q h>| <= C_KP ( eps(k) N_q(h)^2 + N_q(k) ||grad h||_inf N_q(h) ), again tame, and
||grad h||_inf <= C ||h||_2^theta_q N_q(h)^(1-theta_q) with theta_q = s/(2 + s) (same exponent as theta_I with alpha -> s).
So the same Lemma S closure applies, with A_F^S = Sobolev O1 size and eta_S = K_S (1 + R/M_q) R^theta_q M_q^(1-theta_q).
Advantages: no angular loss at the origin (energy methods are coordinate-free; no R6.4, R7, R11 needed for the
inverse), and the first theory agent's BG-q screen (18:40Z, FLOAT) already shows a positive margin c_l + 1 - q - 0.002. Costs: (i) the
map domain changes, so a Sobolev analog of R5 (weak compactness and weak continuity in this ball) must be proved;
it is not IMPORTED; (ii) the C^(1,alpha) regularity of the fixed point then follows from H^(2+s) in C^(1,s) locally plus
R9.4 and R10 (IMPORTED, conditional); (iii) quantitatively the same weak R lever (theta_q = s/(2 + s) < 0.29). combined1's
proved Sobolev closure (HISTORICAL, combined1.report.md lines 21 to 24) used s = 1/5184 and closed only for
X_(s,w)(F) <= 2.1035e-4, a small-ball framework whose k-dependence is non-tame (||DU[k]||_inf bounded through the
H^(1+s) to L^inf embedding with constant 1/(2 sqrt(pi s)), source/c1_full/combined1_theory_agent_4/research/sharp_kernel_audit/PROOF.md); it is not comparable with the present ball of L^2 radius R ~ 0.19.
The Hoelder and Sobolev frameworks share the quantitative bottleneck of section 7: the tame term at R ~ 0.2 with
R^theta of order 0.6 to 0.8. Whether moderate s with a tame Kato-Ponce bound gains enough is OPEN (no estimate made here).

## 9. Proposed ledger wording and registry entries (for the first theory agent and the coordinator)

- L-O2 (OPEN): FW-C2-O3skel-v1:H1 (UT-H) holds with explicit (eps_0, C_0, c_T), for all normalized S1 k with
  ||DU[k]||_inf <= eps_0; C_0 independent of [DU[k]]_alpha and H(k) (or polynomial growth with p < 1, Remark D3).
  Alternative L-O2' (OPEN): H2 (UT-H-sp) plus H3 (COMM), for route E.
- L-O3 (CONDITIONAL on L-O1, L-O2; Theorem D CLAIMED, audit pending): (D1) C_0 (Sigma_F + R) + K (R + M) R^theta_I M^(1-theta_I) <= M
  and (D2) C_eps R^theta_I (R + M)^(1-theta_I) <= eps_0 for some M > 0; sufficient: (THR-D).
- Constants block additions: theta_I, C_I (explicit), c_w and c_w1 (explicit, Lemma W), C_U (R4, symbolic), C_eps,
  C_0, c_T, eps_0 (from O1/O2, symbolic), K, K_max table.
- Hypothesis registry: H4 := (B0n) and Sigma_F < infinity (S_F finite iff sigma <= 5 - 4/c_l, A2.3).

## 10. Source status (for EXISTING_PROOFS_REFERENCE.md)

This note uses R4 (constants A, B_alpha; C_{alpha,sigma} unspecified), R5, R7 (form only), R8.1, R8.2, R9 (form
only) and R11 (qualitative). Per the coordinator's SOURCE_MAP (18:18Z), R4, R5 in its Schauder-Tychonoff form, R7,
R9, R10, R11 and R8.3 have no located source file ("prompt statement only"); R1, R2, R3 and R5.4 are located in a
Sobolev framework (combined1 l2_closure). In particular C_U of R4 has no explicit value anywhere: it is one of the
constants that must be derived (a Hoelder-Riesz bound with an L^2 low-frequency part) before any threshold here
becomes numerical.

## 11. Next steps of the second theory agent

1. Toward H1 near the origin: combine the R7 angular zero of the special source with the R11 triangular form, to see
   whether a tame estimate with C_0 independent of Lambda(k) is plausible (or a lower-bound example showing growth).
2. A lower-bound example for the tame term (is the factor Lambda(k) ||grad z||_inf necessary?), using AT-010-type
   sequences near the y axis, where W_1 = 0 and the stationary transport does not average horizontal oscillations.
3. Explicit C_U (R4) with the L^2 low-frequency part, so that K becomes numerical given C_0, c_T.
4. Send Lemma S, Lemma W and Theorem D to the theory auditor for audit; an the external referee referee check of the same.

Completed: 2026-11-02T18:53Z (numbers checked against scratch/o3/o3_constants.out).
