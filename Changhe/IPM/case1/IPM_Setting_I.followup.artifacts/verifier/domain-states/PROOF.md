# Independent audit of represented fields at different radial scales

Date: 2026-10-20. Status: verification protocol written before this computation. Numerical checks do not prove existence or convergence.

The inputs are exact byte snapshots of the numerics lane's completed stationary trials at L=4 and, when available, L=16. Their finite-dimensional solve residual is not identified with the physical transport residual. The reconstruction, paired whole-plane inverse and Cartesian eighth-order differences are this lane's independent implementations, described in ../inverse/PROOF.md. No numerics-lane evaluator or solver is imported.

Write R=(c_l X+U).grad rho-rho, E=-partial_x U_2+partial_y U_1-partial_x rho. We use the report's N_f=|rho|+sum_i|(c_l X_i+U_i)partial_i rho| and N_v=|rho|+|X.grad rho|+|U.grad rho|. The elliptic denominator is |partial_x rho|+|partial_x U_2|+|partial_y U_1|. The code in this topic explicitly names these denominators, avoiding an older helper's reversed diagnostic labels.

Evaluate two prescribed radius10 points, two points near the expected source, two far points and points at the actual canonical axis zero. Locate that zero independently by solving c_l x+U_1(x,0)=0. A bounded scan supplies a bracket if necessary. Refine angular quadrature from2048 to4096 and radial Gaussian order24 to28, log-panel width0.1 to0.08. Store the signed velocity and gradient differences, rather than treating differences between absolute residuals as error bounds. Compute the source Jacobian and E near its independently located zero by eighth-order Cartesian differences; two steps test differentiation sensitivity. These are numerical diagnostics. Neither finite sampling nor successive quadrature agreement certifies the entire continuum residual.

Density parity is exact from its representation. It gives the canonical velocity parities and U(0)=0 through the paired inverse. An exactly unit first radial node row gives rho=x^2 y+o(r^3), which preserves cubic normalization but does not prove smoothness of the factor. The independent exact binary-data interval calculation in ../center-regularity/PROOF.md tests necessary center compatibility of the represented density. A nonzero forbidden degree-five angular coefficient rules out its smooth factor; the nonzero transport balance determinant rules out exact transport of that fixed field. This says nothing about smooth limits of changing representations.

For an independent identity check, evaluate the origin moment c=integral_0^infinity rho_3(r)/r^2 dr, where rho_3 is the physical third sine coefficient. The defect is 3c_l-1-c. The canonical inverse fixes the harmonic gauge; a linear strain added to remove this defect changes the required velocity law.

The exterior estimate is adjusted to L, rather than using the earlier L=8 constant. Suppose L>=1, 0<1/c_l<1/5. Let B0 be the integer ceiling of the largest absolute nodal value and H the least integer with H^2>=2N(2M-1). Tensor discrete orthogonality gives |b|<=HB0. For r>=1,

    |rho|<=r^3(1+r^2/L^2)^((1/c_l-3)/2)HB0
          <=L^(3-1/c_l)HB0 r^(1/c_l)<=L^3HB0 r^(1/5).

This is because the exponent of the parenthesis is negative and 1+r^2/L^2>=r^2/L^2. Thus C=L^3HB0 is a valid exact bound for integer L. Oddness under central inversion gives, for R>|X|, the absolute omitted velocity bound

    (5C/2)|X| R^(-4/5)/(1-|X|^2/R^2)^2.

It follows by integrating the absolutely bounded paired harmonic series, as proved in ../exterior-tail/PROOF.md. At R=10^30 replace |X| by an integer upper bound to retain rational constants. The corresponding omitted strain bound is 5C/(2*10^24). These bound the infinite exterior of the represented field only. They do not enclose floating-point arithmetic, the unresolved disk at the origin, or interior quadrature.

Dependencies are the standalone inverse, center-regularity and exterior-tail arguments. Evidence will record source hashes, quadrature parameters, signed differences and exact interval conclusions. Domain comparisons concern distinct computed fields and do not themselves establish a branch, a continuum kernel, three-domain convergence or either endpoint.

## Common58point domain comparison

To compare radial-scale trials without selecting favorable sample points, use exactly the58physical points prescribed for the independent soft-action study, in ../sampled-physical-actions/verification/points.json. These are additional to the separately located source checks above. Evaluate all points with4096angles, radial Gaussian order28 and panel width0.08. Refine eighth-order Cartesian density steps from1/8000 to1/16000 to1/32000 times max(1,|x|,|y|). A second differentiation method uses the exact polynomial chain rule: with D=L^2+x^2+y^2, ell=log(D/L^2), q=1-exp(-(1-k)ell/2), c=cos(2s), theta=s+beta sin(2s)/2 and theta=atan2(y,x),

    q_j=(1-k)(1-q)X_j/D,
    c_theta=-2sin(2s)/(1+beta cos(2s)),
    theta_x=-y/r^2, theta_y=x/r^2,
    rho_j=x^2 y exp((k-3)ell/2)
      *[(d_j log(x^2 y)+(k-3)X_j/D)b+b_q q_j+b_c c_theta theta_j].

Here d_x log(x^2 y)=2/x and d_y log(x^2 y)=1/y, and all sample points lie in the first quadrant. Polynomial derivatives b_q,b_c are evaluated by independently differentiated Chebyshev coefficients. This formula follows by the ordinary chain rule from the explicitly defined interpolant. Compare the resulting signed transport residual with the finest Cartesian result using its fixed denominator. Observed derivative differences remain numerical checks, not interval error enclosures. Neither the finite maximum nor a comparison with a different L is a uniform residual certificate or a convergence theorem.
