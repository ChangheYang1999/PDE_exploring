# NEAR_CHECK_v02: the near part of the final closure check at C2-N1-013 (the first theory agent)

Written 2026-11-04 in a work session, for the coordinator 07:08Z item 3(a). It replaces NEAR_CHECK_v01, which stays frozen and
unchanged. The split of the work is in the first theory agent's note 83. The first theory agent supplies this near part. The second theory agent's closure program keeps
Theorem H4-R (AT-364), the far charges, Theorem B, Lemma KB, items 8 and 9 of the theory auditor's
SOURCE013_CHAIN_CONDITIONS_v01 and the final statement. This file is a conditional program with a dry run. The dry
run uses FLOAT stand-ins and proves nothing.

## 0. Changes against v01

1. Sign of the core split (the theory auditor audit_v704: AT2298 REFUTED, AT2299 CONFIRMED, AT2300 OPEN). Since a_n(0) = -c, the
   remainder that the radial identity controls is a_r = a_n + a_c, with a_c = c/(1 + 4|x|^2), so a_n = -a_c + a_r
   (NR-30 Remark 5 applied to -a_n). v01 wrote a_n = a_c + a_r in section 2(a), in H2 and in the docstring. For that
   remainder a_n - a_c the subtraction D_m(a_r)^2 <= D_m(a_n)^2 - K_m is false (AT2298). For a_r = a_n + a_c it holds
   (AT2299). The triangle bounds M4(a_n) <= M4(a_c) + M4(a_r) and T_q(a_n; v) <= T_q(a_c; v) + T_q(a_r; v) hold for
   both signs, because the absolute Fourier moment and tail of -a_c equal those of a_c. The scalar arithmetic of v01
   already had this meaning, so no budget value changes.
2. Rounding interface (the theory auditor audit_v707: AT2307 and AT2308 REFUTED, AT2309 CONFIRMED). In v01 the printed room was
   the lower endpoint of the ball D - p for the internal price ball p, not a lower bound for D_lower - C_N_upper of the
   printed pair; and D_lower was rounded upward. v02 prints one tuple of decimals, each an exact rational, with these
   relations, which the program establishes by exact rational arithmetic on the printed values:
   - each term of e_up is the upward rounding (12 significant digits) of the upper endpoint of its ball;
   - e_up is the upward rounding of the exact sum of the printed terms;
   - c + 1 - q - b0 is printed exactly, from the rationals of the parameter file;
   - the budget margin is the downward rounding of (c + 1 - q - b0) - e_up, and (a) passes if it is >= 0;
   - C_N_upper is the upward rounding of the upper endpoint of the price ball; D_lower is the downward rounding of the
     lower endpoint of the allowance ball;
   - (b) passes if C_N_upper <= D_lower; the remaining allowance is the downward rounding of D_lower - C_N_upper, and
     P_over_D_upper the upward rounding of C_N_upper/D_lower;
   - each probe of the threshold search (c) uses the same budget interface.
   Every consumer, in particular the second theory agent's closure program, should use this tuple and no internal ball.
3. The printed values change only in the last digits from the new rounding: the plan-of-record margin is
   6.30211084899e-3 (v01 printed 6.30211084969e-3 from the ball) and the remaining allowance 8.71922567800e9 (v01
   8.71922567869e9). The thresholds 64626.7 and 65919.9 are unchanged. The parameter file is unchanged.

## 1. Files

All paths are relative to the first theory agent agent. Run with Python 3.12.13 and python-flint 0.9.0:
`python3 -B near_check_v02.py [params.json] > near_check_v02.out`.

| file | role | SHA256 |
|---|---|---|
| research/closure_check/near_check_v02.py | the program (arb, 256 bits, exact rational interface) | 0170560ec8ff6952e2c3458c35ec0a1f7ce639ef096200a186e297f6832f298b |
| research/closure_check/near_params_v01.json | every input, with direction, status and source (unchanged) | 1b5d87bddfa9ff69b3fb173d9590530919feac4c84e5d3fdb9ff513b8126f0b2 |
| research/closure_check/near_check_v02.out | the dry run at the parameters above | 65b1ad8bbbec05cd796bf82c85a625cd95dd21d72e9f60d9f657d25958c2819b |
| research/closure_check/near_check_v02.result.json | machine-readable output for the second theory agent's program | 2d4cffce6b60b12546da88c5348b4f16b4286db0562b177835f211a9e1aa319f |

