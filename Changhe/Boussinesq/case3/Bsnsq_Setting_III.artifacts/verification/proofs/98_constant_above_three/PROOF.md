# A finite-part source constant for every noninteger exponent b>1

Written UTC: 2026-10-21T01:01:03.798267+00:00. This is a source-inverse identity, not a profile theorem.

## Statement and notation

Let b>1 be noninteger, N=floor(b), L>0, and S be C^N on [0,1], with S^(N) Lipschitz near1. Piecewise polynomials with the stated matching regularity are allowed. Put
z=(1+r^2/L^2)^(-1/(2b)), f(z)=S(1-z), f_j=f^(j)(0)/j!,
and q_b(r)=r z^(b+1) S(1-z). Let Omega=q_b(r) cos(theta), using the usual polar angle X=(r cos(theta),r sin(theta)). Equivalently its first sine coefficient for phi=atan2(x,-y) is q_b.

For j=0,...,N-1 define a_j=(j+1)/b<1 and the full homogeneous sources q_j(r)=B_j r^(-a_j), B_j=L^(1+a_j)f_j. Their canonical full-plane homogeneous velocities u_j are defined on r>0, without a cutoff. Let V be the canonical relative velocity of Omega, V(0)=0. Then

C=lim_(r->infinity) [V(r,theta)-sum_(j<N)u_j(r,theta)] = (0,C_2)

uniformly in theta, where

(1) C_2= -b L^2/2 [ integral_0^1 z^(-b)(f(z)-sum_(j<N)f_j z^j) dz + sum_(j<N) f_j/(j+1-b) ].

The integral is absolutely convergent. For 3<b<4 this subtracts exactly three homogeneous source tails. Formula (1) cannot be evaluated at integer b; logarithmic resonances require finite-part conventions such as packet95. For b in (2,3), (1) agrees with packet93 before its integration by parts.

## Proof

The exact change of variables gives q_b(r) dr=-b L^2 z^(-b) f(z) dz. Taylor's theorem with the stated regularity gives f(z)-sum_(j<N)f_j z^j=O(z^N), so the integrand at0 is O(z^(N-b)), with N-b>-1. There is no singularity at z=1.

For r large, the exact relation r=L z^(-b) sqrt(1-z^(2b)) implies
q_b(r)=sum_(j<N)B_j r^(-a_j)+O(r^(-(N+1)/b))+O(r^(-2-1/b)).
This follows by Taylor expansion of f and the square-root factor. The remainder exponent (N+1)/b exceeds1. Near0 the original source is O(r), while every subtracted homogeneous term has exponent a_j<1. Consequently
eta(r)=q_b(r)-sum_(j<N)B_j r^(-a_j)
is absolutely integrable over (0,infinity).

The ordinary full-plane velocity of eta(r)cos(theta) has value at0 equal to (0,(1/2)integral eta dr). Its velocity tends to0 at infinity. The latter also follows directly from its first-mode Green formula: choose d>1 with |eta(r)|<=M r^(-d) at infinity, reducing d below3 if needed. Then r^(-2)integral_0^r rho^2 eta(rho)dr and integral_r^infinity eta(rho)dr both tend to0. The locally integrable singular homogeneous subtractions at0 contribute a finite inner integral. Thus the relative velocity of eta tends to minus its ordinary center velocity. Linearity and the canonical homogeneous inverses give
C_2=-(1/2) integral_0^infinity eta(r)dr.
This proves the existence, uniform angular limit and absence of an arbitrary added velocity.

It remains to evaluate that moment. Put R=L z^(-b)sqrt(1-z^(2b)). At this finite cutoff,
int_0^R q_b dr=bL^2 int_z^1 t^(-b) f(t)dt,
int_0^R B_j r^(-a_j)dr = bL^2 f_j/(b-j-1) * z^(j+1-b)*(1-z^(2b))^((b-j-1)/(2b)).
Integrating the polynomial part of f in the first expression yields
bL^2 f_j [1-z^(j+1-b)]/(j+1-b).
Its divergent z-power is exactly cancelled by the second expression. The remaining difference of that divergent term and its square-root factor tends to0, since it is O(z^(j+1+b)). The absolutely convergent remainder integral passes to its limit. Hence
int eta dr=bL^2 [int_0^1 t^(-b)(f(t)-sum_(j<N)f_j t^j)dt+sum_(j<N)f_j/(j+1-b)],
which proves (1).

## Scope and dependencies

The source identity needs only the stated radial regularity and the canonical first-mode inverse, whose sign and centering were independently derived in packet03. It does not require the Boussinesq PDE, center strain c=1+beta/2 or nonzero temperature. In a larger angular expansion, this first-mode calculation supplies the only possible constant velocity contribution; other modes must separately satisfy their inversion and asymptotic hypotheses. No assertion C=0 for an exact profile with 3<beta<4 is proved here. That requires an extension of the coupled PDE argument of packet90. A source may have C of either sign. At b=3 the two-tail constant generically diverges logarithmically and this three-tail expression has a pole; it is not the log finite part of packet95.
