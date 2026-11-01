# Version6 numerical windows and scope audit

Status: CONFIRMED for the exact retained-ball checks; one numerical window assertion is REFUTED. The reviewed all-order theorems are unaffected.

## Exact claim and definitions

In the theory part theory version6, Section14.6 item2 states that the increment of log10 c_0 is -0.7025 plus or minus0.0005 per order throughout180<=n<=290 at delta2/3. Here c_0=||[t^0]F_n||_A0 for unit input sin(theta), the canonical logarithmic normalization and t=log r. The table defines an increment as the average over the preceding20 orders. We test this exact numerical statement, as well as its possible interpretation as a single-step increment.

The same section says every coefficient ball at order180 has relative radius below10^(-70). This is stronger than topic53's original column-scale result, so it is checked directly on the retained exact dyadic balls.

## Interval method and result

The independently retained topic53 file contains complete density and stream orders140,160,179,180 from the 512-bit checkpoint. For each exact midpoint m and radius r, reconstruct m plus or minus r at640-bit precision; sum their absolute-value intervals to enclose c_0. Subtract the logarithms and divide by the window width. This certifies the stated numerical quantities conditional on the retained balls enclosing the intended coefficients, the same scope as topic53.

The20-order mean ending at180 is

    [-0.70423351448773046478719510648629 +/-4e-33].

It is strictly below -0.7030, the lower endpoint of the claimed interval. Thus the stated window bound is false. It is not a question of outward rounding in the last quoted digit. The corresponding mean ending at160 is -0.70480467168595639471118535665312 to the displayed precision.

Independently parsing the theory part's complete long-double log, removing its exact amplitude5 by subtracting log10(5) per order, gives the20-order means -0.70393032235 at200, -0.70352531493 at220, -0.70331579038 at240, -0.70285914964 at260, -0.70247505883 at280 and -0.70217425076 at290. Those later numbers are reproductions of the floating-point log, not interval certificates. Over180..290 its means range approximately[-0.704422,-0.701911]. Its single-step increments also fail the proposed interval, ranging approximately[-0.706546,-0.696886].

The correct finite statement is that the20-order means drift from about-0.7042 at180 to-0.7022 at290 in the extended-precision run. This is compatible with an eventual geometric rate but does not prove one.

## Relative-radius terminology

For every nonzero retained coefficient compute radius/|midpoint| with interval arithmetic. At order180, both density and stream indeed have every such ratio below10^(-70), and there are no uncertain-zero entries. Thus the literal order180 assertion is CONFIRMED. It must not be generalized to all orders through180: at stream order179, log degree3, stream array index58, the ratio is about10^(-69.06490), larger than10^(-70). The broader valid bound from topic53 is on each column's maximum-amplitude and Wiener scales. The exact packed counterexample is retained in verification/checks.json.

## Other qualifications needed in the version6 text

1. In Section14.8 the claim that rational divisors in the near-resonant band are at least1/b needs the word nonzero. At every exact resonance that divisor is zero. Enlarging T cannot make a band that includes the zero divisor empty. The nonresonant part of the band is the intended object; exact resonances use the separately prescribed integration map.
2. Amplitude-radius formulas with unrestricted real epsilon must use |epsilon|^(1/delta), or explicitly assume epsilon>0. Homogeneity gives epsilon^n coefficients, and the absolute root test uses |epsilon|. Physical radial dilation itself only realizes positive scalings. The case epsilon0 gives the excluded zero solution.
3. The numerical checks sentence after Proposition14.7 equates the angular function [t^(k-1)]F_(3k+1) to |b_k|(k-1)/(3k). The right side is its Wiener norm, as the complete proof in topic44 states. It needs norm bars.
4. Agreement between two floating-point runs supports a finite observation but does not itself exclude roundoff. The statements that a systematic hump is not roundoff or that an error is smaller by2^(-11) should remain numerical expectations pending the requested independent ball calculation.

None of these issues invalidates the complete all-order proofs already confirmed. Source snapshots, their hashes, an independent verification script and all exact radius records accompany this audit.

## Follow-up 2026-10-31T05:22:13Z: version8

The requested increment-window correction, nonzero-divisor qualification and absolute value in amplitude radii have been applied. One adjacent sentence still needs qualification: after allowing every real epsilon!=0, Section3 calls the amplitude change the same series up to dilation. A positive physical dilation lambda changes f_1 to lambda^(-delta) f_1, which has a positive scalar factor. Therefore it cannot realize epsilon<0 for nonzero f_1. The coefficient identity f_n[epsilon f_1]=epsilon^n f_n[f_1] and the radius factor |epsilon|^(1/delta) are valid for either sign. Only their identification with a positive physical dilation requires epsilon>0. Negative epsilon is the opposite real branch of the analytic parameter series.

Section14.6 item2 also duplicates the phrase containing the4/9 and1/2 increments. This is a transcription defect, not a mathematical change. The new ball-arithmetic interior-winner result in V084 supersedes the statement that this transition has not been checked in ball arithmetic. Full growth beyond240 is still not certified by V084.
