# Diagonal bounds from the accepted middle-circle certificates

## Statement and definitions

Use the homogeneous Euclidean Holder space, real or complex, with exponent 0<alpha<1 and seminorm [f]_alpha. Define T_xx by the circular principal-value kernel cos(2theta)/(2 pi r^2), extended modulo constants by convergent increments, and let D_alpha be the norm of R_1^2=T_xx-I/2. These are the conventions of ../../01_setup/PROOF.md.

Let W_j be an accepted upper bound for the middle functional of Theorem 3.6 at phase j*pi/32, let X_j bound the two cross-pole disks, and let E_j bound the exterior functional. Let

    A_alpha = Gamma((alpha+2)/2)/(2 sqrt(pi) Gamma((alpha+3)/2)),
    S_alpha = 2^(1-alpha) A_alpha/alpha + 1/2.

For alpha in {1/1000, 1/100, 1/20, 1/10, 1/5, 99/100}, the accepted constituent certificates give

    D_alpha <= S_alpha + sec(pi/64) max_j (W_j+X_j+E_j).

If the phase interpolation theorem in ../../08_improved_upper_bounds/phase_interpolation/PROOF.md has passed its independent cross-read and acceptance, the sharper right side is

    S_alpha + max_(0<=j<16) H_(pi/32)(W_j+X_j+E_j, W_(j+1)+X_(j+1)+E_(j+1)).

The neighboring formula defines H and proves its validity. Only accepted decimal values in verification/accepted.json are numerical claims. This note is written before the independent recombination.

## Why the constituents may be recombined

The middle functional in Theorems 3.6 and 3.7 is the same signed measure. Its admissible transport plans may depend on the exponent. The V131 direct certificates already bound this measure with such plans. V171 reduces only the residual middle-arc cost, without changing the extracted mass or transport plan. Consequently the old middle upper endpoint minus the exact certified residual saving is a valid W_j for Theorem 3.6.

The cross-pole disk certificate is the same one used by the previously accepted middle composite bound. For E_j, take the smaller rational upper endpoint of the two already accepted exterior certificates, one from the exponent-specific direct table and one from the earlier fine exterior calculation. The minimum is still an upper bound for the norm of that exterior functional at the same phase. Add W_j, X_j and E_j before interpolating or maximizing. The local projection contribution S_alpha is uniform in phase and remains outside that operation; in particular the local identity term is never interpolated on the smaller phase grid.

The proof therefore follows by the triangle inequality on the three regular pieces, the accepted local projection decomposition, and the phase interpolation theorem. The parent proofs establish all origin and infinity convergence statements. The same complex-input estimate follows from their real-kernel phase reduction.

## Independent arithmetic check

Read the already accepted V131 middle and exterior arrays, the exact V171 residual savings, and the cross and fine exterior ball records. Check every dependency hash. Treat each stored ball endpoint as an exact rational bound. At each node subtract the nonnegative residual saving, add the cross upper endpoint and the smaller exterior upper endpoint, and then evaluate the two phase rules at 384 bits. Recompute the near term and the phase maximum at 768 bits through a separate cosine-sine amplitude expression. Verify all proposed upward decimal roundings. Compare the original secant values and maximizing node with the frozen lead submission.

This is a recombination of independently accepted geometric certificates, not a new optimization or a claim about the actual maximizing operator phase.
