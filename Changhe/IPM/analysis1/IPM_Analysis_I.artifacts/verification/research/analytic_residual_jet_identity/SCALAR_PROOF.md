# Literal scalar audit, separate from quadrature validation

For each of the four names in the copied full_g4.json, let S be the exact
binary64 number stored under norm2/name/all. The scalar reported as a norm
is sqrt(S). For the saved ratio let S=K2/F2, with F=eps-eps_t. All these
numbers are positive. They are literal scalars, not enclosures of integrals.
The two interval implementations use the exact rational input S and enclose
its positive square root. The chosen rational target interval [a,b] is also
checked independently by 0<=a<=b and a^2<=S<=b^2. Monotonicity of squaring
on nonnegative reals proves a<=sqrt(S)<=b without relying on either interval
library. The floating conversion only proposes a target; it cannot certify
it because the exact square inequalities must pass.

The absolute relative change between the two saved lobe Gauss results is
|S6-S4|/S4, computed exactly as a rational. These are changes in stored
squared norms, not norms. The part shares use saved positive squared-norm
entries as denominator. Their ratio interpretation is literal only; rounding
means a stored sum need not equal the exact sum of its stored parts.

No derivative evaluation, quadrature error or tail bound follows from these
scalar checks. In particular, the finite-annulus value near44.91 and ratio
near170.5 are not certified norms or inverse lower bounds. A future proof
must supply the field linkage, quadrature or complete integral enclosure,
and both omitted infinite tails. The existing derivative-row scalar sums
cannot yet supply this: their literal cover has gaps and physical linkage
remains open, as established in topics152 and153.
