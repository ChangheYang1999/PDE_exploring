# Radial couplings with two global identity atoms

## Statement

Fix 0<a<1 and 0<delta<1/2. Use the real homogeneous Holder seminorm,
circular principal values, kernels and quotient extension in
../../../01_setup/PROOF.md. Let x=(1/2,0), y=-x and

    w(r,theta) = [cos(2 theta-phi)
       - r^2 Re(exp(i phi)/(1+r exp(i theta))^2)]/(2 pi).

The right local annulus carries w dtheta dr/r. The left annulus carries
its negative under z -> -z. Include the atoms -delta_x/2+delta_y/2.

Partition [delta,1/2] into radial intervals [a_k,b_k] and the circle into
angular arcs I_j. For each k,j assume a fixed sign eps_kj in {-1,1} and
numbers l_kj>=0, v_kj>=0 such that, for every r in [a_k,b_k],

    eps_kj w(r,theta)>=0 for theta in I_j,
    l_kj <= integral_(I_j) |w(r,theta)| dtheta <= v_kj.

For undecided signs set l_kj=0 and retain any valid variation bound.
Choose masses 0<=m_kj<=l_kj log(b_k/a_k). The reflected left cell has
the opposite mass. The two atoms have masses -1/2,+1/2. Consider any
finite nonnegative transport plan with these exact signed marginals.
An edge is called radial if its two non-atomic ends lie in the same
radial interval. Edges with an atom as one or both ends are also allowed.

For a radial edge between angular cells on the same pole, use the cost

    c = d_arc^a J_k,
    J_k = (b_k^a-a_k^a)/(a log(b_k/a_k)),
    d_arc = sup_(theta in I_i,eta in I_j) |exp(i theta)-exp(i eta)|.

For an edge from a cell to its own pole use c=J_k. For an edge connecting
the two poles use c=1. For other radial edges and edges to the other pole
one may use any upper bound for the distance power over their supports.
For edges between distinct radial intervals use the full support
supremum, in particular the universal value 2^a.

Then the local functional has norm at most

    sum_edges flow(edge) c(edge)
       + sum_k [sum_j v_kj log(b_k/a_k)-sum_j m_kj] (1+2b_k)^a.       (1)

Every term in square brackets is nonnegative. The plan need not be
optimal. A global atom may receive flow from, or send flow to, any
number of radial intervals. Its total signed marginal must still be
exactly 1/2.

## Proof

For each radius r and each signed cell with m_kj>0, extract from its
angular variation measure the proportion

    m_kj / [log(b_k/a_k) integral_(I_j)|w(r,theta)| dtheta].

This lies in [0,1] by the lower-mass hypothesis. Thus the extracted
measure has the same angular mass density m_kj/log(b_k/a_k) at every
radius, relative to dr/r. A cell with zero extracted mass needs no
normalization. Reflect the extraction to the left annulus.

Split each extracted cell measure among its incident edges in the
proportions flow(edge)/m_kj. For a radial edge between two non-atomic
cells, the two pieces have exactly the same radial marginal
flow(edge) dr/[r log(b_k/a_k)]. Couple them at the same radius and use
the product of their normalized angular measures. The same-pole
pointwise distance is at most r d_arc. Integration over r gives the
cost flow(edge) d_arc^a J_k. An own-pole atom edge has distance exactly r,
and therefore the cost flow(edge) J_k. Atom pieces from different
radial intervals can be added because the plan enforces their total
marginals. They do not require a shared radial parameter.

All remaining edges can be lifted by product measures, whose costs
are at most their support suprema times the edge masses. All points
in the two closed radius1/2 disks have modulus at most1, so 2^a is a
valid universal distance-power bound. The two centers are distance1
apart.

After extraction, the right residual in radial interval k has total
variation at most sum_j v_kj log(b_k/a_k)-sum_j m_kj. Its left partner
is its negative central reflection. Pair each residual point with its
negative. Since |z-(-z)|<=1+2b_k, the resulting cost is the second term
in (1). Apply |f(z)-f(z')|<=[f]_a |z-z'|^a to each lifted coupling and
add the bounds. This proves (1).

## Completion and exact computation

The small-disk, middle-region, exterior-region and phase-interpolation
arguments of ../PROOF.md apply unchanged. In particular the full
identity atoms have been included here, so no separate half-unit
triangle inequality is added. For m phase half-intervals, q=sec(pi/(4m))
and nodes phi_j=j pi/(2m), j=0,...,2m, the full bound is

    D_a <= S_a(delta)+q max_j(L_j+M_j+E_j)+(q-1)/2,
    S_a(delta)=2 a2(a)delta^a/a
       +(1+2delta)^a delta^2/[2(1-delta)^2],
    a2(a)=2^(1+a/2)/[pi(a+2)].

An implementation may choose rational cell masses by rounding down,
solve a floating linear program only to select flows, round every
proposed flow down, and transport every remaining integer unit
explicitly. The final plan must be checked against every integer
marginal. Support bounds and J_k are evaluated with outward interval
arithmetic. A floating optimal value, or a tolerance-based marginal
check alone, does not prove (1).

No improved numerical operator constant has yet been certified with
this construction. It extends the previously checked local-circle
method by allowing the identity mass allocation to be chosen globally
while retaining exact radial integration on same-circle edges.
