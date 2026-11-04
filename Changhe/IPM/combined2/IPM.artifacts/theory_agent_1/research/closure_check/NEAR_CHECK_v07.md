# NEAR_CHECK_v07: the near part of the final closure check at C2-N1-013, with the certified (R4) version 2 inputs and the certified whole-plane matrix lower (the first theory agent)

Written 2026-11-04 in a work session. It replaces NEAR_CHECK_v06 as the record with certified inputs; versions 1 to 6 stay
frozen and unchanged. The program is unchanged (near_check_v03.py, SHA256
264858463e52094d5fd5fde90764d12e38af0cdc585905298ca6aca5b08dc313); only the parameter file changes. This file is a
conditional program with a dry run. The dry run still uses FLOAT and OPEN stand-ins and proves nothing.

## 0. Changes against v06

1. Proposition R4 version 2 (agent the second theory agent, notes/T2_NEAR_R4_v02.md) is CONFIRMED: the theory auditor's actual review of the numerical auditor's
   complete independent refined replay (all 78 fine panels with the 368 admitted coarse panels and both tails)
   confirms the four global uppers for the exact Source013 near coefficient under the admitted exact Source013 and
   C1 containing-arithmetic hypotheses (AT2520 to AT2522, audit_v767; AT2523 OPEN), and the numerical auditor adopts that review
   (numerical audit exchange v750). The certified uppers are Lambda_+(a_n) <= 5901153228680477/281474976710656 (unchanged from
   version 1), sup((a_n)_- W^2) <= 4877321332131611/562949953421312 (at most 8.663863107), sup((a_n)_+ W^2) <=
   4806001960566741/562949953421312 (at most 8.537174453) and ||(a_n)_+||_1 <=
   21218005723912562034147590433407517/5192296858534827628530496329220096 (at most 4.086439259). They are the values
   of near_params_v03.json (NEAR_CHECK_v04), which were UNAUDITED there.
2. The whole-plane matrix lower is CONFIRMED: the theory auditor's actual review of the numerical auditor's executed complete background union
   (numerical audit exchange v749) confirms M >= (704955805507/10^12) I, |grad h| <= 1/4 and ||Sym Du||_op <= 137/125 on the
   whole plane under the admitted exact-source and containing-arithmetic hypotheses (AT2534 to AT2536, audit_v771;
   AT2537 OPEN), and the numerical auditor actually adopts that review (numerical audit exchange v755, 10:19:46Z), stating that the global
   beta input can now replace REGIONAL in a new conditional closure record. The value 704955805507/10^12 is the
   minimum of the inner, host and outer regional lowers 704955805507/10^12, 890672299617/10^12 and
   761272835221/10^12 (AT2386, AT2514, AT2402).
3. Parameter file near_params_v05.json (new). Against near_params_v03.json only statuses and source texts change:
   the four (R4) entries and beta_star take status CONFIRMED. Every value is unchanged, so every printed number equals
   that of NEAR_CHECK_v04 (near_check_v04.out), which the theory auditor reproduced by an independent 512-bit evaluation (AT2493).
