# The global zero set and quadrant dynamics of the normalized modal field

## Exact background and statement

Let rho be the normalized, exactly joined modal density of proof 04,
constructed from the original trial_v2_h0.008.npz with SHA-256

a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874.

The binary64 input coefficients are exact dyadic rationals. Endpoint
corrections match derivatives through order six. The scalar outer
normalization correction is its unique exact real value, not the
midpoint of a numerical enclosure. Put

 k=1615536043799051/9007199254740992, ell=1/k,
 -Delta psi=partial_x rho, U=(-partial_y psi,partial_x psi),
 V=ell X+U.

Use the canonical full-plane Green construction specified in proof 04.
Define exact rational numbers

 pminus=4841405518533377/562949953421312,
 pplus =4841405518533711/562949953421312,
 qminus=4559930541822721/562949953421312,
 qplus =5122880495244367/562949953421312,
 Qplus=[qminus,qplus] times[-1/2,1/2],
 Qminus={(-x,y):(x,y) in Qplus}.

There is p in [pminus,pplus] such that the full-plane zero set is
exactly {0,(p,0),(-p,0)}. Put P=(p,0). Outside Qplus union Qminus and
away from the origin,

 |V(X)|/|X| >= 3/12500 = 0.00024.                              (1)

Inside Qplus,

 |V(X)| >= 0.1801 |X-P|,                                     (2)

and the reflected inequality holds in Qminus. Both nonzero equilibria
are hyperbolic repellers. The origin is a saddle with linearization

 DV(0)=diag(-A,D), A=2ell-1>0, D=4ell-1=2A+1.

Every trajectory in the open first quadrant has alpha-limit P and
escapes to infinity in forward time. On the positive x-axis, the
segment (0,p) flows from P to0 and the ray (p,infinity) flows from P to
infinity. The positive y-axis flows from0 to infinity. Reflections give
the corresponding statements in the other quadrants.

Every compact set K containing none of the three zeros has a smooth
compactly supported escape function phi with V.grad phi>=1 on K.
If K is invariant under both axis reflections, phi can be chosen even
under both. No quantitative derivative bound for phi is asserted.

These statements concern this specified modal trial. They do not say
that rho solves the stationary IPM equation.

## Source patch and origin

Proof 15 proves the bracket for p, V(P)=0 and

 DV(P)=diag(A_P,mu_P), A_P>10, mu_P>0.99999997745.

The independent source-patch calculation in proof 66 and its V070
audit give ||D^2 V||_F<1.159484 on Qplus and
S(DV)>0.1801 I there. Integrating DV on the segment from P to X gives

 (V(X)-V(P)).(X-P)>=0.1801 |X-P|^2.

Cauchy-Schwarz proves (2) and uniqueness of the zero throughout the
closed patch. Axis reflection gives the same assertions for Qminus.
The exact normalization and inner expansions in topics04 and52 give
the stated origin linearization and V(0)=0.

## Independent cover of the complement

Proof 72's independent_cover.py reconstructs the modal Green data from
the original input, using the separately accepted original-data cache
of proof 68. It covers the closed first quadrant in polar coordinates
(t,theta), with t=log r. Each of the1558 nondegenerate original spline
spans is divided into two exact radial intervals. A further160 exact
radial intervals cover eight log units of the explicit outer tail.
Thus there are3276 finite radial cells. Each is initially crossed
with128 angular intervals [j*pi/256,(j+1)*pi/256], 0<=j<128.

For each box, interval arithmetic encloses q=V_r/r and v=V_theta/r.
The elementary inequality

 |V|/r >= sqrt(dist(0,Iq)^2+dist(0,Iv)^2)

gives a lower bound. There are419220 initially positive boxes. The
remaining108 initial boxes are bisected with exact rational endpoints
until each terminal box is either positive or inside Qplus. This gives
140 positive refined terminal boxes and47 terminal boxes in Qplus.
No unresolved box remains. The exact Qplus containment test uses the
three monotonic extremal formulas of proof 72, including all boundaries.

