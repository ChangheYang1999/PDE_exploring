# Finite extension of the tuned sin(7 theta) series to order 500

Status: finite verification CONFIRMED in V604 on 2026-10-31T22:09:09+00:00.

## Statement, hypotheses and notation

Fix delta=4/5, c_l=5, unit leading amplitude and f_1(theta)=sin(7 theta). Use the uniquely tuned pure density and stream series whose existence and nonzero response bound were established in topic241 and admitted inV503/V504. The finite data of topic271 concern the previous order-300 run. This topic concerns the separately generated order-500 run.

Let f_n and g_n be the sine coefficient arrays, and let M_n be the sum of absolute density sine amplitudes. The stored intervals are assumed to have been produced by the outward interval induction audited in271; the independent checks below verify consistency and an independently reconstructed prefix. A residual interval containing zero alone is not proof of exact compatibility. Exact compatibility follows from the separate tuned-series theorem.

## Complete finite verification argument

Recompute orders1 through20 using the Cartesian derivative recurrence, including every intervening tuned harmonic. Compare every resulting density and stream coefficient with the supplied intervals. This is independent of the producer's polar derivative formulas. At every order through500, decode each dyadic center and radius and verify the full differential Poisson equation and the nonresonant denominator tests. The free harmonic at the last resonant order may be unset because it affects the next period; exclude its full stream norm if it is unset and record that exclusion.

At orders400 and500 form every ordered nonlinear product using Cartesian derivatives and test all resulting coefficient residuals. At order500 this means499 products; no intermediate nonlinear order is included by implication. For the first300 orders compare the newly supplied packed arrays and logged norm values with the archived order-300 source. The previous final free harmonic in g_300 was unset; its slot is excluded from equality and separately checked against the newly tuned H_300. Exact agreement of the other finite arrays is a reproducibility observation, not a tail estimate.

The norm, root and fit checks use only the supplied finite arrays. For inclusive integer windows L<=n<=500 fit y_n=log10(M_n) to the two models a n+b and a n+beta log10(n)+b. Solve the normal equations in directed arithmetic, verifying every pivot excludes zero. The associated finite diagnostics are A=10^a and R_fit=A^(5/4). Separately report the endpoint base 10^((y_500-y_100)/400). These statistics can differ and none is an upper or lower bound for the true convergence boundary. Compare any newly reported rounded values only after the producer has published them.

## Reproducibility and scope

Preserve the independent prefix, input hashes, finite norm and fit tables, complete nonlinear check counts and actual elapsed times. Large coefficient files remain in the numerical experiments. The arithmetic implementation reuses the already reviewed271 method, with the input tag, maximum order and selected nonlinear orders explicitly changed. The same interval library and dyadic decoder are shared; this is not an independent interval-library implementation.

The conclusions concern finite data under the stated input-enclosure hypothesis. The separately proved sufficient radius and necessary radius remain unchanged. Finite continuation to500 cannot establish an eventual growth law, a sharp convergence threshold, monotonicity after the checked range or convergence of the canonical logarithmic series.

The admission also replays each fit at3072bits by centering both regressors, solving the resulting one- or two-dimensional covariance equations and recovering the intercept. This is algebraically equivalent to the normal equations but does not repeat their Gaussian elimination.

## Completed checks

The unit sin7, delta4/5 run through500 passes independent Cartesian prefix20 comparisons on840 density and860 stream coefficients and4 tuned harmonics. All2006500 Poisson coefficients,501000 denominator checks and500 logged density norms pass. Complete nonlinear sums at400 and500 check898 ordered products and14406 residual coefficients. The order500 density root is[0.56103553708529619198930135185363725699 +/- 2.70e-39]; maximum input norm-relative radius is[5.0445066517392440003112293473315741713e-77 +/- 2.18e-115]. Packed overlap through300 is exact on180600 density and180899 stream entries, with300 identical printed norms; the previously unset g300 mode238 is separately verified against H300. The final g500 free harmonic is unset, so its full norm is excluded. All eight fits are independently replayed at3072bits. The line-fit A values for lower endpoints100,200,300,400 are['[0.570996777140135311205858399720376509724667419 +/- 3.93e-46]', '[0.571358453019893054763524975076030958365442386 +/- 3.11e-46]', '[0.572269961188816842705128802721945036049771728 +/- 4.25e-46]', '[0.573802276511543790148033777023990284511390426 +/- 2.19e-46]'], with radius diagnostics['[0.496354623011238422416742582020924817036816589 +/- 1.52e-46]', '[0.496747649980914913801549985262601968898587430 +/- 9.53e-47]', '[0.497738446118499062707771385137742429902415496 +/- 4.37e-46]', '[0.499404939650253023695487478757019519335048000 +/- 6.85e-47]']. The distinct100..500 endpoint base is[0.57363347304639651860375831002784574855961078985434 +/- 9.08e-53] and its radius diagnostic is[0.49922130020785295200619763199547840585277194816263 +/- 2.73e-52]. Main finite audit runtime356.857046seconds.

CONFIRMED for finite arithmetic and recurrence consistency under the stated coefficient-enclosure hypotheses. The independent centered fit replay validates only the stated finite statistics. The earlier separate convergence theorem is unchanged; no sharp radius, eventual growth law, or uncomputed continuation is inferred.
