# The whole-plane full Holder norm is a different, unbounded problem

## Statement

Fix 0<alpha<1. On real functions on R^2 set

    ||f||_(C^alpha)=||f||_infinity+[f]_alpha,
    [f]_alpha=sup_(x!=y) |f(x)-f(y)|/|x-y|^alpha.

Use the circular principal-value operators and normalization from
../01_setup/PROOF.md. For each A in {T_xx,T_xy,R_1^2},

    sup_(0!=f in C_c^infinity(R^2))
        ||Af||_(C^alpha)/||f||_(C^alpha) = infinity.

The assertion remains true if the numerator is only ||Af||_infinity.
It also remains true if that supremum norm is minimized over additive
constants in the output. The finite constants C_alpha and D_alpha
proved elsewhere are homogeneous seminorm bounds, not bounds for this
full norm. No contradiction is involved: the example produces an
increasing oscillation over an increasing spatial scale.

## A uniformly bounded family of smooth inputs

Choose a fixed smooth nondecreasing chi:R-> [0,1] with chi(t)=0 for
t<=1, chi(t)=1 for t>=2 and |chi'|<=2. Such a function may be obtained
by mollifying the piecewise linear transition from 0 at 9/8 to 1 at
15/8 with a nonnegative smooth kernel supported in [-1/8,1/8]. Its
slope is at most 4/3 before and after mollification.

For R>=2, let

    eta_R(r)=chi(r)(1-chi(r/R)),
    f_R^c(r,theta)=eta_R(r) cos(2theta),
    f_R^s(r,theta)=eta_R(r) sin(2theta).

Both functions are defined to be zero at the origin. They vanish on
r<=1 and r>=2R, so they belong to C_c^infinity(R^2). They have magnitude
at most one and eta_R=1 on 2<=r<=R. The inner and outer transition
regions have disjoint interiors. Consequently |eta_R'|<=2 for R>=2.
Where eta_R is nonzero, r>=1. In the orthonormal polar frame the radial
derivative of either f_R is at most 2 and its angular derivative divided
by r is at most 2. Thus |grad f_R|<=2sqrt(2)<3, uniformly in R.

For every pair of points at distance d,

    |f_R(x)-f_R(y)|<=min(3d,2).

The largest value of min(3d,2)/d^alpha is
2^(1-alpha)3^alpha, reached at d=2/3. It follows that

    ||f_R||_(C^alpha)<=1+2^(1-alpha)3^alpha<=4.             (1)

## Exact logarithmic growth of the transform

The inputs vanish near the origin, so their transforms at zero are
ordinary integrals. The kernels are even. Angular integration gives

    T_xx f_R^c(0)
      = (1/(2pi)) integral_0^(2pi) cos(2theta)^2 dtheta
                     * integral_0^infinity eta_R(r) dr/r
      = (1/2) integral_0^infinity eta_R(r) dr/r
      >= (1/2) log(R/2).                                  (2)

The same calculation gives T_xy f_R^s(0)>=(1/2)log(R/2).
Since f_R^c(0)=0, R_1^2 f_R^c(0)=T_xx f_R^c(0) by the exact local
identity R_1^2=T_xx-I/2. Combining (1) and (2) yields the explicit lower
bound

    ||Af_R||_infinity/||f_R||_(C^alpha)
      >= log(R/2)/[2(1+2^(1-alpha)3^alpha)].                (3)

It tends to infinity as R tends to infinity. Each numerator is finite
for fixed R: a compact smooth input has a bounded continuous principal
value transform and the transform tends to zero at spatial infinity.
For the latter claim, once |x|>4R the support is separated from x and
|Tf_R(x)|<=||f_R||_1/[2pi(|x|-2R)^2]. The local identity term also
vanishes there.

Finally a bounded real function F with F(0)>=L and F(x)->0 at infinity
satisfies inf_c ||F+c||_infinity>=L/2. Indeed its oscillation is at least
L, while every translate with supremum norm M has oscillation at most
2M. With L=(1/2)log(R/2), the quotient after arbitrary output
normalization is at least

    log(R/2)/[4(1+2^(1-alpha)3^alpha)] -> infinity.

This proves every assertion of the theorem.

## Dependencies and scope

The proof uses only the kernel normalizations and local identity in
../01_setup/PROOF.md, elementary angular integration, and a fixed smooth
cutoff. It does not assert failure of estimates on a fixed bounded
domain, with a fixed support radius, or with additional decay or
integrability norms. The construction explains why those hypotheses
cannot be silently dropped from full-norm literature statements.
