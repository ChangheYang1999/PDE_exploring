# Lead review of the verifier's low-multipole flux identities

Written 2026-10-29T00:12:40Z (date -u). Reviewed file: RUN_ROOT/verifier/research/low_multipole_flux/PROOF.md (sha256 05a0dbd2d07378fdbb6a81c10fa98b382e28aaa2734fd3649ab0d06196d8d9a5).

Verdict: CORRECT as continuous identities. Not adoptable in production under specification 2.6 on the present evidence;
recommended as a diagnostic.

Checked steps.
1. With div U = 0: d_i a_i = (d_i U_j)(d_j U_i) + U_j d_j (div U) = f, and a_i = d_j (U_i U_j). Checked.
2. int_(B_r) H f dy = int_0^r s^(l+2) F_lm(s) ds for H = conj(H_lm) = s^l conj(Y_lm): checked.
3. Two integrations by parts: int H d_i a_i = int_(dB) H a . n - int (d_i H) a_i, and
   - int (d_i H) d_j (U_i U_j) = - int_(dB) (grad H . U)(U . n) + int (d_i d_j H) U_i U_j; surface element r^2 dOmega.
   Checked. l = 0: grad H = 0; l = 1: conj(H_1m)(r n) = r conj(Y_1m(n)), grad conj(H_1m) = conj(d_m), Hessians vanish.
   Both special cases checked.
4. Green form: P_lm and P'_lm as displayed; in P'_lm the terms r^(-l-1) I' + r^l J' = r F - r F cancel. Checked.
5. Decay: |a| <= |U| |DU| <= C^2 (1 + r)^(-2 alpha - 1), so I_00 = O(r^(1 - 2 alpha)), I_1m = O(r^(2 - 2 alpha)); both
   tend to 0 for alpha > 1, which holds for every c_l in (0.4, 0.5) (alpha in (1, 1.5)). Newton potential of f converges
   for alpha > 1/2. Checked. Parameter derivatives under the stated joint continuity on the compact ball: checked.

Adoption (lead decision, consistent with specification 2.6, v1.8).
(a) At a far-anchor radius the flux value is, up to rounding, the exact-field I_lm(r), whereas production computes
    I_lm(r) by volume quadrature of the discretized source. Their difference is the discretization error of the
    discrete low moments: for l = 0, 3e-13 to 5e-12 of the absolute integral on the saved states; for l = 1 about
    1.7e-10 on the V027 field. Replacing the volume value by the flux value at the anchors therefore removes a
    discretization-level quantity, which specification 2.6 does not allow (its condition is a rounding-level difference,
    1e-13 of the absolute integral, and that condition failed for l = 0 on the saved states). The exterior-monopole
    regression (far rows up to 1.3e-9 relative) indicates the size of the change; R1's invariance limits would fail.
(b) It would also evaluate the anchor rows of l <= 1 with a different discretization from all other rows (including
    the far rows beyond 2^8 R0), so the pressure field would not be one discretization of one Newton potential.
(c) Diagnostic use, recommended: at the anchor radii and at a few far-row radii, compute I_00 and I_1m by the flux
    formula from the production U and a, and compare with the production volume values. This measures the low-moment
    discretization error (deliverable D) and, since the flux values involve no accumulation over the ball, their
    second differences along columns 183, 187, 188 separate volume-accumulated noise from noise of the boundary
    fields, which is what R3 step 1 needs. The discrete divergence of U at those radii should be recorded, since the
    identity uses div U = 0.
