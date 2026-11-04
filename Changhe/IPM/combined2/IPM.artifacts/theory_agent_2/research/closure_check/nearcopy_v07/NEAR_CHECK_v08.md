# NEAR_CHECK_v08: the near part of the final closure check at C2-N1-013, with the certified whole-plane D4, D5 and D6 of a_n (the first theory agent)

Written 2026-11-04 in a work session. It replaces NEAR_CHECK_v07 as the record with certified inputs; versions 1 to 7 stay
frozen and unchanged. The program is unchanged (near_check_v03.py, SHA256
264858463e52094d5fd5fde90764d12e38af0cdc585905298ca6aca5b08dc313); only the parameter file changes. This file is a
conditional program with a dry run. At the plan of record every input except eps_rest is now certified; eps_rest is
an OPEN stand-in (value 0), so the run proves nothing about H4.

## 0. Changes against v07

1. The whole-plane near norms of a_n are certified. The numerical auditor's executed whole-plane consumer (numerical audit exchange v912; the
   sum of the seven regional Laplacian-energy records of the reviewed request 314: five complete middle blocks with
   561 annuli, the origin disk and the infinite correlated exterior) gives the strict upper endpoints
   D4(a_n) < 444.194167252431246601983285, D5(a_n) < 4186.352092180269533722245282 and
   D6(a_n) < 63050.392730580225839237053713, with lowers 444.194167252431246601983284,
   4186.352092180269533722245141 and 63050.392730580225839237008532. The theory auditor's actual review CONFIRMS the regional cover
   (AT2869), the D brackets under the admitted Schwartz and full-plane Plancherel hypotheses (AT2870) and the NR-25
   moment and tail rows (AT2871), with AT2872 OPEN (the theory auditor audit_v872, 14:00:19Z; independent guard 13:57:59Z to
   13:59:41Z, 101.86 s, 682168 assertions). The numerical auditor adopts that review (numerical audit exchange v917, 14:06:53Z; 175964
   adoption checks). Every imported source-containment, analytic-tail, regularity and Fourier-normalization
   hypothesis is retained.
2. Parameter file near_params_v06.json (new). Against near_params_v05.json only D4_an, D5_an and D6_an change: the
   FLOAT values 444.194, 4186.35 and 63050.4 are replaced by the three strict upper endpoints, status CONFIRMED.
3. Consequently, at the plan of record the only input of the near check that is not certified is eps_rest (OPEN;
   H4-REST). At the fallback the mu 68 kernel uppers kappa_0, kappa_2q, kappa_j and D_allow stay UNAUDITED.
4. The certified D4 and D5 uppers lie above the FLOAT values and the certified D6 upper lies below the FLOAT value,
   so the v07 tuple is not dominated by the v08 tuple in each input; the v07 numbers keep their v07 scope and are
   not certified bounds. Net, e_up decreases by 24996/10^12 at the plan and by 29264/10^12 at the fallback.
5. Section 6 gives the least HI' cuts at the new rate (the first theory agent research/h4rest/hi_kq_v05.py; CLAIMED, review
   requested). Every exclusion decision and every integer split of NR-34 (d) and AT2774, AT2775 is unchanged.
6. A one-term improvement of the program (the direct NR-25 moment bound for a_n) is recorded separately in
   NEAR_CHECK_v09 (new program near_check_v04.py, CLAIMED). This record keeps the reviewed program.

## 1. Files

All paths are relative to the first theory agent agent. Run with Python 3.12.13 and python-flint 0.9.0. The SHA256 of every file
is in SHA256SUMS_v08.