The run takes under 1 s on one core. The result file records the SHA256 of the program and of the parameter file
and states the interface relations of section 0 item 2.

## 2. The two checks

Notation of HF1-NEAR (THEORY_NEW_RESULTS NR-22; AT-691): P-S1 with q = 21/10, sigma = 1 and r0 = 1/2; c is the
binary64 reference value 4076476460239181/2251799813685248; cap = c + 1 - q; a_n is the near coefficient of the split
erflog 8, rho 1 at 013. The free parameter is t = 1/10. The low cut is psi = exp(-|xi|^4) with nu = 1/40, and the
kappa_j uppers split at lam_k = 256/25.

(a) Budget inequality (R1). The program evaluates the upper

    e_up = (1 + q^2) max(Lambda_+, 8 (2c - 1))/(2 mu^2) + A4c (1024 c + M4^+(a_r))/mu^4
           + tail_B(a_c) + tail_B(a_r) + t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi))

and decides e_up <= c + 1 - q - b0 through the interface of section 0 item 2. Here:
- A4c = pi^2 (1 + c_aw/2) + C_D/2, with c_aw = 2 q^2 (sinh(x0)/x0)^2, x0 = (q/2) log 2 and C_D = 80127/40000
  (AT-428);
- tail_B(a) = (4/3)^q T_q(a; 3 mu/4) + (8/mu)^q T_q(a; mu/2) is the tail of tail B (AT-757);
- t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi)) is the low-cut term of NR-27 for the quartic cut (AT-1094, AT-1134);
- the core split is a_n = -a_c + a_r with a_c = c/(1 + 4|x|^2) and a_r = a_n + a_c (NR-30 Remark 5; AT2299). It
  uses M4(a_n) <= M4(a_c) + M4(a_r), M4(a_c) <= 1024 c (exact) and T_q(a_n; v) <= T_q(a_c; v) + T_q(a_r; v);
- M4^+(a_r) = ((D4 D6 + D5^2)/(2 pi))^(1/2), evaluated at D_m = D_m(a_r) (NR-25 (iii));
- D_m(a_n + a_c)^2 <= D_m(a_n)^2 - K_m for m = 4, 5, 6 (the radial identity, AT-1344 to AT-1346, with the endpoints
  of AT-1453 and AT-1454; AT2299);
- T_q(a_c; v) <= c pi^(1/2) v^(q + 3/2) e^(-v/2)/(2 (v - 2q - 1)) for v > 2q + 1 (NR-32; AT-1512, AT-1513);
- T_q(a_r; v) <= v^(q - 5) D6(a_r)/(4 pi (5 - q))^(1/2) (NR-25 (i) at m = 6);
- replacing Lambda_+ by max(Lambda_+, 8 (2c - 1)) only enlarges the term, so the result is again an upper.

(b) Near price and allowance. The program evaluates

    P_HF = 2^sigma [ sup(|a_n| W^2) kappa_0^Psi(mu) kappa_2q^Psi(mu)
                     + (1 - t)^-1 sup((a_n)_+ W^2) (kappa_1^Psi(nu, mu)^2 + kappa_2^Psi(nu, mu)^2) ].

Here sup(|a_n| W^2) = max(sup((a_n)_- W^2), sup((a_n)_+ W^2)). One kappa_j upper serves j = 1 and j = 2, because a
rotation by pi/2 carries one symbol to the other and the weight is radial. The program prints C_N_upper >= P_HF and
D_lower <= D, decides C_N_upper <= D_lower and prints the remaining allowance D_lower - C_N_upper, rounded down. D is
the allowance of the 013 budget: the scalar test holds for every C0 below D (the second theory agent T2_O2O3_FINAL_v02 section 0 item
3; AT-831). The remaining allowance is what remains for the far charges and the priced remainder squares of H4-R.

