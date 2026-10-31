# Segment-two interpretation and warning predicates

Read `../PROOF.md` before this note. This note applies the finite projection identities to the previously checked V379 records. It introduces no new Euler computation. The exact inputs and the draft under review are captured in `artifacts/segment2_classification_v1/audit.json`.

Let \(J D^{-1}=QR\), \(Q^TQ=I\), \(q=Q^Tr\), and \(d=\|r\|^2>0\), with the spaces and coefficient phase restriction of the proof. For an SVD \(R=U\Sigma V^T\), the definition is

\[
\eta(0)=d^{-1}\sum_{\sigma_i>0}|u_i^Tq|^2.
\]

The share outside the stored \(Q\) space is

\[
b_Q=1-\|q\|^2/d.
\]

Orthogonal decomposition gives both formulas. In particular, \(b_Q\) is not \(\eta(0)\). Their sum is one if every component of \(q\) along an exact zero singular value vanishes. Full rank is sufficient but not necessary. If a floating SVD treats every returned singular value as positive, the implemented sum includes every left singular vector and is numerically \(1-b_Q\), without establishing exact rank. These distinctions are proved in the final section of `../PROOF.md`.

The independently calculated values, in P1 FREE, P1 FIXED, P2 FREE and P2 FIXED order, are:

| quantity | P1 FREE | P1 FIXED | P2 FREE | P2 FIXED |
|---|---:|---:|---:|---:|
| numerical eta(0) | 0.8511831960 | 0.8366420721 | 0.6324315958 | 0.6386760113 |
| share outside stored Q | 0.1488168040 | 0.1633579279 | 0.3675684042 | 0.3613239887 |
| numerical eta(0) minus eta(1e-8) | 0.0018527859 | 0.0031085915 | 0.0182483632 | 0.0204887312 |

Thus most of the computed reducible share is above the \(10^{-8}\sigma_{\max}\) threshold, but the below-threshold share is nonzero. No accuracy claim for the associated enormous near-zero-band steps follows from this accounting.

specification v1.25 section 11 declares an Outcome D warning when any absorption fraction
\[
c(e)=\|(I-P_a)J_pe\|/\|J_pe\|
\]
is below \(10^{-3}\). Here the parameter columns are nonzero and the retained coefficient projector uses the declared relative cutoff \(10^{-12}\). All eight coordinate-direction values are below this threshold:

| state | c_l fraction | omega fraction |
|---|---:|---:|
| P1 FREE | 0.00000557735 | 0.000254997 |
| P1 FIXED | 0.00000479009 | 0.000271349 |
| P2 FREE | 0.00000549410 | 0.000263913 |
| P2 FIXED | 0.00000549023 | 0.000231222 |

The warning predicate is therefore met at each captured endpoint. This is a direct finite numerical classification under the registered threshold. It is consistent with the independent failures of stationarity in V379 and V381. None of these four reduced systems has the registered parameter-singular flag or a correlation magnitude above 0.999.

The warning does not establish exact linear dependence, nonlinear non-identifiability, or the size of a profile-minimized sensitivity interval. The actual-objective profiles, restart tests, final frozen cohort and final branch ordering are separate requirements. This note does not assign the campaign's final primary category.
