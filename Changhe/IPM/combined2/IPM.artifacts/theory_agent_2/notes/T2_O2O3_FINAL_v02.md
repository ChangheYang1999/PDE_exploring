# T2_O2O3_FINAL_v02: the O2 and O3 results of the second theory agent in final form, with exact hypotheses, constants and audit status

Agent the second theory agent (O2, the uniform small-k lifting; O3, the invariant-ball closure (13.1)). Written 2026-11-03 from 20:50Z
(the freeze time is in the last line). Version v02 is v01 (frozen 21:08:46Z, SHA256
7130dcc8fdc3c5412305773e66efef1973c2ed7decf5246f0742e46fec8d88e1) with the errata of section 8 applied: E1 restricts
the explicit results to q = 21/10 (the theory auditor AT-1577), E2 adds the route F-a S input of notes/T2_FAR_CSW_v01.md. Recipients: the first theory agent (THEORY_NEW_RESULTS, which points to the second theory agent only through
NR-4), the coordinator (Part VII reports, ledger rows O2 and O3), the theory auditor (scope check of the restatements; no new proof is
claimed here). Paths of the second theory agent files are relative to the agent directory theory_agent_2/; files of other agents are given as
<agent>/<path>.

Labels. CONFIRMED means confirmed by the theory auditor with the cited AT number; CLAIMED means proved by the second theory agent
and not yet audited; FLOAT is a sampled value; HEURISTIC is orientation only; OPEN is open. This note restates
audited results; its only new items are elementary arithmetic remarks, labeled CLAIMED. Where the restatement
differs in wording from the audited source, the source governs.

## 0. Answer to the task

The task asks for a uniform small-k lifting and the invariant-ball closure (13.1) with explicit dependence on R, M
and F, preferably a theorem that needs only ||F||_2 small with a strong source norm finite, and otherwise the
sharpest quantitative tradeoff. The final state is as follows.

1. A theorem of the preferred type exists, in qualitative form (Theorem A, section 3.1; CONFIRMED as a conditional
   implication, AT-036, AT-058, AT-059, AT-037). The strong norm is N(F) = ||J^q (W F)||_2. Under the background
   hypotheses (H-S), every real S1 source F with F_y(0) = 0 and N(F) finite has a stationary fixed point in a
   weighted H^q ball as soon as (||F||_2/beta_0)^((q-2)/2) (N(F)/beta_b + (C_eps/beta_b)^(1/2) ||F||_2/beta_0) <=
   tau_S^(q/2), with beta_b = (beta - eps)/2. The admissible ||F||_2 scales like N(F)^(-2/(q-2)), that is
   N(F)^(-20) at q = 21/10. The constants C_eps (Lemma WG, AT-029) and c_1 to c_4 (Lemma KP-W) are finite but not
   numerical. So Theorem A cannot be evaluated at Candidate 007 or at any corrected center.
2. The explicit route is route Q at q = 21/10 (Theorem B, section 3.2; Corollary HF-Q-CE, CONFIRMED as a conditional
   implication, AT-273, with its P-S1 transfer AT-306). All of its k-dependent constants are numerical. It has a floor: its loss
   satisfies L_B(R, K) > lambda_1 K for every R > 0, so eta(R, M) in (13.1) does not tend to 0 as R -> 0. It
   therefore needs N(F) itself to be small. Its sharpest tradeoff is the capacity curve, with the ceiling
   N(F) < b0^2/(4 lambda_1) at every R (Proposition CEIL, CONFIRMED, AT-274; Proposition NEC, CONFIRMED, AT-307):
   0.428139284822 b0^2 at P-S2 and 0.390028619649 b0^2 at P-S1 (upper decimals; the 6-digit 0.428139 is not an
   upper bound, AT-274). Every admissible b0 is at most c + 1 - q = 0.7103192101999... (AT-211). By AT-274 no better
   bound on ||D^q k||_2 can raise the ceiling; only sharper constants in the two K-linear terms of L_B can.
3. Route Q needs one more input that is not numerical yet: the base weak-energy constant C0 = C^opt(b0) at k = 0
   (hypothesis H4). At the chain center C2-N1-013, with the certified N_(21/10)(F_*) <= 0.0055545729030073655758
   (AT-1431) and ||F_*||_2 <= 7.961206656880281e-7 (AT-1413), the scalar test holds for every C0 below an allowance
   D > 1.61e11 at b0 = 0.60 and D > 1.22e11 at b0 = 0.55 (at beta_0 = 7/4 stipulated; AT-831). The N(F)
   part of the test is therefore far from binding at 013. What is missing there is a certified C^opt(b0) <= D (item G3: near and far
   charges), a certified background rate (item B) and the actual-generator hypotheses (item G2). On the far side of
   the split erflog 8, rho 1 the remaining row C2 has no route that fits before the stop (notes/T2_FAR_C2_PLAN_v01.md).
