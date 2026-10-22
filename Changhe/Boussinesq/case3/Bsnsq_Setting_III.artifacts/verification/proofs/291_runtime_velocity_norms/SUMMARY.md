# Independent whole-plane velocity norms versus reported runtime norms

Written 2026-10-22T06:17:20.682617+00:00. CONFIRMED as a finite numerical comparison with the stated conditional interpretation. This is not a certified error bound or a reproduction of absent runtime component arrays. General B2 remains OPEN.

PROOF.md and SUPPLEMENT_PROOF.md contain complete norm, Green inverse, gauge and exact-moment arguments. Six raw archives and six runtime JSON tables were frozen before evaluation. The primary computation passed142/142 controls in 46.208624 seconds, from 2026-10-22T06:11:48.018044+00:00 to 2026-10-22T06:12:34.224579+00:00. An additional independently fixed second-moment and native-knot-partition computation passed27/27 in 5.198724 seconds. Symbolic formula checks passed17/17 in 1.170784 seconds. The primary proof had a dummy-variable typo H_n(r) under the rho integral; Opus501 detected it, and it is corrected to H_n(rho). The code always used the correct integration variable. Original proofs, manifests and completed controls are preserved. The corrected formulas satisfy the exact radial Poisson and derivative identities.

## What was independently evaluated

At each of eight radii100,1000,...,1e9, we evaluated the canonical full-plane relative velocity V=B[Omega]+lambda B[f] on the same181 interior half-circle angles phi=j pi/182 as the runtime tables. The maximum M(V) is over both Cartesian components and these angles. It excludes beta X. The unknown and fixed source keep their separate native bases. Our physical-radius inverse uses adaptive quadrature through infinity and no numerical-lane code or interpolation. We use two tolerances1e-10 and3e-12. The largest relative change of component arrays over48 circles is 1.19810312e-11. At r1e8 and1e9, a second calculation replaces the n2 exterior integral by the exact full-plane strain moment minus the interior moment and partitions both integrals at all native spline breakpoints. Its largest relative array difference is 9.47955625e-13. These are consistency checks, not enclosures.

The numerical lane publishes D=max|V48-V12| and M48=max|V48|, but no V12/V48 component arrays or source-archive hash in those JSON tables. We froze the named raw archive, checked its beta/lambda/K against the table, and inspected the runtime source read-only to identify its norm, angle, source and gauge convention. We did not execute or import that code. Arithmetic of all published ratios agrees with the recorded maxima. The actual runtime difference vectors and exact provenance to a particular source hash remain unverified. Full reproduction of D is OPEN.

## Radius 1e9 comparison

The columns below use the published M48 and D, and our independently computed M. The reverse triangle inequality gives max|V48-V| >= |M48-M| if the reported norm and independent inverse are accurate. Thus the final column is a conditional numerical lower diagnostic for the48-order velocity error, relative to M. Without rigorous error control it is not a proved numerical bound. Independently, D<=max|V48-V|+max|V12-V|, so at least one runtime order has error at least D/2. Small D cannot bound either error from above.

| State | Independent M | Reported M48 | Reported D | |M48-M|/M |
|---|---:|---:|---:|---:|
| rtvel_K32_b3062 | 3255525.751 | 4197433.08 | 1219624.581 | 0.289325719 |
| rtvel_K32_l095 | 1794349.05 | 1689905.447 | 32669.37187 | 0.0582069594 |
| rtvel_K40_b3092 | 3923579.871 | 5118488.047 | 3559544.997 | 0.304545394 |
| rtvel_K48_b3062 | 3234750.706 | 4188451.827 | 1828370.512 | 0.294829867 |
| rtvel_K48_b3092 | 3906358.982 | 5111888.351 | 4058537.139 | 0.308606909 |
| rtvel_L2K40_b3085 | 1054623.902 | 1822977.538 | 291.196362 | 0.728557009 |

The lineage-2 example is particularly informative: the runtime orders agree to about1.6e-4 of their reported48-order norm, while that norm differs from the independent full-plane norm by about0.729 of the latter. The small two-order difference does not measure the common discrepancy. The exact source of that discrepancy is OPEN: these scalar tables alone do not isolate interpolation, quadrature, implementation or provenance. The read-only runtime code identifies a differentiated interpolant of modal stream values, which is a possible source to investigate, not a causal conclusion from this test.

Every radius and both beta-r normalizations appear in verification/NORM_COMPARISON.csv. The original independent component arrays and refined comparison evidence are retained. This packet makes no claim about a pointwise relative error denominator at a zero of velocity, a uniform angular or radial bound, a root shift, discretization convergence, or a B2 profile.

## Actual model review and adjudication

Opus501 and503 both returned claude-opus-5-5 through the existing Bedrock Python client, requested as us.anthropic.claude-opus-5-5. Their public answers were read in full. Opus501 validated the norm inequalities, inverse, gauge and conditional interpretation, identified the displayed dummy-variable typo, and marked the storage-to-moment dependency OPEN because it had not been supplied. The corrected proof and complete storage calculation were sent in503, which explicitly resolves both issues. The verifier independently checked the corrected formulas symbolically and the moment numerically. Its minor notes are accounted for: the knots span[0,1], and both b and L are read as exact binary rationals by exact_moment2. Neither model verified raw artifacts, so their review is not presented as a numerical endorsement.

## Dated verdicts

- CONFIRMED: elementary norm inequalities, full-plane relative inverse formulas, and exact storage-to-moment identity under the stated class.
- CONFIRMED as finite computations: independent component norms and tolerance/partition consistency, artifact arithmetic and stated metadata joins.
- REFUTED as an inference: a small difference between two quadrature orders gives an upper bound for either exact-inverse error.
- OPEN: reconstruction of the runtime difference vectors, certified quadrature/interpolation errors, causal attribution of the common norm discrepancy and general B2.
