# T2_CLOSURE_CHECK_v04: the final closure check at C2-N1-013 at the inputs of NEAR_CHECK_v04 (Proposition R4 v02, regional matrix rate)

Written 2026-11-04 in a work session by the second theory agent. It supersedes T2_CLOSURE_CHECK_v03 for later consumers; versions 01 to 03 stay
unchanged. The program is research/closure_check/closure_check_v04.py, a copy of closure_check_v03.py with the changes
of section 0. Its near part is the first theory agent's NEAR_CHECK_v04 (the first theory agent's note 98, frozen 09:30Z), bound by hash. This file is a
conditional program with a dry run. The dry run uses UNAUDITED, REGIONAL, FLOAT and zero stand-ins in place of open
certificates, and it proves nothing. Stationary existence, O3 and row C2 stay OPEN. All paths are relative to the
agent directory of the second theory agent.

## 0. Changes against v03

1. Near binding. nearcopy_v04/ holds the first theory agent's research/closure_check/{NEAR_CHECK_v04.md, near_check_v03.py,
   near_params_v03.json, mk_params_v03.py, near_check_v04.out, near_check_v04.result.json, hi_r4v02.py, hi_r4v02.out,
   SHA256SUMS_v04}, copied unchanged (sha256sum -c passes); inputs_v04.json pins these hashes (row N1).
2. Near inputs. Lambda_plus, L1_plus, sup_abs_an_W2 and sup_pos_an_W2 take the values of Proposition R4 v02
   (notes/T2_NEAR_R4_v02.md), status UNAUDITED: U = 5901153228680477/2^48, 4.086439259,
   4877321332131611/2^49 (the negative-part sup, the larger of the two) and 4806001960566741/2^49. The theory auditor confirms the
   method and the exact assembly conditionally (AT2467 to AT2470, v753); numerical admission and the numerical auditor's replay are
   pending.
3. Matrix rate. beta_star = 704955805507/10^12 with status REGIONAL, the value of near_params_v03.json. Version 03
   used the cover target 3/5. Every region of the cover now carries its certified matrix level and a kind (cover:
   the chain item 3 root and union certificates; matrix recount: an exact recount of the matrix lower only). Row A1
   asks for a union at level >= beta_*; the new row A1g asks for the level-3/5 cover that the targets g_* and s_* rely
   on, as A1 did in v03. The new regions are r^2 <= 61/67 at 704955805507/10^12 (AN695, AN700, AN706; AT2372, AT2373,
   AT2384 to AT2386) and r^2 >= 49/15 at 761272835221/10^12 (AT2400 to AT2402; AN717).
4. Row N4 also compares beta_star and eps_rest with near_params_v03.json (24 values).
5. Statuses. UNAUDITED, REGIONAL and STANDIN-ZERO (the value 0 for eps_rest and C_rest, which have no bound) count as
   stand-ins, so every row that uses them is at most PASS-COND.
6. Row T1 is now PASS: U >= F = 8(2c - 1), with U - F = 121887363/2^48 <= 4.330309019e-7. Block E then uses U itself as
   the Lambda_+ upper; the maximum with the origin lower F is no longer needed.
