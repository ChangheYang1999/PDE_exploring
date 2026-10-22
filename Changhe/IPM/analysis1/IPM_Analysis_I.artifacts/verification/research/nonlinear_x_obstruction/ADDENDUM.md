# Explicit regularity, normalization and finite arithmetic

2026-10-21. Read with PROOF.md.

H_1 and H_2 mean H_delta at delta1 and2. In this theorem Q_H is an explicitly defined advective unit polynomial U[H].grad H; it is not the full normalization-dependent Q(H). The actual global perturbation h_n has exactly zero Sigma, so its quadratic remainder is precisely its advective product. No separate rank-one term from each packet may be added to it. The total strain is canceled before that product is evaluated.

All velocity regularity used in the proof follows from the explicit unit stream. Its inner polynomial and two exterior rational modes match derivatives through order6 at radius1, as checked in topic137. The scaling U[H_delta](X)=delta^3 U[H](X/delta) makes U[g] a fixed linear combination of these C1 velocities. The translated, scaled packet velocities are also C1, so U[h_n] is C1 and the product with the C4 gradient of h_n is C1. Thus no general singular-integral bound at an L-infinity endpoint is being assumed. Near0 all the streams actually have explicit smooth expressions.

The unit stream is odd in each coordinate. Summing its four translates with all positive coefficients and relabeling their centers makes the total packet stream odd in x and odd in y. The g stream has the same parity. Consequently the full stream has odd-odd parity, psi_xy is even-even, and U[h_n](0)=0. For the diagonal strain, only that unit even-even mixed derivative is evaluated at the four signed diagonal points. The coefficient derivative of xy/r^4 there is3/(4A^4); the mode4 mixed derivative vanishes. One packet contributes-a epsilon^3/688128 and four contribute-a epsilon^3/172032. The compensator in(4) cancels it exactly.

For the error E_n in the unit packet coordinates, the two differentiated terms are

    (a/epsilon)(grad_Z R_n).grad H=O(epsilon^4),
    (a/epsilon)R_n.D2 H=O(epsilon^3).

The value term is also O(epsilon^3), since a^2=epsilon. These bounds hold uniformly on the fixed half-radius disk. The other packet centers have a fixed positive separation from this disk; no assertion that the minimal physical distance is exactly8 is needed.

Fresh symbolic Green integration and a separate rational radial-ODE solve agree on all451 Cartesian coefficients of H, psi, both velocity components, the unit advective polynomial and its two derivatives. Both obtain its nonzero cubic coefficient-1/56. Independent polar disk moments and horizontal-slice beta moments give exactly

    int_(|Z|<=1/2) |grad Q_H|^2 dZ
      = pi *1552530047839457441465148479
        /23683970648207968389305777258496000.

All405 even polynomial terms in this squared-gradient integral are included, with their signs. The final exact rational is positive. Arb512 and mpmath.iv180 independently enclose the positive integral; their exact endpoints are retained. Its approximate2.059374699123306e-7 display is informational and is not a claimed outward bound.

The diagonal stream derivative is also recomputed by rational quotient-rule polynomial recurrences, independently of symbolic differentiation. Four signed translates are checked exactly for n=2,3,7,100; the general formula follows from homogeneity and the verified exact diagonal coefficients, not from these examples. The fixed-strain compensator has J0, Sigma1 and leading radial factor84r^2.

The obstruction concerns the displayed X-to-X quadratic estimate. It does not exclude estimates with h measured in a stronger or graph norm, Q measured in a weaker norm, or a specified restricted finite-dimensional class. Every h_n is compactly supported, so it can preserve a prescribed leading far coefficient as a perturbation; this fact does not imply smallness in any stronger domain norm. No small linearized residual, stationary profile, inverse or IPM endpoint is established.
