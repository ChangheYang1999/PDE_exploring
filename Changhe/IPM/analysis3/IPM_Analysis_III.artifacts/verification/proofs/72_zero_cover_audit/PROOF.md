# Acceptance of a refined zero-set cover

## Setting and exact claim

The vector field is the canonical V of the normalized exact-join modal
background of proof 04. In the closed first quadrant, proof 66 proves
that the source rectangle

 Q=[4559930541822721/562949953421312,
    5122880495244367/562949953421312] times[-1/2,1/2]

contains exactly one zero P. At the origin V(0)=0. A global certificate
of hypothesis(Z) must show that all remaining points in the closed
quadrant have nonzero V. Reflections then give the full-plane result.
This note states acceptance conditions, not an accepted numerical result.

## Exact polar boxes and interval lower bounds

A finite box is specified by exact rational endpoints t0<=t1 and
rational angle coefficients a0<=a1 in [0,1/2], with

 B={exp(t)(cos(theta),sin(theta)):t0<=t<=t1,
                                      pi*a0<=theta<=pi*a1}.

For q=V_r/r and v=V_theta/r, interval bounds q in Iq and v in Iv imply

 |V|/r>=sqrt(dist(0,Iq)^2+dist(0,Iv)^2).

The right side must be rounded downward. A zero lower bound means
unresolved, not a zero of V. B is contained in Q if the following three
outward interval tests succeed:

 exp(t0)cos(pi*a1)>=Q_x_lower,
 exp(t1)cos(pi*a0)<=Q_x_upper,
 exp(t1)sin(pi*a1)<=1/2.

Monotonicity on the closed quadrant proves these tests. No approximate
source center, unchecked floating trigonometry or empirical tolerance
is needed. The tests remain valid for boxes meeting either axis.

## Finite refinement and accounting

Bisection replaces a box by its two closed children, splitting either
one exact t interval or one exact angle-coefficient interval. The union
of the children equals the parent. The recursion must terminate after
a finite specified depth. Every terminal child must either be inside Q
or have a strictly positive finite lower bound. A nonterminal node is
not a leaf and must not be included in leaf counts.

A replayable certificate stores every terminal child with its parent
index, exact endpoints, verdict, q/v intervals and lower bound when
applicable. An independent verifier reconstructs the initial exact
radial/angle cover from the original knot vector, checks that the
unrefined boxes have positive bounds, and checks the refinement tree
with no gaps or duplicate ownership. The number of leaves alone does
not establish coverage. Given these conditions, any nonzero point
outside Q belongs to a positive box, proving(Z).

## Scope of an archived summary

A summary containing only the minimum positive bound and the list of
excluded boxes cannot by itself prove every positive leaf or exact tree
coverage. Correct source code plus a independently checked rerun can
supply the missing evidence. If the archived run used an approximate
rectangle, each excluded box can instead be independently checked
against the exact Q; this repair can accept the actual boxes even when
the implementation's generic approximate-rectangle rule is not proved.

## Specific source-code findings before replay

In the archived zrefine.py, the counter named leaves is incremented at
every visited node before a possible split. For T roots and N total
nodes in a binary refinement forest, the terminal count is (N+T)/2,
since the number of edges is N-T and also twice the internal-node
count. Thus N=463 and T=255 give359 terminal leaves, not463. If34
terminal leaves are excluded and none unresolved,325 leaves are
positive, not429. This bookkeeping error does not by itself disprove
the geometric cover, but the reported counts must be corrected.

The code uses the approximate source center8.600064 and floating
geometry. Shrinking its half-width by a factor1-10^-9 does not prove
containment in the exact Q, since the source-center discrepancy is
larger than that shrinkage. The actual excluded boxes can nonetheless
pass an independent exact-geometry check. The audit reconstructs their
exact dyadic child endpoints from the original source knots and the
rational angle grid, then uses512-bit outward interval geometry.
