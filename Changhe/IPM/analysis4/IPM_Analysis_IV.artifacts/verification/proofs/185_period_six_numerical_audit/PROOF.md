# Independent numerical audit of the period-six branches

Status: CONFIRMED for roots [1, 2, 3, 4, 5, 6] through 60; other branches require individual audits.

## Exact statement and hypotheses

Let delta=1/3,c=3/2, and f_1=sin(theta)+b_i sin(3theta), where b_i is one of the six real roots, in increasing order, of the degree-twelve first-obstruction polynomial154. The all-index response bounds155 and the integer-period theorem131 give its unique tuned pure series. The first true stream harmonic occurs at12; later harmonics occur at multiples of6.

The proposed independent signed Cartesian recurrence encloses every density and stream coefficient through60, including H60 determined by the obstruction at66. Coefficient overlaps test agreement with the separate numerical implementation. Selected norms through300 are finite source-bound interval extractions; the full nonlinear recursion beyond60 is outside this audit.

## Complete enclosure proof

Refine the certified rational isolating interval154 by exact sign-preserving bisection, and enclose the unique root in a ball. Start with the exact unit first harmonic and this enclosing third harmonic. Every Cartesian derivative, product, sum and inverse denominator in the recurrence is performed with directed interval arithmetic. Thus each computed coefficient encloses the unique exact coefficient, inductively. The input interval is never replaced by its midpoint.

At the first resonance12, the compatibility polynomial proves that the obstructed density coordinate is exactly zero. At each later resonance the earlier tuned harmonic cancels the obstruction. Require its ball to contain zero before projecting that known zero coordinate out. The other discarded coefficients are forced to vanish by S1 symmetry and the proved carrier bound, and their balls must also contain zero.

To determine H_n, compute two provisional continuations to n+6, setting the current harmonic to0 and1. By131 the resulting obstruction depends affinely on H_n. Their difference encloses its exact response sigma, which is nonzero by155. Perform H_n=-R/sigma only when the computed response ball excludes zero. This encloses the unique tuning parameter. Repeat this step also at60. Cartesian second derivatives independently check the Poisson equation for every computed stream coefficient.

Directed absolute values and summation enclose angular l1 norms; directed logarithm and exponential enclose their positive order roots. A source stream coefficient at its final resonant order is excluded when its free harmonic remains unset, although the density coefficient at that order is already determined. Every comparison is tied to source hashes and retained selected coefficient records. A finite norm-root table does not prove the convergence boundary of the infinite series.

## Planned evidence

Initial runs use3072-bit arithmetic, the exact polynomial and root intervals154, and the bounds155. Source checkpoints must contain at least300orders. The complete independent prefix, harmonic/response overlaps, operation counts, selected norm balls, coefficient archive hashes and real execution times will be retained. No numerical result is asserted here yet.

## Root 6 review, V355

At 2026-10-31T13:51:38+00:00, The 3072-bit independent prefix through 60 passes 48744 Poisson coefficient checks, 5928 ordered products, 18 provisional continuations and nine compatibility projections. All 3660 density and 3720 stream coefficients overlap the separate numerical implementation, including H_60 determined by the obstruction at 66; all nine harmonic/response pairs pass. Independent archive replay confirms 120 prefix norm overlaps, the reported source norms and their order roots. The source density norm root at 300 is [4.8900118988353610883663012329881070941667010222651 +/- 1.69e-50], with relative norm radius [3.60443746512123907019327560501e-208 +/- 4.31e-238]. The untuned final stream coefficient at 300 is excluded. The original computation took 103.06516367476434 seconds.

CONFIRMED through the stated finite prefix. Later values are source-bound finite extractions, not independent high-order reconstructions or infinite-radius estimates.

## Root 1 review, V368

At 2026-10-31T14:03:08+00:00, The 3072-bit independent prefix through 60 passes 48744 Poisson coefficient checks, 5928 ordered products, 18 provisional continuations and nine compatibility projections. All 3660 density and 3720 stream coefficients overlap the separate numerical implementation, including H_60 determined by the obstruction at 66; all nine harmonic/response pairs pass. Independent archive replay confirms 120 prefix norm overlaps, the reported source norms and their order roots. The source density norm root at 300 is [7.3538624469607081530350954330013439936237612139704 +/- 4.41e-50], with relative norm radius [1.53435438391497077987546652533e-220 +/- 6.37e-251]. The untuned final stream coefficient at 300 is excluded. The original computation took 102.74473130283877 seconds.

