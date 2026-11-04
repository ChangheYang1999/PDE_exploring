# NEAR_CHECK_v04: the near part of the final closure check at C2-N1-013, at the (R4) inputs of Proposition R4 (the first theory agent)

Written 2026-11-04 in a work session. It replaces NEAR_CHECK_v03 for later consumers; versions 1 to 3 stay frozen and
unchanged. The program is unchanged (near_check_v03.py, SHA256 264858463e52094d5fd5fde90764d12e38af0cdc585905298ca6aca5b08dc313);
only the parameter file changes. The division of work is that of NEAR_CHECK_v02 (the first theory agent's note 83). This file is a
conditional program with a dry run. The dry run still uses FLOAT, UNAUDITED, REGIONAL and OPEN stand-ins and proves
nothing.

## 0. Changes against v03

1. Parameter file near_params_v03.json (new; near_params_v02.json stays frozen). Against near_params_v02.json only
   these entries change:
   - the four (R4) entries take the values of the second theory agent's Proposition R4 in its version 2 (agent the second theory agent,
     notes/T2_NEAR_R4_v02.md; values as in its research/near_r4/near_params_r4_v02.json, SHA256
     af240dc1bf0c415e4872bb8f3ba66e6282ee9745b33bdda6cfcf61f9d816a1e8), status UNAUDITED. Proposition R4 is CLAIMED
     by the second theory agent. The theory auditor confirms its method and exact assembly conditionally (AT2447 to AT2451, with the full panel
     reconstruction still required), and the numerical auditor's full local replay of version 1 is running (the numerical auditor AN727, AN728).
     Version 2 lowers three of the four values of version 1 by a finer Region II subdivision; U is unchanged;
   - the Lambda_plus source uses the wording of AT2432: F = 8(2c - 1) = 2950576553396557/140737488355328, about
     20.9651073632, is the origin value and a lower (AT2364); the former value F of near_params_v02.json was the
     uncertified target U = F, not a certified upper;
   - the beta_star source names both certified regions (r^2 <= 61/67 at 704955805507/10^12: AT2372, AT2373, AT2384
     to AT2386; r^2 >= 49/15 at 761272835221/10^12: AT2400 to AT2402). Its value and its status REGIONAL are
     unchanged, since the gap 61/67 < r^2 < 49/15 is not recounted (AT2374, AT2403 OPEN).
   The builder mk_params_v03.py makes the file from near_params_v02.json and the second theory agent's parameter file. It asserts that
   every other entry of the two files agrees, and its output is reproduced byte for byte.
2. Section 6 records what the exact origin lower of u_3 (the numerical auditor AN725; AT2456 to AT2458) implies for the cut of the
   Lemma HI' route of H4-REST at these inputs. This is not part of the near check. It uses the printed e_up of this
   run.

## 1. Files

All paths are relative to the first theory agent agent. Run with Python 3.12.13 and python-flint 0.9.0. The SHA256 of every file
is in SHA256SUMS_v04.

| file | role |
|---|---|
| research/closure_check/near_check_v03.py | the program, unchanged from v03 |
| research/closure_check/near_params_v03.json | every input, with direction, status and source |
| research/closure_check/mk_params_v03.py | builds near_params_v03.json from near_params_v02.json and the second theory agent's near_params_r4_v02.json |
| research/closure_check/near_check_v04.out | the dry run: `python3 -B near_check_v03.py near_params_v03.json > near_check_v04.out` |
| research/closure_check/near_check_v04.result.json | the result file that this run writes as near_check_v03.result.json, renamed |
| research/closure_check/hi_r4v02.py, hi_r4v02.out | section 6 (arb, 256 bits) |

The run was made in a scratch copy of the program with the identical SHA256, on core 40 at nice 19 with one thread,
from 2026-11-04T09:28:26.38Z to 09:28:26.54Z (0.16 s). The result file records the SHA256 of the program (264858...)
and of the parameter file (ccd0f57f...).

Replication. The second theory agent ran the same program on its own parameter file near_params_r4_v02.json (T2_NEAR_R4_v02 section 0
item 4). Its output research/near_r4/near_check_v03_r4v02.out (agent the second theory agent) and near_check_v04.out differ in one line
only, the name and SHA256 of the parameter file: the two parameter files differ only in source, version and
description text, and every value agrees (checked entry by entry).

## 2. The checks

Unchanged from NEAR_CHECK_v03 section 2: (a), (b), (c), (a'), (c') and (d) are exact rational comparisons of displayed
values of one outward run, with the monotonicity statement of that section.

## 3. Hypotheses that the numbers do not supply (OPEN for 013)

H1 to H4 of NEAR_CHECK_v03 section 3, unchanged.

## 4. Parameters (near_params_v03.json)

Every entry of near_params_v02.json (NEAR_CHECK_v03 section 4) is unchanged except:

| name | direction | value | status | source |
|---|---|---|---|---|
| sup_neg_aW2 | upper | 4877321332131611/562949953421312, about 8.663863106 | UNAUDITED | The second theory agent T2_NEAR_R4_v02, Proposition R4 |
| sup_pos_aW2 | upper | 4806001960566741/562949953421312, about 8.537174453 | UNAUDITED | as above |
| L1_pos | upper | 4.086439259 | UNAUDITED | as above |
| Lambda_plus | upper | U = 5901153228680477/281474976710656, with 0 <= U - F <= 4.330309019e-7 | UNAUDITED | as above; F is a lower (AT2364) |

The other non-certified inputs are as in v03: D4_an, D5_an, D6_an (FLOAT; (R1)), beta_star (REGIONAL), eps_rest
(OPEN, value 0), and for the fallback the mu 68 kernel uppers and D_allow (UNAUDITED).

