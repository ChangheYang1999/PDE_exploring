# Exact pole reduction for compactified radial moments

## Statement

Let b>-1 be rational, let N be a rational polynomial, and let
a_1,...,a_s be distinct positive rational numbers with positive integer
multiplicities m_1,...,m_s. Put

    L_i(v)=1+a_i v, D(v)=product_i L_i(v)^m_i.

Then the signed integral

    I=integral_0^1 v^b N(v)/D(v) dv                         (1)

is finite and has the exact finite representation below. Rational
arithmetic determines its polynomial and principal parts. Outward
arithmetic for the real principal hypergeometric function, followed
by finite outward additions and multiplications, encloses I.

Repeated input scales are first combined by adding their multiplicities.
An empty denominator is allowed. This result applies only after exact
endpoint cancellations have made b>-1. It does not justify integrating
separate divergent terms of a convergent signed expression.

The intended campaign scales are a=99 and9999, arising from
R=10 and100 under v=1/(1+r^2). This scalar identity does not construct
the candidate fields or certify a candidate-level norm by itself.

## Exact principal parts

Divide N=QD+S with degree S<degree D. At the pole v_i=-1/a_i,
use z=L_i(v), so v=(z-1)/a_i. For j different from i,

    L_j((z-1)/a_i)=1-a_j/a_i+(a_j/a_i)z.

Its constant term is nonzero. Expand

    S((z-1)/a_i) product_(j different from i)
       [1-a_j/a_i+(a_j/a_i)z]^(-m_j)

through degree m_i-1 over the rationals. Write these coefficients as
c_(i,0),...,c_(i,m_i-1). The finite principal part at this pole is

    sum_(k=0)^(m_i-1) c_(i,k)/L_i(v)^(m_i-k).

Subtracting all these principal parts from S/D removes every finite
pole. The difference is therefore a polynomial. Each subtracted
principal part tends to zero at infinity, as does S/D, so this polynomial
is zero. Thus

    N/D=Q+sum_i sum_(k=1)^m_i A_(i,k)/L_i^k,              (2)

where A_(i,k)=c_(i,m_i-k).

For implementation verification, multiply (2) by D and compare every
rational coefficient with N. Each denominator division must have zero
remainder. This exact replay detects a wrong shift, index or multiplicity
before any ball integration.

## Single-pole moments

Set

    J_k(b,a)=integral_0^1 v^b/(1+a v)^k dv.

The base cases are

    J_0(b,a)=1/(b+1),
    J_1(b,a)=2F1(1,b+1;b+2;-a)/(b+1).                    (3)

To derive (3), expand the denominator for |a|<1, integrate its uniformly
convergent power series, and use
(b+1)_n/(b+2)_n=(b+1)/(b+n+1). Both expressions continue analytically
in a off the real ray (-infinity,-1]; on compact subsets the integral
and its derivatives are dominated by an integrable multiple of v^b.
The identity theorem gives (3) for every positive a. Its argument -a
is away from the principal hypergeometric branch cut.

For k>=2, differentiating v^(b+1)(1+a v)^(-(k-1)) gives

    d/dv[...] = (b-k+2) v^b/(1+a v)^(k-1)
                  +(k-1) v^b/(1+a v)^k.

The boundary value at zero vanishes because b+1>0, and the value at
one is (1+a)^(-(k-1)). Integration yields

    J_k=[(1+a)^(-(k-1))-(b-k+2)J_(k-1)]/(k-1).           (4)

No division by b-k+2 occurs. Integer values where that factor vanishes
are regular and are retained exactly.

Combining (2)--(4) gives

    I=sum_j Q_j/(b+j+1)+sum_(i,k) A_(i,k) J_k(b,a_i).

All coefficients and parameters are exact rationals. The hypergeometric
parameters satisfy the exact relations B-C=-1 and A+B-C=0. The documented
Arb interface can be told these relations to avoid treating rounded
parameter balls as independent near an integer difference. Increasing
precision controls cancellation in the finite final combination. A
finite result is accepted only when its output interval and required
accuracy checks pass.

## Independent calibration formulas

For b=0, elementary antiderivatives give
J_1=log(1+a)/a and, for k>1,
J_k=[1-(1+a)^(1-k)]/[a(k-1)]. For b=-1/2, the substitution v=x^2 gives

    J_1=2 atan(sqrt(a))/sqrt(a),
    J_2=atan(sqrt(a))/sqrt(a)+1/(1+a),
    J_3=3 atan(sqrt(a))/(4 sqrt(a))
                  +3/[4(1+a)]+1/[2(1+a)^2].

For b=1/2, polynomial division after the same substitution gives
J_1=2[1-atan(sqrt(a))/sqrt(a)]/a.
For two distinct simple poles,
1/(L_a L_d)=[a/L_a-d/L_d]/(a-d), giving another closed-form check.
Numerators divisible by D reduce to elementary power moments and check
exact cancellation of all principal parts.

Additional signed moments at the actual two campaign scales are compared
with the independently derived finite-panel binomial method in
../multiscale_moments/PROOF.md. That comparison keeps its explicit remainder.
It supplies a different integral algorithm for those instances; it does
not by itself prove the general identity, whose argument is given above.

## Evidence and limits

Code, exact fixture inputs, actual runtime, complete reconstruction flags
and containing intervals are retained under code/ and verification/.
The proof is written before execution. Independent peer review remains
OPEN until separately recorded. Any later use for a candidate must bind
its exact source and field algebra, verify endpoint powers and include
every required cross term and angular mode.
