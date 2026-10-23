# Audit protocol for the N36 M32 smooth refinement

Date: 2026-10-21. This result concerns a saved finite approximation, not a nearby exact solution or a convergence theorem.

## Formula, domain and dependencies

The density is the independently constructed smooth basis of ../smooth_representation/PROOF.md, with fixed ell=5/2, radial exponent stored as the binary float 0.4, length L=1 and 36 radial degrees, 32 angular terms. It is evaluated on the full plane. The solver selects a finite density formula; all checks reconstruct that formula from its coefficients. The canonical inverse and its uniqueness are in ../inverse/PROOF.md. The independent density-moment inverse used in the current solve is justified in ../smooth_density_moment_inverse/PROOF.md. Cartesian kernel integration, finite differences, complementary angular integrals and exact/MP finite primitives provide separate numerical checks. A prescribed quadratic stream or a finite-box boundary condition is not introduced.

The exact center jets follow ../smooth_canonical_high_jets/PROOF.md. For an exact nondegenerate profile, differentiating transport at zero gives a(ell+c-1)=0. A nonzero exact rational value of this expression for the saved binary coefficients proves only that the finite formula is not an exact profile. It does not quantify proximity to a profile. High derivative residuals and changes in slope across increasing finite systems are relevant observations but cannot by themselves exclude convergence in a weaker norm or prove blow-up of a limiting derivative.

## Comparing independent inverse and derivative evaluations

Let rho, g=grad rho and U be the MP evaluation of a frozen finite formula. Let rhat, ghat and Uhat be an independent numerical evaluation at the same physical point. Write dU=Uhat-U, dg=ghat-g and dr=rhat-rho. For the transport residual, direct expansion gives the exact algebraic identity

    Rhat-R = dU dot g + (ell X+Uhat) dot dg - dr.

This identity separates the effects of velocity, derivatives and density evaluation. Agreement among finite-difference step sizes alone does not establish accurate velocity. In particular, the true odd U2 may be of size y while signed quadrature terms are much larger, so relative cancellation error can dominate a near-horizontal-axis residual.

To check that issue, use the parity interpolation of ../parity_inverse_verification/PROOF.md on the smooth scalar reconstruction. At fixed x>0, g_x(z)=U2(x,sqrt(z))/sqrt(z) is smooth down to z=0. Cubic Lagrange interpolation at z=h^2 times (1,1/4,1/16,1/64) has error bounded by the supremum of the fourth derivative of g_x, times the nodal product divided by 24. The implementation estimates the quotient with direct whole-plane kernel samples at both positive and negative ordinates, then multiplies by the target y. It does not use a prescribed center strain or the comparison MP velocity. Samples at several h and two inverse quadratures are compared with the independent MP primitive only afterwards. The previously manufactured parity gate applies because its hypotheses are smoothness, parity and the canonical inverse, not the choice of density basis. No derivative bound or quadrature enclosure is asserted from this comparison.

## Limits of the finite experiment

The actual stored exponent is retained. At infinity its exact leading transport multiplier ell*p_saved-1 is not replaced by zero merely because decimal 0.4 equals 2/5. Numerical wide grids and selected MP points do not certify a uniform residual bound or all three domain/resolution requirements in the task. A small residual and exact-gauge constraints within roundoff do not imply convergence, stationarity, absence of trivial limits, or a nearby-solution theorem. Each verdict must distinguish these issues.
