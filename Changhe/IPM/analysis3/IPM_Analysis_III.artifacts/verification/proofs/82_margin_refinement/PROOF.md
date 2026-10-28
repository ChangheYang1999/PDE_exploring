# Targeted refinement of the two global energy margins

## Exact assertion to be checked

Use the normalized modal background, weights and definitions of proof 76.
The proposed strengthening is

 kappa_a-bplus >= 5/2,       kappa_R-bplus >= 5/2

almost everywhere on the full plane. This statement is conditional until
all acceptance checks described below pass. The original constants of
proof 68 remain valid independently of this refinement. In particular a
failed target does not refute positive Fredholm margins.

## Dependencies and domain

The density is the exactly joined and normalized construction from the
original trial_v2_h0.008.npz, SHA-256
a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874.
The canonical Green boundary cache and its independently audited error
bounds are those of proof 68. Reflection symmetry reduces the verification
to 0<=theta<=pi/2. Weight derivatives are interpreted almost everywhere
at their finite radial breakpoints; both adjacent values are included in
any box crossing a breakpoint.

The proof 68 full cover has3276 radial intervals and128 angular intervals
on each. On radial cells where both recorded minima already exceed5/2,
the old certificate suffices. Every remaining radial cell is recomputed
from the original density coefficients and canonical Green boundary
intervals. The infinite ends retain the proof 68 bounds, both above5/2.

## Enclosures and the exact angular identity

On each finite radial interval, use the same rigorously bounded radial
Taylor or exponential-polynomial representation as proof 68. Let P_n,Q_n
be interval enclosures of the polar velocity coefficients, and G_j,H_j
those of the radial and angular density-gradient coefficients. Then

 q=ell-sum_(n>=1) P_n cos(2n theta),
 v=sum_(n>=1) Q_n sin(2n theta),
 g_r=sum_(j>=0) G_j sin((2j+1)theta),
 g_theta=sum_(j>=0) H_j cos((2j+1)theta).

Every sum here is finite, through the exact modal bandwidth. To enclose
tan(theta)v at the vertical axis, define

 T_0=0, T_n=-T_(n-1)+2 sin(theta) sin((2n-1)theta).

The addition identity sin(2n theta)+sin((2n-2)theta)
=2 sin((2n-1)theta) cos(theta) proves
T_n=tan(theta)sin(2n theta), with the continuous endpoint value included.
Interval evaluation of the recurrence for every n therefore avoids
introducing a singular quotient. Its interval overestimation is harmless.

The Cartesian gradient is

 g_1=g_r cos(theta)-g_theta sin(theta),
 g_2=g_r sin(theta)+g_theta cos(theta).

The direct bound bplus <= (sqrt(sup|g_r|^2+sup|g_theta|^2)-inf g_2)/2
is valid since rotations preserve length. When inf g_2>0, the exact
identity

 bplus=g_1^2/[2(sqrt(g_1^2+g_2^2)+g_2)]

gives a second valid upper bound using interval lower denominators.
The smaller of these two upper bounds remains valid. The second bound
is optional and is never used when its denominator is nonpositive.

Substitute these enclosures into

 kappa_a=1+ell+mu_a' q/2+(17/4)sum_n Q_n T_n,
 kappa_R=1+ell+mu_R' q/2.

All operations use outward Arb balls. A leaf is accepted only if both
lower endpoints are finite and at least5/2.

## Subdivision and acceptance

Begin with each remaining radial cell and its128 original angular boxes.
An accepted box is retained. A failed box is bisected exactly in either
t=log r or theta/pi; the choice affects efficiency only. Its two children
have disjoint interiors and cover their parent. All endpoints are exact
rationals, and all positive terminal boxes are exported. A maximal-depth
failure is exported as unresolved and prevents acceptance of the target.

The separate audit must check hashes, exact coverage, the choice of
unchanged radial cells, all root labels, exact parent partitions and
finite lower endpoints. Representative terminal boxes are independently
recomputed at higher precision to check the arithmetic path. The proof
of every leaf is its interval computation, not this representative check.
If every root is covered by accepted leaves and both infinite-end
inequalities hold, union of the boxes and reflection prove the assertion.
Neither this bound nor a larger transport margin supplies injectivity or
an infinite-dimensional complement inverse.