## 5. Dry run (near_check_v04.out; it proves nothing)

All entries are printed interface values.

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| e_up | 154030238822/10^12 | 181864800240/10^12 |
| e_up in v03 (FLOAT (R4) values, target U = F) | 154017099351/10^12 | 181851660742/10^12 |
| Lambda term | 1.09395479531e-2 | 1.22644067018e-2 |
| e_nu term t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi)) | 1.27363546618e-3 | 1.27363546618e-3 |
| (a) cap-level margin, lower | 6.28897137799e-3 PASS | 1.34544099599e-2 PASS |
| (a') H4 rate margin at beta_* = 704955805507/10^12, eps_rest = 0, lower | 9.25566685000e-4 PASS | 8.09100526700e-3 PASS |
| (b) C_N_upper | 1.13428316345e11 | 9.02397335558e10 |
| (b) C_N_upper/D_lower, upper | 9.29740297910e-1 PASS | 9.14343229857e-1 PASS |
| (b) remaining allowance D_lower - C_N_upper, lower | 8.57168365500e9 | 8.45376644420e9 |
| (c) D6(a_n) threshold of (a) | 64623.4 | 65917.0 |
| (c') D6(a_n) threshold of (a') | 63279.8 | 64761.8 |
| (d) U threshold of (a) | 33.017 | 43.964 |
| (d) U threshold of (a') | 22.738 | 34.796 |
| required beta_* = b0 + e_up + eps_rest | 704030238822/10^12 + eps_rest | 696864800240/10^12 + eps_rest |

Against v03, e_up rises by 1.3139471e-5 at both cases. Almost all of it is the L1 term (the certified upper 4.086439259
against the FLOAT value 4.0442822); the Lambda term moves by at most 2.3e-10. U lies far inside the (d) thresholds.
The (a') rows take the regional lower 704955805507/10^12 as if it were the whole-plane beta_*, and eps_rest = 0;
neither is certified. At the plan of record the H4 rate then needs D6(a_n) <= 63279.8 (FLOAT value 63050.4; certified
lower 62748, AT-1467).

## 6. Consequence for the Lemma HI' route of H4-REST at these inputs (not part of the near check)

The rate left for all of H4-REST at these inputs is R = beta_* - b0 - e_up. Lemma HI' (T2_H4_v01; AT-362) bounds the
high part of T_IS + C_tr at cut mu_r >= 2 by phi mu_r^(-2) [K u_3 + (nonnegative tail)] ||g||^2, with
K = c_tr' + 5q/2 (about 10.6780402178) and phi = (1 + 5^(1/2))/2 (H4REST_PLAN_v01 section 4). This bound can fit in R
only if u_3 <= R mu_r^2/(phi K). The numerical auditor's exact origin jets give u_3 >= L = 1024389316421/10^12 for the unwindowed
Source013 velocity, provided its Fourier moments are finite and the nonunitary inverse derivative formulas hold
(AN725; the theory auditor AT2456, AT2457 CONFIRMED). Hence this sufficient bound needs mu_r >= (phi K L/R)^(1/2) (AT2464
CONFIRMED). From hi_r4v02.out (arb, 256 bits; displays to the digits shown):

| case and rate | R | u_3 ceiling at mu_r 72 / 100 / 140 / 200 | least mu_r |
|---|---:|---|---:|
| plan, regional lower 704955805507/10^12 | 185113337/200000000000 = 9.25566685e-4 | 0.2777 / 0.5357 / 1.0500 / 2.1428 | 138.2828 |
| plan, ceiling c + 1 - q | 6.288971378e-3 | 1.8870 / 3.6400 / 7.1344 / 14.5600 | 53.0496 |
| fallback, regional lower | 8.091005267e-3 | 2.4277 / 4.6830 / 9.1787 / 18.7320 | 46.7704 |
| fallback, ceiling | 1.345440996e-2 | 4.0369 / 7.7873 / 15.2631 / 31.1491 | 36.2694 |

The theory auditor's directed values for the version 1 tuple and for the near tuple of v03 are 140.055012371285 and 137.311617637995
(AT2465; research/h4_screen_and_origin_cutoffs_audit of agent the theory auditor). The tuple of version 2 lies between them.

Reading. At the plan of record and the regional rate, the cuts 72 and 100 cannot make this sufficient bound fit
(AT2465 for both earlier tuples; the table for this one). That excludes this estimate at these cuts, not the cut of
the near check: the cut mu_r of the H4-REST pieces may differ from the near mu (Theorem H4-R; H4REST_PLAN_v01
section 4). It also excludes nothing at mu_r >= 139 or at the ceiling rate with mu_r >= 54, nor the fallback, a
better rate, a different estimate or a coefficient split (AT2466 OPEN). A larger mu_r moves the cost into the
low-frequency price, which is charged against the remaining allowance of (b) (about 8.57e9 at the plan). The tail
term and the other pieces still share the same R.

## 7. The statement that would follow

As NEAR_CHECK_v03 section 6, with near_params_v03.json in place of near_params_v02.json.

## 8. What is missing before the check can pass with certified inputs

- (R1): certified whole-plane uppers of D4, D5 and D6 of a_n (thresholds in section 5).
- (R4): the theory auditor's audit and the numerical auditor's replay of Proposition R4 at the values of version 2 (or of version 1, whose larger
  values give e_up = 154053513894/10^12 at the plan and also pass: NEAR_CHECK_v03 program, the first theory agent's note 96).
- The H4 rate: a certified whole-plane matrix lower beta_* (the gap 61/67 < r^2 < 49/15) and a certified eps_rest
  with (a') passing. At the plan of record eps_rest must fit in 9.25566685e-4 if beta_* is the regional lower.
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H4 for the actual 013 near coefficient and the actual join, and a review of this version.