4. An explicit theorem of the preferred type needs an explicit weak constant: C_eps and c_1 to c_4 in Theorem A, or
   Cbar in the sharper Theorem A' (AT-114). This is the target (W-REM) of notes/T2_BUD_v01.md section 5
   (see notes/T2_X4_v01.md section 6). It is OPEN.

No complete existence theorem follows from this agent's results. The first unresolved condition stays O3.

## 1. Setting

- Background rho_bar, real, S1 and smooth, with v = U[rho_bar], V = c X + v, div v = 0, v(0) = 0, and
  (BG-reg; gamma_*): |D^j grad rho_bar(X)| + |D^j Dv(X)| <= C_j <X>^(-gamma_* - |j|) for every multi-index j.
  c = c_l is the campaign constant 4076476460239181/2251799813685248 (not varied).
- A_k h = (V + U[k]).grad h - h + U[h].grad rho_bar; L = A_0; T(k) = -A_k^(-1) F; U[f] = (-R_1 R_2 f, R_1^2 f)
  (PROMPT.md (1.2)); S1 means even in x and odd in y.
- (B-L2): the IMPORTED R1/R2 L^2 generator and inverse with signed gap beta_0 > 0, so ||A_k^(-1) G||_2 <=
  ||G||_2/beta_0 whenever R1.2 and R2 apply to V + U[k]. R = ||F||_2/beta_0.
- (R3/R5): the IMPORTED R3 normalization hypotheses (normalized background, a0 > 0) and F real S1 with F_y(0) = 0;
  ell(f) = d_y U_2[f](0).
  The R5 Schauder-Tychonoff mechanism is IMPORTED; its Hilbert-ball form is Proposition R5-S (AT-037).
- Weight and norm: W = (1 + |X|^2/r0^2)^(sigma/2), J = (1 - Delta)^(1/2), N(f) = ||J^q (W f)||_2,
  theta = (q - 2)/q, theta_0 = (q - 1)/q. Range of q (erratum E1): the qualitative results of sections 2.1 to 2.3,
  2.6, 3.1 and 3.1' hold for 2 < q < 3 under their stated hypotheses. The explicit results of sections 2.4, 2.5,
  3.2, 3.3, 3.4 and 4 are stated and audited at q = 21/10 only (AT-234, AT-237, AT-272 to AT-274, AT-306 to
  AT-308); the setting 2 < q < 3 does not extend them (AT-1577). Tuples: P-S2 = (q, sigma, r0) = (21/10, 7/5, 1) and
  P-S1 = (21/10, 1, 1/2). At q = 21/10, theta = 1/21 and theta_0 = 11/21.
- Ball: K(R, M) = {k real S1 : ell(k) = 0, ||k||_2 <= R, N(k) <= M}.
- Frozen matrix: N_q^(k)(X) = q Sym D(V + U[k])(X) + Kmat(X) - (c + 1 + (V + U[k]).grad log W(X)) I, with
  Kmat = [[-rho_y, rho_x/2], [rho_x/2, 0]] (as in notes/T2_O2S_v02.md section 8). (BG-q; q, sigma, r0, beta):
  lambda_max N_q^(0)(X) <= -beta < 0 for every X.
- Source: real S1, F_y(0) = 0, N(F) < infinity. For Candidate 007, N(F) is finite for sigma < 4 - 4/c = 1.7904449
  at every finite q (AT-048).

## 2. O2: the uniform small-k lifting

2.1 Lemma KP-W (research/kpw/PROOF.md; CONFIRMED, AT-049 to AT-051). For real k and u with W k in H^q and u in
H^q, the transport commutator in energy form obeys
    |Re (J^q [W (U[k].grad h)], J^q u)| <= (c_1 eps(k) + c_2 ||k||_2 + c_3 ||U[k]||_inf) N(h)^2 + c_4 N(k) A(h) N(h),
with h = W^(-1) u, eps(k) = ||DU[k]||_(inf,op), A(h) = ||grad h||_inf + ||h||_inf. The constants depend only on
(q, sigma, r0) and two fixed cutoffs; they are finite and not numerical. c_1 >= q is necessary for this global
form (AT-063). The sharp value c_1 = q is OPEN (AT-050). A literal L^2 pairing under the stated data regularity is
REFUTED (AT-051); only the energy form is used.

2.2 Theorem T2-HS1r (notes/T2_O2S_v02.md section 4; CONFIRMED, AT-058). Assume (BG-reg), R1/R2, (BG-q; q, sigma,
r0, beta) with 0 <= sigma < 1 + gamma_*, and 0 < eps < beta. If k is real S1 with N(k) finite and
kappa(k) = c_1 eps(k) + c_2 ||k||_2 + c_3 ||U[k]||_inf < beta - eps, then for every real S1 G with N(G) finite the
L^2 solution z of A_k z = -G has N(z) finite and
    beta_k N(z) <= N(G) + c_4 N(k) A(z) + (beta_k C_eps)^(1/2) ||z||_2,    beta_k = beta - eps - kappa(k).
