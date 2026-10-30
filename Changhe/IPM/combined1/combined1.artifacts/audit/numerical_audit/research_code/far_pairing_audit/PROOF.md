# Full residual pairings at large radial probe indices

## Exact statement and inputs

Fix candidate C1-N1-007-d2w-j7-e2bal and its independently audited
canonical potential at c=4076476460239181/2251799813685248. Put
r2=x2+y2, S=1+r2, t=r2/S, v=1/S, gamma=1/c and delta=1-gamma.
Let R=-partial_y Delta chi, u=(-chi_xyy,chi_xxy) and
F=(cX+u).grad R-R. For a nonnegative integer K set

    phi_K=r v2 t^K sin(theta),
    I_K=int_(R2) F phi_K dX.

All coefficients in chi are exact rationals from the immutable snapshot.
The stored Cartesian first-sine residual projection is bound to that
snapshot and to its independently audited complete residual construction.
It includes every background angular-frequency pair contributing to
sine1. This result computes containing intervals for I_K at a prescribed
finite list of K, without replacing F by an asymptotic model or cutting
off the integration radius. It compares these intervals with the
finite homogeneous model used by the frozen N1 far_weak record. A
comparison of pairings alone gives no necessary correction distance,
full residual norm, inverse bound, or existence statement.

## Whole-plane identity and two finite recurrences

The complete projection has the exact form

    Pi_1 F=r sum_ell v^(ell delta/2) P_ell(t) sin(theta),

with ell>=1 and rational polynomials P_ell. The projection audit proves
this identity by Cartesian differentiation and exact trigonometric
products, and this audit compares it coefficientwise with the complete residual cache, after checking the source hash and its assembly certificate.
Sine orthogonality on the full circle gives pi. Changing from r to v,
using r dr=-dv/(2v2) and r2=(1-v)/v, gives

    I_K=(pi/2) sum_ell int_0^1
             v^(ell delta/2-1) (1-v)^(K+1) P_ell(1-v) dv.  (1)

Every term is integrable because ell delta/2>0 and K+2>0. The
reference is smooth at the origin. There is no angular or radial
quadrature and no interchange of an infinite expansion with an integral.

Put b=ell delta/2, P(t)=sum_j p_j t^j, and
P(1-v)=sum_j q_j v^j. Exact polynomial composition checks that these
are two representations of the same rational polynomial. Formula(1)
can then be evaluated in either of the following finite ways:

    sum_j q_j B(b+j,K+2),
    sum_j p_j B(b,K+2+j).                                (2)

Starting from B(b,K+2)=Gamma(b)Gamma(K+2)/Gamma(b+K+2), the first
recurrence multiplies by(b+j)/(b+K+2+j); the second multiplies by
(K+2+j)/(b+K+2+j). Each ratio is positive. Both identities follow
from Gamma(z+1)=z Gamma(z) for positive z. Exact rational inputs are
converted to outward Arb balls, and every operation encloses its true
value. Agreement between the endpoint recurrences checks the algebra
and cancellation; Arb and Gamma are common trusted dependencies.
Large K is a scalar parameter, not the degree of a constructed
polynomial. No coefficient array of length K is created.

At the small indices already independently checked by the projected
residual probe calculation, require containment overlap with its I_K.
Require more than150 relative bits for every nonzero final pairing and
both endpoint recurrences. Tiny values or cancellation alone do not
establish their sign; the containing interval must exclude zero.

## Independent asymptotic coefficients and the finite model

For r>1 set z=r^-2. The exact first-sine expression becomes

    sum_ell r^(1-ell delta) (1+z)^(-ell delta/2)
                                      P_ell(1/(1+z)).

Since P is finite, its coefficient at z^q is

    a_(ell,q)=sum_j p_(ell,j) binom(-ell delta/2-j,q),
    e_(ell,q)=1-ell delta-2q.                             (3)

The generalized binomial recurrence is exact over the rationals. Each
series converges for |z|<1, and termwise Cartesian differentiation was
already justified in the underlying field audit. Retain the finite
q<=3 sectors satisfying the frozen cutoff e>=-7 and compare their
exponents and first-sine amplitudes to the N1 floating table. This
comparison establishes which model was evaluated, with explicit
floating conversion errors. It never identifies that finite model with F.
Compute also a_(1,4), and compare exactly with the coefficient obtained
independently from the j0 potential by N4-195. Higher potential
coefficients cannot alter q<=3. The finite residual branch range has
no collision between the e_(1,4) exponent and another ell, as checked
in195. Thus a nonzero a_(1,4) is an actual omitted residual sector.

Let F_tr=sum a_(ell,q) r^e sin(theta) over this finite list, using only
the first sine coefficients because other harmonics pair to zero.
For every listed K with K+(e+3)/2>0, its full-radius pairing is

    I_tr(K)=(pi/2) sum a_(ell,q)
                  B(K+(e+3)/2,(1-e)/2).                 (4)

This follows by the substitution r2 and the standard beta integral.
All beta parameters are checked positive. The finite power model may
be singular at the origin, but this specified pairing remains integrable
when those conditions hold. Its interior contribution is part of(4).

Evaluating(1) and(4) separately therefore encloses the actual global
pairing error E_K=I_K-I_tr(K), including the exterior remainder and
any artificial interior contribution. A relative error |E_K|/|I_K|
is reported only when the denominator interval excludes zero. When
I_tr is nonzero, |I_tr|/sum |individual model terms| quantifies
cancellation within the finite model. Neither quantity is a spatial
convergence radius or an upper estimate of an omitted field norm.
An exact total error at a finite K does not prove a uniform error bound
for all larger K or identify a global maximizing probe.

## Provenance and scope

Bind the exact canonical source, compressed projection, projection
construction report, previous small-index pairings, N4-195 coefficient
record, this proof and code, and the frozen N1 table/code/publication.
Keep exact reconstructed sectors in JSON. The proof is written before
execution. New candidate pairings and errors remain OPEN until an
independent peer checks them. Existing analytic and numerical results
are referenced with their hypotheses, and no optimizer or foreign code
is executed.
