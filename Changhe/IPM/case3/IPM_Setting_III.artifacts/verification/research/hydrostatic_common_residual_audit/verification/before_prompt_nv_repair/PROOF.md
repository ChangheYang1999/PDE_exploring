# Independent common-point residuals for seven auxiliary trial states

Result287. Written before new evaluation at 2026-10-21T21:08:41.009997+00:00. This is a diagnostic of the epsilon=0 hydrostatic auxiliary equation. Its inverse is not the two-dimensional IPM inverse, so no result here supplies an admissible full-plane candidate or a YES endpoint. The main problem remains UNRESOLVED.

Let g be a frozen numerical density, even in x and odd in y, with formal far-field exponent p=1/c in (0,1). On the upper half-plane define

    V1(x,y) = - integral_y^infinity g_x(x,t) dt,
    V2(x,y) = integral_0^y t g_xx(x,t) dt
              + y integral_y^infinity g_xx(x,t) dt.

Extend by the required parities. Differentiating the integrals gives div V=0 and the auxiliary stream function Phi with Phi_yy=g_x and V=(-Phi_y,Phi_x). The choice of the integrals to infinity supplies the auxiliary canonical closure, not a freely added strain. The decay g_x,g_xx at fixed x is sufficient for these integrals for each frozen density, as proved and manufactured-tested in the existing independent inverse results. The full tail is integrated; no finite outer wall is imposed.

Put W=(c*x+V1,c*y+V2). The signed residual and denominators are

    Rh = W1*g_x + W2*g_y - g,
    Nf = |W1*g_x| + |W2*g_y| + |g|,
    Nv = hypot(W1,W2)*hypot(g_x,g_y) + |g|.

Both normalized residuals use their own pointwise denominator. At y=0, parity gives g=g_x=V2=0, hence Rh=Nf=0. These points have no defined Rh/Nf ratio and are excluded from that maximum; their absolute residual is retained. Nv need not vanish on that axis. A zero denominator is recorded explicitly rather than replaced by an epsilon floor. At other points with Nf=0 all three terms vanish and Rh=0. By the Cauchy-Schwarz inequality Nf<=Nv. Every reported regional maximum must include its physical coordinates, signed residual, denominator and velocity, and distinguishes a maximum of pointwise ratios from a ratio of maxima.

The target producer table uses 37 logarithmic radii from 10^-3 to 10^6 and nine equally spaced quadrant angles, including both axes, for 333 points. Use these common reporting points only; our differentiator is the independently derived analytic Cartesian jet of the coefficient expansion, and the inverse uses physical dyadic Gauss-Legendre panels and the full tail t=R/u^(1/(1-p)). The three rules are (finite order, tail order, split multiplier)=(32,96,16),(48,160,64),(64,192,128). Our implementation imports no producer evaluator, differentiated closure or quadrature code. The coefficient files and the reporting point definitions are inputs, not evidence of correctness. In particular the independently audited coefficient loader is retained and bound by hash.

The five regions are [0,.1), [.1,1), [1,100), [100,10^4), [10^4,10^6]. The producer's last label is half-open after rounding 10^6+1, but its code includes radius10^6. We include that endpoint and record it. Quadrant axis coordinates are set exactly to zero by their index, avoiding a trigonometric roundoff coordinate in an exact parity test. The other common coordinates are recomputed independently.

Compare the signed residuals and both normalized ratios across the three inverse rules. For any material discrepancy with a printed token, refine its maximizing point and adjacent potential maximizing points with a separately implemented adaptive Gauss-Kronrod inverse. Existing exact manufactured tests for the analytic jets, fixed inverse and adaptive inverse must match the module hashes used. Quadrature agreement is observed numerical sensitivity, not a certified error enclosure. If a displayed token cannot be reproduced at its own rounding precision, record the mismatch rather than loosening the tolerance. The source's comparison of its standard and doubled quadrature is not a proof of absolute error, and our independent comparison cannot reproduce that producer-only difference without running its code.

The seven states are four c=2 states (N=96,128 continued,160,192) and three c=3 states (N=64,96,128). They remain auxiliary trial states, with exact center and cubic compatibility defects already audited in prior results. Finite sampled residual improvement does not establish convergence, smoothness, a uniform global bound or an exact auxiliary solution. It has no direct implication for the primary IPM endpoint.

All files and computation remain in the verifier lane. No JavaScript/TypeScript/Node, servers/listeners/tunnels, RLScience cluster, Lean/Lake, commits/push/posts. Run one heavy process, single-threaded at nice19 and below16GB. Preserve failed gates before any repair.
