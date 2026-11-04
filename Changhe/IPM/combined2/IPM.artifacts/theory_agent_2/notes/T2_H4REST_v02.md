# T2_H4REST_v02: addendum to T2_H4REST_v01 at the NR-34 cuts and the inputs of NEAR_CHECK_v07; errata after AT2580 to AT2587; status of each rest piece

Written 2026-11-04 in a work session by the second theory agent (completed 2026-11-04T11:07Z). For the first theory agent (publication) and the theory auditor
(audit); cc the coordinator. T2_H4REST_v01 stays unchanged. This addendum corrects three of its statements (section 1) and
replaces its budgets (section 0 there), its price tables (section 4 there) and its status table (section 5 there).
The lemmas, the field data and the routes of v01 are not repeated.

Labels as in v01: CLAIMED (proved by the second theory agent, not audited), FLOAT (binary64 observation, not a bound), HEURISTIC,
EXTRAPOLATED (a FLOAT quantity used outside its computed range), OPEN. CONFIRMED and REFUTED are the theory auditor's audit
statuses. No line of this note is a bound on eps_rest or C_rest, and H4-REST stays OPEN. All paths are relative to the
agent directory of the second theory agent.

## 0. Summary

1. Errata (section 1), all from the theory auditor's audit of v01 (AT2580 to AT2587, audit_v784):
   - the price consequence of Corollary O holds for the near-check expression with the fixed registered kernel
     constants (CONFIRMED, AT2583), and not "in every variant" (OPEN, AT2584);
   - the sentence "No window radius works" is withdrawn (REFUTED, AT2585);
   - the cuts 117 and 139 are superseded (AT2586).
