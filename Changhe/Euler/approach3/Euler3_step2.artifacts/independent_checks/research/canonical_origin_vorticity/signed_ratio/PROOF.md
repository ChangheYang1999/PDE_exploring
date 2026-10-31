# Signed origin ratios

## Statement

Let U be a smooth divergence-free field satisfying the finite-potential hypotheses in ../general_modes/PROOF.md. Let Omega = curl U and let R_Omega be the rotating vorticity residual defined there. Put a = R_Omega,3(0) and b = Omega3(0). Suppose exact rational closed intervals A = [a_minus,a_plus] and B = [b_minus,b_plus] contain a and b, respectively, and 0 does not belong to B. Then b is nonzero and

    a/b belongs to [min E,max E],
    E = {a_minus/b_minus, a_minus/b_plus,
         a_plus/b_minus, a_plus/b_plus}.                         (1)

If B contains zero, this interval rule makes no ratio assertion. It does not assign a value to a possible 0/0. A nonzero numerator still provides the exact field obstruction from the parent proof, whether or not the ratio is defined.

In the even-azimuthal class of ../../canonical_origin_vorticity/PROOF.md, write the four alternating coefficient sums as a1,a2,g1,g2 and nu2 = sqrt(5/(16 pi)). If a1 is nonzero, the sharper formula is

    a/b = 1 + 12 nu2 (g1 a2/a1 - g2).                            (2)

All saved binary64 coefficients are interpreted as exact rational numbers. Thus (2) divides by the exact nonzero rational a1. It requires no uncertain interval denominator.

## Proof

Because B is a closed interval avoiding zero, it is contained in either the positive or the negative half-line. The reciprocal map is continuous and decreasing there. It maps B onto [1/b_plus,1/b_minus]. Multiplication of two real intervals has extrema among the four endpoint products: for a fixed second argument the product is linear in the first, and after taking either endpoint it is linear in the second. Applying this observation to A and the reciprocal interval proves (1), including negative denominators and numerator intervals crossing zero.

The even-mode origin identities give a = 2 nu1 [a1 + 12 nu2(g1 a2-a1 g2)] and b = 2 nu1 a1, where nu1 = sqrt(3/(4 pi)) is positive. Cancel the common factor and divide by a1 to obtain (2). If a1 = 0, b is exactly zero and no signed ratio is defined.

For decimal presentation at an integer scale D > 0, floor(D times the lower endpoint)/D and ceil(D times the upper endpoint)/D enclose the same ratio. Integer division of exact rational numerators computes those bounds without binary floating-point rounding.

## Interpretation and dependencies

This signed ratio is a pointwise component diagnostic. It is neither a norm of R_Omega nor an estimate of distance from an Euler solution. In the general-mode class it depends on the chosen axial direction; it can become large because the axial vorticity is small. The exact residual vector must therefore be reported beside it. A zero-containing component interval is inconclusive unless a separate exact identity establishes cancellation.

The parent general-mode proof supplies the residual and vorticity intervals. The even-mode proof supplies (2). No pressure evaluation enters the ratio. A point residual excluding zero obstructs only the exact represented field with the stated smoothness hypotheses. It does not exclude nearby fields, prove profile nonexistence, or bound an integrated residual. Formal verification is not claimed.
