# The complement of all regular attractor basins

Written: 2026-11-02T21:51:53Z. Audit A206: CONFIRMED, checking Theory Agent C C21.

## Statement and hypotheses

Assume a C2 Euler profile with uniformly sublinear velocity, 0<c<1/2 and arbitrary real omega. Let calA be the nonempty family of ALL regular basic hyperbolic backward attractors in the exact class of A115/CO9. For each A, let W(A) denote its backward-flow basin. Set

    K=R3 minus union_(A in calA) W(A).

Then K is closed and invariant for the complete carrier flow, contains every boundary of W(A), and meets every sphere of sufficiently large radius. For every z in K its backward limit alpha(z) is nonempty, compact, invariant, contained in K and disjoint from every A in calA. For almost every vortical z in K, alpha(z) meets the carrier-zero set or the vorticity-zero set. Thus either such exceptional cases have positive volume, or K intersect {Omega!=0} is null.

## Proof

Each basin is open and invariant in both time directions. Their union is open and invariant, proving the first assertion about K. Distinct basins are disjoint by A115. If a boundary point of one basin belonged to a different basin, the latter's openness would give a neighbourhood disjoint from the former, contradicting the boundary property. A basin does not contain its own boundary. Thus every basin boundary lies in K.

Fix one A0. Its connected trapping region has one torus boundary by A087. The basin-boundary theorem A189 applies and makes its boundary meet every sphere beyond a fixed radius. Hence K also meets every such sphere.

Backward carrier trajectories are precompact by uniform sublinearity and radial inward trapping. Their limits are therefore nonempty compact invariant sets. Closedness and invariance of K give alpha(z) subset K whenever z is in K. Every A belongs to its own basin, so no such limit meets any A.

A115 says that, outside a null set of vortical points, a backward limit wholly contained in the regular set belongs to one of these regular basins. Such membership is excluded on K. The remaining cases are precisely the carrier-zero or vorticity-zero cases in CO9. If the vortical part of K has positive volume, removing the null exceptional set leaves positive volume in those cases; otherwise its vortical part is null.

## Dependencies and scope

The only inputs are the exact classifications A115, the trapping-boundary topology A087 and the basin-boundary result A189. No new PDE estimate is used. Nonemptiness and unboundedness of K do not imply positive volume or even the presence of vortical points. A null invariant curve is topologically compatible. The conditional regular completion A181 is not an actual constructed example and does not remove that qualification.

Precision update 2026-11-03T21:40:29.641112+00:00: ALL makes the original exhaustive-family meaning explicit. An arbitrary subfamily does not suffice for the almost-everywhere classification step. The original is preserved in the team records.
