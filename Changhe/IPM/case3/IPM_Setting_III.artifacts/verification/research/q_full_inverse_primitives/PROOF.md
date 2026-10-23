# Finite compact-coordinate primitives for the canonical Q inverse

Status: analytical derivation complete; implementation and manufactured checks pending. This argument was written before the implementation. Date: 2026-10-20. This is result 86 in the reading-order index.

## Statement and notation

Let L>0, kappa>1, r_c=L 2^(-kappa), and let B_0,...,B_(M-1) be real polynomials. Set B_j=0 for j>=M. The compact coordinate s in [0,1) is defined by

    r = r_c sqrt(s) (1-s)^(-kappa),  w=1-s,
    rho(r,theta)=r w sin(theta) sum_(j=0)^(M-1) s^j B_j(2s-1) cos(2j theta).

For this proof only, write B_j(s) for the polynomial B_j(2s-1) after the change of variable. Define polynomials

    D_0(s)=B_0(s)-s B_1(s)/2,
    D_j(s)=(B_j(s)-s B_(j+1)(s))/2,  j>=1,
    J(s)=1+(2 kappa-1)s,  H_j(s)=J(s)D_j(s).

The sine coefficient of rho/r at frequency 2j+1 is b_j(s)=w s^j D_j(s). For j=1,...,M put

    K_j=2 kappa(j+1),  Kbar_j=2 kappa(j-1),
    A_j(s)=(1/2)s^(-j-1) w^(K_j)
               int_0^s u^(2j-1)(1-u)^(-K_j) H_(j-1)(u) du,
    Bcal_j(s)=(1/2)s^(j-1) w^(-Kbar_j)
               int_s^1 (1-u)^(Kbar_j) H_j(u) du.                 (1)

Here H_M=0. Then the canonical stream and velocity are given by finite sums

    psi/r^2=sum_j p_j sin(2j theta),  p_j=(Bcal_j-A_j)/2,
    U_r/r=-sum_j 2j p_j cos(2j theta),
    U_theta/r=sum_j d_j sin(2j theta),
    d_j=(2j(A_j+Bcal_j)-b_(j-1)-b_j)/2.                         (2)

These formulas contain the full exterior integrals, with no artificial boundary, free harmonic strain, or density-dependent truncation radius. They apply to the finite density formula whether or not the transport equation holds. Its exponent at infinity is gamma=1-1/kappa in (0,1).

## Canonical inverse proof

The product-to-sum identity gives the stated b_j. Let t=log r and a dot denote d/dt. The frequency n=2j coefficient of rho_x is

    S_n=(dot b_(j-1)-(n-2)b_(j-1)+dot b_j+(n+2)b_j)/2.

Solving the radial Poisson equation -Delta psi=rho_x with regularity at zero and subquadratic growth at infinity gives

    psi_n(r)=(1/(2n))[r^(-n) int_0^r v^(n+1) S_n(v)dv
                              +r^n int_r^infty v^(1-n)S_n(v)dv].

The integrals converge. At zero b_0=a+O(r^2), b_j=O(r^(2j)) for j>=1, and the cancellation in S_2 removes the constant. At infinity b_j and dot b_j are O(r^(-1/kappa)), so S_n has the same bound. Integrating the differentiated b terms by parts yields

    A_j = int_0^infty exp(-(2j+2)v) b_(j-1)(log r-v)dv,
    Bcal_j = int_0^infty exp(-(2j-2)v) b_j(log r+v)dv,
    psi_n/r^2 = (Bcal_j-A_j)/2.

For j=1 the exterior exponential is 1; its b_1 factor still decays as r^(-1/kappa). Boundary terms at both radial endpoints vanish by the estimates above. Logarithmic differentiation gives

    dot A_j=b_(j-1)-(2j+2)A_j,
    dot Bcal_j=(2j-2)Bcal_j-b_j.