2. Cuts. At the whole-plane rate the least cut of the Lemma HI' upper with K_half is 207.422143510389 at the plan of
   record and 70.154855285062 at the fallback (lower displays, NR-34 Corollary (d); CONFIRMED, AT2564 to AT2566,
   AT2599 to AT2608). These cuts use the certified lower u_3 >= L2 = 3799152003154/10^12. The same rule at the first numerics agent's
   FLOAT values of u_3 (notes 10:52Z) gives cuts of about:
   - 241 (plan) and 81.5 (fallback) from the sampled value u_3 >= 5.12321;
   - 492 (plan) and 166 (fallback) from the FLOAT upper u_3 <= 21.3616 (the first theory agent's note 104 item 3).
   These are HEURISTIC readings.
3. T_IS near part (NE-lo), route TIS-P + SW + HS (section 3).
   - Plan of record. At every cut from 208 to 241, every row costs more than (C). The cheapest row is nu = 1/40: its
     price is 2.24 to 3.05 x the closure room, and its slack 0.529 is about 39 x ((A) + (B)).
   - Fallback, slack within (A) + (B). If both budgets may be spent on T_IS alone, the price is 13.8 to 15.9 x the
     closure room at mu_r 72 to 82.
   - Fallback, frequency-separated budget of v01 section 6 (slack beta_* - b0 = 0.19). The price is 0.82 x the
     closure room at mu_r 72, 0.91 x at 76 and 1.04 x at 82. This is EXTRAPOLATED and conditional on the OPEN band
     separation of that route.
   - The HI' upper reaches mu_r 72 only if u_3 <= 4.0016, and mu_r 76 only if u_3 <= 4.4586. The sampled lower
     through the identity u_3 = 2 m_2(S) is 5.12321 (FLOAT; it certifies nothing).
4. C_vs1 + C_vs3 near part (section 4). The fixed-expression lower of Corollary O is:
   - 2.3097549e10 at the plan of record, at least 2.32 x the exact closure room 9941475955 (CONFIRMED, AT2583);
   - 1.8263687e10 at the fallback, at least 1.93 x the exact closure room 47277952671/5. This uses the fallback kernel
     values, which are UNAUDITED.
   The joint coefficient M, priced in the near-check form, costs 199 x (plan) and 166 x (fallback) the closure room
   (FLOAT).
5. So none of the sufficient estimates priced here fits at either case. In the near-check form C_vs alone costs more
   than the closure room at both cases, whatever T_IS costs. For the coordinator's request (10:54Z item 2(d)), section 5 states the status of each
   piece and the room it must fit, and section 6 names the one route the second theory agent takes.

## 1. Errata to T2_H4REST_v01

E-H4REST-v01-1 (Corollary O, scope; AT2583, AT2584).
- Text to withdraw. Section 0 item 3 says "This holds in every variant of that form, without FLOAT input". Section 2,
  Consequence, gives the bound in terms of kappa_0 and kappa_2q as if they were the kernel norms.
- Correct statement. The constants of near_params_v04.json and near_params_v05.json are registered UPPER
  certificates: kappa_0 <= A0 = 3.20696761 and kappa_2q <= A2 = 1059792560 (AT-1491, AT-1492). The price expression
  P_HF of the near check, evaluated with these fixed constants for the coefficient f = chi_n K and with a nonnegative
  second term, is at least 2 A0 A2 rhobar_y(0) >= 2.3097549e10. This fixed-expression exclusion is CONFIRMED (AT2583).
- What does not follow. Upper certificates give no lower for the true kernel norms, for the same expression with
  other valid constants, or for the actual form C_vs. That broader claim is OPEN (AT2584).
- Unchanged. The origin inequality rhobar_y(0) >= 3.397977278 is CONFIRMED (AT2583).

E-H4REST-v01-2 (far window; AT2585).
- Text to withdraw. Section 0 item 4 says "No window radius works".
- Correct statement. Up to the largest sampled radius 1.628e5, the sampled |K|_op stays above the far thresholds.
  This excludes that sampled window only.
- If a certified decay ||K(X)||_op <= C |X|^(-gamma) were available, every radius R >= (C/eps)^(1/gamma) would meet the
  far supremum threshold eps. But a small far supremum does not fit Lemma VS3-FG, which needs the Fourier moment
  M_F >= sup ||F||_op of the cut coefficient. A larger window also raises the near price.
- HEURISTIC, extrapolating the sampled exponent 0.4444 from the last unit of y (scratch/window_extrap.py and .out):
  - |K|_op would reach 6.37e-3 ((B)/2) near r = 1.5e8, 4.05e-3 ((A)/2 at the fallback) near r = 4.1e8, and 4.63e-4
    ((A)/2 at the plan) near r = 5.4e10;
  - at r = 1.5e8, |K|_op W^2 would be about 5.7e14, against sup chi_n |K|_op W^2 = 143.4 now.
- Existence of a usable combined window stays OPEN (AT2585).

E-H4REST-v01-3 (cuts; AT2586). The cuts 117 and 139 of v01 (from the first theory agent's note 102 item 5(b)) are superseded by the first theory agent
note 103 and NR-34 Corollaries (c) and (d) (AT2564 to AT2566). The v01 rows at mu_r 72, 117, 139 and 140 remain as
historical orientation only. The new cuts are in section 2.

Also: the plan (C) values in v01 used 8.40533101300e9 (NEAR_CHECK_v05/v06) and 9775123313 (closure check v05). Here
they are 8571683655 (NEAR_CHECK_v07) and the exact room 9941475955 of closure check v06. The theory auditor's audit of closure check
v06 (AT2617 to AT2621, exchange v793) CONFIRMS it as a conditional calculation and states these exact rooms; the
printed rooms 9941475900 and 9455590500 are smaller lower displays.

## 2. Budgets and cuts

| | plan of record (11/20, 72) | registered fallback (103/200, 68) |
|---|---|---|
| (A) rate room for eps_rest (NEAR_CHECK_v07, CONFIRMED AT2573, AT2574; units norm(g)^2) | 185113337/200000000000 = 9.25566685e-4 | 8091005267/10^12 = 8.091005267e-3 |
| (B) free gain (far margin; units norm(g)^2) | 0.0127320502923 | 0.0127320502923 |
| (A) + (B), if both may go to one term | 0.0136576 | 0.0208231 |
| (C) near-check allowance (NEAR_CHECK_v07; units norm(h)^2, h = W^(-1) J^(-q) g) | 8571683655 | 8453766444.2 |
| (C) closure room D_out - C0 (closure check v06, exact) | 9941475955 | 47277952671/5 = 9455590534.2 |
| beta_* - b0 (slack of the frequency-separated route) | 0.154955805507 | 0.189955805507 |
| least HI' cut, K_half, u_3 >= L2 (CONFIRMED) | 207.422143510389 | 70.154855285062 |
| least HI' cut, K_q / K (the first theory agent's note 103) | 223.601268661262 / 266.304848871307 | 75.627000950848 / 90.070316592505 |
| HI' cut, K_half, at sampled u_3 >= 5.12321 (HEURISTIC) | 240.87 | 81.47 |
| HI' cut, K_half, at FLOAT u_3 <= 21.3616 (HEURISTIC) | 491.85 | 166.35 |

The HEURISTIC rows use the scaling mu_r ~ u_3^(1/2) of the NR-34 rule mu_r >= (phi K' u_3/R)^(1/2). Read the other
way, the HI' upper with K_half fits at mu_r only if u_3 <= L2 (mu_r/mu_0)^2, with mu_0 the least cut. That gives
about:

| | mu_r 208 | mu_r 224 | mu_r 241 |
|---|---|---|---|
| plan of record | u_3 <= 3.8204 | u_3 <= 4.4307 | u_3 <= 5.1287 |

| | mu_r 72 | mu_r 76 | mu_r 82 | mu_r 88 |
|---|---|---|---|---|
| fallback | u_3 <= 4.0016 | u_3 <= 4.4586 | u_3 <= 5.1904 | u_3 <= 5.9777 |

Conditions.
- The (A) + (B) rows assume that the free gain (B) and the rate room (A) may both be spent on the HS slack of T_IS.
  In the closure check (A) is the room of the whole of eps_rest. (B) is the far margin of the closure check, which
  does not assign it to eps_rest. Whether either may be assigned to one term is a condition, not checked here.
- The beta_* - b0 rows are the frequency-separated route of v01 section 6 (OPEN). It needs that e_up is carried by
  frequencies above the low cut nu, and that the cross terms between the bands are controlled.

## 3. T_IS near part at the new cuts (research/h4rest/price_orient2.out; FLOAT)

Route: Lemma TIS-P, Lemma SW on the band (nu, mu_r), Lemma HS below nu. These lemmas are CONFIRMED under their
hypotheses (AT2580, AT2581).
- price = 2 q s_S (kv_n^2 + kv_p^2 + 2 kv_1 kv_n), with s_S = 8.38046 (FLOAT);
- slack = 21.1545 nu;
- kv_Phi <= low_Phi(nu) + high_Phi(mu_r), with high bands from kappa_rest2.out, kappa_rest3.out, kappa_rest3b.out and
  kappa_rest3c.out;
- the low band below nu = 1/100 is EXTRAPOLATED as (nu low_Phi at 1/100)/nu.
Each cell is the price, then its ratio to the near-check (C) and to the exact closure room (C).

Plan of record (mu_r 200 is below the least cut and is shown for reference):

| nu (slack) | mu_r 200 | mu_r 208 | mu_r 224 | mu_r 241 |
|---|---|---|---|---|
| 1/40 (0.5289) | 2.054e10 (2.40/2.07) | 2.229e10 (2.60/2.24) | 2.601e10 (3.03/2.62) | 3.029e10 (3.53/3.05) |
| 1/100 (0.2115) | 5.252e10 (6.13/5.28) | 5.695e10 (6.64/5.73) | 6.639e10 (7.75/6.68) | 7.726e10 (9.01/7.77) |
| 7.3249e-3 (0.155 = beta_* - b0) | 7.195e10 (8.39/7.24) | 7.799e10 (9.10/7.84) | 9.086e10 (10.60/9.14) | 1.057e11 (12.33/10.63) |
| 6.4561e-4 (0.01366 = (A) + (B)) | 9.575e11 (111.71/96.32) | 1.026e12 (119.68/103.19) | 1.171e12 (136.66/117.83) | 1.339e12 (156.22/134.69) |
| 6.0186e-4 (0.01273 = (B)) | 1.039e12 (121.26/104.55) | 1.113e12 (129.81/111.93) | 1.269e12 (148.03/127.63) | 1.449e12 (169.01/145.72) |
| 4.3753e-5 (9.256e-4 = (A)) | 4.610e13 (5378.60/4637.51) | 4.711e13 (5496.21/4738.91) | 4.926e13 (5746.67/4954.86) | 5.173e13 (6035.19/5203.63) |

Registered fallback (mu_r 68 is below the least cut and is shown for reference):

| nu (slack) | mu_r 68 | mu_r 72 | mu_r 76 | mu_r 82 | mu_r 88 | mu_r 105 | mu_r 139 | mu_r 166 |
|---|---|---|---|---|---|---|---|---|
| 1/40 (0.5289) | 2.297e9 (0.27/0.24) | 2.568e9 (0.30/0.27) | 2.855e9 (0.34/0.30) | 3.318e9 (0.39/0.35) | 3.820e9 (0.45/0.40) | 5.452e9 (0.64/0.58) | 9.674e9 (1.14/1.02) | 1.396e10 (1.65/1.48) |
| 1/100 (0.2115) | 6.204e9 (0.73/0.66) | 6.891e9 (0.82/0.73) | 7.620e9 (0.90/0.81) | 8.796e9 (1.04/0.93) | 1.007e10 (1.19/1.06) | 1.421e10 (1.68/1.50) | 2.493e10 (2.95/2.64) | 3.580e10 (4.24/3.79) |
| 8.9794e-3 (0.19 = beta_* - b0) | 6.989e9 (0.83/0.74) | 7.754e9 (0.92/0.82) | 8.566e9 (1.01/0.91) | 9.875e9 (1.17/1.04) | 1.129e10 (1.34/1.19) | 1.591e10 (1.88/1.68) | 2.784e10 (3.29/2.94) | 3.994e10 (4.72/4.22) |
| 9.8433e-4 (0.02082 = (A) + (B)) | 1.239e11 (14.66/13.11) | 1.309e11 (15.48/13.84) | 1.383e11 (16.35/14.62) | 1.502e11 (17.76/15.88) | 1.630e11 (19.29/17.24) | 2.050e11 (24.25/21.68) | 3.134e11 (37.08/33.15) | 4.234e11 (50.09/44.78) |
| 6.0186e-4 (0.01273 = (B)) | 2.731e11 (32.30/28.88) | 2.845e11 (33.65/30.08) | 2.965e11 (35.08/31.36) | 3.160e11 (37.38/33.42) | 3.371e11 (39.87/35.65) | 4.057e11 (47.99/42.90) | 5.830e11 (68.96/61.66) | 7.628e11 (90.24/80.68) |
| 3.8247e-4 (0.008091 = (A)) | 5.934e11 (70.19/62.75) | 6.112e11 (72.30/64.64) | 6.302e11 (74.55/66.65) | 6.609e11 (78.17/69.89) | 6.940e11 (82.10/73.40) | 8.019e11 (94.86/84.81) | 1.081e12 (127.87/114.32) | 1.364e12 (161.34/144.25) |

- The kv_n row of the high bands stays between 5.88 (mu 68) and 6.97 (mu 241). kv_1 grows like mu^2.081 between 68
  and 224 (FLOAT).
- The rows at nu = 1/40 and 1/100 have slacks 0.53 and 0.21. These are above every budget of section 2 at both cases,
  so those rows fit no budget pair.
- Reading at the fallback (FLOAT, EXTRAPOLATED, conditional on the OPEN route of v01 section 6). On the
  frequency-separated budget the NE-lo price of T_IS is below the closure room at mu_r 72 (0.82) and 76 (0.91), and
  just above it at 82 (1.04). The HI' upper allows mu_r 72 only if u_3 <= 4.0016; the sampled lower is 5.12321 (FLOAT).
  Where it fits, it takes most of (C), leaving little for C_tr and nothing for C_vs.
- C_tr, low part: not recomputed at the new cuts. v01 gives at most 3.93e-3 x (C) at mu_r <= 200 for the leading symbol
  (HEURISTIC). kappa_1.1 at mu 208 to 241 was not run.

## 4. C_vs1 + C_vs3 near part, both cases (research/h4rest/price_orient2.out)

Near-check form at the near cut of each case. Each case uses the kernel values of near_params_v05.json
(research/closure_check/nearcopy_v06/). The per-unit prices reproduce the split printed in near_check_v07.out to a
relative 2e-6.

| case | kappa_0, kappa_2q, kappa_j (status) | per unit: kappa_0 kappa_2q part, kappa_j part |
|---|---|---|
| plan of record | 3.20696761, 1059792560, 37912 (CONFIRMED) | 6.79744e9, 6.38809e9 |
| fallback | 3.2126528, 836515933, 33926.469 (UNAUDITED) | 5.37487e9, 5.11558e9 |

Prices (FLOAT; ratio to the near-check (C) / to the exact closure room):

| coefficient | plan of record | fallback |
|---|---|---|
| chi_n K alone (sup abs W^2 143.408) | 1.8909e12 (220.6/190.2) | 1.5044e12 (178.0/159.1) |
| chi_n M = a_n I - chi_n K, joint (151.91, lambda_max part 147.984) | 1.9779e12 (230.8/199.0) | 1.5735e12 (186.1/166.4) |
| joint, increment over the a_n price | 1.8645e12 (217.5 x near (C)) | 1.4833e12 (175.5 x near (C)) |

Corollary O, fixed expression (exact rationals; scope of E-H4REST-v01-1). rhobar_y(0) >= 3.2c - 3.1 + beta_* =
116753610257539473358201/34359738368000000000000 >= 3.397977278.
- Plan of record: 2 A0 A2 rhobar_y(0) >= 2.3097549e10. That is at least 2.69 x the near-check (C) and at least 2.32 x the
  exact closure room (CONFIRMED, AT2583).
- Fallback, with its kernel values as the fixed constants: 2 kappa_0 kappa_2q rhobar_y(0) >= 1.8263687e10. That is at
  least 2.16 x the near-check (C) and at least 1.93 x the exact closure room. The arithmetic is exact. The constants are
  UNAUDITED, so this is not a CONFIRMED exclusion.
- The joint coefficient M has no such lower: |M_11(0)| = rhobar_y(0) - c is not above sup |a_n| W^2 (v01 section 2).

## 5. Status of each rest piece at both cases (for the final report; coordinator 10:54Z item 2(d))

Rooms: rate-side pieces (units norm(g)^2) must fit (A), plus (B) only under the condition of section 2. Price-side
pieces (units norm(h)^2) must fit (C), together with the near check's own price. "Excluded" means that a named
sufficient estimate is excluded by a CONFIRMED test. The estimate, not the term, is excluded.

| piece | route | plan of record | fallback | room |
|---|---|---|---|---|
| T_IS and C_tr above mu_r | Lemma HI' with K_half (NR-34) | excluded below 207.422143510389 (AT2564 to AT2566); OPEN at or above (needs a certified upper of u_3; HEURISTIC cut about 492 with the FLOAT upper) | excluded below 70.154855285062; OPEN at or above (HEURISTIC about 166) | (A) |
| T_IS near, below mu_r (NE-lo) | TIS-P + SW + HS | forms CONFIRMED (AT2580, AT2581); no priced row fits a budget pair (FLOAT, section 3); OPEN | as at the plan if the slack must fit (A) + (B); within the closure room only on the OPEN frequency-separated route at mu_r 72 to 76 (EXTRAPOLATED); OPEN | (C), slack in (A) or (B) |
| C_tr, low | leading symbol | HEURISTIC small (v01); remainder OPEN | same | (C) |
| C_vs1 + C_vs3 near, K priced alone | near-check form, fixed constants | excluded: >= 2.3097549e10 (AT2583) | >= 1.8263687e10 with UNAUDITED constants (exact arithmetic; not CONFIRMED) | (C) |
| C_vs1 + C_vs3 near, joint M | Lemma MX into the near check | forms CONFIRMED, formal symbol only (AT2580, AT2582); matrix rate lemma OPEN; price FLOAT 199 x room | price FLOAT 166 x room; OPEN | (C) and the rate |
| T_IS, C_vs1, C_vs3 far | sup norms, Lemma VS3-FG | sampled window fails (FLOAT); a usable combined window OPEN (AT2585) | same | (A) (or (B) under the condition) |
| C_vs2 (weight commutator) | none | OPEN | OPEN | not determined |
| eps_rest, C_rest in total | closure check v06 | zero stand-ins; OPEN (AT2587) | same | (A); (C) |

## 6. Route taken (coordinator 10:54Z item 2(d))

the second theory agent takes the second OPEN route of v01 section 6: a price for the matrix coefficient of C_vs1 + C_vs3 that does not
go through sup |M| W^2 or sup |K| W^2. Reason: section 4 shows that in the near-check form C_vs costs more than the
closure room at both cases, whatever T_IS costs. The frequency-separated budget (the first route) could at most bring
the T_IS NE-lo price near the closure room at the fallback (section 3). It cannot close the rest term without a C_vs
price. The first route is not pursued now.

Content of the route, stated as a target (OPEN; nothing here is proved).
- K is first derivatives of rhobar: K_11 = -d_y rhobar, K_12 = K_21 = d_x rhobar/2, K_22 = 0. So the kernel of Lemma
  MX has the factor zeta in Khat(zeta).
- The braces of Lemma MX vanish to second order in zeta at high frequency (Remark MX-HF).
- A price that uses these two facts would carry a coefficient of rhobar or its Fourier moments, not of sup |K| W^2.
  The rate side of the joint form stays inside the scalar bound at the formal level (v01, FLOAT: sup Sig[M] 44.60
  against 50.23).
- The missing pieces are a remainder estimate for the expansion and a weighted price lemma in the style of QW-Q. The
  required size is the closure room of section 2.
- A certified result is not expected before the Part VII deadline (15:35Z). This is HEURISTIC and agrees with
  theory_v21 V21-1 (g).

## 7. Files and runs

All in research/h4rest/. SHA256 sums are in research/h4rest/SHA256SUMS_h4rest_v02. That file lists this note, the new
programs and outputs, and the inputs read from earlier runs (the v01 entries are unchanged). Every run used one thread,
nice 19 and Python 3.12.13.

| file | content | run |
|---|---|---|
| kappa_rest3.py (unchanged), kappa_rest3b.out | high bands at mu 68, 76, 208, 224 | core 40, 10:38:13.07Z, file written 10:46:25.86Z, 492.0 s |
| kappa_rest3.py (unchanged), kappa_rest3c.out | high bands at mu 82, 88, 105, 166, 241 | core 41 under timeout 1200 s, 10:56:02.26Z, file written 11:04:11.95Z, 489.0 s |
| price_orient2.py, price_orient2.out | sections 2 to 4 | core 41 under timeout 120 s, 11:05:01.59Z to 11:05:01.64Z |
| ../../scratch/window_extrap.py, .out | E-H4REST-v01-2 (HEURISTIC) | core 41 under timeout 60 s, 11:06:58.93Z |

- Core use. kappa_rest3b, the earlier v01 runs and the closure check v06 ran on core 40. Item 2(a) of the
  coordinator's 08:49Z note had given core 40 to the theory auditor's reviews, and the second theory agent noticed this only at 10:56Z. A first
  kappa_rest3c run on core 40 (start 10:55:01.07Z) was stopped after its first two lines and restarted on core 41,
  which the coordinator's 10:54Z note item 2(c) assigns to the second theory agent. Its lines agree with the restarted run (54976 and
  63621.7). The stopped output is kept as scratch/kappa_rest3c_core40_stopped.out.
- price_orient2.py reads the near-check kernel values and the printed split from
  research/closure_check/nearcopy_v06/ (near_params_v05.json, near_check_v07.out). It asserts that the split is
  reproduced. It computes Corollary O and the closure rooms in exact rationals.
