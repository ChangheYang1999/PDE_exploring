# Whole-plane residual norms for source013

Written 2026-11-03T17:51:45.017309Z after all six finite stages completed. The independent actual-output review is pending.

## Exact statement and hypotheses

Fix c = 4076476460239181/2251799813685248, authoritative Candidate007 with exact input hash ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21, and correction013 with canonical input hash 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33. Let psi = partial_y chi_007 + phi_013, rho = -Delta psi, u = (-psi_xy,psi_xx), F = (cX+u).grad rho-rho, W(X) = sqrt(1+4|X|^2), and g = WF. Use the unitary Fourier transform and the inhomogeneous Sobolev norm

    N_s(g)^2 = integral (1+|xi|^2)^s |g_hat(xi)|^2 dxi.

Assume the accepted source identities, containing primary arithmetic, complete analytic remainders and actual independently reviewed regional certificates listed in ../../PROOF.md and the exact finite request retained in verification/bindings_v01.json. Then g belongs to H^3 and has these containing integer-norm intervals:

| m | Lower N_m(g) | Upper N_m(g) |
|---|---:|---:|
| 0 | 0.0013532483424295800722 | 0.0013532915780295398223 |
| 1 | 0.0013570907686964908636 | 0.0219038413730882314394 |
| 2 | 0.0034386898906426931721 | 0.0311161442531531477532 |
| 3 | 0.3653713152531953519335 | 0.3673303126562534250846 |

The complete P-S1 fractional norm satisfies

    0.0034386898906426931721 <= N_(21/10)(g) <= 0.0398284014018200711806.

The unweighted residual satisfies

    0.0000007959400186993612 <= ||F||_2 <= 0.0000007961206656880281.

Every decimal here is rounded outward by an exact rational comparison. These are full-plane norms of this fixed source, not sampled diagnostics.

## Complete argument

For j = 0,1,2,3 let [L_j,U_j] be the sum of the containing integrals of the full ordered Cartesian tensor |D^j g|^2 over the origin disk r <= 1/50, all 114 annular panels 1/50 <= r <= 10000, and the infinite exterior r >= 10000. The six annulus blocks and both endpoint regions have actual independently reviewed source identities and complete analytic remainders. Their overlaps are null circles, so addition of their exact endpoints contains the whole-plane energies. Smoothness identifies the classical derivatives with the weak derivatives. Their square integrability proves g in H^3.

Parseval and the binomial theorem give N_m(g)^2 = sum_(j=0)^m binom(m,j) integral |D^j g|^2. Thus E_m^- = sum binom(m,j)L_j and E_m^+ = sum binom(m,j)U_j contain its square. Both containing computations verify the square-root endpoints by exact squaring. The publication script independently checks all four binomial sums and squares.

Holder interpolation gives N_(21/10)(g) <= ((E_2^+)^9 E_3^+)^(1/20). Monotonicity gives the lower sqrt(E_2^-). Interpolating order 2 between orders 1 and 21/10 gives the additional lower ((E_2^-)^11/E_1^+)^(1/20). Taking the larger lower proves the fractional interval. Its endpoints satisfy the exact twentieth-power inequalities, checked in both numerical routes and again here. No interpolation equality or unresolved inverse constant is assumed.

For the unweighted norm, divide the analytic weighted zeroth radial integrand by 1+4r^2 on each annular panel. Its strictly positive complex-disk denominator lower bound gives an analytic quotient with a complete Cauchy remainder. One route integrates the exact rational reciprocal coefficients, selecting each original coefficient endpoint according to the exact sign of its integration weight. The independent route encloses the formal reciprocal by truncated Newton iteration at higher precision. Both include every Taylor-tail allowance, so their nonempty interval intersection contains the same panel integral. The exact source and all 114 panel identities are rechecked; no local interval is reused for a different panel.

On the origin disk, 1 <= W^2 <= 1+4/2500 gives the lower weighted energy divided by 1+4/2500 and the original weighted upper. On the infinite exterior W^2 >= 1+4*10000^2 gives upper weighted energy divided by that constant and lower zero. Summing these bounds and all quotient-panel intervals contains integral |F|^2. Exact squaring and outward decimal comparisons prove its displayed norm interval.

## Evidence, execution and scope

Weighted result ../../verification/weighted_publication_v01/result.json: SHA256 d6b2bfb13133379714602d6db6803f129ee82cdda980e6a00038be8711fb466f; unweighted result ../../verification/unweighted_publication_v01/result.json: SHA256 92cb0e5f48f470a76c723bd42355763211813031895f415c245fc8b5a9707c77. Each retains its separate primary and independent reduction records and every regional dependency. The six-stage execution ran 2026-11-03T17:49:42.359820Z to 2026-11-03T17:51:35.331365Z, elapsed 112.97152602858841 seconds, six zero exits, no stop reason and no old-process signals. Receipt SHA256 215e8d17e293f498753f05424c66f0318e488fb7aa597131db6b9407189c9734. Local verification/bindings_v01.json contains exact source, result, request, receipt, proof and display bindings. No Lean formalization or build is claimed.

This conditional result awaits independent actual-output review. It covers P-S1 and unweighted L2 only; P-S2 and the strong Holder norm S_F are different quantities. It supplies no background gap, near or far coefficient bound, full inverse, invariant-ball closure or stationary existence theorem. No closure ratio can be computed without the missing same-source hypotheses.
