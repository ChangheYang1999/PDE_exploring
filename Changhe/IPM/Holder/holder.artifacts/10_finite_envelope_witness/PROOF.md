# Finite cone envelopes as rigorously admissible witnesses

## Statement and scope

Use the real homogeneous Holder seminorm and singular-integral conventions in
`../01_setup/PROOF.md`. Fix 0<alpha<1, finitely many points p_i in R^2 and real
numbers v_i. No consistency assumption on the data is required. Define

$$U(z)=\min_i(v_i+|z-p_i|^\alpha),\qquad
L(z)=\max_i(v_i-|z-p_i|^\alpha),\qquad f(z)=\tfrac12(U(z)+L(z)).$$

Then [f]_alpha<=1. If the data satisfy |v_i-v_j|<=|p_i-p_j|^alpha,
f(p_i)=v_i for every i. If the data are invariant under (p,v) to (-p,-v),
f is centrally odd. If they are also invariant under ((X,Y),v) to
((X,-Y),v), f is even in Y and odd in X.

These statements convert arbitrary finite numerical data into an admissible
function. A numerical objective at the nodes is not its operator value.
The cell and endpoint estimates below give a way to certify that value.
No numerical lower bound is asserted in this note.

## Admissibility and symmetry

The function z to |z-p|^alpha has Holder seminorm at most one, by the triangle
inequality and |a^alpha-b^alpha|<=|a-b|^alpha for nonnegative a,b.
Adding a constant, changing sign, or taking a finite maximum or minimum
preserves that bound. Averaging U and L proves [f]_alpha<=1.

Under the stated consistency inequalities, each term defining U at p_j is
at least v_j and the j-th term equals v_j. Likewise every term defining L
is at most v_j and its j-th term equals v_j. This proves interpolation.
Without consistency, the seminorm proof still applies; the actual values
at the poles must be evaluated instead of being assumed.

Central data symmetry gives U(-z)=-L(z), so f(-z)=-f(z).
Reflection symmetry gives U(X,-Y)=U(X,Y) and the same identity for L.
Central oddness implies |f(z)|<=2^(alpha-1)|z|^alpha.

## A certified local variation bound

Let q be any point, let eta>=0, and let d=min_i |q-p_i|. On the closed ball
B(q,eta),

$$|f(z)-f(q)|\le\epsilon(q,\eta),$$

where epsilon=eta^alpha always, and if eta<d it may be replaced by

$$\epsilon(q,\eta)=\min\{\eta^\alpha,
\alpha\eta(d-\eta)^{\alpha-1}\}.$$

Indeed every cone has gradient of norm alpha |z-p_i|^(alpha-1) away from
its vertex. On this convex ball that norm is at most
alpha(d-eta)^(alpha-1). Each cone is therefore Lipschitz there with that
constant; the finite maxima, minima and their average have the same
constant. This argument does not differentiate a minimum across a switch
of its active cone.

For a measurable cell E contained in B(q,eta), a real integrable density k,
and any certified values of m=int_E k and t>=int_E |k|, one consequently has

$$\left|\int_E k(z)f(z)\,dz-mf(q)\right|\le t\epsilon(q,\eta).$$

The same formula applies to f-c for any constant c. Interval enclosures of
m and f(q), together with an upper bound for t epsilon, give an enclosure
of the cell integral. Exact integration of a cancellation term before
applying this estimate avoids an artificial error from an arbitrary
additive constant.

## Pole and tail estimates for the axis functional

Let x=(1/2,0), y=-x and

$$\nu(z)=\operatorname{Re}\frac{z}{\pi(z^2-1/4)^2}
=K_{xx}(z-x)-K_{xx}(z-y).$$

Suppose f has the central and Y-reflection symmetries above. Then its
R_1^2 increment is

$$R_1^2f(x)-R_1^2f(y)=\operatorname{pv}\int_{\mathbb R^2}\nu f-f(x).$$

The integral is four times the integral over the first quadrant Q.
For 0<delta<1/2, the full contribution of the two pole disks, including
the smooth other-pole terms, has absolute value at most

$$E_{\rm pole}=
\frac{2a_2(\alpha)\delta^\alpha}{\alpha}
+\frac{\delta^2(1/2+\delta^\alpha)}{(1-\delta)^2},\qquad
 a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(2+\alpha)}.$$

For each own-pole term, subtract f at that pole. The exact angular bound
proved in `../02_upper_bounds/PROOF.md` gives a_2 delta^alpha/alpha for
each disk. On the x disk, central oddness and [f]<=1 give
|f(z)|<=|f(x)|+delta^alpha<=1/2+delta^alpha; the other kernel is bounded
by 1/(2pi(1-delta)^2). Its area is pi delta^2. The y disk gives the same
bound, proving the formula.

For any R>1/2, the contribution outside the midpoint disk B(0,R) has
absolute value at most

$$E_{\rm tail}(R)=
\frac{2^\alpha R^{\alpha-1}}
{(1-\alpha)(1-1/(4R^2))^2}.$$

Indeed |nu(z)|<=|z|/[pi(|z|^2-1/4)^2] and
|f(z)|<=2^(alpha-1)|z|^alpha. Polar integration and
(1-1/(4r^2))^-2<=(1-1/(4R^2))^-2 give the result.
If the compact first-quadrant region is cut instead at |z-x|<=R,
its omitted part, with its four symmetric copies, is contained in
|z|>R-1/2, so E_tail(R-1/2) is a safe bound.

Thus a certified lower enclosure J_low of four times the integral over
Q intersect {delta<=|z-x|<=R}, together with a certified upper enclosure
b for f(x), proves

$$D_\alpha\ge J_{\rm low}-E_{\rm pole}-E_{\rm tail}(R-1/2)-b.$$

All such lower bounds hold for the compact smooth test-class supremum
by the approximation theorem in the setup note. The finite node data,
all rounding rules, and all cell enclosures must be supplied before a
computed number may be called certified.

## Exact finite-tree evaluation

The minima, maxima and nearest-vertex distance can be evaluated without
scanning every vertex at every query. A tree node stores a rectangle
containing its vertices and their minimum and maximum values v_min,v_max.
If d_box is a certified lower bound for the distance of q from this
rectangle, then all its upper cones are at least v_min+d_box^alpha and
all its lower cones are at most v_max-d_box^alpha. Once evaluated vertices
give upper and lower candidate values U_* and L_*, the entire tree node
may be skipped if

$$v_{\min}+d_{\rm box}^\alpha\ge U_*,\qquad
v_{\max}-d_{\rm box}^\alpha\le L_*.$$

If the nearest distance is needed at the same time, also require
$d_{\rm box}\ge d_*$, where d_* is the current nearest candidate distance.
With interval data these comparisons use the adverse endpoints: a lower
bound must exceed the upper endpoint of the candidate it bounds below,
and conversely for upper bounds. The leaves are checked exactly by
outward ball arithmetic. Tree construction and traversal order may use
floating heuristics, because no node is discarded without these certified
comparisons. This proves that the final returned intervals enclose U(q),
L(q) and the nearest distance for the exact decimal input data.
