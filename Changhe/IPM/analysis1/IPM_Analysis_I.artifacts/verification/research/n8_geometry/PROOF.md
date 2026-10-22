# Exact disc geometry for the N8 source certificate

Status: proof established below; arithmetic checks pending. This topic concerns geometric coverage only. It does not accept the derivative enclosures or resolve the Bernstein and coordinate domain pairing in topic82.

## Statement and notation

Let p belong to the exact dyadic bracket [p_-,p_+] copied from topic82, let P=(p,0), and let R=3 delta, where delta is one of the exact decimal rationals 0.0165,0.05,0.1,0.2. The fine run has intended delta_max=0.0165 and the full run has intended delta_max=0.2. The density is odd in y; its stream function is odd in y under the canonical inverse. Thus each absolute Cartesian derivative and each derivative Frobenius norm is invariant under reflection y to -y. Both discs are contained in x>0, so only 0<=theta<pi/2 is needed.

The exact radial partition is the rational partition already checked in topic31 and topic69, with 7810 endpoints. This topic extracts its N8 subarray and compares every endpoint to the binary64 midpoint/radius input in cert_green.npz. It also recreates the geometry portion of the frozen N8 algorithm, without invoking that producer. The exact binary64 operands, including the floating values of 3*delta_max and 3*delta*(1+1e-6), are distinguished from the rational target radii.

The following are sufficient for complete coordinate coverage of a disc: its radial interval [p_- - R,p_+ + R] lies inside the selected exact radial partition, the least possible angular cap is at least asin(R/p_-), and every coordinate cell excluded by the producer is disjoint from the closed disc for every p in the bracket. Each condition will be verified separately by interval arithmetic. A pass does not prove that the polynomial bound paired with a coordinate cell applies on that cell.

## Radial and angular coverage

For X in the disc, the triangle inequality gives p-R<=|X|<=p+R. Since p>R, elementary right-triangle geometry gives |arg X|<=asin(R/p). One can also derive this by minimizing |r(cos theta,sin theta)-(p,0)| over r>=0: its minimum is p |sin theta| for |theta|<pi/2. The larger bounds p_- - R and p_+ + R and asin(R/p_-) cover every allowed center.

Each exact cell endpoint lies in its supplied midpoint/radius interval. The recreated midpoint-radius difference yields h_up at least the true radial log width. For every true point t=t_a+u, 0<=u<=h_up, there is k in {0,...,K-1} with k h_up/K<=u<=(k+1)h_up/K. The coordinate ball enclosing the two endpoint balls therefore contains t. Consecutive exact radial cells abut. Consecutive angular node balls contain their common node, hence their hulls cover all angles between zero and the least permitted final node. Exponentiation is increasing, so exact endpoint enclosures prove radial coverage or exhibit its failure.

For the fine run's larger delta rows, X=P+(2 delta,0) lies strictly inside B_(3delta)(P). If its radius lower bound p_-+2delta exceeds the largest possible coordinate radius of the entire fine grid, these rows cannot cover their stated discs. This is a statement about the actual coordinate cover once the exponential upper bound has been proved, and strengthens the metadata-only statement in topic82. It does not establish that a printed derivative upper bound is numerically false.

## A directed test for excluded cells

Consider a coordinate box with r in [a,b], theta in [alpha,beta], where 0<a<=b, 0<=alpha<=beta<pi. Let p_0=(p_-+p_+)/2 and epsilon=(p_+-p_-)/2. For fixed r and p_0, the squared distance is r^2+p_0^2-2 r p_0 cos theta. Its theta derivative is 2 r p_0 sin theta>=0, so its minimum is attained at alpha. At that angle the minimizing radius is

 r_c=clamp(p_0 cos alpha,a,b).

Completing the square gives the exact minimum

 d_0=sqrt((r_c-p_0 cos alpha)^2+(p_0 sin alpha)^2).

By the reverse triangle inequality, the distance from any point of the box to (p,0), for any p in the bracket, is at least d_0-epsilon. Therefore a directed lower enclosure greater than R proves disjointness. This stable formula avoids the subtractive cancellation in r^2+p_0^2-2 r p_0 cos alpha. Interval evaluation of clamp is valid because clamp is monotone in its input. Every omitted box must pass; a single undecided box leaves the filter unaccepted.

The producer converts Arb lower/upper values to nearest binary64 values. Those converted numbers need not be outward endpoints. The independent disjointness test uses the exact endpoint rationals of the Arb coordinate and angular balls, then re-evaluates exponentials and the stable distance formula in independent interval arithmetic. Thus it does not assume that nearest conversion is directed. The recreated floating exclusion mask is compared with every published ncells count, as a consistency check on the frozen geometry.

## Dependencies and scope

The partition's mathematical connection to the exact trial is the existing audited topic31/69 dependency. Reflection symmetry follows from the specified finite sine expansion and the canonical inverse. The check uses only exact scalar data extracted into JSON; it does not copy large coefficient tables into code. The numerical run must preserve all source hashes, endpoint comparisons, omitted-cell counts, strict lower gaps, and directed fine-grid counterexamples. Arb and mpmath.iv checks use independent formulas where practical. No flow-field, local coefficient, inverse or existence certificate follows from geometry alone.
