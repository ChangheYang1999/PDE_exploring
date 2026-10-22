# P324: exact nonlinear coefficient checks

Checked 2026-10-22T09:15:13.022559+00:00. CONFIRMED within the finite local scope of PROOF.md. The evaluator was written independently of lead and numerics code. It uses verifier-owned rational Laurent arithmetic and directly recomputes the nonlinear transport forcings.

| Run | Parameters and stages | Passed | Thermal / vorticity / Poisson consistency | Negative checks | Minimum tested range |
|---|---|---:|---|---:|---:|
| n5w100 | C=1, k=-1; n=2..5 | 76/76 | 18 / 18 / 18 | 0 | 96 |
| n8w160 | C=1, k=-1; n=2..8 | 163/163 | 42 / 42 / 42 | 0 | 150 |
| n10w190 | C=1, k=-1; n=2..10 | 236/236 | 63 / 63 / 63 | 0 | 176 |
| n5w110_C2khalf | C=2, k=1/2; n=2..5 | 92/92 | 18 / 18 / 18 | 16 | 106 |
| n2w50_v3 | C=1, k=-1; n=2..2 | 23/23 | 3 / 3 / 3 | 4 | 52 |
| n2w50_v4_C2khalf | C=2, k=1/2; n=2..2 | 23/23 | 3 / 3 / 3 | 4 | 52 |

Every Poisson check tests a defining construction/update identity and is not independent evidence that Poisson has been solved. The genuine independent substitutions here are the thermal and vorticity coefficient operators. The finite analytic-jet checks detect negative powers only. General analyticity is supplied by P321/P326.

The final source, range and precision comparison passes176/176. Exact constants and finalized overlapping coefficients agree across widths100/160/190. The version2/version4 C=2 stage2 constants also agree. Original 40-check and intermediate comparison code are retained; the final file supersedes their counts.

The longest run started2026-10-22T09:05:35.013337Z and completed2026-10-22T09:13:19.996150Z, elapsed464.982813s. All other run times and hashes are in their JSON records. Actual Claude Opus5.5 reviews563,564,567 progressively checked the sources and reporting; follow-up567 found no remaining material defect. Reporting repairs and rejected model remarks are in verification/model_adjudication.md.

Growth in the transverse index, convergence of the formal series, an actual local PDE solution and a full-plane B2 endpoint are OPEN. Large finite constants prove neither convergence nor divergence. No heavy process remains.
