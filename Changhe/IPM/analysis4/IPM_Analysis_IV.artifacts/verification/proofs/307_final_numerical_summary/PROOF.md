# Rounding and finite-window scope in the final numerical summary

Status: finite endpoint checks CONFIRMED; unsafe certificate rounding REFUTED within the scope below, V641 at 2026-10-31T23:36:10+00:00.

## Statement and hypotheses

Consider the unit-amplitude tuned single-harmonic profiles with (delta, M) equal to (4/5, 7), (4/7, 9) and (4/9, 11). Topics 245 and 228 prove that uniform termwise convergence with two angular derivatives requires R greater than a positive threshold T. Their thresholds are

    T = {4d [a Gamma(a) Gamma(b) / Gamma(a+b)]^(1/a)}^(-1/delta),
    d = delta/(1-delta),
    a = 2/(M+1-delta), b = 2M/(M+1-delta).

A decimal l is justified as a necessary lower bound by this theorem if l <= T. Replacing T with a nearest decimal larger than T is not a consequence of the theorem. This observation does not disprove a stronger bound for the full series.

Separately, let M_n be the audited positive density norm for the sin(7 theta) run through order 500. For two distinct indices L<U define its finite endpoint base

    A[L,U] = exp((log M_U - log M_L)/(U-L)).

Its apparent physical-radius diagnostic is A[L,U]^(5/4). The windows 100..300, 300..500 and 100..500 are distinct statistics. A difference between their rounded results is not a discrepancy between implementations.

## Complete verification argument

Evaluate the three gamma expressions from their exact rational arguments at two independent working precisions, and compare them with the earlier admitted enclosures. Test each decimal asserted as a lower endpoint by a directed strict comparison. Record safe downward replacements. The arithmetic proves the direction of each rounding error. The actual necessary-radius theorem remains the earlier highest-sector proof, not a finite norm fit.

Decode the exact dyadic norm balls at indices 100, 300 and 500 from the admitted order-500 evidence. Their lower endpoints must be positive, so real logarithms are well-defined. Apply the endpoint formula to each of the three windows and enclose its exponential with directed arithmetic. Verify each printed four-place decimal by placing the entire enclosure inside the corresponding nearest-rounding interval. This checks only those finite endpoint statistics.

A fitted law over finitely many indices does not on its own imply an asymptotic equivalence or exclude factorial growth after the measured range. This is an inference limitation, not a construction of an alternative solution to the IPM recurrence. Any statement about its actual infinite asymptotic law needs the separate recurrence theorems or an all-order bound. Describe the reported finite ratio fit as consistent with a geometric law and a power correction over its stated window.

## Dependencies and scope

Dependencies: necessary-radius proofs 228 and 245; the order-500 finite audit 293; positive-real interval arithmetic. No high-order recurrence, full source checkpoint, or convergence theorem is recomputed here. The report excerpts are preserved to make subsequent prose repairs auditable.

## Completed checks

The necessary thresholds are 0.090297348070617..., 0.236597752797397... and 0.507476695384643... for sin7, sin9 and sin11. The decimals 0.0903, 0.2366 and 0.5075 in the numerical experiments' stated proved brackets all round upward. Safe replacements are 0.0902973, 0.2365977 and 0.507476. The theory part already uses these safe values. The sin7 endpoint bases 0.5734 on100..300, 0.5739 on300..500 and 0.5736 on100..500 all round correctly. Their distinct windows explain the different values; there is no numerical discrepancy. The latter two physical diagnostics are approximately0.4994762251 and0.4992213002.

REFUTED only as a claim that the three displayed lower endpoints follow by downward rounding from the cited necessary-radius certificates. This does not refute a stronger lower bound for the actual full series. The three endpoint computations are CONFIRMED as finite statistics. The asymptotic equivalence inferred from a finite ratio fit remains OPEN; the existing numerical-evidence heading does not supply an all-order estimate.

## Repair closure, V643

At 2026-10-31T23:40:06+00:00, each repaired line was compared with the directed bounds established above. All three texts now use the safe decimals. The finite-fit wording explicitly excludes the unsupported asymptotic inference. This closes the publication repair while preserving the original countercheck.
