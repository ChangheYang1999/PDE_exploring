# T2_CLOSURE_CHECK_v07: the final closure check at C2-N1-013 at the inputs of NEAR_CHECK_v08 (whole-plane D4, D5, D6 of a_n, CONFIRMED)

Written 2026-11-04 in a work session by the second theory agent. It supersedes T2_CLOSURE_CHECK_v06 for later consumers; versions 01 to 06 stay
unchanged. The program is research/closure_check/closure_check_v07.py, built from closure_check_v06.py by
scratch/mk_cc_v07.py with the changes of section 0. Its near part is the first theory agent's NEAR_CHECK_v08 (record of 14:12Z, manifest
SHA256SUMS_v08), bound by hash. This file is a conditional program with a dry run. The dry run still uses zero stand-ins
(eps_rest and C_rest; at the fallback also the three mu 68 kernel uppers, UNAUDITED), and it proves nothing. Stationary
existence, O3 and row C2 stay OPEN. All paths are relative to the agent directory of the second theory agent.

## 0. Changes against v06

1. Near binding. nearcopy_v07/ holds the first theory agent's research/closure_check/{NEAR_CHECK_v08.md, SHA256SUMS_v08,
   mk_params_v06.py, near_check_v03.py, near_check_v08.out, near_check_v08.result.json, near_params_v06.json,
   run_nc08.sh}, copied unchanged. The builder checks the 7 listed files against SHA256SUMS_v08, and inputs_v07.json
   pins all 8 hashes (row N1). The program near_check_v03.py is byte-identical to its copy in nearcopy_v06/.
2. Near inputs. D4_an, D5_an and D6_an take the values of near_params_v06.json, status CONFIRMED:
   444.194167252431246601983285, 4186.352092180269533722245282 and 63050.392730580225839237053713. These are the upper
   endpoints of the numerical auditor's executed whole-plane near consumer. The theory auditor's actual review CONFIRMS its brackets
   D4 in [444.194, 444.195], D5 in [4186.352, 4186.353] and D6 in [63050.392, 63050.393] under the admitted Schwartz and
   full-plane Plancherel theorem and the imported source-containment, analytic-tail, regularity and
   Fourier-normalization hypotheses (AT2869 to AT2871, audit_v872; adopted, numerical audit exchange v917; adoption CONFIRMED,
   AT2885, audit_v876). AT2872 (that the near inputs alone close H4, the inverse and the invariant ball) is OPEN, and
   nothing here claims it. Version 06 used the FLOAT stand-ins 444.194, 4186.35 and 63050.4. The new D4 and D5 are
   larger and D6 is smaller, so under the witness rule of the program this is a new input set: NEAR_CHECK_v08 is the
   same-input near run (row N4), and the rows of this run decide. Every other input equals inputs_v06.json.
3. Block H. H-NEARU is supplied. Its Lambda_+, ||(a_n)_+||_1 and W^2 parts cite Proposition R4 v02 as in v06, and its D4
   to D6 part cites AT2869 to AT2871. Everything else is as in v06.

## 1. Files and run

| file | role |
|---|---|
| research/closure_check/closure_check_v07.py | the program |
| research/closure_check/inputs_v07.json | every input, with sense, status and source |
| research/closure_check/closure_check_v07.out | the dry run: `python3 -B closure_check_v07.py > closure_check_v07.out` |
| research/closure_check/closure_check_v07.json | its result file |
| research/closure_check/nearcopy_v07/ | the bound near part (item 0.1) |
| research/closure_check/ps1copy/ | The first theory agent's budget_013h CE code, unchanged from v03 |
| scratch/mk_cc_v07.py | the builder of the program, the inputs and nearcopy_v07/ |
| scratch/mk_ccnote_v07.py | the writer of this note and of SHA256SUMS_v07, from the run |
| scratch/run_cc07.sh | the driver of the three steps (build, run, note) |

The SHA256 of every file is in research/closure_check/SHA256SUMS_v07. Run on core 41 at nice 19 with one thread, Python
3.12.13, python-flint 0.9.0, from 2026-11-04T14:15:15.59Z to 14:15:18.13Z (the program reports 2.4 s), exit 0.

