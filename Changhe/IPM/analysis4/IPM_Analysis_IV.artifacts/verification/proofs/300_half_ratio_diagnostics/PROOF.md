# Ratio and root diagnostics for the canonical half-exponent run

Status: finite fit CONFIRMED and root/ratio substitution REFUTED in V602 on 2026-10-31T22:01:56+00:00.

## Statement and hypotheses

Let M_n be the positive plain density coefficient norm of the canonical unit-sine series at delta=1/2. Let q_n=M_n/M_(n-1) for n>=2. The supplied interval norms through n=300 are those independently recomputed in topic291. Any enclosed numerical result below is conditional on those coefficient enclosures, unless identified as an exact scalar identity. The issue under review is whether a fitted law for q_n can be described as the same law for M_n^(1/n).

## Argument

For every positive finite sequence,

    log(M_n)/n = log(M_1)/n + (1/n) sum_(j=2)^n log(q_j).

This is the logarithm of the telescoping product M_n=M_1 product_(j=2)^n q_j. Consequently a ratio fit and a root fit are different statistics. In particular, if an infinite positive sequence satisfies q_n=L(1-a/n+O(n^-2)), where L>0 and a is real, then Taylor expansion of log(1+x) at zero gives log(q_n)=log L-a/n+O(n^-2). Summing, using the convergent sum of n^-2 and the harmonic-number asymptotic, yields log M_n=n log L-a log n+C+O(1/n). Thus M_n^(1/n)=L exp((-a log n+C)/n+O(n^-2)). No such infinite asymptotic hypothesis follows from a finite regression.

The independent finite fit uses x_n=1/n, y_n=q_n for n=200,...,300. Write xbar and ybar for the arithmetic means. The unique least-squares slope is B=sum((x_n-xbar)(y_n-ybar))/sum((x_n-xbar)^2), the intercept is L=ybar-B*xbar, and a=-B/L when L is nonzero. The denominator is positive since the x_n are distinct. Differentiating the sum of squared residuals proves these normal equations. Interval evaluation encloses their values for the supplied interval norms. Its root-mean-square residual is sqrt(mean((y_n-L-B*x_n)^2)). Centered sums are replayed at two precisions.

For each order with a nonconstant logarithmic column, topic291 records a certified maximizing factorial-weighted column and whether it lies below the constant column. Those records can certify absence of a finite interior maximum through300; they imply nothing about later orders. Printed finite diagnostics are checked with their explicit rounding units. The stated per-order increment range is checked over271,...,300.

## Dependencies and scope

Topic291 provides independently computed norm balls, Poisson consistency and exact low-order coefficients. The producer report is frozen by hash before comparison. We do not infer convergence, a limiting ratio, or a future hump from these finite statistics. A correction to which statistic was fitted is an editorial correction supported by the exact product identity above.

Written 2026-10-31T21:54:39+00:00.

## Completed verification

The consecutive-ratio fit over200..300 has L=[0.38385768622139342734582475005512740 +/- 3.58e-36], a=[1.8374489216973561829110622733914366 +/- 7.95e-35] and RMS residual [0.000724739104934886407124826576432195 +/- 4.18e-37]. Its three printed rounding bins pass. At300 the root is [0.37158891332430729794930352501411455 +/- 2.81e-37], the actual ratio is [0.38107160806583006126713991458220672 +/- 4.01e-36] and the fitted ratio is [0.38150662324928428917569974750737638 +/- 1.34e-36]. The mean log10 increment over271..300 is [-0.41870918846155326351688440788848151 +/- 2.09e-36]. At every order with nonconstant columns, density9..300 and stream8..300, column1 is the unique nonconstant factorial maximum and is below the constant column. Both centered arithmetic replays agree; actual audit time 0.012839322909712791seconds.

Finite fit CONFIRMED under the input enclosure hypothesis. Substituting the root statistic for the consecutive ratio is REFUTED. No limiting ratio, infinite convergence or future-hump claim follows.

## Additional finite decay-rate scope check

The current numerical summary describes the canonical rational logarithmic runs as following a common factor 10^(-0.70) per order and explicitly includes delta=1/2 through300. Test this assertion on the already verified positive density norms M_n for that run. For d_n=log10(M_n/M_(n-1)), n=271,...,300, their mean is exactly log10(M_300/M_270)/30 by telescoping. Thus any assertion that every increment is within0.01 of -0.70 would put the mean in[-0.71,-0.69]. The certified interval for the mean is disjoint from this range, so this run is a finite counterexample to the common reported rate. The minimum and maximum intervals also give a direct check of all thirty increments. This argument does not refute convergence of this particular infinite series; no convergence or nonconvergence conclusion follows from this finite statistic.

Dependencies: the unchanged interval diagnostics in verification/checks.json, already admitted in V602, and topic291's underlying coefficient audit. The added calculation only checks strict rational interval separation and the transcription of the affected summary clause; it does not rerun the recurrence.

Protocol appended 2026-10-31T23:08:19+00:00.

Completed 2026-10-31T23:08:19+00:00, V624: For delta=1/2 the mean density log10 increment on271..300 is [-0.41870918846155326351688440788848151 +/- 2.09e-36]. All thirty increments lie strictly between-0.421 and-0.417, disjoint from[-0.71,-0.69]. The common10^-0.70 per-order summary therefore fails for the explicitly included half-exponent run. REFUTED for the universal finite decay-rate description. CONFIRMED for the half-exponent counterexample. Infinite convergence remains OPEN.
