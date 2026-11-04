# T2_BUD_v01: the Cbar budget at P-S2 and what it demands of the missing high-frequency estimate

Version 1. Owner: the second theory agent. Written 2026-11-03T00:34Z to 00:45Z. Plain-text mathematics as in T2_REV_v01. Paths are
relative to the combined2 root; files of this agent are given relative to theory_agent_2/. Requested by the coordinator's team notes
23:56Z item 5 (Cbar budget at P-S2 with c_W = 7441/5000 for N in {0.05, 0.077, 0.1} and ||F_*||_2 in
{1e-5, 3e-5, 6e-5}, labelled FLOAT inputs) and 23:43Z item 2 (orientation level). Builds on notes/T2_CEPS_v01.md
(Definition CB, Theorem CB-ZERO, Lemma LOW, target HF-EXP; the theory auditor AT-175 to AT-178, AT-184 to AT-187) and on
notes/T2_EXP_v01.md (AT-064 constants, (CF3) branch form).

Labels. Every number in the tables is FLOAT arithmetic on FLOAT background inputs and is HEURISTIC orientation, not a
certificate and not a closure. Proposition S is CLAIMED (elementary, an implication from CONFIRMED results). HF-EXP and
(W-REM) are OPEN.

## 0. Summary

1. Fixed-rate budget (AT-151 form, Cbar <= (L6 - N)^2/(b R^2)) at P-S2, c_W = 7441/5000: of order 1e9 at
   ||F_*||_2 = 1e-5, 1e8 at 3e-5 and 1e7 at 6e-5 (table A). With the gap loss tau(M) of (CF3) included the budget falls by
   a factor of about 5 at N = 0.05 and 12 to 20 at N = 0.077, and is empty at N = 0.1 for b = 0.6607 and
   ||F_*||_2 >= 3e-5 (table B). Largest N with Cbar = 0:
   0.0955 to 0.1046 at b = 0.6607 and 0.111 to 0.121 at b = 0.7103 (delta0 -> 0).
2. Proposition S: when every k-dependent loss is a rate loss l(M) plus a gradient-only tame term T_1 N(k) ||grad h||_inf G,
   the invariant-ball condition is one scalar inequality; when l is of Gagliardo-Nirenberg form it depends on the losses
   only through one coefficient S, and the admissible level is L6(S) = L6(C_grad) (C_grad/S)^(q/2).
3. Requirement on HF-EXP at Lambda = 1 (table D). Keeping the principal part pointwise (GN form), the remainder
   coefficient d' must satisfy d' <= 0.30 at N = 0.077, d' <= 1.03 at N = 0.05, d' <= 2.46 at N = 0.03
   (||F_*||_2 = 3e-5, b0 = 0.6607, Cbar = 0, tame coefficient 1). Without principal retention d <= 0.77, 1.52, 2.95.
   The only explicit constants proved so far for any piece of this remainder (AT-186: A_q = 11.61, D_q = 9.61 for the
   homogeneous unweighted bare remainder) are 4 to 40 times larger.
4. At q = 21/10 smallness of R buys almost nothing in the k-dependent terms: R^theta (c_W M)^(1-theta) lies between 0.86 M
   and 1.02 M for the radii in question. The R-small terms are R D_low(1) (about 1.3e-3), the s_3 weight branch (below
   1e-3) and the weak term (b Cbar)^(1/2) R. So the explicit closure at P-S2 is a question of order-one constants in
   the high-frequency estimate, and the weak constant enters only through (b0 Cbar)^(1/2) R.

## 1. Inputs (all FLOAT)

- P-S2 = (q, sigma, r0) = (21/10, 7/5, 1), theta = (q - 2)/q = 1/21, c_W = 7441/5000 (T2_CWS2_v01, AT-169).
- AT-064 constants at q = 2.1: C_grad = 0.695444, C_sym = 0.245877, C_DU = 0.549797, C_U = 0.299056
  (scratch/at064/closure_fn_v2.py, consts(q, "v2")).
