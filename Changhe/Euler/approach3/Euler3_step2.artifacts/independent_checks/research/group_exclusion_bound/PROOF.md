# A norm bound for excluding small Jacobian groups

Status: proved exact finite-dimensional statement. This is a review of the bound claimed in specification v1.16 section 3.6(j)(2)(i), not a claim about an Euler solution or an observed numerical derivative error.

## Statement, hypotheses and notation

Let d,D be vectors in R^n with its Euclidean norm, d nonzero. Let P be an orthogonal coordinate projection onto a row group and let tau>0. If

max(||Pd||, ||PD||) < tau ||d||,

then ||P(D-d)|| < 2 tau ||d||. In general the factor 2 cannot be replaced by 1, even if D-d is entirely supported on that group and ||D||=||d||. Consequently this hypothesis alone does not imply a whole-column relative error at most tau under denominator max(||d||,||D||,F) when F<=||d||.

For k pairwise disjoint excluded groups P_i satisfying these hypotheses, the error supported on their union is less than 2 sqrt(k) tau ||d||. This bound concerns those groups only; error in remaining rows must also be included. The groups used in the campaign can overlap, so a disjoint partition or an overlap-aware bound is needed to apply this extension.

## Proof

The triangle inequality gives

||P(D-d)|| <= ||PD||+||Pd|| < 2 tau ||d||.

For a counterexample to the factor 1, take n=2, tau=1/1000000, a=3tau/4, d=(1,a), D=(1,-a), and let P retain only the second coordinate. Both group norms are a, which is strictly smaller than tau||d|| because ||d||>=1. The error is supported on the group. Both full norms equal sqrt(1+a^2), and the whole-column relative error is

2a/sqrt(1+a^2) = (3tau/2)/sqrt(1+9tau^2/16) > tau.

The last strict inequality follows by squaring the positive quantities: 9/4 > 1+9tau^2/16 at the specified rational tau. Thus the asserted threshold guarantee is false. The same pair can be assigned at every step of an abstract ladder; quantifying the small-group condition over steps does not repair the bound. This is an algebraic counterexample to a norm inference, not a construction of the campaign's residual map.

For k disjoint groups the squared union error is the sum of their squared errors, each less than 4tau^2||d||^2. Taking square roots proves the stated union bound. This completes the proof.

## Dependencies and scope

Only the Euclidean triangle inequality, the Pythagorean identity for disjoint coordinate projections, and rational arithmetic are used. The exact rational counterexample is checked in verification/counterexample_v1.json by formal/check_counterexample_v1.py. No formal proof-assistant verification is claimed.

specification v1.16 still retains a separate whole-column check. This counterexample refutes its explanatory bound; it does not show that its entire amended gate necessarily accepts a failed whole-column comparison. Excluding a previously required per-group comparison and replacing it with coverage on other columns is nevertheless a change to aggregate acceptance. Passing a group on five other coefficient directions does not prove its derivative on the excluded direction. A small relative group norm also does not, by itself, identify floating-point rounding as the cause of a mismatch.
