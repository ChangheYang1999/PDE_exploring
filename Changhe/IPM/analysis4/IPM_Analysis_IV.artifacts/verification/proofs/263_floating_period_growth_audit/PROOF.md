# Finite audit of floating period-seven and period-eight growth data

Status: finite audit completed in V540. The protocol was written before computation. This topic makes no new infinite-order convergence claim.

## Claim and scope

For each Q in {7,8} and each increasingly numbered real compatibility root, compare every available printed floating density/stream norm and tuning response with the independently computed directed prefix of261, or the longer third-root prefix of262 when available. Record the actual discrepancy; no floating value is called an enclosure. Independently reproduce the producer's least-squares block-maxima fits from its printed decimal rows.

The target coefficients are those of the unique tuned branches proved in253 and256. Their exact algebraic initial roots differ from the rounded binary inputs used by the floating program. Agreement is a finite reproducibility observation. It supplies neither a tail estimate nor the true convergence radius.

## Method

Parse the producer metadata, order rows, and tuning rows. For each matching prefix order compute the directed logarithm of its positive norm. Directed arithmetic encloses the absolute difference between the printed decimal and the true norm logarithm. The scalar summary uses the midpoint of that narrow error enclosure; the full enclosure is retained. For a tuning row compare the signed response directly and the sign and logarithm of the homogeneous coefficient. Preserve the producer file and the referenced prefix and polar-replay hashes. Missing rows are reported as missing, not silently treated as agreement.

For each complete block jQ<n<=(j+1)Q, take the maximum printed density logarithm and the maximum stream logarithm separately. At block endpoints at least100,150,200, respectively, fit y=a*x+b by the exact rational normal equations

    a=(m*sum(x*y)-sum(x)*sum(y))/(m*sum(x*x)-sum(x)^2),
    b=(sum(y)-a*sum(x))/m.

The printed decimals are exact rationals for this calculation. Evaluate A=10^a and the apparent exterior number 10^(a*Q/2) using directed arithmetic. Compute the RMS residual from the exact rational sum of squares. This reproduces a finite statistic from rounded inputs. Differences between windows do not bound the error relative to an infinite-order limit.

## Implementation limitations checked by inspection

The producer computes each tuning response by subtracting two full continuations, which may lose relative precision. Its long-double mode first parses the profile coefficients through binary64 and its norm helper converts a sum to binary64. Thus that mode alone is not a rigorous error estimate and does not restore an exact algebraic initial root. The independent directed prefixes use refined exact root intervals and both Cartesian and positive-frequency polar recurrences.

Dependencies:253,256,261,262 for completed prefixes;01 and130 for the recurrence and tuning identity. All recorded numerical comparisons retain their exact finite order and arithmetic scope.

## Completed finite check

The twenty baseline float64 files were frozen on2026-10-31T19:11:28+00:00. Their2464 matched density/stream logarithms and144 tuning values satisfy the explicit discrepancy bounds in FIT_TABLE.md. All H signs agree. The120 density and stream fits were recomputed with exact rational normal equations and256-bit directed transcendental evaluation. Two baseline runs overflowed. The proof of the finite statistic is its exact normal-equation calculation; no tail extrapolation is certified.

## Extended finite check

V543 at 2026-10-31T19:22:20+00:00 additionally checks six completed files: both rescaled root1 runs and the binary64 and extended-precision root3 runs. The Q7 root3 comparisons now extend through140, and the Q8 root3 comparisons through96. All1,184 norm comparisons,74 tuning comparisons and36 printed-data fits pass the bounds and ranges in EXTENDED_TABLE.md. The root1 density apparent radii span5058.30 to5273.56 forQ7 and77597.86 to84823.81 forQ8 over the three stated windows. These are finite fit statistics only. Arithmetic took0.20953seconds.