(c) The (R1) threshold. The program also finds the largest D6(a_n) upper on a grid of 1/10 for which (a) still
passes at the other inputs. Each probe is a full outward check through the same interface.

Monotonicity. Each term of e_up and of P_HF is nondecreasing in every upper parameter. Each is nonincreasing in the
lowers K_m, and the remaining allowance grows with D. Hence a pass stays a pass when every parameter is replaced by a
certified bound in the stated direction that is at least as good as the parameter value.

## 3. Hypotheses that the numbers do not supply (OPEN for 013)

- H1. The AT-428 hypotheses (N1) for a_n: a_n is in C^2 with bounded Hessian, a_n^ is in L^1, and M4(a_n) is finite.
  (N2) and (N3) follow once the uppers of the parameter file are certified.
- H2. The core split. a_n = -a_c + a_r on the whole plane with a_r = a_n + a_c, and the D_m(a_n) are the whole-plane
  norms of NR-25 of the actual 013 near coefficient, finite for m = 4, 5 and 6. The premises of the radial identity
  behind K_m must also hold for this a_n.
- H3. The theory auditor's condition 4 (SOURCE013_CHAIN_CONDITIONS_v01). The erflog cut is not compactly supported. The global
  assumptions of HF1-NEAR for a_n must therefore be met by an explicit decay or integrability argument, or by a
  certified truncation and remainder.
- H4. The near form enters the 013 budget as in the planning model used since theory_v10 (HF1_NEAR.md section 5;
  theory_v15 V15-4). That is, the near rate is charged against c + 1 - q - b0 and the near constant against D.
  The second theory agent's program must confirm this join with H4-R and the far form.

## 4. Parameters (near_params_v01.json, unchanged)

Directions: "upper" means a certified replacement must be at most the value; "lower" means at least the value.

| name | direction | value | status | source |
|---|---|---|---|---|
| q, sigma, r0 | exact | 21/10, 1, 1/2 | FIXED | P-S1 |
| c | exact | 4076476460239181/2251799813685248 | EXACT | Candidate 007 reference value |
| C_D | exact | 80127/40000 | EXACT | AT-428 |
| t, nu, lam_k | exact | 1/10, 1/40, 256/25 | FIXED | choices of the construction (NR-27; theory_v12 V12-1 (f) 1) |
| D4_an, D5_an, D6_an | upper | 444.194, 4186.35, 63050.4 | FLOAT | The second theory agent 2026-11-03T17:59Z; certified lower D6(a_n) >= 62748 (AT-1467) |
| K4, K5, K6 | lower | exact differences (K6 = 1863221906.74933) | CONFIRMED | AT-1453, AT-1454 |
| sup_neg_aW2, sup_pos_aW2 | upper | 8.6524467, 8.5262260 | FLOAT | The second theory agent 2026-11-03 11:32Z item 2 (erflog 8, rho 1); (R4) |
| L1_pos | upper | 4.0442822 | FLOAT | same; (R4) |
| Lambda_plus | upper | 20.862082 | FLOAT | same; (R4) |
| kappa_0, kappa_2q, kappa_j at mu 72 | upper | 3.20696761, 1059792560, 37912 | CONFIRMED | AT-1491, AT-1492; (R2) |
| kappa_0, kappa_2q, kappa_j at mu 68 | upper | 3.2126528, 836515933, 33926.469 | UNAUDITED | this agent's arb runs in research/kernel_n6/runs |
| D at b0 11/20 | lower | 1.22e11 | CONFIRMED at stipulated inputs | AT-831 (beta_0 = 7/4, norm of F_* in L^2 at most 7.97e-7, N(F_*) <= 0.006) |
| D at b0 103/200 | lower | 9.86935e10 | UNAUDITED | research/kernel_n6/b0scan/budget_b0scan3.out (same stipulated inputs) |

