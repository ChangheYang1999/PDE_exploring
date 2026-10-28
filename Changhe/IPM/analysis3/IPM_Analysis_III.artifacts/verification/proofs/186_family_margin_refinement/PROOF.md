# Targeted refinement of the decoupled a=4 margin

## Quantity and proposed bound

Use the exact normalized modal trial, canonical velocity V, parameter ell and complete global cover of proof 160. For the decoupled remainder weight with inner radial exponent17/2, outer exponent37/20 and angular exponent4, put

 q=V.e_r/r, v_theta=V.e_theta/r,
 b_plus=(|grad rho|-rho_y)/2,
 m_4=1+ell-(17/4)q+4tan(theta)v_theta-b_plus for r<1,
 m_4=1+ell-(37/40)q+4tan(theta)v_theta-b_plus for r>1.

The expressions at r=1 are interpreted one-sided. The weight is continuous there; the energy identity has no interface atom. Proof 160 already proves m_4>=1.13 globally. This topic attempts the stronger exact rational target12501/10000. Its status is PENDING until the production and independent audit records both pass. No result is inferred from a numerical sample.

## Reuse and refinement argument

Proof 160's independently audited partition has3276 radial roots,128 angular roots per ordinary radial root and a complete binary refinement tree in each. Each stored leaf carries a downward-rounded integer lower bound in millionths for m_4. Leaves whose stored lower bound is at least1250100 already prove the new target and may be retained verbatim. Every other leaf is replaced by a finite binary partition of that same rectangle. Each child is enclosed by the original-data interval method of proof 160 at512-bit precision, including all261 velocity and262 density sine modes. If every replacement leaf has a directed lower bound at least12501/10000, the target holds on every compact rectangle of the original cover. The complete origin and infinity estimates are recomputed with the same exact target. Together these covers prove the global assertion.

The angular quotient tan(theta) sin(2n theta) is evaluated through its finite trigonometric recurrence, so endpoint rectangles containing the vertical axis remain valid. The upper bound for b_plus uses both the direct gradient bound and, when rho_y>0, the identity b_plus=rho_x^2/[2(|grad rho|+rho_y)]. Taking the smaller of two valid upper endpoints preserves validity. No angular mode or radial tail is dropped.

The independent audit must verify the source, cache and prior-certificate hashes; identify exactly the old leaves below the new threshold; verify each replacement tree, including every endpoint and child; check all directed accepted endpoints; and replay selected worst and representative replacements at higher precision using the independently assembled angular formula from proof 160. The stored production status alone is insufficient for acceptance.

## Relation to the numerics team's outer refinement

The numerics team reports the same global a=4 target after replacing its first outer interval by eight subintervals of width1/16. Its two-stage aggregation and the generic coverage checker are separate from the original-data proof above. Actual completeness of those eight cells can be checked, but that does not by itself certify every cell enclosure or the rest of that team's global array. This topic's stronger certificate, if completed, depends only on the verifier's prior complete cover and fresh original-data enclosures. It is not an endorsement of the generic merge program.

The bound is for one endpoint of the angular family. The previously proved a=18/5 lower bound1.10534 remains unchanged. Affine interpolation in a then yields the corresponding convex-combination lower bound for all18/5<=a<=4. No injectivity or inverse constant for the full coupled linearization follows from this coefficient margin alone.

Dependencies: topics68,82,160,168 for the exact trial, interval reconstruction, prior complete cover, weight and energy identity.

## Certified result

The production and independent audits pass. Of the423719 previous leaves,415300 already meet the target. Exactly8419 leaves across718 radial roots are replaced by16838 children, each with a directed512-bit lower bound above12501/10000. The audit checks every old-parent identity and the complete binary child partitions, giving432138 final leaves with no gap, overlap of interiors or missing parent. Thirty worst or representative replacements are independently reassembled at640 bits and meet the target. Both analytic half-lines are reassembled from their exact certified error endpoints and also meet the target. Therefore

 m_4 >= 12501/10000 = 1.2501 on the full punctured plane.

The exact normalized original-data object and hashes are the ones in proof 160. The a=18/5 bound remains1.10534. For s=(a-18/5)/(2/5) in[0,1], affine dependence gives m_a>=(1-s)1.10534+s1.2501.

A first audit stopped because it required the640-bit interval lower endpoint to exceed the stored512-bit lower endpoint exactly. Such endpoint monotonicity is not required and is not guaranteed by two valid interval evaluations. The completed audit requires the claimed target, records the differing endpoints and verifies overlap with a separate640-bit evaluation of the production formula. This changes no production leaf or bound. The failed audit and the original proof are retained in evidence; the certificate binds the final proof and the complete audit. No injectivity of the full coupled operator follows.