4. Consequently the (a') margins of section 5 are rooms at a certified whole-plane beta_*, and at the plan of record
   the only inputs of the near check that are not certified are D4, D5 and D6 of a_n (FLOAT; (R1)) and eps_rest
   (OPEN; H4-REST).
5. Section 6 adds the least HI' cut with the T_IS coefficient q (AT-362; CLAIMED, the first theory agent research/h4rest/hi_kq_v02).

## 1. Files

All paths are relative to the first theory agent agent. Run with Python 3.12.13 and python-flint 0.9.0. The SHA256 of every file
is in SHA256SUMS_v07.

| file | role |
|---|---|
| research/closure_check/near_check_v03.py | the program, unchanged from v03 |
| research/closure_check/near_params_v05.json | every input, with direction, status and source |
| research/closure_check/mk_params_v05.py | builds near_params_v05.json from near_params_v03.json, checked entry by entry against near_params_v04.json |
| research/closure_check/near_check_v07.out | the dry run: `python3 -B near_check_v03.py near_params_v05.json > near_check_v07.out` |
| research/closure_check/near_check_v07.result.json | the result file that this run writes as near_check_v03.result.json, renamed |

The builder asserts that every entry other than the four (R4) entries agrees with near_params_v04.json (the
version 1 record, whose beta_star differs from near_params_v03 only in its source text, so beta_star is checked by
value and kind), that the four values are those certified in AT2521 and adopted in numerical audit exchange v750, that the
decimal 4.086439259 is at least the certified exact upper of ||(a_n)_+||_1 and 4.086439258 is below it, that each
version 2 value is at most its version 1 value, and that U - F = 121887363/281474976710656 < 4.330309019e-7. Its
output is reproduced byte for byte. The run was made in a scratch copy of the program with the identical SHA256, on
core 40 at nice 19 with one thread, from 2026-11-04T10:19:56.31Z to 10:19:56.63Z (0.32 s). The result file records
the SHA256 of the program (264858...) and of the parameter file (87966f8d...). Against near_check_v04.out the output
differs only in the parameter-file line and in the two lines that list the inputs that are not certified.

## 2. The checks, 3. the hypotheses

Unchanged from NEAR_CHECK_v03 sections 2 and 3: (a), (b), (c), (a'), (c') and (d) are exact rational comparisons of
displayed values of one outward run; H1 to H4 of NEAR_CHECK_v03 section 3 are not supplied by the numbers (OPEN for
013).

## 4. Parameters (near_params_v05.json)

Every entry of near_params_v03.json (NEAR_CHECK_v04 section 4) keeps its value. Changed statuses:

| name | direction | value | status | source |
|---|---|---|---|---|
| sup_neg_aW2 | upper | 4877321332131611/562949953421312, at most 8.663863107 | CONFIRMED | The second theory agent T2_NEAR_R4_v02, Proposition R4; AT2467 to AT2469, AT2520 to AT2522; numerical audit exchange v750 |
| sup_pos_aW2 | upper | 4806001960566741/562949953421312, at most 8.537174453 | CONFIRMED | as above |
| L1_pos | upper | 4.086439259 (rounded up from the certified exact upper) | CONFIRMED | as above, AT2521 |
| Lambda_plus | upper | U = 5901153228680477/281474976710656, U - F = 121887363/281474976710656 | CONFIRMED | as above, AT2522; F is a lower (AT2364) |
| beta_star | lower | 704955805507/10^12 | CONFIRMED (whole plane) | AT2534 to AT2536; numerical audit exchange v749, v755 |

The inputs that are not certified are: at the plan of record D4_an, D5_an and D6_an (FLOAT; (R1)) and eps_rest (OPEN,
value 0); at the fallback, in addition, the mu 68 kernel uppers kappa_0, kappa_2q, kappa_j and D_allow (UNAUDITED).

## 5. Dry run (near_check_v07.out; it proves nothing)

All entries are printed interface values.

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| e_up | 154030238822/10^12 | 181864800240/10^12 |
| Lambda term | 1.09395479531e-2 | 1.22644067018e-2 |
| e_nu term t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi)) | 1.27363546618e-3 | 1.27363546618e-3 |
| (a) cap-level margin, lower | 6.28897137799e-3 PASS | 1.34544099599e-2 PASS |
| (a') H4 rate margin at beta_* = 704955805507/10^12, eps_rest = 0, exact | 185113337/200000000000 PASS | 8091005267/10^12 PASS |
| (b) C_N_upper | 1.13428316345e11 | 9.02397335558e10 |
| (b) C_N_upper/D_lower, upper | 9.29740297910e-1 PASS | 9.14343229857e-1 PASS |
| (b) remaining allowance D_lower - C_N_upper, lower | 8.57168365500e9 | 8.45376644420e9 |
| (c) D6(a_n) target of (a) (sufficient) | 64623.4 | 65917.0 |
| (c') D6(a_n) target of (a') (sufficient) | 63279.8 | 64761.8 |
| (d) U targets of (a), (a') | 33.017, 22.738 | 43.964, 34.796 |
| required beta_* = b0 + e_up + eps_rest | 704030238822/10^12 + eps_rest | 696864800240/10^12 + eps_rest |

The (a') margins are exact differences of the printed values: 704955805507/10^12 - 11/20 - 154030238822/10^12 =
185113337/200000000000 = 9.25566685e-4, and 704955805507/10^12 - 103/200 - 181864800240/10^12 = 8091005267/10^12 =
8.091005267e-3. beta_* is now a certified whole-plane lower; eps_rest = 0 is a stand-in. Against NEAR_CHECK_v06 the
printed e_up is lower by 363673/15625000000 (about 2.33e-5) at both cases. The (c) and (c') values are the largest
passing values on a grid of 1/10 with the other inputs fixed, hence sufficient one-variable targets, not necessary
bounds (AT2495).

Reading. At the plan of record the near check now has two kinds of input left that are not certified: D4 to D6 of
a_n ((R1); (a') passes for every D6(a_n) upper <= 63279.8 with the other inputs fixed, a sufficient target, against
the FLOAT value 63050.4 and the certified lower 62748, AT-1467), and eps_rest (H4-REST): every full-L^2 rest loss of
the H4 join must fit in 185113337/200000000000 = 9.25566685e-4 for (a') to pass at the plan of record, and in
8091005267/10^12 at the fallback. The ceiling c + 1 - q would leave 6.28897137799e-3 and 1.34544099599e-2, but using
it in place of beta_* needs an additional principal or joint estimate (audit_v760).

## 6. Consequence for the Lemma HI' route of H4-REST (not part of the near check)

The rule of AT2439 and AT2464 (the first theory agent THEORY_NEW_RESULTS NR-34): with the numerical auditor's exact origin lower
u_3 >= L = 1024389316421/10^12 (AN725; AT2457, under finite Fourier moments and valid nonunitary inverse derivative
formulas), the HI' sufficient bound can fit in the rate room R only if mu_r >= (phi K' L/R)^(1/2). With K = c_tr' + 5q/2
(AT2464) and K_q = c_tr' + q (the T_IS coefficient q, which AT-362 confirms in place of 5q/2; CLAIMED), the first theory agent's
research/h4rest/hi_kq_v02.py (exact rationals and arb at 256 bits, directed 12-place displays; output hi_kq_v02.out;
both in research/h4rest/SHA256SUMS_v03; run on core 40 at nice 19 from 10:18:39.29Z to 10:18:39.37Z) gives:

| case and rate | R | least mu_r, K | least mu_r, K_q |
|---|---:|---:|---:|
| plan, whole-plane lower 704955805507/10^12 | 185113337/200000000000 | [138.282830152122, 138.282830152123] | [116.108348710641, 116.108348710642] |
| plan, ceiling c + 1 - q | 6.288971378e-3 | 53.049623668932 (LB) | 44.542798242881 (LB) |
| fallback, whole-plane lower | 8091005267/10^12 | 46.770377422336 (LB) | 39.270466804208 (LB) |
| fallback, ceiling | 1.345440996e-2 | 36.269351312275 (LB) | 30.453343231707 (LB) |

The K enclosure at the plan agrees with the theory auditor's (AT2496). At the plan of record and the whole-plane rate the u_3
ceilings R mu_r^2/(phi K') (arb balls in hi_kq_v02.out) put the cuts mu_r <= 138 below L and mu_r >= 139 above it
with K, and mu_r <= 116 below L and mu_r >= 117 above it with K_q; so with K the cut 140 is no longer excluded at
these inputs (the exclusion of 140 in AT2510 is at the version 1 tuple). This excludes that sufficient estimate at
the smaller cuts only, not the near mu, a larger cut, the ceiling rate, the fallback, a better rate or a different
estimate (AT2466, AT2511 OPEN). The cut mu_r of the H4-REST pieces may differ from the near mu (Theorem H4-R).

## 7. The statement that would follow

As NEAR_CHECK_v03 section 6, with near_params_v05.json in place of near_params_v02.json.

## 8. What is missing before the check can pass with certified inputs

- (R1): certified whole-plane uppers of D4, D5 and D6 of a_n (the sufficient one-variable targets of section 5).
- H4-REST: a certified eps_rest with (a') passing; at the plan of record eps_rest <= 185113337/200000000000.
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H4 for the actual 013 near coefficient and the actual join, and a review of this version.