The stipulated inputs of D cover the certified values: the norm of F_* in L^2 is at most 7.961206656880281e-7
(AT-1413) and N_(21/10)(F_*) <= 0.0055545729030073655758 (AT-1431). beta_0 = 7/4 is a premise. For it, g_* <= 1/4
suffices (AT1690), and that is item B of the ledger.

## 5. Dry run (near_check_v02.out; FLOAT and UNAUDITED stand-ins, so it proves nothing)

All entries are the printed interface values of section 0 item 2.

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| Lambda term, upper | 1.09395477272e-2 | 1.22644064485e-2 |
| M4 term with the core split, upper | 7.67826923156e-3 | 9.65067457109e-3 |
| tail_B(a_c) (NR-32), upper | 3.34435220884e-6 | 9.16101163103e-6 |
| tail_B(a_r) (m = 6), upper | 1.34135441818e-1 | 1.58666922489e-1 |
| low-cut term, upper | 1.26049622145e-3 | 1.26049622145e-3 |
| e_up | 1.54017099351e-1 | 1.81851660742e-1 |
| c + 1 - q - b0 (exact) | 1805033838292609/11258999068426240 | 10995494028437637/56294995342131200 |
| (a) margin, lower | 6.30211084899e-3 | 1.34675494579e-2 |
| (b) C_N_upper | 1.13280774322e11 | 9.01223641738e10 |
| D_lower | 1.22000000000e11 | 9.86935000000e10 |
| C_N_upper/D_lower, upper | 9.28530937066e-1 | 9.13153998732e-1 |
| remaining allowance D_lower - C_N_upper, lower | 8.71922567800e9 | 8.57113582620e9 |
| (c) (R1) threshold for D6(a_n) | 64626.7 | 65919.9 |

For both cases an exact check of the printed tuple gives D_lower - C_N_upper - (remaining allowance) = 0, e_up at
least the sum of the printed terms, and the margin at most (c + 1 - q - b0) - e_up. The values agree with the
planning model (theory_v15 V15-0 items 1 and 2: P/D 0.9286 with the audited D and 0.9132 at the fallback; thresholds
64626 and 65919). The model used a quadrature for tail_B(a_c); here the closed form of NR-32 replaces it, and the
thresholds agree with the model to within the grid step 0.1. In both cases the uncertified inputs are D4, D5 and D6
of a_n, the two sups, ||(a_n)_+||_1 and Lambda_+. At the fallback, the kernel uppers and D are also unaudited.

## 6. The statement that would follow

Suppose H1 to H4 hold. Suppose further that, for one case (b0, mu) of the parameter file, every parameter marked
FLOAT or UNAUDITED is replaced by a certified bound in its direction at least as good as its value, and that the
program then prints PASS for (a) and (b). Then by HF1-NEAR (AT-691) with tail B (AT-757), NR-27 (AT-1094, AT-1134),
NR-25, NR-30 Remark 5 and NR-32, for every h with g = J^q W h in L^2:

    (TII + C_aw)[a_n](g) <= (c + 1 - q - b0) ||g||^2 + P ||h||^2,

where P is the printed C_N_upper. So the near constant satisfies C_N <= P <= D_lower <= D at that b0, with at least
the printed remaining allowance left for the far and remainder charges. The certified D carries the conditions of
section 4. Nothing about the far form, H4-R, the invariant ball, O3 or existence follows from this check alone.

## 7. What is missing before the check can pass with certified inputs

- (R1): certified whole-plane uppers of D4, D5 and D6 of a_n. At the FLOAT D4 and D5, D6(a_n) <= 64626.7 suffices
  at mu 72, and D6(a_n) <= 65919.9 at the fallback. The certified lower is 62748 (AT-1467).
- (R4): certified uppers of sup((a_n)_- W^2), sup((a_n)_+ W^2), ||(a_n)_+||_1 and Lambda_+(a_n).
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H3 for the actual 013 near coefficient, and H4 in the second theory agent's program.
- A review of the whole program (AT2300 OPEN; AT2309 confirms only the rounding interface).
