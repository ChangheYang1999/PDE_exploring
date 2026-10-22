# Angular transition widths and the location of a possible jump

Written 2026-10-21T04:06:55.232743+00:00 before implementation. Status: proved elementary diagnostic statements, no assertion about a B2 solution or continuation limit.

## Definitions and exact claims

Write delta=pi/2-theta on the right side of the upper half-axis. For a smooth x-odd vorticity field with a smooth angular tail, the rescaled curve a(delta) vanishes at delta=0 and extends oddly through0. Fix an angular cap d in(0,pi/2). Suppose a'(0)>0 and let delta_p be its first positive local maximum in(0,d], or d if a is increasing throughout this interval. Put A_p=a(delta_p)>0. When the curve is strictly increasing on(0,delta_p), define delta_q uniquely by a(delta_q)=q A_p for q=0.1 and0.9. The width is w=delta_0.9-delta_0.1. These quantities describe an adjacent peak or band endpoint. They do not establish the existence of a plateau, and should not be labeled plateau measurements without checking flatness on an interval.

The mean value theorem gives a point between the two crossings where

    a'(delta_*)=0.8 A_p/w.

It does not locate that large derivative at the axis. If a sequence has A_p>=A_*>0 and delta_0.9 tends to0, it cannot converge uniformly near0 to a continuous curve taking value0 there: uniform convergence and continuity would give a_n(delta_0.9)->0, whereas the values are at least0.9 A_*. This is an exclusion of a continuous uniform limit, not of pointwise or weak limits, and not a statement about finite continuation data.

## A necessary location qualification

Growth of the axis slope Q_n, a shrinking 10-to90 percent width of order1/Q_n, and an order-one height do not by themselves locate a limiting jump on the axis. Fix delta_0>0 and for n>=2 define the smooth odd increasing function

    a_n(delta)=tanh(n^2 delta)/n
        +(1-1/n)[tanh(n(delta-delta_0))+tanh(n(delta+delta_0))]/2.

It has a_n(0)=0, a_n(+infinity)=1 and

    Q_n=a_n'(0)=n+(1-1/n)n sech^2(n delta_0) ~ n.

For every fixed0<delta<delta_0, a_n(delta)->0; for delta>delta_0, a_n(delta)->1. Thus there is no jump across the axis; the transition is at delta_0. For a fixed q in(0,1), set delta=delta_0+t/n. Uniformly for bounded t, a_n(delta) tends to(1+tanh(t))/2. Strict monotonicity and this locally uniform convergence imply

    n(delta_q-delta_0) -> artanh(2q-1),
    n w_n -> 2 artanh(0.8)=log9.

To justify inversion, choose t_- and t_+ on opposite sides of artanh(2q-1); the two limiting function values straddle q, so for all large n the unique crossing lies between them. Let t_- and t_+ approach the target. Consequently w_n Q_n ->log9 even though both crossing angles tend to delta_0, not0. The example can be used on a fixed angular neighborhood with d>delta_0 and extended smoothly away from that neighborhood. It is a counterexample to the diagnostic inference only; it is not a PDE solution or a represented branch state.

## Extraction from saved finite angular fields

In the saved convention phi=theta+pi/2, the upper-axis approach has phi=pi-delta. If the independently evaluated radial coefficients of G are g_k(r), then

    a_r(delta)=r^(1+s) sin(delta) sum_k (-1)^k g_k(r) T_k(cos(delta)),
    a_r'(0)=r^(1+s) sum_k (-1)^k g_k(r),  s=1/beta.

For r tending to infinity in a native r2 archive, g_k(r)~L^(1+s)r^(-1-s) c_k, where c_k is the exact spline endpoint of the stored coefficient polynomial; the radial factor t^min(k,2) tends to1. The limit is a_infinity=L^(1+s)sin(delta) S(cos(delta)), S(z)=sum(-1)^k c_k T_k(z). This is the actual stored field's angular tail, not the solution obtained by transporting its temperature with a separately prescribed velocity.

For a curve sin(delta)S(cos(delta)), its derivative is

    D(cos(delta)),  D(z)=zS(z)-(1-z^2)S'(z).

Thus possible adjacent extrema can be found through a separately implemented Chebyshev polynomial derivative and root computation, then checked by direct trigonometric evaluation and an independent high-precision root calculation. Because this is floating numerical root finding, all unverified isolation, monotonicity and sampling limitations must be stated. The archive's axis slope and the axis-ODE functional of packet112 answer different questions whenever its PDE or center relations have nonzero residuals. Neither may be substituted for the other.

## Scope and dependencies

Only elementary differentiation, the mean value theorem, monotone inverse convergence, the radial envelope in the explicitly inspected archive format, and the independent reader's endpoint formula are used. This result adds a location diagnostic; it proves no smoothness loss along the actual lambda path and excludes no B2 profile. Record delta_0.1, delta_0.9, delta_p, A_p, w and Q, and their finite-radius versus exact-tail distinctions, before making a limiting claim.
