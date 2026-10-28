# Robustness group (i): why the R0 re-expanded warm starts failed, and a corrected-start proposal (numerics, shift 10, 2026-10-26T17:42Z)

Scope: the Stage II robustness registration reports/STAGE2_ROBUSTNESS_REGISTRATION_20261026.md, group (i) (St-A = nest6 (0.45, 1) p0, c_l 0.45,
omega 1, omega/c_l 20/9; R0 0.3 -> 0.6 and 0.15) and the held groups (ii) and (iv) (St-B at omega 0.3, omega/c_l 2/3; St-C = cont150 at L8).
Lead rules: the reply message of 2026-10-26 (shift 10) and d128 HT item 5. Nothing in this file is a reading of R0 sensitivity. CPU only.

## 1. What happened (primary-reported)
- s5r0_L6_cl0.45_om+1.0_fixed_R0p6: LM status xtol after one accepted step (12 s); max|U| 1.229 -> 15.25, holdout rho_u^max 0.8875 / 0.8889. Failed re-solve.
- s5r0_L6_cl0.45_om+1.0_fixed_R0p15: LM status xtol after one accepted step (11 s); rms_mom 0.0935 -> 0.2045, a_max 3.38. Failed re-solve.
- The control s5ctl_L6_cl0.45_om+1.0_fixed_R0p3_ctl ran its 300 iterations normally (battery at the time of writing).

## 2. Mechanism (scripts/block_costs.py and scripts/fix_reexpanded_start.py, CPU; reports/block_costs/)
The worker's non-PDE cost block is the closure rows plus the gauge rows (far anchor rows are PDE rows under far_merged).

| start | pde cost | closure cost (m) | gauge cost | coefficient norms A / C / B / D / E |
|---|---|---|---|---|
| control St-A at R0 0.3 | 2.68e-7 | 4.8e-9 (0.346) | 0 | 64 / 3.4 / 1.2e7 / 5.4e4 / 1.1e4 |
| re-expanded R0 0.6 (rcond 1e-12, all channels) | 4.48e-8 | 3.70e-1 (3049) | 6.2e-5 | 6.6e5 / 1.8e6 / 7.8e6 / 1.4e8 / overflow |
| re-expanded R0 0.15 (rcond 1e-12, all channels) | 2.79e-5 | 4.6e-5 (34) | 2.4e-5 | 7.1e9 / 7.9e8 / 6.4e11 / 3.7e10 / overflow |
| re-expanded om0.3 R0 0.6 (St-B) | see JSON | 11.6 (17083) | | |

Zeroing the B/D/E coefficients of the R0 0.6 start changes U on the training grid by a relative 2.1e6 (max|U| 1.227 -> 3.7e6). The fit with all
channels (condition numbers 1e25-1e26, rcond 1e-12 after column scaling) therefore represents the parent velocity as a catastrophically cancelling
combination of enormous components; the velocity on the fit grid is reproduced (fit error 2.6e-2) but the representation is numerically meaningless:
the closure rows see a carried first correction with mismatch 3049, the LM's first step follows them and the amplitude blows up (R0 0.6), or the
state is thrown off and the step size collapses to xtol (R0 0.15). The E channel coefficients overflow the double range in norm. The 'zeroed' and
'closure-consistent' corrections of THESE fits are meaningless because their A/C part alone is garbage.

## 3. Corrected start rule (lead criterion (iii)): regularized A/C-only re-fit, B/D/E zero by construction
scripts/reexpand_state.py SRC --R0 X --channels 0,0,0 --rcond RC (the A/C columns only; the destination job's channels 4/4/4 are filled with zeros
by the worker's embed_state, so the carried B/D/E coefficients are 0 by the stated rule). Results for St-A (reports/block_costs/refit_*.json,
compare_parent_vs_refit_*.json):

| refit | fit error (rel L2 on the fit grid / max pointwise) | condition, rank | pde cost | closure cost (m) | gauge cost (int F^2) | A / C norms | compare_fields vs parent: norm_star_U, norm_star1 (DU, Omega) |
|---|---|---|---|---|---|---|---|
| R0 0.6, rcond 1e-6 | 3.61e-2 / 0.12 (worst radius 0.57, rel 9.3e-2) | 8.5e3, 672 of 672 | 9.4e-9 | 4.0e-8 (1.0) | 2.3e-4 (0.99957) | 47.5 / 1.78 | 0.0781, 0.308 / 0.328 (gauge-aligned angle 1e-4) |
| R0 0.6, rcond 1e-3 | 3.62e-2 / 0.12 | 8.5e3, 643 of 672 | (same to 3 digits) | | (0.99964) | | |
| R0 0.15, rcond 1e-6 | 2.47e-2 / 0.12 (worst radius 0.55, rel 9.3e-2) | 8.5e3, 672 of 672 | 2.83e-5 | 4.0e-8 (1.0) | 7.0e-4 (1.00075) | 1.1e5 / 1.0e3 (the basis scale at R0 0.15 differs; the fit is well conditioned) | 0.0783, 0.308 / 0.328 (aligned angle = the period, identity) |

