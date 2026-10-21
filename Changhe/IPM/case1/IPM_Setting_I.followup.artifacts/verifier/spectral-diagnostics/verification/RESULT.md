# Independent spectral-diagnostic audit

Date: 2026-10-20T18:43:45Z. Verdict: the stored diagnostic arrays are CONFIRMED; several prose ranges and the inference excluding limiting singular or approximate-kernel behavior are REFUTED. Q1 remains OPEN.

Own DCT-I and DCT-II transforms reconstruct all18directions on the96/L8,120/L8 and96/L4 states. No numerics code is imported. Against the supplied diagnostic arrays, the largest spectrum-statistic discrepancy is1.89e-14; nodal fractions agree exactly; axis profile discrepancy is1.75e-16; second-difference discrepancy is5.21e-13. Input checksums are in audit.json. These comparisons reproduce calculations on specified finite arrays, not an exact PDE Jacobian.

| State | Max radial upper-third coefficient energy, first6 | Max angular upper-third energy, first6 | Plain nodal fraction within2ofP, first6 | Plain nodal fraction r>=100, first6 |
|---|---:|---:|---:|---:|
|96,L8|5.30453e-5|2.38932e-4|0.0004261to0.0614227|0.536824to0.928085|
|120,L8|2.71110e-5|6.55129e-5|0.00002399to0.0539966|0.563557to0.858442|
|96,L4|4.74816e-4|5.37468e-5|0.0001648to0.0235581|0.333943to0.914300|

The narrower two-softest statement is supported: their unweighted delta-b nodal energy fraction at r>=100 is79.664to92.808percent across these three cases, including the compactified endpoint q=1. The fraction within2ofP is at most0.15145percent. This metric includes asymptotic coefficient nodes and is not a physical-area or relative-density localization norm. Earlier physical-weighted diagnostics use a different variable and measure.

For96,L8 Ritz1, normalized axis second differences are-0.01820775,-0.00763515,-0.00142891,+0.000517546 at h=1,.5,.25,.125. Direct Chebyshev differentiation and the analytic q-chain rule give+0.0012069983, and the new h=.0078125 result is+0.0012042641. Thus the quoted stability on the originally tested steps is false in this case. For120,L8 Ritz1 the direct derivative is-0.0722712271, versus-0.0674999659 at h=.125. The normalizer is the maximum of the absolute axis variation at the prescribed61points, not a continuous supremum. All exact derivative formulas here are evaluated in floating point, not interval arithmetic.

Every finite interpolant is analytic near P simply because its finite basis and coordinate maps are analytic there. Small coefficient tails do not imply uniform C2 bounds: f_N=1+T_N/N, evenN, has upper-third relative coefficient energy1/(N²+1), converges uniformly, and satisfies|f_N''(0)|=N. Analytic approximants can also converge in C2 to a nonsmooth function, as shown in PROOF.md. The actual stored modes are not proved to have either behavior. These examples identify the missing inference, not a new explanation of the modes.

Suggested report sentence: “The two softest stored directions have small upper-third coefficient energies and little unweighted nodal delta-b energy near P; most of that nodal energy lies at r>=100, including the compactified endpoint. These finite-basis diagnostics do not establish uniform regularity, a continuum kernel, or the absence of limiting singular directions.”
