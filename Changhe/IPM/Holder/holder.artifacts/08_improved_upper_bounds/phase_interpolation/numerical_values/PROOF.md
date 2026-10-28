# Improved values from unequal phase interpolation

## Statement and hypotheses

Use the homogeneous Holder seminorm and the circular-principal-value operators modulo constants of ../../../01_setup/PROOF.md. For each exponent below, the proposed C or D upper endpoint follows from the corresponding accepted phase arrays of V168 or V171 and the interpolation theorem in ../PROOF.md. No input transport plan or residual measure changes. The local contribution is bounded uniformly before interpolation; for D this contribution includes the entire local identity measure.

The proposed endpoints are:

| alpha | C upper | D upper |
| --- | ---: | ---: |
| 1/1000 | 637.0403844930 | not recomputed |
| 1/100 | 64.0881631620 | not recomputed |
| 1/20 | 13.1839509406 | not recomputed |
| 1/10 | 6.8511402022 | not recomputed |
| 1/5 | 3.7431650122 | not recomputed |
| 3/10 | 2.7726584812 | 3.2173694859 |
| 1/2 | 2.1934098609 | 2.6458416700 |
| 3/4 | 2.6387679109 | 3.0981226274 |
| 9/10 | 5.0066105983 | 5.4695864502 |
| 99/100 | 42.2175842339 | not recomputed |

The alpha1/1000 endpoint is weaker than the selected analytic bound and should not replace that table entry. These are upper bounds, not exact norms or claims of a maximizing phase.

## Argument and certification

The accepted arrays give17 nonnegative rational upper endpoints u_j at j*pi/32. Let S be the unchanged uniform local bound. For each adjacent pair the interpolation theorem bounds the regular functional by H_(pi/32)(u_j,u_(j+1)). Hence S plus the maximum of these16 bounds is an upper bound for the complete operator. The first program evaluates this expression at384 bits and rounds each final value upward to ten decimal places. Every proposed endpoint is at most the corresponding previously accepted upper endpoint.

A separate acceptance program rereads the phase arrays from their accepted sources, checks all hashes and uniform contributions, and recomputes each adjacent maximum at768 bits through the representation u*cos(t)+b*sin(t), b=(v-u*cos(delta))/sin(delta). It verifies that every stored rational interval endpoint dominates the fresh ball upper endpoint, that the maximum and sum were taken exactly, and that the displayed decimal was rounded upward. This independently checks the arithmetic expression, including the cases where its maximum occurs at an endpoint.

## Status and dependencies

The first arithmetic pass has completed. The result remains OPEN until the independent acceptance program and the lead's analytic cross-read both pass. The acceptance record, when present, is ../verification/accepted.json. The parent analytic proof was written before the numerical pass. Its separate local identity and symmetry prerequisites were already audited in V168 and V172.