7. Block H texts name the R4 status, the regional matrix lower and the exclusions of AT2456 to AT2458 (unsplit TIS-FG)
   and AT2463 to AT2465 (the HI' cut).

## 1. Files and run

| file | role |
|---|---|
| research/closure_check/closure_check_v04.py | the program |
| research/closure_check/inputs_v04.json | every input, with sense, status and source |
| research/closure_check/closure_check_v04.out | the dry run: `python3 -B closure_check_v04.py > closure_check_v04.out` |
| research/closure_check/closure_check_v04.json | its result file |
| research/closure_check/nearcopy_v04/ | the bound near part (item 0.1) |
| research/closure_check/ps1copy/ | The first theory agent's budget_013h CE code, unchanged from v03 |

The SHA256 of every file is in research/closure_check/SHA256SUMS_v04. Run on core 40 at nice 19 with one thread,
Python 3.12.13, python-flint 0.9.0, from 2026-11-04T09:35:41.53Z to 09:35:43.91Z (2.3 s), exit 0.

## 2. Dry run (closure_check_v04.out; it proves nothing)

Common rows: N1 PASS, N4 PASS, C1 PASS, T1 PASS; A1 OPEN (gap 61/67 < r^2 < 49/15 at level beta_*); A1g OPEN (gap
57/71 < r^2 < 49/15 for the level-3/5 union; 15/17 < r^2 < 49/15 with the certified roots that have no union); A2, A4,
A5, B1 to B3, D1 PASS-COND. The far margin is unchanged, 71675071190082633/5629499534213120000 (>= 0.0127320502923).

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| e_up (printed by NEAR_CHECK_v04, exact) | 154030238822/10^12 | 181864800240/10^12 |
| N2, N3 (independent e_HF and P_HF balls against the printed values) | PASS, PASS | PASS, PASS |
| E2 margin beta_* - b0 - eps_rest - e_up, lower | 0.00092556668 PASS-COND | 0.0080910052 PASS-COND |
| beta_* needed by E2, b0 + eps_rest + e_up | 704030238822/10^12 + eps_rest | 696864800240/10^12 + eps_rest |
| C0 = C_rest + C_N_upper (exact) | 113428316345 | 451198667779/5 |
| D_out <= D = Z/R_*^2 (certified f and n; beta_0* = 7/4 a target) | 123369792300 | 99695324090 |
| G4: C0/D_out, upper; room D_out - C0, lower | 0.91941726; 9941475900 PASS-COND | 0.90515513; 9455590500 PASS-COND |
| J1 (E2 and G4 at the original rate) | PASS-COND | PASS-COND |
| G5 companion (information) | b0 = 11/20, the original | b0 = 13/25: E2 margin 0.0030910052, C0/D_out 0.87715371 |

Against v03 the two transcription rows still pass and e_up rises by 1.3139471e-5 at both cases (the certified L1
upper in place of the FLOAT value). E2 and J1 change from FAIL to PASS-COND because beta_* is now the regional lower
0.704955805507 and no longer the target 3/5. That is a change of input, not of the bounds: the rows say that the
regional value would be enough at both cases if it held on the whole plane and eps_rest were 0. Neither is
certified.

## 3. What the dry run needs before any row can be PASS

- A1: a certified matrix lower >= 704030238822/10^12 + eps_rest (plan) on the gap 61/67 < r^2 < 49/15 (AT2374, AT2403
  OPEN). On the two certified regions the levels 0.704955805507 and 0.761272835221 already exceed it at eps_rest <=
  9.25566685e-4.
- A1g: the level-3/5 cover with g_* <= 1/4 and s_* <= 137/125 on 57/71 < r^2 < 49/15.
- (R1): certified uppers of D4, D5, D6 of a_n (D6 threshold 63279.8 for E2 at the plan, NEAR_CHECK_v04 section 5).
- (R4): the admission of Proposition R4 v02 (the theory auditor numerical admission, the numerical auditor replay).
- H4-REST: eps_rest and C_rest with E2 and G4 passing, that is eps_rest <= 9.25566685e-4 at the plan if beta_* is the
  regional value, and C_rest <= 9941475900 for G4 (the allowance against this program's D_out; NEAR_CHECK_v04 uses its
  stipulated D_lower 1.22e11 and gets 8.57168365500e9). The unsplit TIS-FG route cannot fit the free gain
  (AT2456 to AT2458), and the HI' upper fits the rate room at the plan and the regional rate only for a rest cut
  mu_r of about 140 or more (AT2463 to AT2465; NEAR_CHECK_v04 section 6: 138.2828 at the v02 tuple).
- The open hypotheses of block H: H-B, H-RC, H1, H2, H-BALL, H4-REST, H-N1, H-NEARU, H-REG.
- For the fallback only: an audit of the mu 68 kernel uppers.

## 4. The statement that would follow

As T2_CLOSURE_CHECK_v03 section 7, with inputs_v04.json in place of inputs_v03.json and NEAR_CHECK_v04 in place of
NEAR_CHECK_v02: if every required row of one case were PASS and every hypothesis of block H were supplied, Theorem B
would give a stationary solution h = h_* + k with ||k||_2 <= R_* <= 4.54926094679e-7 and ||J^(21/10)(W k)||_2 <= M
(M = 387/1000 at the plan of record). The dry run gives CLOSURE OPEN.
