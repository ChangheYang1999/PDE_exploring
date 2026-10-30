# Varying the exponent requires a nonlinear tail chart

Status: new normalization audit, OPEN independent Opus review. It
sharpens the design warning in T2 the review of T4-189, Remark R4. It is not
an obstruction to using a genuinely nonlinear parameterized tail.

## Spaces, tails and exact statement

Let a be real. Write E_a=L2(R2,(1+r^2)^(-a)dX). Fix a nonzero smooth
real angular function Theta with S1 parity. Choose a radial smooth cutoff
chi with 0<=chi<=1, chi=0 for r<=1 and chi=1 for r>=2, and set

    T_gamma(X)=chi(r) r^gamma Theta(theta).

Let I be a nontrivial interval in (0,1) such that gamma>=a-1 for every
gamma in I. The following assertions hold.

1. The equivalence classes of T_gamma, gamma in I, are linearly
   independent in D'(R2)/E_a. In particular, for a fixed gamma0 in I,
   no finite-dimensional linear space Z of distributions can contain
   all differences T_gamma-T_gamma0 modulo E_a.
2. If gamma!=gamma0 both belong to I, then for every finite real
   polynomial P, T_gamma-chi r^gamma0 P(log r)Theta is not in E_a.
   Thus no finite logarithmic Taylor correction represents an actual
   exponent change with an E_a remainder.
3. This does not prevent a finite-parameter nonlinear chart. If I is
   compact and b>1+max I, gamma -> T_gamma is a C-infinity map from a
   neighborhood of I to E_b. On I its N-th derivative has the explicit
   bound

    ||partial_gamma^N T_gamma||_(E_b)^2
       <= ||Theta||_(L2(S1))^2 (2N)!/[2epsilon]^(2N+1),
    epsilon=b-1-max I>0.                            (1)

The inclusion E_a subset E_b is continuous here because b>a. Therefore
(gamma,h) -> T_gamma+h, with h in E_a, is a well-defined smooth map to
the weaker ambient space E_b. It does not become a map into a single
affine E_a space, and no stationary equation or inverse is supplied.

## Proof of linear independence modulo the correction space

Take distinct gamma1,...,gammaM in I and real coefficients, not all zero.
Let gamma* be the largest exponent having a nonzero coefficient b*.
The sum on r>=2 equals

    r^gamma* [b*+o(1)]Theta(theta).

Its angular squared norm is at least
|b*|^2 ||Theta||2^2 r^(2gamma*)/4 for all sufficiently large r.
For each fixed real a, the weight (1+r^2)^(-a) is comparable to r^(-2a)
there, with positive constants. The radial square integral consequently
dominates a positive multiple of

    int_R^infinity r^(2gamma*-2a+1)dr,

which diverges because gamma*>=a-1, including equality. Thus no such
nonzero finite sum lies in E_a, proving assertion1's independence.

For the affine claim, choose any finite number of distinct exponents
other than gamma0. A relation among their differences would give a
relation among those tails and T_gamma0, just proved impossible. Their
classes are therefore also independent. The image of any finite-dimensional
Z in the quotient has dimension at most dim Z and cannot contain them all.
No topology on the quotient is used.

## Proof for finite logarithmic corrections

If gamma>gamma0, r^(gamma0-gamma)P(log r) tends to zero. Hence T_gamma
is the nonzero leading power of the difference, which is not in E_a.
If gamma<gamma0 and P is nonzero, let N be its degree and b_N its
nonzero leading coefficient. The angular norm of the difference is
asymptotic to |b_N| r^gamma0 (log r)^N ||Theta||2. This also has infinite
E_a norm, since gamma0>=a-1. If P=0, T_gamma itself has infinite norm.
This proves assertion2. It covers every finite Taylor polynomial in
(gamma-gamma0)log r, not just the first derivative.

## Smooth nonlinear chart in a weaker ambient space

All formal derivatives are

    partial_gamma^N T_gamma=chi r^gamma (log r)^N Theta.

Since b>1 and r>=1 on the cutoff support, (1+r^2)^(-b)<=r^(-2b).
Their squared norms are at most

    ||Theta||2^2 int_1^infinity
         r^(-1-2epsilon)(log r)^(2N) dr.

With t=log r this becomes the elementary exponential moment in(1).
The identity int_0^infinity e^(-2epsilon t)t^(2N)dt
=(2N)!/(2epsilon)^(2N+1) follows by repeated integration by parts.
On a slightly larger compact interval the same argument has a positive
margin. Difference quotients and their derivatives are then dominated
in E_b by the corresponding logarithmic majorants, proving C-infinity
smoothness. Addition of h is bounded E_a -> E_b, which proves assertion3.

## Application and limits

For the campaign gamma=1/c. On a positive c interval the preceding
nonlinear chart can equivalently use c as its coordinate. At first order
partial_c T_(1/c)=-c^-2 chi r^(1/c)log(r)Theta, but this tangent formula
does not supply the full finite change modulo E_a. The additional tail
amplitude and angular coordinates can be prescribed separately.

A proposed augmented existence theorem must encode the full parameterized
tail and verify its residual cancellations, velocity normalization,
strictly subcritical remainder inverse and nonlinear mapping estimates.
A matrix with one exponent-tangent column alone verifies none of these.
Conversely, assertions1 and2 do not rule out such a nonlinear construction.

Dependencies: finite sums of distinct powers, elementary weighted L2
integrability and dominated differentiation. No outside theorem, numerical
input, origin trace or fractional operator is used.
