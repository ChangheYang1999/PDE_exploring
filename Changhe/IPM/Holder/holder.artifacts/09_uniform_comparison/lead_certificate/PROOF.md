# A uniform quantitative comparison on every Holder exponent

## Statement, notation and scope

Use the real homogeneous Holder space and the increment-defined operators of
../../01_setup/PROOF.md. Thus 0<alpha<1, [f]_alpha is the supremum of
|f(x)-f(y)|/|x-y|^alpha, T_xx has kernel cos(2theta)/(2pi r^2), T_xy has
kernel sin(2theta)/(2pi r^2), and R_1^2=T_xx-I/2. Their seminorm operator
constants are C_alpha,C_alpha,D_alpha. The same constants arise from compact
smooth tests, by the approximation theorem there.

Define a positive lower function ell(alpha) as follows. For 0<alpha<1/200,

    ell(alpha)=(sqrt(2)-1)^alpha [4/(pi alpha(alpha+2))-1/4].

For 199/200<alpha<1, put

    J(alpha)=integral_0^(pi/6) sin((alpha+2)t) sin(t)^alpha dt,
    M(alpha)=(alpha+1)2^(alpha-1)J(alpha)/cos((alpha+2)pi/6),
    ell(alpha)=2^(1-alpha)(M(alpha)+1/4).

On [1/200,199/200], use the polygonal signed-distance witness I(alpha,a)
defined and evaluated in ../../05_team_audit/structured_layercake/PROOF.md,
with the fixed shape a from the following table. At a shared group endpoint
choose the group on its right, except that 199/200 belongs to the last group.

| alpha interval | shape a | exterior plan reference exponent |
|---|---|---|
| [1/200,19/100] | 14/25 | 1/20 |
| [19/100,7/20] | 53/100 | 27/100 |
| [7/20,1/2] | 97/200 | 17/40 |
| [1/2,3/5] | 89/200 | 11/20 |
| [3/5,7/10] | 39/100 | 13/20 |
| [7/10,4/5] | 33/100 | 3/4 |
| [4/5,9/10] | 53/200 | 17/20 |
| [9/10,199/200] | 1/5 | 24/25 |

The certified conclusion is

    ell(alpha) <= C_alpha <= 1.0825 ell(alpha),
    ell(alpha) <= D_alpha <= 1.2894 ell(alpha),       0<alpha<1.

In particular these yield explicit homogeneous seminorm inequalities for
T_xx,T_xy and R_1^2 with constants 1.0825 ell and 1.2894 ell. The sharper
piecewise upper functions used in the proof may be used instead. This is a
relative enclosure, not an exact finite-alpha norm formula. The verification
ledger controls acceptance of the numerical conclusion.

## Upper functions on the middle interval

For each table row fix the exterior integer transport plans in the saved
far2_g*.json certificate. There are 512 angular cells, 128 radial intervals
in u=1/r from 1/4 to 1, and phases j*pi/32, 0<=j<=16. Each plan is chosen at
the reference exponent and then kept fixed on the whole group. Exact
integer marginals, not solver optimality, establish feasibility. Its costs
are evaluated by the exterior-circle theorem of ../../08_improved_upper_bounds.

Write E_j(alpha) for these exterior costs, including the explicit positive
harmonic tail on 0<u<1/4. Let M_j(alpha) be the exact compact reflection-orbit
cost, including the smooth cross-pole disks, in the same upper-bound folder.
Put q=sec(pi/64), a2=2^(1+alpha/2)/(pi(alpha+2)), and

    A(alpha)=Gamma((alpha+2)/2)/(2sqrt(pi)Gamma((alpha+3)/2)),
    U_C=2^(1-alpha)a2/alpha+q max_j(M_j+E_j),
    U_D=2^(1-alpha)A/alpha+1/2+q max_j(M_j+E_j).

The previously proved transport and phase-completion theorems give
C_alpha<=U_C and D_alpha<=U_D. The exact compact costs are bounded at the
nodes by 384 by 384 interval rectangles. A certificate's interval lower
endpoint for this upper plan is never used as an operator lower bound.

## Why interpolation is valid

Every positive moment integral integral d^alpha dmu, mu>=0, is log-convex
by Holder's inequality. Sums, products and maxima preserve log-convexity.
The local term for C is 4*2^(-alpha/2)/(pi alpha(alpha+2)), with logarithmic
second derivative alpha^(-2)+(alpha+2)^(-2). The local D term is a sum of
positive moment terms; A has its positive angular integral representation.

