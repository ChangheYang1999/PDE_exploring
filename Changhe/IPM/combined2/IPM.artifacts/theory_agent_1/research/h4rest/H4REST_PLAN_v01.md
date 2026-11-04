# H4REST_PLAN_v01: the needs and producers of the H4-REST pieces at C2-N1-013, and the eps_rest left by U (the first theory agent)

Written 2026-11-04 in a work session for coordinator note 08:49Z item 2(c), to be completed with the second theory agent. This is a
planning statement. Section 2 is exact arithmetic of printed values (research/h4rest/h4rest_budget.py and .out,
Python 3.12.13, python-flint 0.9.0, under 1 s on core 40). Section 3 states one new elementary lemma (CLAIMED, audit
requested). Everything else is a description of what is missing, with no new bound. Labels: CONFIRMED (cited audit),
CLAIMED, FLOAT, HEURISTIC, OPEN.

## 1. The pieces

Setting of the second theory agent's T2_H4_v01 section 2 (P-S1, q = 21/10, W^2 = 1 + 4|X|^2, v = Rg, S = Sym D ubar, J = <D>).
Proposition FG of T2_FAR_v01 (CONFIRMED conditionally, AT-513) gives
    D_rem(g) <= -(G - A_far) ||J^(-1) g||^2 + D_rem^n(g),   D_rem^n = T_IS + Q_(a_n) + C_tr + C_aw[a_n] + C_vs,
with G = q (c - s_*). The near weight form (Q + C_aw)[a_n] is the subject of NEAR_CHECK (e_up ||g||^2 + P_HF ||h||^2).
H4-REST is the rest of D_rem^n, each piece with its full coefficient (no near and far split is made yet):
- T_IS = (q/2) <([n, [S, n]] - [J^(-1), [J^(-1), S]]) v, v>, n = 1 - |D|/<D>; coefficient S (first derivatives of
  ubar); order -4 at high frequency and of size one at |xi| below 1 (T2_H4_v01, Proposition DR; AT-332).
- C_tr = Re<[J^q, ubar.grad] J^(-q) g, g> - q int (Bg)^T S (Bg); coefficient ubar; order -2 with third derivatives of
  ubar (Lemma KER).
- C_vs1 = Re<[J^q, grad rhobar.] J^(-q) U[g], g>: the velocity-source commutator, order -1 with a symmetric part of
  order -2 and third derivatives of rhobar.
- C_vs2 = Re<J^q (grad rhobar.(W U[W^(-1) u] - U[u])), g>: the weight commutator at the H^q level, coefficient
  grad W/W of size sigma/|X|.
- C_vs3 = Re<grad rhobar.U[g], g> - int (Rg)^T K (Rg): the R1 symmetrization; its principal part is exactly the K term
  of P0, and its remainder involves [grad rhobar, R_a] (order -1, symmetric part of order -2).
Their identities are CLAIMED by the second theory agent and partly CONFIRMED (DR and KER identities, AT-332; the C_vs split is CLAIMED).
None of the five has an NE bound (T2_H4_v01 section 5: NE-lo and NE-vs OPEN) for any background, and no input of
them is certified at 013. The second theory agent's closure program enters them as eps_rest = C_rest = 0 (H4-REST OPEN).

## 2. The three budgets the pieces may use (exact; h4rest_budget.out)

In the NE form of Theorem H4-R a piece may be paid from three places. Each is shared by all five pieces.

(A) Rate room, for full L^2 losses eps ||g||^2 (the eps_rest of reading (ii), AT2333):
    R(U) = (beta_* - b0) - e_up - k (U - F),   k = (1 + q^2)/(2 mu^2),   F = 8(2c - 1) = 20.9651073632,