- b: the k = 0 margin, b = 0.6607 (007 mesh margin at P-S2, r 0.73, numerics_v02 rows 124 and 158) or b = 0.7103 (the
  exact origin cap c_l + 1 - q, an upper value). A certified rate b0 < beta is needed for C^opt(b0) < infinity; the tables
  use these values as orientation only.
- beta_0 = 2.09 (the coordinator 23:56Z item 2) or 1.862 (re-centered lower value, theory_v03 T3.4c); R = ||F_*||_2/beta_0.
- delta0 in {0, 0.1} (tame coefficient 1 + delta0).
- Code: research/ceps/budget_ps2.py (tables A, B, C; output research/ceps/budget_ps2.out) and research/bud/hf_budget.py
  (table D; output research/bud/hf_budget.out). Run on core 40 at nice 19, OMP_NUM_THREADS=1.

## 2. Table A: AT-151 budget at fixed rate

Cbar_max = (L6 - N)^2/(b R^2), L6 = b (1 - theta)/(2 - theta) M_*, M_* = [(2 - theta) d2]^(-q/2),
d2 = ((1 + delta0)/b) C_grad c_W^(1-theta) R^theta (AT-124, AT-151). This is the fixed-rate form: it uses the k = 0
margin b on every trial ball and ignores the gap loss. It is valid as a level only if M_* <= Mbar; M_* is 0.48 to 0.63.
beta_0 = 2.09; the beta_0 = 1.862 rows (in the output file) are 20 to 25 percent lower.

| b | 1 + delta0 | ||F_*||_2 | L6 | Cbar_max at N = 0.05 | N = 0.077 | N = 0.1 |
|---:|---:|---:|---:|---:|---:|---:|
| 0.6607 | 1.0 | 1e-5 | 0.18756 | 1.25e9 | 8.08e8 | 5.07e8 |
| 0.6607 | 1.0 | 3e-5 | 0.17753 | 1.20e8 | 7.42e7 | 4.42e7 |
| 0.6607 | 1.0 | 6e-5 | 0.17148 | 2.71e7 | 1.64e7 | 9.39e6 |
| 0.6607 | 1.1 | 1e-5 | 0.16970 | 9.47e8 | 5.68e8 | 3.21e8 |
| 0.6607 | 1.1 | 3e-5 | 0.16063 | 8.99e7 | 5.14e7 | 2.70e7 |
| 0.6607 | 1.1 | 6e-5 | 0.15515 | 2.03e7 | 1.12e7 | 5.59e6 |
| 0.7103 | 1.0 | 1e-5 | 0.21756 | 1.73e9 | 1.22e9 | 8.50e8 |
| 0.7103 | 1.0 | 3e-5 | 0.20593 | 1.66e8 | 1.14e8 | 7.67e7 |
| 0.7103 | 1.0 | 6e-5 | 0.19892 | 3.79e7 | 2.54e7 | 1.67e7 |
| 0.7103 | 1.1 | 3e-5 | 0.18632 | 1.27e8 | 8.17e7 | 5.09e7 |

## 3. Table B: (CF3) with the gap loss (orientation level, the coordinator 23:43Z item 2)

(CF3) in the AT-134 branch form (research/explicit/closure_fn_v4.py): (6) with b replaced by the trial-ball rate
g(M) = b - tau(M), tau(M) = q C_sym R^theta (c_W M)^(1-theta) + min(sigma C_DU R^theta (c_W M)^(1-theta),
(sigma/(2 r0)) C_U R^theta_0 (c_W M)^(1-theta_0)), theta_0 = (q - 1)/q (trial-ball rate dependence: AT-178). Budget =
(w/R)^2 with w the largest weak coefficient for which some radius closes; the radius at which it is attained is
given. "none": no radius closes even at Cbar = 0. beta_0 = 2.09.

