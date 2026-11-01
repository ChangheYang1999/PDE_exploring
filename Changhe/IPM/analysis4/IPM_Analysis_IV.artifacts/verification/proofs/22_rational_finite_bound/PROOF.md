# Geometric control below the first rational exceptional order

Status: proof complete; numerical constants are certified separately. This is a finite-order theorem, not a convergence theorem at rational parameters.

## Statement and notation

Let `0<delta<1` be rational, `c=1/(1-delta)`, and let `delta/2=p/q` in lowest terms. Write its canonical finite continued fraction as `[0;a_1,...,a_J]`, with `a_J>=2`, convergent denominators `q_0=1,...,q_J=q`, and define

\[
 B_{\rm rat}=\sum_{k=0}^{J-1}\frac{\log q_{k+1}}{q_k},\quad
 \lambda=\frac32+\frac\delta2+\frac1\delta,\quad
 K=\frac{2\lambda(L+2)}{c-1}.
\]

Let `f_1` be a nonzero real odd sine polynomial with positive odd frequencies at most `L`, `F=||f_1||_1` its coefficient sum norm, and

\[
 A=8K e^{2B_{\rm rat}} F/\delta,\quad
 d_n=\operatorname{dist}(n\delta,2\mathbb Z).
\]

The pure stationary density/stream/potential recursion exists uniquely through all orders `1<=n<q`, and

\[
 \frac{\|f_n\|_1}{d_n}\le\frac{A^n}{8Kn}.
\tag{1}
\]

For each integer `1<=N<q` form the finite sums with density exponents `p_n=1-n delta`, stream exponents `P_n=p_n+1`, and potential exponents `p_n+3`. If `t=A r^{-delta}<1`, their stationary residual satisfies

\[
 \sup_\theta r^{-\gamma}|(cX+u_N)\cdot\nabla\rho_N-\rho_N|
 \le \frac{\lambda(L+2)A}{64K^2}\frac{N t^N}{1-t},
 \qquad \gamma=1-\delta.
\tag{2}
\]

The same bound with `t=A R^{-delta}` holds uniformly over `r>=R`. It is a weighted absolute residual bound; it is not divided by the actual density, which can vanish.

## Rational arithmetic and tree bound

For `1<=n<q`, the integer `np` is not divisible by `q`, so `d_n=2||np/q||>=2/q>0`. In particular there is no stream or potential exceptional exponent at these orders. The finite support and multiplier bounds from topics 01 and 13 apply.

The best-approximation fact used in topic 13 remains valid through the final convergent: for `1<=m<q_k`,

\[
 \|m p/q\|\ge\|q_{k-1}p/q\|\ge\frac1{q_k+q_{k-1}}.
\tag{3}
\]

For completeness, the proof by expressing the integer pair `(m,l)` in the unimodular basis of consecutive convergents uses the opposite signs of their errors. Before the last step those signs are strict. At the last step the error of `(q_J,p_J)` is zero and that of `(q_{J-1},p_{J-1})` is `1/q_J`; a nonzero integer combination with first coordinate between 1 and `q_J-1` cannot have a smaller absolute error. Equivalently the exact error formula at the final complete quotient `a_J` gives `1/q_J>=1/(q_J+q_{J-1})`. Thus the endpoint introduces no failure of (3).

Set `S_k={m>=1:||mp/q||<1/(4q_k)}`. Any member of `S_k` is at least `q_k`, and two distinct members differ by at least `q_k`: a smaller positive difference would have distance to the nearest integer below `1/(2q_k)`, contradicting (3). The marked-tree leaf-charge argument of topic 13 therefore bounds by `2n/q_k` the number of internal vertices whose subtree sizes lie in `S_k`, for a binary tree with `n` leaves.

No integer `m<q` belongs to `S_J`, because its distance is at least `1/q`. A size outside `S_0` has `d_m^{-1}<=2`. A size in `S_k` but not `S_{k+1}` has `d_m^{-1}<=2q_{k+1}`. Assigning each such size to its last set and using the preceding count proves

