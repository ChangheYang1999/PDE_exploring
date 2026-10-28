# Phase coverage after the local diagonal estimate

## Statement

Let 0<alpha<1, and use the real homogeneous Euclidean Holder space, circular principal values and extension modulo constants of 01_setup/PROOF.md. Put x=1/2, y=-1/2, G(z)=z/(pi(z^2-1/4)^2), and K_phi(z)=Re(exp(i phi)/(2pi z^2)). Let M_phi be the regular increment functional remaining after the two radius-1/2 local convolutions are removed from the K_phi increment. If B_j is an upper bound for the norm of M_{j pi/(2m)}, then

D_alpha <= 2 A_alpha 2^(-alpha)/alpha + 1/2 + sec(pi/(4m)) max_{0<=j<=m} B_j,

where A_alpha=Gamma((alpha+2)/2)/(2 sqrt(pi) Gamma((alpha+3)/2)). The regular estimate may further split the functional into cross-disk, middle and exterior terms, provided their bounds are summed at a common phase before the maximum. In the accepted numerical application m=16.

## Proof

Write L_phi for the two local convolutions and M_phi for the rest. The projection decomposition in 08_improved_upper_bounds/local_projection/PROOF.md gives, for every phase and every input with Holder seminorm at most one, an upper bound 2 A_alpha 2^(-alpha)/alpha for the two paired terms. The remaining convolution measure together with the local identity term has total mass 1/2 and one sign. Its increment has absolute value at most 1/2. Rotation of that measure with phi preserves its mass and positivity. Consequently this part is bounded uniformly before the phase discretization.

The regular functional M_phi equals cos(phi) M_0+sin(phi) M_{pi/2}. Its operator norm is the restriction of a seminorm of these two real coefficients. The domains of its cross-disk, middle and exterior pieces are invariant under conjugation, and G(conj(z))=conj(G(z)), with the same identity for the individual rational kernel terms. Conjugating the input is an isometry of the Holder seminorm and sends M_phi to M_{-phi}. Thus their norms are equal. Changing phi by pi negates the functional and leaves its norm unchanged. It suffices to cover [0,pi/2].

For two successive grid nodes at distance delta=pi/(2m), every intervening unit coefficient vector is a nonnegative linear combination of the endpoint vectors with coefficients whose sum is at most sec(delta/2). The triangle inequality for the regular operator seminorm gives the stated estimate. Each B_j may be the sum of any valid bounds for its three pieces; the pieces are evaluated at the same node. Adding the already uniform local bound proves the claim.

## Audit scope

This argument applies to the accepted middle-circle D upper bounds, whose implementation is code/combine_middle_upper.py and whose residual replacement is code/combine_middle_balanced_residuals.py. It does not justify a [0,pi/2] grid for a different density that retains fixed identity atoms inside the phase-dependent transport problem. That separate construction needs the larger range described in 08_improved_upper_bounds/paired_local_diagonal/PROOF.md. No numerical endpoint is asserted by this reread alone.