The two infinite radial ends use the accepted analytic Green error
bounds of proof 68. If E_P bounds the radial mode error sum and E_T
bounds sum_n 2n times the angular mode error, their vector error has
norm at most E_P+E_T/2. The limiting inner field satisfies
|V00(X)|/r>=A; the limiting outer field satisfies |ell X|/r=ell.
Consequently A-E_P-E_T/2 and ell-E_P-E_T/2 are valid end bounds.
Both are positive and exceed (1).

All finite boxes and both ends have lower bound at least3/12500. The
smallest stored exact endpoint is approximately
0.000240912559929205850488186750079. This approximation is diagnostic;
the accepted short bound (1) is the exact rational3/12500.

## Separate acceptance audit

The audit_independent.py calculation uses640-bit arithmetic. It checks
input, script, proof and cache hashes, reconstructs all3276 radial
intervals from the original knots, verifies their adjacency and the
agreement with both end cutoffs, and checks the full initial angular
count. For every exceptional parent it checks that the closed terminal
rectangles are inside the parent, have disjoint interiors and sum to
its exact rational area. A finite union of closed rectangles with these
properties covers the whole parent: any omitted point would have a
relative open neighborhood of positive area. Hence there is no gap at
an edge or vertex.

The audit independently recomputes all140 exceptional positive boxes
at640 bits, checks the saved interval-distance inequalities in exact
rational arithmetic, verifies all47 Qplus containment tests and both
end formulas, and verifies the global aggregation. It passed at
2026-10-28T05:50:38.271404+00:00. The complete cover SHA-256 is

e10701a9aee56c3f1067dbb49aae63cdf236d9faf272f10e54bbdd45064346c7.

The source reconstruction, Green formulas, finite Taylor remainders,
angular interval formulas and analytic end bounds are justified in
topics19,56 and68. Arb's outward interval arithmetic and exact integer
arithmetic are computational dependencies. No value from a floating
sampling grid enters this acceptance.

Every nonzero point outside Qplus in the closed first quadrant is
therefore nonstationary. The origin and source-patch results show that
its only zeros are0 andP. Equivariance under each axis reflection gives
the stated full-plane zero set and the global inequality (1).

## Dynamics and escape

Proof 52 proves that V is globally Lipschitz and C1, has the axis
symmetries, div V=2ell>0, and satisfies

 V(X)=(-Ax,Dy)+O(r^3) at0,
 V(X)=ell X+O(r^k) at infinity, 0<k<1.

The global zero-set hypothesis of proof 60 is now established, and its
source is a repeller by the certified diagonal linearization. The
proof of proof 60 applies with exactly these hypotheses: backward
orbits are bounded by the outward radial field at infinity; periodic
orbits are excluded by the divergence theorem; the planar limit-set
theorem and the invariant axes exclude an interior limit at the saddle.
Thus interior backward limits are P and forward trajectories escape.
The scalar signs on the axes give the remaining orbit descriptions.

For completeness the compact escape assertion uses the separate
argument in proof 60, not a quantitative return-time estimate. Failure
of a smooth function with positive directional derivative on K would,
by separation and Riesz representation, produce an invariant
probability measure supported in K. Its compact invariant support has
no equilibrium. The planar limit-set theorem would then give a
periodic orbit, contradicting positive divergence. Scaling the positive
minimum gives V.grad phi>=1. Averaging over the two reflections gives
the even choice when applicable.

## Dependencies and remaining limits

Dependencies: topics04,15,19,52,56,60,66,68,69 and72 with their cited
accepted audits. The global flow is qualitative. No high-regularity
inverse, injectivity of the linearized nonlocal operator, complement
inverse, nonlinear contraction, or existence of an exact IPM profile
follows from the zero-set theorem alone.
