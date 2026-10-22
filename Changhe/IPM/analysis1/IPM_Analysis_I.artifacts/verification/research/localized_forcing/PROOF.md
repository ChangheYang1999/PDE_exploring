# Conditional localized forcing estimate and independent certificate audit

Written 2026-10-21T07:39:14.613756+00:00 before this topic's checking code. Status OPEN. This proof
establishes a conditional analytic reduction, not acceptance of the numerics
lane's advertised constants. The trial is the normalized finite angular
modal reconstruction, not the original exponential X3 field.

## Statement, notation and hypotheses

Let delta=33/2000, P=(p,0), with p in the exact source bracket from topic76.
Let g be the true stationary residual of the fixed canonical modal trial,
locally W^{4,infinity} on a neighborhood of the closed disk B_{9delta/4}(P).
Let S(v)=1-126v^5+420v^6-540v^7+315v^8-70v^9 for 0<=v<=1, extended as1 forv<0
and0 forv>1. Set tau(X)=S((|X-P|-7delta/4)/(delta/2)) and f=tau*g.
The sine symmetry makes g odd in y and tau even in y.
Use the unitary Fourier transform and N_lambda,s(f)^2=
int(lambda^2+|xi|^2)^s |fhat(xi)|^2 dxi, lambda>0, s=31/10.

A finite family of measurable polar cells C_j must cover supp f up to null
sets. Overlap is allowed. Suppose certified numbers a_j>=area(C_j) and
F0_j,F1_j,FL_j,FL1_j,FL2_j bound respectively |f|, |grad f|,
|Delta f|, |grad Delta f|, |Delta^2 f| on C_j. Vector bounds mean Euclidean
norms. The following sufficient upper bounds hold:

 I3=sum_j a_j[lambda^2(lambda^2 F0_j+FL_j)^2
                    +(lambda^2 F1_j+FL1_j)^2],
 I4=sum_j a_j[lambda^4 F0_j+2lambda^2 FL_j+FL2_j]^2,
 N_lambda,3(f)<=sqrt(I3), N_lambda,4(f)<=sqrt(I4),
 N_lambda,31/10(f)<=I3^(9/20)*I4^(1/20).                  (1)

A cell may instead denote only its upper-half-plane portion and a_j bound
twice its area. This uses the symmetry of the absolute values of the
relevant derivatives; it must not omit any positive-measure portion.

## Proof of the reduction

S'=-630 v^4(1-v)^4, so0<=S<=1 and its first four derivatives vanish at both
endpoints. Thus the radial cutoff is C4: it is constant near P and has no
radial singularity there. The product f is compactly supported W4,infinity,
hence H4. No distributional surface terms arise at the cutoff joins. Local
W4,infinity of the residual must separately follow from the actual trial
regularity; no C6 assertion at the coordinate origin is required here,
since this disk is separated from that origin.

Plancherel gives
 N_lambda,3(f)^2=lambda^2 ||(lambda^2-Delta)f||2^2
                        +||grad(lambda^2-Delta)f||2^2,
 N_lambda,4(f)^2=||(lambda^2-Delta)^2 f||2^2.
Triangle inequalities pointwise, followed by integration over the covering
cells, give I3 and I4. Overlap only increases a nonnegative sum. Holder
with conjugate exponents10/9 and10 in Fourier space gives
 N_lambda,31/10(f)^2<=N_lambda,3(f)^(9/5)*N_lambda,4(f)^(1/5).
Taking a square root and using I3,I4 gives (1). This is an upper bound, not
an equality or an a posteriori closing condition.

## Leibniz formulas, with all terms

For two smooth functions tau and g, direct differentiation gives
 Delta(tau*g)=tau Delta g+2grad tau dot grad g+g Delta tau,
 grad Delta(tau*g)=grad tau Delta g+tau grad Delta g
 +2D2tau grad g+2D2g grad tau+grad g Delta tau+g grad Delta tau,
 Delta^2(tau*g)=tau Delta^2g+g Delta^2tau+2Delta tau Delta g
 +4grad tau dot grad Delta g+4grad g dot grad Delta tau
 +4D2tau:D2g.
These follow by applying the scalar product rule successively to each
summand of Delta(tau*g). They hold almost everywhere for the stated
functions by approximation on this compact disk. Use Frobenius norm for
the Hessians in the contraction bounds.

For rho=|X-P|>0 and tau=t(rho), radial differentiation in dimension2 gives
 |grad tau|=|t'|, Delta tau=t''+t'/rho,
 ||D2tau||F^2=(t'')^2+(t'/rho)^2,
 |grad Delta tau|=|t'''+t''/rho-t'/rho^2|,
 Delta^2tau=t''''+2t'''/rho-t''/rho^2+t'/rho^3.
This uses the radial and tangent eigenvalues t'' and t'/rho of D2tau.
On support of a nonzero derivative, rho>=7delta/4, so all divisions are
bounded. The scalar triangle bounds used by the source follow from these
identities. Positivity and signs of S itself can sharpen bounds but are
not needed for this reduction.

## Distinct finite numerical obligations

To accept a numerical conclusion one must independently verify:
A. The modal coefficients, canonical Green data and all radial derivative
Taylor model enclosures, including every truncation and rounding error.
B. Cartesian differentiation from the complete polar jet and all angular
Taylor remainders. Differentiating a remainder bound without a derivative
bound is forbidden; the source must use separate jets for every order.
C. Bivariate products and Bernstein coefficient enclosures, under the
actual floating evaluation model or by independent interval computation.
Topic72 only establishes a conditional dot-tree theorem, not the actual
BLAS implementation. Positive-sum allowance formulas also need proof.
D. The same spatial cell must be used by the derivative suprema, distance
bounds, cutoff ranges and area. Any rounding shift between these cells
requires a covering argument or extra remainder.
E. All cutoff polynomial ranges must cover the exact argument intervals.
Converting Arb endpoint bounds to float with round-to-nearest is not by
itself outward rounding. Calling a standard noninteger power and multiplying
by a guessed relative allowance is not by itself a proved library bound.
F. The merged parts have identical parameters and source versions, cover
exactly the required radial cells and all included angular subcells, have
no omitted support, and their nonnegative sums round upward.
G. Every advertised decimal ceiling must be at least the independently
validated enclosure endpoint. Componentwise bounds cannot be relabelled
as vector norms without the appropriate combination.

The current source has a possible domain mismatch in D: Bernstein phi
subcells start at -w_up, whereas geometry starts at theta1. The exact
angular half-width is dtheta/2<=w_up. These are shifted by
w_up-dtheta/2. This identifies a proof obligation, not a demonstrated
violation of any output bound. Source cutoff endpoint conversion and
fractional powers in E also require a finite audit or a repaired producer.

## Dependencies and scope

The analytic statement depends only on its displayed hypotheses, elementary
product rules, Plancherel, Holder and the proved radial formulas. Application
to the IPM trial depends on the independent certificates for that trial and
its regularity. The forthcoming code will first check exact dyadic aggregate
arithmetic, published ceiling direction, cutoff coverage and source hashes.
It will not label a full residual certificate CONFIRMED merely because two
floating totals agree. The full PDE inverse, global forcing, nonlinear
remainder, normalization neighborhood and closing inequality remain OPEN.