\[
 \prod_{v\text{ internal}}d_{|v|}^{-1}
 \le 2^{n-1}\exp(2nB_{\rm rat}),\qquad n<q.
\tag{4}
\]

Put `Y_n=n||f_n||_1/d_n`. The already verified recurrence estimate is

\[
 Y_n\le\frac K{d_n}\sum_{i+j=n}Y_iY_j,\qquad Y_1=F/\delta.
\]

Iterating it over full ordered binary trees and using (4) and the Catalan bound `C_{n-1}<=4^{n-1}` gives

\[
 Y_n\le (8K)^{n-1}e^{2nB_{\rm rat}}(F/\delta)^n=A^n/(8K).
\]

This proves (1). The generic inverses give a unique pure potential and stream at all these orders.

## Residual bound

All stationary coefficients of orders at most `N` cancel exactly. The residual is the sum over ordered pairs `1<=i,j<=N<i+j` of

\[
 r^{1-(i+j)\delta}\big[P_i g_i f_j'-p_j g_i'f_j\big].
\]

The stream multiplier and support estimates imply

\[
 \|P_i g_i f_j'-p_j g_i'f_j\|_1
 \le \lambda(L+2)\frac{ij}{d_i}\|f_i\|_1\|f_j\|_1
 \le\frac{\lambda(L+2)}{64K^2}A^{i+j}.
\]

In the last step use (1) and `d_j<=1`. For a fixed sum `s=i+j`, at most `N` ordered pairs occur. Multiplying by `r^{-gamma}` and summing `s=N+1,...,2N` yields

\[
 \frac{\lambda(L+2)A}{64K^2}N\sum_{s=N+1}^{2N}t^{s-1}
 \le\frac{\lambda(L+2)A}{64K^2}\frac{Nt^N}{1-t}.
\]

This proves (2), including the asserted uniformity in `r>=R`.

## Exact stored Candidate 007 parameter

For the parameter and leading density independently extracted in topic 02,

\[
 q=8152952920478362,\qquad N=q-1=8152952920478361.
\]

Every coefficient through `N` is defined and obeys (1), regardless of whether the first compatibility coefficient at `q` vanishes. The bound permits a mathematically defined truncation with this enormous number of terms; no such polynomial has been computed or stored.

The accompanying Arb certificate starts from the exact rational input, computes the finite continued fraction exactly, and encloses every logarithm and exponential in `B_rat`, `A`, and the logarithm of the residual bound. At `r>=(2A)^(1/delta)`, use `t<=1/2`. The certificate separately verifies convenient strict upper bounds and an integer exponent `E` for which the residual is below `2^-E`. The printed centers of intervals are not used as upper bounds.

## Dependencies and scope

This proof depends on the independently derived recurrence and potential inversion in topic 01 and the detailed multiplier and marked-tree proof in topic 13. It verifies the theory part's Theorem E, using `J` for the continued-fraction length to avoid overloading `K`. It does not prove compatibility at `q`, infinite convergence at the stored parameter, a global stationary solution, or closeness of the finite truncation to an exact solution.

## Certified constants

Arb 512-bit arithmetic gives `A<87214` for `f_1=sin(theta)` and `A<13178350` for the exact raw Candidate profile, both at the stored rational parameter. With `N=8152952920478361` and `r>=(2A)^(1/delta)`, the weighted residuals are respectively below

\[2^{-8152952920478302},\qquad 2^{-8152952920478298}.\]

The corresponding base-10 logarithms of `(2A)^(1/delta)` are approximately 11.7101980148021746 and 16.5788758314798067. These last decimal values are descriptions, not outward radius bounds. One may use the strict integer upper bounds for `A` in the radius expression to obtain a fully explicit sufficient radius. Exact input, continued-fraction denominators, interval values and hashes are retained in `verification/rational_constants.json`.
