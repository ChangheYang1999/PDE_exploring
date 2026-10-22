# Exact source constraints of three saved scaling projections

Written UTC: 2026-10-21T20:42:11.400749+00:00. This is the standalone proof for topic168. It precedes the checker.

## Statement and scope

Fix the 1953 exponential-polynomial function columns of the immutable M16/s16
family named in evidence/source_binding.json, its two exact dyadic join points
b_- and b_+, and the three saved v2 projection coefficient vectors named there.
Interpret every stored binary64 scalar as the exact rational number it represents.
The family is identified by all function-column labels and angular indices, the
count1953, and its independently saved join points. This identifies the explicit
mathematical interpretation below. The new projection files do not store the
join points or a hash of their column pickle. We do not attest which pickle an
unobserved historical execution read merely because these labels match.

For NJ in{0,1}, define C_NJ on original coordinates x by the left-minus-right
value traces (NJ=0), or value and first-t-derivative traces (NJ=1), at both joins,
separately for m=0,...,15. Only the first1953 function coordinates contribute.
The next coordinates KP and TAU, and all16 extra free-tail coordinates if
present, are zero columns of this SOURCE-DEFINED matrix. This last convention
is precisely the finite source recipe, not an assertion that their physical
traces vanish. The three vectors have1955,1955,1971 coordinates respectively.

The certificate, if its exact computations pass, gives every coordinate of C_NJ x
as a rational number, an independently recomputed identical rational, and a
strict outward decimal enclosure of its absolute value. A nonzero coordinate
proves x is not in the exact kernel of this explicit matrix. No conclusion
about an ideal exact projection, a physical trace of the complete field, a
Sobolev norm, or the IPM inverse follows from that alone. We do not extend the
orthogonal-projection interpretation of topic165 to these floating vectors.

## Notation and exact trace argument

A column of angular index m has pieces
  f(t)=exp(alpha (t-a)) P(t-a),  a<=t<b,
where P(s)=sum_{j=0}^d c_j s^j has ascending coefficients. On an inner half-line
(-infinity,b), the anchor is b instead. Outside its pieces the function is zero.
All supports within each function column have disjoint interiors. At each of
the two selected joins there is at most one piece ending and one beginning.
These facts and alpha*s=0 at every contributing endpoint must be checked from
all1953 columns. Consequently exp(alpha*s)=1 exactly at those endpoints.
The left trace contribution is P(s), and the derivative contribution is
alpha P(s)+P'(s). Subtract the right contributions. This proves each exact
matrix entry T_{i,j,nu}; linearity gives
  (C_NJ x)_{m,j,nu} = sum_{i<1953: mode(i)=m} x_i T_{i,j,nu}.
Every sum is finite and all operands are rational, so rational arithmetic is
an exact proof of its value. The defining zero columns remove all later
coordinates from this source functional, regardless of their nonzero values.

For the alternate computation expand every monomial directly and use
  (d/dt)(exp(alpha s)c_j s^j)
    =exp(alpha s)c_j(alpha s^j+j s^(j-1)),
with the j=0 derivative term omitted. The product rule gives the same trace
without Horner recursion. Reversing the summation order by matrix row rather
than by column supplies a second computation. Use python Fraction plus NumPy
binary64 decoding for one, and python-flint fmpq plus independently decoded
NPY/IEEE754 words for the other. The frozen pickle remains a shared input;
its permitted data classes, actual scalar types, supports and dimensions are
checked. No producer function is imported or executed.

## Rounding and normalization

For any exact q, n=floor(10^30 |q|) gives
  n/10^30 <= |q| < (n+1)/10^30.
Both independent calculations check this strict upper inequality. Arb256 and
mpmath.iv100 additionally enclose the exact rational maximum of each vector;
their directed endpoints are compared to that rational directly. Their
intervals need not contain one another. The maximum is attained in this finite
row set, so a recorded maximizing row proves its location and size.

The inspected floating source forms a diagonally scaled constraint matrix,
normalizes its rows, and uses an SVD nullspace, followed by x=Qy in original
coordinates. For an EXACT positive diagonal D, row scaling and C D z=0 with
x=D z are equivalent to Cx=0. This algebra does not make the rounded stored
x exactly null. The reported source join_residual concerns its normalized
basis matrix, not the raw exact Cx computed here; the two quantities must not
be compared as though they had the same units or vector normalization.

## Dependencies and limits

The density, Poisson law, residual and trial norm are not used. Topics147/148
supply previously inspected source conventions and frozen columns; topic165
supplies immutable projection files and the energy/distance caution. Their
verdicts and all inherited files are rehashed before and after the computation.
The present proof rederives the traces and checker recomputes them independently.
No inferred small repair bound is claimed, especially not for the full physical
field. Internal spline joins, exact physical cancellation with KP/TAU, and any
finite-section-to-global comparison remain outside this result.
