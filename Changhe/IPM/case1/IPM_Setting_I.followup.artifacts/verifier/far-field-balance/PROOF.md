# The first far-field transport balance

Date: 2026-10-20. Status: necessary asymptotic identity and numerical trial audit. It is not an existence theorem or a condition on freely prescribable data.

## Statement

Let 0<k<1, c_l=1/k, and let rho be a real, x-even, y-odd, locally C^(2,alpha) density with its canonical full-plane velocity U. Suppose it has at infinity the uniform differentiable expansion

    rho(r,theta)=r^k F(theta)+r^(2k-1) G(theta)+o(r^(2k-1)),

where F and G are smooth periodic functions, and the remainder has radial derivative o(r^(2k-2)) and angular derivative o(r^(2k-1)). Assume globally |rho|<=C(1+r)^k and |grad rho|<=C(1+r)^(k-1). The latter estimate concerns large r; local boundedness is sufficient near zero. Write

    S(theta)=k cos(theta) F(theta)-sin(theta) F'(theta).

Let P be the unique odd-in-x, odd-in-y periodic solution of

    -P''-(k+1)^2 P=S.

Equivalently, for its Fourier coefficient of order m,

    P_m=S_m/(m^2-(k+1)^2).

There is no zero denominator since k+1 is strictly between1 and2. The homogeneous density r^k F has canonical stream function r^(k+1)P and velocity

    U_infinity=r^k[-P' e_r+(k+1)P e_theta].

Then the full physical transport residual R=(c_l X+U).grad rho-rho satisfies, uniformly in angle,

    r^(1-2k) R(r,theta) -> D(theta),
    D=(1-c_l)G-k F P'+(k+1)P F'.                         (1)

In particular an exact profile with this differentiable expansion must obey

    G=[-k F P'+(k+1)P F']/(c_l-1).                       (2)

No equation -k F P'+(k+1)P F'=0 is implied. It is the next radial coefficient G that balances this nonlinear term. The expansion hypothesis is stronger than the class-wide trace statement in ../far-field-trace/PROOF.md. It holds for each fixed finite nodal representation used below, but is not asserted for every admissible profile.

## Proof of the inverse limit and residual identity

The kernel and contact term are those in ../inverse/PROOF.md. For rho_infinity=r^k F the source derivative is r^(k-1)S. Applying the polar Laplacian to r^(k+1)P gives the displayed angular equation. The corresponding velocity has degree k and the correct parities. The symmetric canonical integral of rho_infinity exists: smooth angular behavior gives local principal-value cancellation away from zero, local integrability holds at zero, and oddness cancels the leading far kernel term so its tail is bounded by C|X| integral_R^infinity s^(k-2)ds. Scaling gives a homogeneous degree-k velocity. The difference between this velocity and the one from r^(k+1)P is globally distributionally curl-free and divergence-free, and is smooth harmonic on the entire plane. Indeed the homogeneous stream has locally integrable second derivatives and no delta source at zero, since its gradient tends to zero there; both velocities extend continuously to zero. A globally harmonic sublinear field is constant, and parity makes that constant zero. Thus this is the canonical velocity, with no harmonic gauge freedom.

For clarity the required velocity limit can also be checked directly. Set E=rho-rho_infinity. At |X|=r the scaled density difference E/r^k tends uniformly to zero on every comparable annulus, and its scaled gradient is bounded. In the local kernel disk |X-Y|<eta r subtract E(X); its normalized principal value is at most C eta, uniformly in r. On eta r<|X-Y|<r/2 the normalized integral tends to zero for each fixed eta>0, using uniform amplitude convergence and the integrable logarithm log(1/eta). The contact term also tends to zero. In the region away from the observation point scale Y=r Z. On tau<|Z|<T the normalized difference converges uniformly to zero, while the small ball and the paired far tail are bounded by C(tau^(k+2)+r^-k tau^2) and C(T^(k-1)+r^-k/T), respectively. First choose eta,tau small and T large, then let r grow. Hence U/r^k converges uniformly to -P'e_r+(k+1)P e_theta.

The differentiable expansion gives

    grad rho=r^(k-1)(k F e_r+F' e_theta)+o(r^(k-1)).

Consequently the nonlinear advection divided by r^(2k-1) converges to -k F P'+(k+1)P F'. The exact Euler part gives

    c_l r rho_r-rho=(1-c_l)r^(2k-1)G+o(r^(2k-1)),

because c_l k=1. Adding the two terms proves(1). An exact profile has R identically zero, so(2) follows. The estimates include angles at which F vanishes; no division by F occurs.

## What a small far-field normalized residual means

For an angle where

    N_infinity=|F|+c_l {|cos(theta)[k cos(theta)F-sin(theta)F']|
                           +|sin(theta)[k sin(theta)F+cos(theta)F']|}

is positive, the report's N_f=|rho|+sum_i |W_i rho_i| has N_f/r^k tending to N_infinity. Indeed W_i=c_l X_i+O(r^k), and the differentiated leading density gives each displayed term after division by r^k. Equation(1) therefore implies

    |R|/N_f=r^(k-1) |D|/N_infinity+o(r^(k-1)).

Thus this normalized residual tends to zero in every fixed finite nodal trial at such angles, even when its first transport balance D is nonzero. Small values at a very large radius do not establish the identity(2), or control defects at moderate radii. This is a consequence of the normalization and the imposed leading exponent c_l k=1, not a uniform lower or upper bound on the residual over the plane.

## Exact coefficients of a nodal trial

For a fixed stored field write

    rho=x^2 y (1+r^2/L^2)^((k-3)/2) b(q,s(theta)),
    q=1-(1+r^2/L^2)^(-(1-k)/2),
    theta=s+(beta/2)sin(2s)

in the first quadrant, followed by the exact reflection parities. The stored b is a tensor polynomial in2q-1 and cos(2s). Its smooth angular continuation and finite radial degree imply

    F=L^(3-k) cos^2(theta) sin(theta) b(1,s(theta)),
    G=-L^(4-2k) cos^2(theta) sin(theta) b_q(1,s(theta)).   (3)

To see this, q=1-L^(1-k)r^(k-1)+O(r^(k-3)), and the radial prefactor is L^(3-k)r^k[1+O(r^-2)]. Taylor expansion of the finite polynomial gives the next coefficient in(3) and a remainder O(r^(3k-2)), with the corresponding differentiated bounds. Since 3k-2<2k-1, this is the required little-o remainder. The prefactor's O(r^(k-2)) term is smaller still. The same finite representation satisfies the stated large-r gradient bound.

If c_nm are the independently reconstructed tensor cosine coefficients, then

    b(1,s)=sum_m (sum_n c_nm)cos(2ms),
    b_q(1,s)=sum_m (2 sum_n n^2 c_nm)cos(2ms),

using T_n(1)=1 and T_n'(1)=n^2. These formulas do not use the orbit solver's last row or its inverse.

## Computation and scope

The independent implementation obtains F,G and F' from(3), with the derivative of the angular coordinate computed analytically. It solves the homogeneous Poisson problem by physical-angle Fourier coefficients. This is distinct from both the numerics lane's inverse and this lane's real-space quadrature. Multiple angular resolutions and the manufactured density x^2 y(1+r^2)^(-7/5) check the calculation; its known homogeneous stream is given in ../far-field-trace/PROOF.md. A direct full-plane residual check at growing radii tests(1) separately.

A nonzero computed D is a far-field defect of the represented trial, not a lower bound on all nearby fields or a certified uniform error. A floating Fourier calculation is not an interval certificate. Numerical D approaching zero under changes of representation would still require the full transport, center, source and convergence checks. This identity neither replaces the B_j tests nor decides the strong-setting endpoint. Code and observations are retained in the adjacent named folders. No formal build is used.

## A zero leading normalizer: an explicit analytic trial

Added 2026-10-20 after fred50 identified an omitted qualification in the proposed report text. The positivity condition in this proof's normalized statement was already explicit, but AV45 did not catch its omission in that draft. It is essential, even for normalized smooth canonical trials satisfying the central c_l identity.

Here is a directly computable variant of fred50's cutoff example. Fix k=1/5, c_l=5, t=37087/336 and put

    rho=x^2 y [(x^2-y^2)^2(1+r^2)^((k-7)/2)
                  +(1+r^2)^(k-2)+t r^2 exp(-r^2)].        (4)

This density is real analytic on the plane, has the required parities, is x^2 y times a positive smooth function with a(0)=1, and obeys the sublinear density and gradient bounds. Its canonical inverse exists. Its exterior coefficients are

    F=cos^2(theta)sin(theta)cos^2(2theta),
    G=cos^2(theta)sin(theta).

The prefactor errors have size O(r^(k-2)) and O(r^(2k-3)), both smaller than r^(2k-1), with the required differentiated bounds. The Gaussian term is negligible there.

To check the central strain, differentiate the first canonical kernel, using rho=O(r^3) at zero and sublinear growth for convergence. This gives

    psi_xy(0)=1/pi int y(3x^2-y^2)rho(x,y)/r^6 dxdy.

The angular integrals for x^2 y times a radial factor and for the additional cos^2(2theta) factor are 1/4 and 1/16. They follow by reflection x<->y and sin^2(2theta)cos^2(2theta)=sin^2(4theta)/4. Thus the three terms of (4) contribute

    S_1=1/[2(1-k)(3-k)(5-k)],
    S_2=1/[8(1-k)],
    S_3=t/8.

For example, S_1 follows from (1/16)int_0^infinity r^5(1+r^2)^((k-7)/2)dr and the beta integral; the other two are elementary radial integrals. At k=1/5, S_1+S_2=545/2688 and t/8=14-545/2688. Hence psi_xy(0)=14=3c_l-1 exactly.

On the ray theta=pi/4 the leading F and its first derivative both vanish, whereas G>0 and G'=-G. Put q=2k-1. The velocity has size O(r^k) by the inverse limit already proved, so its contribution to transport is o(r^q) on this ray. The Euler part of R is (1-c_l)G r^q+o(r^q). Moreover x rho_x/r^q tends to kG and y rho_y/r^q tends to (k-1)G. Consequently

    |R|/N_f -> (c_l-1)/(c_l+1)=2/3.                       (5)

Thus an unqualified all-angle limit zero is false. This trial is not a transport solution; it refutes only that asserted consequence of the expansion and the normalizations. The leading normalizer vanishes on this ray. Its nonzero limit does not contradict the restricted statement above.

For a separate exterior bound in the numerical check, |rho|<=224 r^(1/5) for r>=1. The first two terms are each at most r^(1/5), and the Gaussian term is at most 2t r^(1/5): r^(24/5)exp(-r^2)<=r^6 exp(-r^2)<=27exp(-3)<2. Since 2+2t<224, the bound follows. It controls the omitted tail independently of the computed velocity. Values of the quadrature are still floating evidence, not certificates of its interior error.
