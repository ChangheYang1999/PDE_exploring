# Finite cell geometry audit plan

The domain assigned to a saved row is the intersection of its Bernstein
rectangle with the original radial spline cell, its parent Taylor-model
angular interval, and the upper half-plane. In local coordinates the
Bernstein rectangle is

 ks*hk <= sigma <= (ks+1)*hk,
 -w_up+kp*wk <= phi <= -w_up+(kp+1)*wk.

The angular centre is theta_c. Intersect phi with [-w_up,w_up] and theta
with [0,infinity). Intersect sigma with the actual spline-cell interval,
which is contained in [0,h_up]. Thus no Taylor remainder is used outside
its proved parent domain. Bounding a polynomial on a larger Bernstein
rectangle is harmless after restriction. Radial or angular overshoots do
not require extrapolation of a remainder.

Since KSUB*hk>=h_up and KP*wk>=2*w_up, these restricted rectangles cover
every parent cell in the upper half-plane. The parent radial cells are
required to cover B_{3delta}(P); the original canonical knot locations and
Taylor data are still inherited hypotheses of the full forcing audit.

The source uses slightly shifted angular rectangles for geometry. We do
not assume they coincide. For all106496 possible row indices, independently
bound the distances on the actual restricted Bernstein domain. A saved
row must have dmin no greater than the independently proved distance
lower bound and dmax no smaller than the distance upper bound. Its area
must exceed the independently computed area bound. A missing row must
be certified disjoint from the open support disk rho<9delta/4. This finite
check, if it passes, resolves the angular shift for this output regardless
of whether the producer's generic geometry explanation was sufficient.

For an angular interval0<=a<=b<pi/2 and r in[r1,r2], distance squared is
r^2-2rp cos(theta)+p^2. It increases with theta and is convex in r. At a,
its minimum is the sum of the squared distance of p*cos(a) from[r1,r2]
and (p*sin(a))^2. With interval p we use separately enclosing intervals in
this formula, which gives a safe lower bound. The maximum is bounded at
r1,r2 and b. Evaluate it in the stable equivalent form
(r-p*cos(b))^2+(p*sin(b))^2. Both-half-plane area is
(r2^2-r1^2)*(b-a). Nonnegative quantities are evaluated in Arb with exact
binary input rationals. All endpoint comparisons use exact Fractions.

The geometry audit also checks all native h and w power upper bounds
against exact rational powers. It does not validate any residual Taylor
coefficient or midpoint-radius matrix product. A later independent
interval method must cross-check the same distances and areas before a
final finite-geometry verdict is issued.

For finite radial coverage, reconstruct the exact 7810 knot points from
partition_exact.json and match the14 relevant points to their tb boxes.
The same exact point serves as the upper endpoint of one cell and the
lower endpoint of its neighbor. Prove exp(t_4096)<p_min-3delta and
exp(t_4109)>p_max+3delta. Prove theta_max>asin(3delta/p_min). These strict
inequalities cover the entire disk B_{3delta}(P) for every admitted P.
The parent angular centres are the exact dyadics theta_max(2q+1)/32;
w_up>=theta_max/32 covers both true parent endpoints. This closes the
finite spatial coverage assertion relative to the identified partition.
Canonical Green and residual Taylor data remain separate dependencies.
