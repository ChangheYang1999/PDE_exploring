# A common physical sampling audit of the two numerical soft spaces

Date: 2026-10-20. Status: derivation and evaluation protocol written before computation. Numerical outcomes pending. No continuum spectral theorem is claimed.

## Statement being checked

The numerics lane supplies two finite arrays of measured orbit-map actions, at96x40 and120x48 solved nodal states. The10softest right Ritz vectors of each array are algebraically defined by SVD, using the unit nodal coordinate norm including c_l and the auxiliary scalar C. This audit checks their actual physical transport derivatives at a common set of explicitly saved points. It uses independently reconstructed density coefficients, Cartesian finite differences and our independently implemented full-plane real-space inverse. It does not execute the numerics residual, trajectory integration or differentiation code.

The underlying finite density, canonical inverse and exact parameter derivative are defined in ../ritz-resolution/PROOF.md and ../linearized-check/PROOF.md. In detail,

    rho=x^2 y P_k(r)b(q,s), P_k=(1+r^2/L^2)^((k-3)/2),
    q=1-(1+r^2/L^2)^(-(1-k)/2), k=1/c_l,
    theta=s+(beta/2)sin(2s).

For a nodal variation delta b_nodes and delta c_l, let delta b_interp denote the polynomial interpolant of the varied nodes at fixed q. At a fixed physical point,

    delta k=-delta c_l/c_l^2,
    delta q=-(1-q)log(1+r^2/L^2)delta k/2,
    delta rho=x^2 y P_k[delta b_interp
                  +(log(1+r^2/L^2)/2)b delta k+b_q delta q]. (1)

The auxiliary scalar C has no direct term in this physical formula. The velocity variation is the same canonical full-plane inverse applied to delta rho. Linearity follows by the paired kernel integral and its uniform integrable tail, proved in ../exterior-tail/PROOF.md. With R=(c_l X+U).grad rho-rho, the exact numerator derivative is

    delta R=delta c_l X.grad rho+(c_l X+U).grad delta rho
                              +delta U.grad rho-delta rho. (2)

All normalizers in the sampled action matrix are held at the base state:

    N_f=|rho|+|W_1 rho_x|+|W_2 rho_y|,
    A_ij=delta_j R(X_i)/N_f(X_i).

Thus A is not the derivative of the quotient R/N_f. The actual N_f values are stored and must be positive for this definition. The direction norm is initially the unscaled nodal norm and is explicitly grid dependent. Four independently chosen smooth nodal calibration directions, normalized and orthogonalized to the ten Ritz vectors, supplement that space. They are references for the sampled magnitude, not candidate kernel directions.

## Common sampling and physical metric

The prescribed points cover eight finite radii and six angles, four additional near-source points, and six far-field points. They are fixed in verification/points.json before evaluating either field. No point is selected to maximize apparent softness. The near-source points test the represented finite fields at the published source location; they do not assume the exact stagnation point is8.6. This finite sampling is not a supremum or an integral enclosure.

Alongside A, store the pointwise physical density variations and their independently differenced gradients. A secondary finite metric on a direction is

    ||delta||_P^2 = mean_i |delta rho(X_i)/(1+|rho(X_i)|)|^2
                             +|delta c_l|^2.

The base state in this denominator is specified separately for each grid. Hence it is a comparable physical sampling protocol, not literally the same infinite-dimensional norm or an exact common Hilbert space. Its Gram matrix is computed from the saved variations. If that Gram matrix is positive definite and sufficiently conditioned, singular values of A/sqrt(number_of_points) after whitening this metric can be reported. If it is not, the metric degeneracy must be stated and no inverse square root inferred.

The raw node-unit actions, per-point maxima and finite metric matrices are independently reproducible from the stored data. A small sampled singular value means a cancellation at this sampling resolution. It does not prove an exact PDE kernel, a family, isolation, or convergence of a continuum operator. In particular, the counterexample in ../crossgrid-actions/PROOF.md applies to inferences based only on soft-vector agreement and dense-core consistency.

## Error controls and admissibility limits

Each action is computed with two spatial finite-difference steps; the discrepancy is stored separately from inverse quadrature error. The initial pass uses2048angles, radial Gauss order24 and logarithmic panel size0.1. A subsequent independent refinement of selected points is permitted only to investigate an unresolved quadrature error or a proposed smallest-action conclusion. The outer truncation radius is10^30. Exact rational envelopes for rho and delta rho give point-specific outer velocity bounds using an integer observer radius that contains the actual binary point. Their conversion to a residual error uses numerical gradients and is labelled accordingly. Interior floating-point quadrature is not interval certified.

