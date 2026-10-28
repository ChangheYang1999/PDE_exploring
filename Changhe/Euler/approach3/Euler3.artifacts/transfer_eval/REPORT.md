# Cross-code evaluation of the verifier's exported D2 state (lead item 2)

Written 2026-10-24T21:54Z (file time; the clock is date -u). Script: scripts/eval_transfer.py. Inputs: <independent-route directory>/independent/exports/d2_projected_release
(SPEC 10 export, state "UNVALIDATED APPROXIMATION", c_l = 0.45, omega = 0.3, omega/c_l = 2/3, R0 = 0.3, Cartesian degree 2,
five radial channels). Outputs: transfer_eval/d2_projected_release_L6_Nk16.json, d2_projected_release_L8_Nk24.json,
the fitted primary states *_L6_Nk16.pt and *_L8_Nk24.pt (label "transferred"), logs d2_L6_Nk16.log, d2_L8_Nk24.log.
Elapsed: 20 s (L = 6) and 42 s (L = 8) on one GPU. The transferred states are not candidates and are not in the ledger.

## Part A: the exported samples themselves (no primary basis, their pressure)

Five-term momentum split from the exported U, DU (their convention DU[i,j] = d_j U_i, transposed to the primary GU) and grad P
on their 105 thin spheres with their angular weights. Relative divergence of the exported DU: 4.3e-16.

| quantity | value |
|---|---|
| rho_u, maximum over single spheres | 0.1220 at r = 0.459 |
| rho_u, maximum over dyadic shells (core ball r < R0, then doublings; spheres weighted by r^3) | 0.1169 on [0.3, 0.6) |
| rho_nl, maximum over single spheres | 0.178 |
| rho_nl at the far spheres | 0.07 (residual is 7 percent of the nonlinear terms out to r = 3e5) |
| pi_u, maximum over dyadic shells | 0.405 on [0.6, 1.2) |

## Part B: their basis re-evaluated, the primary basis fitted, primary diagnostics with the primary pressure

Their BASIS.md was implemented independently (vector potential with torch autograd curl). Against their 16384 exported random
points: maximum relative error 2.2e-14, median 3.4e-16. So the exported numbers and the written basis description agree.

The primary basis was then fitted to that field (fit_field, weighted least squares on the primary training grid), and the fitted
state was evaluated with spec_diagnostics on the training grid and on the holdout grid, with the primary full-space pressure
rebuilt from the fitted field. The fit error bounds what the numbers can mean.

| primary fit | fit error on their random points (scaled) | core fit error (r < 4 R0) | training rho_u_max | holdout rho_u_max | holdout rho_Om_max |
|---|---|---|---|---|---|
| L = 6, Nk = 16, Nr = 48, NkB = NkD = NkE = 4 | 6.2e-5 | 8.3e-5 | 0.11220 | 0.11328 | 0.14871 |
| L = 8, Nk = 24, Nr = 72, NkB = NkD = NkE = 4 | 2.1e-4 | 2.9e-4 | 0.11344 | 0.11327 | 0.14867 |

(The L = 8 fit error is larger because the Tikhonov floor acts on a worse-conditioned normal matrix; it is still far below
the residual level.)

Comparison with the verifier's own numbers for the same state (meta.json and the 21:44Z note):

| quantity | verifier (independent route) | primary diagnostics on the transferred state (L = 6 fit, holdout grid) |
|---|---|---|
| fresh rho_u | 0.11328836 | 0.11328 |
| max rho_Omega | 0.14874261 | 0.14871 |
| N_F | 0.26168010 | 0.26167472 |
| e_F | 0.01711912 | 0.01711842 |
| N_core | 1.37047529 (sampled) | 1.37047214 |
| e_core | 0.46955063 (sampled) | 0.46954847 |
| max abs Omega | 51.3177 (sampled) | 51.3035 at r = 0.0307 (holdout grid sample) |
| strain ratio at the vorticity maximum | 0.9139 | 0.9391 (grid point, not a located maximum) |
| lambda_max(S) at the vorticity maximum | 12.0533 | 12.0446 |

Primary holdout rho_u per dyadic shell (core ball first): 0.0036, 0.0067, 0.0122, 0.0214, 0.0432, 0.0774, 0.1133, 0.0965,
0.0355, 0.0081, 0.0011, 1e-4, then below 1e-5. The maximum sits at r of order 0.3 to 0.6, the same shell as in Part A.

Conclusion: the two codes (different bases, different pressure solvers, different quadratures) agree on the D2 state's
momentum defect rho_u to four digits (0.1133), on rho_Omega to four digits, and on N_F, e_F, N_core, e_core to five digits.
This cross-validates the two residual evaluations against each other; it does not make the state a candidate (rho_u = 0.11 is
far from the Tier S threshold 1e-2).

Caveat on rho_nl for transferred states: the primary holdout rho_nl_max is 59 (L = 6) and 628 (L = 8), while Part A gives 0.18.
The large values come from the far shells, where the fit error (1e-4 of the linear terms, which decay like r^-alpha) exceeds the
nonlinear terms (which decay like r^-(2 alpha + 1)). rho_nl of a transferred state is therefore not meaningful beyond the core
shells; rho_u is, because its denominator includes the linear terms.

