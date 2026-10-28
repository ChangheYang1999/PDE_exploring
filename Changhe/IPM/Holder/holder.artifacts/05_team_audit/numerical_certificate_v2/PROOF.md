# Audit of the revised polar-cell certificate

## Exact claim and scope

Let 0<alpha<1. Write [f]_alpha for the Euclidean homogeneous Holder
seminorm on R^2. Use the normalized real operators and the compact-test
extension proved in ../../01_setup/PROOF.md. The polygonal distance witness
in ../structured_witness/PROOF.md has [f]_alpha<=1 and vanishes at both
unit-separated evaluation points. Thus any rigorous lower bound for its
increment I is a lower bound for both C_alpha and D_alpha.

The revised numerical method in source/certify_lb.py is an outward
interval enclosure of I under the parameter restrictions and mesh choices
of the reported polygon runs. It changes the earlier audited method in
../numerical_certification/PROOF.md only as detailed below. That earlier
proof supplies the domain decomposition, omitted-region estimates, exact
local contribution, first-order fallback and kernel derivative bounds.

The polyline approximation of the curved zero set is also an admissible
zero set. The additional geometric reasoning below validates its feature
pruning and nearest-point test for queries with both coordinates at most
10^300 in absolute value. This restriction is needed because the source's
ray bounding box has the finite artificial endpoint 10^300. Every reported
run has outer radius at most 10^40. A future unrestricted implementation
should replace that box by the actual unbounded quadrant.

## Stable kernel identity

In coordinates z=(X,Y) with poles 0 and e_1, set

    A=X^2+Y^2, B=(X-1)^2+Y^2,
    N=A(3X^2-Y^2)-2XA-4X^3+4X^2-X.

Direct polynomial expansion gives

    (X-1)A^2-XB^2=N.

Consequently

    K_xy(z-e_1)-K_xy(z)=YN/(pi B^2 A^2).

This is an exact identity away from the poles. It combines the cancellation
before interval evaluation. An independent calculation in centered complex
coordinates w=X-1/2+iY gives the same density as

    -Im(w/[pi(w^2-1/4)^2]).

The source therefore changes conditioning without changing the integral.
The verification script checks the polynomial identity symbolically and
compares all three formulas with Arb at 2000 independently chosen points.

## The tighter distance Hessian

For distance d to a line, segment or ray, away from the set and from the
transition between interior and endpoint projection, d is either the
absolute value of an affine function or Euclidean distance to one fixed
vertex. In an interior regime the only nonzero eigenvalue of D^2(d^alpha)
is alpha(alpha-1)d^(alpha-2). In a vertex regime the radial and tangential
eigenvalues are respectively

    alpha(alpha-1)d^(alpha-2), alpha d^(alpha-2).

Thus the operator norm is at most alpha d^(alpha-2), since 0<alpha<1.
For f=2^(alpha-1) sigma d^alpha the bound is

    ||D^2 f|| <= 2^(alpha-1) alpha d^(alpha-2).

This improves the safe earlier triangle-inequality factor 2-alpha. The
first derivatives agree at an interior/endpoint transition: both gradients
point from the same nearest point to the query. They are locally Lipschitz.
Hence the almost-everywhere Hessian bound gives the usual Taylor remainder
along segments that cross those transitions.

For a finite polygonal union, a unique nearest point throughout a ball
implies the same conclusion there. Partition by the finitely many segment,
ray and vertex projection regimes. At each transition, uniqueness makes
the nearest point, and therefore the distance gradient, agree. The same
uniform derivative bound holds along any line segment in the ball, by
piecewise integration and continuity. This establishes the C^(1,1) Taylor
estimate required by the centroid rule. No differentiability across a
medial axis is asserted; such cells use the first-order fallback.

## Exact centroid rule

For an annular sector with radial endpoints r_1,r_2 and angular half-width
h, its centroid is on the bisector at radius

    r_bar=(2/3)(r_2^2+r_1 r_2+r_1^2)/(r_1+r_2) * sin(h)/h.

This is the earlier formula after exact factorization of differences of
powers. The squared distance to a corner with radius r is

    (r-r_bar)^2+4r r_bar sin(h/2)^2.

For angular width at most pi, the greatest distance is at an angular
endpoint and then, by convexity in r, at a radial endpoint. Both corner
expressions therefore give a valid enclosing radius. The integrated
second moment is

    M_2=(2h)(r_2^4-r_1^4)/4-area*r_bar^2.

If H bounds the Hessian of kf on all centroid-to-cell segments, the
integral lies in area*(kf)(centroid)+[-HM_2/2,HM_2/2], since the linear term
integrates to zero. Interval evaluation contains the exact centroid and
moment, and taking an upper endpoint for M_2 is safe.

## Complete geometric pruning for the curved polyline

The vertices are binary floating-point numbers interpreted subsequently
as exact dyadic coordinates. They need not lie on the analytic zero curve:
every such continuous graph, together with its reflected copies and the
horizontal axis, gives the signed-distance Holder witness. Its sign is
constant in each complementary component. The first vertical segment and
all later heights at least y_1 ensure the exact local two-line geometry in
a disk of radius y_1/2 about a pole.

A floating nearest-feature proposal gives a candidate only. The exact
Arb distance to that feature provides an upper bound. A different feature
is removed only if its certified bounding-box distance lower bound exceeds
that upper bound. Segment boxes contain their whole segment. For the
positive ray, and queries within the stated coordinate range, clipping the
unbounded positive quadrant at 10^300 leaves the same nearest point of that
quadrant to the query; its distance remains a lower bound for distance to
the ray. Taking the minimum over the surviving exact distances is valid.

For a ball of radius r centered at c, let D=d_Z(c). A feature with distance
strictly larger than D+2r at c cannot be nearest at any point of that ball:
its distance there is greater than D+r, while d_Z there is at most D+r.
The candidate enumeration uses this rule with enclosing intervals.

If one feature survives, its convexity gives uniqueness. Suppose exactly
two survive, and they are adjacent features sharing a vertex V. If either
has another finite endpoint, that endpoint belongs to a third feature
(the next segment, the ray or the horizontal axis at a pole). If that outer
endpoint were a nearest point anywhere in the ball, the third feature would
also survive. Hence under the two-candidate hypothesis distinct nearest
points can only be interior projections on the two rays issuing from V.
The equal-distance locus for two such interior projections is the positive
internal bisector ray in the direction e_1+e_2, where e_1,e_2 are the unit
vectors from V into the features. On the opposite bisector both projections
are behind V and the common nearest point is V. The other angle bisector
cannot have both projections positive. Thus, if the ball misses the
positive internal bisector ray, its nearest point is unique throughout.
The source tests this disjointness using an outward distance enclosure.
This proof needs the complete candidate list and endpoint incidence. It
would be false for two arbitrary isolated finite segments.

Finally, the sign routine checks every graph segment whose height range
may intersect the queried height interval, and includes the final ray when
needed. Their union encloses all possible boundary abscissae. An uncertain
sign returns both signs, so it cannot exclude the true witness value.

## Reproducibility and numerical status

The source snapshot and exact symbolic checks are hashed in verification/.
The independent layer-cake method uses a different one-dimensional exact
formula for the same polygonal witnesses. Its recomputed enclosures are
compared to every reported polygon enclosure before individual numbers
receive a verification verdict. This proof does not turn a floating
quadrature observation into a certified operator norm.