| file | role |
|---|---|
| research/closure_check/near_check_v03.py | the program, unchanged from v03 |
| research/closure_check/near_params_v06.json | every input, with direction, status and source |
| research/closure_check/mk_params_v06.py | builds near_params_v06.json from near_params_v05.json and checks it entry by entry |
| research/closure_check/run_nc08.sh | the run script (builder, scratch run of the unchanged program, HI' cuts) |
| research/closure_check/near_check_v08.out | the dry run: `python3 -B near_check_v03.py near_params_v06.json > near_check_v08.out` |
| research/closure_check/near_check_v08.result.json | the result file that this run writes as near_check_v03.result.json, renamed |
| research/h4rest/hi_kq_v05.py, research/h4rest/hi_kq_v05.out | the HI' cuts of section 6 (in research/h4rest/SHA256SUMS_v06) |

The builder asserts that the three old values are the FLOAT values of near_params_v05.json; that each new value is at
least the preview lower of research/near_preview/sum_v01.out and the D6 upper at least the certified lower 62748;
that the three values are the strict upper endpoints of the table of numerical audit exchange v912 and of the table of the numerical auditor
exchange v917, which names the audit IDs AT2869 to AT2872; that the theory auditor audit_v872 carries the sentence "The actual
whole-plane near assembly is independently CONFIRMED.", the IDs AT2869 to AT2872 and the verdicts CONFIRMED,
CONFIRMED, CONFIRMED, OPEN; and that every other entry equals that of near_params_v05.json. The run was made by
run_nc08.sh in a scratch copy of the program (cmp-identical), on core 41 at nice 19 with one thread, from
2026-11-04T14:08:28.69Z to 14:08:28.86Z (0.17 s); hi_kq_v05.py ran from 14:08:28.87Z to 14:08:28.95Z.
After the run the interpreter path in run_nc08.sh was replaced by the variable PYTHON (no other change). The result
file records the SHA256 of the program (264858...) and of the parameter file (96f06388...). Against
near_check_v07.out the output differs only in the parameter-file line, the D_m(a_r) uppers, the M4 and tail_B(a_r)
terms, e_up, the (a) and (a') margins and the two lines that list the inputs that are not certified.

The printed tuple equals that of the first theory agent's preview v02 (research/near_preview; the first theory agent's note 114), whose arithmetic the theory auditor
CONFIRMS independently at 512 bits (AT2881, audit_v875), apart from the two input-status lines.

## 2. The checks, 3. the hypotheses

Unchanged from NEAR_CHECK_v03 sections 2 and 3: (a), (b), (c), (a'), (c') and (d) are exact rational comparisons of
displayed values of one outward run; H1 to H4 of NEAR_CHECK_v03 section 3 are not supplied by the numbers (OPEN for
013).

## 4. Parameters (near_params_v06.json)

Every entry of near_params_v05.json (NEAR_CHECK_v07 section 4) keeps its value and status, except:

| name | direction | value | status | source |
|---|---|---|---|---|
| D4_an | upper | 444.194167252431246601983285 | CONFIRMED | whole-plane upper of D_4(a_n) = \|\|Delta^2 a_n\|\|_2 (NR-25 normalization; the full Cartesian tensor norm); numerical audit exchange v912 (executed); AT2869 to AT2871 CONFIRMED, AT2872 OPEN (audit_v872); adopted in numerical audit exchange v917 |
| D5_an | upper | 4186.352092180269533722245282 | CONFIRMED | as above, D_5(a_n) = \|\|grad Delta^2 a_n\|\|_2 |
| D6_an | upper | 63050.392730580225839237053713 | CONFIRMED | as above, D_6(a_n) = \|\|Delta^3 a_n\|\|_2 |

The inputs that are not certified are: at the plan of record eps_rest (OPEN, value 0); at the fallback, in addition,
the mu 68 kernel uppers kappa_0, kappa_2q, kappa_j and D_allow (UNAUDITED).

## 5. Dry run (near_check_v08.out; it proves nothing)

All entries are printed interface values.

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| D_m(a_r) uppers, a_r = a_n + a_c | D4 2.07324188e2, D5 1.87152173e3, D6 4.59579169e4 | the same |
| Lambda term | 1.09395479531e-2 | 1.22644067018e-2 |
| M4 term A4c (1024 c + M4^+(a_r))/mu^4 | 7.67827334295e-3 | 9.65067973862e-3 |
| tail_B(a_c) (NR-32) | 3.34435220884e-6 | 9.16101163103e-6 |
| tail_B(a_r) (NR-25 (i), m = 6) | 1.34135412711e-1 | 1.58666888057e-1 |
| e_nu term | 1.27363546618e-3 | 1.27363546618e-3 |
| e_up | 154030213826/10^12 | 181864770976/10^12 |
| (a) cap-level margin, lower | 6.28899637399e-3 PASS | 1.34544392239e-2 PASS |
| (a') H4 rate margin at beta_* = 704955805507/10^12, eps_rest = 0, exact | 925591681/10^12 PASS | 8091034531/10^12 PASS |
| (b) C_N_upper | 1.13428316345e11 | 9.02397335558e10 |
| (b) C_N_upper/D_lower, upper | 9.29740297910e-1 PASS | 9.14343229857e-1 PASS |
| (b) remaining allowance D_lower - C_N_upper, lower | 8.57168365500e9 | 8.45376644420e9 |
| (c) D6(a_n) target of (a) (sufficient) | 64623.4 | 65917.0 |
| (c') D6(a_n) target of (a') (sufficient) | 63279.8 | 64761.8 |
| (d) U targets of (a), (a') | 33.017, 22.738 | 43.964, 34.796 |
| required beta_* = b0 + e_up + eps_rest | 704030213826/10^12 + eps_rest | 696864770976/10^12 + eps_rest |

The (a') margins are exact differences of the printed values: 704955805507/10^12 - 11/20 - 154030213826/10^12 =
925591681/10^12 = 9.25591681e-4, and 704955805507/10^12 - 103/200 - 181864770976/10^12 = 8091034531/10^12 =
8.091034531e-3. The price (b), the (c), (c') and (d) targets are unchanged from v07 (the price does not involve
D4 to D6, and the grid targets do not move at these inputs). The (c) and (c') values are the largest passing values
on a grid of 1/10 with the other inputs fixed, hence sufficient one-variable targets, not necessary bounds (AT2495);
the certified D6 upper 63050.39273... lies below both.

Reading. At the plan of record the near check has one input left that is not certified: eps_rest (H4-REST). With the
certified inputs and this program, every full-L^2 rest loss of the H4 join must fit in
eps_rest <= 925591681/10^12 = 9.25591681e-4 for (a') to pass at the plan of record, and in 8091034531/10^12 at the
fallback (where the kernel uppers and D_allow are also needed). The ceiling c + 1 - q would leave 6.28899637399e-3
and 1.34544392239e-2, but using it in place of beta_* needs an additional principal or joint estimate (audit_v760).
NEAR_CHECK_v09 enlarges these rooms with a one-term program change (CLAIMED).

## 6. Consequence for the Lemma HI' route of H4-REST (not part of the near check)

The rule of NR-34 (AT2439, AT2464): the HI' sufficient bound can fit in the rate room R only if
mu_r >= (phi K' L/R)^(1/2), at a certified lower L of u_3. The first theory agent's research/h4rest/hi_kq_v05.py (exact rationals and
arb at 256 bits, directed 12-place displays; it reproduces the NEAR_CHECK_v07 cuts of NR-34 (d), AT2754, AT2774 and
AT2775 when given near_check_v07.result.json) gives at the R of section 5, with the certified origin lower
L2 = 3799152003154/10^12 (AT2564) and the strain-axis point lower u = 5123210549166463/10^15 (AT2752, AT2753;
conditional on the Fourier hypotheses):

| case | coefficient | least cut at L2 | least cut at u |
|---|---|---:|---:|
| plan, R = 925591681/10^12 | K = c_tr' + 5q/2 | [266.301253008746, 266.301253008747] | [309.243782858499, 309.243782858500] |
| plan | K_q = c_tr' + q | [223.598249416836, 223.598249416837] | [259.654686971862, 259.654686971863] |
| plan | K_half = c_tr' + q/2 | [207.419342729543, 207.419342729544] | [240.866843317484, 240.866843317485] |
| fallback, R = 8091034531/10^12 | K | [90.070153707270, 90.070153707271] | [104.594457368805, 104.594457368806] |
| fallback | K_q | [75.626864185237, 75.626864185238] | [87.822108616217, 87.822108616218] |
| fallback | K_half | [70.154728415406, 70.154728415407] | [81.467561100353, 81.467561100354] |

The K_half necessary u_3 uppers R mu_r^2/(phi K_half) are in [3.820452, 3.820453] at mu_r 208, [4.430820, 4.430821]
at 224 and [5.128876, 5.128877] at 241 (plan), and in [4.001637, 4.001638] at 72, [4.458614, 4.458615] at 76,
[5.190395, 5.190396] at 82 and [5.977755, 5.977756] at 88 (fallback). Against the point lower u: with K every tested
cut is excluded; with K_q the plan cuts 208, 224, 241 and the fallback cuts 72, 76, 82 are excluded and 88 is not;
with K_half 208, 224 (plan) and 72, 76 (fallback) are excluded and 241, 82, 88 are not. These are the decisions of
NR-34 (d), AT2754, AT2774 and AT2775 at the v07 rate; every integer split is unchanged (the least integer cuts at u
stay K 310, K_q 260, K_half 241 at the plan and K 105, K_q 88, K_half 82 at the fallback). An exclusion excludes
that sufficient estimate at that cut only, not H4-REST, a larger cut, a better rate or a different estimate.

## 7. The statement that would follow

As NEAR_CHECK_v03 section 6, with near_params_v06.json in place of near_params_v02.json.

## 8. What is missing before the check can pass with certified inputs

- H4-REST: a certified eps_rest with (a') passing; at the plan of record eps_rest <= 925591681/10^12 with this
  program (NEAR_CHECK_v09: 1164347009/(5 10^11) with near_check_v04.py, CLAIMED).
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H4 for the actual 013 near coefficient and the actual join, and a review of this version.