The unrestricted version HS0 (no condition on kappa(k)) is OPEN.

2.3 Theorem WG-K / UT-K and the gradient-only estimate (notes/T2_WGK_v01.md; CONFIRMED, AT-065, AT-066, AT-069;
the theory auditor research/sharp_full_garding/PROOF.md, CONFIRMED, AT-114). Fix a reference ball
Kbar = {k real S1 : ||k||_2 <= Rbar, N(k) <= Mbar} (no ell constraint) and put
betaK = -sup over k in Kbar and X of lambda_max N_q^(k)(X); assume betaK > 0. For every 0 < eps < betaK and
delta0 > 0 there is a finite Cbar = C(eps, delta0, Rbar, Mbar), uniform on Kbar, with
    Re (J^q [W A_k W^(-1) u], J^q u) <= -(betaK - eps) ||J^q u||_2^2 + Cbar ||h||_2^2
                                        + (1 + delta0) N(k) ||grad h||_inf ||J^q u||_2,            (1)
and for every k in Kbar and real S1 G with N(G) finite, z = -A_k^(-1) G satisfies, with b = betaK - eps,
    b N(z) <= N(G) + (1 + delta0) N(k) ||grad z||_inf + (b Cbar)^(1/2) ||z||_2,   ||z||_2 <= ||G||_2/beta_0.   (2)
Cbar is not numerical. betaK <= beta can fail for an arbitrary certified lower beta (AT-069 REFUTES that
comparison); betaK is the margin of the actual perturbed matrix on Kbar.

2.4 Theorem HF-Q at q = 21/10 (notes/T2_CEPS_v02.md section 3; CONFIRMED with exact constants, AT-234, AT-237;
general weight HF-Q-G with sigma > 0 and r0 > 0, notes/T2_PS1_v01.md section 2, CONFIRMED, AT-306). The coefficient
53/100 comes from the scalar bound H_q(t) = t^q - t^(-q) - q (t - t^(-1)) <= (53/50)(t - 1)^q for t >= 1, which is
proved at q = 21/10. It fails at other q in (2, 3): at q = 5/2 and t = 2, H = 31 sqrt(2)/8 - 15/4 > 53/50 (AT-1577
REFUTES the reading for all 2 < q < 3; an HF-Q inequality at other q with another constant is OPEN, AT-1579). The
closed forms below are written with q but are claimed only at q = 21/10. For real S1 k with R = ||k||_2 and K = ||D^q k||_2
finite and every real S1 Schwartz u (g = J^q u, G = ||g||_2, h = W^(-1) u):
    |Re (J^q [W (U[k].grad h)], g)| <= L_B(R, K) G^2,
    L_B(R, K) = q C_sym R^theta K^(1-theta) + (53/100) S_core K + (sigma/(2 r0) + A0(B) L_0) C_a R^(1-1/q) K^(1/q)
                + B S_w [(sigma/(2 r0)) K + q 2^(q-2) (L_1 R^(1/q) K^(1-1/q) + L_q R)],
for every B > 1/2, with A0(B) = sup over x >= 0 of ([(1 + x)^q + (1 + x)^(-q) - 2]/2 - B x^q),
S_core = 1/[2 (pi (q - 1)(q - 2))^(1/2)] and S_w = (2 pi (q - 1))^(-1/2). C_sym, C_a and the weight constants
L_0, L_1, L_q are given in closed form in the cited sections; at P-S2 (upper decimals; T2_CEPS_v02 section 3 with
erratum E2 of T2_CEPS_v02a):
    L_B(R, K) <= 0.516341 R^(1/21) K^(20/21) + 0.450791 K + (0.241725 + 0.759399 A) R^(11/21) K^(10/21)
                 + 0.380377 B [0.7 K + 6.30203 R^(10/21) K^(11/21) + 16.5433 R]
for the certified pairs (B, A) of AT-235. The bound has no tame term and no weak term. L_B is nondecreasing in R
and K. The two K-linear terms give the floor L_B(R, K) > lambda_1 K with
    lambda_1 = (53/100) S_core + S_w sigma/(4 r0):  0.583922122691 (P-S2),  0.640978603636 (P-S1)
(lower 12-digit decimals, rechecked in Arb at 200 bits for this note). The earlier display "l_Q > 0.869 M" is REFUTED as a universal coefficient
(AT-238, AT-243); the valid form at P-S2 and the input c_W M is L_B(R, c_W M) > lambda_* M,
lambda_* = c_W lambda_1 = 0.868992902989... (notes/T2_CEPS_v02a.md erratum E1).