## Addendum 2026-10-24T22:09Z: SPEC 11c test N1 for the D2 state (tail constraints kept)

Lead's 21:55Z note, item N1, and SPEC 11c: fit the independent field into the primary basis with the tail constraints kept, labelled
transferred, and read the fitted field's own holdout rho_u^max against the source value (can represent if <= 1.5 times; cannot if
>= 3 times at the highest level). Run: scripts/eval_transfer.py ... --levels 6:16:48,8:20:60 --tail_constraints --source_rho_u 0.11328836
(transfer_eval/d2_tc.json, d2_tc.log; 51 s for both levels on one GPU).

| level | fit error on their random points (scaled) | core fit error (r < 4 R0) | holdout rho_u_max | ratio to source 0.11328836 | holdout rho_nl_max over shells with r_hi <= 4 | holdout rho_Om_max |
|---|---|---|---|---|---|---|
| L = 6, Nk = 16, Nr = 48, tail constraints | 8.3e-4 | 1.1e-3 | 0.11321 | 0.9993 | 0.172 | 0.14848 |
| L = 8, Nk = 20, Nr = 60, tail constraints | 2.2e-3 | 3.1e-3 | 0.11328 | 0.9999 | 0.172 | 0.14869 |

N1 reading for D2: the primary basis CAN represent the independent D2 state at L = 6 already (ratio 1.0; the SPEC threshold is 1.5).
The fit error with the tail constraints (1e-3) is larger than without (6e-5) but far below the residual level 0.11; the rho_nl values over
the inner shells (0.172) agree with the direct evaluation of their samples (0.178). The fitted states transfer_eval/d2_tc_L6_Nk16.pt and
d2_tc_L8_Nk20.pt are warm starts for the primary ladder, never evidence (SPEC 11c). The same test for D6 released is run as soon as the
verifier's export independent/exports/d6_projected_release is complete.

## Addendum 2026-10-24T22:19Z: SPEC 11c test N1 for the D6 released state (lead 21:55Z item N1)

Export <independent-route directory>/independent/exports/d6_projected_release (finished 22:14Z; c_l 0.45, omega 0.3, omega/c_l 2/3, Cartesian degree 6,
five radial channels, R0 0.3; the verifier's fresh holdout rho_u^max 0.072870900755279, rho_nl^max 0.0946). Their BASIS.md re-evaluated
independently matches their random samples to 3.8e-13. Direct split of their samples with their pressure: rho_u 0.0796 on the dyadic
shell [0.3, 0.6), 0.0857 on the worst single sphere (r 0.399). Command: scripts/eval_transfer.py ... --levels 6:16:48,8:20:60,10:24:72
--tail_constraints --source_rho_u 0.072870900755279 (transfer_eval/d6_tc.json, d6_tc.log; 143 s on one GPU; the fitted states
d6_tc_L6_Nk16.pt, d6_tc_L8_Nk20.pt, d6_tc_L10_Nk24.pt are worker-loadable warm starts labelled transferred).

| primary level (tail constraints kept) | fit error on their random points (scaled) | core fit error (r < 4 R0) | holdout rho_u_max | ratio to source 0.07287 | holdout rho_nl_max over shells with r_hi <= 4 | holdout rho_Om_max | time |
|---|---|---|---|---|---|---|---|
| L = 6, Nk = 16, Nr = 48 | 1.0e-2 | 8.8e-3 | 0.07403 | 1.016 | 0.0966 | 0.1202 | 19 s |
| L = 8, Nk = 20, Nr = 60 | 1.1e-2 | 1.2e-2 | 0.07539 | 1.035 | 0.0950 | 0.1391 | 40 s |
| L = 10, Nk = 24, Nr = 72 | 1.6e-2 | 1.7e-2 | 0.07758 | 1.065 | 0.0954 | 0.3599 | 81 s |

N1 reading for D6 (SPEC 11c): the primary basis CAN represent the independent D6 released state, already at L = 6 (ratio 1.02 against
the threshold 1.5). The fit error (1e-2, growing with L) comes from the Tikhonov floor on a singular normal matrix (the fit has null
directions; condition estimates 1e304 and above); it is well below the residual level 0.073 for rho_u but visible in rho_Om at L = 10.
rho_nl over the inner shells (0.095 to 0.097) agrees with the verifier's 0.0946. Consequence stated by the lead (21:55Z): the factor of
four between the routes' best values (primary 0.35, independent 0.073) is a search failure of the primary route, not a limit of its
representation near the core edge. The fitted L = 6 state is now the warm start of primary continuation arms d6t (L 6 and 8, fixed
parameters, five-term weighting, tail constraints, far anchoring, no Sigma_Z row) and d6tZ (L 6, with the Sigma_Z = 1 ramp; the
state's own Sigma_Z is 0.35). A fitted state is a warm start, never evidence.
