# Decimal endpoint conversion must preserve enclosure

Status: the declared endpoint property of the retained numerical certificate is REFUTED. The formulas and underlying ball computations are not refuted.

## Exact claim

The file retained in `sources/theoremE_constants_arb.json` labels its decimal strings as rigorous upper and lower bounds for the constants in the finite rational-parameter theorem. Its generator computes an Arb endpoint and then formats that endpoint to a smaller number of significant decimal digits with the radius omitted.

The claimed property is that a declared lower endpoint is no greater than the exact real constant, and a declared upper endpoint is no smaller than that constant.

## Independent check

The script `code/decimal_bound_audit.py` reads the decimal strings as exact rational numbers. It independently recomputes each constant with exact rational input, exact continued fractions, and Arb at 512 bits, using the formulas proved in topic 22. It subtracts each declared endpoint in the appropriate direction. A strictly negative interval for the resulting safety margin disproves the claimed endpoint.

Of the 49 declared endpoints, 21 are independently confirmed by a strictly positive safety margin, 16 are refuted by a strictly negative margin, and 12 cannot be separated from equality by this interval comparison. Some of the last group are exact rational constants; their classification does not affect any refutation.

For example, for the extracted Candidate profile at the stored exponent, the declared upper endpoint

\[
  A_{\rm up}=13178349.58647113629214680
\]

is below the actual constant by more than \(1.20\cdot10^{-18}\). The declared radius upper endpoint \(8060282572610030\) is below the actual radius by more than \(2.18\). Both comparisons are strictly separated by the independent balls. The error is small relative to the constants but invalidates the asserted enclosure.

The issue follows directly from rounding to nearest after taking an endpoint: the rounding error can exceed the original interval radius and can have either sign. Calling `upper()` before that conversion does not preserve the upper-bound property.

## Repair

Retain an enclosing ball with its radius, serialize exact dyadic endpoints, or explicitly round decimal endpoints outward. For a positive scale \(10^d\), the rational

\[
 10^{-d}\left\lceil 10^d\,\operatorname{upper}(A)\right\rceil
\]

is an upper bound when the endpoint and ceiling are computed with certified directions. The corresponding floor of a lower endpoint is a lower bound. Topic 22 already supplies the safe strict integer bounds \(A<87214\) and \(A<13178350\) for the two stored-parameter profiles.

## Dependencies and scope

The dependencies are the exact formulas and input extraction in topics 02 and 22 and the enclosure guarantees of the executed Arb arithmetic. The evidence retains both source files, their hashes, every declared decimal, every independent ball and every comparison. This is an audit of numerical certificate serialization. It changes neither the convergence theorem nor the valid integer bounds.

## Repaired serialization

The numerical experiments supplied a new generator that converts exact dyadic endpoints with explicit decimal ceiling and floor. The independent repair audit retains the new source and output separately in `repair/`, leaving the refuted historical snapshot intact. It checks 63 declared directions, including the new integer upper and radius lower bounds: 62 are strictly separated in the correct direction, none are refuted, and one is an equality unresolved by direct interval subtraction. The outward-conversion algorithm itself preserves endpoint direction, including at equality. The repaired single-sine and raw Candidate upper bounds are `87213.989478538511` and `13178349.586471136293`; the repaired raw Candidate radius upper bound is `8060282572610032.190`.
