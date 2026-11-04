# T2_CLOSURE_CHECK_v06: the final closure check at C2-N1-013 at the inputs of NEAR_CHECK_v07 (Proposition R4 v02 and the whole-plane matrix rate, both CONFIRMED)

Written 2026-11-04 in a work session by the second theory agent. It supersedes T2_CLOSURE_CHECK_v05 for later consumers; versions 01 to 05 stay
unchanged. The program is research/closure_check/closure_check_v06.py, built from closure_check_v05.py by
scratch/mk_cc_v06.py with the changes of section 0. Its near part is the first theory agent's NEAR_CHECK_v07 (the first theory agent's note 102), bound
by hash; the theory auditor reproduces that record (AT2573 to AT2576, exchange v782). This file is a conditional program with a
dry run. The dry run still uses FLOAT and zero stand-ins (D4, D5, D6 of a_n; eps_rest and C_rest; at the fallback
also the three mu 68 kernel uppers), and it proves nothing. Stationary existence, O3 and row C2 stay OPEN. All paths
are relative to the agent directory of the second theory agent.

## 0. Changes against v05

1. Near binding. nearcopy_v06/ holds the first theory agent's research/closure_check/{NEAR_CHECK_v07.md, near_check_v03.py,
   near_params_v05.json, mk_params_v05.py, near_check_v07.out, near_check_v07.result.json, SHA256SUMS_v07}, copied
   unchanged. The builder checks the six listed files against SHA256SUMS_v07, and inputs_v06.json pins all seven
   hashes (row N1).
2. Near inputs. Lambda_plus, L1_plus, sup_abs_an_W2 and sup_pos_an_W2 take the values of Proposition R4 v02
   (notes/T2_NEAR_R4_v02.md), status CONFIRMED (AT2520 to AT2522, audit_v767; adopted, numerical audit exchange v750):
   U = 5901153228680477/2^48 (unchanged from version 1), 4.086439259, 4877321332131611/2^49 (the negative-part sup,
   the larger of the two) and 4806001960566741/2^49. These are the values of closure check v04, where they were
   UNAUDITED; version 05 used the larger version 1 values.
3. Background. beta_star = 704955805507/10^12, g_star = 1/4 and s_star = 137/125 take status CONFIRMED. The theory auditor's actual
   review of the numerical auditor's executed complete background union confirms M >= (704955805507/10^12) I, |grad h| <= 1/4 and
   ||Sym Du||_op <= 137/125 on the whole plane under the admitted exact-source and containing-arithmetic hypotheses
   (AT2534 to AT2536, audit_v771; adopted, numerical audit exchange v755). The region records gain the host region
   7/9 <= r^2 <= 49/15 (kind cover, level 890672299617/10^12; AT2512 to AT2515), so the union that rows A1 and A1g
   recompute has no gap: the inner records reach r^2 = 61/67 (matrix level 704955805507/10^12) and 57/71 (cover
   level 3/5), both above 7/9. Region cutoff 2026-11-04T10:43Z.
4. Program. The notes of rows A1 and A1g follow the outcome, and a CONFIRMED input status of beta_*, g_* or s_* is
   lowered to a stand-in (REGIONAL or STANDIN-TARGET) when the union has a gap. Neither happens in this run.
5. Block H. H-B is supplied (it follows A1 and A1g, as in v05) and cites AT2534 to AT2536. H-NEARU cites Proposition
   R4 v02. H4-REST cites T2_H4REST_v01 and the HI' cuts of the first theory agent's note 103 and AT2564 to AT2569. H-RC, H2 and H-BALL
   keep status OPEN; their texts say which part runs through H-B.

## 1. Files and run

| file | role |
|---|---|
| research/closure_check/closure_check_v06.py | the program |
| research/closure_check/inputs_v06.json | every input, with sense, status and source |
| research/closure_check/closure_check_v06.out | the dry run: `python3 -B closure_check_v06.py > closure_check_v06.out` |
| research/closure_check/closure_check_v06.json | its result file |
| research/closure_check/nearcopy_v06/ | the bound near part (item 0.1) |
| research/closure_check/ps1copy/ | The first theory agent's budget_013h CE code, unchanged from v03 |
| scratch/mk_cc_v06.py | the builder of the program, the inputs and nearcopy_v06/ |

The SHA256 of every file is in research/closure_check/SHA256SUMS_v06. Run on core 40 at nice 19 with one thread,
Python 3.12.13, python-flint 0.9.0, from 2026-11-04T10:47:20.32Z to 10:47:25.16Z (the program reports 4.6 s), exit 0.

## 2. Dry run (closure_check_v06.out; it proves nothing)

