# Fixed-map gun support and a sufficient homogeneous package

## Exact statement and notation

Use the unchanged bundled balanced engine: a 12 by 12 map, T=250 ticks,
unit movement, nonnegative catalog damage, unlimited splash application to
each adjacent copy, and at most one selected target per gun per tick. Fix
a legal defender map after all construction. Let P=(p_0,...,p_L) be its
selected route. Buildings and route remain fixed during this combat.

Append N entries of a single type with HP H and base damage b to an
attacker roster with exactly e active entries before the append. Earlier
entries can have arbitrary types. Appended entry j, indexed from zero, is
eligible when s_j=(e+j) mod T satisfies s_j+L<T. Let E be the eligible
indices and n=|E|. Put S equal to the sum of splash damage along
p_0,...,p_(L-1). Suppose H>S, and write a=H-S.

For each gun g with catalog damage d_g, let

    I_g = {i in {0,...,L-1}: p_i lies in the gun's range},
    U_g = union over j in E of {s_j+i: i in I_g},
    C(N) = sum_g d_g |U_g|.

Then at least max(0,n-floor(C(N)/a)) appended copies arrive, and their
base damage is at least b times that integer. This bound ignores damage
from the e earlier entries and from ineligible appended entries.

If every cell outside P is occupied, the bound also holds against every
legal simultaneous submission of the defender, regardless of its gold.
No such submission can change the map. Otherwise this is a certificate
for the fixed map only and must not be called response-robust.

## Proof

An eligible copy starts at p_0 on tick s_j and, if alive, is at p_i on
tick s_j+i. A gun can assign damage to that copy only at a tick belonging
to s_j+I_g. Therefore, even if other entries are present, all damage this
gun assigns to eligible appended copies is at most d_g |U_g|. The bound
allows every such possible shot to occur and ignores overkill, earlier
deaths and competition with other entries. These omissions can only
increase the upper bound. Summing over guns gives C(N).

Every eligible copy killed before arrival received at most S splash
damage and therefore at least H-S=a gun damage. Death requires HP to be
nonpositive after simultaneous damage is applied. Consequently there are
at most floor(C(N)/a) such deaths. Every surviving eligible copy arrives
at tick s_j+L<T; there are no collisions or movement delays. Subtraction
proves the arrival and damage lower bounds.

If all cells outside P are occupied, the graph induced by the remaining
cells is exactly P: a nonconsecutive edge would contradict that P is a
shortest path. Building on an internal path cell disconnects spawn and
base, building at either endpoint is forbidden, and every other cell is
occupied. The action interface has no removal or upgrade. Thus every
legal defender action preserves the map, proving the response-robust
extension.

## Finding the smallest sufficient N

This section finds the smallest N that satisfies this bound, not the
smallest actual damaging attack. Suppose the requested damage is D>0
and let h=ceil(D/b). Let A=T-L, the number of eligible birth residues.
A is positive on this grid. For each 0<=r<T let n_r count eligible
residues among e,e+1,...,e+r-1 modulo T.

For N<T, explicitly evaluate the bound. For N=qT+r with q>=1 and
0<=r<T, all eligible birth residues occur, so every U_g is already its
full-cycle union and C(N)=C_* is independent of q and r. Also
n=qA+n_r. Hence the least sufficient q at this remainder is

    q_r = max(1, ceil((h+floor(C_*/a)-n_r)/A)).

Compare q_r T+r for all remainders with the sufficient values N<T.
The least candidate is the smallest N certified by the bound. This
requires at most two passes over T phases. A bit at position t represents
possible gun damage on tick t; OR of shifted coverage bitsets implements
the unions exactly. No floating point arithmetic is required.

In particular, binary search on the bound for N<T is not justified:
adding a new birth residue increases both n and the possible gun damage
C(N), so the lower bound can decrease. Enumeration avoids assuming that
monotonicity. The formula after a full cycle follows from the proved
constant support, rather than from an empirical monotonicity claim.

## Dependencies, implementation and limits

This argument refines analysis/full_map_capacity/PROOF.md by replacing
250 times total gun damage with the exact union of eligible copy firing
opportunities. It uses td_game/combat.py for ordering, dense indexing,
targeting and damage, td_game/actions.py for available actions, and
pathfinding.py for the selected route. All constants and catalog values
are loaded from the supplied configuration by the implementation.

Earlier roster entries must be counted after active filtering. The
package's order relative to those entries affects the residue offset e.
The result says nothing about affordability, attacker survival, future
rounds on a changing map, or global strategic strength. H<=S makes this
particular bound inapplicable. This is an informal proof; no proof
assistant or modified engine is used. The proof was written before its
component checks were run.
