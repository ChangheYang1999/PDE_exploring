# Late Phase III saved-factor check

Registered 2026-10-30T10:23:28.158835+00:00, before independent matrix computations of the F1m3, F2m4, PERT and P3cont4 endpoints. Lead numerical summaries have already been read. This plan extends ../PROOF.md and spectral_gap/PROOF.md with the existing qualified arithmetic; it does not create a new mathematical claim.

First apply the unchanged endpoint/QR witness auditor, with only the four endpoint identities and registration paths changed. It verifies the complete and closure-lagged factors, current coordinates, checkpoint, source copy, full manifest, and original lagged factor. Its largest-singular-value tolerance remains1e-12.

Then use the already qualified independent_sensitivity_gesdd_v1.py. Reconstruction/orthogonality controls remain1e-11, partition1e-10, lead eta comparison absolute2e-7, direct physical-gradient comparison relative1e-10 and reduced-system comparison relative1e-4. No tolerances will change on these outputs. Report tiny singular values only as floating-point values, never exact rank. Report widths as local quadratic model widths, not uncertainty.

For P3cont4 apply the existing1e-11 reporting filter separately to the complete normalized matrix T and phase-complement coefficient matrix A. The lead's margins.py currently computes T; its gap is not by itself the coefficient-cutoff gap. Report eta only when its T cutoff passes, and reduced values only when their A cutoff passes. Target the lead's chosen1e-8 coefficient cutoff. For the even-mode ends compare the established1e-12 default. Preserve other calculated cutoffs as diagnostics with their margins.

The computations use saved factors, not a new residual or full Jacobian, and do not establish a matrix-error bound against the unavailable full Jacobian. They can confirm finite-dimensional failures of stationarity(b),(d) only under that saved-factor interpretation. The final field cohort and its random data remain untouched.

CPU35, nice10, one busy computation and one BLAS thread, hidden GPU. Individual endpoint stage300s, sensitivity stage360s, no new stage after11:15Z, all work killed by11:25Z if needed. Preserve failures and timeouts. No JS/TS, servers, RLScience/cluster, paid remote compute, Lean or writes outside this side.
