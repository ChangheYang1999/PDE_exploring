# Common-potential logarithms for the seventh and ninth harmonics

Status: PROVED. Exact Cartesian and polar calculations agree, and the independent theory-part review at18:19Z confirms the reconstruction, uniqueness, logarithm sign and amplitude scaling. Admitted in V524.

## Statement and notation

Take h=2, Q in {5,7}, delta=4/Q, c=Q/(Q-4), M=Q+2, and leading density f_1(theta)=epsilon sin(M theta), with real epsilon nonzero. The already admitted tuned density and stream series converge on their stated exteriors. Define the following constants at unit amplitude. At the first resonance n=Q, let beta_pure be the frequency-two stream amplitude forced by a pure degree-zero common potential representing f_Q. Let R_1 and sigma_1 be the constant and linear parts of the order-2Q compatibility condition when the free frequency-two stream coefficient is H_Q. Set

    H_Q=-R_1/sigma_1,    lambda_Q=beta_pure-H_Q.

If sigma_1 and lambda_Q are nonzero, every common potential on the prescribed exponent lattice for this tuned density and stream pair requires the term epsilon^Q lambda_Q log r at order Q, modulo the irrelevant constant gauge. A pure common-potential series cannot satisfy the order-2Q compatibility condition. Exact calculations below determine these two constants for each of the two profiles.

## Derivation

At n=Q the density, stream and potential exponents are -3, -2 and0. The first compatibility frequency1 is absent by the signed-support theorem, so its coefficient is exactly zero. If D_(2k) are the cosine coefficients of the degree-minus-two field Delta chi, then the density identity gives

    a_1=2D_0=0,
    a_(2k+1)=(k+1)D_(2k)+kD_(2k+2),    k>=1.

Finite-support backward substitution, starting above the largest frequency, determines D_(2k). The associated pure potential has cosine coefficient -D_(2k)/(4k^2). The smooth periodic pure degree-zero solution is unique modulo a constant by the common-potential uniqueness argument in36. Direct differentiation gives beta_pure=D_4/8.

The next compatibility condition is R_1+sigma_1 H_Q=0. Since sigma_1 is nonzero, the only possible free amplitude is the one in the statement. The harmonic logarithm satisfies Delta log r=0 and partial_xy log r=-r^(-2)sin(2theta). Adding lambda_Q log r changes beta_pure to H_Q without changing the density. If lambda_Q is nonzero, no constant gauge can remove this correction and no pure degree-zero potential has the required stream coefficient. Every term at order Q scales by epsilon^Q under the quadratic recurrence, proving the general amplitude factor.

All later common-potential reconstruction is supplied by the admitted rational theorem; the only exceptional logarithmic order for h=2 is Q. This result concerns the common potential. It does not introduce logarithms into the tuned density or stream, and it asserts no whole-plane extension.

## Independent exact check

Construct the first Q density coefficients and their particular streams with the exact Cartesian recursion. Continue twice to order2Q, with H_Q=0 and1, to determine R_1 and sigma_1. Continue a third time using the resulting exact H_Q and require the order-2Q obstruction to vanish exactly. Independently construct the finite pure degree-zero potential from the D coefficients and differentiate both it and its logarithmic correction. Require exact equality of every density and stream coefficient. The sign or nonvanishing of lambda_Q is taken from its exact rational, not from floating-point subtraction.

Dependencies:01 for Cartesian signs and the density recurrence,36 for pure-potential uniqueness and gauge,144 for affine response,228 for the same degree-zero reconstruction,233 and241 for the separately admitted convergence of the two density/stream pairs.

## Exact results

Both exact implementations agree on beta_pure, R_1, sigma_1, H_Q and lambda_Q. The Cartesian implementation also verifies every coefficient of the reconstructed density and stream, and checks the tuned order-2Q obstruction exactly. The polar replay confirms that the pure-potential obstruction R_1+sigma_1 beta_pure equals sigma_1 lambda_Q and is nonzero.

| Leading unit profile | sigma_1 | H_Q | lambda_Q | Sign of lambda_Q |
|---|---:|---:|---:|---:|
| sin(7 theta), delta=4/5 | 0.0000194701466744668482055 | 0.000843850893134458693432 | -0.000844351932666868990396 | negative |
| sin(9 theta), delta=4/7 | -0.00959906357874719218656 | -0.000127607811755652271611 | 0.000125629761803687664577 | positive |

The table is a decimal display. The exact rational constants and exact equality flags are in verification/checks.json; the independently reproduced constants and exact nonzero pure obstructions are in verification/polar_replay.json. The sign follows from those rationals. For arbitrary real nonzero epsilon, the necessary logarithmic coefficient is epsilon^Q lambda_Q. In particular, the unit-amplitude sign reverses when epsilon is negative because both Q values are odd.
