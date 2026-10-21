# Accompanying artifacts for section 6: exclusion certificates, B_3 functional code and symbolic checks

## Purpose

This folder is the lead researcher's part of the accompanying artifacts of section 6 of the report (the strong setting
P_inf). Item 6.3.1 (o) of the report states that the least-squares fit that produced the fitted reference, the
certificate programs, their inputs and the explicit remainder-bound formulas are in the accompanying artifacts. They
are here, in `exclusion_certificates/`, together with the derivation of item 6.3.1 (n). The folder also holds the lead
researcher's code for the obstruction functional B_3 used in 6.3.2 and 6.4 (`b3_functional/`) and the lead researcher's
symbolic and numerical checks of statements in 6.3.1, 6.4 and 6.5 (`symbolic_checks/`).

Every program was rerun from these copies for this package, with two exceptions in `symbolic_checks/`: one long
numerical check was not rerun (its original run took more than 90 minutes; its log, complete for one of its two
parameter values, is included), and one exact check stopped at the time limit of 540 s after its first steps.
Commands, run times and results are listed below.
`SANITIZE_LOG.md` lists every change made to the copied files.

### Authorship and status of the derivations

- The `PROOF.md` derivations in `exclusion_certificates/` were written by external referees, and so were the
  certificate programs beside them (all `.py` files in `exclusion_certificates/` except `bref_input.py`, which is the
  lead researcher's evaluator of the exact functional supplied to the referee as an input). They were checked by the
  verifier as described in the report (items 6.3.1 (n) and 6.3.1 (o), which also state which steps were checked by
  hand, which were rerun on copies and which were recomputed with separately written code). A second external referee
  audited the first part of 6.3.1 (o) (`exclusion_theorem/audited_estimate/` and `raw_bounds/norm_repair/`), and a third
  external referee reran the certificate and the budgets (`audit_rerun/`). The lead researcher reran the certificate
  programs and checked the quantities listed in 6.3.1 (o).
- The code in `b3_functional/` and `symbolic_checks/` was written by the lead researcher, except
  `b3_functional/dcode/vb3ibp.py`, the verifier's estimator of the first run, included because the lead researcher's
  estimator imports it.
- The interval programs (`obstruction_certificate/verification/certify.py`,
  `trace_uncertainty/verification/analytic_bounds.py`, and the interval checks of `audit_rerun/audit_checks.py`) use
  outward-rounded interval arithmetic (`mpmath.iv`; certify.py at 40 decimal places with rigorous Taylor remainders on
  whole intervals, the audit at 50). The exact programs (`rational_certificate.py`, `norm_repair.py`,
  `radius.py`) use Python `Fraction` arithmetic; where they print decimals, these are rounded outward from the exact
  fractions, and radius.py combines Fraction arithmetic with interval jets followed by outward rational rounding.
  `fit_reference.py`, `reconstruct_reference.py`, `numerical_checks.py` and `compare.py` are numerical evidence, not
  certificates; each says so in its docstring and in the status field of its output.

## Software and general instructions

- Python 3.9.25 with numpy 2.0.2, scipy 1.13.1, mpmath 1.3.0 and sympy 1.14.0 was used for all reruns below.
  Two programs were also run with Python 3.12.13, numpy 2.5.0, scipy 1.18.0, mpmath 1.3.0 and sympy 1.14.0, which
  reproduces their stored outputs byte for byte (see the notes to the rerun table).
- Run everything single-threaded:
  `export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1`.
  All reruns were done with `timeout 540`.
- The referee programs set an address-space limit of 1.9 GB (`resource.setrlimit(resource.RLIMIT_AS, ...)` with
  1 900 000 000 bytes; radius.py inherits it from certify.py, which it imports), and `audit_checks.py` also sets a CPU
  limit of 500 s. The `resource` module requires Linux or another Unix system.
- The programs write their outputs beside themselves and overwrite the stored files. To compare with the stored
  outputs, run them on a copy of this folder.
- All paths inside the programs are relative to the program file, so the working directory does not matter; the
  programs of `b3_functional/` that read stored traces take the trace folder from the environment variable `TRACE_DIR`
  (see there).

## exclusion_certificates/

Report items: 6.3.1 (o) (both parts) and, for `a4_exclusion/`, 6.3.1 (n).

| Folder or file | Content |
|---|---|
| `reference_fit/PROOF.md` | The explicit compatible reference w_0 of the form of 6.3.2 (e) with q of degree 12 fitted to the computed trace: compatibility and negativity certified, approximation numerical only (6.3.1 (o), first part (v)). |
| `reference_fit/verification/fit_reference.py` | The least-squares fit that produced the coefficients q_0, ..., q_12 of 6.3.1 (o); freezes them as exact decimal strings and checks w_0 < 0 on (0, 1) and H >= A_0 by rational Bernstein bounds. Output `data/fitted_reference.json`. |
| `reference_fit/verification/reconstruct_reference.py` | Numerical reconstruction (65 digits, mpmath) of g_0 from the frozen reference; g_0(1) = 0.40222790015532244. Output `data/reconstruction_numerical.json`. |
| `reference_fit/data/fitted_reference.json` | The fitted reference: A_0 = 10.150725, L_0 = 8.6000638, the exact decimals q_0, ..., q_12, sampled residuals and the Bernstein certificates. |
| `reference_fit/data/reconstruction_numerical.json` | Output of reconstruct_reference.py. |
| `reference_fit/data/c6g_traces.npz` | Input of the fit: the stored axis trace of the candidate X3 computed by the first-run verifier (arrays x, w, wp, wpp_fd, wpp_ode, c_l, c, source, Mmax; md5 e53abea1da447eb20638b116efecf153). Also used by `b3_functional/` through `TRACE_DIR`. |
| `raw_bounds/01-differential/PROOF.md` | First part of 6.3.1 (o), (i): normalization u = x/x*, the functional B(A, e, w~) and its full first variation with the adjoint weight. |
| `raw_bounds/02-remainder/PROOF.md` | First part, (i): the second-order remainder bound with constants polynomial in the reference; these are the explicit remainder-bound formulas of 6.3.1 (o). |
| `raw_bounds/03-norm-and-radius/PROOF.md` | First part, (ii) and (iii): weaker norms, the failure of a plain C^2 tail norm, the radius formula and the radii. |
| `raw_bounds/03-norm-and-radius/verification/rational_certificate.py` | Exact rational constants and radii (Fraction only) for three cases: the computed parameters with q = 0 (B >= 0.321857, dual norm <= 12240, second-order constant <= 235346, delta_0 >= 0.1046, radius 1e-6) and the reference of 6.3.1 (n) at A = 4 (radii 1e-8 with parameter widths, 1e-7 at fixed parameters). Output `rational_bounds.json`. |
| `raw_bounds/03-norm-and-radius/verification/numerical_checks.py` | Numerical evidence separate from the certificate: B at the computed parameters by two formulas, B_e, B_A, B_AA and the responses DB(phi_j) by finite-part beta moments. Output `numerical_checks.json`. |
| `raw_bounds/04-exclusion/PROOF.md` | Certificate inventory and the reference-dependent exclusion theorem of the first part. |
| `raw_bounds/norm_repair/norm_repair.py` | The second referee's repair for the norm with R_v taken after subtracting c_j phi_j: reuses rational_certificate.py with three origin constants replaced by the bounds of section 7 of `exclusion_theorem/audited_estimate/02-remainder/PROOF.md`. Output `norm_repair.json` (constants 12519 and 245246, delta_0 >= 0.10269550, radius 1.8749e-6 above 1e-6; first part (ii) of 6.3.1 (o)). |
| `obstruction_certificate/PROOF.md` | Second part of 6.3.1 (o), (i): the certified obstruction on the fitted reference. |
| `obstruction_certificate/verification/certify.py` | Interval Taylor certificate (mpmath.iv, 40 digits): 0.2830400682 < B(A_0, e_0, w_0) < 0.2851567624, 0.40222790015 < g_0(1) < 0.40222790016, the first parameter derivatives at the reference and the second derivatives on the parameter box. Output `data/obstruction_certificate.json`. |
| `obstruction_certificate/data/fitted_reference.json` | Input of certify.py; byte-identical to `reference_fit/data/fitted_reference.json`. |
| `obstruction_certificate/data/obstruction_certificate.json` | Output of certify.py. |
| `radius_budget/PROOF.md` | Second part, (ii): the reference inventory, the quadratic budget, the radii 4.5e-6 and 5e-6 and the conversion constant 415/4 between the two remainder conventions. |
| `radius_budget/verification/radius.py` | Complete fitted-reference inventory and exact rational radius calculation; uses the interval results of certify.py. Output `radius_certificate.json`. |
| `trace_uncertainty/PROOF.md` | Trace distances (the three referee pairs of the first part (v)), the Taylor separations and why samples do not control N (second part (iv)), and the conditional analytic estimate of the further statements after the second part. |
| `trace_uncertainty/verification/compare.py` | Numerical comparisons, not certificates: N-distances among the approximants K = 12, K = 18 and the fitted reference, and B on each aligned shape recomputed with bref_input.py. Output `numerical_comparison.json`. |
| `trace_uncertainty/verification/analytic_bounds.py` | Exact jet comparisons (lower bounds for the Taylor separations), the norm conversion and interval examples of the conditional analytic bound. Output `analytic_bound_certificate.json`. |
| `trace_uncertainty/verification/bref_input.py` | The lead researcher's exact functional B supplied to the referee; byte-identical to `b3_functional/xref/bref.py`. |
| `trace_uncertainty/verification/ref_c6g_K12.json`, `ref_c6g_K18.json` | Inputs: the approximants K = 12 and K = 18 of 6.3.2 (e); byte-identical to the files in `b3_functional/xref/`. |
| `exclusion_theorem/fitted_reference_exclusion/PROOF.md` | Second part, (iii): the resulting conditional exclusion theorem around the fitted reference. |
| `exclusion_theorem/audited_estimate/01-differential/` to `04-exclusion/` (`PROOF.md` each) | The second referee's audit of the first part (normalization and differential, remainder bound with the repair for the phi_j convention in its section 7, norm and radius, PDE exclusion theorem). |
| `audit_rerun/audit_checks.py` | The third referee's independent exact and interval checks (it imports no certificate-generating module), adapted to this folder layout. Outputs `audit_checks.json` and `installed_rounding.json` (evidence that the installed mpmath rounds outward). |
| `audit_rerun/sources.json` | Manifest of the referee's input files with their SHA-256 digests; for each, whether it is here as a byte-identical copy, here with documented edits, or not included. |
| `audit_rerun/expected/` | The certificate outputs as the referee received them (the replay checks compare against these). |
| `audit_rerun/referee_run/` | The referee's own run: `audit_checks.json` (PASS, 140 checks) and `installed_rounding.json`. |
| `a4_exclusion/PROOF.md` | Item 6.3.1 (n): the quantitative Lipschitz estimate and the explicit exclusion near the rational reference at A = 4. No program. |

### How to run

From `exclusion_certificates/` (any working directory works), with the environment above:

```
timeout 540 python3 reference_fit/verification/fit_reference.py
timeout 540 python3 reference_fit/verification/reconstruct_reference.py
timeout 540 python3 raw_bounds/03-norm-and-radius/verification/rational_certificate.py
timeout 540 python3 raw_bounds/03-norm-and-radius/verification/numerical_checks.py
timeout 540 python3 raw_bounds/norm_repair/norm_repair.py
timeout 540 python3 obstruction_certificate/verification/certify.py
timeout 540 python3 radius_budget/verification/radius.py
timeout 540 python3 trace_uncertainty/verification/analytic_bounds.py
timeout 540 python3 trace_uncertainty/verification/compare.py
timeout 540 python3 audit_rerun/audit_checks.py
```

radius.py reads `obstruction_certificate/data/obstruction_certificate.json`, analytic_bounds.py reads
`numerical_comparison.json`, and norm_repair.py reads the source text of rational_certificate.py (it records its
SHA-256, which is unchanged in this copy), so run them in this order.

### Rerun results

Run one at a time, single-threaded, under Python 3.9.25 unless noted; each output was compared with the stored file
(JSON compared as parsed data and byte for byte); the stored files were then restored.

| Program | Time | Result |
|---|---|---|
| fit_reference.py | 0.76 s | Python 3.9.25 / numpy 2.0.2: differs from the stored file in the fitted digits (the 13 coefficients agree to about 9 to 10 significant digits, for example q_0 = -3.1086642790748611 against -3.1086642790748664; the sampled residuals change slightly). Python 3.12.13 / numpy 2.5.0: 0.97 s, byte-identical. See note 1. |
| reconstruct_reference.py | 0.18 s | byte-identical |
| rational_certificate.py | 0.04 s | byte-identical |
| numerical_checks.py | 3.63 s | byte-identical |
| norm_repair.py | 0.04 s | byte-identical |
| certify.py | 33.8 s | identical except the field `elapsed_seconds` (33.7 s against 25.18 s stored), against both the stored output and `audit_rerun/expected/` |
| radius.py | 1.86 s | Python 3.9: identical content, two keys ("KD" and "d") in a different order (the program collects values from `locals()`). Python 3.12.13: 1.54 s, byte-identical. |
| analytic_bounds.py | 0.07 s | byte-identical |
| compare.py | 291 s | byte-identical; prints B on the aligned shapes: fitted 0.284073229231419611, K12 0.267482167464615773, K18 0.299650248137408487 |
| audit_checks.py | 0.09 s | PASS, 102 checks. The 95 arithmetic, interval and replay checks are the same checks as in the referee's run of 140 and all pass; the other 7 confirm the byte-identical copies listed in `sources.json`. The referee's run had 45 provenance checks of its own file layout instead (source digests and copies of files not included or edited here). `exact_and_interval_results` is identical to the referee's, and `installed_rounding.json` is byte-identical to `referee_run/installed_rounding.json`. Rerun once more after the last documentation edits: same output. |

Note 1. The certified statements use only the frozen exact decimals stored in `fitted_reference.json`, so the
library-dependent last digits of a new least-squares solve do not affect any certificate; the stored file is the one
reproduced byte for byte under Python 3.12.13 with numpy 2.5.0.

## b3_functional/

The lead researcher's evaluators of the obstruction functional B_3 (natural units) and its exact form B. Report items
6.3.2 (a) to (e), 6.3.1 (o) and two items of 6.4.

| File | Description | Report item |
|---|---|---|
| `b3infl/b3core.py` | The lead researcher's B_3 estimator: the original form of R10 evaluated with the first-run verifier's machinery (`dcode/vb3ibp.py`), one fixed configuration (for derivatives) and the 32-variant median (for values). Usage: `python3 b3core.py <traces.npz>`. | 6.3.2 (a), (c), (d) |
| `b3infl/infl.py` | Response of B_3 to localized perturbations of the axis velocity w (Gaussian bumps in log x and one-sided lambda-type perturbations). Usage: `python3 infl.py <traces.npz> <out.npz>`. | 6.3.2 (c) (estimator artefacts) |
| `b3infl/infl2.py` | The same with the finite part at 0 taken from a fit window the perturbation does not touch. Usage as infl.py. | 6.3.2 (c) |
| `b3infl/lamfit.py` | Least-squares fit of the one-sided non-analytic content of w at x* (exponent mu + 1, mu = g*/A) with a control fit. Usage: `python3 lamfit.py <traces.npz>`. | exploratory, no report value |
| `b3exact/lin_r12.py` | Exact first-order response of B_3 on the R12 axis data to w -> w (1 + eps b) with a flat bump b. Usage: `python3 lin_r12.py L x0[,x0,...] [sig]`. | 6.3.2 (c), the table |
| `b3exact/exact_analytic.py` | Exact B_3 on R12 data perturbed in a direction analytic near 0, with central differences, compared with the b3core estimators. Usage: `python3 exact_analytic.py L '<sympy expression of b in t>' [e]`. | 6.3.2 (c), the value 948.844 |
| `b3exact/check_lin.py` | Checks of lin_r12.py: the finite-part framework against the closed form C_A (1 - S_A/L^2) and the linearization against finite-eps differences. No arguments. | 6.3.2 (a), (c) |
| `b3grad/b3grad.py` | Gradient of the B_3 estimator with respect to the arrays w, w', w'' by central differences, for constrained fits. Usage: `python3 b3grad.py <traces.npz> <out.npz> [xr]`. No report value rests on it. | tool |
| `hminus/hminus.py` | Pointwise test of the sufficient sign condition (H_-) and B_3 from the convergent formula. Usage: `python3 hminus.py r12 <L>` (R12 data) or `python3 hminus.py trace <name>[,<name>...] [wpp_ode or wpp_fd]`. | 6.4, "(H_-) on the stored fits" |
| `hminus/out_r12_8.6001.json`, `out_r12_5.3436.json` | Stored outputs on R12 data at L = 8.6000638 and at the zero L* = 5.3435753609604. | same |
| `hminus/out_traces_wpp_ode.json`, `out_traces_wpp_fd.json`, `out_traces_ode_output.txt`, `out_traces_fd_output.txt` | Stored outputs on the stored traces of the first investigation (both w'' forms). | same |
| `hminus/split.py` | Amplitude split of the sign criterion: B_3(mu) = mu^(-1-beta) (b0 + b1/mu), the zero mu_0 and the (H_-) range of mu. Usage as hminus.py. | 6.4, "Reading and size of the sign criterion of 6.3.1 (k)" |
| `hminus/split_r12_8.6001.json`, `split_traces_wpp_ode.json`, `split_traces_output.txt` | Stored outputs of split.py. | same |
| `xref/bref.py` | The exact obstruction functional B (natural units) on an analytic compatible reference trace: finite part at 0 from the Taylor series, mpmath quadrature, Taylor series at the source. Module: `B(A, e, qcoef, dps=40)`. | 6.3.2 (e), 6.3.1 (o) (iv), (v) |
| `xref/fitref.py` | Fits the exactly compatible analytic approximants (q of degree K in u^2) to a stored trace and evaluates B with bref.py. Usage: `python3 fitref.py <trace name> K[,K2,...] [wfit]`; writes `ref_<name>_K<K>.json` beside itself (its docstring still names the original folder). | 6.3.2 (e), 6.3.1 (o) (iv), (v) |
| `xref/ref_c6g_K4.json` to `ref_c6g_K18.json` | The approximants K = 4, 6, ..., 18 of the computed trace (exact decimal coefficients, fit errors, B). | 6.3.2 (e), 6.3.1 (o) |
| `s4a/s4a.py` | B_3 on stored traces by b3core (medians of the original and integrated forms, and the fixed configuration). Usage: `python3 s4a.py <name>[,<name>...]`. | 6.3.2 (d), the lead researcher's medians |
| `s4a/s4a_all_output.txt` | Stored output of s4a.py on all stored traces of the first investigation, both w'' forms. | 6.3.2 (d) |
| `dcode/vb3ibp.py` | The first-run verifier's estimator (integrated-by-parts w-only form and original form); imported by b3core.py, lamfit.py, hminus.py and split.py. Usage: `python3 vb3ibp.py <traces.npz> [out.json]` or `python3 vb3ibp.py test`. | dependency; section 5 step 2 |

Traces. The programs that read stored traces take them from the folder named by the environment variable
`TRACE_DIR` (default `../traces` relative to the program, which is not included). Only the trace of the candidate,
`exclusion_certificates/reference_fit/data/c6g_traces.npz` (trace name `c6g`), is included; the other stored traces of
the first investigation are not. lin_r12.py and exact_analytic.py read c6g_traces.npz directly by a relative path.

Smoke tests (from a scratch copy of this folder, with `TRACE_DIR` set to `exclusion_certificates/reference_fit/data`,
Python 3.9.25, timeout 540):

| Command | Time | Result |
|---|---|---|
| `python3 hminus.py r12 8.6000638` | 0.90 s | byte-identical to `out_r12_8.6001.json` |
| `python3 hminus.py r12 5.3435753609604` | 0.87 s | byte-identical to `out_r12_5.3436.json` |
| `python3 split.py r12 8.6000638` | 1.31 s | byte-identical to `split_r12_8.6001.json` |
| `python3 fitref.py c6g 12` | 33.5 s | byte-identical to `ref_c6g_K12.json` |
| `python3 lin_r12.py 8.6 0.5,1,2,3 0.3` | 19.1 s | exact responses -4.63172e6, -6.36862e4, -8.96490e2, -7.57306e1, as in the table of 6.3.2 (c) |
| `python3 exact_analytic.py 8.6 't**2*exp(-t**2/8)'` | 265 s | 9.488437e2 (report: the lead researcher's evaluation 948.844) |
| `python3 check_lin.py` | 6.6 s | finite-part B_3 0.32579173 against the closed form 0.32579196; nonlinear differences -6.368567e4 and -6.368613e4 against the linear response -6.36862e4 |
| `python3 s4a.py c6g` | 2.0 s | the two c6g lines of `s4a_all_output.txt` reproduced exactly (timings aside): medians 0.29961 and 0.29959 (integrated form), 0.30287 and 0.30282 (original form) |

The arguments of hminus.py and split.py must be the full values of L (8.6000638 and 5.3435753609604): the output
name rounds L to four decimals, and the stored outputs were made with the full values.

## symbolic_checks/

The lead researcher's checks of statements of external referees, of the verifier and of the lead researcher, mostly
exact sympy computations, renamed to describe their content. Run from `symbolic_checks/` as
`timeout 540 python3 <script>.py [arguments]`; only two scripts take arguments (shown in the table).
`local_exclusion_reference_values.py` and `reference_taylor_separations.py` read files from `b3_functional/xref/` and
`exclusion_certificates/reference_fit/data/` by paths relative to their own location. Stored logs of the original
runs are kept beside nine scripts (`_output.txt` or `.out` with the script's name; renamed from `.log` for publication); the outputs of the reruns for this package
are in `rerun_outputs/` (`<script>.out`, with `_a`, `_b`, `_c` for the three modes of local_exclusion_reference_values.py).

Rerun with Python 3.9.25 (sympy 1.14.0, mpmath 1.3.0, numpy 2.0.2, scipy 1.13.1), one at a time, timeout 540.

| Script | What it checks | Report item | Time | Result |
|---|---|---|---|---|
| `compact_canonical_extension_identities.py` | local identities of the compact canonical extension and the separable density formula (verifier's result) | 6.3.1 (c) | 0.87 s | pass (all residuals 0) |
| `higher_order_transport_identity.py 2 4 6` | a referee's residual identity (3.4) for K_n, n = 2, 4, 6, without imposing the equations | 6.3.1 (h) | 0.79 s | pass (residual 0) |
| `fourth_order_transport_identity.py` | a referee's identities (18) to (20) for the fourth-order quantity K | 6.3.1 (h) | 0.56 s | pass, identical to the stored log |
| `fourth_order_identity_density_bound.py` | a referee's identity (17) (same identity in another form) | 6.3.1 (h) | 0.56 s | pass, identical to the stored log |
| `log_cutoff_transport_example.py` | a referee's example (M) with a logarithmic cutoff, A q = 4 | 6.3.1 (h) | 2.79 s | pass, identical to the stored log |
| `frozen_fifth_order_examples_traces.py` | axis limits (16), the Q_2 closed form (14) and the cone blow-up (17) of a referee answer | 6.3.1 (j) | 0.96 s | pass (Z_3, Z_5 table as stated; d_y^4 Q_2 = 3 kappa/(r (1 + kappa^2)^(5/2))) |
| `Q2_velocity_and_axis_drift.py` | velocity and axis drift of the Q_2 example | 6.3.1 (j), nonlinear remainder | 540 s | TIMEOUT (rc 124); the first two exact steps printed before the limit (-Lap U2 - v0_ss = 0 and -dU2/dy(s, 0) = 4 S^2/5 for the first sign); the later simplifications did not finish within 9 minutes (two runs, the second unbuffered) |
| `Q2_cone_recurrence_log_defect.py` | the cone reduction (5.1) and the Q_2 compatibility defect: no correction without log r | 6.3.1 (j) | 4.26 s | pass (frozen checks [0, 0, 0]; consistent through angular order 7, inconsistent at orders 9 and 11, as stated) |
| `transport_example_cutoff_numerics.py` | a referee's transport example with an explicit C^infinity cutoff, A = 6/5 and 5/4 | 6.3.1 (j) | not rerun | skipped: the original run took more than 90 minutes; its log `transport_example_cutoff_numerics_output.txt` is complete for A = 6/5 and incomplete for A = 5/4 |
| `log_primitive_transport_example.py` | the verifier's example with a log primitive at A = j - 1 | 6.3.1 (j) | 1.43 s | pass, identical to the stored log |
| `thin_packet_velocity_suppression.py` | a referee's packet estimate (21) for thin packets (numerical) | 6.3.1 (j) (iii) | 22.6 s | pass, identical to the stored log |
| `local_exclusion_reference_values.py a` | B, dB/de and dB/dA at fixed shape at A = 10.150725 and at A = 4, e = 1/16 | 6.3.1 (o), first part (iv) | 0.08 s | pass: 0.325795091172477577, -15.1525473710004066, -0.0151217387326; 0.153095696660659004, -4.15355281375005299, -0.0651471618470 |
| `local_exclusion_reference_values.py b` | DB(phi_3), DB(phi_5), DB(phi_7) by central differences of bref.py | 6.3.1 (o), first part (iv) | 171 s | pass: 0.82913517178, 0.48431395934, 0.21490833993 |
| `local_exclusion_reference_values.py c` | B and g(1) of the fitted reference, and the referee's closed form of g_0(1) on K = 12, 18 | 6.3.1 (o), first part (iv), (v) | 30.9 s | pass: B = 0.2840732292314196, g(1) = 0.402227900155322443, g* = 29.7492; closed form equals the rebuilt g(1) in all 20 printed digits on K = 12 and K = 18 |
| `reference_taylor_separations.py` | Taylor separations of the aligned references (lower bounds for N-distances) and their order-7 coefficients | 6.3.1 (o), second part (iv); the order-7 coefficients in first part (v) | 0.06 s | pass: 0.5005586, 0.5325893, 0.0328100; order-7 coefficients 6.8559 (K12), 6.3755 (K18), 6.3431 (fit) |
| `finite_angular_modes_identities.py` | the verifier's result on finitely many physical angular modes: coefficient formula, identity and classification | 6.3.1 (p) | 17.2 s | pass (all True) |
| `source_cone_seed3_recurrence.py` | the verifier's construction on a left cone for the seed m = 3 (recurrence (11), forcing (14)) | 6.3.1 (r) (i) | 2.97 s | pass (predicted coefficients reproduced at A = 3, 5/2, 6; residuals about 1e-15) |
| `source_cone_general_seed_recurrence.py` | the verifier's construction for general odd seeds m >= 3 | 6.3.1 (r) (i) | 4.72 s | pass (30 of 30 checks True in six cases; residuals 1e-14 or smaller) |
| `cone_family_G5_G7.py` | the axis coefficients G_5, G_7 of the multi-seed cone solutions | 6.3.1 (r) (i) | 23.1 s | pass (residuals 0) |
| `third_order_forcing_and_r12_fifth_coefficient_A2.py` | (a) the forcing F of (D + 2 b_y - 1) K = F; (b) B_5 and G_5 on R12 data at A = 2, L = 2 | 6.3.1 (m); 6.4, "The range 1 < A <= 2 beyond 6.3.1 (m)" | 5.51 s | pass (residuals 0; B_5 = 11/1474560) |
| `resonant_fifth_order_log_residue_A2.py` | the log term of the fifth-order axis equation at A = 2 (resonance residue) | 6.4, same item | 5.75 s | pass (residues 0, 0, -273 eps/2) |
| `r12_third_coefficient_zero_SA.py` | B_3 on R12 data for 1 < A < 2 vanishes at L^2 = S_A | 6.4, same item | 205 s | pass (J at the zero about 1e-28; ratios 0.5 and -1 as stated) |
| `frozen_kernel_fourier_solution.py` | the frozen operator at P in Fourier variables and its general solution for both signs of eta | 6.4, "The frozen kernel at P" | 2.57 s | pass (all True) |
| `frozen_packet_even_y3_trace_at_source.py` | G_3(0) for an imaginary even packet at A = 3, g* = 3.5 (numerical) | 6.4, "The frozen kernel at P" (iii) | 1.40 s | pass, standard output identical to the stored log (G_3(0) = 3.103652e-5; -2.879341e-5 against -2.879354e-5); a scipy IntegrationWarning is printed on standard error |
| `frozen_packet_odd_y3_trace.py` | the y^3 axis coefficient of an odd packet: K s^(1/2) + c_1 s (numerical) | 6.4, "The frozen kernel at P" (iii) | 1.00 s | pass (5.996e-5 at s = 1e-4 against K = 6.048e-5; c_1 = -5.224e-5, stable); same warning |
| `r12_fifth_coefficient_finite_part.py` | B_5 on R12 data at L^2 = S_A, 1 < A < 2, from the axis hierarchy | 6.5, "Toward NO_inf for 1 < A <= 2" | 18.1 s | pass (B_5 equals the referee's formula (21) to 20 digits at A = 5/4, 3/2, 9/5) |
| `r12_fifth_coefficient_sign.py` | positivity of the polynomial factor and the value at A = 2 | 6.5, same item | 0.42 s | pass (P(1 + z) positive; -7.45988e-6 against -11/1474560) |
| `euler_beta_finite_part.py` | finite parts of Euler-type integrals against beta-function values | 6.5, same item | 0.48 s | pass (differences 3.59e-14, 3.25e-14, 2.85e-14) |
| `r12_fifth_coefficient_global_sign.py` | the verifier's global-sign proof for R12 data | 6.5, same item | 7.74 s | pass for all exact checks; one diagnostic line (a direct Taylor-subtraction quadrature, "FP Euler vs Beta") prints meaningless values of order 1e46 to 1e131 because of cancellation; that comparison is done accurately by euler_beta_finite_part.py |
| `r12_third_coefficient_general_L.py` | general-L identities of the corollary of the verifier's seventh-order resonance proof | 6.5, same item | 1.26 s | pass, identical to the stored `.out` |
| `r12_seventh_coefficient_A2.py` | B_7 = -23/29059430400 at A = 2, L = 2 | 6.5, same item; 6.4, "B_5 and B_7" | 2.52 s | pass, identical to the stored `.out` |
| `area_preserving_pullback_structure.py` | the structure of a referee's counterexample for a generic generating function F(s, v) | 6.5, "Higher jets" | 0.80 s | pass (all residuals 0) |

Summary: 31 runs of 29 scripts (one script in three modes); 30 runs pass (exit code 0, results as stated in the
report or identical to the stored logs), one run times out (`Q2_velocity_and_axis_drift.py`), and one script was not
rerun (`transport_example_cutoff_numerics.py`).

## Changes made to the copies

Code was changed only where a path pointed outside this folder, plus neutral wording in comments, docstrings and one
printed label; no computation was changed. In detail (`SANITIZE_LOG.md` lists every change with the original text):

- `reference_fit/verification/fit_reference.py`: the input trace is read from `data/c6g_traces.npz`, and the output
  field `source_file` is the relative name `reference_fit/data/c6g_traces.npz`.
- `raw_bounds/norm_repair/norm_repair.py`: the reused source is `../03-norm-and-radius/verification/rational_certificate.py`
  (relative), and the output field `source` is that relative name.
- `radius_budget/verification/radius.py`, `trace_uncertainty/verification/analytic_bounds.py` and `compare.py`: paths to
  `obstruction_certificate/` follow the new folder names; an unused absolute path was removed from compare.py.
- `audit_rerun/audit_checks.py`: reads the certificate folders under their new names, checks only the files that are
  here as byte-identical copies, no longer checks the digests of the referee's original files (these are not part of
  this package), and records the mpmath module path relative to the site-packages folder.
- `b3_functional/`: the import paths of `dcode/` and `b3infl/` and the output paths are relative to the program; the
  trace folder is taken from `TRACE_DIR`; lin_r12.py, exact_analytic.py and check_lin.py read their inputs by relative
  paths.
- `symbolic_checks/`: renamed scripts; local_exclusion_reference_values.py and reference_taylor_separations.py read
  their inputs by relative paths.
- In the PROOF.md files, references to the referee's own folder names were replaced by links to the corresponding files
  here, and sentences that pointed to files not included were dropped. JSON outputs that recorded absolute input paths
  record relative ones.
- The docstring of `rational_certificate.py` still gives the run command of the referee's own layout; it was left
  unchanged because norm_repair.py records the SHA-256 of that file.

## Not included

- The referee's provenance files (the input manifest with digests of the original inputs, its artifact checker and its
  verification log) and the collaboration status files. `audit_rerun/sources.json` lists them with their digests.
- The stored traces of the first investigation other than `c6g_traces.npz`, which the programs of `b3_functional/` can
  read through `TRACE_DIR`.
- The referee's copy of the remainder estimate under `radius_budget/verification/reference_estimate.md`: it is
  byte-identical to `raw_bounds/02-remainder/PROOF.md` (same SHA-256), and the links in `radius_budget/PROOF.md` point
  there.
- The index and verification summaries of the referee answers, the private copy of the obstruction certificate that the
  audit referee checked (the audit now checks the copies here), and the short verification note of the 6.3.1 (n)
  referee, which only points to the proof and to that referee's shared checks file (also not included).
- The research records of the run (work logs, notes, job queues).
