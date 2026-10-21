# Row-weight audit

Date: 2026-10-20T19:06:20.185610+00:00. Saved-matrix arithmetic CONFIRMED; the claimed continuum classification REFUTED as an inference; the continuum alternatives remain OPEN.

Own ideal-node geometry and own SVDs reproduce all masks, row counts, fractions and reweighted singular values for120x48,L8;96x40,L8;96x40,L4. No numerics evaluator is imported. The files behind the action matrices are frozen in spectral-diagnostics/data; source hashes and numerical discrepancies are in audit.json.

The reported fractions are SQUARED Euclidean norms. For the four softest120x48 modes at distance5, they are0.904557,0.961522,0.699525,0.884813. The corresponding norm fractions OUTSIDE are0.308938,0.196158,0.548156,0.339392. Over allthreefiles andfourmodes the near5squared fraction ranges0.699525to0.961522, not0.82to0.96. Thus the action is concentrated there in this finite metric, but its only defect is nearP is false as an exact support claim. No physical pointwise relative1e-6 test was performed by this row calculation.

The exact row-weight identity and singular-value bounds are in PROOF.md. Reweighting also amplifies errors in the saved finite-difference actions; the softest values remain subject to that error floor. Pure transport and coupled linearized kernels cannot be identified from the row distribution alone.

The asserted rate-based separation is invalid without additional operator-consistency and approximation hypotheses. The exact matrices A_N=diag(N^-3,1) tend to A=diag(0,1), which has a genuine kernel in a fixed analytic basis, despite algebraic small singular values. C-infinity alone also does not imply exponential Chebyshev decay; an explicit counterexample and full proof are provided. No rule selecting interpretation(A) over(B) follows from the given two-grid rates or a future third scalar trend alone.