Reading: with the channel columns removed the fit is well conditioned (8.5e3) and the coefficients are of the control's size; the fit error 3.6e-2 is
the same at rcond 1e-6 and 1e-3, so it is the representability limit of the basis change (a different twist radius changes the function space), not
a conditioning artefact. The closure rows cost 4e-8 with m = 1 (no carried correction, by the rule), the gauge row 2.3e-4 (int |F|^2 - 1 = -4.3e-4,
inside the registered warm-start gauge rule 0.02), the PDE block 9.4e-9.

## 4. The lead's criteria, literally
- (i) relative change of U on the holdout nodes at most 1e-6 and both holdouts within 1 per cent of the parent's: NOT MET and not attainable by any
  re-expansion across an R0 change at fixed L6 Nk16: compare_fields norm_star_U 0.078 (max over shells of the shell-RMS ratio), 0.31 for DU. The worker
  holdout of the fitted start is unevaluated (a CPU evaluation takes about 15 min per state and would only confirm a difference of order 1e-2).
- (ii) gauge, pivot and closure row costs at most 2x the parent's: NOT MET literally (the parent's gauge cost is 0 and its closure cost 4.8e-9 with the
  carried correction present; the refit has 2.3e-4 and 4.0e-8 with m = 1 by the rule). Relative to the PDE cost both are what the LM removes in its
  first iterations without a visible excursion in the earlier arms (the S7 (c) and all-m arms started with gauge rows of this size).
- (iii) B/D/E from a stated rule: MET (zero).

## 5. Proposal (the lead decides; nothing runs without a dated note)
Option A: accept the regularized A/C-only refit (rcond 1e-6) as the group (i)/(ii)/(iv) WARM START with the fit error recorded as the start's distance
(3.6e-2 at R0 0.6, 2.5e-2 at R0 0.15; compare_fields norm_star_U 0.078 for both), under the registration's existing reading (variant against its re-solved control after the solve, the field
difference beside the control's own drift, the 'within / above the residual level' flag). It tests whether the LM at the other twist radius returns to
the same floor state from a start 3.6e-2 away. Budget as registered (L6 about 1.2 GPU-h per variant; L8 about 4.5 GPU-h); the L8 refits of cont150
would be produced the same way (CPU, about 10 min each) before launch; all variants end before 2026-10-27T16:30Z.
Option B (the lead's default): record group (i), (ii) and (iv) R0 variants as 'R0 re-expansion failed; sensitivity to R0 not tested' and give the GPU
time back to the R1 to R4 list. The far-anchor variants (group (iii)) and all controls are unaffected either way.
Numerics recommendation: Option A for the two L6 branches only (about 2.5 GPU-h in total, four variants), Option B for the L8 pair unless the lead wants
them at 9 GPU-h; if criterion (i) is kept at 1e-6, Option B for all.

## 6. Appendix (2026-10-26T17:49Z): R0 0.15 numbers appended (reports/block_costs/refit_nest6_om1_R0_0.15_AConly_rc1e-6.json, compare_parent_vs_refit_R0_0.15_rc1e-6.json). The PDE block of the R0 0.15 refit is 2.8e-5 (about 100x the control's 2.7e-7): the fit error of the smaller twist radius turns into a larger momentum residual at the start. Both refits sit at compare_fields norm_star_U 0.078 against the parent, which is above the control's holdout rho_u^max 0.046, so by the registration's own descriptive threshold the START is already 'above the residual level'; a re-solve that ends within the residual level of the control would then be the informative outcome.

## 7. Dated correction (2026-10-26T18:10Z; lead d128 HY item 3 (d), HX-R4; the rows above are left as written)
- Section 3 table, row 'R0 0.6, rcond 1e-3': the PDE block cost is 1.579e-8 (reports/block_costs/refit_nest6_om1_R0_0.6_AConly_rc1e-3.json), not '(same to 3 digits)' as 9.407e-9; the
  closure cost 3.979e-8 and the gauge cost 1.641e-4 (int|F|^2 0.99964) differ from the rcond 1e-6 row as well. Only the fit error (3.62e-2 against 3.61e-2) is the same to two digits.
- Section 3 and 6, R0 0.15: the raw coefficient norms A 112434, C 1021 are NOT of the control's size (64 / 3.4). The sentence 'the coefficients are of the control's size' holds for the
  R0 0.6 refit (47.5 / 1.78) only. At R0 0.15 the basis functions carry R0^(alpha + l) factors with R0 half the control's, so the raw coefficient scale is not comparable across R0; the
  conditioning statement (8.5e3, full rank) and the field-level checks (block costs, compare_fields) are the ones that carry.
- The 'fit error (rel L2 on the fit grid)' of reexpand_state.py is the unweighted relative L2 error with angular quadrature weights summed over the radial nodes WITHOUT radial weights
  (every training radius counts once); the 'weighted relative residual' column of the same tool uses the fit weights ((1 + r^2/R0^2)^alpha times the angular weights). Both are grid
  estimates, not norms on a stated domain.
- HX-R3 (lead HY 3 (a)): the claim that the HT criteria 'cannot be met by any re-expansion across an R0 change at fixed L6 Nk16' is withdrawn as a theorem; the attempted re-expansions
  failed the original matching criteria and the registered refits have the stated distances.
