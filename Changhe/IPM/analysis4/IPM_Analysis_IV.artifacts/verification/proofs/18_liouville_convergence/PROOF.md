# Convergent examples outside every polynomial Diophantine class

Status: PROVED from the independently confirmed Brjuno theorem, with a complete arithmetic proof below. This is an explicit construction of a sufficient parameter class. It is not a claim that every Liouville parameter is admissible.

## Statement and notation

Let a finite simple continued-fraction prefix `[0; a_1,...,a_N]`, with positive integer partial quotients, have denominator `q_N >= 2`. Suppose its cylinder is contained in `(0,1/2)`. Write `p_k/q_k` for the convergents, with `q_{-1}=0`, `q_0=1`, and extend the prefix recursively by

\[
 a_{k+1}=2^{\lfloor\sqrt{q_k}\rfloor},\qquad
 q_{k+1}=a_{k+1}q_k+q_{k-1}\quad(k\ge N).
\tag{1}
\]

The infinite continued fraction defines an irrational number `alpha` in `(0,1/2)`. Set `delta=2 alpha` and `c=1/(1-delta)`. Then:

1. The Brjuno sum `B(alpha)=sum_{k>=0} log(q_{k+1})/q_k` is finite. More explicitly, the tail from `k=N`, with `Q=q_N`, is at most
   \[
   \frac{4\log(4Q)}Q+
   \frac{2\log2}{(1-2^{-1/2})\sqrt Q}.
   \tag{2}
   \]
2. For every `tau>0` and `kappa>0`, infinitely many positive integers `n` satisfy
   \[
   \operatorname{dist}(n\delta,2\mathbb Z)<\kappa n^{-\tau}.
   \tag{3}
   \]
   Both `alpha` and `delta` are Liouville numbers: they have rational approximations of arbitrarily high polynomial order.
3. For every nonzero S1 leading profile `f_1` that belongs to an analytic Fourier space `A_{sigma_0}`, the pure stationary far-field recursion at this `c` converges on some exterior domain, with the weighted derivatives and potential reconstruction stated in topics 13 and 14.
4. Parameters constructed in this way are dense in `0<delta<1`.

Thus the sufficient Brjuno class is strictly larger than the union of the polynomial Diophantine classes. Failure of every polynomial Diophantine bound is not by itself an obstruction to the IPM exterior series.

## Arithmetic proof

The convergent recursions give `q_{k+2}>=2q_k`. Consequently

\[
 q_{N+r}\ge 2^{\lfloor r/2\rfloor}Q.
\tag{4}
\]

Equation (1) and `q_{k-1}<=q_k` imply

\[
 q_{k+1}\le 2q_k 2^{\sqrt{q_k}},\qquad
 \frac{\log q_{k+1}}{q_k}
 \le \frac{\log(2q_k)}{q_k}+\frac{\log2}{\sqrt{q_k}}.
\tag{5}
\]

For `q>=2`, both functions on the right decrease with `q`. Grouping the indices `r=2j,2j+1` in (4), their sums are bounded by

\[
 \frac2Q\sum_{j\ge0}\frac{\log(2Q)+j\log2}{2^j}
 =\frac{4\log(4Q)}Q,
\]

and

\[
 \frac{2\log2}{\sqrt Q}\sum_{j\ge0}2^{-j/2}
 =\frac{2\log2}{(1-2^{-1/2})\sqrt Q}.
\]

This proves (2). The finite initial part of the Brjuno sum is finite.

For completeness, the basic convergent error follows directly by writing the remaining tail as `t=[a_{k+1};a_{k+2},...]`:

\[
 \alpha=\frac{p_kt+p_{k-1}}{q_kt+q_{k-1}},\qquad
 \left|\alpha-\frac{p_k}{q_k}\right|
 =\frac1{q_k(q_kt+q_{k-1})}
 <\frac1{q_kq_{k+1}},
\tag{6}
\]

using the determinant identity `|p_k q_{k-1}-p_{k-1}q_k|=1` and `t>a_{k+1}`. Therefore, at `n=q_k`,

\[
 d_n\le 2|q_k\alpha-p_k|
 <\frac2{q_{k+1}}
 \le\frac{2^{1-\lfloor\sqrt{q_k}\rfloor}}{q_k}.
\tag{7}
\]

Since `sqrt(q)/log(q)` tends to infinity, the final bound is eventually smaller than `kappa q_k^{-tau}` for every prescribed `tau,kappa`. This proves (3). Equation (6) also gives approximation errors smaller than `q_k^{-M}` for every fixed `M` and all sufficiently large `k`. The rational `2p_k/q_k` approximates `delta`; reducing it only decreases its denominator, so the same conclusion holds. Infinitely many reduced denominators are distinct because they are at least `q_k/2` and tend to infinity.

To see density, take an irrational point in any prescribed open subinterval of `(0,1/2)`. Its nested continued-fraction cylinders have diameter

\[
 \frac1{q_N(q_N+q_{N-1})},
\]

as follows by comparing the tail values `t=1` and `t=infinity` in the same fractional-linear formula. Their diameters tend to zero. A sufficiently long prefix has its entire cylinder in the prescribed interval, and (1) extends that prefix. Doubling proves density for `delta`.

## Application to the IPM recurrence

Topics 13 and 14 establish convergence for every irrational `delta` with finite `B(delta/2)`. Their proofs use that sum, not a polynomial lower bound on every divisor. Equation (2) supplies exactly the required arithmetic hypothesis, and (3) shows that the independent Diophantine theorem in topic 07 cannot cover these examples. No other modification of the density, stream, or potential recursion is needed. Nonzero `f_1` makes the resulting exterior solution nonzero, because the weighted density tends to `f_1` as `r` tends to infinity.

One can start (1) with the exact 31-term prefix of the stored reference `delta/2`. Its denominator is `Q=8152952920478362`. In that case the reference itself is the last rational convergent. Equation (6) gives the exact bound

\[
 |\delta-\delta_{\rm ref}|
 <\frac{2^{1-\lfloor\sqrt Q\rfloor}}{Q^2}.
\tag{8}
\]

The number is specified by integer recursions; storing its enormous later partial quotients is unnecessary. This is a theoretical example, not a finite-precision numerical experiment. It does not resolve compatibility at the first resonance of the stored rational parameter itself.

## Dependencies, provenance, and scope

The only IPM dependency is the confirmed Brjuno convergence theorem in topics 13 and 14. The arithmetic argument above is self-contained. No formal proof assistant was run.

The distinction between Brjuno and Liouville numbers is classical. As a primary reference, the introduction to Laura Luzzi, Stefano Marmi, Hitoshi Nakada and Rie Natsui, *Generalized Brjuno functions associated to alpha-continued fractions*, arXiv:0705.1690v1 (2007), explicitly notes that some Liouville numbers satisfy the Brjuno condition. That reference was consulted on 2026-10-31 for context; it is not a substitute for the construction and bounds proved here.

This result neither establishes necessity of the Brjuno condition for IPM nor proves divergence at any explicitly specified irrational parameter. Those are separate open questions.
