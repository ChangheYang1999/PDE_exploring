# NEAR_CHECK_v06: the near part of the final closure check at C2-N1-013, with the certified (R4) inputs (the first theory agent)

Written 2026-11-04 in a work session. It replaces NEAR_CHECK_v05, whose text it repeats with the wording corrections of
section 0; versions 1 to 5 stay frozen and unchanged. The program, the parameter file, the run and its outputs are
those of v05 (no new run): near_check_v03.py (SHA256 264858463e52094d5fd5fde90764d12e38af0cdc585905298ca6aca5b08dc313)
on near_params_v04.json (SHA256 b85052bce7b9eed4d41039875652dface1c0a826eab85ee0f702453ed8fd756e). This file is a
conditional program with a dry run. The dry run still uses FLOAT, REGIONAL and OPEN stand-ins and proves nothing.

## 0. Changes against v05, and errata to v04 and v05

1. Wording of the D6 thresholds (the theory auditor AT2495 REFUTED, audit_v760). The program reports in (c) and (c') the largest
   D6(a_n) upper on the grid of 1/10 at which the test passes with all other inputs fixed. Such a value is a
   sufficient one-variable target, not a necessary bound: at the inputs of NEAR_CHECK_v04, D6 = 63279.81 also passes
   (a'), with a positive enclosed margin of about 5.72e-8 (AT2495). Errata:
   - E-NC04-1: NEAR_CHECK_v04 section 5 says "At the plan of record the H4 rate then needs D6(a_n) <= 63279.8". Read
     "At the plan of record (a') passes for every D6(a_n) upper <= 63279.8, with all other inputs fixed (a sufficient
     target; the exact one-variable threshold lies above it)".
   - E-NC05-1: NEAR_CHECK_v05 section 5 says "the H4 rate needs D6(a_n) <= 63274.0 at the regional rate". Read "(a')
     passes at the regional rate for every D6(a_n) upper <= 63274.0, with all other inputs fixed (a sufficient
     target)". Section 5 below has the corrected text.
2. E-NC04-2 (audit_v760): NEAR_CHECK_v04 section 5 calls 4.086439259 "the certified upper". Read "the proposed
   outward upper of Proposition R4 version 2 (UNAUDITED, pending the replay of its 78 fine panels, AT2470)". Its table
   already gives the status UNAUDITED.
3. The theory auditor confirms NEAR_CHECK_v04 as a conditional scalar check (AT2493: the builder bytes, the near output and an
   independent 512-bit evaluation agree; AT2496: the four HI' cutoff restrictions of its section 6, with the plan
   regional least cut enclosed by 138.282830152122 and 138.282830152123; AT2497 CONFIRMED; AT2498 OPEN). The
   version 2 values stay conditional on their actual admission; only the common Hessian upper U is discharged by
   version 1 (audit_v760).
4. Everything else is the text of v05 (its section 0 is kept below as section 0'). The (a') margins and the eps_rest
   rooms are exact differences of displayed values of the run; the eps_rest room is the exact condition of the (a')
   comparison of this run with the other inputs fixed, not a property of the actual rest forms.

## 0'. Changes of v05 against v04 (unchanged)

1. Parameter file near_params_v04.json (new; near_params_v03.json stays frozen). Against near_params_v03.json only
   the four (R4) entries change. They take the values of the second theory agent's Proposition R4 in its version 1 (agent the second theory agent,
   notes/T2_NEAR_R4_v01.md, values as in its research/near_r4/near_params_r4_v01.json, SHA256
   23a900299fc35f932ccf9e1d279584f1c4f6a73221abd5581610d7c4dbe36ab5), with status CONFIRMED: the theory auditor confirms these
   four global uppers for the exact Source013 near coefficient under the admitted C1 source and containing-arithmetic
   hypotheses, after its method review (AT2447 to AT2449), the numerical auditor's complete independent replay (the numerical auditor AN730) and its
   actual review of that replay (AT2477 to AT2479, the theory auditor audit_v756). AT2480 keeps OPEN everything beyond these four
   inputs.
2. The smaller values of version 2 (NEAR_CHECK_v04) stay UNAUDITED until their 78 fine panels are replayed
   (AT2470). Every term of the program is nondecreasing in these uppers, so version 1 gives the certified record and
   version 2 can only lower e_up, by 363673/15625000000 (about 2.33e-5) at both cases.
3. The builder mk_params_v04.py makes the file from near_params_v03.json and the second theory agent's version 1 file. It asserts that
   every other entry agrees (for beta_star all fields except the source text, which near_params_v03 rewrote), that
   the four values are those certified in AT2478, that the decimal 4.161116960 is at least the certified exact upper
   21605754517791033335004488160772637/5192296858534827628530496329220096 of ||(a_n)_+||_1, and that
   U - F = 121887363/281474976710656 < 4.330309019e-7 (AT2479). Its output is reproduced byte for byte.

## 1. Files

All paths are relative to the first theory agent agent. Run with Python 3.12.13 and python-flint 0.9.0. The SHA256 of every file
is in SHA256SUMS_v05 (SHA256 52418a3b22c8229705c3c093d14c89e3af3427718e226fb9dc59e0a5de42854f), and that of this
file and of NEAR_CHECK_v05.md in SHA256SUMS_v06.

| file | role |
|---|---|
| research/closure_check/near_check_v03.py | the program, unchanged from v03 |
| research/closure_check/near_params_v04.json | every input, with direction, status and source |
| research/closure_check/mk_params_v04.py | builds near_params_v04.json from near_params_v03.json and the second theory agent's near_params_r4_v01.json |
| research/closure_check/near_check_v05.out | the dry run: `python3 -B near_check_v03.py near_params_v04.json > near_check_v05.out` |
| research/closure_check/near_check_v05.result.json | the result file that this run writes as near_check_v03.result.json, renamed |

The run was made in a scratch copy of the program with the identical SHA256, on core 40 at nice 19 with one thread,
from 2026-11-04T09:41:27.06Z to 09:41:27.22Z (0.16 s). The result file records the SHA256 of the program (264858...)
and of the parameter file (b85052bc...).

Replication. Every printed value equals that of the first theory agent's run of 09:17Z on the second theory agent's near_params_r4_v01.json (the first theory agent
note 96), which was byte-identical to the second theory agent's own run, and which the theory auditor reproduced by an independent 512-bit
evaluation (AT2449). The outputs differ only in the parameter-file line and in the two lines that list the inputs
that are not certified.

## 2. The checks, 3. the hypotheses

Unchanged from NEAR_CHECK_v03 sections 2 and 3: (a), (b), (c), (a'), (c') and (d) are exact rational comparisons of
displayed values of one outward run; H1 to H4 of NEAR_CHECK_v03 section 3 are not supplied by the numbers (OPEN for
013).

## 4. Parameters (near_params_v04.json)

Every entry of near_params_v03.json (NEAR_CHECK_v04 section 4) is unchanged except:

| name | direction | value | status | source |
|---|---|---|---|---|
| sup_neg_aW2 | upper | 2442770293098857/281474976710656, at most 8.678463435 | CONFIRMED | The second theory agent T2_NEAR_R4_v01, Proposition R4; AT2447 to AT2449, AN730, AT2477 to AT2479 |
| sup_pos_aW2 | upper | 4811915830260861/562949953421312, at most 8.547679596 | CONFIRMED | as above |
| L1_pos | upper | 4.161116960 (rounded up from the certified exact upper) | CONFIRMED | as above, AT2478 |
| Lambda_plus | upper | U = 5901153228680477/281474976710656, U - F = 121887363/281474976710656 | CONFIRMED | as above, AT2479; F is a lower (AT2364) |

The inputs that are not certified are: at the plan of record D4_an, D5_an and D6_an (FLOAT; (R1)), beta_star
(REGIONAL) and eps_rest (OPEN, value 0); at the fallback, in addition, the mu 68 kernel uppers kappa_0, kappa_2q,
kappa_j and D_allow (UNAUDITED).

## 5. Dry run (near_check_v05.out; it proves nothing)

All entries are printed interface values.

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| e_up | 154053513894/10^12 | 181888075312/10^12 |
| Lambda term | 1.09395479531e-2 | 1.22644067018e-2 |
| e_nu term t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi)) | 1.29691053832e-3 | 1.29691053832e-3 |
| (a) cap-level margin, lower | 6.26569630599e-3 PASS | 1.34311348879e-2 PASS |
| (a') H4 rate margin at beta_* = 704955805507/10^12, eps_rest = 0, exact | 902291613/10^12 PASS | 1613546039/200000000000 PASS |
| (b) C_N_upper | 1.13594668987e11 | 9.03719483185e10 |
| (b) C_N_upper/D_lower, upper | 9.31103844156e-1 PASS | 9.15682880013e-1 PASS |
| (b) remaining allowance D_lower - C_N_upper, lower | 8.40533101300e9 | 8.32155168150e9 |
| (c) D6(a_n) threshold of (a) | 64617.5 | 65912.0 |
| (c') D6(a_n) threshold of (a') | 63274.0 | 64756.8 |
| (d) U threshold of (a) | 32.973 | 43.924 |
| (d) U threshold of (a') | 22.694 | 34.756 |
| required beta_* = b0 + e_up + eps_rest | 704053513894/10^12 + eps_rest | 696888075312/10^12 + eps_rest |

The (a') margins are exact differences of the printed values: 704955805507/10^12 - 11/20 - 154053513894/10^12 =
902291613/10^12 = 9.02291613e-4, and 704955805507/10^12 - 103/200 - 181888075312/10^12 = 1613546039/200000000000 =
8.067730195e-3. They take the regional lower as if it were the whole-plane beta_*, and eps_rest = 0; neither is
certified.

Reading. With (R4) certified, the near check at the plan of record has three kinds of input left that are not
certified: D4 to D6 of a_n ((R1); (a') passes at the regional rate for every D6(a_n) upper <= 63274.0 with the other
inputs fixed, a sufficient target, against the FLOAT value 63050.4 and the certified lower 62748, AT-1467), a
whole-plane beta_* (the gap 61/67 < r^2 < 49/15), and eps_rest (H4-REST). The Lambda input is no longer a constraint:
the certified U lies 4.4e-7 above the floor F and far inside the (d) thresholds.

## 6. Consequence for the Lemma HI' route of H4-REST (not part of the near check)

At these inputs the rate left for all of H4-REST at the plan of record and the regional rate is R = 902291613/10^12.
With the numerical auditor's exact origin lower u_3 >= L = 1024389316421/10^12 (AN725; AT2457), the HI' sufficient bound can fit in R
only if mu_r >= (phi K L/R)^(1/2), K = c_tr' + 5q/2 (AT2464). At this tuple the theory auditor's directed lower display of that
least cut is 140.055012371285 (AT2465, its "R4 v01 tuple"). The first theory agent's research/closure_check/hi_r4v01.py (arb, 256
bits; output hi_r4v01.out; both in SHA256SUMS_hi_v01; run on core 40 at nice 19 at 09:43:12Z, under 1 s) evaluates
the ceilings u_3 <= R mu_r^2/(phi K) and the least cut for the four cases (decimals rounded to nearest at the digits
shown, not directed; hi_r4v01.out has ten digits):

| case and rate | R | u_3 ceiling at mu_r 72 / 100 / 140 / 200 | least mu_r |
|---|---:|---|---:|
| plan, regional lower 704955805507/10^12 | 902291613/10^12 | 0.2707 / 0.5222 / 1.0236 / 2.0889 | 140.0550 |
| plan, ceiling c + 1 - q | 6.265696306e-3 | 1.8800 / 3.6265 / 7.1080 / 14.5061 | 53.1481 |
| fallback, regional lower | 1613546039/200000000000 | 2.4207 / 4.6695 / 9.1523 / 18.6781 | 46.8378 |
| fallback, ceiling | 1.343113489e-2 | 4.0299 / 7.7738 / 15.2367 / 31.0952 | 36.3008 |

The ceiling rows use c + 1 - q in place of beta_*, an upper that no matrix recount can exceed (AT-211); they need an
additional principal or joint estimate and are not a consequence of beta_* >= b0 (audit_v760). The reading of
NEAR_CHECK_v04 section 6 is unchanged: this excludes that sufficient estimate at the cuts 72 and 100, not the near mu,
a cut at least 141, the ceiling rate, the fallback, a better rate or a different estimate (AT2466 OPEN).

## 7. The statement that would follow

As NEAR_CHECK_v03 section 6, with near_params_v04.json in place of near_params_v02.json.

## 8. What is missing before the check can pass with certified inputs

- (R1): certified whole-plane uppers of D4, D5 and D6 of a_n (the sufficient one-variable targets of section 5).
- The H4 rate: a certified whole-plane matrix lower beta_* (the gap 61/67 < r^2 < 49/15; the completed core 49 host
  record, AT2471 to AT2473, and the conditional union theorem, AT2474 to AT2476, await the numerical auditor's recount, the matrix
  adapter and the actual reviews) and a certified eps_rest with (a') passing. At the plan of record eps_rest must fit
  in 902291613/10^12 for the (a') comparison of this run if beta_* is the regional lower.
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H4 for the actual 013 near coefficient and the actual join, and a review of this version.
- Proposition R4 version 2 only: the replay of its 78 fine panels and their actual review (AT2470).
