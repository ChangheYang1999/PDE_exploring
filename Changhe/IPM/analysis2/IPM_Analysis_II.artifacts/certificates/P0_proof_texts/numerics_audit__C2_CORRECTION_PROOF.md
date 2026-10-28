# Audit of corrected derivative-summary rounding and tensor aggregation

Status: CONFIRMED aggregation and corrected-summary audit at256bits. This is an aggregation audit conditional on the saved scalar component enclosures, not a new independent full-plane field certificate.

## Exact statements

For each saved cell and derivative orderd, suppose b_(i,d-i)>=|partial_x^i partial_y^(d-i)rho| on that cell. Then the ordered Cartesian derivative tensor satisfies

    |D^d rho|_F <= (sum_(i=0)^d binom(d,i)b_(i,d-i)^2)^(1/2).

For velocity sum the same squares over both components. This follows directly from the definition of the ordered tensor: the mixed derivative with i x-indices occurs binom(d,i) times. It requires no new field evaluation. Exact rational arithmetic on the binary64 saved bounds and outward ball square roots give a valid combined upper bound whenever the component bounds are valid.

For an origin square[-r0,r0]^2 and weight omega(r)=(1+4r^2)^(2/5), the correct radial maximum is(1+8r0^2)^(2/5). On a polar cell with outer radiusr_hi it is(1+4r_hi^2)^(2/5). The squared upper bounds may be compared first, before taking any root.

## Why finite component bounds can give a nonfinite computed norm

An interval enclosure of a component is not its nonnegative upper bound. In ball arithmetic the product of a ball with itself may lose correlation. A ball enclosing[0,1] can consequently produce a product enclosure with a negative lower endpoint. A square-root call on that enclosure may return nonfinite even though every component remains bounded. Treating each saved scalar upper bound as an exact nonnegative number avoids this dependency loss.

This explains a possible source of nonfinite tensor entries; the audit checks the actual finite component records before attributing any missing cell to a field remainder failure. The exact code path uses abs(o[name]) balls and multiplies them as independent factors in frob. The combined upper bounds below remain conditional on the correctness of the underlying component box calculations.

## Corrected summary audit

The corrected summary is checked against all40081 unique saved records. The audit verifies every count, advertised six-significant-digit upper bound, and the origin-square correction factor by256-bit arithmetic on exact rational versions of the saved inputs. It separately checks the new all-component aggregation and identifies whether it fills the previously nonfinite tensor entries. No repaired summary is written into the numerical work.

## Verified aggregation

Every six-significant-digit bound and every finite/nonfinite count in certSups_131_summary2.json passes the independent check. Its saved origin correction factor exceeds the exact required ratio, which lies near1.0000399948007039007. Thus the specific rounding and origin-square issues of V083 are repaired in that summary, within its stated field-by-field finite-cell scope.

All individual scalar component upper bounds are finite on all40081 records. Combining them as exact nonnegative rational numbers yields the following sufficient bounds on the entire saved cell cover, conditional on those component enclosures:

| field | unweighted upper | omega-weighted upper | formerly missing tensor cells recovered |
| --- | --- | --- | --- |
| D rho | 10.30040 | 218.71159 | 0 |
| D2 rho | 3.74723 | 12.35714 | 2955 |
| DU | 1.14601 | 20.52772 | 278 |
| D2U | 1.78951 | 6.09589 | 11917 |

The cover reaches radius101.778502590813; a full-plane assertion still requires the exterior argument. The tensor bounds need no new field evaluation, but do not independently validate the component enclosure algorithm. They are weaker than the separate verified Bernstein bounds used in the current inverse theorem, and do not alter that theorem's constants.