2.5 Theorem CE and Corollary CE-B at q = 21/10 (notes/T2_X4_v01.md sections 2 to 4; CONFIRMED, AT-272, AT-273;
transfer CE-G with 0 < sigma <= 2 and r0 > 0, AT-306). For k in L^2 with N(k) finite and every rho1, rho2 > 0,
    ||D^q k||_2 <= N(k) + E(||k||_2, ||D^q k||_2; rho1, rho2),
with E an explicit finite sum of terms c R^(1-s/q) K^(s/q), s in {0, q - 2, 1, q - 1, 2}. A rational Kbar with
Kbar - M - E(R, Kbar) > 0 bounds ||D^q k||_2 on K(R, M), and Kbar/M = 1 + O((R/M)^(1/q)). Every uniform input
satisfies Kbar >= M (AT-274). Two displayed decimals of the draft constants were REFUTED as upper endpoints, with
the upper replacements kappa_alpha <= 1.12395461 and L_w <= 3.38860664 (AT-272); the saved norm, capacity and budget
tables are CONFIRMED at their stipulated data (AT-275).

2.6 Re-centering (notes/T2_O2S_v02.md section 9; CONFIRMED under explicit L^2 center and domain conditions,
AT-060). After a change of center h_*, the L^2 coercivity is beta_0* >= beta_0 - ||grad h_*||_inf (T2-RC-L2), and the
criterion of Theorem A holds with the starred data (beta_0*, beta_b*, C_eps*, tau_S*, N(F_*), ||F_*||_2). These
starred data must be certified at the new center; none of them transfers from 007.

2.7 OPEN in O2: HS0; c_1 = q; numerical values of C_eps, c_1 to c_4 and Cbar; a numerical all-k matrix margin betaK
at any center.

## 3. O3: the invariant-ball closure (13.1)

3.1 Theorem A (preferred type; Theorem D-S with Corollary D1-S, notes/T2_O2S_v02.md section 5; CONFIRMED as a
conditional implication: D-S and THR-S AT-036 and AT-059, the inverse premise AT-058, the fixed-point step AT-037).
Assume (H-S): (BG-reg; gamma_*), R1/R2/R3 with all their hypotheses, (B-L2), (BG-q; q, sigma, r0, beta) with
2 < q < 3 and 0 < sigma < 1 + gamma_*, F real S1 with F_y(0) = 0, 0 < N(F) < infinity, and 0 < eps < beta. Put
    kappa_bar(R, M) = c_1 C_GN^U R^theta (c_W M)^(1-theta) + c_2 R + c_3 C_inf^U R^theta_0 (c_W M)^(1-theta_0),
    beta_* = beta - eps - kappa_bar(R, M),
    A_F = N(F)/beta_* + (C_eps/beta_*)^(1/2) R,
    eta(R, M) = (c_4/beta_*) [C_GN c_W^(1-theta) R^theta M^(1-theta) + C_inf c_W^(1-theta_0) R^theta_0 M^(1-theta_0)].
(i) If beta_* > 0 and A_F + eta(R, M) M <= M, then T(K(R, M)) is contained in K(R, M), N(T(k)) <= A_F + eta(R, M) M
on K(R, M), and there is a stationary solution rho_bar + h with h = T(h) in K(R, M) (weighted C^(1, q-2) by the
NR-1 embedding). This is (13.1) with H = N.
(ii) (THR-S) With beta_b = (beta - eps)/2, rho_C = (beta_b/C_eps)^(1/2) and tau_S as in notes/T2_O2S_v01.md
section 6, the condition of (i) holds with M = 2 (N(F)/beta_b + R/rho_C) whenever
    (||F||_2/beta_0)^((q-2)/2) (N(F)/beta_b + (C_eps/beta_b)^(1/2) ||F||_2/beta_0) <= tau_S^(q/2).
Dependence on R, M and F: F enters through N(F) and R only; eta(R, M) -> 0 as R -> 0 at fixed M (powers
R^theta M^(1-theta) and R^theta_0 M^(1-theta_0)); kappa_bar -> 0 likewise. The GN constants C_GN, C_inf, C_GN^U,
C_inf^U are explicit (AT-033, AT-064); c_W, C_eps and c_1 to c_4 are finite and not numerical.
Necessary screen of the sufficient criterion (AT-061, CONFIRMED algebraic implications): with h_0 = -L^(-1) F and C_U
as defined there, (i) requires N(h_0) R^((q-2)/2) < [beta/(c_1 C_U)]^(q/2) and
N(F) R^((q-2)/2) < beta [beta/(c_1 C_U)]^(q/2). With c_1 >= q (AT-063) these become numerical tests of this
criterion once C_U is evaluated. They are necessary for the criterion only, not for existence.

