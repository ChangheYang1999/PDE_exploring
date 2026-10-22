# A scaling vector alone does not rule out a finite inverse constant

Written 2026-10-22T11:58Z, before any separate review of this issue.

## Statement and hypotheses

Let X be a real normed vector space, D a real linear subspace, and L:D->X linear. Suppose K is in D with K nonzero and LK nonzero. Then on the linear subspace E=span{K}, the best constant in

    ||h||_X <= C ||Lh||_X for all h in E

is the finite positive number C_K=||K||_X/||LK||_X. In particular, containing K alone cannot imply failure of every finite constant. The inverse of L:E->L(E) exists and is bounded in these inherited norms. No inverse onto all of X is asserted.

## Proof

Each h in E is tK for a real scalar t. By linearity and absolute homogeneity of the norm,

    ||h||_X=|t| ||K||_X,
    ||Lh||_X=|t| ||LK||_X.

The denominator ||LK||_X is positive by hypothesis. Thus the displayed estimate holds with equality for C=C_K and all t. Any admissible C is at least C_K by setting t=1. The map tLK -> tK is well-defined since LK is nonzero, is linear, and has norm C_K. This proves all assertions.

## Application and limits

For the exactly normalized canonical modal trial, the accepted modal_graph_scaling proof and NONZERO_IMAGE.md establish K in X, LK in X and LK nonzero. The selected-annulus certificate independently gives K nonzero. Thus the theorem applies to that K and its actual linearized L.

The centre-quasimode theorem rules out a finite same-X constant only on domains containing the quasimode sequence. It applies to the specified broad graph domain D and its normalized zero-strain core under the established containment, but not to every subspace merely because it contains K. K has J=-2, so E need not satisfy the normalized J=0 condition; no normalized-domain counterexample is claimed here.

In the saved lead report post1138_1157/report.md, timeline11:47 first treats every domain containing K, then says 'by5(p) no finite C exists on these domains'. Read as including every domain containing K, this is false. The precise repair is to restrict that final nonexistence statement to D and its stated normalized core, or to domains containing the quasimodes. The lower quotient C>0.069361443018 for a domain containing K remains valid. This correction changes no numerical bound and proves no PDE existence or exclusion.

Dependencies: elementary norm and linearity axioms; modal_graph_scaling/PROOF.md, ADDENDUM.md, NONZERO_IMAGE.md and FINAL_ADJUDICATION.md; scaling_selected_application/PROOF.md, mandatory coefficient correction and evidence/verdict.json; center_weighted_quasimodes/PROOF.md and its domain hypotheses.