| b | 1 + delta0 | ||F_*||_2 | max N (Cbar = 0) | budget at N = 0.05 (M) | N = 0.077 (M) | N = 0.1 (M) |
|---:|---:|---:|---:|---:|---:|---:|
| 0.6607 | 1.0 | 1e-5 | 0.10461 | 2.54e8 (0.336) | 6.47e7 (0.331) | 1.80e6 (0.326) |
| 0.6607 | 1.0 | 3e-5 | 0.09897 | 2.27e7 (0.318) | 4.55e6 (0.312) | none |
| 0.6607 | 1.0 | 6e-5 | 0.09554 | 4.90e6 (0.306) | 8.10e5 (0.301) | none |
| 0.6607 | 1.1 | 3e-5 | 0.09334 | 1.75e7 (0.298) | 2.48e6 (0.293) | none |
| 0.7103 | 1.0 | 1e-5 | 0.12135 | 4.03e8 (0.364) | 1.55e8 (0.359) | 3.59e7 (0.355) |
| 0.7103 | 1.0 | 3e-5 | 0.11480 | 3.69e7 (0.344) | 1.25e7 (0.339) | 1.92e6 (0.334) |
| 0.7103 | 1.0 | 6e-5 | 0.11084 | 8.13e6 (0.332) | 2.51e6 (0.327) | 2.57e5 (0.322) |
| 0.7103 | 1.1 | 3e-5 | 0.10827 | 2.94e7 (0.323) | 8.45e6 (0.318) | 5.90e5 (0.314) |

Reading (HEURISTIC). The FLOAT C5 + h value N_P-S2 = 0.0765 at ||F_*||_2 = 2.8e-5 (the coordinator 23:56Z item 2) lies below
the Cbar = 0 orientation level 0.093 to 0.115 at ||F_*||_2 = 3e-5, with a budget of 2e6 to 1e7 for the weak constant at
N = 0.077. This uses AT-114's betaK through tau(M), that is, (CF3) presupposes AT-114 (1) with a Cbar computed on a
reference ball; it says nothing about whether such a Cbar is of order 1e6 (the first theory agent QWG_v01 section 6 orders are far
above; T2_CEPS_v01 section 4).

## 4. Proposition S (CLAIMED; elementary consequence of AT-114 (2), (6) with the trial-ball rate of AT-178)

Setting and notation as in AT-114 and T2_CEPS_v01 section 1: Q_k(u) = Re (J^q [W A_k W^(-1) u], g), g = J^q u,
G = ||g||_2, h = W^(-1) u, K(R, M) = {k real S1 : ||k||_2 <= R, N(k) <= M}, d := c_W^(1-theta) R^theta.

Proposition S. Let b0 > 0, R > 0, M > 0, T_1 >= 1, Cbar >= 0 and l(M) in [0, b0). Suppose
    (1_l)  Q_k(u) <= -(b0 - l(M)) G^2 + Cbar ||h||_2^2 + T_1 N(k) ||grad h||_inf G
for all k in K(R, M) and all real S1 Schwartz u. Then AT-114 (1) holds on K(R, M) at rate b(M) = b0 - l(M) with tame
coefficient 1 + delta0 = T_1, and AT-114's invariant-ball condition (6) on this trial ball is
    (6_l)  N(F) + (b(M) Cbar)^(1/2) R + T_1 C_grad d M^(2-theta) <= b(M) M.
A sufficient condition is
    (S)    N(F) + (b0 Cbar)^(1/2) R <= Phi(M) := (b0 - l(M)) M - T_1 C_grad d M^(2-theta).
If l(M) = S_rate d M^(1-theta) (Gagliardo-Nirenberg form), then Phi(M) = b0 M - S d M^(2-theta) with S = T_1 C_grad + S_rate,
and
    sup over M > 0 of Phi = L6(S) := b0 ((1 - theta)/(2 - theta)) M_S,   M_S = [(2 - theta) S d/b0]^(-q/2),
    L6(S) = L6(C_grad) (C_grad/S)^(q/2),
