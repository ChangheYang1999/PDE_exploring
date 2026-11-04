# NEAR_CHECK_v03: the near part of the final closure check at C2-N1-013 (the first theory agent)

Written 2026-11-04 in a work session. It replaces NEAR_CHECK_v02 for later consumers; versions 1 and 2 stay frozen and
unchanged. The division of work is that of NEAR_CHECK_v02 (the first theory agent's note 83): the first theory agent supplies the near part, and the second theory agent's
closure program keeps Theorem H4-R (AT-364), the far charges, Theorem B, Lemma KB and the final statement. This file
is a conditional program with a dry run. The dry run uses FLOAT, TARGET, REGIONAL and OPEN stand-ins and proves
nothing.

## 0. Changes against v02

1. The Lambda contract (the theory auditor audit_v724: AT2364 CONFIRMED, AT2365 REFUTED, AT2366 OPEN). The exact near
   coefficient has Hess a_n(0) = diag(8(2c - 1), 8), so Lambda_+(a_n) = sup_x max(0, lambda_max(Hess a_n(x))) is at
   least F = 8(2c - 1) = 2950576553396557/140737488355328 = 20.9651073632 (AT2364). near_params_v01.json gave
   Lambda_plus the FLOAT value 20.862082 as an upper, which no certified bound can replace (AT2365), and its source
   line called max(Lambda_plus, 8 (2c - 1)) "again an upper", which holds only when Lambda_plus is a certified upper
   (AT2366). near_params_v02.json sets Lambda_plus to F with the new status TARGET: at that value a certified
   replacement must prove that the supremum is attained at the origin. The program prints whether the parameter value
   is at least F and, in (d), the largest U on a grid of 1/1000 at which each budget test passes. Any certified
   global upper U >= F at most that threshold serves. The formula of the Lambda term is unchanged; for U >= F the
   maximum in it equals U, so every printed value of v02 is unchanged at U = F.
2. The H4 rate test (the theory auditor audit_v715: AT2333 CONFIRMED, AT2334 REFUTED, AT2335 CONFIRMED, AT2336 OPEN). In the H4
   join the principal part gives -beta_* ||g||^2, and the near loss and every other full-L^2 loss eps_rest are paid
   from it, so the H4 step at rate b0 needs e_up + eps_rest <= beta_* - b0 with a certified whole-plane matrix rate
   beta_* (reading (ii)). Test (a') decides this through the same rational interface, with beta_* (a lower) and
   eps_rest (an upper) as named parameters, and (c') prints its D6(a_n) threshold. The cap-level test (a),
   e_up <= c + 1 - q - b0, is kept: it is the case beta_* = c + 1 - q, the largest rate that AT-211 allows, and the
   near-form inequality of section 6 uses it.
3. Hypothesis H4 of v02 (the near rate charged against c + 1 - q - b0) is replaced by the join of AT2333 (section 3).
4. New statuses in the parameter file: TARGET (a value that a certified replacement must meet; no bound at this
   value is known), REGIONAL (certified on a stated region only) and OPEN (no bound is known). Only FIXED, EXACT and
   CONFIRMED count as certified.

## 1. Files

All paths are relative to the first theory agent agent. Run with Python 3.12.13 and python-flint 0.9.0:
`python3 -B near_check_v03.py [params.json] > near_check_v03.out`. The SHA256 of every file is in SHA256SUMS_v03.

| file | role |
|---|---|
| research/closure_check/near_check_v03.py | the program (arb, 256 bits, the exact rational interface of v02) |
| research/closure_check/near_params_v02.json | every input, with direction, status and source |
| research/closure_check/near_check_v03.out | the dry run at the parameters above |
| research/closure_check/near_check_v03.result.json | machine-readable output for the second theory agent's program |

The run takes under 1 s on one core. The result file records the SHA256 of the program and of the parameter file,
the interface relations, the Lambda contract and the H4 parameters.

## 2. The checks

(a), (b) and (c) are those of NEAR_CHECK_v02 section 2, with the interface of its section 0 item 2: e_up is the
upward rounding of the exact sum of the displayed term uppers, and every pass is an exact rational comparison of
displayed values. In addition:

(a') H4 rate. The H4 margin is the downward rounding of (beta_* - b0 - eps_rest) - e_up, computed exactly from the
rationals of the parameter file and the displayed e_up; (a') passes if it is >= 0.

(c') The largest D6(a_n) upper on a grid of 1/10 at which (a') passes at the other inputs.

(d) The largest U on a grid of 1/1000, starting from F, at which (a) passes, and the same for (a'), with U in place
of Lambda_plus and the other inputs unchanged. Each probe is a full outward check through the same interface.

Monotonicity. Each term of e_up and of P_HF is nondecreasing in every upper parameter (including U and eps_rest) and
nonincreasing in the lowers K_m and beta_*, and the remaining allowance grows with D. Hence a pass stays a pass when
every parameter is replaced by a certified bound in the stated direction that is at least as good as the parameter
value. This is a statement about the terms and the outward rounding of one run; it does not compare a changed input
with an old pinned output (AT2354, AT2369).

## 3. Hypotheses that the numbers do not supply (OPEN for 013)

- H1 to H3 as in NEAR_CHECK_v02 section 3: the AT-428 hypotheses (N1) for a_n; the core split a_n = -a_c + a_r with
  a_r = a_n + a_c and the whole-plane D_m(a_n) of the actual 013 near coefficient, with the premises of the radial
  identity; the theory auditor's condition 4 for a cut that is not compactly supported.
- H4. The join of the near form with H4-R and the far form in the composition of AT2333: the principal part
  contributes -beta_* ||g||^2 with a certified whole-plane matrix rate beta_*, the near loss and eps_rest are paid
  from it, the near constant is charged against D, and the literal strict and tail hypotheses of H4-R are retained.

## 4. Parameters (near_params_v02.json)

Every entry of near_params_v01.json is unchanged (NEAR_CHECK_v02 section 4) except:

| name | direction | value | status | source |
|---|---|---|---|---|
| Lambda_plus | upper | 2950576553396557/140737488355328 = 8(2c - 1) | TARGET | AT2364 to AT2366; a certified global upper U at most the threshold (d) serves |
| beta_star | lower | 704955805507/10^12 | REGIONAL | AT2372, AT2373, AN700: certified on t in [0, 17/64] union [35/128, 61/128] only (AT2374 OPEN) |
| eps_rest | upper | 0 | OPEN | the remainder pieces T_IS, C_tr and C_vs1 to C_vs3 of H4-R (H4-REST); no 013 bound |

## 5. Dry run (near_check_v03.out; it proves nothing)

All entries are printed interface values. The rows of NEAR_CHECK_v02 section 5 (the five terms, e_up, the cap-level
margin, the price, the allowance and the D6 threshold of (a)) are reproduced digit for digit.

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| e_up | 1.54017099351e-1 | 1.81851660742e-1 |
| (a) cap-level margin, lower | 6.30211084899e-3 | 1.34675494579e-2 |
| (a') H4 rate margin at beta_* = 0.704955805507, eps_rest = 0, lower | 9.38706156000e-4 | 8.10414476500e-3 |
| (b) C_N_upper/D_lower, upper | 9.28530937066e-1 | 9.13153998732e-1 |
| (c) D6(a_n) threshold of (a) | 64626.7 | 65919.9 |
| (c') D6(a_n) threshold of (a') | 63283.0 | 64764.6 |
| (d) U threshold of (a) | 33.042 | 43.986 |
| (d) U threshold of (a') | 22.764 | 34.818 |

The (a') rows take the regional lower of AT2373 as if it were the whole-plane beta_*, and eps_rest = 0; neither is
certified. At the plan of record the H4 rate then needs D6(a_n) <= 63283.0 (the FLOAT value is 63050.4 and the
certified lower 62748, AT-1467) and a certified global Hessian upper within about 1.80 of the origin value 20.965.
At beta_* = 3/5 the test (a') fails at both cases for every D6(a_n) upper (theory_v20 V20-4 (e) 2).

## 6. The statement that would follow

Suppose H1 to H3 hold. Suppose further that, for one case (b0, mu), every parameter marked FLOAT, UNAUDITED, TARGET,
REGIONAL or OPEN is replaced by a certified bound in its direction at least as good as its value, and that the
program then prints PASS for (a) and (b). Then, as in NEAR_CHECK_v02 section 6, for every h with g = J^q W h in L^2,

    (TII + C_aw)[a_n](g) <= (c + 1 - q - b0) ||g||^2 + P ||h||^2,

with P the printed C_N_upper, so C_N <= P <= D_lower <= D at that b0. If moreover H4 holds and (a') prints PASS with
a certified whole-plane beta_* and a certified eps_rest, then the near loss fits the H4 rate budget at rate b0
(AT2333). Nothing about the far form, the remainder pieces of H4-R, the invariant ball, O3 or existence follows
from this check alone.

## 7. What is missing before the check can pass with certified inputs

- (R1): certified whole-plane uppers of D4, D5 and D6 of a_n (thresholds in section 5).
- (R4): certified uppers of sup((a_n)_- W^2), sup((a_n)_+ W^2) and ||(a_n)_+||_1, and a certified global upper of
  Lambda_+(a_n) at least 8(2c - 1) and at most the threshold (d).
- The H4 rate: a certified whole-plane matrix lower beta_* and certified eps_rest with (a') passing.
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H4 for the actual 013 near coefficient and the actual join, and a review of this version.
