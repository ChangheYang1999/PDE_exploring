# Factorial-norm growth need not prevent exterior convergence

Status: PROVED after the independent theory-part review at06:30Z, retained in sources/lead_review_0630.md. It satisfies the potential and Poisson identities but deliberately does not satisfy the stationary nonlinear recurrence.

## Statement

Set delta=2/3, c=3, t=log r, q_n=4-2n/3, and

\[
 k_n=\max\{0,\lfloor(n-1)/3\rfloor-1\},\qquad a_0=-27/400.
\]

Consider the radial potential coefficients

\[
 \chi_n(r)=a_0r^{q_n}t^{k_n},\qquad \chi=\sum_{n\ge1}\chi_n,
\]

and define each stream and density term from this same potential by

\[
 \psi_n=\partial_x\partial_y\chi_n,
 \qquad \rho_n=-\partial_y\Delta\chi_n.
\]

Then all three series converge absolutely and uniformly, with every fixed Cartesian derivative in its natural radial weight, on r>=e. Their sums are real analytic there. The leading density is r^(1/3)sin(theta), the stated S1 symmetry holds, and the stream is the canonical polynomial-log Poisson solution with zero resonant constants at every order.

Nevertheless, for every fixed s>0, the density and stream coefficient norms ||F_n||_{!,s} and ||G_n||_{!,s} grow faster than every geometric sequence. In fact

\[
 \lim_{n\to\infty}\frac{\log\|F_n\|_{!,s}}{n\log n}
 =\lim_{n\to\infty}\frac{\log\|G_n\|_{!,s}}{n\log n}=\frac13.
 \tag{1}
\]

These statements show that factorial-norm Gevrey growth alone cannot prove divergence of a physical exterior series, even when the potential identities, Poisson equation, canonical resonant constants and rational log-degree bounds are imposed. They do not settle convergence of the actual stationary IPM recursion.

## Exact coefficient formulas

Write D=partial_t and H_n=a_0t^(k_n). For a radial function, direct Cartesian differentiation gives

\[
 \partial_x\partial_y\{r^qH(t)\}
 =\tfrac12r^{q-2}(q+D)(q-2+D)H(t)\sin(2\theta),
\]

\[
 -\partial_y\Delta\{r^qH(t)\}
 =-r^{q-3}(q-2+D)(q+D)^2H(t)\sin\theta.
\]

Consequently

\[
 G_n=\tfrac12(q_n+D)(q_n-2+D)H_n\sin(2\theta),\qquad
 F_n=-(q_n-2+D)(q_n+D)^2H_n\sin\theta.
 \tag{2}
\]

The density and stream radial exponents are q_n-3=1-2n/3 and q_n-2=2-2n/3, as required. At n=1, q_1=10/3 and k_1=0; the choice of a_0 gives F_1=sin(theta) and G_1=-(3/20)sin(2theta).

The Poisson identity follows from commuting derivatives:

\[
 -\Delta\psi_n=-\partial_x\partial_y\Delta\chi_n=\partial_x\rho_n.
\]

Every stream coefficient has only frequency2. Its only possible genuine resonance is n=6, where q_6=0 and k_6=0, so G_6=F_6=0. At all other resonant orders the resonant angular frequency is absent. Thus every resonant constant is zero. The density log degree is at most k_n, exactly the canonical degree upper bound at delta2/3; the stream degree is also at most k_n and hence obeys its own upper bound. The potential is even in both Cartesian coordinates and its derived density has S1 symmetry.

## Uniform convergence of all derivatives

For t>=1, every fixed derivative of r^(q_n)t^(k_n) is bounded by a fixed polynomial in n times r^(q_n-h)t^(k_n), where h is the derivative order. To see this directly, each Cartesian derivative introduces a radial factor r^(-1), a bounded trigonometric factor, and an operator formed from q_n, an integer shift, D and an angular derivative. The degree in t never increases, k_n<=n, and t^(k_n-l)<=t^(k_n) whenever t>=1. After a fixed number of derivatives, only a fixed number of such terms occur, each with a polynomial coefficient in n.

After removing the leading radial weight, the common exponential factor is bounded by

\[
 r^{-2(n-1)/3}t^{k_n}
 \le \left(t^{1/3}e^{-2t/3}\right)^{n-1}.
\]

For t>=1 the function inside parentheses decreases, since the derivative of its logarithm is1/(3t)-2/3<0. It is therefore at most e^(-2/3)<1. A geometric series with any fixed polynomial factor in n converges. This proves the claimed uniform weighted derivative convergence for chi, psi, rho and the velocity u=(-psi_y,psi_x). The respective leading radial exponents are10/3,4/3,1/3 and1/3.

At every exterior point, r, theta and a branch of log r have holomorphic extensions to a sufficiently small complex neighborhood. The strict geometric margin above persists on a smaller such neighborhood. Hence the convergent sums are real analytic. Termwise differentiation proves the potential and Poisson identities for the sums.

## Growth in every fixed weighted factorial norm

The potential coefficient has exact norm |a_0| k_n!s^(k_n). For n>6, the top log coefficients of (2) are nonzero and give

\[
 \|F_n\|_{!,s}\ge |a_0|\,|q_n-2|q_n^2\,k_n!s^{k_n},
\]

\[
 \|G_n\|_{!,s}\ge \tfrac12|a_0|\,|q_n(q_n-2)|\,k_n!s^{k_n}.
\]

Conversely ||D||_{!,s}<=1/s, so the operator factorizations in(2) bound each norm above by the same factorial factor times a polynomial in n. Since k_n/n tends to1/3, the elementary asymptotic log(k!)=k log k-k+O(log k) proves(1). Thus neither sequence is geometrically bounded in this fixed norm, despite the physical exterior convergence already proved.

## This is not a stationary IPM solution

The nonlinear recurrence is intentionally absent from the construction. It already fails at order2. Formula(2) gives F_2=(8/25)sin(theta), whereas the stationary recurrence generated by F_1=sin(theta) and G_1=-(3/20)sin(2theta) gives

\[
 F_2^{\rm stationary}=-(3/40)\sin\theta-(1/40)\sin(3\theta).
\]

The order2 stationary residual is therefore

\[
 -\lambda_2F_2+J_{1,1}(G_1,F_1)
 =-(79/100)\sin\theta-(1/20)\sin(3\theta)\ne0.
\]

This explicit failure is part of the scope of the counterexample. A proof that the actual generated stationary sequence diverges would still require information beyond growth in the weighted factorial norm alone.

## Dependencies and verification

Only exact Cartesian derivatives, a geometric series estimate and factorial asymptotics are used. The accompanying check compares the radial formulas against the independent Laurent Cartesian derivative engine over a finite set of orders, verifies the canonical resonance condition and evaluates the order2 residual exactly. The all-order argument is the proof above, not the finite computation.
