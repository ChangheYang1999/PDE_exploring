# Independent refinement of the old anisotropic margin to three

## Statement and hypotheses

Use exactly the normalized joined modal trial, canonical Green reconstruction, weight and coefficient margin m_old of proof 193. In particular the inner radial logarithmic slope is -17/2, the outer slope is -5/4, the angular weight is |cos(theta)|^(-17/2), and both one-sided energy expressions are retained at r=1. The assertion to check is

 m_old(X) >= 3 for every X !=0.

This is a coefficient inequality only. It implies neither injectivity of the coupled operator nor a quantitative inverse or nonlinear existence. Until the production and audit below pass, the assertion is OPEN. All exact input hashes and actual run times belong to the evidence files.

## Complete argument

Proof 193 proves a complete cover with1352 unrefined radial roots and281535 angular rectangles, together with the two analytic half-lines. This cover is itself assembled from topics68 and82 by exact binary partitions and exact retained-parent identities. Reconstruct every retained root and angular leaf of that final cover. Retain precisely those whose directed rational lower bound is at least3. For each deficient complete radial root partition the angular quadrant into128 equal exact intervals. For each deficient angular rectangle use the rectangle itself as the new parent. No region is omitted because a neighboring rectangle has a good lower bound.

For each new parent, enclose all261 velocity modes and262 density modes using the original source, exact scalar repair, certified Green cache and the exponential-polynomial Taylor enclosure of topics68,82,193. Assemble q=V.e_r/r, tan(theta)V.e_theta/r, rho_x and rho_y. Bound b_plus=(|grad rho|-rho_y)/2 by the directed norm bound, and also by rho_x^2/(2(|grad rho|+rho_y)) when rho_y is strictly positive. Either upper bound is valid, so their smaller upper endpoint is valid. Form m_old with the exact weight coefficients. Accept only when its directed rational lower endpoint is at least3. Otherwise bisect the exact radial or angular interval. A finite complete binary tree partitions its parent with disjoint interiors and closed union. A failed depth limit remains an unresolved parent and cannot support the assertion.

The independent audit reconstructs the entire prior cover and the exact list of deficient parents. It verifies every new journal identity, rational endpoint, binary-tree coverage, directed lower endpoint and source/code hash. It independently re-evaluates the lowest and representative new rectangles at640bits with the angular sums assembled in a different order. This replay checks the implementation but is not a statistical proof: the universal claim comes from the analytic interval enclosure applied to every accepted rectangle. The original-data production uses512bits. Both analytic half-line formulas of proof 193 must separately exceed3 at both precisions.

Once all finite rectangles and both half-lines pass, their union is the punctured plane by parity and the prior coverage theorem. The displayed margin bound follows pointwise, including the continuous trigonometric extension at the vertical axis and both traces at r=1. The exact weight is continuous at r=1, so its weak first derivative produces no interface measure.

## Dependencies and verification status

Topics04,68,82,193 and their archived exact original-data, Green, scalar-repair, coverage and replay certificates. No numerics-team merged arrays are certificate inputs. No numerical conclusion has yet been accepted in this file.

## Accepted certificate, 2026-10-28T16:07:41.696755+00:00

The512-bit original-data production completed at2026-10-28T16:04:09.861502+00:00 in164.259825seconds. It replaced19186 deficient parents by36196 rectangles, with zero failures. The complete coverage audit and alternate640-bit replay completed at2026-10-28T16:07:10.940023+00:00 in74.157722seconds, status CONFIRMED. It retained1335 complete prior radial roots and264525 prior angular leaves, verifies every new binary tree, and replays34 lowest/representative rectangles with independently assembled angular sums. Both analytic half-lines also exceed3. All finite lower endpoints and both half-line expressions are exact directed rationals in the evidence. Therefore m_old>=3 is CONFIRMED on the whole punctured plane, with both one-sided expressions at r=1. The result is a coefficient inequality, with no inverse or nonlinear conclusion.

Journal SHA c6604baa96ade01eb204a91429fc7d6e3e1a3cdd5b911a5786ba44fab5029994; production metadata SHA d3bc1249f48ee92da02f7f146bdb918fc0ab78043e7958574ee14b6740b3b53d; audit SHA 271980386cad3e3a27b7845473eaa574a197961c59dc6694fd5255c457c4e20e. The preliminary proof used before computation is archived as evidence/proof_before_certificate.md, matching the production hash. The auditor's first attempt stopped before replay because its identity dictionary omitted the radial row; the stopped log is retained. The corrected audit uses(row,parent id), validates exact parent cardinality and coverage, and passed. Production inputs, journal and all numerical enclosures were unchanged. This was an audit-code identity error, not an unresolved coefficient bound.
