# Independent floor1 review

Date: 2026-10-23T07:22:03.609291+00:00. Source archive SHA256 f4c73485061e3f4be55ce3be51d7636b90b0feecd42d3e0890bf2736aed9c43d. The full report was read, including the fixed-ball variant, determinant separation, forced identities and grid certificate. Lead section 8 uses only the global compactness corollary, simplified by the independently checked L2.

| Check | Method and result | Verdict |
|---|---|---|
| Global compactness floor | C2 local limit, fixed tail localization of curvature norm, curl-free pressure reconstruction, exact obstruction. The explicit proof is research/compact-residual-floor/PROOF.md. | CONFIRMED |
| No pressure bound | Test curl against compactly supported fields; reconstruct a global C2 pressure from the limit C1 force. | CONFIRMED |
| Fixed D2 modulus | The shrinking-core example preserves D2 norm and all weighted bounds through order two while residual is O(ell^2); common D2 continuity fails. | CONFIRMED |
| Approximate incompressibility | A joint vanishing residual and divergence defect gives an exactly divergence-free compact limit. | CONFIRMED |
| Legacy stagnation margin | C1 convergence preserves abs(V)+abs(det DV)>=delta; all zeros are isolated in a fixed compact ball, hence finite. L2 renders this condition unnecessary in the global corollary. | CONFIRMED |
| Fixed-ball L2 variant | Backward trapping gives vorticity zero locally under the legacy margin. For the harmonic limit, the ball Poisson Hessian identity has coefficient 15. Choosing radius sqrt(30K) bounds its curvature by 1/2, contradicting retained unit curvature. The chosen outer radius contains every required ball. | CONFIRMED |
| Determinant and zero separation | abs(det A)>=delta with operator norm A<=M bounds the least singular value by delta/M^2; a common derivative Lipschitz bound gives a positive zero-separation radius. A bound only at each approximate zero is not closed under limits, as the report's local example shows. | CONFIRMED |
| Forced Bernoulli and curl identities | R_m=kappa V+Omega cross V+grad H and curl R_m=R_omega+(div U)Omega agree with the separately derived identities. Variation of constants adds the transported curl-residual source. | CONFIRMED |
| Grid margin | The determinant differential satisfies abs(D det(A)[B])<=3 M^2 abs(B) in the stated bounds, so Lip(abs(V)+abs(det DV))<=M+3M^2L. The net certificate is valid only with certified pointwise and derivative bounds. | CONFIRMED |
| Explicit numerical floor | Neither compactness nor the dynamical inequalities supply a numerical epsilon_0. No computable screening threshold has been proved. | OPEN |
| Model review provenance | floor1's separate Opus call failed. Actual Opus lead review is supplied by THEORY_NOTES v3 and the lead's 07:19 reply, independently checked in THEORY_V3_AUDIT.md. | CONFIRMED |

A merely decreasing relative training loss is outside the corollary's conclusion. No present checkpoint has certified global membership in the stated compact class.
