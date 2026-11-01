# Conditional continuation checks after order400

Status: completed targets are admitted separately below. No infinite convergence or asymptotic law is claimed.

## Exact scope

Use the canonical logarithmic recurrence at delta=2/3 with f_1=sin(theta), but with the order329 checkpoint coefficients replaced by their stored midpoints as documented in138 and189. Every subsequent value is conditional on that replacement. Directed arithmetic after the reset does not restore the discarded uncertainty. This topic extends the completed finite audit254 to later saved orders, at most440 in the present campaign.

For each reported checkpoint N, independently compute the density and stream plain coefficient sums, their nth roots, factorial-column maxima, period-three decrements, and least-squares logarithmic slopes over the final27 orders. Check the logarithmic Poisson equation in every stored coefficient at N-2,N-1,N, and check the canonical zero constant at resonant columns. Compare the norm, increment, ratio and hump entries in the latest ten-order table using their stated rounding. The precision monitor and residue class have a separate bookkeeping audit. Record the exact checkpoint hash, actual maximum stored order, reset metadata and actual computation time. The producer writes checkpoints by atomic replacement, so the open file is a coherent snapshot even while the continuation runs.

## Identities behind the checks

Write f_n(theta,L)=sum_(q,j) a_(n,q,j) L^q sin((2j+1)theta) and g_n(theta,L)=sum_(q,j>=1) b_(n,q,j) L^q sin(2j theta), where L=log r and P_n=2-2n/3. The coefficient identity -Delta psi=partial_x rho is exactly

    (4j^2-P_n^2)b_(q,j)
      -2P_n(q+1)b_(q+1,j)-(q+1)(q+2)b_(q+2,j)
    =[(P_n-2j)a_(q,j-1)+(q+1)a_(q+1,j-1)
      +(P_n+2j)a_(q,j)+(q+1)a_(q+1,j)]/2.

Terms outside the stored support are zero. This follows by applying the radial operator P_n+partial_L twice and the angular second derivative to each stream term, and by applying the polar Cartesian x derivative to each density term. Checking every finite coefficient therefore checks the full Poisson identity for the stored orders. The canonical condition is b_(0,j)=0 whenever P_n=-2j. It does not fix an earlier uncertainty box.

For either field let M_n=sum_(q,j)|a_(n,q,j)|, with b replacing a for the stream. The displayed root is M_n^(1/n). The factorial-column diagnostic is max_q(q! sum_j|a_(n,q,j)|)/sum_j|a_(n,0,j)|; its maximizer is asserted only when interval comparisons strictly separate it from all other columns. The three-order decrement is log10(M_(n+3)/M_n). A27-point slope is the exact normal-equation expression sum_(n=b-26)^b (n-(b-13))log10(M_n)/sum(n-(b-13))^2, evaluated with directed arithmetic.

When fitting shifted multipliers, use the independently checked identity254. If x_n is the complete coefficient vector, S shifts its predecessor by one angular index, and a_n=<Sx_(n-3),x_n>/||x_(n-3)||_2^2, then the squared relative projection residual is e_n^2=1-<Sx_(n-3),x_n>^2/(||x_(n-3)||_2^2||x_n||_2^2). Expanding this expression gives ||x_n||_2/||x_(n-3)||_2=|a_n|/sqrt(1-e_n^2). Fits against log n,1/n,n are finite statistics only. A limiting multiplier or a factorial growth exponent cannot be inferred from the fit residual.

## Evidence and dependencies

Dependencies:01 and10 for the recurrence and logarithmic derivative identities;138 and189 for reset provenance;215 and254 for shifted profiles and earlier finite audits. Retain each target's compact derived evidence rather than another full checkpoint. Historical checks through400 are not overwritten. Verification may use a later atomic snapshot provided its actual maximum order is recorded and the checked range is explicit.

## Order410: admitted 2026-10-31T19:37:55+00:00

