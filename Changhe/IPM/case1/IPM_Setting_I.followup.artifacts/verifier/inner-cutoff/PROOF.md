# The omitted inner disk in the independent inverse

Date: 2026-10-20. Status: exact bounds for the specified field representation and a conditional local Hessian bound. These estimates do not certify the remaining quadrature.

## Exact field and center hypothesis

Use the exact ideal-node interpolant b through the stored binary nodal values, of radial Chebyshev degree N and angular cosine degree M-1, with first radial row identically1. Assume L>=1, 0<k<1/5, |beta|<1, and

    rho(x,y)=x^2 y (1+r^2/L^2)^((k-3)/2) b(q(r),theta),
    q(r)=1-(1+r^2/L^2)^(-(1-k)/2).

Let B0 be an integer upper bound on the absolute nodal values and H an integer satisfying H^2>=2N(2M-1). Define

    D=(N^2 H B0+3/2)/L^2.

Then for all r>=0 and all angles,

    |rho-x^2 y| <= r^3 |cos(theta)^2 sin(theta)| D r^2.       (1)

This deliberately coarse bound is useful only for small r. It does not assert that the factor is smooth at the center.

## Proof of the center bound

Tensor discrete orthogonality and Cauchy-Schwarz give |b|<=HB0 on the interpolation rectangle, as proved in ../exterior-tail/PROOF.md. The same discrete orthogonality and Cauchy-Schwarz give sum_(n,m)|a_nm|<=HB0 for its tensor coefficients. Since T_n'(z)=n U_(n-1)(z) and |U_(n-1)(z)|<=n on [-1,1], termwise differentiation gives |d_q b|<=2N^2HB0. The bound on U follows by writing U_(n-1)(cos(t)) as the sum of the n complex exponentials exp(i(n-1-2j)t), j=0,...,n-1, and using continuity at the endpoints. Since b(0,theta)=1 exactly,

    |b(q,theta)-1| <= 2N^2 H B0 q.

Put a=(1-k)/2, so 0<a<1/2. The elementary derivative estimate for (1+t)^(-a) gives q<=a r^2/L^2. With t=(k-3)/2 in (-3/2,0), the radial prefactor w=(1+r^2/L^2)^t satisfies 0<w<=1 and |w-1|<=(3/2)r^2/L^2. Hence |wb-1|<=|b-1|+|w-1|<=Dr^2. Multiplication by |x^2y| proves (1).

## The missing origin strain

Let rho_3(r) be the physical sine3theta Fourier coefficient, normalized by

    rho_3(r)=(1/pi) integral_0^(2pi) rho(r,theta) sin(3theta) dtheta.

The canonical strain is c=integral_0^infinity rho_3(r)/r^2 dr. Its part from0<r<eps is

    c_inner = eps^2/8 + e_inner,       |e_inner| <= D eps^4/4.       (2)

Indeed x^2y=r^3(sin(theta)+sin(3theta))/4, giving the first term. By parity and (1), the remainder of rho_3 has absolute value at most

    (4/pi) D r^5 integral_0^(pi/2) cos(theta)^2 sin(theta) |sin(3theta)| dtheta
      <= (4/(3pi)) D r^5 < D r^5.

Integration after dividing by r^2 proves (2). At eps=10^(-7), eps^2/8=1/800000000000000 exactly. For integral L the remainder bound is rational. This supplies the missing origin contribution to the independently computed strain; it does not enclose numerical errors in the computed annulus.

## The origin-centered cutoff at an observation point

Let X satisfy |X|>eps. The canonical real-space kernel is

    K(z)=(-2z_1 z_2, z_1^2-z_2^2)/(2pi|z|^4),  |K(z)|=1/(2pi|z|^2).

The absolute contribution of a removed origin disk |Y|<eps, with any multiplier between0and1 such as the split partition, is bounded by

    (1+D eps^2) eps^5 / [5(|X|-eps)^2].                        (3)

The triangle inequality gives |X-Y|>=|X|-eps; (1) gives |rho(Y)|<=(1+D eps^2)|Y|^3. Integrating the resulting radial bound proves (3). The paired version has the same bound. At X=0 the origin-disk velocity vanishes by central oddness and kernel evenness.

## The observation-centered principal-value cutoff

Suppose rho is C^2 on the closed disk of radius eps about X, and let H_X bound the operator norm of its Hessian there. In the centered subtraction formula the omitted local disk contributes at most

    H_X eps^2/4.                                               (4)

Taylor's integral formula gives

    |(rho(X+z)+rho(X-z))/2-rho(X)| <= H_X |z|^2/2.

Integrate this against |K(z)| and use polar coordinates to obtain (4). For X=0, central oddness makes the symmetrized density identically zero, so its local contribution also vanishes exactly.

If rho is C^4 on this disk and M4 bounds the fourth directional derivative |D^4rho(Z)[e,e,e,e]| over unit e and all Z in the disk, the more precise expansion is

    U_local_inner = eps^2*(-rho_xy(X)/8, (rho_xx(X)-rho_yy(X))/16) + rem,
    |rem| <= M4 eps^4/96.                                     (5)

