# Polynomial logarithms do not permit finite termination

Status: CONFIRMED after independent adversarial review, 2026-10-31T03:52:43Z. See V049 and topic43 for the exact scope and evidence.

## Exact statement

Let c>1. Suppose, on an exterior domain, the real density and stream are finite sums

\[
 \rho(r,\theta)=\sum_{s\in S}r^s F_s(t,\theta),\qquad
 \psi(r,\theta)=\sum_{q\in Q}r^q G_q(t,\theta),\qquad t=\log r,
\]

where S and Q are finite sets of distinct real exponents. Each F_s and G_q is a nonzero polynomial in t with real analytic angular coefficients on the circle. Every angular coefficient of F_s is odd under theta -> -theta and even under theta -> pi-theta. Every angular coefficient of G_q is odd under both reflections. Assume S is nonempty, min S<1, and

\[
 -\Delta\psi=\partial_x\rho,\qquad
 c r\partial_r\rho-\rho+
 \frac{\psi_r\rho_\theta-\psi_\theta\rho_r}{r}=0.
 \tag{1}
\]

These assumptions are inconsistent. Consequently a nonzero stationary far-field solution with these analytic symmetries cannot be a finite polynomial-log expansion, even when arbitrary finite real exponent sets and density-free stream multipoles are permitted.

## Angular lemma

We use the lemma proved in topic 26: if f and g are nonzero analytic angular functions with the density and stream symmetries respectively, and a,b are real and not both zero, then

\[
 a g f'-b g'f
\]

is not identically zero. For completeness, their orders of vanishing at zero are positive odd integers s,t. An identity would force as=bt. At pi/2 the orders are a nonnegative even integer s' and a positive odd integer t', forcing as'=bt'. If either a or b vanishes, the first equation already contradicts the assumptions. If s'=0, the second equation contradicts b!=0. Otherwise elimination gives t s'=t' s, with an even left side and an odd right side. Analyticity guarantees finite vanishing orders.

## The least radial exponents

Let s_* be the least density exponent. Let f be the nonzero highest t-degree coefficient of F_(s_*), with degree K. The coefficient of the same highest t degree in the Cartesian derivative of r^(s_*) F_(s_*) is

\[
 s_*\cos\theta\,f-\sin\theta\,f'.
 \tag{2}
\]

If f vanishes to odd order v>=1 at zero, the leading Taylor coefficient in (2) is a nonzero multiple of s_*-v. Since s_*<1, it is nonzero. Thus this density term has nonzero x derivative. The Poisson equation requires a stream term at exponent s_*+1, so Q is nonempty and its least exponent q_* satisfies

\[
 q_*\le s_*+1.
\]

The least nonlinear radial exponent is therefore uniquely q_*+s_*-2. It obeys

\[
 q_*+s_*-2\le2s_*-1<s_*.
 \tag{3}
\]

Only the pair of the least stream and density exponents produces it. The linear terms in (1) have exponents in S, so none can cancel it. Distinct exponential-polynomial functions exp(lambda t) P(t) are linearly independent on any open half-line. Hence the entire polynomial-log coefficient at this least exponent must vanish.

Let g be the highest t-degree coefficient of G_(q_*), with degree M. The coefficient of t^(K+M) in this nonlinear term is

\[
 q_* g f'-s_* g'f.
 \tag{4}
\]

Radial differentiation of the polynomial itself only lowers the t degree. If (q_*,s_*)!=(0,0), the angular lemma shows that (4) is nonzero, a contradiction.

## The remaining zero-exponent pair

Suppose q_*=s_*=0. Since every density exponent is nonnegative, the right side of the Poisson equation has no radial exponent -2. The stream term at exponent zero must therefore solve the homogeneous equation

\[
 (\partial_t^2+\partial_\theta^2)G_0=0.
\]

In its highest t degree, this equation says g''=0. Periodicity forces g to be constant, and odd symmetry forces that constant to be zero. This contradicts the choice of g. The exceptional pair is impossible as well, proving the theorem.

## Dependencies and scope

The argument uses the independently derived Cartesian Poisson and stationary identities, the analytic vanishing-order lemma, polynomial degree, and independence of distinct real exponential-polynomial functions. It applies to the prescribed powers p_n=1-n delta, because their least density exponent is below one. It does not require rational delta. It does not treat infinite logarithmic series or establish their convergence or divergence. Analyticity matters: the proof does not cover smooth functions flat at an axis.
