# Stronger radial weights on the higher background derivatives

## Statement

For the exact recovered state131 and its canonical full-plane velocity,

    sup_X <r>^2 |D^4 rho(X)|_F <512,
    sup_X <r> |D^3 U(X)|_F <16,

where <r>=(1+|X|^2)^(1/2) and the Frobenius norms count every ordered Cartesian derivative. These are continuum inequalities for this reference, not assumptions on a new reference or bounds from a grid.

## Exact algebraic formulas

Use the source, polynomial derivation and parity conventions of SHARP_COEFFICIENT_PROOF.md. Put t=r^2/(1+r^2), z=cos(2theta), delta=1-1/c, q=(1-t)^(delta/2). The exact sixth- and seventh-order polar recurrence, with all negative powers cancelling as rational identities, gives

    D^3 U=(1-t) sum_(j=0)^3 q^(j+1) P_(3,j)(t,z) A_3(theta),
    D^4 rho=sqrt(t)(1-t)^(3/2) sum_(j=0)^3 q^(j+1) P_(4,j)(t,z) A_4(theta).

Each tensor component has its own rational polynomial and angular factor. The factors A_3 are1 or sin(2theta); A_4 are sin(theta) or cos(theta). The identities follow from U=(-chi_xyy,chi_xxy), rho=-chi_xxy-chi_yyy. Consequently the radial factors for the displayed theorem are exactly

    sqrt(1-t),                     for <r>D^3 U,
    sqrt(t)*sqrt(1-t),              for <r>^2 D^4 rho.

No asymptotic truncation is used. The formulas extend continuously to the compactified endpoints. Quadrant parity extends the bounds to the whole plane.

## Interval verification and source binding

The script verification/r2_extra_audit.py reconstructs all rational polynomials directly from the recovered original state. It compares them exactly with extra_coefficient_polynomials.json and verifies the source hash against the earlier independently audited certificate. That earlier audit includes all13 distinct components at seven rational points against seventh-order Cartesian potential jets, and rejects non-finite values. The exact polynomial equality makes those checks apply to the current polynomials as well.

The script traverses the entire315-leaf binary partition of extra_coefficient_certificate.json. It reconstructs every Bernstein subdivision at384 bits, verifies exact rectangle coordinates and complete binary coverage, and rejects a leaf with a descendant. On each rectangle it takes the Bernstein hull of the polynomial in t,z and the degree-four polynomial in q. The angular factors are bounded on that same rectangle. It then multiplies by the nonnegative radial bounds above and sums the squared tensor-component bounds with binomial multiplicities. Thus different component maxima are allowed at different points, as required for an upper bound.

The largest recomputed enclosures are below324.712695 and8.091291, respectively. Every leaf is strictly below512 and16. The complete enclosures, input hashes and source hash are in verification/r2_extra_audit.json. A final audit checks all leaf bounds and binds the proof and script hashes. The chronological verifier ledger records the resulting verdict. This proof uses V045 and V047 only for the already audited algebraic source and Cartesian comparison, not for an interpolation of their weaker radial bounds.
