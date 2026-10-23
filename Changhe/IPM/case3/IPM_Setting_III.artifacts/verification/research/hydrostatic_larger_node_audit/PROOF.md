# Result 318: independent larger-grid hydrostatic node audit

Written UTC 2026-10-22T04:11:47.753378+00:00, before new candidate evaluation.

## Exact statement and scope

This finite audit reconstructs the collocation coordinates specified by the
stored N192/M48 and N224/M56 auxiliary hydrostatic trials. It recomputes
their density jets and complete vertical inverse independently of the
producer's code, then compares sampled regional residual maxima with note166.
It does not authenticate historical solver matrices or exported coordinates:
the coordinate lists here are reconstructed from the stated convention.
The resulting finite comparisons are not a full-plane elliptic IPM inverse,
a proof of hydrostatic existence or exclusion, or an error enclosure.
The main endpoint remains UNRESOLVED.

## Fields, coordinates and complete inverse

The numeric checkpoint supplies local Chebyshev coefficients of
b_k(t), in the stored affine coordinates for each k, and ordered Radau
basis nodes t_k. With P=2, L=1, sigma=(1+t)/2 and w=(1-t)/2,
r=L sqrt(sigma)/(1-t)^P and
 g(x,y)=y w sum_(k=0)^(M-1) sigma^k b_k(t) cos(2k theta).
The formula has even-x, odd-y parity. The reader's safeguarded inversion
retains sigma and w separately. Our Cartesian differentiation recurrence,
already derived and tested in independent_hydrostatic_evaluator/PROOF.md,
gives J=(g,g_x,g_y,g_xx). It uses no producer derivative or inverse.

For radial indices i=1,...,N, reconstruct r_i from stored t_i and take
 theta_j=(j+1/2) pi/(2M), j=0,...,M-1,
 (x_ij,y_ij)=(r_i cos theta_j,r_i sin theta_j), in radial-major order.
All coordinates are positive and finite; axes are not sampled here. The
coordinate formula is checked against the known96 export as a manufacture
of this reconstruction, not as authentication of192/224 historical arrays.
A separate scalar forward-map/inverse check and trigonometric parity tests
must be made for every state.

For x,y positive, define
 V1=-integral_y^infinity g_x(x,t) dt,
 V2=integral_0^y t g_xx(x,t) dt + y integral_y^infinity g_xx(x,t) dt.
The formulas and auxiliary gauge V2(x,0)=0 are proved in the earlier
independent inverse proof. In particular d_y V2=integral_y^infinity g_xx,
so d_x V1+d_y V2=0. This is a vertical hydrostatic inverse, not the
elliptic inverse required for the main IPM problem. For these finite
representations g is asymptotically order r^(1/2), and the fixed-x
horizontal derivatives make these integrals convergent. The previously
proved t=R/u^2 substitution includes the whole infinite tail, not a wall.

## Residual arithmetic and comparisons

Use c=2, R=(2x+V1)g_x+(2y+V2)g_y-g,
 Nf=abs((2x+V1)g_x)+abs((2y+V2)g_y)+abs(g),
 Nv=abs(g)+abs(xg_x+yg_y)+abs(V1g_x+V2g_y).
Every binary64 input operand is converted exactly to a rational, these
expressions are evaluated exactly, and each final diagnostic is rounded
once. A zero denominator produces an undefined ratio and an explicit count.
There is no arbitrary denominator floor. Regions use binary64 hypot at
boundaries0.1,1,100. Retain signed R and both denominators at each separate
maximizer; no ratio of regional maxima is substituted for a pointwise ratio.

Rule B uses physical dyadic panels, order64, tail order192, split factor128,
and inner scale1/8, exactly the independent implementation in result309.
Run B at every reconstructed node, N224 first. After each state, select the
union of its regional absR/Rf/Rv maxima, each component's absolute maximum,
absolute gxx and five-point finite-difference gxx-proxy maxima, first/middle/
last indices, and inner/outer panel-width/count extremes. The proxy is only
a witness selector, never an error estimate. At all selected points run A
(order48,tail160,split64,dyadic) and C(order88,tail256,split512,ratio3/2).
Report every pairwise component discrepancy, exact residual spread,
spread/abs(R_B), and spread/Nf_B, with explicit zero cases. A and C are
selected-point sensitivity tests, not all-node verification.

Before final numerical acceptance, independently recompute all stored
residual arithmetic and summaries, and evaluate the selected local jets
with the separately implemented scalar density at72/108digits. An MP
same-node integrand check at the global Rf maximizer of each state is
planned separately. The all-node stage alone has no MP accuracy verdict.
Neither MP precision agreement nor A/B/C agreement bounds common error.
Pure relative differences use abs(a-b)/max(abs(a),abs(b)); both-zero pairs
are counted as undefined. Printed producer values are finite rounded
observations. Any disagreement is reported without assuming either finite
rule equals the exact integral.

## Reproducibility, manufactured tests and integrity

All source hashes, state hashes and static claim files are bound before
execution. Candidate data must not be substituted after selection.
A new atomic snapshot stores coordinates, own jets, velocity, Phi,
dV2dy, tail components, metadata and residuals. On restart, validate schema,
shape, finite prefix, undefined-ratio convention, empty suffix, source
hashes and indices; replay the boundary row. Final verification separately
recomputes every residual and selected quadrature rows. This is restart
integrity, not authentication of arbitrary histories.

Manufactures cover hand residuals, zero ratios, ties, empty regions,
coordinate reconstruction at96, phase interruption/resume, altered bindings,
invalid suffixes and altered replay rows. Existing analytic manufactured
inverse tests are reused only through their bound proof, code and evidence.
The candidate stage follows actual Opus5.5 design review and independent
resolution of any objections. No producer code is imported or executed.
A single low-priority, single-threaded process runs under14GiB and a4h cap;
no second heavy process starts while it runs. Commands finish within10min.
All writes stay in this lane. No JavaScript/TypeScript/Node, servers,
listeners, tunnels, RLScience, Lean/Lake, commits/push/posts or human contact.

## Limits of interpretation

A sizable resolved-rule residual at reconstructed collocation nodes cannot
be explained solely by sampling between those nodes. It also cannot
exclude additional off-node aliasing. Without a same-jet actual-map export
or independent evaluation of the stated map rule, its cause cannot be
assigned exclusively to map quadrature. Historical solver node maxima are
metadata, and can include normalization rows. The source of nonlinear
stalls, the exact integral error and infinite-sequence convergence remain
open. No finite result here can change the main UNRESOLVED verdict.

Reading order: this proof; the bound independent inverse and density proofs;
INPUTS; manufacture/design gates; finite all-node results; separate MP and
final arithmetic audit; RESULTS when published.
