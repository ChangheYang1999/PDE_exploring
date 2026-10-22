# Restricted domains and precise scope of the finite checks

Added2026-10-21after the actual Opus5.5 review. Read with PROOF.md.

Fix any p in the exact binary64 endpoint interval saved as x_star_bracket.
All geometric assertions below hold simultaneously for every such p, and
all conditional physical-model hypotheses must likewise hold uniformly
for that p. The residual g is odd in y on a neighborhood of the entire
support, including its reflection. It suffices that the physical p lies
in this interval; the proof does not replace p by its floating midpoint.

Let t_i be the exact shared knot between adjacent radial cells. The physical
parent is t_i<=t<=t_(i+1) and |theta-theta_c|<=w. Its local coordinate
sigma=t-t_i lies in[0,h], with h>=t_(i+1)-t_i. The fine rectangle with
indices ks,kp is

 [ks hk,(ks+1)hk] x [-w+kp wk,-w+(kp+1)wk].

Assign to a row only the intersection with that physical parent and with
theta>=0. Because64hk>=h and8wk>=2w, these intersections cover the entire
upper part of the parent. The exact knots are shared between neighbors;
no gap results from restriction. The centers theta_c and w cover the full
angular range. Topic115's exact disk-coverage proof establishes that these
parents cover B_(3delta)(P), uniformly over the p interval. Thus their
restrictions cover the cutoff support. The radial enclosing boxes in the
new geometry programs are supersets of the restricted radial intervals;
the angular intervals are explicitly intersected with the parent and
theta>=0. Their area bounds cover the restricted sets and their reflected
copies. A larger box or duplicate boundary can only increase the sum.

A block has hb=32hk and wb=4wk. Its shifts are
 a_s=bs hb, a_p=-w+bp wb+wb/2.
The exact coordinate relation is sigma=sigma'+a_s, phi=phi'+a_p.
The block polynomial can be bounded on[0,hb]x[-wb/2,wb/2]. The old
remainder is invoked only on the intersection just specified. The same
restriction is retained through addition, multiplication, recentering,
series composition and Bernstein conversion. These operations use a
supremum of a polynomial on a larger rectangle, which bounds it on the
restricted set. A remainder valid only on that set remains sufficient
for each pointwise product estimate. Nothing asserts a physical remainder
bound on the overhang. The same argument applies to a trigonometric
Taylor remainder valid for |phi|<=w.

For q=(x-p)^2+y^2, the model's coefficient radii include the uncertainty in
p, and the scalar radius is part of the bound on q-c0. In the inspected
source, sup_crude returns an inflated sum of coefficient magnitudes plus
self.r; the latter is not omitted. Soundness of those coefficients and
radii is a separate hypothesis. The condition used for the binomial
series must bound the true q on the restricted block, including every
remainder and coefficient uncertainty. Comparing a polynomial on the
whole block only weakens the resulting bound.

An inside or transition regime is accepted only if its distance interval
is contained in the corresponding true regime. Both interval geometry
engines and an exact rational regime pass check that implication for the
saved rows. The upper half-plane convention and reflection are legitimate
because P=(p,0), tau is even in y, and g is odd in y. Straddling or failed
series blocks use the separate pointwise construction. No polynomial
continuation of S is asserted to equal the cutoff outside its transition.

The current frozen source is v2.2; the saved merged data is v2.1. The exact
calculus comparison binds to the current source expressions, and the
finite summation binds to the historical saved data. Those are separate
results. Neither is an attestation of historical execution. The individual
c0, Umax, xr and tail values and the composed coefficient arrays were not
saved. The maximal recorded ratio and maximal tail do not identify their
operands and cannot by themselves validate each series computation.
A subsequent replay can certify its own saved operands, but such a replay
must not silently attest the old arrays. The scalar tail, full composed
model arithmetic and physical forcing remain OPEN here.
