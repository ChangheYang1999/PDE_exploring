# Conditional arithmetic audit through order360

Status: CONFIRMED finite conditional arithmetic, V408; literal exact-cycle descriptions refuted in V409. The source is the midpoint continuation of the canonical logarithmic recurrence at delta=2/3. It does not propagate the uncertainty discarded through order329.

## Statement and scope

For each stored density or stream coefficient at orders324 through360, define its plain norm as the sum of absolute values of all sine coefficients in all logarithmic columns. Denote these norms M_n and N_n. This audit checks their interval enclosures, the reported finite three-order decrements, and ordinary least-squares slopes over the specified27-order windows. It also checks the logarithmic Poisson identity coefficient by coefficient at358,359,360. Exact selected source arrays and a hash of the full checkpoint are retained.

The conclusions concern the supplied loaded continuation. They neither identify its coefficients with the original canonical solution nor establish eventual periodicity, a limiting slope, or infinite convergence. In particular, a finite sequence of nearly equal three-order decrements is not a proof that the decrements converge.

## Arithmetic argument

All source midpoint-radius pairs are loaded as outward intervals. For each column q, summing the absolute values gives an enclosure of its angular Wiener norm. Summing over q gives the plain norm. Positivity permits outward logarithms, roots, and ratios. Multiplying column q by q! and comparing disjoint intervals certifies a unique factorially weighted maximizing column whenever these comparisons succeed. Its logarithm relative to the unweighted column0 is the reported hump height.

For a window ending at b with27 consecutive indices, the least-squares slope of y_n=log10 M_n is

    sum_(n=b-26)^b (n-(b-13)) y_n / sum_(n=b-26)^b (n-(b-13))^2.

The same formula applies to N_n. It is an exact linear expression in the log-norm enclosures. A three-order decrement is y_(n+3)-y_n; interval subtraction encloses it, regardless of dependence. Disjoint decrement intervals refute an exact finite period-three geometric cycle. They do not rule out asymptotic approach to a cycle.

Stream mass is grouped by the exact distance min(|P_n+2j|,|P_n-2j|), P_n=2-2n/3, of its frequency2j to the Poisson characteristic. This is a finite diagnostic partition. Summed shares and their differences are outward quotients of positive norm intervals.

## Poisson identity

Let F[q,j] multiply (log r)^q sin((2j+1)theta) in the density coefficient, and G[q,j] multiply (log r)^q sin(2j theta) in the stream coefficient. Missing entries are zero. Direct polar differentiation gives

    (4j^2-P_n^2)G[q,j]-2P_n(q+1)G[q+1,j]-(q+1)(q+2)G[q+2,j]
      = ((P_n-2j)F[q,j-1]+(q+1)F[q+1,j-1]
          +(P_n+2j)F[q,j]+(q+1)F[q+1,j])/2.

This is obtained from -Delta psi=partial_x rho, not by invoking the source's inverse routine. At resonance, a stored canonical constant is checked to equal zero. Interval zero containment verifies finite consistency of the supplied arrays; it is not an independent high-order nonlinear reconstruction or an existence theorem.

## Dependencies

Topic01 derives the density/stream recurrence independently from the common potential. Topics160 and190 explain the reset-state provenance limitation. Topic189 gives the earlier350 audit and its explicit counterexamples to claims of exact periodicity. The present computation extends that finite audit without changing its mathematical scope.

## Completed audit

All128881 selected Poisson coefficients and59 printed diagnostic comparisons pass. The computation inspected1908667 coefficient positions, in22.761859574820846 seconds. The density and stream slopes over334 through360 are approximately-0.5443957797462090 and-0.5420885657003361. At360 the density root is0.2013526629910598373, not the printed0.2012.

The three density decrements starting at351,354,357 are approximately-1.6321123664,-1.6297132154,-1.6283347550. Their interval enclosures are disjoint, so an exact finite geometric period-three cycle is ruled out. This does not rule out an asymptotic cycle. The older336->339 decrement of-1.5845902525 also refutes the repeated claim that every decrement from333 onward is within0.02 of-1.63.
