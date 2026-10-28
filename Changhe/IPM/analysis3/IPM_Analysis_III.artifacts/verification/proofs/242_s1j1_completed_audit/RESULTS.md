# Accepted completed-run checks

Recorded 2026-10-28T16:55:14.211498+00:00. The run completed before this audit. The independent check ran at 2026-10-28T16:54:16.133953+00:00 in 3.827553 seconds, single-threaded. Its producer and original-data hashes were checked. No quadrature was rerun in this check.

## Certified input result

With the exact functions, low norm and binary summation convention of PROOF.md, for every real vector v of length38,

 |v^T(G_f-G)v| < 0.000431058 v^T G v, for v nonzero.

Equivalently, (1-0.000431058)G < G_f < (1+0.000431058)G as quadratic forms. The 640-bit proof uses an exact dyadic whitener and interval row sums. Its identity defect is less than1.746e-61; its exact directed relative-error upper endpoint is strictly below0.000431058. The displayed decimal was compared to that endpoint using rational arithmetic. The entire exact G, including both infinite ends, comes from the original-data certificate of proof 239. The input is positive definite.

All1569 expected cell IDs occur once in the four final part files, with counts393,392,392,392. All four completion records and DONE are in the archived log. Checkpoint prefixes are duplicates and were excluded; no base or resumed run was used. This proves accounting and provenance, not correctness of the producer's output integrations.

## Floating output observations

Every entry in this table is an uncertified finite-matrix diagnostic. Restrictions and whitening use70 decimal digits, followed by a symmetric double-precision eigensolve. The high_input and high_graph rows refer to the exact rational32- and29-dimensional subspaces of proof 240, still evaluated in the LOW norms. They are not high-norm singular values. The c0 row uses only the stored binary strain constraint.

| Section | Dimension | First value | Second value | Third value |
| --- | ---: | ---: | ---: | ---: |
| all | 38 | 4.7481346288 | 15.1418685728 | 34.2871047477 |
| inner_pure | 33 | 50.3200901662 | 51.5761369577 | 53.1575002648 |
| pure | 26 | 50.3200902219 | 52.3913830813 | 56.3793501246 |
| outer | 5 | 4.7557814675 | 15.1894087364 | 34.9383031151 |
| high_input_in_LOW_norms | 32 | 5.8702526254 | 23.4364131200 | 51.5912748426 |
| high_graph_in_LOW_norms | 29 | 7.4691975230 | 41.2424592742 | 51.6020221040 |
| all_exact_input_midpoint_FLOATING_output | 38 | 4.7481356018 | 15.1418741043 | 34.2870790899 |
| stored_c0_FLOATING_constraint | 37 | 4.7481445676 | 15.1419387755 | 34.2892567876 |

The weakest coefficient vector of the full section is concentrated in the shifted outer columns, especially out9, out5 and out8. This is a numerical observation about the declared coordinate normalization. It supplies no localization theorem or continuum lower bound. The comparison with the exact input midpoint is also floating and does not certify the output.

## Evidence and limits

- PROOF.md SHA256 ea5e6803cd0873f416c1c19fd9b07903432dd967d8a8bb2fc6c65603479a9bba.
- code/check.py SHA256 b95b38e5a6c014b3fea179f6c668502dcb6c0f9dcc8783f23a9a37f86ab601a3.
- evidence/check.json SHA256 d914261070b49feed82cd4d341c0e10225c0df940a989eaf494d15b41b170cd4.
- evidence/acceptance.json records exact outward rounding and the already reviewed domain dependencies.
- All four final arrays, metadata, frozen producers and the complete production log are archived in evidence/source. Their hashes, the exact dyadic whitener and the assembled matrices are recorded in evidence/check.json.

The output division and integration errors are still OPEN. This result supplies no certified output Gram, operator singular value, high-norm inverse, complement estimate, base injectivity, nonlinear smallness or profile existence theorem. No failed calculation preceded the accepted run.