Thus (2) follows by differentiating psi. Changing the integration variable to the compact coordinate and using d log r/ds=J(s)/(2s(1-s)) gives (1). The scale r_c cancels exactly. Regularity of the compact map at zero and finite polynomial angular factors makes rho smooth there. The full radial Green solution is also smooth and odd in x and y; its velocity is O(r^gamma) at infinity. The difference of two admissible velocities is an entire harmonic vector field with sublinear growth, hence constant, and the stated parities set that constant to zero. This proves that the displayed inverse has the required gauge. The harmonic Liouville step is the same elementary mean-value gradient estimate used in the separately checked canonical-inverse proof.

## Finite primitive formulas

Write H_j(1-v)=sum_k e_(jk) v^k. Direct integration in the exterior part of (1) gives the polynomial expression

    Bcal_j=(1/2)s^(j-1) w sum_k e_(jk) w^k/(Kbar_j+k+1).        (3)

All denominators are strictly positive. This includes the whole infinite tail.

For the interior term, expand

    (1-v)^(2j-1) H_(j-1)(1-v)=sum_k f_(jk) v^k.

Then

    A_j=(1/2)s^(-j-1) sum_k f_(jk) F_(K_j,k)(w),
    F_(K,k)(w)=(w^K-w^(k+1))/(k+1-K),                         (4)

with continuous limiting value F_(K,k)(w)=-w^K log w when k+1=K. Formula (4) is an exact finite sum. Near a zero denominator its evaluation must use expm1 or the limiting logarithm, rather than subtracting two almost equal powers.

For small s, (4) can lose digits through cancellation. An alternative using H_(j-1)(u)=sum_k h_k u^k is

    A_j=(1/2)s^(j-1) sum_k h_k s^k Z_(2j+k),
    Z_m = w^(K_j)/m * 2F1(K_j,m;m+1;s).                       (5)

Indeed Z_m=w^(K_j)s^(-m) int_0^s u^(m-1)(1-u)^(-K_j)du. The binomial series on 0<=u<=s<1 may be integrated termwise by uniform convergence, proving (5). Integration of the derivative of u^m(1-u)^(1-K_j) gives the backward recurrence

    Z_m=((m+1-K_j)s Z_(m+1)+w)/m.                              (6)

One initial hypergeometric evaluation at the largest needed index followed by (6) computes the finite sequence. No numerical stability bound is asserted for this recurrence. The implementation must allocate guard digits and compare independently increased precision; manufactured quadrature checks are required before applying it to data.

## Center and boundary safeguards

As s tends to zero, A_1 tends to a/4 and A_j=O(s^(j-1)) for j>1. Equation (3) gives finite Bcal_1(0). Consequently

    psi_xy(0)=-a/4+Bcal_1(0)
             =-a/4+int_0^1 [(1-s)/4+kappa s/2]
                                     [B_1(s)-s B_2(s)]ds.

This is the independently checked cancellation-renormalized strain identity. In particular it is not imposed using c_l+c=1. Purely radial densities rho=a y(1-s) have Bcal_j=0, and c=-a/4 for every kappa>1 and L>0.

At s=1 the physical radius is infinite and no point value is assigned. Evaluations approaching it must retain w separately when 1-w rounds to 1. At r=0 parity gives rho=U=psi=0, grad rho=(0,a), and both normalized residual denominators vanish; their ratios are undefined there. On y=0 the same ratios are undefined, while the absolute transport residual is exactly zero. Near this axis no positive floor is inserted in a denominator.

## Dependencies and scope

The derivation uses the finite Q density representation, the canonical radial Green equation, polynomial algebra, and convergent one-dimensional integration. It is independent of the producer's inverse, collocation matrix and numerical differentiation. The numerical implementation may use the verifier's existing independently tested compact-map and scalar Clenshaw density reconstruction. Comparisons at multiple precision levels and with real-space Cartesian-FD checks are numerical evidence, not certified bounds or a proof of existence of a nearby profile.
