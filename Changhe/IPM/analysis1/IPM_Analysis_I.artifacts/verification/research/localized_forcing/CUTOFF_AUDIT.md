# Exact cutoff interval audit

Written before its checking code. For every saved distance bracket [d0,d1],
use the exact rational delta=33/2000 and form the exact sigma endpoints
(d0-7delta/4)/(delta/2), (d1-7delta/4)/(delta/2), clipped to[0,1].
No exported binary sigma endpoint is assumed outward. S is decreasing, so
S at the clipped lower endpoint bounds its absolute value from above.
If d1<=7delta/4, all cutoff derivatives are identically zero.

For j=1..4, polynomial differentiation and exact division factor S^(j) as
v^(5-j)(1-v)^(5-j) Q_j(v), with
Q1=-630;
Q2=-2520+5040v;
Q3=-7560+35280v-35280v^2;
Q4=-15120+136080v-317520v^2+211680v^3.
The factor v(1-v) is nonnegative, increases to1/4 at1/2, then decreases.
On any rational interval its maximum is obtained at an endpoint or at1/2.
A Bernstein bound of the polynomial Q_j on that interval gives a bound
on |Q_j|. Multiplying these two independent upper bounds is safe. Use
subdivision only to improve this estimate, not to assert sampled maxima.

For polynomial Q(v)=sum q_i v^i on[A,B], first rewrite v=A+(B-A)t.
Its coefficient of t^l is sum_{i>=l} q_i C(i,l) A^(i-l)(B-A)^l.
Its degree-n Bernstein coefficient at k is sum_{l<=k} c_l C(k,l)/C(n,l).
The Bernstein basis is nonnegative and sums to1 on[0,1], so max |b_k|
is a rigorous range bound. Arb evaluation of these exact rational formulas
or exact rational arithmetic must include every subinterval endpoint.

Multiply by(2/delta)^j to obtain radial derivative bounds T_j.
For inverse radii use the exact lower bound max(d0,7delta/4), never the
producer's round-to-nearest exported cutoff radius. Derive TL, TL1, TL2
and T2F from the proven radial formulas in PROOF.md. Each saved bound
must be at least the new independently proved upper endpoint. This is a
sufficient finite verification; failure would leave the saved bound OPEN,
not establish a false bound for the actual cutoff. Missing-support cells
are addressed by the separate geometry audit. This audit says nothing
about the residual fields or actual BLAS.

A sharper primary method uses all stationary points, rather than a product
bound on subdivisions. The only possible interior extrema of |S^(j)|,
other than zeros (whose absolute value is0), are zeros of S^(j+1).
Their complete lists on(0,1) are:
j=1: 1/2;
j=2: (7-sqrt(7))/14,(7+sqrt(7))/14;
j=3: (7-sqrt(21))/14,1/2,(7+sqrt(21))/14;
j=4: (1+e sqrt((15+d 2sqrt(30))/35))/2 for e,d in{-1,1}.
Indeed S2 has its single remaining linear factor, S3 its quadratic factor,
S4 has Q4=-15120(1-2v)(1-7v+7v^2), and
S5=-15120 P4(2v-1), P4(x)=(35x^4-30x^2+3)/8.
These identities can be verified by integer polynomial differentiation
and expansion. All roots are real, lie in(0,1), and their counts exhaust
the remaining degrees. Evaluate at the two exact endpoints and at every
root whose enclosing interval intersects the sigma interval. Evaluating a
root outside the interval is harmless; never omit an intersecting root.
Arb ball evaluation then proves a bound of each derivative on the entire
interval, without trusting the producer's16 rounded subdivisions.
