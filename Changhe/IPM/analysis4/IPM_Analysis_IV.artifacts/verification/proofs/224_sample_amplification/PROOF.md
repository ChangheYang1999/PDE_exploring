# A specified norm for the selected perturbation

Status: finite comparison verified in V463; the unqualified no-amplification claim is refuted in V464.

## Objects and claim being checked

Fix the two saved delta=2/3, unit-sine logarithmic continuations from217, both initialized through order329. For field A equal to density or stream and order n, write x_(A,n) for the full midpoint-run coefficient vector and y_(A,n) for the perturbed-run vector. All logarithmic and sine columns are included, and omitted coordinates are zero. Define

    d_(A,n)=||y_(A,n)-x_(A,n)||_1/||x_(A,n)||_1,
    D_in=max_{A,1<=n<=329} d_(A,n).

The zero-over-zero case, if both input vectors vanish, is assigned zero; a nonzero difference with zero reference norm would instead make this normalization undefined and must stop the audit. For each later n, use the same relative norm d_(A,n). A value d_(A,n)>D_in is amplification of this selected displacement in this specified norm. It need not be amplification in another norm.

## Finite verification argument

Decode each saved coefficient as its exact dyadic midpoint and nonnegative dyadic radius. Directed subtraction and absolute-value summation enclose the norm of every possible difference of vectors in the two saved boxes. Directed division by the strictly positive reference norm encloses d_(A,n). The interval maximum over the finite input set encloses D_in. Therefore an output lower endpoint strictly greater than the input upper endpoint certifies the displayed finite amplification. Conversely, upper endpoints below the input lower endpoint would certify attenuation at those tested output orders. If the intervals overlap, neither verdict follows from this comparison.

The reverse triangle inequality also gives

    | ||y_(A,n)||_1/||x_(A,n)||_1 -1 | <= d_(A,n).

Thus a difference of coefficient norms is a lower bound on the relative vector difference, not an interchangeable measure of the displacement. The calculation records both quantities and their distinction.

## Dependencies and limitations

Topic217 identifies the exact selected-input construction and verifies its saved values. The continuation intervals cover arithmetic for these selected input configurations. They do not enclose the full canonical uncertainty discarded at329. This comparison is finite and conditional on those configurations; it supplies no global Lipschitz constant, no bound for the entire input box, and no convergence or instability theorem for the infinite canonical series. It audits only the wording of the single-sample experiment under an explicitly defined norm.

## Verified finite comparison

For the two snapshots identified by SHA256 in verification/checks.json, D_in is enclosed near3.57601732305863e-6. The stream outputs at330 and331 exceed D_in by factors1.2284477612 and1.9183745652. All other tested outputs through340 lie below D_in. At340 the density and stream differences are respectively about3.34349e-8 and7.97135e-9. These statements use the full relative vector norm defined above, not a difference of scalar norms.