The exact nodal densities retain all previously proved center incompatibilities. No small sampled action repairs those defects, and no conclusion about a smooth limit follows from finite-state behavior. This audit addresses TASK question1 only as additional numerical evidence under a separately implemented physical evaluator.

Dependencies: the exact nodal definition and parameter differentiation in ../linearized-check/PROOF.md; own inverse and manufactured tests in ../inverse/PROOF.md; exact omitted-tail bounds in ../exterior-tail/PROOF.md; finite-array SVD audit in ../ritz-resolution/PROOF.md. No formal builds are authorized.

## Full refinement before a sampled singular-value claim

Added2026-10-20 before the refinement pass. The first96state has a well-conditioned finite metric on the prescribed14columns (QR condition about365), and small singular values after the physical metric is imposed. Their numerical stability requires a comparison of the whole finite action matrix, because a pointwise refinement on a few rows cannot bound the matrix difference. Therefore all58prescribed points of both states will be refined to4096inverse angles with the same radial rule. This is a resolution check prompted by the proposed smallest sampled singular values, not a new sampling choice. The matrices remain finite observations; neither a continuum operator error nor a rigorous quadrature enclosure is inferred.

For stable whitening, factor M=QT by thin QR, where M has the density-sampling rows and one delta-c_l row defined above. Then A T^(-1) has the stated physical domain norm. Use a linear solve instead of explicitly forming the inverse. Report the singular values of M and its condition number; reject whitening if the smallest singular value is less than10^(-10) times the largest. This threshold is a numerical safeguard, not a mathematical rank certificate. The Frobenius norm of the difference of the two whitened sampled matrices bounds the difference of their singular values as finite computed matrices, up to floating-point arithmetic. It is only a refinement discrepancy, not a bound on all remaining quadrature error. The analogous spatial-step discrepancy and the explicitly bounded exterior term are reported separately.

A common sampled overlap uses the column spaces of M_96 and M_120 in the same59-dimensional coordinate space. Their different base density denominators are retained explicitly. These cosines measure agreement under that common sampling protocol, not convergence in a prescribed continuum function space.

## Spatial refinement prompted by the broad sampling

Added2026-10-20 before further derivative computation. The two original Cartesian steps disagree primarily at point5, near the vertical axis at radius0.2. That discrepancy is material after whitening the physical metric, especially at120. It prevents accepting the initial smallest sampled singular values with the previously available step comparison. The full inverse refinement remains necessary but does not resolve this separate derivative issue.

Keep all points and directions fixed. Compute the base density and its14density variations at Cartesian eighth-order steps1/4000,1/8000,1/16000and1/32000times max(1,|x|,|y|), and save the signed gradients at every point. Use the same independently derived density formulas and the saved velocity arrays; no new velocity solve is needed. For a fixed chosen base normalizer, the difference of two resulting action matrices is exactly the difference obtained by substituting these gradients into equation(2), up to floating-point arithmetic. Its whitened Frobenius norm is a finite step discrepancy. It is not a certified bound on all differentiation error.

A vectorized evaluation of the14density variations is algebraically identical to equation(1): evaluate their separate tensor polynomial coefficients by the two-variable Chebyshev recurrence, and add the base polynomial and its q derivative with each delta-c_l coefficient. Comparison with separately called scalar density variations at the same points detects array-order mistakes. This improves computation efficiency without reusing another lane's residual or inverse code. Point selection and domain metric are unchanged. The refined denominator at a state is held fixed when comparing its four gradient steps, so no derivative of that denominator is introduced.

For the recombination, use the signed gradients at step1/32000 as the chosen base and compare all larger saved steps against it, keeping its N_f fixed. At each inverse resolution save the resulting signed matrices and compute their differences by a direct triangular solve with the same T. This avoids replacing an actual signed difference by an unnecessarily large entrywise absolute bound. Once the4096inverse is complete, use its base N_f for both inverse resolutions, so their matrix difference isolates the inverse change with the chosen gradients. In both cases this is a difference between finite computed matrices, not an enclosure of the unknown derivative or inverse. Exterior-tail bounds remain entrywise absolute estimates and are propagated through |T^(-1)|, with their use of numerical gradients explicit.