CONFIRMED through the stated finite prefix. Later values are source-bound finite extractions, not independent high-order reconstructions or infinite-radius estimates.

## Root 2 review, V370

At 2026-10-31T14:03:11+00:00, The 3072-bit independent prefix through 60 passes 48744 Poisson coefficient checks, 5928 ordered products, 18 provisional continuations and nine compatibility projections. All 3660 density and 3720 stream coefficients overlap the separate numerical implementation, including H_60 determined by the obstruction at 66; all nine harmonic/response pairs pass. Independent archive replay confirms 120 prefix norm overlaps, the reported source norms and their order roots. The source density norm root at 300 is [0.46908222861948418601572476878899466545850813082837 +/- 2.97e-51], with relative norm radius [1.87050304338445475869164104680e-194 +/- 4.40e-224]. The untuned final stream coefficient at 300 is excluded. The original computation took 101.09628377016634 seconds.

CONFIRMED through the stated finite prefix. Later values are source-bound finite extractions, not independent high-order reconstructions or infinite-radius estimates.

## Root 5 review, V377

At 2026-10-31T14:11:27+00:00, The 3072-bit independent prefix through 60 passes 48744 Poisson coefficient checks, 5928 ordered products, 18 provisional continuations and nine compatibility projections. All 3660 density and 3720 stream coefficients overlap the separate numerical implementation, including H_60 determined by the obstruction at 66; all nine harmonic/response pairs pass. Independent archive replay confirms 120 prefix norm overlaps, the reported source norms and their order roots. The source density norm root at 300 is [2.2003161118231496008179858218198450409376238537321 +/- 1.88e-50], with relative norm radius [1.83886504759862751622977483456e-206 +/- 4.85e-236]. The untuned final stream coefficient at 300 is excluded. The original computation took 97.45719607779756 seconds.

CONFIRMED through the stated finite prefix. Later values are source-bound finite extractions, not independent high-order reconstructions or infinite-radius estimates.

## Root 3 review, V390

At 2026-10-31T14:33:39+00:00, The 3072-bit independent prefix through 60 passes 48744 Poisson coefficient checks, 5928 ordered products, 18 provisional continuations and nine compatibility projections. All 3660 density and 3720 stream coefficients overlap the separate numerical implementation, including H_60 determined by the obstruction at 66; all nine harmonic/response pairs pass. Independent archive replay confirms 120 prefix norm overlaps, the reported source norms and their order roots. The source density norm root at 300 is [0.83536419915090503895692237894749230721500251906048 +/- 3.39e-51], with relative norm radius [1.63585422593399468564506406102e-200 +/- 1.07e-230]. The untuned final stream coefficient at 300 is excluded. The original computation took 61.73156146612018 seconds.

CONFIRMED through the stated finite prefix. Later values are source-bound finite extractions, not independent high-order reconstructions or infinite-radius estimates.

## Root 4 review, V392

At 2026-10-31T14:33:39+00:00, The 3072-bit independent prefix through 60 passes 48744 Poisson coefficient checks, 5928 ordered products, 18 provisional continuations and nine compatibility projections. All 3660 density and 3720 stream coefficients overlap the separate numerical implementation, including H_60 determined by the obstruction at 66; all nine harmonic/response pairs pass. Independent archive replay confirms 120 prefix norm overlaps, the reported source norms and their order roots. The source density norm root at 300 is [1.3604841165707205318217780119876753417520812741695 +/- 1.05e-50], with relative norm radius [2.66304214497527733394978954410e-197 +/- 5.17e-228]. The untuned final stream coefficient at 300 is excluded. The original computation took 60.31102565024048 seconds.

CONFIRMED through the stated finite prefix. Later values are source-bound finite extractions, not independent high-order reconstructions or infinite-radius estimates.
