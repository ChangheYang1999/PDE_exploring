# Stable Green moments and modal range bounds

## Statement and scope

All variables are real. Let n>=1 be an integer, a a fixed radial logarithm,
and let fhat(s) be continuous on [0,h], h>0. Write F(s)=exp(2a+2s)fhat(s).
For the radial Green components used in this project put

    Ahat(s)=exp(-2(a+s)) A_n(a+s),
    Bhat(s)=exp(-2(a+s)) B_n(a+s),
    alpha=2n+2, beta=2n-2.

Suppose their endpoint values Ahat(0), Bhat(h) are enclosed rigorously and
F([0,h]) is enclosed in a real interval I. Then the ranges are contained in

    Ahat([0,h]) subset hull(Ahat(0),
             exp(-alpha h) Ahat(0)+(1-exp(-alpha h)) I/alpha),
    Bhat([0,h]) subset hull(Bhat(h),
             exp(-beta h) Bhat(h)+(1-exp(-beta h)) I/beta)   (n>1),
    Bhat([0,h]) subset hull(Bhat(h), Bhat(h)+h I)             (n=1).

Here hull means the smallest closed interval containing all indicated
intervals, and interval arithmetic is outward. These statements do not
require a primitive divided by a small exponent. They can be applied on
subcells, provided their boundary values are enclosed independently.

For integer p>=0 define the entire real function

    phi_p(z)=integral_0^1 exp(zu) u^p du.

For every integer N>=1 and |z|<=M,

    |phi_p(z)-sum_{j=0}^{N-1} z^j/(j! (p+j+1))|
        <= exp(M) M^N / (N! (p+N+1)).                         (1)

Consequently integral_0^h exp(lambda u)u^p du equals
h^(p+1) phi_p(lambda h), including lambda=0. The analogous damped left
moment is exp(-lambda h) times this expression. Formula (1) gives rigorous
ball evaluation for small lambda without subtracting large primitives.

There is also a uniform half-line estimate. Let beta>0, gamma>0 and s<=0.
For every integer p>=0,

    |exp(beta s) integral_s^0 exp((gamma-beta)u) u^p du|
        <= exp(min(beta,gamma)s) |s|^(p+1)/(p+1).             (2)

For any eta<min(beta,gamma), the supremum after multiplication by
exp(-eta s) is at most

    1/(p+1) * ((p+1)/(exp(1)*(min(beta,gamma)-eta)))^(p+1).  (3)

These are sufficient bounds, not optimal ones. They remain bounded when
gamma approaches beta. For a polynomial sum_p c_p u^p one sums the
right sides with |c_p|. The hypotheses beta>0 and gamma>0 matter for (3).
The n=1 constant at minus infinity is treated separately below.

## Green convention and derivation

The forcing mode is f_n(t)=exp(2t) fhat(t-a). By definition

    A_n(t)=exp(-2nt) integral_{-infinity}^t exp((2n+2)v)f_n(v)dv,
    B_n(t)=exp(2nt) integral_t^infinity exp((2-2n)v)f_n(v)dv.

Whenever these integrals exist, differentiation gives

    A_n'=-2n A_n+exp(4t)fhat(t-a),
    B_n'= 2n B_n-exp(4t)fhat(t-a).

Thus

    Ahat'=-alpha Ahat+F,
    Bhat'= beta Bhat-F.                                    (4)

Variation of constants, forwards for Ahat and backwards for Bhat, gives

    Ahat(s)=exp(-alpha s)Ahat(0)
                 + integral_0^s exp(-alpha(s-u)) F(u)du,
    Bhat(s)=exp(-beta(h-s))Bhat(h)
                 + integral_s^h exp(-beta(u-s)) F(u)du.    (5)

For a nonnegative kernel its normalized integral against F belongs to I.
For alpha>0 the first expression therefore has the form

    d Ahat(0)+(1-d)q/alpha,
    d in [exp(-alpha h),1], q in I.