where U is the certified global upper of Lambda_+(a_n) (AT2364 to AT2366; the second theory agent's (R4) job) and e_up the printed
near upper. k = 5.217978395e-4 at mu 72 and 5.849913495e-4 at mu 68.

| U | plan (11/20, 72), beta_* regional | plan, ceiling beta_* = c + 1 - q | fallback (103/200, 68), regional | fallback, ceiling |
|---:|---:|---:|---:|---:|
| F | 0.000938706156 | 0.006302110849 | 0.008104144765 | 0.013467549458 |
| 21 | 0.000920499254 | 0.006283903947 | 0.008083732874 | 0.013447137567 |
| 21.5 | 0.000659600334 | 0.006023005027 | 0.007791237200 | 0.013154641893 |
| 22 | 0.000398701414 | 0.005762106107 | 0.007498741525 | 0.012862146218 |
| 22.5 | 0.000137802494 | 0.005501207187 | 0.007206245850 | 0.012569650543 |
| 23 | negative | 0.005240308267 | 0.006913750175 | 0.012277154868 |
| 25 | negative | 0.004196712588 | 0.005743767476 | 0.011107172169 |
| R(U) = 0 at | 22.764091 | 33.042794 | 34.818551 | 43.986899 |

"Regional" takes beta_* = 704955805507/10^12, certified by both auditors on 0 <= r^2 <= 61/67 only (AT2373, AT2386);
the outer region has the larger lower 761272835221/10^12 (AT2400 to AT2402), and the gap 61/67 < r^2 < 49/15 has no
recount, so it is not a whole-plane value. "Ceiling" is beta_* = c + 1 - q, the largest rate AT-211 allows: no
matrix recount can give more room than this column. Entries are decimals of exact rationals, rounded to 12 places;
the last row is rounded down. So at the plan of record every certified U leaves eps_rest at most 0.0063021108, and
at most 0.000938706156 - 5.2179784e-4 (U - F) if the whole-plane rate equals the regional lower.

(B) Unused free gain, for losses C ||J^(-1) g||^2. Route F-a charges the far weight part to G; the second theory agent's exact margin
(T2_CLOSURE_CHECK_v02 row B1) is G - A_far = q (s_max - s_*) >= 71675071190082633/5629499534213120000 =
0.0127320502923 at s_* = 137/125, for both cases. By the remark of AT-513, T_IS, C_tr and C_vs may share this
remainder, and a piece paid from it costs no rate and no price. It requires the strain bound s_* <= 137/125 on the
whole plane (chain item 3, now on 91 indices).

(C) Price allowance, for C_rest ||h||^2: D_lower - C_N_upper >= 8719225678 at the plan of record and
42855679131/5 = 8571135826.2 at the fallback (NEAR_CHECK_v02; AT2341); with the second theory agent's exact D_out at the plan of record
the room is >= 10089017000 (T2_CLOSURE_CHECK_v02).

## 3. One elementary bound for T_IS (CLAIMED)

Lemma TIS-FG. Put M_S = (2 pi)^(-2) int |zeta|^2 (1 + 2 <zeta>^2) ||S^(zeta)||_op d zeta. If M_S is finite, then for
every test
    |T_IS(g)| <= (q/2) M_S ||J^(-1) g||^2.
Proof. In the kernel of Lemma KER the symbol factor is (n(xi) - n(eta))^2 + (p(xi) - p(eta))^2 with p = 1/<.>.
- |p(xi) - p(eta)| = |<eta> - <xi>| p(xi) p(eta) <= |zeta| p(xi) p(eta).
- n is radial with |n'(rho)| = (1 + rho^2)^(-3/2), decreasing in rho, so |n(xi) - n(eta)| <= |zeta| P^3 with
  P = max(p(xi), p(eta)). Peetre gives P <= 2^(1/2) <zeta> P' with P' = min(p(xi), p(eta)), and P <= 1, so
  P^3 <= 2^(1/2) <zeta> P P' = 2^(1/2) <zeta> p(xi) p(eta).
- Hence the factor is at most |zeta|^2 (1 + 2 <zeta>^2) p(xi)^2 p(eta)^2 <= |zeta|^2 (1 + 2 <zeta>^2) p(xi) p(eta).
- Young's inequality for the convolution kernel ||S^(xi - eta)||_op |zeta|^2 (1 + 2<zeta>^2) acting on p |v^| gives
  |T_IS(g)| <= (q/2) M_S ||J^(-1) v||^2, and ||J^(-1) v|| = ||J^(-1) g|| (Plancherel; R commutes with J). QED.
Consequence. T_IS can be paid entirely from budget (B) if (q/2) M_S <= 0.0127320502923, that is M_S <= 0.012125762.
Since 1 + 2<zeta>^2 >= 3 and |Delta S(X)| <= M2(S) <= M_S/3 pointwise (Fourier inversion), this needs
sup |Delta S| <= 0.004041921 on the whole plane; FLOAT data on second derivatives of S at 013 decide whether that is
plausible. Otherwise T_IS needs a near and far split: the far part by this lemma with the moments of (1 - chi) S, and
the near part by Lemma HI' (high part, l = (5q/2)|zeta|^3) and an NE-lo bound (low part, priced by Lemma QW-Q).

## 4. A ceiling for the high-frequency part of T_IS + C_tr (CLAIMED, a property of Lemma HI')

Lemma HI' of T2_H4_v01 (the second theory agent's T2_NELO_v01 cites AT-361 to AT-366 as conditional confirmations of that note's
section 2, Lemmas HI, QW-Q, QW-S and Theorem H4-R; the pure high part is CONFIRMED in AT-333) bounds the
high-frequency part of T_IS + C_tr at cut mu_r >= 2 by
    phi mu_r^(-2) [(c_tr' + 5q/2) u_3 + (1 + q) 2^(q+1) T_(q+2)(ubar; mu_r/2)] ||g||^2,
with u_3 = (2 pi)^(-2) int |zeta|^3 |ubar^(zeta)| d zeta and c_tr' + 5q/2 = 10.67804022 (arb). That loss is a full
L^2 loss, so it is paid from (A). Dropping the tail term, it fits in R(U) only if
    u_3 <= R(U) mu_r^2/(phi (c_tr' + 5q/2)).
At U = F (h4rest_budget.out; the cut mu_r of these pieces may differ from the near mu, Theorem H4-R):

| mu_r | plan, regional | plan, ceiling | fallback, regional | fallback, ceiling |
|---:|---:|---:|---:|---:|
| 72 | 0.2817 | 1.891 | 2.432 | 4.041 |
| 100 | 0.5433 | 3.648 | 4.691 | 7.795 |
| 200 | 2.173 | 14.59 | 18.76 | 31.18 |
| 400 | 8.693 | 58.36 | 75.05 | 124.7 |
| 1000 | 54.33 | 364.8 | 469.1 | 779.5 |

Since |(e.grad)^3 ubar_k(X)| <= u_3 for every unit e, component k and point X, one FLOAT evaluation of the third
derivatives of ubar of 013 gives a lower for u_3 and so the smallest cut mu_r this route can use. A larger mu_r moves
the cost into the low-frequency price, which grows like kappa[Phi](mu_r)^2 (about mu_r^2.2 for order -1 pieces,
Table H4-2, FLOAT) against budget (C). This ceiling is a property of the sufficient bound, not of H4.

## 5. What each piece needs, and who would produce it

| piece | bound needed (NE form) | certified 013 inputs | theory owner | input producer |
|---|---|---|---|---|
| T_IS | Lemma TIS-FG into (B), or a near/far split: far part by TIS-FG, near part by HI' (into (A)) and NE-lo (into (C)) | M_S or the moments of chi S and (1 - chi) S; u_3; sup of S W | The first theory agent (TIS-FG), the second theory agent (NE-lo) | moments: the numerical auditor's admitted source containment, or the second theory agent's Theorem C1 panel engine extended to derivatives of ubar |
| C_tr | HI' high part into (A) (section 4); NE-lo for the low part, written as order -1 squares by Lemma POL and priced by QW-Q (kappa_(q-1)) into (C); far part into (B) if its sup norms are small | u_3, T_(q+2)(ubar; mu_r/2), sup of the third derivatives of ubar weighted by W | The second theory agent (NE-lo, T2_H4_v01 section 5) | as for T_IS; kappa_(q-1)(mu_r) upper by the NR-28/NR-29 method (the first theory agent) |
| C_vs1 | as C_tr with grad rhobar in place of ubar, composed with the bounded velocity map U | moments of grad rhobar to order 3; ||U|| on S1 (AT-181) | The second theory agent | as for C_tr |
| C_vs2 | the H^q-level commutator of J^q with the weight difference; only the L^2 tail bound of AT-214 exists | sup of grad rhobar on the far set; the commutator form is new theory | The second theory agent with the first theory agent (OPEN) | none until the form exists |
| C_vs3 | the kernel of [grad rhobar, R_a] (order -1, symmetric part order -2) in NE form; principal part already in P0 | moments of grad rhobar | The second theory agent (kernel form "straightforward and not written", T2_H4_v01) | as for C_vs1 |

Screening that decides the feasibility of the plan of record before any certified run (FLOAT, HEURISTIC use only):
u_3, M_S (or sup |Delta S|) and the order-3 moments of grad rhobar at 013. If FLOAT u_3 exceeds about 0.28 the HI'
route cannot use mu_r = 72 at the regional rate, and if it exceeds 1.89 not at any rate (section 4). Producer: a
numerics agent with the 013 evaluator (the first numerics agent or the second numerics agent); no core is assigned for it at this time (coordinator 08:49Z
item 2).

## 6. Status

- H4-REST stays OPEN. The budgets of section 2 are exact; TIS-FG and the ceiling of section 4 are CLAIMED.
- With the certified U of the second theory agent's (R4) job, the rate left for all of H4-REST at the plan of record is R(U) of
  section 2, at most 0.000938706156 at the regional lower and at most 0.006302110849 at any rate; the fallback
  leaves 0.008104144765 and 0.013467549458 at U = F.
- HEURISTIC: no 013 moment of ubar, S or grad rhobar is known even as FLOAT, and the NE-lo and NE-vs forms are not
  written. A certified H4-REST before the team stop (17:05Z) is not expected.