where L6(C_grad) is the AT-124 level at 1 + delta0 = 1. So (S) holds at some M <= Mbar if and only if
N(F) + (b0 Cbar)^(1/2) R <= sup over M <= Mbar of Phi, which is L6(S) when M_S <= Mbar.

Proof. (1_l) is AT-114 (1) with b replaced by b(M) and 1 + delta0 by T_1 on the trial ball K(R, M). AT-114 (2) and (6)
use (1) only through the scalar step b x^2 <= D x + C L^2 (T2_CEPS_v01 D6), and AT-178 CONFIRMS that the rate may
change with the trial ball. Multiplying (6), a + zeta_grad M <= M with a = N(F)/b + (Cbar/b)^(1/2) R and
zeta_grad = (T_1/b) C_grad d M^(1-theta), by b = b(M) gives (6_l). Since b(M) <= b0, (S) implies (6_l). For the GN form,
Phi'(M) = b0 - (2 - theta) S d M^(1-theta) vanishes at M_S, 1/(1 - theta) = q/2, and Phi(M_S) = b0 M_S (1 - theta)/(2 - theta);
L6(S) scales as S^(-q/2). QED.

Remarks.
- Cbar enters (S) only through (b0 Cbar)^(1/2) R. With (W-REM) below, Cbar = C^opt(b0), the first theory agent's k = 0 constant, and no
  reference ball is needed for it (T2_CEPS_v01 Corollary CB-B).
- The GN form is the right bookkeeping for losses bounded through ||Sym DU[k]||_inf, ||DU[k]||_inf: their AT-064 bounds
  are C R^theta (c_W M)^(1-theta). The s_3 branch has R^theta_0, theta_0 = 11/21, and is below 1e-3 here.
- At the radii in question R^theta (c_W M)^(1-theta)/M is 0.86 to 1.02 (R between 4.8e-6 and 2.9e-5, M between 0.05 and
  0.3; at q = 21/10, R^theta is about 0.56 to 0.62). So a rate loss d_hf M without R-factor costs about as much as the GN
  form with the same coefficient.
- The model check: S = C_grad + q C_sym (s_3 dropped), b0 = 0.6607, ||F_*||_2 = 3e-5, Cbar = 0 gives the level 0.09910
  against 0.09897 from (CF3) in table B.

Table C (from research/ceps/budget_ps2.out). S_max(N) = C_grad (L6(C_grad)/(N + (b0 Cbar)^(1/2) R))^(2/q) is the
largest S for which (S) holds; S_rem = S_max - C_grad - q C_sym is the room left for k-dependent losses other than the
principal part, at T_1 = 1. b0 = 0.6607, beta_0 = 2.09, ||F_*||_2 = 3e-5.

| Cbar | N = 0.01 | 0.02 | 0.03 | 0.05 | 0.077 | 0.1 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10.77 / 9.55 | 5.56 / 4.35 | 3.78 / 2.57 | 2.33 / 1.11 | 1.54 / 0.33 | 1.20 / -0.01 |
| 1e4 | 9.69 / 8.48 | 5.27 / 4.06 | 3.65 / 2.44 | 2.27 / 1.06 | 1.52 / 0.31 | 1.19 / -0.02 |
| 1e6 | 5.16 / 3.94 | 3.59 / 2.38 | 2.77 / 1.55 | 1.90 / 0.69 | 1.35 / 0.14 | 1.08 / -0.13 |

(entries S_max / S_rem; at b0 = 0.7103 the Cbar = 0 row is 12.40/11.19, 6.41/5.20, 4.36/3.14, 2.68/1.47, 1.78/0.56,
1.38/0.17.)

## 5. What the budget demands of HF-EXP and of (W-REM)

Target (W-REM) (OPEN). Explicit T_1 >= 1 and a nondecreasing explicit l_E with
    E(k, u) <= T_1 N(k) ||grad h||_inf G + l_E(M) G^2   for all k in K(R, M), all real S1 Schwartz u,