To verify the constants, expand the symmetrized density as (1/2)r^2 e^T Hess(rho)(X)e plus a remainder of absolute value at most M4 r^4/24. The angular kernel is (-sin(2theta),cos(2theta)). The angular averages of its product with (1/2)e^T Hess(rho)e are (-rho_xy/4,(rho_xx-rho_yy)/8); the radial integral of r dr is eps^2/2. This proves (5). The independent symbolic test checks the angular constants separately.

## Dependencies and scope

Dependencies are the kernel normalization, elementary Taylor formulas, tensor orthogonality, and the finite trigonometric identity for U_n proved above. The test code independently checks the angular constants. No numerical Hessian sample is a certificate of H_X; a rigorous bound on that disk is required before applying (4) numerically. The exact strain bound (2) needs no such local Hessian estimate and applies to the stored interpolant despite its nonsmooth higher center jet.

## Planned interval Hessian enclosure at a positive observation point

This protocol is written before its implementation. It closes only the hypothesis of(4), not the remaining inverse quadrature.

Enclose the disk in the rectangle x in[x0-eps,x0+eps], y in[y0-eps,y0+eps], assuming both intervals are positive. Treat every stored parameter and nodal value as its exact binary rational, with k=1/c_l. The source arrays are exported to exact hexadecimal-binary64 JSON and imported through the shared exact-data interface, which checks the source hash, shape, finite values and exact round-trip agreement; each output records the JSON and original source hashes. The final dependency manifest pins the code and proof. Compute the tensor Chebyshev coefficient intervals by the exact cosine-transform formula at ideal nodes using outward-rounded real-ball arithmetic. With radial indices j,n=0,...,N, weights omega_0=omega_N=1/2 and other omega=1, and angular index a,m=0,...,M-1, set

    R_nj=(2/N) omega_n omega_j cos(pi*n*j/N),
    A_am=(2/M) eta_m cos(pi*m*(2a+1)/(2M)),
    eta_0=1/2, eta_m=1 otherwise,
    coefficient matrix = R * reversed_radial_nodal_matrix * A.

Discrete cosine orthogonality proves this is precisely the ideal-node interpolant. Enclosing the transcendental cosines and every arithmetic operation therefore encloses its exact coefficients.

Let theta=atan(y/x). Choose any finite real approximate s0. Since F(s)=s+(beta/2)sin(2s) has F'(s)>=1-|beta|>0 on the real line, its unique exact inverse satisfies

    |s-s0| <= |F(s0)-theta|/(1-|beta|).

This encloses s without trusting the approximate inverse. Define c=cos(2s), D=L^2+x^2+y^2, q=1-(1+(x^2+y^2)/L^2)^(-(1-k)/2), z=2q-1. Ordinary differentiation gives

    theta_x=-y/r^2, theta_y=x/r^2,
    theta_xx=2xy/r^4, theta_xy=(y^2-x^2)/r^4, theta_yy=-2xy/r^4,
    c_theta=-2sin(2s)/(1+beta cos(2s)),
    c_thetatheta=-4cos(2s)/(1+beta cos(2s))^2
                  -4beta sin(2s)^2/(1+beta cos(2s))^3,
    q_i=(1-k)(1-q)X_i/D,
    q_ij=(1-k)(1-q)[delta_ij/D-(3-k)X_i X_j/D^2].

The chain rule determines b_i and b_ij from the six polynomial evaluations b,b_z,b_c,b_zz,b_zc,b_cc. Chebyshev differentiation uses only integer factors and divisions by2, so the differentiated coefficient intervals remain rigorous. Let p=x^2 y (1+r^2/L^2)^((k-3)/2), t_i=partial_i log p. Then

    t_x=2/x+(k-3)x/D, t_y=1/y+(k-3)y/D,
    t_ij=-diag(2/x^2,1/y^2)_ij
             +(k-3)[delta_ij/D-2X_i X_j/D^2],
    rho_ij=p[(t_i t_j+t_ij)b+t_i b_j+t_j b_i+b_ij].

The polynomial values are enclosed by direct tensor summation of T_n(z)=cos(n arccos z) and T_m(c)=cos(m arccos c), with each coordinate interval checked to lie strictly inside(-1,1). The cosine identity follows from its addition formula and the defining Chebyshev recurrence. Thus each factor is enclosed on its whole interval; finite interval sums and products enclose each differentiated polynomial. Direct interval Clenshaw is mathematically valid but can produce exponentially wide bounds near the endpoints, so it is not used for these rectangles. A single degree120 manufactured term demonstrates this loss of information without changing the underlying polynomial. Interval substitution encloses each entry on the entire rectangle. The sum of their absolute upper bounds, |rho_xx|+2|rho_xy|+|rho_yy|, bounds the Hessian operator norm throughout the disk: the spectral norm is at most the Frobenius norm, which is at most the sum of the absolute entries. Substitution in(4) then yields a rigorous local-hole bound for the ideal-node interpolant. The test protocol must check exact small polynomial transforms and derivatives and a manufactured radial factor before these enclosures are reported. A failed or wide enclosure remains inconclusive; floating samples are not substitutes.

No result from this planned computation has yet been claimed. Disk bounds do not certify annular quadrature, state reconstruction roundoff, or the full residual. The exact-input representation and any later numerical use of gradients must remain explicit.
