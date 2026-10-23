# Canonical residuals on a shared finite sampling set

Written before the new evaluator on 2026-10-21 UTC. This is a finite numerical comparison protocol and an algebraic derivation of its measured quantities. It is not a theorem about a nearby exact profile.

## Definition and hypotheses

Take a frozen unforced Q density checkpoint, with N radial degree, M angular terms, ell>1, L>0 and map exponent kappa>1. Its coefficients define

    rho=y w sum_{k=0}^{M-1} sigma^k B_k(t) cos(2k theta),
    sigma=(1+t)/2, w=(1-t)/2,
    r=L sqrt((1+t)/2)/(1-t)^kappa.

The coefficient reconstruction and independent canonical inverse are proved in the earlier Q-reader, angular-Green and complementary-chart results. The density is smooth at zero, even in x and odd in y, and grows like r^{1-1/kappa}. The inverse is the full-plane parity-preserving sublinear solution. No finite physical box or adjustable harmonic strain enters it. We use the saved map exponent, and verify checkpoint and exported-data hashes before comparing.

The producer's regional grid is reproduced only as a set of physical locations. Its actual exported radial nodes t_i, i=0,...,N, are treated as finite decimal representations of binary floating-point numbers. The new radial set is the union of t_i for i>=1 and (t_i+t_{i+1})/2. Its image under the displayed map has 2N positive radii. Values r>=10^120 are excluded only when needed to match the original overflow guard. The base angular locations are theta_j=(j+1/2) pi/(2M), j=0,...,M-1. Include their consecutive midpoints and the five extra locations theta_0/4, theta_0/2, (theta_{M-1}+pi/2)/2, pi/2-(pi/2-theta_{M-1})/4, pi/2. Thus there are 2M+4 angular locations, no exact x-axis, and minimum angle pi/(16M). The physical grid has 2N(2M+4) points unless the radial guard removes some.

Only this sampling definition comes from the producer's diagnostic. No producer evaluator, differentiation routine, radial inverse, or optimization code is imported or executed. Reading its source to identify its finite domain is part of the audit. Arithmetic operation order may change the physical radii by floating-point rounding. The archived actual t_i and generated physical points make that difference explicit; no bit-exact coordinate identity is promised merely from matching formulas.

## Residual and normalizations

Let H=rho/r, H_r=rho_r, H_theta=rho_theta/r, v_r=U_r/r and v_theta=U_theta/r. Then

    g_x=H_r cos(theta)-H_theta sin(theta),
    g_y=H_r sin(theta)+H_theta cos(theta),
    u_x=U_1/r=v_r cos(theta)-v_theta sin(theta),
    u_y=U_2/r=v_r sin(theta)+v_theta cos(theta).

These identities follow from the polar-coordinate differentiation formula and the orthonormal polar frame. Therefore the exact physical residual R=(ell X+U).grad rho-rho obeys

    R/r=(ell cos(theta)+u_x)g_x
               +(ell sin(theta)+u_y)g_y-H.

The prompt's denominators divided by r are

    N_f/r=|(ell cos(theta)+u_x)g_x|
                 +|(ell sin(theta)+u_y)g_y|+|H|,
    N_v/r=|H|+|cos(theta)g_x+sin(theta)g_y|
                 +|u_x g_x+u_y g_y|.

The canonical implementation uses a defect chart near zero to avoid subtracting the exact linear density and strain numerically, and the full chart farther out. Adding the unforced center defect a(ell+c-1)sin(theta) to the defect residual recovers the same R/r. This follows by expanding rho=a y+h and U=(-c x,c y)+v. The normalizations always refer to the full original unforced equation. There is no fitted forcing term, denominator floor or removal of a small-denominator neighborhood.

## Finite comparison and obligations

For each inverse order, save maxima of |R|, |R|/N_f and |R|/N_v in the six producer radial bins and over the whole finite grid. Record the separate maximizing physical coordinates, raw R and both denominators. Record every nonpositive denominator and nonfinite value rather than filtering it silently. Compare radial quadrature orders on identical saved physical points. Recheck selected maxima with the independent multiprecision source-primitives inverse at two target precisions; finite-difference Cartesian checks are already available on the independent offset grids and may be extended to these points.

If the shared-grid canonical maxima differ from the producer table, this concerns a different inverse and differentiation of the same saved density, with explicitly recorded rounding in the shared sampling formulas. It must not be called a pointwise inverse error: differences of maxima can occur at different points. A pointwise inverse discrepancy requires evaluating both velocities at the same point, which is a separate comparison. The existing independently offset grid is still needed to show sample-set sensitivity.

Positive sampled denominators establish positivity only at these points. A shared grid leaves an origin neighborhood, near-axis wedges, radial/angular gaps and the far tail unsampled. Neither agreement of two inverse orders nor agreement with a producer table is a uniform error bound, an existence certificate or a limiting convergence result.
