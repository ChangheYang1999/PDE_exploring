# Two newer c=2 hydrostatic trial states, with independently refined inverse quadrature

Result219. Written before the audit code on 2026-10-21T12:40:14.094409+00:00. The inputs are hsE_c2.0_N128_hr_cont and hsE_c2.0_N160_hr, frozen in result217 and copied with matching hashes here. They are auxiliary hydrostatic trial states, not full elliptic IPM candidates. The first is the continuation past the earlier40-step cap. This audit makes no assumption of convergence, a solution, or equal optimization budgets.

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


## New verification protocol

First repeat the unchanged independent density/center audit on these two frozen inputs. The earlier ten-state audit206 contained the capped N128 state, not this continuation or N160. Then re-evaluate every one of its774 independent physical points under two higher full-tail quadratures: finite order40/infinite order320/split factor512, and finite order64/infinite order512/split factor2048. The inner scale remains0.125; all integrals include the core through fixed physical cuts and the complete infinite tail. Refinement does not impose a finite-box boundary condition.

Re-evaluate each distinct maximizing point of the most refined regional table at order88/tail768/split4096. Record pointwise velocity, absolute residual, both positive denominators, both normalized residuals, signed changes and maximizing locations. A zero denominator is undefined, never floored. The original baseline table is retained even if its digits are unstable. A change of the maximizing location under refinement must not be confused with convergence at a fixed point: report the maximum pointwise change over the entire common grid separately.

All formulas, the elementary finite-radius identity, and the limitations proved above apply unchanged. In addition to exact center values, selected70/100-digit scalar derivatives validate the analytic Cartesian derivatives independently. These are numerical checks, not interval enclosures. The common grid spans radii from1e-5 to1e4 and includes extents10,100,10000, exact axes and near-axis angles. They do not cover the whole plane and cannot certify a uniform residual bound.

Dependencies: [independent evaluator](../independent_hydrostatic_evaluator/PROOF.md), [first finite-state audit](../hydrostatic_state_audit/PROOF.md), [extended audit](../hydrostatic_extended_state_audit/PROOF.md), and the hash-frozen states of [core moments](../hydrostatic_axis_core_moment/PROOF.md). The transport coefficient and center slope are invariants of the residual isotropic scaling; no normalization sets either to1. A hydrostatic finite trial cannot meet the primary SettingIII endpoint regardless of its residual size.

## Additional power-tail comparison (2026-10-21T12:45:14.410647+00:00)

Result221 independently proves and manufactures the exact substitutiont=R/u^P, P=1/(1-p), for the same complete infinite tail. Its checked implementation is an additional evaluation method, not a modified density or inverse gauge. Once its manufactured gate passes, evaluate the same774 points at finite/tail/split settings40/128/32 and64/192/128 with this substitution, after retaining both higher linear-tail tables above. Label method switches separately from same-method order refinement. Re-evaluate the union of all regional maximizing points at power setting88/256/512. Keep the original linear-tail88/768/4096 witnesses as well, since their difference exposes a systematic quadrature effect. Compare each numerical center with the exact rational center independently. This is a stronger evaluation of the frozen states, not evidence of convergence of the producer solver. Dependency: [power-tail proof and manufactures](../hydrostatic_power_tail_inverse/PROOF.md).
