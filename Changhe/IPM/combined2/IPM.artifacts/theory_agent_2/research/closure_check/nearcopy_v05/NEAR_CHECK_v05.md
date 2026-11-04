# NEAR_CHECK_v05: the near part of the final closure check at C2-N1-013, with the certified (R4) inputs (the first theory agent)

Written 2026-11-04 in a work session. It replaces NEAR_CHECK_v04 as the record with certified (R4) inputs; versions 1 to 4
stay frozen and unchanged. The program is unchanged (near_check_v03.py, SHA256
264858463e52094d5fd5fde90764d12e38af0cdc585905298ca6aca5b08dc313); only the parameter file changes. This file is a
conditional program with a dry run. The dry run still uses FLOAT, REGIONAL and OPEN stand-ins and proves nothing.

## 0. Changes against v04

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
is in SHA256SUMS_v05.

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
certified: D4 to D6 of a_n ((R1); the H4 rate needs D6(a_n) <= 63274.0 at the regional rate, against the FLOAT value
63050.4 and the certified lower 62748, AT-1467), a whole-plane beta_* (the gap 61/67 < r^2 < 49/15), and eps_rest
(H4-REST). The Lambda input is no longer a constraint: the certified U lies 4.4e-7 above the floor F and far inside
the (d) thresholds.

## 6. Consequence for the Lemma HI' route of H4-REST (not part of the near check)

At these inputs the rate left for all of H4-REST at the plan of record and the regional rate is R = 902291613/10^12.
With the numerical auditor's exact origin lower u_3 >= L = 1024389316421/10^12 (AN725; AT2457), the HI' sufficient bound needs
mu_r >= (phi K L/R)^(1/2), K = c_tr' + 5q/2 (AT2464). At this tuple the theory auditor's directed lower display of that least cut
is 140.055012371285 (AT2465, its "R4 v01 tuple"). The reading of NEAR_CHECK_v04 section 6 is unchanged: this excludes
that sufficient estimate at the cuts 72 and 100, not the near mu, a cut at least 141, the ceiling rate, the fallback,
a better rate or a different estimate (AT2466 OPEN).

## 7. The statement that would follow

As NEAR_CHECK_v03 section 6, with near_params_v04.json in place of near_params_v02.json.

## 8. What is missing before the check can pass with certified inputs

- (R1): certified whole-plane uppers of D4, D5 and D6 of a_n (thresholds in section 5).
- The H4 rate: a certified whole-plane matrix lower beta_* (the gap 61/67 < r^2 < 49/15; the completed core 49 host
  record, AT2471 to AT2473, and the conditional union theorem, AT2474 to AT2476, await the numerical auditor's recount, the matrix
  adapter and the actual reviews) and a certified eps_rest with (a') passing. At the plan of record eps_rest must fit
  in 902291613/10^12 if beta_* is the regional lower.
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H4 for the actual 013 near coefficient and the actual join, and a review of this version.
