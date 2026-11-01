# Certified Fourier mass by distance to the diagonal

Status: finite interval method and certificates. No all-order assertion is made.

## Exact definitions

At delta=2/3 and leading density sin(theta), use the canonical zero resonant stream constants. For a density coefficient at order n and physical sine frequency m=2j+1 define s=m+3-2n/3. For a stream coefficient m=2j define s=m+2-2n/3. At each positive log degree q, partition the modes into |s|<=q/4, q/4<|s|<=q, and |s|>q. At q=0 partition instead into |s|<=2 and |s|>2.

The mass in a band is the sum of absolute physical sine coefficients. Its fraction is that mass divided by the entire column mass, when the latter is positive. The factorial-column winner is the nonconstant q maximizing q! times the column mass. Its location is certified by strict interval comparison with every other nonconstant column. This is also the winner of the ratio to the constant-column mass when that denominator is positive.

## Certificate argument

Every saved coefficient is an exact dyadic center and nonnegative dyadic radius representing a previously audited512-bit Arb enclosure. Unpack it exactly and use640-bit outward-rounded interval arithmetic for absolute values, band sums and fractions. Membership is decided by integer inequalities: put S=3(m+offset)-2n, offset3 for density and2 for stream; compare4|S| with3q and |S| with3q. Thus band membership has no floating-point uncertainty. At degree0 compare |S| with6.

Since the bands are a disjoint exhaustive partition, their mass sums enclose the full column mass. Dividing a nonnegative band enclosure by a strictly positive total gives a certified enclosure of its fraction. The summed fractions must contain1. No interpretation of the mass distribution is used to prove the earlier coefficient enclosures.

## Scope

These are finite data, conditional on the correctness of the coefficient enclosure recurrence already independently checked in topics21,33,45 and65. They help distinguish whether an observed factorial-column maximum is concentrated near the small Poisson divisor. They do not prove a uniform band estimate, an asymptotic growth law, or convergence of the infinite generalized series. Source hashes, per-column intervals and winner comparisons are retained in verification/.

## First retained certificate

The certificate20261031T054453Z/checks.json audits82442 packed coefficients at n240,250,260. Every column partition passes and every nonconstant factorial-column winner is strictly certified. The winning density columns are42,44,46. Stream winners are1,44,46; at240 the stream has not yet switched to an interior winner.

At250,q44 the fraction in |s|>q is .9998631423076869802650140966 +/-2.63e-29 for density and .9966503370060595191185081096 +/-3.38e-29 for stream. At260,q46 it is .9998716996807454575149473747 +/-2.28e-29 for density and .9976627889032786908358021552 +/-2.99e-29 for stream. Thus these particular interior maxima are dominated by modes outside the linear small-divisor band. This is a finite observation, not an exclusion of future near-diagonal growth. Actual audit0.9437104864045978 seconds.

The signed refinement20261031T054613Z/checks.json separates s<-q and s>q. At260,q46 the upper-side fractions are2.102959497452888750114425160e-10 +/-2.93e-38 for density and1.715049278056388680094559397e-9 +/-3.55e-37 for stream. The lower-side fractions are .9998716994704495077696584997 +/-3.43e-29 and .9976627871882294127794134751 +/-2.44e-29. Thus the off-band mass is overwhelmingly on the low-frequency side at this order and column. The reported largest-mode field is a comparison candidate; only the band fractions and column winners are certified by the stated procedure. Actual signed audit1.1997319152578712 seconds.

## Update 2026-10-31T05:51:53Z: orders 263, 265, 268, 270

The certificate 20261031T055117Z audits 124,911 balls. At 270 the density and stream winners both have q=48. Their off-band fractions are .9999092749295313734210596256 +/-1.86e-29 and .9987275611775679547212824275 +/-2.56e-29. The upper-side fractions are only 6.267793930486288097364651008e-11 +/-2.10e-39 and 5.175934696190340297499491954e-10 +/-4.40e-38. Thus the same low-frequency concentration persists at these selected finite orders. Actual audit time 1.4160367120057344 seconds.

## Whole-stream partition by the smallest scalar Poisson shift

A separate diagnostic groups the entire plain stream mass, summed over all log columns, by the smallest absolute shift of each stream frequency. At order n and frequency2j define

    d_(n,j)=min(|2-2n/3+2j|, |2-2n/3-2j|).

For each value d<=4, sum the absolute coefficients over every q and j with d_(n,j)=d. Put all remaining coefficients in one complementary band. This is a disjoint partition of the plain stream norm N_n. Its fractions therefore sum to1. The stream's zero-frequency channel is identically zero and is omitted. Multiplying all distances by3 reduces every membership test to exact integers.

For comparing adjacent orders, the near mass A_n is the sum over d_(n,j)<=2/3. The identity

    N_n-N_(n-1)=(A_n-A_(n-1))+((N_n-A_n)-(N_(n-1)-A_(n-1)))

separates changes in that specified band and its complement. A change in the fraction alone does not imply that the absolute band mass increased. A finite list of changing fractions also does not prove monotone or asymptotic concentration. In particular, this diagnostic compares moving frequency bands, not a fixed Fourier subspace.

The interval implementation is code/stream_mode_share_audit.py. It compares the peer's rounded midpoint table only after allowing its printed rounding tolerance. The source enclosure uncertainty is kept separately by Arb. Prepared code does not count as an executed certificate; completed checks are recorded in the chronological verification ledger (not included).

## Density-index correction identified 2026-10-31T09:03:48Z

The peer band implementation passes offset3 to an expression `2*k+offset-n*delta` for density. Since the physical density frequency is2k+1, this evaluates m+2-n*delta. The documented density distance m+3-n*delta requires offset4. The independent integer audit above already uses offset4 and needs no repair. The peer stream expression2j+2-n*delta matches its documented distance.

To isolate the discrepancy without modifying the source checkpoint or peer code, the comparison script `code/density_band_offset_audit.py` recomputes both offset3 and offset4 from the identical frozen density balls at order320. It compares the offset3 fractions with the printed three-decimal table using a half-unit rounding tolerance. If those comparisons pass while offset4 excludes the printed intervals, the discrepancy is in partition membership rather than coefficient generation. The script stores the original source, original table, exact source hash, both interval fractions and every comparison result. Executed results are recorded separately in the verifier ledger.