V547 confirms5,190,391 coefficient positions, 167,280 final-three-order Poisson identities and59 printed norm/increment/hump comparisons. The full-vector audit covers348..410 in both fields. The density fits on357..410 have beta=0.4715502999, inverse-order fitted limit=0.0387986926, and per-order log slope=0.000534796405. These are finite statistics of the midpoint continuation. The three fit families are not certified asymptotic laws. The final checkpoint's top-level reset flag can be absent because the live producer predates the provenance repair; that absence does not make the computation canonical. The two main arithmetic stages took46.157 and50.289seconds.

## Precision-monitor supplement at order410

V548, recorded 2026-10-31T19:39:04+00:00, recomputes the ten printed density precision monitors and residue classes for401..410. For each logarithmic column, select a largest absolute midpoint as pivot and form the largest radius of a coefficient divided by that interval pivot. Take the largest such column monitor and its base-ten logarithm. This is a monitor of the stored intervals, not a bound on the original canonical sequence after the reset. Every column in these ten orders has a valid nonzero pivot; no uncertain column is skipped. All ten values reproduce the table rounding and the stored monitor to within1e-6.

The checkpoint retains neither a top-level reset flag nor a reset ancestor in its statistics. External provenance and the verified continuation history still require conditional interpretation. The successful computation took14.18501seconds. An auxiliary attempt selected zero pivots because its logarithmic comparison key could be NaN; that attempt is retained as rejected evidence and is not a producer defect. Exact absolute midpoint comparison fixes it.

## Order420: admitted 2026-10-31T20:34:09+00:00

V571 confirms5,952,247 coefficient positions, 175,561 final-three-order Poisson identities and59 printed norm/increment/hump comparisons. The full-vector audit covers348..420 in both fields. The density fits on357..420 have beta=0.4828550993, inverse-order fitted limit=0.0394760961, and per-order log slope=0.000540919911. These are finite statistics of the midpoint continuation. The three fit families are not certified asymptotic laws. The final checkpoint's top-level reset flag can be absent because the live producer predates the provenance repair; that absence does not make the computation canonical. The two main arithmetic stages took65.794 and104.031seconds.

### Order420 monitor admitted 2026-10-31T20:34:09+00:00

V572 verifies all ten printed precision-monitor bins and residue classes through420. All normalization pivots are resolved. This is a finite statistic of the reset continuation. The checkpoint does not itself retain reset ancestry; the external provenance in topics160 and189 is required. No canonical error or convergence statement follows.

## Order430: admitted 2026-10-31T21:44:59+00:00

V590 confirms6,751,395 coefficient positions, 184,041 final-three-order Poisson identities and59 printed norm/increment/hump comparisons. The full-vector audit covers348..430 in both fields. The density fits on357..430 have beta=0.4932980252, inverse-order fitted limit=0.0401320953, and per-order log slope=0.000545959172. These are finite statistics of the midpoint continuation. The three fit families are not certified asymptotic laws. The final checkpoint's top-level reset flag can be absent because the live producer predates the provenance repair; that absence does not make the computation canonical. The two main arithmetic stages took56.073 and66.582seconds.

### Order430 monitor admitted 2026-10-31T21:47:12+00:00

V591 verifies all ten printed precision-monitor bins and residue classes through430. All normalization pivots are resolved. This is a finite statistic of the reset continuation. The checkpoint does not itself retain reset ancestry; the external provenance in topics160 and189 is required. No canonical error or convergence statement follows.

## Order440: admitted 2026-10-31T23:04:43+00:00

V622 confirms7,588,581 coefficient positions, 192,720 final-three-order Poisson identities and59 printed norm/increment/hump comparisons. The full-vector audit covers348..440 in both fields. The density fits on357..440 have beta=0.5032595165, inverse-order fitted limit=0.0407806085, and per-order log slope=0.000550375518. These are finite statistics of the midpoint continuation. The three fit families are not certified asymptotic laws. The final checkpoint's top-level reset flag can be absent because the live producer predates the provenance repair; that absence does not make the computation canonical. The two main arithmetic stages took67.062 and67.084seconds.

### Order440 monitor admitted 2026-10-31T23:04:43+00:00

V623 verifies all ten printed precision-monitor bins and residue classes through440. All normalization pivots are resolved. This is a finite statistic of the reset continuation. The checkpoint does not itself retain reset ancestry; the external provenance in topics160 and189 is required. No canonical error or convergence statement follows.
