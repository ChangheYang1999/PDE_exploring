# Invariance checks and the limits of the converse

The first actual Opus5.5 review accepted the complete theorem. We now check its added infinite-codimension example explicitly and add an example where Q does not commute. These are exact regression examples for the analytic argument, not tests of the IPM operator.

Take X=L2(R), S(t)f(x)=f(x+t), D(L)=H1(R) and Lf=f'. The generator identification follows by the Fourier multiplier (exp(i t xi)-1)/t: H1 gives convergence to i xi by dominated convergence, and convergence of the quotient in L2 forces xi*fhat in L2 by a subsequence and Fatou. Put phi=1_[0,1] and N=span{phi}. Its distributional derivative is delta_0-delta_1, not an L2 function, so D(L) intersect N={0}. The invariance condition on that domain holds vacuously. But S(t)phi=1_[-t,1-t], and for every t>0 this cannot be a scalar multiple of phi because the supports differ on a set of positive measure. Thus generator invariance alone can fail for a closed N without the finite-codimension or other resolving hypothesis. This verifies the review's example for an explicit phi; it is outside our theorem's premises and is not a counterexample to the theorem.

For a finite-dimensional check that Q need not commute, take the Euclidean space X=R2, a>0, b!=0,

 L=[[-a,b],[0,0]], N=span{e1}, M=span{e2}, Q=diag(1,0).

Then L^2=-aL and

 S(t)=I+(1-exp(-a t))L/a
     =[[exp(-a t),(b/a)(1-exp(-a t))],[0,1]].

Differentiation shows S'=LS and S(0)=I; direct multiplication or uniqueness of the finite-dimensional ODE gives the semigroup law. Its action on N is multiplication by exp(-a t), hence ||S(t)Q||=exp(-a t). But QS(t)-S(t)Q has upper-right entry(b/a)(1-exp(-a t)), nonzero for t>0. Here N is invariant while M is not. The theorem deliberately does not require M-invariance and uses Qn=n only. The inverse on N is multiplication by-1/a; BQ=diag(-1/a,0). The full L is singular. Thus BQ is not a full-space inverse, even though it has the claimed bound1/a. If the lead assumes both summands invariant, its stronger premises also suffice.

For the positive scalar generator L=1, semigroup growth is exp(t); for L=-1, the integral inverse is-1. This confirms both the inverse sign and the failure of the converse.

The final implication should be stated as follows: a dynamic-rescaling proof based on exponential decay of the realized linearized semigroup, after finitely many modulation directions are removed, supplies the stationary inverse on that same space and domain. It must establish that decay estimate, which is generally stronger than invertibility. This conditional implication does not assert a necessary feature of every possible dynamic method.
