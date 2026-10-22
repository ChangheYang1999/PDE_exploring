# Full modal Green boundary linkage to the canonical archive

## Exact statement and scope

The exact normalized modal_v2 density, its canonical inverse and scalar
normalization are those of topics15,21,31 (modal_repair, modal_green, middle_residual). On every original spline
span [a,b], the accepted canonical archive of topic31 encloses the degree7
polynomials H_j(t), j=0,...,261, with H_261=0, and the scaled moments
I_n(a), J_n(b), n=1,...,261. The polynomial coordinate is
x=t-(a+b)/2. These are imported whole-plane canonical moments, not
values from the numerics lane's Green array. Their recurrences and
finiteness have been audited; this result does not independently
reintegrate all original spans or the two infinite tails.

The density and stream function conventions are

 rho(r,theta)=r^3 sum_(j=0)^261 H_j(log r) sin((2j+1)theta),
 psi(r,theta)=r^4/2 sum_(n=1)^261 [J_n(log r)-I_n(log r)]sin(2n theta),
 I_n'=-(2n+4)I_n+H_(n-1),
 J_n'=(2n-4)J_n-H_n.

The numerics artifact cert_green.npz stores dimensional A_n and B_n
at7810 exact child boundaries t_i of7809 closed middle cells. Its
parent array and outward coordinate balls define the same exact
partition as topic31. We shall verify at every boundary and every
mode that the exported midpoint/radius intervals contain the true
canonical values

 A_n(t)=exp(4t)[(H_(n-1)(t)+H_n(t))/2-2n I_n(t)],
 B_n(t)=exp(4t)[2n J_n(t)-(H_(n-1)(t)+H_n(t))/2].          (1)

Each value is recomputed by two interval methods described below. Both
use the accepted canonical archive; they use different propagation
identities, polynomial coordinates and interval libraries. Neither
method reads the target A/B intervals until making the comparison.
A pass requires containment, not just overlap. Disjointness refutes
the exported claim if the input/proof audit passes. Overlap without
containment leaves it OPEN. No partial run certifies omitted values.

The result establishes boundary membership for A/B only. It does not
establish membership of the saved density polynomial arrays T, all
radial Taylor models, any angular range bound, a whole flow field,
compactness, a global inverse or a decisive IPM endpoint.

## 1. Derivation of the dimensional identities

Writing m=2n, differentiation of r^3 H_j(log r) in x gives the sine
forcing of -Delta psi:

 F_n=[(4-m)H_(n-1)+(4+m)H_n+H'_(n-1)+H'_n]/2.

