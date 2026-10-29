# Start here

This folder holds the accompanying artifacts of the report "Backward self-similar axisymmetric Euler profiles with swirl for
1/2 < c_l < 3/4: final report", published beside it (euler_axis.report.md). Every reference in the report to "the accompanying
artifacts" points into this folder. All paths below are relative to this folder.

Outcome in one line: label C (unsuccessful numerical search) for 1/2 < c_l < 3/4, separate label D (rigorous obstruction) for
0 < c_l < 1/2, and the smooth case c_l = 1/2 open. Every saved state is an approximation that fails the pre-registered
acceptance criteria; none is a solution.

Roles used in the provenance tags of all documents: [lead] is the report author (formulation, analysis, report); [primary
search] is the primary numerical search; [verifier] is the independent verifier, whose separate implementation was written
from the exchange-format description and the pre-registered specification; [referee] or [independent referee] is an external
referee, a second model consulted with self-contained questions, whose results are treated as claims and checked as stated.

## Required deliverables

| deliverable | location |
|---|---|
| START_HERE.md | START_HERE.md (this file) |
| FINAL_REPORT.md | published beside this folder as euler_axis.report.md |
| MATHEMATICAL_FORMULATION.md | MATHEMATICAL_FORMULATION.md |
| AXISYMMETRIC_OBSTRUCTION_AUDIT.md | AXISYMMETRIC_OBSTRUCTION_AUDIT.md |
| ORIGIN_AND_AXIS_REGULARITY.md | ORIGIN_AND_AXIS_REGULARITY.md |
| FAR_FIELD_ANALYSIS.md | FAR_FIELD_ANALYSIS.md |
| FULL_SPACE_PRESSURE.md | FULL_SPACE_PRESSURE.md |
| NUMERICAL_METHODS.md | NUMERICAL_METHODS.md |
| PARAMETER_SWEEP.csv | PARAMETER_SWEEP.csv |
| CANDIDATE_LEADERBOARD.csv | CANDIDATE_LEADERBOARD.csv |
| INDEPENDENT_VALIDATION.md | INDEPENDENT_VALIDATION.md (chronological log of the independent verifier) |
| FAILURE_ANALYSIS.md | FAILURE_ANALYSIS.md |
| RUNBOOK.md | RUNBOOK.md (launch, monitor, resume and revalidate the primary search) |

Also included:
- ACCEPTANCE_SPECIFICATION.md: the specification registered at 2026-10-28T18:24Z, before any candidate existed, with the
  residual definitions, gauges and the acceptance thresholds of labels A and B (never relaxed).
- FAILURE_MAP.csv: one row per finished search run of the primary search (526 rows), with its failure class.
- numerical_code/: the primary numerical project: solver and operators (src/), operator tests (tests/), job supervisor and
  worker (supervisor/), sweep, leaderboard, revalidation, figure and resume scripts (scripts/), optimizer configurations
  (configs/), environment lock file (env/), hardware inventory (hardware/), and the exported coefficients of the registered
  states with complete basis definitions, evaluation code and self-tests (candidates/). No state was accepted, so there
  are no accepted candidate coefficients; the exported states are the rejected approximations described in the report.
- independent_validator_source/: source code, tests and environment lock files of the independent validator
  (validator/), its single-command reproduction script reproduce_r5.py with its lock files, and the exported R5 state.
  This is published for inspection. The reproduction script first verifies the checksum manifest of the complete
  validation bundle (about 190 MB, not published because of the size limit of this folder), so it does not run unchanged
  here; its tested runs are recorded in section 9.1 of the report and in INDEPENDENT_VALIDATION.md.
- author_checks/: the symbolic and numerical check scripts of the report author with their saved outputs, cited by name in
  the mathematical documents.
- figures/: all figures of the report with their data (see below).
- SHA256SUMS: SHA-256 checksums of every other file in this folder; check with `sha256sum -c SHA256SUMS` from this folder.

Not included because of the size limit: the full run archive of the primary search (run folders, optimizer checkpoints,
logs, run ledger), the complete validation bundle with its evidence records, and the external referee's reports. The
verifier checked earlier assemblies that contained them; this published subset and its manifest were assembled after the
team stop and were not checked by the verifier.

## Figures of the report (section 9)

The data of each figure are stored next to its image (CSV, compressed CSV, JSON or NPZ files in the same folder, with the
plotting script where one was used). Every figure shows approximate states that are not solutions.

| figure | content | image files |
|---|---|---|
| F1 | residual versus spectral resolution | figures/primary_search/F1_residual_vs_resolution.png |
| F2 | residual versus spatial radius (L1) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/registered_radius.png |
| F3 | spectral coefficient decay (L1, L2) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/angular_coefficients.png and radial_coefficients.png; figures/independent_validation/ladder_l2_coefficients_20261029T021255Z/angular_coefficients.png and radial_coefficients.png |
| F4 | swirl and poloidal field distributions (L1) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/field_distribution.png |
| F5 | c_l continuation | figures/primary_search/F5_cl_continuation.png |
| F6 | far-field convergence (L1) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/far_field.png |
| F7 | energy-flux identity errors (L1) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/balances.png |
| F8 | axis and origin residuals (L1) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/axis_origin.png |
| F9 | interface jumps (L1) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/interface_jumps.png |
| F10 | pressure differences (L1) | figures/independent_validation/ladder_l1_20261029T004517.856506Z/pressure.png |
| F11 | closed single-source problem | figures/closed_single_source/F11_closed_single_source.png (plotted by author_checks/fig_closed_t1.py) |

figures/primary_search/ also holds per-state diagnostic plots (axis, cost, fields, residual versus radius, spectral decay) of
the main ladder and continuation states of the primary search.

## Where to start

1. Read the summary at the top of the report.
2. For the mathematics: AXISYMMETRIC_OBSTRUCTION_AUDIT.md (obstructions and necessary conditions), then
   MATHEMATICAL_FORMULATION.md, ORIGIN_AND_AXIS_REGULARITY.md, FAR_FIELD_ANALYSIS.md and FULL_SPACE_PRESSURE.md.
3. For the numerics: ACCEPTANCE_SPECIFICATION.md, NUMERICAL_METHODS.md, CANDIDATE_LEADERBOARD.csv, FAILURE_ANALYSIS.md and
   RUNBOOK.md; to evaluate a saved state, see the BASIS.md, field_eval.py and SELFTEST.txt files under
   numerical_code/candidates/.
4. For the checks: INDEPENDENT_VALIDATION.md and sections 6 and 9.1 of the report.
