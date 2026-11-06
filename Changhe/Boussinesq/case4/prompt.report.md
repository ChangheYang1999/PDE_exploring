# Research summary at the user-requested stop

**No new high-accuracy, nontrivial profile with physical a0 = O(1) or smaller was found.** Substantially smaller-slope numerical fields were constructed and tested, but their independently evaluated PDE residuals remain much larger than the reference residual.

The user requested stopping before the 24-hour program finished. All active case4 computations and follow-up controllers were stopped at 2026-11-06T00:49:33.817717+00:00, after approximately **17 hours 22 minutes** of the research window. All saved scripts, checkpoints, exact definitions, numerical results, validation records and logs remain on disk. The reference project was used read-only. This is an early-stop report, not a claim that the full 24-hour program was completed.

## Independently measured results

Here J is the original complete whole-plane vorticity-residual norm, with the smooth axis extensions, compactified infinite tail and one origin contribution. It is not the penalty-augmented objective.

| Profile | Physical a0 | Conservative observed independent J | sqrt(J) | Structural evidence |
|---|---:|---:|---:|---|
| Original literal-beta-3 baseline | 600.000000000015 | 1.610297644e-9 | 4.01285e-5 | Independently recovered baseline; later free-beta accuracy not imported |
| Best independently checked fresh state | 66.3131200485 | 0.126295944426 | 0.355381407 | Own global chart certificate, 56 independently replayed leaves |
| Negative-initialization ancestry endpoint | 42.7003175433 | 2.822178848675 | 1.67993418 | Own global chart certificate, 52 independently replayed leaves |
| Low1023 iter4 | 2.89512550354 | 14.84422960774 | 3.852820993 | Full numerical quadrature/MP/origin checks; no complete global chart certificate |

The best fresh state has full-M J = 0.126295937439177 and full-K J = 0.126295926895902; the independently refined adaptive integral gives 0.126295944426204. Its normalized global chart-Jacobian lower bound is 0.0294723629213. This certifies its coordinate chart, not the Boussinesq PDE. Its residual remains about 7.84e7 times the reference J, so it is exploratory, not an accepted accurate profile.

The bounded chart attempt at a0 = 2.8951255 stopped after 180 seconds with 175 positive leaves and seven cells unresolved. It produced neither a certificate nor a counterexample. No later coefficient vector inherits an earlier state's certificate.

## Latest complete saved optimization checkpoints

These final saved states were improving when stopped. **Their listed J values are training values, not newly independently validated norms.** No completed optimizer result was fabricated for a stopped run; all NPZ/exact/direct bundles listed below are complete and hash-checked.

| Search | Stage initial a0 | Last saved a0 | Pure training J | Saved accepted updates |
|---|---:|---:|---:|---:|
| Main wider core | 30.477299 | 39.328373 | 1.26186971 | 13 |
| Low-slope penalty restart | 2.8951255 | 2.4142892 | 14.0328653 | 6 |
| Narrow PDE-only restart | 66.31312 | 111.24673 | 0.0146558205 | 12 |
| Narrow penalty 1e-5 | 66.31312 | 77.816934 | 0.025288914 | 12 |
| Narrow penalty 1e-4 | 66.31312 | 54.040356 | 0.136183579 | 11 |

The last checkpoint paths and exact hashes are in [user_stop_last_complete_checkpoints_v1.json](/mnt/d/Changhe_D/case4/diagnostics/user_stop_last_complete_checkpoints_v1.json). These are stage initial values; the lineages themselves originated from fresh initializations rather than the archived a0-about-600 coefficients.

The pure PDE-only narrow search reached a0 = 111.2467 with training J = 0.0146558. A penalty of 1e-5 retained a smaller a0 = 77.8169 at training J = 0.0252889, while 1e-4 reached a0 = 54.0404 at training J = 0.136184. The low-slope restart reached a0 = 2.41429 with training J = 14.0329. These observations show an optimization tradeoff; they do not establish a mathematical lower bound on a0.

## Work actually performed

