# Finite modifications cannot repair a non-Fredholm operator

Date: 2026-10-20. Status: CONFIRMED after actual Claude Opus5.5 review and follow-up, with the conditional application limits below. This is a conditional functional-analytic statement, not a claim that the full IPM operator satisfies its premises.

## Statement and notation

Work over one fixed scalar field, real or complex, with every dimension taken over that field. Let D and Y be Banach spaces, and let A:D -> Y be bounded. Let E be a closed subspace of D with finite codimension d. Let F and G be finite-dimensional Banach spaces. Let K:E -> Y be bounded and have finite rank, and let B:F -> Y, C:E -> G and H:F -> G be bounded. Define

T:E direct-sum F -> Y direct-sum G,
T(e,f)=(Ae+Ke+Bf, Ce+Hf).

Here direct sums have any product Banach norm. A bounded map is Fredholm when its kernel and cokernel have finite dimensions and its range is closed. Then T is Fredholm if and only if A is Fredholm. In that case

index(T)=index(A)-d+dim(F)-dim(G).

In particular, a non-Fredholm bounded operator cannot be made Fredholm by finitely many continuous linear domain conditions, scalar unknowns, finite-rank terms or finite-dimensional target extensions of the displayed form.

## Finite-codimension restriction

We first prove that A_E=A|E is Fredholm if and only if A is Fredholm, and that its index drops by d.

Assume A is Fredholm. Its finite-dimensional kernel N has a closed complement D_0 in D. Such a complement can be constructed by extending coordinate functionals on N using Hahn-Banach. The restriction A:D_0 -> R=range(A) is a continuous bijection between Banach spaces, hence a Banach-space isomorphism by the bounded inverse theorem. Let P_0:D -> D_0 be the projection along N. We claim

P_0(E)=(E+N) intersect D_0.

Both inclusions follow directly by writing e=P_0e+n. The space E+N is closed: the quotient map D -> D/E takes N to a finite-dimensional, hence closed, subspace and E+N is its inverse image. Thus P_0(E) is closed in D_0. The isomorphism just identified shows A(E)=A(P_0(E)) is closed in R and therefore in Y.

The kernel of A_E is a subspace of N and is finite-dimensional. The linear map D/E -> R/A(E), induced by v -> Av, is onto, so dim(R/A(E)) <= d. Together with the finite-dimensional quotient Y/R, this proves that Y/A(E) is finite-dimensional. Hence A_E is Fredholm.

Conversely, assume A_E is Fredholm. A closed finite-codimension subspace has a finite-dimensional complement F_0, so D=E direct-sum F_0 and A(D)=A(E)+A(F_0). This range is closed: its image modulo the closed subspace A(E) is finite-dimensional, hence closed, and the range is the inverse image of that subspace. Its codimension is finite because it contains A(E). Projection D -> D/E maps ker(A) into the finite-dimensional space D/E, with kernel ker(A_E). Thus ker(A) is finite-dimensional. This proves A is Fredholm.

For the index, all spaces in the following exact sequence are finite-dimensional:

0 -> ker(A_E) -> ker(A) -> D/E -> Y/A(E) -> Y/A(D) -> 0.

The middle map sends v+E to Av+A(E); all other maps are inclusions or quotient maps. Its kernel consists exactly of classes represented by elements of ker(A), because Av belongs to A(E) precisely when v-e belongs to ker(A) for some e in E. The other exactness assertions follow directly from the definitions. The alternating sum of the dimensions is zero, giving index(A_E)=index(A)-d.

## Finite-rank perturbations

For a bounded finite-rank map K:D -> Y, the kernel E_K is closed and has finite codimension. The restrictions of A and A+K to E_K are identical. The preceding result implies that A and A+K are Fredholm simultaneously. If they are Fredholm, applying the index-drop formula to their common restriction gives index(A+K)=index(A). This proves the required finite-rank invariance without a perturbation homotopy or an implicit compactness assertion.

Apply this result also with E in place of D. The map

T_0:E direct-sum F -> Y direct-sum G, T_0(e,f)=(Ae,0)

has kernel ker(A_E) direct-sum F, range A(E) direct-sum {0}, and cokernel (Y/A(E)) direct-sum G. Its range is closed exactly when A(E) is closed. Therefore it is Fredholm exactly when A_E is, and index(T_0)=index(A_E)+dim(F)-dim(G). The difference T-T_0 has finite rank: K and B have finite-dimensional ranges in Y, while all other components take values in the finite-dimensional G. Finite-rank invariance now proves the statement and its index formula.

## Conditional application to the source obstruction

The separate source_localization/PROOF.md establishes non-Fredholmness for a specified ordinary H^s graph realization under explicit source, coefficient regularity, core and adjoint concentration hypotheses. If a full realization satisfies those hypotheses, the present theorem shows that finite bounded border terms do not remove that obstruction. A finite scalar normalization term whose forcing lies in H^s and whose scalar coefficient functional is bounded in the chosen graph norm is a bounded finite-rank perturbation. If its forcing q lies outside H^s, it can instead be represented in a target extension H^s direct-sum span(q), provided this direct-sum target and the scalar functional have actually been defined as Banach spaces and a bounded map. The theorem then applies to that extended map, with its changed index bookkeeping.

Every domain restriction used here must be closed and have finite codimension in the selected graph norm. For example, evaluating the cubic center coefficient is not automatically continuous in ordinary H^s at s<4. An algebraic condition on a dense nonclosed subspace is not an E allowed in this statement. The theorem does not cover changing the infinite-dimensional norm, a weighted or anisotropic domain, an infinite collection of asymptotic coefficients, or a different closed realization. Such changes may alter the source obstruction and require separate analysis.

The source-localization hypotheses have not been established for the full weighted SPEC formulation or for an unknown exact P_2 profile. Consequently this is no existence or exclusion endpoint and no unconditional index calculation for IPM.

## Dependencies and verification scope

The proof uses elementary Banach-space quotients, Hahn-Banach, the bounded inverse theorem, and the elementary alternating-dimension formula for an exact sequence of finite-dimensional vector spaces. No numerical input or compact perturbation theorem is needed. The application additionally depends on the conditional source-localization theorem, not on a numerical fit or a presumed Fredholm homotopy.

## Verification record

The first actual claude-opus-5-5 review identified that boundedness of the finite-rank K was used by the proof but had not been explicit in the theorem statement. This was repaired, together with a single scalar-field convention and continuous linear domain conditions. The final review accepted the theorem at2026-10-20T16:36:01.252181+00:00, while requesting an explicit bounded scalar coefficient in the H^s normalization application; that premise is now stated. See notes/reviews/finite_modifications_response.md and finite_modifications_closure_response.md at the lane root, with actual-model metadata. No numerical calculation is involved.