This follows directly from partial_x=cos(theta)partial_r-
(sin(theta)/r)partial_theta and the sine product identities. With
S=(H_(n-1)+H_n)/2 the proposed A=e^(4t)(S-mI) satisfies

 A'=e^(4t)[4S+S'-m(4I+I')]
    =e^(4t)[4S+S'-m H_(n-1)+m^2 I]
    =-m A+e^(4t)F_n.

Similarly B=e^(4t)(mJ-S) satisfies B'=mB-e^(4t)F_n.
The canonical endpoint definitions fix the integration constants,
so these A and B are precisely the dimensional Green integrals.
In particular this derivation neither differentiates a sampled
velocity nor introduces an arbitrary homogeneous solution.

## 2. Method A: finite polynomial particular solutions, Arb

For the constant-coefficient equation y'+kappa y=f(x), with f a
polynomial of degree d and kappa nonzero, define p by the finite
backward recursion

 p_(d+1)=0,
 p_j=[f_j-(j+1)p_(j+1)]/kappa, j=d,...,0.

Coefficient comparison proves p'+kappa p=f exactly. Thus for any
anchor x0 and any x on the same span,

 y(x)=p(x)+exp[-kappa(x-x0)] [y(x0)-p(x0)].               (2)

For I use kappa=2n+4, f=H_(n-1), x0=a-(a+b)/2.
For J use kappa=4-2n, f=-H_n, x0=b-(a+b)/2.
When n=2 in J, kappa=0: take p_0=0 and p_(j+1)=f_j/(j+1),
then use y=p+y(x0)-p(x0). This is an exact polynomial primitive,
not division by an interval containing zero. Values of H and p are
evaluated by Horner in the original midpoint coordinate. All input
ball widths propagate through (2). Cancellation can widen a ball;
it cannot justify throwing away its radius. Arb rounds every
operation outward and every result must be finite.

## 3. Method B: convolution power moments, mpmath.iv

For y'(u)=lambda y(u)+f(u), 0<=u<=L and
f(u)=sum_(j=0)^7 c_j u^j, variation of constants gives

 y(u)=exp(lambda u)y(0)+sum_j c_j u^(j+1) Phi_j(lambda u),
 Phi_j(z)=integral_0^1 exp[z(1-v)]v^j dv
         =j! sum_(l=0)^infinity z^l/(j+l+1)!.            (3)

The series follows by the uniformly convergent exponential series
on the compact unit interval and the exact beta integral
integral_0^1(1-v)^l v^j dv=j!l!/(j+l+1)!.
Truncating after l=N has absolute remainder at most

 j! |z|^(N+1)/(j+N+2)! /[1-|z|/(j+N+3)],                (4)

provided |z|<j+N+3. This is the geometric bound on the remaining
successive-term ratios, all bounded by the displayed first ratio.
For z=0 the sum is exactly1/(j+1). For u=0 no moment is needed.
Every condition and the tail are evaluated with outward intervals;
a failed ratio or finiteness check aborts. Signed alternating sums
are enclosed by adding the symmetric absolute tail, never by an
unjustified alternating-series assumption.

For I set u=t-a, lambda=-(2n+4), f(v)=H_(n-1)(a+v).
For J set u=b-t, lambda=4-2n, f(v)=H_n(b-v).
The latter equation follows by differentiating J(b-u), including
both sign changes. The coefficients c_j are obtained by exact
binomial translation and, for J, reversal of the midpoint polynomial,
with interval input coefficients. Method B evaluates H at t using
these translated endpoint polynomials. Thus it does not use the
particular polynomial or exponential cancellation of Method A.
Formula(1) completes the reconstruction in this second engine.

## 4. Coverage, directed comparisons and saved evidence

Original spans are indexed0,...,1557 and have positive integer child
counts. For a span with first child index q and count c, its assigned
boundaries are q,...,q+c-1 at a+(b-a)j/c for0<=j<c. The final right
endpoint b of the last span is included once. Thus exactly7810
boundaries are covered without duplication. At shared original knots
we use the right-hand span; continuity of the density and canonical
moments makes that value equal to the left limit. The finite endpoint
extension conventions have already been verified in topic31.

Every NPZ binary64 midpoint and nonnegative radius is converted to its
exact dyadic rational. The containment comparison uses exact endpoints
of the computed ball and the exact interval[mid-radius,mid+radius].
All NPZ entries and all input/output ball endpoints must be finite.
Zero-radius target intervals are accepted only for exactly equal point
values. An overlap flag cannot pass the final gate.

The disk limit prevents storing millions of repeated long interval
strings. For each completed original span, store the exact geometry,
counts of every outcome and both methods, the worst containment
margin with its full exact endpoints, and a hash of all streamed
value records in a fixed order. Store every failed comparison in full.
The full checker source and all input hashes are retained, so the
stream is reproducible. The independent methods run through every
entry. A separate final audit checks exact coverage, all counters,
source/input hashes, current file sizes, selected fresh enclosures,
absence of partial records and a complete footer before acceptance.

Partial runs and queue preparation remain OPEN. Successful equality
or overlap between the two computed intervals is diagnostic only;
canonical enclosure follows from each method's own formulas and
input certificate. The old selected180-entry check is a separate
cross-check, not a substitute for full coverage.