where E(k, u) = Q_k(u) - Q_0(u) = Re (J^q [W (U[k].grad h)], g) (T2_CEPS_v01 section 2). Under (W-REM), (1_l) holds with
Cbar = C^opt(b0) and l = l_E, because Q_0(u) <= -b0 G^2 + C^opt(b0) ||h||^2 by the definition of C^opt (attained, D1).
This is CB-ZERO with the split built into l_E. The route through CB-ZERO at Lambda = 1 with HF-EXP gives
    form 1 (HF-EXP first form):  l_E(M) = R D_low(1) + d_hf M,  T_1 = 1 + delta_hf;
    form 2 (principal part kept, bounded pointwise by AT-064 GN constants):
                                 l_E(M) = R D_low(1) + q C_sym d M^(1-theta) + s_3(M) + d'_hf M,  T_1 = 1 + delta_hf,
with D_low(1) = 87.95 at P-S2 (T2_CEPS_v01 section 3; R D_low(1) = 1.3e-3 at ||F_*||_2 = 3e-5). In form 2 the principal
part of the high piece e = Q_1 k is bounded with ||e||_2 <= R and ||J^q e||_2 <= ||J^q k||_2 <= c_W N(k), which is what
the AT-064 GN constants need; its coefficient q C_sym d M^(1-theta) is about 0.47 M at M = 0.31. Bounding it instead by
the plain Fourier L^1 norm of the high piece costs about 1.07 M (HEURISTIC arithmetic: q/2 times 0.886 for Sym DU plus
0.135 for the weight term), so the principal part should not be put into d_hf.

Table D (research/bud/hf_budget.out). Largest admissible d_hf (form 1) and d'_hf (form 2) for which (S) holds at some
M <= 1; b0 = 0.6607, beta_0 = 2.09.

| ||F_*||_2 | Cbar | delta_hf | form 1 at N = 0.01 / 0.03 / 0.05 / 0.077 | form 2 at N = 0.01 / 0.03 / 0.05 / 0.077 |
|---:|---:|---:|---|---|
| 1e-5 | 0 | 0 | 10.23 / 3.00 / 1.56 / 0.81 | 9.73 / 2.52 / 1.10 / 0.36 |
| 3e-5 | 0 | 0 | 10.17 / 2.95 / 1.52 / 0.77 | 9.64 / 2.46 / 1.03 / 0.30 |
| 3e-5 | 0 | 0.5 | 9.81 / 2.62 / 1.19 / 0.45 | 9.29 / 2.12 / 0.71 / none |
| 3e-5 | 0 | 1.0 | 9.46 / 2.29 / 0.87 / 0.13 | 8.93 / 1.79 / 0.38 / none |
| 3e-5 | 1e6 | 0 | 5.18 / 2.12 / 1.18 / 0.61 | 4.67 / 1.63 / 0.70 / 0.14 |
| 6e-5 | 0 | 0 | 10.10 / 2.92 / 1.49 / 0.75 | 9.55 / 2.40 / 0.99 / 0.25 |
| 6e-5 | 1e6 | 0 | 3.25 / 1.55 / 0.89 / 0.45 | 2.73 / 1.05 / 0.40 / none |

At b0 = 0.7103 the entries rise by about 0.2 to 0.6 for N >= 0.03 (output file). "none": (S) fails even with d = 0 at that tame
coefficient, because the tame term alone (1 + delta_hf) C_grad exhausts the room.

Comparison with the explicit constants available now.
- The homogeneous unweighted bare remainder (principal part removed) has the CONFIRMED bounds (AT-186, the external referee t2-cbar1
  section 4) |F_q| <= A_q K H_0^(alpha/q) G^(2-alpha/q) with A_(21/10) = 11.609 and, for inputs above mu,
  |F_q| <= D_q K mu^(-alpha) G^2 with D_(21/10) = 9.605, alpha = q - 2, K = ||D^q k||_2. With K <= c_W M these are
  coefficients A_q c_W = 17.3 and D_q c_W = 14.3 times M, multiplied by (H_0/G)^(alpha/q) or mu^(-alpha) (D_q c_W
  mu^(-alpha) is still 9.0 at mu = 100). Table D asks for d'_hf <= 0.3
  to 2.5 at N between 0.077 and 0.03. These constants are crude by design (3^q factors, Peetre steps), and they bound
  only the unweighted homogeneous piece. So an explicit closure at P-S2 needs a high-frequency remainder estimate with
  near-sharp constants, or a smaller N(F).
