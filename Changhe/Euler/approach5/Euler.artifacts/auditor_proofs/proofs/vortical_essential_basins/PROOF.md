# Vortical SRB basins are open modulo null sets

Date: 2026-11-02T22:12:50Z. Verdict: CONFIRMED as a conditional-on-the-given-measure consequence, A223. This does not assert SRB existence.

## Exact hypotheses

Let B be a complete C2 vector field on R3 and W a C1 vector field with [B,W]=-kappa W, kappa>0. Write Psi for the flow of -B, Gamma for the locally defined W flow, and O={W!=0}. Assume all forward Psi orbits are bounded. Let nu be a compactly supported full-flow-ergodic probability with nu(O)=1, simple spectrum (positive, zero, negative), stable direction R W, and center direction R B. Assume its unstable conditional probabilities are equivalent to arclength on local unstable plaques, with strictly positive local densities.

The last hypothesis follows, in the Euler application, from A207: alpha=(B cross W) dot dy obeys the exact expanding one-form law, and the given vortical SRB measure has conditional density proportional to positive alpha-length. No 2026 generalized-measure existence theorem is used in the present implication.

Let B_nu be the continuous-time basin of nu, defined by convergence against every bounded continuous observable. Then there is a unique maximal open set D_nu contained in O for which

    B_nu subset D_nu,     Leb(D_nu minus B_nu)=0,     nu(D_nu)=1.

The set D_nu is invariant under all Psi times and locally saturated by W flow. Distinct such probabilities have disjoint sets D_nu. If additionally div B=d>0 is constant, each nonempty D_nu has infinite Lebesgue volume.

Here open modulo null sets does not mean every point of D_nu is generic. In particular carrier equilibria or other exceptional points may lie inside D_nu.

## Proof

A point of {W=0} cannot belong to B_nu. Its orbit remains in that closed set by exact transport, so the bounded continuous observable min(1,|W|) has time average zero. Its nu integral is positive. Hence B_nu is contained in O.

Take a nu-typical regular point x on a local unstable plaque gamma. Disintegration and strict positive conditional density imply that the set T of continuous-time nu-generic regular points has full arclength in a sufficiently small open subarc of gamma. At x the vectors gamma-prime, -B and W are independent. By continuity, after restricting the arc and all times, the map

    H(s,t,tau)=Gamma_tau(Psi_t gamma(s))

is a C1 diffeomorphism from a small open box to an open neighborhood V of x contained in O.

Fixed Psi-time shifts preserve all continuous-time empirical limits. Short W shifts do so as well. Indeed exact bracket transport gives

    Psi_r Gamma_tau y=Gamma_(tau exp(-kappa r)) Psi_r y.

For generic y on the plaque, its forward orbit is bounded and its limit measure is compactly supported. The global bounded-orbit hypothesis places the whole future in a compact set; local W flow is therefore uniformly available at small parameters there. The right side approaches Psi_r y as r tends to infinity. Every bounded continuous observable is uniformly continuous on the compact set containing these two futures. Thus the two time averages have the same limit.

The same conclusion holds for every finite W shift for which the initial flow segment exists: conjugating that whole segment by Psi_r proves the identity wherever needed, and the exponentially shrinking parameter eventually lies in the uniform compact neighborhood. No global completeness of W is required.

Consequently H(T times the time rectangle) is contained in B_nu. Its complement in V is null by Fubini and the C1 change-of-variables theorem. This construction works at nu-almost every regular point x.

Define D_nu to be the union of all open V contained in O with Leb(V minus B_nu)=0. Second countability supplies a countable subcover, so D_nu is open and its nonbasin part is null. The preceding construction gives nu(D_nu)=1. A smooth diffeomorphism preserves null sets. Since B_nu is invariant under every Psi_t and O is invariant, the defining property yields Psi_t D_nu=D_nu. The corresponding local W-flow invariance follows from the basin-shift identity just proved and local invertibility of Gamma_tau.

It remains to show that no basin point lies outside D_nu. Choose a nonnegative continuous compactly supported function phi inside D_nu with int phi dnu>0. Such a function exists because D_nu is open and has full nu measure. Any y in B_nu has positive limiting time average of phi, and therefore Psi_t y belongs to D_nu for some t. Invariance gives y in D_nu. This proves B_nu subset D_nu and hence the asserted equality modulo null sets. Maximality and uniqueness follow from its definition.

Basins of distinct probabilities are disjoint. If their two open sets overlapped, the overlap would be a nonempty open set of positive volume, while each basin would have full volume there. This is impossible. Finally, if div B=d>0, invariance under the forward B flow Phi gives Leb(D_nu)=exp(dt)Leb(D_nu). Since D_nu is nonempty and open, its volume is positive; that identity excludes finite volume.

## Euler consequence and limits

For a C2 uniformly sublinear Euler profile, every forward Psi orbit is bounded, kappa=1+c, and the exact expanding one-form has rate 1-2c>0 when 0<c<1/2. Therefore every GIVEN vortical SRB probability has such an invariant open basin domain, for every finite omega. The result permits the support of nu to meet either degeneracy set; it uses independence only at its typical points.

If the separately proposed conditional almost-everywhere vortical basin-coverage theorem is established, the union of these pairwise disjoint open domains has full volume in O. The remaining relative closed set may still be nonempty and may separate different domains. No uniform hyperbolicity, finiteness, uniqueness, topological attraction or nonexistence follows.

## Verification evidence

Checked the disintegration-to-full-arclength step against A207's positive density statement, the inverse-function step against the three independent directions, and the passage from a local full basin to every basin point using a compact continuous observable. Null sets are handled by a countable subcover. This proof avoids a generic Pesin stable-holonomy claim; the stable motion is the explicit C1 W flow.
