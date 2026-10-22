# First review and explicit dependencies

The first authenticated Claude Opus 5.5 review completed with end_turn and confirmed the local join theorem under its stated hypotheses. It correctly left the finite derivative trace claim open until calculation. Both exact engines have now checked every stated trace. Its remaining questions are resolved or scoped as follows.

The stream convention is U=(-partial_y psi,partial_x psi) and -Delta psi=partial_x h. Fourier transformation gives psihat=i xi_1 hhat/|xi|^2 and the displayed velocity multiplier. For compact h supported away from the origin one may define psi by convolution with the differentiated two-dimensional Poisson kernel, up to an additive constant. Its local derivatives at the origin are smooth. In particular Sigma=partial_xy psi(0) is finite. The proof uses only that Sigma is a finite scalar, and does not depend on its sign or magnitude.

All background regularity is explicitly assumed. No new assertion that an arbitrary nondecaying density has a canonical velocity with the required regularity is used. When applying this theorem to a particular approximate or exact IPM profile, the background hypotheses must already have been established. The theorem does not use the global L2 multiplier to define U[rho] for such a density. It uses that multiplier only for the compact perturbation h. The incidental sentence in PROOF about backgrounds having the required local velocity regularity is to be read with this condition, not as a separate regularity theorem.

For multiple modes, take the finite union of their piece endpoints as the common interface set. Each originally smooth piece remains C2 after subdivision. This removes the implicit common-partition assumption in the angular argument. At a support interface, the exterior radial coefficient and its derivative are both zero.

Equation(5) is an exact algebraic identity for the stated piecewise affine scalar function. Its asymptotic divergence for fixed nonzero J follows by multiplication by d and taking d to zero. The connection to the existing numerical row grid remains a warning about possible interpretation, not a certificate that the grid crosses or detects any particular join.

The reviewer also queried topic132's radial norm factor because its original proof delegated the X definition. That issue had already been resolved in topic132's mandatory REVIEW_RESOLUTIONS and final adjudication. To check it here, use

    w=m^(-2)(1+r^2/L^2)^(-3/2),
    m=(r/L)^3(1+r^2/L^2)^((k-3)/2).

For h=r^3 B(log r) Phi, each term h^2 and r^2|grad h|^2 has the factor r^6, and polar area is r^2 dt dtheta. Hence

    r^8 w=L^6 r^2(1+r^2/L^2)^(3/2-k).

The exponents are 8-6=2 and (3-k)-3/2=3/2-k. This matches topic132's W. The new derivative-join conclusion needs only the exact affine repair, not that quantitative norm bound. All single-column ratios in topic132 are norm ratios, meaning square roots of energy integrals. No relative estimate on squared energy is being asserted here.

The local theorem and finite audit do not establish a bounded global H1 image, an actual retained subspace, a matrix perturbation, a certified singular value, a global inverse, a nonlinear remainder or a decisive IPM endpoint. These conclusions remain OPEN.