- Structural point (HEURISTIC, not a lower bound). In the near-diagonal region |p| <= |r|/2 of the commutator symbol
  (a = U[k] at frequency p, u at frequency r) the second-order Taylor remainder is at most about
  (q(q-1)/2)(3/2)^(q-2) |p|^2 <r>^(q-1), which after interpolation costs a multiple of ||D^(1+alpha') U[k]||_A G^2,
  0 < alpha' < q - 2, A the Fourier L^1 norm; its GN bound has the same scaling R^theta' M^(1-theta') with theta' < theta,
  and a crude evaluation at alpha' = 0.05 gives a coefficient near 0.9 M. That is inside the room at N = 0.03, borderline
  at N = 0.05 and outside at N = 0.077 (form 2). The far region (k at high frequency against u at low frequency) is the
  tame term; its coefficient T_1 must stay near 1 (delta_hf = 0.5 already removes the N = 0.077 column in form 2).
  These orders are planning advice only; the sharp constants are OPEN and are the subject of T2_CEPS_v02.
- Lambda in CB-ZERO. At q = 21/10 the AT-112 gain Lambda^(-(q-2)/4) = Lambda^(-1/40) is useless for an explicit closure
  (a factor 1/2 needs Lambda = 2^40), while R D_low(Lambda) grows like Lambda^(q+1) (88, 588, 1964 at Lambda = 1, 2, 3).
  Lambda = 1 is the natural cut; the high piece must be estimated with GN bookkeeping in ||e||_2 <= R, not by its
  frequency gap.

## 6. Consequences for the exchange

- To the first theory agent (theory_v04): table A answers the coordinator 23:56Z item 5 in the AT-151 form; table B gives the (CF3) orientation
  level at P-S2 with c_W = 7441/5000 (23:43Z item 2). Proposition S (CLAIMED) can be quoted as the scalar form of (6)
  with a trial-ball rate. Both are HEURISTIC in their numbers.
- For the Cbar route: with CB-ZERO or (W-REM), Cbar = C^opt(b0) is the first theory agent's k = 0 constant; the budget for it at
  N = 0.077 is of order 1e6 to 1e7 only if the high-frequency constants are small (table D, Cbar = 1e6 rows). Near
  N = 0.05 to 0.077 (form 2), 0.1 in d'_hf costs about 0.004 in admissible N, and 0.5 in delta_hf costs about as much
  as 0.33 in d'_hf.
- To the first numerics agent and the coordinator (planning, HEURISTIC): at fixed explicit-constant quality, lowering N(F) from 0.077 to 0.05
  roughly triples the room for the high-frequency remainder (form 2: 0.30 to 1.03), and to 0.03 multiplies it by 8.
  Lowering ||F_*||_2 from 6e-5 to 1e-5 changes the room by about 0.1 at Cbar = 0; it matters mainly through Cbar.
- Distinctions carried from AT-175 to AT-187: the CB sandwich is proved, equality of optimal constants is not (AT-175);
  the low loss is not negligible at all cutoffs 1 to 3 (AT-176; here only Lambda = 1 is used); the trial-ball rate changes
  with M (AT-178; built into Proposition S); the coarse complete principal bound (q + sigma) sup ||Sym Da||_op = (7/2)
  sup ||Sym Da||_op at P-S2 (AT-180) is an alternative to the s_3 branch for velocities with a(0) = 0 and is weaker here
  because s_3 carries R^theta_0; the packets of AT-185 do not refute the full sharp tame estimate; the AT-186 constants
  bound the bare homogeneous remainder only.
