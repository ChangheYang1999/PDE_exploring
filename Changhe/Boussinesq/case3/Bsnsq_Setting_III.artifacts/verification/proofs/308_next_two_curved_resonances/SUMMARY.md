# P308 next two local transverse compatibility conditions

Published 2026-10-22T07:49:47.182865+00:00. Own mathematical verdict: CONFIRMED. External model audit: OPEN because actual Opus5.5 requests534 and535 returned no audit text. No broad B2 endpoint is asserted.

For beta=2, s=y_*-y and Ck nonzero, use B=s+ks^2-(Ck/260)s^13 and H=-k^7/231 from P306. The two free homogeneous constants E and F in theta2=D/24 and omega1=gamma/6 can be chosen uniquely to remove the next temperature and vorticity resonances. The complete arbitrary-parameter proof is in PROOF.md. With the explicitly specified normalizations, the residue matrix is

    [ 12 C k / 25          0          ]
    [ -9 k^8 / 1925       -9 C k / 20 ].

Its determinant is -27 C^2 k^2 /125, hence nonzero. The two affine constants are finite Laurent coefficients of the baseline solution. The proof derives every matrix coefficient using convergent analytic units and residue integration by parts, including the explicit s^13 curvature corrections. It does not infer arbitrary-parameter validity from samples.

A separate exact Fraction recurrence checks six rational parameter pairs, all four matrix entries, their determinant, the affine dependence, and both tuned equations. All256 controls pass in 4.023423 seconds. Independent Sympy Cartesian expansion and finite residue sums give23 of23 controls in 0.870010 seconds. The original182-control output is preserved. The preparation was recorded before calculation, and the complete proof hash was recorded before the matrix extension.

The resulting analytic local polynomial stream has exact Poisson relation, thermal residual O(x^8) and vorticity residual O(x^7). The free homogeneous constants in theta3 and omega2 remain. This proves compatibility of only finitely many local transverse equations. It gives no convergent full transverse series, local exact transport solution, center attachment, canonical full-plane inverse or global B2 profile. The prior sign restriction Ck<0 belongs to this explicit polynomial B family; it is not a universal endpoint obstruction.

Reading order: P303, P306, then this PROOF.md, followed by verification/symbolic_checks.json and verification/fraction_checks.json. Formal sources are documented in formal_sources/README.md; no Lean build was used.
