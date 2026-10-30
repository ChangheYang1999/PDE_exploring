# Independent audit of rational-pole radial integration

Status: analytic identity CONFIRMED by the argument below; independent
arithmetic comparisons are recorded separately. Only the scalar primitive
is covered, not any candidate field or full-plane norm built from it.

## Statement

Let b>-1 be rational, N a rational polynomial, and
D(v)=product_i(1+a_i v)^m_i, with distinct positive rational a_i and
positive integer m_i. Repeated input scales are first combined. Then

    I=int_0^1 v^b N(v)/D(v)dv

is finite. Exact rational partial fractions followed by outward evaluation
of the single-pole moments encloses I. The empty product is allowed.
Separate terms with divergent endpoint powers are outside this statement.

## Partial fractions and independent reconstruction

The principal-part procedure in source/N4_PROOF.md is correct: after
polynomial division, the remainder is expanded at each pole in the local
coordinate z=1+a_i v. The other denominator factors have nonzero constant
term, so finite Taylor inversion gives the entire principal part. The
difference after removing all parts has no finite poles and vanishes at
infinity, hence is zero. The code then verifies the identity exactly after
multiplication by D. Its multiplicities are positive integers, equal scales
are merged before division, and every required polynomial division has
zero remainder.

The independent checker uses a different construction. If d=degree D,
use the polynomial coefficient vectors of

    D(v)v^j, 0<=j<=degree N-d,
    D(v)/(1+a_i v)^k, 1<=k<=m_i,

with the first list empty if degree N<d. Their number is
max(d,degree N+1). These vectors are linearly independent: dividing a zero
combination by D, each principal part must vanish at its own pole; the
remaining polynomial then vanishes. They form a basis of the polynomial
space of the indicated dimension. Exact rational Gaussian elimination
therefore gives the unique partial fractions. Multiplying the computed
answer by D and comparing every coefficient checks the reconstruction.
This algorithm does not use the peer's local Taylor expansions.

## Independent single-pole moments

For every positive integer k,

    J_k(b,a)=int_0^1 v^b(1+a v)^(-k)dv
       =2F1(k,b+1;b+2;-a)/(b+1).                      (1)

For |a|<1, expand (1+a v)^(-k), integrate each absolutely convergent
term, and use (b+1)_j/(b+2)_j=(b+1)/(b+j+1). Both sides extend analytically
to the connected a-plane cut along (-infinity,-1], so the identity theorem
gives (1) at every positive a. Equivalently, the defining Euler integral
of this hypergeometric function gives the same formula directly.

The peer computes only J_1 by (1), then obtains higher moments from

    J_k=[(1+a)^(1-k)-(b-k+2)J_(k-1)]/(k-1).            (2)

Differentiate v^(b+1)(1+a v)^(-(k-1)); its derivative is
(b-k+2)v^b/(1+a v)^(k-1)+(k-1)v^b/(1+a v)^k. The zero boundary term
vanishes because b+1>0. Integration proves (2). In particular, no division
by the possibly zero quantity b-k+2 occurs.

The independent checker evaluates (1) directly for every k, rather than
using (2). Its hypergeometric parameters have exact integer differences
B-C=-1 and A+B-C=k-1. The documented bc and abc flags therefore apply;
they preserve these exact relations when rational parameters are enclosed
by rounded balls. The same outward-arithmetic library is a shared trusted
component, while the partial-fraction algorithm and higher-moment path are
independent.

Polynomial parts integrate as sum_j Q_j/(b+j+1). Finite outward additions
of these terms and the principal parts enclose I. Cancellation may widen
the result but cannot invalidate containment; the checker requires finite
intervals, positive accuracy and overlap with both the peer result and
its stored independent elementary/panel comparison. Additional fixtures
include resonant b-k+2=0 and a near-endpoint b=-999/1000. These checks
support implementation correctness and do not replace the analytic proof.

## Scope

The frozen source hashes, all fixture inputs, reconstructed coefficients,
actual runtimes, precision and comparisons are retained. Subsequent uses
for candidate010 still need verified field differentiation, correct
endpoint cancellations, angular products and all cross terms. No scalar
calibration alone proves a candidate-level residual norm or existence.
