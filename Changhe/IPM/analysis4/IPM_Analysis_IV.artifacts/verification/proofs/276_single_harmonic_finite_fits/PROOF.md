# Finite growth fits for tuned single harmonics

Status: finite-statistic verification protocol, written before computation. No limiting growth law is claimed.

## Exact statement and hypotheses

Fix one of the unit-amplitude single-harmonic branches sin(7 theta), delta=4/5; sin(9 theta), delta=4/7; sin(11 theta), delta=4/9; or sin(17 theta), delta=6/13. Let F_n>0 be the density sine Wiener norms enclosed by the finite checkpoint audit271, and let y_n=log10(F_n). The checkpoint and its tuning data must have the exact hashes used in271. Assume the producer interval-execution hypotheses specified there. Fix a finite inclusive interval L<=n<=U within the completed checkpoint, with at least three distinct positive orders.

The following are finite statistics of those norms: the endpoint slope (y_U-y_L)/(U-L); the least-squares line y_n=a n+c; and the least-squares model y_n=a n+b log10(n)+c. Define the fitted geometric base A=10^a, and its radius diagnostic R_fit=A^(1/delta). Define RMS as the square root of the arithmetic mean of the squared fit residuals over exactly the same integer orders. The result is an outward interval enclosure for each statistic, together with exact stated windows. Endpoint slopes and least-squares slopes are different statistics.

Finite response signs, minima over the stored tuning indices, and the last stored harmonic root |H_n|^(1/n) are also enclosed from the matching tuning file. These checks do not locate an infinite response minimum unless another theorem supplies that conclusion.

## Proof of the enclosure method

Decode the norm intervals as exact dyadic midpoint-radius pairs. Positivity permits directed logarithms. For a model with row vector X_n=(n,1) or (n,log10(n),1), form G=sum X_n^T X_n and d=sum X_n^T y_n. The line design has rank two at distinct orders. The three-column design has rank three: strict concavity of log on positive reals makes its values at any three distinct orders noncollinear with the n column and constant column. Therefore G is positive definite and the unique least-squares coefficient vector is G^(-1)d.

Compute G and d in outward interval arithmetic and solve the normal equations by Gaussian elimination. Each selected pivot must exclude zero; otherwise the calculation fails rather than returning a statistic. The ordinary elimination identities then prove by induction that every intermediate interval contains its exact counterpart, and the final vector contains the unique exact solution. Evaluate residuals, RMS, powers, endpoint slopes and finite harmonic roots by the same directed operations. Correlations between source intervals may widen the result but cannot invalidate inclusion.

A displayed decimal with final place u agrees in rounding when the entire computed interval lies in the appropriate half-open rounding bin of width u. For an approximate range or an explicitly rounded-down bound, use its stated direction and precision instead. Preserve a discrepancy rather than changing the published number silently.

## Scope and dependencies

The finite norms and tuning inputs are established under the hypotheses of271. The arithmetic implementation uses the same independently decoded intervals but does not import the producer's fitting code. A fit can vary strongly with its window or model. Neither a fitted A nor A^(1/delta) proves a coefficient asymptotic or a sharp convergence radius. The separately admitted infinite convergence theorem for each branch remains independent of these fits. The source hashes, exact windows, arithmetic precision, pivots, results and actual runtime are retained in verification.
