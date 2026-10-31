# Finite-volume vorticity diagnostics

Status: exact integration formulas and finite-sample identities. They do not give a quadrature error bound or certify an Euler profile.

## Statement and notation

Let c and w be real numbers, J(x1,x2,x3)=(-x2,x1,0), and let U belong to C^2 on an open set containing the closure of a bounded measurable domain D in R^3. Write DU for the Cartesian Jacobian, Omega=curl U, and DOmega for its Jacobian. Define

    V1=Omega,
    V2=c DOmega y,
    V3=w (J Omega-DOmega Jy),
    V4=DOmega U,
    V5=-DU Omega,
    Rv=V1+V2+V3+V4+V5.

When div U=0, Rv is the curl of

    (1-c)U+c DU y+w(JU-DU Jy)+DU U+grad P

for any C^2 pressure P. Without the divergence hypothesis, the curl contains the additional term (div U)Omega, as proved in the vorticity identity topic.

Let positive sample weights a_i sum to one, with points y_i in D, and let

    Q(F)=sum_i a_i |F(y_i)|^2.

If their denominators are positive, define

    rho_v=sqrt(Q(Rv))/sum_(k=1)^5 sqrt(Q(Vk)),
    rho_v_nl=sqrt(Q(Rv))/(sqrt(Q(V4))+sqrt(Q(V5))),
    sigma_v=sqrt(Q(Rv))/sqrt(Q(Omega)).

For a disjoint finite partition of D into domains D_j of positive volumes v_j, and normalized quadratures Q_j on those domains, the corresponding finite-volume ratio is

    sigma_v(D)^2 =
      sum_j v_j Q_j(Rv) / sum_j v_j Q_j(Omega).

The square root is taken only for a positive denominator. This combines squared integrals using physical volumes. An equal average of the individual ratios, or a sum of normalized shell means without volumes, is a different statistic.

## Normalized shell, cap, and translated-ball rules

For 0<=a<b, spherical coordinates with

    r(t)=(a^3+(b^3-a^3)t)^(1/3), 0<t<1,

give the normalized shell rule

    mean_D F = (1/(4 pi)) int_(S^2) int_0^1 F(r(t)n) dt dS(n).

For a ball centered at z, replace r(t)n with z+b t^(1/3)n.

Fix 0<delta<1 and put mu0=sqrt(1-delta^2). The two axis caps are the directions with |n3|>mu0, equivalently sin(theta)<delta. The normalized angular mean on their union is

    1/(4 pi(1-mu0)) int_0^(2 pi) int_mu0^1
       [F(sqrt(1-mu^2)cos(phi),sqrt(1-mu^2)sin(phi),mu)
        +F(sqrt(1-mu^2)cos(phi),sqrt(1-mu^2)sin(phi),-mu)]
       dmu dphi.

With a normalized Gauss rule on [mu0,1], equally weighted azimuthal nodes, and a factor 1/2 for each hemisphere, the combined angular weights sum to one. Combining this rule with the radial rule gives normalized volume means on the portions of each shell inside the two caps.

## Proof

The formula for Rv follows from the Cartesian curl identities in ../vorticity_identity/PROOF.md. In particular, differentiating c DU y adds c Omega to c DOmega y. Together with the curl of (1-c)U this gives V1+V2. The rotational and nonlinear terms give V3 and V4+V5 under div U=0. The curl of a C^2 gradient is zero.

The finite ratios are definitions in a Euclidean space whose coordinates are multiplied by sqrt(a_i). Multiplying a normalized mean by its domain volume gives its unnormalized quadrature integral. Additivity on the partition proves the finite-volume ratio formula.

For the shell formula, dy=r^2 dr dS and r^2 dr=(b^3-a^3)dt/3; division by 4 pi(b^3-a^3)/3 gives the result. Translation has Jacobian one and proves the ball formula. For the caps, dS=dphi dmu and their combined area is 4 pi(1-mu0); dividing the two integrals by that area proves the cap normalization.

## Numerical scope

The numerator uses the stable linear curl plus V4+V5. The five individual terms are retained for denominators and for a direct-versus-stable consistency diagnostic. A vanishing denominator is reported as undefined, without an added epsilon.

A result on |y|<R is a finite-ball value. Without a bound on the exterior integrals, it is not the full-space sigma_v. Centered balls use a recorded sampled maximum location and effective radius; the quadrature does not certify a continuous maximizer. Two quadrature levels show computed changes, not error enclosures.

Dependencies: the vorticity identity and potential representation topics, spherical-coordinate integration, and finite sums. No formal source or formal verification is supplied.
