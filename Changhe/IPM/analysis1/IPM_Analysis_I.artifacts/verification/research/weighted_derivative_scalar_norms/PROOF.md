# Conditional weighted derivative norms from cell majorants

2026-10-21. This argument precedes the new arithmetic. It concerns a finite collection of derivative majorants, not an independently verified physical residual.

## Statement and hypotheses

Fix exact real numbers L>0 and 0<k<1. Put r=exp(t), u=r/L, m=u^3(1+u^2)^((k-3)/2), and w=m^(-2)(1+u^2)^(-3/2). For a measurable radial set E and an odd sine expansion f(r,theta)=sum_{N>=0} f_N(t)sin((2N+1)theta), define

||f||_(X(E))^2 = integral_{r in E, 0<=theta<2pi} [f^2+r^2|grad f|^2]w r dr dtheta.

Assume the series and first derivatives converge in the weighted square-integral sense. Let I_i=[a_i,a_i+h_i], h_i>0, be finitely many log-radius intervals. Suppose throughout I_i the nonnegative constants W_pq,i majorize sum_N (2N+1)^q |partial_t^p f_N(t)| for (p,q)=(0,0),(1,0),(2,0),(0,1),(1,1). These are explicit hypotheses about f, not consequences of importing numbers.

Define g=f-partial_t f and
A_i=W00_i^2+W10_i^2+W01_i^2,
B_i=(W00_i+W10_i)^2+(W10_i+W20_i)^2+(W01_i+W11_i)^2.
Then, for E=exp(union_i I_i),

||f||_(X(E))^2 <= pi sum_i h_i v(a_i) A_i,
||g||_(X(E))^2 <= pi sum_i h_i v(a_i) B_i,
v(t)=L^2u^(-4)(1+u^2)^(3/2-k).

The sums allow overlaps. They do not cover gaps or either omitted infinite tail. For a restricted physical region, summing every interval that intersects the region still gives an upper bound on its covered part, and may include excess measure.

## Proof

Orthogonality of sine and cosine frequencies over the full circle gives
||f||_(X(E))^2=pi integral_{log E} v(t) sum_N [f_N^2+(partial_t f_N)^2+(2N+1)^2 f_N^2]dt.
The factor v follows from r dr=exp(2t)dt and r^2|grad f|^2=|partial_t f|^2+|partial_theta f|^2. For nonnegative b_N, sum b_N^2 <= (sum b_N)^2. Apply this separately to the three terms. For g, use triangle inequalities for each coefficient and its t and theta derivatives. This yields A_i and B_i.

Differentiating log v with respect to t gives -4+(3-2k)u^2/(1+u^2), which is strictly negative for0<k<1. Thus v(t)<=v(a_i) on I_i. Integrating each interval gives the inequalities. The integrand is nonnegative, so summing overlapping intervals dominates the integral over their union. The same argument applied to the intersections with a radial region proves the restricted assertion. Truncation of the Fourier series followed by weighted convergence justifies the countable case.

## What this cannot prove

An upper bound for ||g||_(X(E)) on a bounded annulus gives no upper bound for ||g||_X on the full plane. For an explicit logical counterexample, choose a nonzero smooth radial function chi compactly supported outside E, away from zero, and H(r,theta)=chi(r)sin(theta). Then H has zero norm on E and positive finite full-plane norm. Arbitrary multiples have arbitrarily large full norm. This example demonstrates failure of an inference from restricted norms alone; it is not an alternative residual of the fixed IPM trial.

If the actual scaling vector K lies in the graph domain, LK=g, and a full-plane estimate ||h||_X<=C||Lh||_X holds there, then C>=||K||_X/||g||_X. A numerical lower bound on C obtained in this way requires a rigorous positive lower bound on the numerator and a rigorous full-plane upper bound on the denominator. A floating numerator, a conditional majorant, or a finite-annulus denominator does not supply those premises. This does not disprove the actual numerical quotient.

## Arithmetic and geometry audit plan

Interpret each saved binary64 t_a,h,W exactly as its dyadic value. Independently compute the displayed finite sums using Arb and mpmath.iv, including all input conversion, exponentials, powers, pi and square roots. Compare saved and printed rounded values only at the scalar level. Check adjacent literal intervals for gaps and overlaps using exact rational arithmetic; do not silently regard floating endpoints as a proven exact partition. Record the extreme radii as interval evaluations. The theorem is conditional on physical derivative majorants and coverage. No global inverse or decisive IPM endpoint is asserted.