3.1' Theorem A' (AT-114 (6), the theory auditor research/sharp_full_garding/PROOF.md; CONFIRMED as a conditional implication).
Under the setting of 2.3 and (R3/R5), for 0 < R <= Rbar and 0 < M <= Mbar put a = N(F)/b + (Cbar/b)^(1/2) R and
zeta = ((1 + delta0)/b) C_grad c_W^(1-theta) R^theta M^(1-theta). If a + zeta M <= M, then T(K(R, M)) is contained
in K(R, M), and R5-S gives the conditional fixed point. Compared with Theorem A, the tame coefficient is
1 + delta0 in place of c_4, the value term ||h||_inf is gone, and the gap is the actual perturbed margin betaK of
the reference ball. Cbar depends on (Rbar, Mbar, eps, delta0) and is not numerical.

3.2 Theorem B (route Q at q = 21/10; Corollary HF-Q-CE, notes/T2_X4_v01.md section 4; CONFIRMED as a conditional
implication, AT-273; at a general weight HF-Q-CE-G, AT-306, within the weight ranges of 2.4 and 2.5). Assume, for one background and weight:
- H1: closed generator, core, weighted semigroup and graph comparison on a reference ball that contains K(R, M)
  (the AT-237 bridge, exactly as listed in notes/T2_CEPS_v02a.md section 1);
- H2: the imported L^2 inverse, ||z||_2 <= R for z = T(k), k in K(R, M), and N(z) < infinity qualitatively;
- H3: (R3/R5) and N(F) < infinity;
- H4: the base weak energy at k = 0, Q_0(u) <= -b0 G^2 + C0 ||h||_2^2 for all real S1 Schwartz u, with b0 > 0 and
  finite C0 >= 0 (C0 = C^opt(b0) is allowed);
- H5': b' = b0 - L_B(R, Kbar) > 0 for a Kbar of Corollary CE-B at (R, M) and some B > 1/2.
Then b' N(z)^2 <= N(F) N(z) + C0 R^2 for z = T(k) and every k in K(R, M). Hence each of
    (direct)        N(F) <= b' M - C0 R^2/M,
    (conservative)  N(F) + (b0 C0)^(1/2) R <= b' M
gives T(K(R, M)) contained in K(R, M), with the L^2 and normalization constraints. In the form (13.1):
    N(T(k)) <= A_F + eta(R, M) N(T(k)),   A_F = (N(F) + (b0 C0)^(1/2) R)/b0,   eta(R, M) = L_B(R, Kbar(R, M))/b0,
and the closure condition is A_F <= (1 - eta(R, M)) M. Here Kbar(R, M) = M (1 + eps(R, M)) with
eps(R, M) = O((R/M)^(1/q)), certified between 0.003274 and 0.031478 on the grid of notes/T2_X4_v01.md Table C and
between 0.0035 and 0.0042 in the 013 cells of section 4.

3.3 The tradeoff of Theorem B at q = 21/10 (Propositions CEIL, NEC and NEC-R; notes/T2_X4_v01.md section 4 and
notes/T2_PS1_v01.md section 5; CONFIRMED, AT-274 and AT-307).
- At every R > 0, every capacity of Theorem B satisfies N(F) < (b0 - lambda_1 M) M <= b0^2/(4 lambda_1).
- With b0 <= c + 1 - q = 0.7103192101999... (AT-211):

| tuple | lambda_1 | 1/(4 lambda_1) (upper) | ceiling at the cap b0 = c + 1 - q (upper) |
|---|---:|---:|---:|
| P-S2 (7/5, 1) | 0.583922122691 | 0.428139284822 | 0.216019123430 |
| P-S1 (1, 1/2) | 0.640978603636 | 0.390028619649 | 0.196790258489 |

