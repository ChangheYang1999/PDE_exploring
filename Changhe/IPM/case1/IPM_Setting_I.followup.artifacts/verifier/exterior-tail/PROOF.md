# Exterior multipoles and an explicit truncation bound

Date: 2026-10-20. Status: the estimates below are proved for the stated represented fields. They bound an omitted density tail, not quadrature error or the transport defect. No existence claim follows.

## Statement and notation

Let rho be even in x and odd in y. Suppose |rho(Y)| <= C |Y|^gamma for |Y| >= R, where 0 < gamma < 1. For |X| < R define the exterior velocity by the canonical symmetric integral over |Y| >= R. Write z=x+iy, and define the real angular coefficients

    rho_n(r) = (1/pi) integral_0^(2pi) rho(r cos theta,r sin theta) sin(n theta) dtheta.

Then the exterior complex velocity V_R=U_1+i U_2 is

    V_R(z) = -sum_(m>=0) (m+1) conjugate(z)^(2m+1) M_(2m+3)(R),
    M_(2m+3)(R) = integral_R^infinity rho_(2m+3)(r) r^(-2m-2) dr.

The series converges absolutely and locally uniformly in |z|<R. In particular the leading term is (-c_R x,c_R y), with c_R=M_3(R). Put t=|X|/R. The following bounds hold:

    |U_ext(X)| <= [2 C/(1-gamma)] |X| R^(gamma-1)/(1-t^2)^2,

    |U_ext(X)-(-c_R x,c_R y)|
      <= [2 C/(3-gamma)] |X|^3 R^(gamma-3) (2-t^2)/(1-t^2)^2.

The norm here is the Euclidean norm, equal to the complex modulus. A pure first angular sine mode supported outside R induces identically zero velocity inside R. These assertions concern a cutoff in the density variable centered at the origin. A cutoff centered at each observation point is a different truncated operator.

## Proof of the expansion and estimates

For a vector Z identified with its complex coordinate, the kernel in the task obeys

    K_1(Z)+i K_2(Z)=i/[2pi conjugate(Z)^2].

For |z|<|Y| the geometric derivative series gives

    1/(conjugate(z)-conjugate(Y))^2
      = sum_(n>=0) (n+1) conjugate(z)^n/conjugate(Y)^(n+2).

On a finite annulus this series converges uniformly if |z| stays in a compact subset of |z|<R. The n=0 angular integral is zero by inversion oddness. All even n vanish for the same reason. The reflection parities also make every surviving angular integral purely imaginary. For n=2m+1 it is i pi rho_(2m+3)(r). Multiplying the kernel prefactor and the polar measure r dr yields exactly the displayed negative real coefficients.

The bound |rho_n(r)| <= 2 C r^gamma follows directly from its defining angular integral. Thus

    |M_(2m+3)(R)| <= 2 C R^(gamma-2m-1)/(2m+1-gamma).

This summable estimate justifies passage to the exterior limit, exchange with the series, and local uniform convergence. Replacing the denominator by 1-gamma and summing sum_(m>=0)(m+1)t^(2m)=(1-t^2)^(-2) proves the first estimate. For the remainder start at m=1, replace the denominator by 3-gamma and use

    sum_(m>=1) (m+1)t^(2m-2)=(2-t^2)/(1-t^2)^2.

The first-mode assertion follows because every displayed moment then vanishes. The expansion is anti-holomorphic with real coefficients, so the exterior velocity is divergence free and curl free inside the disk. Its first term is a harmonic strain. It represents omitted exterior data; it is not a free global gauge. An entire harmonic velocity of sublinear growth and the required parities is zero, by the mean-value derivative estimate and parity.

## A uniform coefficient bound for X3

Interpret the saved floating-point coefficients as the exact real numbers they represent. The X3 density is

    rho=x^2 y (1+r^2/L^2)^((k-3)/2) exp(H+S),

where H is the angular sum of nonnegative, partition-of-unity B-splines, with the m>=2 terms multiplied by a damping factor of modulus at most one. The saved knot vector has the usual repeated end knots, and its B-spline basis is nonnegative and sums to one on q in [0,1]. Every coefficient row has absolute sum less than 4. Therefore |H|<4, uniformly in q and angle.

The singular part S is s^(p3/2) times a finite Chebyshev sum times |cos theta|^(p3-2) sin(theta)^2. Here 0<=s<=1, p3>6, and the sum of the absolute singular coefficients is less than 16. Since

    |cos theta|^(p3-2) sin(theta)^2 <= cos(theta)^4 sin(theta)^2 <= 4/27,

one has |S|<64/27, hence H+S<7. The saved L satisfies 1<L<8 and 0<k<1/5. For r>=1,

    |rho| <= L^(3-k) r^k exp(7) < 512 * 3^7 * r^(1/5).

We used only e<3 in the last bound. Thus C_X3=1119744 and gamma=1/5 are valid. The exact coefficient inequalities and knot checks are recorded by code/coefficient_bounds.py. The large constant is deliberate: it makes the tail estimate independent of a fitted angular envelope.

## A uniform coefficient bound for the nodal dnSB field

The saved state has N=120, M=48, L=8, 0<k<1/5 and absolute nodal values less than 27. Its density is the same radial prefactor times the tensor Chebyshev interpolant b, evaluated at q in [0,1] and cos(2s) in [-1,1]. This section concerns the exact interpolant through the saved nodal numbers. The independently computed DCT representation approximates that interpolant in floating point; its arithmetic error is not included in the exterior bound.

Use the discrete probability measure on the N+1 Lobatto nodes with endpoint weights 1/(2N) and interior weights 1/N. The squared norms of T_0 and T_N are 1, and those of the remaining T_j are 1/2. On the M angular Gauss nodes with weights 1/M, the squared norm of T_0 is 1 and those of the remaining T_m are 1/2. Tensor orthogonality and Cauchy-Schwarz give, everywhere on the interpolation rectangle,

    |b(q,s)| <= max_nodes |b| * sqrt(2N(2M-1)) < 27*151 = 4077.

Indeed the squared norm of the interpolant equals the weighted nodal squared norm, at most max_nodes |b|^2. The dual norm of point evaluation is at most the square root of the sum of reciprocal basis norms: sqrt(2N(2M-1)). No derivative or endpoint extrapolation is used. It follows that

    |rho| <= 512*4077*r^(1/5) = 2087424*r^(1/5),  r>=1.

The radial and angular node identities used here are part of the representation; the numerical node arrays are also checked against them to report the floating-point transcription discrepancy.

## Numerical size and scope

The bound script evaluates the analytic tail inequality with rational upper bounds. For example, at R=10^30 and |X|<=10^5, the tail is below 6e-13 for either saved field. The omitted strain coefficient is below 6e-18. More precise outward rational bounds are saved in verification/coefficient_bounds.json. These are bounds on the exact represented density's omitted exterior contribution. They do not certify the quadrature inside R, the physical residual, the orbit map, a continuum solution, or a grid limit.

Dependencies: the task's canonical kernel, a geometric series, elementary Fourier orthogonality, B-spline positivity and partition of unity, Chebyshev discrete orthogonality, and Cauchy-Schwarz. No teammate inverse or solver code is used. There is no formal proof-assistant build.