## Independent chain-rule check of the Cartesian differences

Written before this additional computation. The finite polynomial representation permits a derivative check that uses no spatial finite difference. All prescribed points have x,y>0. Write D=L^2+x^2+y^2, ell=log(D/L^2), theta=atan2(y,x), c=cos(2s), where theta=s+(beta/2)sin(2s). Then

    ell_x=2x/D, ell_y=2y/D,
    q_x=(1-k)(1-q)x/D, q_y=(1-k)(1-q)y/D,
    c_theta=-2sin(2s)/(1+beta cos(2s)),
    theta_x=-y/(x^2+y^2), theta_y=x/(x^2+y^2).

Let P=x^2 y exp((k-3)ell/2), B=b-(1-q)b_q, and let d denote the fixed-q nodal interpolant of the variation. The varied density is P F with

    F=d+delta k ell B/2,
    F_q=d_q+delta k ell [2b_q-(1-q)b_qq]/2,
    F_c=d_c+delta k ell [b_c-(1-q)b_qc]/2,
    F_ell=delta k B/2.

Here q,c,ell are independent arguments for these partial derivatives. At a fixed physical point, the exact chain rule gives

    (delta rho)_x=P[(2/x+(k-3)x/D)F+F_q q_x+F_c c_x+F_ell ell_x],
    (delta rho)_y=P[(1/y+(k-3)y/D)F+F_q q_y+F_c c_y+F_ell ell_y].

The base formula has F=b, F_q=b_q, F_c=b_c, F_ell=0. Polynomial derivatives are evaluated by differentiated Chebyshev coefficients. Compare the resulting signed action matrix with that obtained from the finest Cartesian stencil, holding its denominator and metric fixed. This is an independent differentiation-method check on the same finite density, not a certificate of continuum approximation or floating-point roundoff.

## Cost of changing c_l within a sampled finite span

This further finite diagnostic uses only the saved matrix A/sqrt(number_of_points), denoted A_0, and the functional l=(delta_j c_l)_j. On a specified d-column span assume A_0 has full column rank and l is nonzero. Thin QR gives A_0=Q R. For every coefficient vector v,

    |l.v|=|(R^(-T)l).(Rv)|<=|R^(-T)l| |A_0v|.

Equality is attained at v=R^(-1)R^(-T)l/|R^(-T)l|^2. Thus the exact finite least cost with l.v=1 is alpha_c=1/|R^(-T)l|. This value is independent of coordinates in the fixed span. Linear solves with R avoid normal equations; the actual constraint and minimizing residual are checked. If R is numerically singular or l=0, no positive value is inferred. Increasing the span can only decrease the cost. A value computed on the specified span is an upper bound on the corresponding infimum over a larger space, not a lower stability bound for the PDE. Its units are the RMS of delta R/N_f per unit delta c_l. It is not comparable without qualification with an orbit-map residual norm. The minimizing direction and constraint are finite linearized data at an unconverged represented profile; they do not produce a nonlinear continuation curve.

## Independent radial quadrature refinement

After the full4096-angle pass completes, repeat the identical58points and14directions at4096angles with Gaussian radial order32 and log-panel width0.075. The angular rule, inverse partition, represented inputs, finite metric and refined Cartesian derivatives remain fixed. This separates a radial quadrature comparison from the angular2048to4096 comparison. Form both signed physical matrices using the same denominator and source QR within each comparison; the Frobenius norm of their difference bounds the operator norm of that numerical difference. Weyl's finite-matrix inequality bounds the corresponding singular-value change by that norm. Neither statement bounds an unknown quadrature remainder. The exact exterior bound is carried separately and is not combined with observed differences into a certified numerical error estimate. No continuum spectral conclusion follows.


## Radial refinement and bounded intermediate arrays

The finer radial rule uses 4096 angular samples, Gauss order32 and logarithmic panel width at most0.075. The partition, angular offset, inner cutoff and outer cutoff are unchanged. Its global and local finite sums may be evaluated in radial blocks. This replaces a sum over all radial indices by the sum of sums over a partition of those indices. In exact arithmetic the value is identical. The cached density values and each quadrature weight are unchanged. In floating arithmetic only the order of summation changes; a check against the existing evaluator at the same rule is recorded separately. Neither that agreement nor the radial difference is a certified quadrature remainder. Blocking avoids the simultaneous allocation of several arrays of the full radial-by-angular-by-direction size.
