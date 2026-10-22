# Agreement of two runtime orders does not certify their full-plane accuracy

Status: complete elementary proof before artifact controls. All numerical uses below are conditional on reported runtime values, common coefficients and sample sets. They are not interval enclosures or independently reproduced component arrays.

## Statement

Fix one radius. Let S be a common finite set of Cartesian component indices at points on that circle. All applications below are made separately at each radius; maxima are never pooled across radii. For vectors of sampled component values V_12,V_24,V_48,V_ref indexed by S, write

    ||V||_S=max_{i in S}|V_i|,
    M_j=||V_j||_S, M_ref=||V_ref||_S,
    D_jk=||V_j-V_k||_S, e_j=||V_j-V_ref||_S.

Then

    e_j >= |M_j-M_ref|,
    |M_48-M_24| <= D_24,48,
    |D_12,48-D_12,24| <= D_24,48,
    e_24 >= max(0, |M_48-M_ref|-D_24,48).           (1)

No upper bound on e_24 or e_48 follows from a small D_24,48. The inequalities require exactly the same component norm and index set. Distinct lower bounds may be attained at different indices. If V_ref is only a numerical approximation, these become conditional comparisons to that approximation, not certified lower bounds on true full-plane error.

## Proof

For any component vectors A,B, |A_i|<=|B_i|+|A_i-B_i| at each i. Taking maxima gives ||A||_S<=||B||_S+||A-B||_S. Exchanging A and B yields the reverse triangle inequality. Apply it to (V_j,V_ref), (V_48,V_24), and (V_48-V_12,V_24-V_12) to obtain the first three statements. Also e_48<=e_24+D_24,48, so e_24>=e_48-D_24,48>=|M_48-M_ref|-D_24,48; nonnegativity gives the last formula. For the absence of an upper bound, take V_24=V_48=V_ref+H for an arbitrary constant component vector H. Their difference is zero while either error can be arbitrarily large. Also |M_48-M_ref|<=|M_48-M_24|+|M_24-M_ref|<=D_24,48+|M_24-M_ref|. Thus the direct lower bound |M_24-M_ref| always dominates the transferred lower bound in (1).

## Intended artifact application

The two new NUM JSON files label the K48,beta3.092 stored state and the quadrature pairs12/24 and24/48. The JSON key named max_U48 is generic in the current exporter: for the12/24 file it represents M_24, and for24/48 it represents M_48. It must not be read as48point data in both files. The reports describe181angles phi=j*pi/182,j=1,...,181, both Cartesian components, and eight radii10^2,...,10^9. The source code is inspected read-only to check consistency of that interpretation; it is not executed or reused.

P291 independently computed M_ref at precisely those angles by physical-radius full-plane quadrature, with separately checked endpoint moments and partition changes. Its finite numerical accuracy tests are not rigorous enclosures. This packet only recomputes reported scalar arithmetic and joins the new metadata and M_48 values to that existing independent evidence. The new JSON files omit component arrays, source hashes and an explicit sample-angle list. Consequently the runtime values and provenance are attributed claims, not authenticated reconstructions of every run.

In particular, a small24/48increment accompanied by a large difference of either reported norm from M_ref is evidence of a common runtime discrepancy, conditional on these premises. It does not determine whether interpolation, implementation, input provenance or another source causes it, and does not certify quadrature convergence. Any reported48/96NaNs are excluded from a finite numerical comparison; this packet neither diagnoses their cause nor infers divergence from them. Literal-profile exclusions and the general B2 question are separate: no new existence or nonexistence result follows from (1).

## Dependencies and scope

Only the elementary finite-dimensional norm inequalities above are proved here. P291 supplies the independently computed reference data with its original stated limitations. Frozen JSON inputs, source excerpts, metadata and independent arithmetic checks are in verification/. No runtime component arrays or whole-plane error enclosures are produced, no numerical-lane code is executed, and no finite-box boundary is introduced. General B2 remains OPEN.