- Recovered and independently evaluated the original fixed-beta-3 baseline with the original full quadrature machinery. The later beta = 2.99999021854 state was kept separate.
- Ran fresh multistart searches over initial slopes including 0.01, 0.03, 0.1, 0.3, 0.5, 1, 2 and 5, with multiple shapes, curvature signs and core scales. The known large-slope coefficient branch was not used as the ancestry of the fresh searches.
- Made physical a0 a joint variable with every independent coefficient. The current production maps preserve beta = 3, Q00 = 1, the original exact binary64 phase value 1.2 and strain -2. The generating representation preserves temperature transport and Poisson identities, parity and the canonical velocity family. Only a0 > 0 was imposed in the current strategy; initial slopes were not fixed targets or proximity boxes.
- Tested PDE-only optimization, several slope penalties and constrained-optimization attempts. Reoptimized complete coefficient vectors and refined bases/cores, including 402-, 1023- and 2375-coordinate production searches. A further 802-coordinate basis was prepared and zero-embedding/source checks started, but it was not optimized before stopping.
- Implemented and verified primal/Q5 and Gram accelerations, retaining original-value/Jacobian comparisons, all-column checks, original-A KKT tests and the original SVD fallback.
- Used independent adaptive integration, original full-M/K rules, selected Cartesian multiprecision evaluations, exact-center and coefficient-semantics checks, origin/radius/order studies, far-field and regularity diagnostics, and state-specific interval chart proofs. The final refreshed catalog contains 83 optimizer runs/attempts, 642 frozen states, 23 states with independent full-quadrature records and nine structural chart certificates. These are records, not 642 solutions or nine PDE existence proofs.
- Verified physical-a0 Jacobian columns numerically in all five current searches. Eight additional retrospective initial/final checks closed the remaining accepted historical LOG-coordinate cases, including 8942 coordinates and a0 about 7.33e-16. All eight passed; the worst best-step relative difference was about 5.45e-8. They restore the original saved map/pivots/theta and do not claim that an omitted historical check had actually run at its original time. Actual failed zero-update attempts remain recorded as failures.

## Degeneracy, aliasing and diagnosed failures

A fresh hollow-temperature search moved from a0 = 0.1 to 1.25e-8 but retained training J = 8.186853734e8 and very weak sampled temperature forcing. An independently refined diagnostic integral gives **J = 8.115182562e8** on 862624 positive-weight nodes; the candidate is rejected. A 100-digit Cartesian calculation confirms a large real PDE defect. Tiny slope alone is not a success.

Its original near-coordinate inverse failed at one point because convergence required 83 iterations while the original limit was 80. An explicitly recorded diagnostic with maximum 320 iterations, the SAME 3e-14 tolerance and unchanged equations, bracket and Newton/bisection steps passed successful-point bit-identity and bad-point MP comparisons. Its method is `ORIGINAL_NEAR_320_DIAGNOSTIC`; it is not an unmodified-80-engine result, a rigorous residual bound, or a new optimization.

Earlier coarse quadrature understated the hollow initializer's norm by about a factor of four. The optimizer was not launched until the refined 612064-node initial rule converged numerically. Other failed or underresolved attempts were preserved rather than treated as low-residual discoveries.

Scaling and center analysis showed that physical spatial dilation preserves a0; reducing it is a shape change. The center equations admit formal positive slopes without proving a universal lower bound. The value a0 = 70 is not an imposed boundary. The maximization argument for the zero-temperature limit and the canonical strain constraint does not prove nonexistence for small positive a0 without additional uniform regularity/tail assumptions. Optimizer failures likewise do not prove nonexistence.

## Saved outputs and remaining work

- [RESULTS.csv](/mnt/d/Changhe_D/case4/RESULTS.csv): refreshed comparison catalog; penalties, training and independent measurements are distinguished.
- [BEST_CANDIDATE](/mnt/d/Changhe_D/case4/BEST_CANDIDATE/README.md): the best independently checked fresh exact pair, explicitly exploratory/not accepted.
- [CONTINUATION_REPORT.md](/mnt/d/Changhe_D/case4/CONTINUATION_REPORT.md), [VALIDATION_REPORT.md](/mnt/d/Changhe_D/case4/VALIDATION_REPORT.md), and [FINAL_REPORT.md](/mnt/d/Changhe_D/case4/FINAL_REPORT.md): detailed campaign records with this early-stop status attached.
- [Original-320 diagnostic report](/mnt/d/Changhe_D/case4/positive_chart_fresh_v1/original320_v2/run_v1/REPORT.md).
- [Stop receipt](/mnt/d/Changhe_D/case4/diagnostics/user_requested_stop_v1.json): 16 verified case4 processes terminated, zero remaining research processes. Existing files were not deleted or rewritten by the stopping procedure.

Not completed: the remainder of the 24-hour window, independent endpoint validation of the five last saved optimization states, their own new chart/regularity checks, and optimization of the 802-coordinate refinement. No rigorous whole-plane residual or PDE existence certificate was produced. The strongest numerical accuracy still belongs to the original large-slope baseline. The fresh candidates would require substantial residual reduction before an existence-proof effort could be justified.

An operations-note encoding error during bookkeeping was recovered from preserved handoff records. Older OPERATIONS prose was not recovered verbatim; numerical checkpoints, validation records, certificates and research processes were unaffected. The incident and recovery are recorded in [operations_encoding_recovery_v1.json](/mnt/d/Changhe_D/case4/diagnostics/operations_encoding_recovery_v1.json).

All experimental artifacts are in `/mnt/d/Changhe_D/case4`; only this Markdown report is stored beside the prompt.
