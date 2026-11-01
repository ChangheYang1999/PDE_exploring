# A computable Liouville parameter with a divergent pure series

Status: CONFIRMED after independent adversarial review, 2026-10-31T03:52:43Z. See V049 and topic43 for the exact scope and evidence.

## Statement

Fix a finite rational odd-sine leading profile with nonzero `sin(theta)` coefficient. Let `I` be any nonempty open interval with rational endpoints whose closure lies in `(0,1)`. Assuming the theorem of topic 31, there is a computable irrational `delta_*` in `I` such that

\[
 \limsup_{n\to\infty}\|f_n(\delta_*)\|_0^{1/n}=\infty.
\]

The parameter can moreover be chosen Liouville: for every positive integer `M`, it has infinitely many rational approximations `a/p` with

\[
 0<|\delta_*-a/p|<p^{-M}.
\]

Thus the pure density series has zero radius of convergence. The same construction works in a prescribed rational neighborhood of the stored Candidate parameter, with either the single-sine profile or the exact Candidate leading profile. It does not assert divergence of a logarithmic repair or give a convergent algorithm of practical numerical cost.

## Exact functions available to the algorithm

Every finite density and stream coefficient is a rational function of `delta`, away from its finitely many rational exceptional values. This follows by induction from the finite Fourier recurrence: addition, multiplication and division only use rational coefficients and the factors `n delta-2j`, `delta`, and `1-delta`. The angular support is finite at every order.

By topic 31, all sufficiently large primes `p` and all even `4<=a<p` give a nonzero first-resonance coefficient at `r=a/p`. Topic 15 proves that at least one Fourier coefficient of `f_(p+1)` has a nonzero simple pole there. Such a coefficient can be found effectively by computing the exact rational functions or the nonzero residue supplied by that topic. Denote one such rational function by `R_r(delta)`.

For the single-sine input the pole can be chosen at angular frequency `a-1`, and its residue is

\[
 -\frac{\kappa j_0(1+\gamma_*)}{2p^2(c_*-1)},
 \quad j_0=a/2-1,\quad\gamma_*=1-r,\quad c_*=(1-r)^{-1},
\]

which is nonzero. For the general rational profile, topic 15's highest-frequency coefficient gives an effective nonzero choice.

## Nested rational intervals

Enumerate the rational numbers in `(0,1)` as `r_1,r_2,...`, for example by increasing reduced denominator and then numerator. Start with any nondegenerate closed rational interval `I_0` contained in `I`.

At step `k>=1`, choose the first prime-denominator center `t_k=a_k/p_k` in a fixed enumeration satisfying all of the following: it lies in the interior of `I_(k-1)`, its prime exceeds both `k` and all preceding selected primes, and its prime is allowed by topic 31 for the input profile. Such a center exists because the allowed prime-denominator centers of arbitrarily large denominator are dense.

Compute a pole coefficient `R_(t_k)` of order `n_k=p_k+1`. Its absolute value tends to infinity as `delta` approaches `t_k` from either side. Therefore there is a nondegenerate closed rational interval `I_k` satisfying

\[
 I_k\subset\operatorname{int}I_{k-1},\qquad
 |I_k|<2^{-k},\qquad
 I_k\subset(t_k-p_k^{-k},t_k+p_k^{-k})\setminus\{t_k\},
\]

\[
 I_k\cap\{r_1,\ldots,r_k\}=\varnothing,
 \qquad |R_{t_k}(\delta)|>k^{n_k}\quad(\delta\in I_k).
 \tag{1}
\]

Require also that `I_k` avoid all poles of the finitely many coefficient functions through order `n_k`, except the center which is already excluded. There are only finitely many such rational poles; their removal leaves intervals arbitrarily close to the center on either side.

These choices are effective. Enumerate closed dyadic intervals in a fixed computable order, test the rational containment and exclusion conditions, and verify the strict polynomial inequality in (1) by exact rational interval bounds or polynomial root isolation. A nonzero simple pole guarantees an open set on which the inequality has a strict margin, so a suitable dyadic interval and a finite verification eventually occur. Fixing the enumerations makes every choice deterministic.

## The limit and its properties

Nestedness and the length bound give exactly one real number `delta_*` in every `I_k`. Their rational endpoints approximate it to an error below `2^-k`, so it is computable. For every rational `r_j`, all intervals with `k>=j` exclude that number, hence the limit is irrational.

Since `delta_*` belongs to `I_k`, equation (1) implies

\[
 \|f_{n_k}(\delta_*)\|_0
 \ge |R_{t_k}(\delta_*)|>k^{n_k}.
\]

The orders `n_k` increase strictly, so the coefficient-root limsup is infinite. The series in `z=r^(-delta_*)` therefore has zero radius.

Also `|delta_*-a_k/p_k|<p_k^{-k}` and the error is nonzero by irrationality. The primes increase without bound. For any fixed `M`, all steps `k>M` give the stated Liouville approximations. This proves every assertion.

## Dependencies and limitations

The construction uses the prime-denominator obstruction of topic 31, the independently audited nonzero pole calculation of topic 15, exact finite rational-function arithmetic, root isolation or strict interval polynomial bounds, and completeness of the real numbers. No numerical implementation of the nested choices is claimed here. The theorem gives an unambiguous computable divergent parameter, but the enormous finite orders may make its digit computation impractical. It is consistent with topic 18's distinct Liouville parameters for which the series converges.
