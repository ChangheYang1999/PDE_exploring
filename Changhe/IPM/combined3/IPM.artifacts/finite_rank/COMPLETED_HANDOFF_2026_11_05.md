# Completed source and finite-rank handoff

The actual Candidate013 whole-plane source coefficient certificate is complete. The final fixed-parameter numerical join also passes, including the independent root and auditor reconstructions. The coefficient producer and its adopted output are frozen. All inherited candidate data were read without modification; every file produced by this work is under `combined3`.

The closing proof uses the local integer background-energy identity in the auxiliary norm
\[
 Q(g)=\|\sqrt{1+4|x|^2}\,J^{21/10}g\|_2.
\]
The older separate compact-remainder pricing route is retained as reproducible research, but its incomplete or nonclosing estimates are not premises of the closing proof.

## Actual source certificate

`Q_source_certificate_v01/result.json` has status `CERTIFIED_WHOLE_PLANE_Q_SOURCE_CONSTANTS`, finished at **2026-11-05 01:53:14 UTC**, and SHA256
`b593bf4fda27af6cc8cbd8a6808fcf821dbe0d2327f32e9d7b741599e6201500`.
It includes all **2303** exact rational radial panels between \(10^{-5}\) and \(10^5\), with exact-source Taylor/Arb enclosures and explicit analytic origin and infinite exterior tails. The stored exact-source hashes bind Candidate007 and Candidate013 separately. No sampled norm is promoted to a certificate.

With \(b=\nabla\rho_*\), \(D_j=\||D|^jb\|_2\), \(X_j=\||D|^j(xb)\|_2\), and \(H_1=\sup W|Db|_F\), convenient outward bounds are:

| Quantity | Rigorous upper bound |
|---|---:|
| \(H_1\) | 14.830022 |
| \(D_1\) | 17.011863 |
| \(D_2\) | 10.465985 |
| \(D_3\) | 28.414492 |
| \(D_4\) | 992.320397 |
| \(X_2\) | 57.993746 |
| \(X_4\) | 279.211967 |
| \(A_2\) | 222.176812 |
| \(A_{21/10}\) | 247.657246 |

`Q_SOURCE_CONSTANT_CERTIFICATE_PROOF.md` supplies the radial identities, rigorous panel integration, remainder estimates, and tails. `Q_SOURCE_FRACTIONAL_COMMUTATOR.md` proves the actual fractional source bound, including the cutoff passage for the slowly decaying coefficient and its growing coordinate multiple. `TRANSPORT_THIRD_SYMBOL_REFINEMENT.md` supplies the improved third-symbol bound and the corresponding growing-velocity cutoff passage. The radial identities were separately checked against Cartesian derivatives in `Q_source_radial_reduction_audit.json`.

The earlier exploratory value 16.453 was a sampled **Cartesian componentwise angular-l1 majorant**, rather than a sampled Frobenius Hessian norm. The certified 14.830022 uses the tighter polar component combinations before angular enclosure. Those different upper-bound constructions are consistent.

The original producer may be reproduced or resumed with:

```sh
PYTHONDONTWRITEBYTECODE=1 /tmp/ipm-combined3-venv/bin/python -B \
  Changhe/IPM/combined3/IPM.artifacts/finite_rank/certify_Q_source_constants.py \
  --out Changhe/IPM/combined3/IPM.artifacts/finite_rank/Q_source_certificate_v01 \
  --workers 6 --chunk 16
```

Saved chunks bind the original configuration and all source-code/data hashes. Three host restarts were survived by resuming these checkpoints. The disjoint end-chunk prefetch has its own binding manifest. A second assembly process, `replay_Q_source_assembly_memoized.py`, reuses the identical input records in a separate directory and only memoizes a pure exact-rational binomial function; its manifest records the final comparison without changing the original producer or output.

## Final numerical join and scope

The strict consumer `../operator_theory/fixed_parameter_closure_v01.json` selects
\[
 c=4076476460239181/2251799813685248,\quad
 R=381377/10^{12},\quad M=3/10,
\]
with source split radius 30000. The auxiliary matrix lower bound is \(7/10\). The signed matrix-prefix certificate includes its analytic origin/exterior coverage and an independent replay, so it does not require waiting for the redundant full-panel matrix calculation.

The source, local coefficients, actual matrix, forcing bound, scalar nonlinear inequality, and L2 resolvent constants are all bound and checked by that consumer. Its independent 768-bit root reconstruction is `../ROOT_FINAL_LOCAL_Q_REPLAY.json`; a further independent join is `../independent_closure_audit/final_join_audit.json`. They agree on:

| Quantity | Certified value, displayed approximately |
|---|---:|
| Background loss on the boundary scale | 0.1576521494423 |
| Nonlinear loss | 0.2279989010220 |
| Frozen exterior decay | 0.3143489495358 |
| Self-map energy margin | 0.0260144054582 |
| Contraction ratio | 0.1222349413236 |

The globally valid background form has outward constants \(\varepsilon=3491/31250\), \(C=28427625600\). With those rounded constants the self-map margin remains greater than 0.02601426. The final scalar join is a numerical premise of the separately audited analytic local-energy, forced-evolution, regularity, and Banach arguments; this handoff does not substitute a numerical check for those proofs.

The explicit graph comparison in `Q_TO_INHERITED_N_EXPLICIT.md` also preserves the originally requested norm bound: for the chosen \(Q\)-ball, the independently reconstructed inherited norm bound is less than **0.355363**, hence less than **0.387**. The fresh nonlinear proof is referenced in `QNORM_NONLINEAR_BOUND.md`; no missing old numerical PR/CORE audit is a premise.

## Actual finite-rank deliverable, qualified

`actual_rank1_operator_tail_certificate.json` and `ACTUAL_RANK1_OPERATOR_TAIL_PROOF.md` give an actual smooth normalized S1 basis
\[
 \phi_{01}(x,y)=\sqrt{2/\pi}\,y e^{-(x^2+y^2)/2},
\]
an enclosed matrix entry \(A_{11}=-0.0686740077826\ldots\), the original-norm dual Gram entry \(B_{11}=76.2424846959\ldots\), and the certified tail bound
\[
 \|K-PKP\|_{L^2\to L^2}<7071/10000,\qquad C_N<1309/250.
\]
The tail follows from actual full-plane \(\kappa_{HS}\le0.710328127936\) and Hilbert–Schmidt orthogonality after subtracting a lower enclosure of \(|A_{11}|^2\). Its independent rank-one replay includes the quadrature tails and source bindings. The Gram refers to \(N_2(g)=\|J^q(W_2g)\|_2\), not to \(Q(g)\). This rank-one estimate is explicitly **nonclosing** and is not charged in the successful local-energy join. Higher-rank matrices and earlier source/Ew screens remain exploratory unless their individual files state and verify a rigorous certificate.

The additional universal full-gradient Gaussian Cvs3 high-pass Hilbert–Schmidt bound in `CVS3_GAUSSIAN_HS_ONE_THIRD_PROOF.md` is independently certified. It is likewise an auxiliary result, not an additional loss in the final local identity.
