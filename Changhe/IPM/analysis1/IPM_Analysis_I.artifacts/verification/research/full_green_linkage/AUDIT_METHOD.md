# Independent checks of the boundary computation

The claim and assumptions are those of PROOF.md and ADDENDUM.md.
These checks are diagnostic until the complete run is present. No
finite sample substitutes for the two complete propagation methods.

Before the whole run, manufactured polynomial solutions test each
propagator against exact rational values. Given a polynomial y of
degree at most7, take f=y'-lambda y and the exact endpoint y(0).
Variation of constants then gives precisely that polynomial at every
rational test point. Rates0,2,-2,-6,-518,-526 exercise the zero-rate,
growing and strongly decaying cases. Degree0 through7 and a signed
mixed polynomial exercise every coefficient. The reference values
are exact Fraction polynomial evaluations, independent of either
propagation algorithm. Tests also challenge nonfinite interval
endpoints and each directed comparison outcome.

For the final selected third-method check, write the anchored ODE
as y'=lambda y+sum_(j=0)^7 c_j u^j. Its Taylor coefficients obey

 y_0=anchor, y_(j+1)=(lambda y_j+c_j)/(j+1),

where c_j=0 for j>=8. This follows by direct coefficient comparison.
For K>=8 the omitted terms after degree K form an exponential-series
tail with absolute first term bounded by

 |y_K| u^K |lambda u|/(K+1).

Every subsequent term ratio is at most |lambda u|/(K+2). If this
number is below1, division by one minus this ratio bounds the entire
absolute tail. At u=0 the anchor is exact; at lambda=0 the solution
has degree at most8. Using K128 and Arb1024 gives a third propagation
identity with a complete tail. Endpoint polynomial translations use
an independent direct binomial sum from the imported midpoint
coefficients. The source code does not import the primary checker.
The exact input uncertainty is propagated in every coefficient.

The final artifact audit checks all1558 spans and7810 boundaries,
all counters, no failed record, exact continuity of the partition,
all selected fixture and input-hash sample indices, exact saved
endpoint comparisons, every source/input hash, the complete footer
and the stream-of-span-hashes digest. It recomputes each selected
entry by the third method and requires containment in the exact
NPZ interval and overlap with both saved complete-method enclosures.
The old180 selected enclosures are also compared. A third-method
failure does not override two passes; it leaves the claim OPEN for
investigation. The full two-engine source and its input archive are
retained so all omitted stream entries can be recomputed.