Common rows: N1, N4, A1, A1g, A2, A4, A5, B1 to B3, C1, D1 and T1 are PASS. Against v05, A1 and A1g change from OPEN
to PASS, and A2, A4, A5 and B1 to B3 change from PASS-COND to PASS: their only stand-ins were beta_*, g_* and s_*.
The far margin is unchanged, 71675071190082633/5629499534213120000 (>= 0.0127320502923).

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| e_up (printed by NEAR_CHECK_v07, exact) | 154030238822/10^12 | 181864800240/10^12 |
| N2, N3 (independent e_HF and P_HF balls against the printed values) | PASS, PASS | PASS, PASS |
| A3, G1, G2, G3 | PASS | PASS |
| E0 (HF1-NEAR conditions) | PASS-COND (D4, D5, D6) | PASS-COND (D4, D5, D6) |
| E2 margin beta_* - b0 - eps_rest - e_up, lower | 0.00092556668 PASS-COND | 0.0080910052 PASS-COND |
| beta_* needed by E2, b0 + eps_rest + e_up | 704030238822/10^12 + eps_rest | 696864800240/10^12 + eps_rest |
| C0 = C_rest + C_N_upper (exact) | 113428316345 | 451198667779/5 |
| D_out <= D = Z/R_*^2 (certified f and n; beta_0* = 7/4 now CONFIRMED through A2) | 123369792300 | 99695324090 |
| G4: C0/D_out, upper; room D_out - C0, lower | 0.91941726; 9941475900 PASS-COND | 0.90515513; 9455590500 PASS-COND |
| J1 (E2 and G4 at the original rate) | PASS-COND | PASS-COND |
| stand-ins of J1 | C_rest, D4_an, D5_an, D6_an, eps_rest | these and kappa_0, kappa_2q, kappa_j |
| G5 companion (information) | b0 = 11/20, the original | b0 = 13/25: E2 margin 0.0030910052, C0/D_out 0.87715371 |

Every number equals closure check v04, which had the same input values; only statuses changed. Against v05 the
plan e_up is lower by 363673/15625000000 (about 2.33e-5, the version 2 L1 upper), the plan E2 margin rises from
0.00090229161 to 0.00092556668 and the plan room from 9775123300 to 9941475900; at the fallback the room rises from
9323375700 to 9455590500. The exact plan rate room is 185113337/200000000000 = 9.25566685e-4 and the exact fallback
rate room 8091005267/10^12, as in NEAR_CHECK_v07 and AT2573.

## 3. What the dry run needs before any row can be PASS

At the plan of record the stand-in inputs are now D4, D5 and D6 of a_n (FLOAT) and eps_rest, C_rest (zero, no bound).

- (R1): certified uppers of D4, D5, D6 of a_n. NEAR_CHECK_v07 section 5 gives the sufficient one-variable D6 target
  63279.8 for (a') at the plan (64761.8 at the fallback), against the FLOAT value 63050.4 and the certified lower
  62748 (AT-1467).
- H4-REST: eps_rest and C_rest with E2 and G4 passing, that is eps_rest <= 185113337/200000000000 at the plan and
  C_rest <= 9941475900 against this program's D_out (8571683655 against NEAR_CHECK_v07's stipulated D_lower;
  AT2573). At the fallback the limits are eps_rest <= 8091005267/10^12 and C_rest <= 9455590500. T2_H4REST_v01
  (CLAIMED lemmas, FLOAT prices) finds no estimate of the rest pieces within these price limits; C_vs is the larger
  obstruction. The Lemma HI' upper fits the rate room only for mu_r >= 207.422143510389 (K_half) at the plan and
  mu_r >= 70.154855285062 (K_half) at the fallback (AT2564 to AT2569); these restrict that sufficient upper only.
- The open hypotheses of block H: H-RC, H1, H2 (the uniform small-k inverse, O2), H-BALL, H4-REST, H-N1 and H-NEARU
  (its D4 to D6 part). H-REG is not needed for V11-2 (a), (b).
- For the fallback only: certified mu 68 kernel uppers kappa_0, kappa_2q, kappa_j (UNAUDITED; AT2573).

## 4. The statement that would follow

As T2_CLOSURE_CHECK_v03 section 7, with inputs_v06.json in place of inputs_v03.json and NEAR_CHECK_v07 in place of
NEAR_CHECK_v02: if every required row of one case were PASS and every hypothesis of block H were supplied, Theorem B
would give a stationary solution h = h_* + k with ||k||_2 <= R_* <= 4.54926094679e-7 and ||J^(21/10)(W k)||_2 <= M
(M = 387/1000 at the plan of record). The dry run gives CLOSURE OPEN.
