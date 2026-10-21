# Physical transport actions of nodal directions

Date: 2026-10-20. The differentiation formulas below are proved. Their application to the saved directions is numerical evidence, not a continuum spectral theorem.

## Statement and hypotheses

Fix L>0 and |beta|<1. Let c>1, k=1/c, ell=log(1+r^2/L^2), q=1-exp(-(1-k)ell/2), and let s(theta) invert theta=s+(beta/2)sin(2s). For a smooth finite tensor polynomial b(q,s), with b(0,s)=1 and the required reflection symmetries, define

    P(x,y)=x^2 y exp((k-3)ell/2),  rho=P b(q,s).

Take a direction (dot b, dot c) with dot b(0,s)=0. The coefficient values of dot b are specified on the same nodes, and L and beta are fixed. Then at each fixed physical point

    dot k=-dot c/c^2,
    dot rho=P [dot b +(ell/2) dot k (b-(1-q)b_q)].

Let T be the canonical full-plane velocity operator, U=T rho and dot U=T dot rho. Put W=cX+U and R=W.grad rho-rho. The physical transport derivative is

    dot R=dot c X.grad rho + W.grad(dot rho) + dot U.grad rho-dot rho.

The formulas apply to the finite represented field whether or not it is a stationary profile or has a smooth center. They give no derivative of an orbit-discretized residual map.

## Proof

At fixed X, the radial logarithm ell and angle s are independent of c. Differentiating q gives dot q=-(ell/2)(1-q)dot k, and differentiating P gives dot P=(ell/2)P dot k. The product rule proves the density formula. Spatial differentiation commutes with parameter differentiation at every point where the represented field has the required derivatives. The center normalization cancels the lower terms; in the present finite representations the resulting fields have at least the C^2 regularity needed for the paired kernel.

On a sufficiently small compact parameter interval around c>1, choose gamma strictly between the largest k on that interval and 1. Finite angular/radial polynomials and their parameter derivatives are bounded on the compactified domain. Differentiating the radial power contributes at most a logarithm. Thus the densities, their parameter derivatives and first spatial derivatives satisfy uniform growth bounds with exponent gamma. The centered-pair proof in ../inverse/PROOF.md then supplies an integrable majorant near zero and infinity, locally uniformly in the parameter. Differentiation under that integral is legitimate by dominated convergence. Linearity of T proves dot U=T dot rho. The remaining identity is the product rule applied to R.

The algebraic parameter C saved with a numerics-lane state is not an additional argument of this density reconstruction. It enters the orbit solver's equations. Its variation is included in the recorded nodal-vector norm, but only b and c determine the physical density and velocity above. Any comparison of physical actions must account for this distinction.

## Independent numerical implementation

The nodal direction is reconstructed by DCT coefficients, as is the base density. The q derivative of the base polynomial is computed by the exact Chebyshev recurrence for polynomial differentiation. A separate implementation evaluates the same density derivative in Cartesian coordinates on the CPU. Both agree within floating-point error at the tested points. The velocity action is computed by this lane's real-space full-plane inverse, and the spatial density derivatives use eighth-order centered Cartesian differences. No numerics-lane residual, inverse, orbit integrator, or derivative code is imported.

The input directions are data from ritz_n120m48_S.pt. That file stores the right vectors in descending singular-value order. The six directions used here are its last six columns, reversed, which agrees with the reported c variations. They are orthonormal in the saved physical Euclidean node coordinates. A seventh, independently constructed direction has dot b equal to the interpolant through nodal values proportional to q^2(1-q)cos(4theta), with dot c=dot C=0 and unit nodal norm. It is a calibration direction, not a random sample of all stiff directions.

The initially selected first six columns were caught by the c-variation assertion and a comparison with the JSON metadata before any result was accepted. Their output is explicitly named discarded_wrong_order and is not evidence for any conclusion in this report.

## Scope of the point-action measurements

The recorded dot R/Nv uses the fixed base denominator Nv=|rho|+sum_i|W_i partial_i rho|. Its columns are evaluated at a finite list of physical points. Their Euclidean singular values refer only to that sampled matrix and the stated input coordinates. They are not the singular values of the numerics lane's scaled orbit Jacobian, and they neither establish nor exclude a continuum kernel. In particular, a nonzero physical action of an interpolated discrete direction can reflect representation and equation errors as well as lack of a continuum null direction.

The initial 16-point evaluation gives maximum absolute dot R/Nv of about 1.74e-4, 2.55e-4, 8.72e-4, 3.09e-3, 2.79e-3 and 4.48e-3 for the six directions, versus 0.151 for the chosen calibration direction. Quadrature refinement and independent finite perturbations are required before treating the small actions as resolved. Even the resolved values would establish only these tested actions at the approximate base field. A nearby nonlinear family, an isolated solution and absence of a nearby solution all remain open.

Dependencies and evidence: ../inverse/PROOF.md; ../inverse/code/linearized.py, prepare_directions.py and density.py; ../inverse/verification/dnSB_directions.npz, parameter_derivative_check.json and dnSB_actions_2048.json. No formal proof-assistant build was run.