## 2. Dry run (closure_check_v07.out; it proves nothing)

Common rows: N1, N4, A1, A1g, A2, A4, A5, B1 to B3, C1, D1 and T1 are PASS, as in v06. The far margin is unchanged,
71675071190082633/5629499534213120000 (>= 0.0127320502923).

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| e_up (printed by NEAR_CHECK_v08, exact) | 154030213826/10^12 | 181864770976/10^12 |
| N2, N3 (independent e_HF and P_HF balls against the printed values) | PASS, PASS | PASS, PASS |
| A3, G1, G2, G3 | PASS | PASS |
| E0 (HF1-NEAR conditions) | PASS | PASS |
| E2 margin beta_* - b0 - eps_rest - e_up, lower | 0.00092559168 PASS-COND | 0.0080910345 PASS-COND |
| beta_* needed by E2, b0 + eps_rest + e_up | 704030213826/10^12 + eps_rest | 696864770976/10^12 + eps_rest |
| C0 = C_rest + C_N_upper (exact) | 113428316345 | 451198667779/5 |
| D_out <= D = Z/R_*^2 | 123369792300 | 99695324090 |
| G4: C0/D_out, upper; room D_out - C0, lower | 0.91941726; 9941475900 PASS-COND | 0.90515513; 9455590500 PASS-COND |
| J1 (E2 and G4 at the original rate) | PASS-COND | PASS-COND |
| stand-ins of J1 | C_rest, eps_rest | these and kappa_0, kappa_2q, kappa_j |
| G5 companion (information) | b0 = 11/20, the original | b0 = 13/25: E2 margin 0.0030910345, C0/D_out 0.87715371 |

Against v06, E0 changes from PASS-COND to PASS at both cases, and D4_an, D5_an, D6_an leave the stand-ins of J1. The
plan e_up is lower by 24996/10^12 (about 2.4996e-8) and the fallback e_up lower by 29264/10^12 (about 2.9264e-8). The
C0, D_out, C0/D_out and room values of both cases are those of v06 (C_N_upper does not depend on D4, D5, D6). The exact
rate rooms beta_* - b0 - e_up are now 925591681/10^12 at the plan (v06: 185113337/200000000000) and 8091034531/10^12 at
the fallback (v06: 8091005267/10^12). Each v06 room is below the new one, so a price that fits a v06 room also fits the
new room. The numerical auditor's independent recomputation of the near tuple at the same inputs (numerical audit exchange v920, 14:12:53Z;
CONFIRMED for the conditional scalar arithmetic) states the same e_up and rate rooms.

## 3. What the dry run needs before any row can be PASS

At the plan of record the only stand-in inputs are now eps_rest and C_rest (zero, no bound).

- H4-REST: eps_rest and C_rest with E2 and G4 passing, that is eps_rest <= 925591681/10^12 at the plan and
  C_rest <= 9941475900 against this program's D_out. At the fallback the limits are eps_rest <= 8091034531/10^12 and
  C_rest <= 9455590500. H4-REST is OPEN at both cases; its state by piece is in notes/T2_PART7_v12.md section 5.2.
- The open hypotheses of block H: H-RC, H1, H2 (the uniform small-k inverse, O2), H-BALL, H4-REST and H-N1. H-REG is not
  needed for V11-2 (a), (b).
- For the fallback only: certified mu 68 kernel uppers kappa_0, kappa_2q, kappa_j (UNAUDITED; AT2573).

## 4. The statement that would follow

As T2_CLOSURE_CHECK_v03 section 7, with inputs_v07.json in place of inputs_v03.json and NEAR_CHECK_v08 in place of
NEAR_CHECK_v02: if every required row of one case were PASS and every hypothesis of block H were supplied, Theorem B
would give a stationary solution h = h_* + k with ||k||_2 <= R_* <= 4.54926094679e-7 and ||J^(21/10)(W k)||_2 <= M
(M = 387/1000 at the plan of record). The dry run gives CLOSURE OPEN.