For the compact orbit, write h,v,d for horizontal, vertical and diagonal
Euclidean distances and a,b>=0 for its two kernel masses. Since
h^alpha+v^alpha>=d^alpha, the orbit cost is

    2[(a-b)h^alpha+b d^alpha] if a>=b,
    2[(b-a)v^alpha+a d^alpha] if b>=a.

The selection depends only on the masses, not on alpha. Both expressions
are positive moment sums. The exterior plans are fixed and their angular
costs are sums of fixed positive coefficients times fixed distances to the
power alpha. The radial factors are integral u^(-alpha)du. The residual
mass bound is also fixed. For higher harmonics the code uses the Jensen
upper replacement

    a_k(alpha) <= [2k cos(pi/(2k))/(k^2-1)]^alpha/pi,

not equality with the exact angular integral. This replacement and the
explicit last-series remainder are log-convex. Consequently log U_C and
log U_D are convex within each group.

For the fixed polygonal shape, the positive layer-cake formula is

    I(alpha,a)/alpha = (1/2) integral_0^infinity (2t)^alpha J_a(t) dt/t,
    J_a(t)>0.

Thus g(alpha)=log(I(alpha,a)/alpha) is convex. The shape must remain fixed
when comparing neighboring exponents.

## Finite, outward verification

Take neighboring upper nodes a<b, and certified upper values U(a)<=A,
U(b)<=B. On [a,b], log U(t)<=E(t), where E is the affine interpolant of
log A,log B. For consecutive lower nodes x0<x1<x2<x3 in one shape group,
with [x1,x2] contained in [a,b], let l(x)<=I(x,a0)/x<=u(x). Convexity gives

    L1(t)=log l(x1)+(t-x1)[log l(x1)-log u(x0)]/(x1-x0) <= g(t), t>=x1,
    L2(t)=log l(x2)+(x2-t)[log l(x2)-log u(x3)]/(x3-x2) <= g(t), t<=x2.

For any rational c in [x1,x2], E(t)-log t-L1(t) is convex on [x1,c], and
the corresponding expression with L2 is convex on [c,x2]. Hence the four
endpoint evaluations at (x1,L1),(c,L1),(c,L2),(x2,L2) bound the logarithmic
ratio throughout [x1,x2]. This remains valid for an imperfect split point.

The independent code ../../code/check_uniform_comparison.py checks all
58 upper intervals and 232 lower intervals per operator, exact group
coverage, neighboring-node existence, common shapes, exterior reference
exponents and source hashes. It takes every maximum with outward Arb
arithmetic at 256 bits. Its improved split point is a rational approximation
of the intersection of L1 and L2. The original lead implementation normally
chose c=x2; that is also valid but gives a slightly larger enclosure.

The resulting middle-interval upper ratios are

    U_C/I <= 1.0824118312,
    U_D/I <= 1.2893632770.

A separate 90-decimal calculation from the same adverse endpoints and
recorded rational splits gives respectively 1.08241183104452... and
1.28936327680851..., below those displayed bounds. It checks every segment,
not only the segment attaining the maximum. Complete inputs are under
data/; the independent output and its hashes are in
../../data/uniform_comparison_independent.json and
../../data/uniform_comparison_mpmath.json (paths relative to this proof).
The input statements and programs are snapshotted in source/.

## Completion at both endpoints

The endpoint theorem in ../endpoints/PROOF.md proves C/ell<=1.0172482934
on (0,1/200] and C/ell<=1.0262309397 on [199/200,1). For D, use the already
proved C<=D<=C+1/2. The small-exponent ell is a product of two positive
decreasing functions, so ell(alpha)>=ell(1/200)>126.199. Therefore

    D/ell <= 1.0172482934+1/(2*126.199) < 1.0213.

At the other endpoint, delta=1-alpha<=1/200 and the endpoint proof gives

    delta ell(alpha)>=(alpha+1)(alpha+2)sqrt(3)/(8pi)>0.411775.

Thus ell>=82.355 and D/ell<1.0262309397+1/(2*82.355)<1.0324. Both endpoint
ranges are covered by the larger middle constants. Lower bounds follow
from the admissible witnesses and C<=D. Approximation transfers the result
to the initial compact smooth test class and back to the homogeneous space.

## Dependencies and reproduction

This result depends on the setup, polygonal witness, compact reflection,
exterior-circle and endpoint theorems identified above. It introduces no
new assertion about principal-value convergence or full inhomogeneous
Holder norms. The original nodal data are recomputed with the already
audited certificate programs by ../../code/reproduce_uniform_nodes.py;
its logs, outputs and comparisons are kept in verification/recomputed/.
All required JSON files are explicitly registered in the independent
output's source_hashes map. Importing those files is not itself a proof:
the preceding transport, moment, quadrature and endpoint arguments supply
the soundness justification.
