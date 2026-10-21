# Five resolutions on one prescribed physical sample

Date: 2026-10-21. This protocol is written before the new aggregation program. It concerns exact arithmetic on saved binary components, not a proof of the PDE or of convergence.

## Statement and definitions

Let S be the58 ordered physical points in ../sampled-physical-actions/verification/points.json. For each frozen state with (N,M)=(72,30),(84,35),(96,40),(108,44),(120,48), use this verifier's previously completed whole-plane velocity values U_j and density/gradient samples rho_j,d_j at S. Preserve the state hashes. The72state is dnB, not the later dnC state. The120state is dnSB_n120m48.npz, retained from the previously audited branch, not a newly substituted dnB state. Explicit expected MD5 identities from prior audits are registered in verification/registration.json, with the post-original-computation registration timing stated. Interpret every saved binary scalar as its exact rational value. Let c_j be the saved parameter and set

    W_j=c_j X+U_j,
    R_j=W_j dot d_j-rho_j,
    F_j=|rho_j|+sum_i |W_(j,i)d_(j,i)|,
    V_j=|rho_j|+|X dot d_j|+|U_j dot d_j|.

V_j is the earlier published secondary diagnostic normalization. It omits c_j in the X dot d_j term and is not a triangle bound for the transport equation. The principal comparison uses F_j. Require all denominators to be positive. Compute maximum and RMS of |R_j|/F_j and |R_j|/V_j over S, plus the maximum of |R_j|/F_120. The shared denominator separates changes in residual from changes in normalization. Record exact residual/denominator fractions, pointwise inter-state changes, density and velocity differences, and all state/point/source hashes. RMS uses a final floating square root of an exactly accumulated rational average of squares. Maxima and comparisons are exact for these rational component formulas.

## Justification and limitations

Each formula uses only finite sums, products and absolute values of rational numbers. A finite set has an attained maximum, determined by exact rational comparison. The RMS squared is an exact finite rational sum divided by58. Replacing F_j by the same positive F_120 preserves pointwise comparisons across fields without changing the residual itself. The Cauchy or continuum limit is not implied by any of these finite identities: five terms do not determine an infinite sequence. An increase in the finite sequence does not preclude eventual convergence, and a decrease does not prove it.

For72,84,108 the whole-plane rule uses4096angles, radial order28 and logarithmic panel0.08. For96,120 the selected finer radial rule uses4096angles, radial order32 and panel0.075. Every rule has exterior cutoff10^30. Thus this is a common point set, not perfectly identical quadrature. Gradient values all use this lane's independent eighth-order centered Cartesian differences at relative step1/32000, namely h=(1/32000)max(1,|x|,|y|), with each completed experiment's analytic-gradient and step comparisons retained. The broad files and refined-gradient files use different storage schemas for the same field quantities; their provenance is recorded in verification/registration.json. Aggregation imports no numerical-lane code and does not recompute the physical inverse. Previously reported sensitivities and exterior estimates retain their scopes; the interior quadrature is not interval certified. L=8 is a compactification scale and is not a physical boundary.

The exact center exclusions for these fixed interpolants are established separately. They do not rule out a smooth limiting profile. This comparison cannot decide a continuum kernel, isolation, family, B_3/B_5/B_7 vanishing or either task endpoint.

## Dependencies and verification

Input studies: ../third-grid/PROOF.md, ../fourth-grid/PROOF.md, ../fifth-grid/PROOF.md and ../sampled-physical-actions/PROOF.md. Data source pins and exact finite row arithmetic are recorded under verification/. A110-digit Decimal reimplementation checks R,F,V and both normalized ratios on the same parsed binary components, with actual counters. It does not independently evaluate the inverse or control physical error. The rehash loop checks mutation during aggregation, while the explicit previously accepted state identities and inspected source files provide the separate provenance binding. The new code goes in code/. No formal proof assistant build is used.
