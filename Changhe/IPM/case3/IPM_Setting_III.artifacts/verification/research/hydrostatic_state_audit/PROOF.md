# 187. Independent audit of finite hydrostatic states

Written 2026-10-21 before the state computations. Verdicts will be attached to individual checks. These are finite inputs to the limiting hydrostatic operator, not candidates for original full-plane IPM. Coordinates are (x,y), the transport coefficient is ell>1, P>1 is the saved radial-map exponent and p=1-1/P is the actual density exponent. All saved binary coefficients and basis nodes are part of the reconstructed definition. An explicitly recorded constructor-node fallback is needed if the producer omitted those nodes.

## Definition, hypotheses and dependencies

For a finite Q polynomial density g=y w sum_k sigma^k beta_k(t)cos(2k theta), with r=L sqrt(sigma)/(2w)^P, use the independent Cartesian jet and vertical inverse of result185. That result proves its smoothness, parity, sublinear density/gradient/Hessian bounds, canonical hydrostatic inverse and gauge, and an exact all-angular-mode center functional. Its114 manufactured tests pass. The present code imports no producer evaluation, differentiation, solver or inverse module. The producer files are numeric inputs only. Direct scalar MP differentiation independently checks g_x,g_y,g_xx at selected physical points; full vertical integration uses physical composite Gauss-Legendre cells and a Gauss-Jacobi infinite tail, unlike the producer's barycentric differentiation, centered second difference and rational-power tail rule.

Write a=g_y(0), c_H=Phi_xy(0)=integral_0^infinity g_xx(0,t)dt and v(y)=ell y+V2(0,y). For every such density, whether or not it solves transport, v'(0)=ell+c_H. Hence its exact first-order transport defect is a(ell+c_H-1). This center condition is not inferred from a small fitted residual. The exact rational all-mode formula for c_H in result185 is used independently of the vertical quadrature.

## Finite-radius identity for arbitrary inputs

For every R>0 define

 D(R)=integral_0^R(1-t/R)g_xx(0,t)dt-(1-v(R)/R).

Then D(R)=ell+c_H-1, independently of R. Indeed the first term is integral_0^R g_xx-(1/R)integral_0^R t g_xx, and v(R)/R=ell+(1/R)integral_0^R t g_xx+integral_R^infinity g_xx. The middle terms cancel. All integrals converge by the bounds of result185. The equality does not use the transport equation. For an exact nondegenerate hydrostatic profile D=0. Any variation of a numerical D(R) with R diagnoses the evaluation error of this identity; it does not represent variation in the center condition itself. In particular a uniform trapezoid on (0,R] omitting [0,R/2000] is inaccurate for a fixed small core as R grows. Composite integration with fixed inner physical cuts and the exact center give independent comparisons.

## Parameter and center compatibility

Let the nonzero positive-axis tail be G(y)=K y^p(1+O(y^(-1/P))), which follows from the finite map and polynomials when its leading angular coefficient is nonzero. Then G'=pK y^(p-1)(1+O(y^(-1/P))) and V2(0,y)=O(y^p). Therefore

 R_H(0,y)=(ell p-1)K y^p+o(y^p),
 |R_H|/Nf -> |ell p-1|/(|ell p|+1),
 |R_H|/Nv -> |ell p-1|/(p+1).

Thus keeping P fixed and allowing only ell and polynomial coefficients to vary does not free the nonzero axis tail exponent: exact transport still requires ell=1/p. A near-unchanged ell in such a solve does not establish nonselection of ell. It records a fixed-exponent experiment. The center expansion g=a y+b x^2 y+e y^3+o(r^3), a nonzero, would also require b=6e/a for an exact hydrostatic solution whose center relation holds, since v=G/G'=y-2(e/a)y^3+o(y^3) and v''=-g_xx=-2by+o(y).

## Residual sampling and conditioning scope

The independently sampled quantities are R_H=(ell x+V1)g_x+(ell y+V2)g_y-g, Nf=|(ell x+V1)g_x|+|(ell y+V2)g_y|+|g| and Nv=|g|+|xg_x+yg_y|+|V1g_x+V2g_y|. Zero denominators on the horizontal symmetry axis are marked undefined, with absolute residuals still recorded. They are never replaced by an arbitrary floor. Independent physical grids include near-center points, exact axes, intervening radial/angular points and extents10,100,10000. The endpoint still requires far more than these finite samples. Selected maxima and probes are recomputed with changed finite/tail orders and split radii. MP checks apply to the reconstructed finite polynomial, not an unknown continuum solution. Discrepancies are numerical comparisons, not rigorous enclosures.

For a linear map between coefficient and sample Euclidean norms, rescaling a basis vector by epsilon rescales its matrix column by epsilon. Even the identity physical map in two differently scaled coordinate bases can have singular values1 and epsilon. Thus tiny coefficient singular values do not prove an intrinsic continuum near-nullspace or underdetermination. Quotienting an actual dilation tangent and choosing specified function norms is additional work. The frozen high-frequency Cauchy calculation of186 concerns an initial-value estimate, not nullity of a global collocation Jacobian. Also, a Jacobian with ell held fixed is not the Jacobian of a free-ell solve. These scope distinctions must accompany any producer conditioning table.

## Evidence plan and limitations

Freeze the producer numeric states and exact source snapshots used for the static audit. Record their hashes, actual P, nodes and any fallback, reconstruct stored beta values, compute exact center and MP cubic coefficients, run changed full-tail quadratures, and compare true transport residuals at independent points. Dynamic state reconstruction and the original full-plane inverse are already tested in results173,176,179 and180; those do not validate the present limiting equation automatically. The actual Opus5.5 lead is kept informed through the lane notes and its replies will be checked independently. No original YES/NO endpoint follows from this study.
