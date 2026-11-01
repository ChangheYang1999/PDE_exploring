# A geometric density coefficient bound does not control the polynomial-log Poisson inverse

Status: CONFIRMED counterexample to the proposed inverse estimate. Whether the full nonlinear recurrence supplies additional cancellations remains OPEN.

## Statement

Fix \(\delta=4/9\), \(p_n=1-n\delta\), \(P_n=p_n+1\), and \(t=\log r\). There are real S1 density polynomials \(F_n(t,\theta)\) with

\[
 \deg_t F_n\le\lfloor(n-1)/9\rfloor,\qquad
 \deg_\theta F_n\le2n-1,\qquad
 M_n:=\sum_\ell\|[t^\ell]F_n\|_{\ell^1}\le1,
\]

whose weighted density series converges with every derivative on a sufficiently large exterior domain, but whose modewise polynomial-log Poisson inverse has divergent stream terms at every fixed radius.

This family is not claimed to solve the nonlinear stationary recursion. It shows that the bound on \(M_n\) and the degree bounds alone do not justify the phrase “and the same for the stream, potential and derivatives” in a convergence criterion.

## Construction and density convergence

Set \(F_1=\sin\theta\). For every integer \(k\ge0\), put

\[
 n_k=9k+8,\qquad j_k=2k+1,\qquad
 F_{n_k}=t^k\sin((4k+1)\theta),
\]

and set every other \(F_n\), except \(F_1\), to zero. The asserted degrees and \(M_n\le1\) follow immediately. In particular the log degree is exactly the permitted bound at each \(n_k\).

The additional terms in the weighted density series have absolute values bounded by

\[
 r^{-\delta(n_k-1)}t^k
 =r^{-28/9}(r^{-4}\log r)^k,\qquad r>1.
\]

For any sufficiently large \(R\), the ratio \(r^{-4}\log r\) is uniformly less than one on \(r\ge R\). Every fixed angular or weighted radial derivative introduces only polynomial factors in \(k\), and differentiating \(t^k\) preserves the same geometric domination after choosing a slightly larger ratio below one. The density therefore has all the stated uniform weighted derivative convergence.

## The stream coefficient

At order \(n_k\),

\[
 P_{n_k}=-4k-\frac{14}{9},\qquad
 P_{n_k}+2j_k=\frac49=:s.
\]

This is a nonresonant mode. In the factorized Poisson inverse, the input coefficient \(A_{n_k,j_k-1}=t^k\) gives

\[
 B_{n_k,j_k}(t)
 =-\frac12(D+s)^{-1}t^k
 =-\frac{(-1)^k k!}{2s^{k+1}}
       \sum_{\ell=0}^k\frac{(-st)^\ell}{\ell!},
 \qquad D=\partial_t.
\]

There is no second input coefficient \(A_{n_k,j_k}\) in this mode. The displayed polynomial is verified by direct multiplication by \(D+s\), which telescopes to \(-t^k/2\).

At every fixed real \(t\), the sum tends to \(e^{-st}>0\). Thus for all sufficiently large \(k\),

\[
 |B_{n_k,j_k}(t)|\ge
 \frac{e^{-st}k!}{4s^{k+1}}.
\]

Multiplication by the radial factor \(r^{P_{n_k}}\) contributes only a geometric factor in \(k\). The factorial remains dominant. A Fourier coefficient is bounded by twice the angular supremum, so the stream terms fail to tend to zero in angular supremum norm at every fixed \(r>0\). No choice of resonant constants affects this nonresonant calculation.

## Consequence for the open logarithmic problem

A geometric bound on \(M_n\) proves convergence of the density series but does not, by itself, prove convergence of its normalized polynomial-log stream. The full stationary recursion might prevent the example's forcing pattern. That would require an additional argument, and is not established by the density bound alone.

A sufficient estimate that is already justified is geometric growth of the factorial norm

\[
 \|F_n\|_{!,4b}
 =\sum_\ell \ell!(4b)^\ell
             \|[t^\ell]F_n\|_{\ell^1}
 \le C A^n
\]

at \(\delta=a/b\), with the analogous smaller-strip norm for analytic angular data. Topic 17 proves a uniform polynomial-log Poisson inverse bound in this norm. The potential inverse also has bounded rational first-order factors and the finitely many exceptional low orders can be handled separately. Together with degree and bandwidth bounds, such an estimate would give the needed exterior convergence with derivatives. Replacing the current factorial loss by a geometric bound is still OPEN.

## Dependencies and scope

The proof uses the independently derived factorized Poisson inverse in topic 10, the degree bounds in topic 17, the exponential series, and factorial growth. It is an exact construction and needs no numerical computation. It is not a counterexample to the Brjuno convergence theorem, which concerns pure series at irrational parameters, and is not an example of a divergent stationary IPM logarithmic series.
