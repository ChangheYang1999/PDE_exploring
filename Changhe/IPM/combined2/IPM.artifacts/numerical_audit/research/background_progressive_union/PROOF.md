# Extending the audited background cover through ordinary roots

This argument precedes its consumer. It states a conditional assembly theorem, not a claim that any pending ordinary root has been computed.

## Exact statement

Fix c = 4076476460239181/2251799813685248, Candidate 007 with SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21, and correction C2-N1-013 with raw SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a. Let psi = partial_y chi_007 + phi_013, rho = -Delta psi, h = -Delta phi_013, u = (-psi_xy,psi_xx), V = cX+u, and

    M = (c+1+V.X/(1/4+|X|^2))I - (21/10) Sym DV
        + [[rho_y,-rho_x/2],[-rho_x/2,0]].

The fields and their regularity are the same imported fields as in ../background_slabs_union/PROOF.md. No new regularity theorem is asserted here. Put t = |X|^2/(1+|X|^2), and I_j = [j/128,(j+1)/128] for finite roots j < 127. The last region is [127/128,1), corresponding to all finite points with |X|^2 >= 127.

Assume the complete 86-index cover of ../background_slabs_union/PROOF.md has been computed and independently audited. Its ordinary and balanced roots, independently reconstructed capped slabs, and complete exterior must all have the same fixed source. In particular its weaker conjunction holds for j in {0,...,55} union {98,...,127}; its stronger conjunction holds for j in {0,...,55} union {99,101,103} union {105,...,127}.

Let m be an integer with 55 <= m <= 97. For every integer 56 <= j <= m, assume an actual ordinary-root publication and its adopted independent review establish the displayed passing joint flags on all of I_j and all angles. Every such publication must have a complete successful execution receipt, the exact same source and parameter, its full angular cover, its original exact j/128 endpoints, and authenticated immutable dependencies. A saved producer flag alone is insufficient. Assume its weaker conjunction passes; use its stronger conjunction only if that independently reviewed flag also passes.

The weaker conjunction is

    M >= (3/5)I, |grad h| <= 1/4, ||Sym Du||_op <= 137/125.

It then holds on

    0 <= |X|^2 <= (m+1)/(127-m), or |X|^2 >= 49/15.

For m < 97 the sole open gap in this selected evidence is

    (m+1)/(127-m) < |X|^2 < 49/15.

For m = 97 the gap is empty and the weaker conjunction holds on the entire plane. It has exactly 128 distinct original indices. The stronger conjunction replaces 1/4 by 71/500. Its domain is exactly the union of the independently passing stronger flags, and must be reported separately. If all added ordinary stronger flags pass, at m = 97 its only gaps are the four roots 98,100,102,104. Thus even a complete weaker cover does not assert the stronger global bound.

## Proof

The previously audited weaker inventory contains all roots from 0 through 55 and from 98 through 127. Adjoining roots 56 through m gives precisely {0,...,m} union {98,...,127}; these sets are disjoint. There are m+1+30 = m+31 indices. The first consecutive block has union [0,(m+1)/128], including its endpoints. The second block and the exterior have union [98/128,1). For m < 97, (m+1)/128 < 98/128, so the only missing transformed interval is the open interval between these endpoints. For m = 97 the endpoints coincide and are included, hence the union is [0,1).

The increasing inverse transformation is |X|^2 = t/(1-t). It sends (m+1)/128 to (m+1)/(127-m), and 98/128 to 49/15. It maps [0,1) onto all nonnegative finite squared radii. This proves the stated weaker domains and, at m = 97, covers every finite X in the plane. Infinity is not an additional point to be checked.

At any covered X, at least one selected local theorem gives all three inequalities for the same fields. Taking their union preserves that conjunction. A failed or missing stronger flag contributes no region to the stronger cover. For the stronger domain, form the Boolean mask of precisely the selected indices with passing stronger flags. Each maximal consecutive run gives one interval whose endpoints are the first index divided by 128 and one plus the last index divided by 128. Distinct runs have strictly positive gaps. This proves the exact stronger domain without assuming any additional numerical bound.

For a separate finite verification of the union operation, compare membership in the original interval list and the merged list at every rational endpoint j/128 below 1 and at each midpoint (2j+1)/256. Membership is constant on each elementary open interval, so these comparisons prove equality everywhere in [0,1). The same method applies separately to both conjunctions.

## Dependencies, execution and scope

The consumer imports the completed base union and its independent audit and checks their matching source identities and coverage. It imports each newly added ordinary-root theorem through its result, successful receipt, adopted actual review and standalone publication. Exact hashes must be checked at input and again at completion. The consumer records its real dates and duration and never launches a field computation or a remote job. A missing, failed, changed or unfinished input aborts the assembly rather than becoming a conditional numerical result.

The underlying interval conclusions retain the imported Arb containing-arithmetic hypotheses. Hash verification authenticates those completed proofs; it is not itself a proof that a field lies in an interval. No Lean or Lake build is claimed. An empty weaker complement proves only the three displayed global background bounds. Any near estimate, inverse bound, invariant-ball theorem and stationary IPM existence conclusion requires its own remaining hypotheses and proof. In particular O3 is not closed by this assembly.
