# Finite audit of the period-nine floating runs

Status: CONFIRMED in V568 on 2026-10-31T20:24:33+00:00. The protocol and argument preceded computation. Finite comparisons do not certify the high-order coefficient arrays.

## Statement and exact targets

Fix delta=2/9, c=9/7 and a unit normalized leading profile sin(theta)+b_i sin(3theta), where b_i is one of the ten exact algebraic roots in267. The producer ran rescaled floating recurrences, printed their density and stream norms normalized to unit amplitude, and printed affine responses. This check freezes each output, reads its amplitude and completion information, and compares the available low-order norms and every saved affine response with exact-root directed values.

The low-order targets are the sine-polynomial coefficients of f_1,...,f_18 and g_1,...,g_17 from267. These precede the first free stream harmonic. At the exact algebraic root the first compatibility vanishes. The response targets are the exact small polynomials and generic rational formula independently reconstructed in277. This formula remains valid at the producer's rounded binary64 input, so the effect of root rounding can be separated from the residual numerical discrepancy.

## Finite comparison argument

For each root use its certified closed rational isolating interval. Evaluate every exact rational coefficient polynomial in directed arithmetic, sum the absolute values to enclose the sine Wiener norm, and take its logarithm after proving positivity. The difference between the printed decimal and this enclosure contains the actual finite logarithmic discrepancy. No interval inclusion is attributed to the producer's decimal itself.

For each saved tuning index evaluate sigma_k at the exact-root interval and at the exact dyadic rational obtained by the producer's binary64 parsing. The reference values must exclude zero before computing relative errors. Record the discrepancy from each target and the relative change caused by root rounding. The exact response identity makes these comparisons valid independently of the accuracy of the high-order continuation.

## Reproduction of the printed-data fits

Read each printed logarithmic norm as an exact decimal rational. On every complete period block jQ<n<=(j+1)Q, take the maximum density logarithm and maximum stream logarithm separately, with Q=9. For each endpoint cutoff100,150,200, use the exact two-column normal-equation formula from263 to fit a line to the selected block maxima. Its denominator is strictly positive because there are distinct block endpoints. Compute the residual sum of squares as a rational, and use directed arithmetic for its square root, the base10 exponential, and the radius diagnostic A^(9/2).

Compare the resulting intervals with the rounding bins in the producer's fit table. These are exact statistics of the printed decimal data. They do not enclose a fit to unknown exact high-order coefficients. Record the actual last printed order and the last complete block endpoint: an output announcing a last computed density order does not imply that its norm was printed or used in the fit.

## Scope and dependencies

Dependencies are267 for root isolation and low-order coefficients,277 for the all-index response identity, and263 for the exact finite fit formula. The saved source and target hashes specify the experiment. The conclusions concern finite reproducibility, finite error measurements and correct model attribution. They do not prove an asymptotic growth law or a sharp convergence radius. Independent convergence of these branches has already been proved with separate majorants.