For fixed endpoint value and q it is affine in d; its extrema occur at
an endpoint of the d interval. Taking interval hulls proves the first
range claim. The second follows identically with h-s in place of s. If
beta=0, (5) is Bhat(h)+(h-s)q, whose extrema also occur at endpoints of
h-s and of I. The same reasoning works when endpoint values are themselves
intervals because one also takes their extrema.

The modal fields in the numerical scripts are

    Pe_n=(Ahat+Bhat)/2, Qe_n=(Bhat-Ahat)/2.

Equation (4) yields the useful identities

    Pe_n'=2n Qe_n-2Pe_n,
    Qe_n'=2n Pe_n-2Qe_n-F.                                 (6)

These equations give derivative enclosures from rigorous Ahat, Bhat and F
ranges. Higher derivatives follow by differentiation when F is smooth.
This avoids differentiation of a badly conditioned primitive expansion.

## Proof of the moment estimate

Taylor's theorem for exp(zu) about zero gives an error bounded by
exp(M)(M u)^N/N! for 0<=u<=1. Multiply by u^p, integrate, and use
integral_0^1 u^(p+N)du=1/(p+N+1). This proves (1). Integrating the polynomial
part proves the stated series coefficients. Substitution u=hv proves the
finite moment formula. Multiplication by exp(-lambda h) proves the left
moment formula. All statements include z=0; no division by z is used.

For z in a real ball, the same estimate holds uniformly with M any upper
bound of |z|. Every arithmetic operation in a numerical enclosure must be
outward; a nearest floating conversion of an interval hull is insufficient.

## Proof of the half-line bounds and the constant mode

For u in [s,0], if gamma-beta>=0 then exp((gamma-beta)u)<=1.
If gamma-beta<0 it is at most exp((gamma-beta)s). In either case the
integrand's exponential prefactor is bounded by exp(min(beta,gamma)s).
The integral of |u|^p on [s,0] is |s|^(p+1)/(p+1), proving (2).
Putting v=-s and c=min(beta,gamma)-eta>0 reduces the weighted supremum to
sup_{v>=0} exp(-cv)v^(p+1)/(p+1). Its unique positive maximum is at
v=(p+1)/c, proving (3).

For an inner forcing term c exp(e s)s^p, the scaled B equation uses
beta=2n-2, gamma=e+2. The exact anchored contribution is

    c exp(2a) exp(beta s)
                 integral_s^0 exp((gamma-beta)u)u^p du.

The exponent difference is e+4-2n. The n=27 matched correction has
that difference close to zero, but beta and gamma close to52, so (2)-(3)
are uniformly well-conditioned.

When n=1, beta=0. If gamma>0, the full component has a finite constant
Bhat(-infinity), and the correct expression after subtracting it is

    Bhat(s)-Bhat(-infinity)
          = -exp(2a) sum_p c_p integral_{-infinity}^s
                                      exp(gamma u) u^p du. (7)

The remaining primitive uses powers of 1/gamma, not 1/(gamma-beta) near
zero. For the current inner modes gamma>=2. Its constant is fixed by
the exact central-strain normalization, not by discarding a small
nonzero floating constant. The leading density has only forcing mode
n=1 at exponent e=0; these facts are established in topics50 and52.

## Original-data check and numerical evidence

The code reads bi from the original read-only NPZ, checks its SHA-256,
and computes the exact resonance difference

    bi+4-54 = 75/70368744177664.

It tests the unit p=6 inner contribution at s=-1 using both the primitive
and (1), then verifies the same result at higher precision. It also checks
finite-cell hulls against high-precision point enclosures for a signed
polynomial forcing. Point samples are implementation checks only; (4)-(5)
prove the entire-cell range theorem. Evidence is in evidence/check.json.

No global IPM coefficient certificate, matrix entry or inverse norm is
claimed here. Applying these methods to the full coefficient arrays is a
separate computation in the numerics team.

## Dependencies

Only differentiation of convergent modal Green integrals, variation of
constants and elementary Taylor estimates are used. The identification of
the actual inner exponent and normalized constant uses the exact modal
object checked in topics04,50 and52. The range result itself is independent
of those data.
