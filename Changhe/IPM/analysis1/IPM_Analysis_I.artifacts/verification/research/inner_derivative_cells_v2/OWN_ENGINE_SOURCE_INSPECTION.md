# Independent source inspection before the inner run

Written 2026-10-22T09:37:01.698497+00:00. This is source reasoning only. No181smoke or full cell computation has run, and no new enclosure is accepted here.

Read both complete sources engine_arb.py and engine_iv.py. For exp(lambda tau) times a degree-six polynomial, after tau=tc+h z the omitted exponential terms start at N=Q-l+1. Leibniz differentiation gives the primary physical derivative tail

 |b_l| exp(lambda tc) exp(|lambda h|)|lambda h|^N h^-p sum_(q=0)^p binom(p,q)(l)_(p-q)/(N-q)!.

N>2 ensures every factorial through p=2 is defined. This follows from sum_(j=N)^infty (j)_q x^j/j! <=exp(x)x^N/(N-q)!. It bounds the derivative of the remainder, not merely its value. The independent engine differentiates each analytic exponential-polynomial first and expands the result to degree Q-p. The exact Taylor coefficients of that analytic derivative equal the differentiated original Taylor coefficients. The saved overlap counts test that relationship but do not themselves prove it.

The physical Green ODE recurrence represents y'=lambda y+sig G. For the degree-Q recurrence polynomial, the defect is d z^Q with |d| bounded from lambda p_Q+sig G_Q. Integrating from z=0 in either direction gives e0<=exp(|lambda h|)h(|d|/(Q+1)+eG0); differentiating the error equation gives e1<=|lambda|e0+eG0+|d| and e2<=|lambda|e1+eG1+Q|d|/h. The sources implement these expressions. The independent engine uses the explicit coefficient sum for the ODE rather than the recurrence, and density moments rather than the physical forcing moment pair.

In the independent angular convolution, cosine models carry half coefficients and sine models carry opposite full coefficients. This represents the common factor2i times the sine product. The positive output coefficient therefore is the physical sine coefficient. Frequencies522 and521 give maximal residual frequency1043. The summed derivative remainder is weighted by1043 for angular differentiation; this is a finite spectral bound. The primary full convolution and the independently quantized integer convolution retain all degrees through2Q. Bernstein evaluation applies to the first Q+1 terms and the high-degree derivative coefficients are bounded separately in absolute value.

The physical norm-cell weight is L^6 exp(-4t)(1+exp(2t)/L^2)^(3/2-k). Its logarithmic derivative is -4+(3-2k)u^2/(1+u^2)<0 for the exact k range, so the left endpoint supplies the upper weight. Parseval contributes pi, and the physical interval width is b-a. The bounds for eps-D eps use triangle inequalities on each radial and angular derivative before squaring. They are upper bounds, not estimates of actual cancellation.

The exact canonical input identity, center-strain removal, all input enclosures, actual cell coverage, storage completeness, two-engine audits, selected replays and actual completed model review still need the prepared workflow and executed data. The current source inspection does not discharge those remaining execution obligations.
