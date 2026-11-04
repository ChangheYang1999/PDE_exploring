# Whole-plane union of the Source013 background estimates

## Exact statement and hypotheses

Fix c = 4076476460239181/2251799813685248, Candidate 007 with SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21, and Source013 correction with SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a. The complete field archive has SHA256 3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb. Write psi = partial_y chi_007 + phi_013, rho = -Delta psi, h = -Delta phi_013, u = (-psi_xy,psi_xx), V = cX+u, and

    M = (c+1+V.X/(1/4+|X|^2))I - (21/10) Sym DV
        + [[rho_y,-rho_x/2],[-rho_x/2,0]].

All fields, their smoothness, symmetry, exact source identities and the containing-arithmetic premises are imported from the stated source and regional proofs. Assume the following three complete, independently reviewed regional results for these same fields.

1. On 0 <= |X|^2 <= 61/67, M >= beta_in I, where beta_in = 704955805507/10^12. On |X|^2 >= 49/15, M >= beta_out I, where beta_out = 761272835221/10^12. On the union of these regions, |grad h| <= 1/4 and ||Sym Du||_op <= 137/125.
2. The complete ordinary-host reconstruction, exact recount and their independent actual review provide all 42 closed slabs j = 97,96,...,56, with |X|^2 in [j/(128-j),(j+1)/(127-j)]. On each slab the passing small_strain conjunction gives M >= (3/5)I, |grad h| <= 1/4 and ||Sym Du||_op <= 137/125.
3. The matrix adapter and its distinct independent actual review give M >= beta_j I on every host slab, where beta_j is its exact downward-rounded rational lower. Every beta_j is at least 3/5. All host records have successful complete execution receipts, not stopped or partial records.

Then, with beta = min(beta_in,beta_out,beta_56,...,beta_97), the whole plane satisfies

    M >= beta I,  |grad h| <= 1/4,  ||Sym Du||_op <= 137/125.

In particular beta >= 3/5. If every beta_j >= beta_in, then beta = beta_in. This last numerical condition is not assumed verified before the actual host and matrix records exist.

For the stronger gradient target 71/500, include only slabs whose independently reviewed both_small conjunction is true, together with the previously admitted strong-region indices. That selected mask alone determines the stronger domain. No whole-plane bound at 71/500 is implied by the weaker conclusion.

## Complete argument

Let t = |X|^2/(1+|X|^2). This maps every finite nonnegative squared radius monotonically to [0,1), with inverse |X|^2 = t/(1-t). The inner region is [0,61/128] in t. The outer region is [98/128,1). The 42 host slabs are exactly [j/128,(j+1)/128], j = 56,...,97, and their union is [56/128,98/128]. Consecutive slabs include their shared endpoints. The host overlaps the inner region on [56/128,61/128] and meets the outer region at 98/128. Therefore these three regions cover [0,1), including the origin and every finite exterior point.

At each point choose one regional theorem whose domain contains it. That theorem gives the two scalar bounds in the conclusion. It also gives M >= beta_region I, with beta_region >= beta by definition of the minimum. For each vector z in R^2,

    z.Mz >= beta_region |z|^2 >= beta |z|^2.

This proves the matrix inequality. Overlaps require no addition or averaging and do not change any constant. The numerical comparisons beta_in >= 3/5 and beta_out >= beta_in, together with the stated host comparisons, prove the final claims about beta.

For the stronger gradient statement, each selected root represents a closed interval with the original exact endpoints. Merge consecutive selected indices into maximal runs. Each run covers exactly the interval from its first left endpoint to its last right endpoint; distinct runs leave a strict open gap. At endpoints and elementary interval midpoints, membership in the unmerged and merged sets is equivalent. Membership is constant inside each elementary interval, so this finite check verifies the full reported domain. The formal terminal value t=1 records an unbounded exterior; it is not an additional point of the plane.

## Evidence interface and dependencies

The consumer must authenticate the completed m=60 union, the independently adopted inner and outer matrix recounts, the complete host recount and its actual adoption, and the stronger matrix recount and its actual adoption. An adoption must bind the exact result and successful execution receipt. All claimed domains, source identities, flags and exact constants must agree with those records. All dependencies are rehashed at completion. No new field calculation is performed by this union.

Dependencies are ../background_progressive_union/PROOF.md and its completed m=60 result; ../background_matrix_margin_recount/PROOF_v02.md and its ordinary, balanced and rectangular actual adoptions; ../ordinary_slabs_host_method/PROOF.md for the complete source reconstruction; and ../ordinary_host_matrix_margin/PROOF.md for the exact eigenvalue adapter.

## Status and scope

This proof is a conditional assembly theorem written before the host finishes and before the union consumer is implemented. Its premises must be discharged by the actual reviewed records. The result concerns only the displayed background inequalities. It does not estimate fourth through sixth derivatives of the near coefficient, bound H4 remainder terms, construct a uniform small-parameter inverse, close an invariant ball or prove stationary IPM existence. The established analytical theorems may be applied only with all their additional hypotheses.