- At fixed R the necessary level of NEC-R is lower. At the cap and P-S1 it is 0.137614, 0.131360 and 0.127466 at ||F||_2 = 1e-6, 1e-5 and 3e-5 (beta_0 = 209/100; upper decimals).
- The allowed C0 at given (R, M, N(F)) is D = M (b' M - N(F))/R^2 (direct form). Since R enters squared, D grows
  like R^(-2) as ||F||_2 -> 0 while the N(F) budget stays below the ceiling. This is the precise sense in which
  route Q rewards a small ||F||_2: it buys room for the weak constant, not for N(F).

3.4 Why route Q cannot give "only ||F||_2 small", and what would. On route Q the k-dependent increment is bounded
entirely by G^2 (no tame and no weak part), and its K-linear terms (53/100) S_core K and B S_w (sigma/(2 r0)) K
carry no power of R. By the packet construction of AT-274, every uniform bound Kbar on ||D^q k||_2 over K(R, M) is
at least M, so no K-input removes them. The floor eta(R, M) > lambda_1 M/b0 holds at every R. A vanishing loss is sufficient for
the preferred type but is not a logically necessary property of every weak-smallness theorem (AT-273 REFUTES that
universal necessity). The preferred type is reached by Theorems A and A', whose k-dependent terms vanish as R -> 0
at fixed M, at the price of a weak constant (C_eps or Cbar) that is not numerical. An explicit version needs an
explicit weak constant with a tame loss Delta(R, M) -> 0 as R -> 0 (the target (W-REM), notes/T2_BUD_v01.md
section 5; qualitatively this is AT-114 with AT-071 (7), notes/T2_X4_v01.md section 6). It is OPEN. The best
explicit high-frequency remainder known to the second theory agent (AT-220 to AT-223) is all-quadratic, with Delta about 1.9 M, not
small in R.

## 4. Theorem B at the chain center C2-N1-013 (P-S1, CE input)

Center: Candidate 007 plus the exact correction b18s2 (ledger v07 identity hashes). Inputs:

| input | value | status |
|---|---|---|
| N_(21/10)(F_*) at P-S1 | in [0.0035510975483434412497, 0.0055545729030073655758] | CONFIRMED (AT-1430, AT-1431) |
| ||F_*||_2 | in [7.959400186993612e-7, 7.961206656880281e-7] | CONFIRMED (AT-1413; inputs AT-1411, AT-1412) |
| beta_0 (L^2 gap) | 7/4 | stipulated (item B / G2) |
| background cover (beta_* >= 3/5, g_* <= 1/4, s_* <= 3/2; gives the rate b0) | | OPEN (item B) |
| H1, H2 (actual generator, reference ball) | AT-600 reduction (at exact009); KB margin AT-832 | OPEN (item G2) |
| H4: C^opt(b0) | reduction Theorem H4-R (notes/T2_H4_v01.md; AT-364) to near and far charges | OPEN (item G3) |

Allowance (the first theory agent research/qwg/v02/hfq_ps1/budget_013g/budget_013g.out, SHA256 ed86024b...; its cells are among the
52 cells CONFIRMED by AT-831; reference-ball margin AT-832). At ||F||_2 <= 7.97e-7, beta_0 >= 7/4 and N(F) <= 0.006, which covers the
certified interval (monotonicity: the second theory agent's notes 20:54Z item 3), the direct test of Theorem B holds for every C0 <= D:
- b0 = 0.55: D > 1.22e11 (M = 0.386, B = 13/25, Kbar/M = 1.00410, Z = D R^2 > 0.02535);
- b0 = 0.60: D > 1.61e11 (M = 0.424, B = 13/25, Kbar/M = 1.00392, Z > 0.03357).
The N(F) budget is not binding at 013. Since Z = D R^2 = M (b' M - N) with Z a lower decimal, b' M > Z/M + N, so
N = 0.006 is less than 8.4 percent of b' M at b0 = 0.55 and less than 7.1 percent at b0 = 0.60 (CLAIMED,
elementary arithmetic on the printed cells). The binding quantity is C^opt(b0).

H4 at 013 (item G3). Theorem H4-R (AT-364) bounds C^opt(b0) by C_N plus priced squares of named remainder estimates.
- Near side: Proposition HF1-NEAR is CONFIRMED conditionally (AT-691); its numerical near constants are OPEN
  (ledger v07, row G3; AT-931). Only a lower bound is certified: D6(a_r) >= 45543 (AT-1456; AT-1457 refutes the
  reproduction of two older endpoints; AT-1458: no near closure follows).
- Far side at the split erflog 8, rho 1 (owner the second theory agent). Proposition F (notes/T2_FAR_F_v01.md; CONFIRMED as a
  conditional theorem, AT-1236): if a certified S^+ >= S_h^B (rows C3, C4) and a certified A_low^+ >= A_low(8 pi)
  (row C2) satisfy S^+ <= Gbar - SC^+ and A_low^+ <= Gbar - S^+, then
  B_(a_f)(g) <= [max(SC^+, A_low^+) + S^+] ||J^(-1) g||^2 <= Gbar ||J^(-1) g||^2 for every g in the test class,
  with Gbar = q (c - 3/2) = 0.65167... Rows:
  - C5a, C5b (qualitative hypotheses of Lemma HSB on a_f): CONFIRMED (AT-1147 to AT-1150; AT-1151 refutes one proof
    sentence of C5a, and its replacement preserves C5a and C5b; AT-1152: explicit far constants do not follow from
    C5);
  - C1: SC(a_f) <= SC^+ = 0.46564943200002806, CONFIRMED (AT-1230 to AT-1234), so the first condition holds for every
    S^+ <= Gbar - SC^+ (> 0.186020);
  - C3 with C4: Theorem CS-B (notes/T2_FAR_CS_v02.md, with the 20:19Z correction in team notes),
    S^+ = 0.059699233948103884, CLAIMED; Lemma KP, the analytic Lemma KT and the room arithmetic CONFIRMED
    (AT-1536 to AT-1538); the numerical application OPEN (AT-1540). Every FLOAT S_h^B computed at erflog 8, rho 1 is
    below 0.0227 (team notes 21:02Z);
  - C2: a certified A_low^+(8 pi) <= Gbar - S^+ (> 0.591971). OPEN with no route that fits before the stop
    (notes/T2_FAR_C2_PLAN_v01.md; the coordinator 20:49Z item 3 records it OPEN with no C2 code). The FLOAT band value
    is 0.3848;
  - D0 (binding of the C1 manifest to the 013 identity): CONFIRMED (AT-1230);
  - C6 (the strain bound s_* <= 3/2; item B) and C7 (near side): OPEN.
- Far side by route F-a (the first theory agent's note 44; AT-911) at erflog 8, rho 1, Rw = Ww = 200, at a strain bound s^+ below 3/2
  (erratum E2): Corollary CS-W with Proposition DW (notes/T2_FAR_CSW_v01.md, CLAIMED) gives the S input
  S_h^B(a_W) <= 0.05970055144902641 from Theorem CS-B (so it inherits AT-1540). The row then needs
  max(SC^+(a_W), A_E^+) <= q (c - s^+) - 0.17373975 with OMF^+(a_t) = 0.11403919054571054 (CLAIMED); at
  s^+ = 137/125 that is 1.3263305 against FLOAT A_E 1.1342736. A_E^+ and s^+ are OPEN.
So Theorem B at 013 reduces to: item B, item G2, a certified near constant, and on the far side row C2 and the
numerical CS-B application, all to be combined into a certified C^opt(b0) <= D.

## 5. Status table

| result | where | status |
|---|---|---|
| Lemma KP-W (finite c_1 to c_4) | research/kpw/PROOF.md | CONFIRMED (AT-049 to AT-051) |
| c_1 >= q for KP-W | | CONFIRMED (AT-063) |
| c_1 = q | | OPEN (AT-050) |
| T2-HS1r (restricted uniform inverse) | T2_O2S_v02 section 4 | CONFIRMED (AT-058) |
| HS0 (unrestricted) | | OPEN |
| WG-K, UT-K, S-inv-K, THR-K | T2_WGK_v01 | CONFIRMED conditional (AT-065, AT-066, AT-069) |
| gradient-only inverse estimate and Theorem A' | The theory auditor sharp_full_garding | CONFIRMED conditional (AT-114) |
| Theorem A (D-S, THR-S) | T2_O2S_v02 section 5 | CONFIRMED conditional (AT-036, AT-059) |
| R5-S (fixed point in the Hilbert ball) | T2_O2S_v02 section 6 | CONFIRMED conditional (AT-037) |
| re-centering RC, RC-L2 | T2_O2S_v02 section 9 | CONFIRMED under explicit L^2 center and domain conditions (AT-060) |
| Theorem HF-Q, Lemma CORE | T2_CEPS_v02 section 3 | CONFIRMED (AT-234, AT-237) |
| HF-Q at a general weight; CE-G; HF-Q-CE-G | T2_PS1_v01 sections 2, 3 | CONFIRMED (AT-306) |
| Theorem CE, Corollary CE-B, HF-Q-CE (Theorem B) | T2_X4_v01 | CONFIRMED (AT-272, AT-273, AT-283) |
| Proposition CEIL, Kbar >= M | T2_X4_v01 section 4 | CONFIRMED (AT-274; 0.428139 not an upper) |
| Propositions NEC, NEC-R | T2_PS1_v01 section 5 | CONFIRMED (AT-307) |
| Theorem H4-R (reduction of C^opt) | T2_H4_v01 section 4 | CONFIRMED conditionally (AT-364) |
| allowance D at 013 | The first theory agent budget_013g | CONFIRMED at stipulated inputs (AT-831) |
| Proposition F (far assembly) | T2_FAR_F_v01 | CONFIRMED conditional (AT-1236) |
| C1, SC^+ | T2_FAR_C1_v01 | CONFIRMED (AT-1230 to AT-1234) |
| Theorem CS-B, S^+ | T2_FAR_CS_v02 | analytic parts CONFIRMED (AT-1536 to AT-1538); application OPEN (AT-1540) |
| Corollary CS-W, Proposition DW (route F-a S input) | T2_FAR_CSW_v01 | CLAIMED |
| scope of this note (v01) | | CONFIRMED with the q = 21/10 restriction (AT-1576, AT-1578); all-q reading REFUTED (AT-1577) |
| row C2 | T2_FAR_C2_PLAN_v01 | OPEN (Lemma QID, Proposition ZO CLAIMED) |
| explicit C_eps, c_1 to c_4, Cbar; (W-REM) | | OPEN |
| explicit C^opt(b0) at any center | | OPEN |

## 6. What would close O3, in order of leverage

1. A certified C^opt(b0) <= 1.61e11 at b0 = 0.60 (or <= 1.22e11 at b0 = 0.55) at 013, together with items B and G2.
   The far part needs row C2 (no feasible route before the stop) and the numerical CS-B application.
2. For a theorem of the preferred type with numbers: an explicit Cbar in AT-114 (1) on one reference ball, with a
   numerical all-k margin betaK. Then Theorem A' is a numerical criterion with eta -> 0 as R -> 0.
3. Within route Q, sharper principal constants in the K-linear terms of L_B (the core 53/100 and the weight term)
   are the only way to raise the ceiling (AT-274: the ceiling is intrinsic to this loss formula). Replacing 53/100 by 1/2 would gain at most 6 percent in that term
   (T2_CEPS_v02 section 3, Remark (ii), FLOAT probe); it is not needed at 013, where N(F) is not binding.

## 7. Files (SHA256 at the time of writing)

- notes/T2_O2S_v02.md da418c668509c239ae52e817ac021c2b251a246871efd618e67575a94418a7ff
- research/kpw/PROOF.md c06f660d173bad61f92cdccface7f4acf77233a9d659878040259a0e72f963c0
- notes/T2_WGK_v01.md e71e1848f6f2f98aae0c85737619233fa5bb08b5b4da705b66a4528397a81c71
- notes/T2_CEPS_v02.md 62d86ab10ec6a910d45d18a297ce505b88a21c4dea471ad56184a7a0ea2016b3
- notes/T2_CEPS_v02a.md f6ee3d4814d03f79f5af0a3087a12753b9a58fba7368652edf388e767fa547cf
- notes/T2_X4_v01.md f23c72d77ffe418350b051422f065165628e43aee8349085f0a5099f9cb48050
- notes/T2_PS1_v01.md b97ea1590c6ee58d04ab507bf3ae106388b8a47a2ea9ebdbc8d520cdb8097d44
- notes/T2_H4_v01.md 6a00743b1c899fe42ac367a849e68f91041519ae5d61a19aa714fa6aaf60bbb4
- notes/T2_FAR_F_v01.md fc3bb9aa5ecc0b17f4c43e6178377e4ddb28739e85edef749a1fcdab0b11cfff
- notes/T2_FAR_C1_v01.md a00ee53fdcfc379b636c655e2316dc5440903568974cdffcfeea6a268a72b18b
- notes/T2_FAR_CS_v02.md aa1f9eda052ae1479dd5dc4f0325bc49110d080d20a55422a19e2cfde11dcaa6
- notes/T2_FAR_C2_PLAN_v01.md d9604af8f6abb707745cf37e42328a2403d919b6c08a7443b3703237c874ec9e
- notes/T2_BUD_v01.md 46b73b8da2fe7bb642613fcbc51f334f49ce91e18756e51c8583afee4a1966f1
- theory_agent_1/research/qwg/v02/hfq_ps1/budget_013g/budget_013g.out ed86024bbbd85399ba62447f492124b0d3d84128af1d45fc60d84acb770e2a2d
- notes/T2_FAR_CSW_v01.md 45e8788e72aceaa76bbe62b1b7b6406c1a526c439c15e5279d7098b60bc961bb
- notes/T2_O2O3_FINAL_v01.md 7130dcc8fdc3c5412305773e66efef1973c2ed7decf5246f0742e46fec8d88e1

## 8. Errata relative to v01

- E1 (the theory auditor AT-1576 to AT-1579, 21:19Z). The setting line of v01 put 2 < q < 3 in front of every result. The explicit
  HF-Q coefficient 53/100 rests on a scalar inequality proved at q = 21/10 and false at q = 5/2, t = 2 (AT-1577), so
  sections 2.4, 2.5, 3.2, 3.3, 3.4 and 4 are now stated at q = 21/10, with the weight ranges sigma > 0, r0 > 0
  (HF-Q-G) and 0 < sigma <= 2, r0 > 0 (CE-G) of AT-306. P-S1 and P-S2 satisfy both. The qualitative results keep
  2 < q < 3. No number of v01 changes.
- E2 (new item, CLAIMED). Section 4 gains the route F-a far row with the S input of notes/T2_FAR_CSW_v01.md, and
  section 5 gains its status row and the scope verdicts of v01.

Frozen 2026-11-03T21:23:48Z as notes/T2_O2O3_FINAL_v02.md (immutable; corrections go to a new version).
