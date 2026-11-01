# Explicit exterior radii for the delta3/5 branches

Status: root4 is PROVED with exponent65/3, V424, and root1 with exponent139/6, V428. Root2 has exponent70/3, V437. Root3 has exponent67/3, V446. All four radius claims are PROVED.

## Statement and hypotheses

Fix one of the four real compatibility roots b from topic200, and start with f1=sin(theta)+b sin(3theta), delta=3/5 and c=5/2. Assume topic204 supplies a certified rational lower bound s>0 for every tuning response, and topic202 supplies independent enclosures of the tuned coefficients. For N in{10,20,30,40}, use positive rational upper bounds

    d_j >= j ||f_j||_1,  1<=j<=N,
    e_a >= 10a |H_(10a)|,  1<=a<N/10.

The procedure below certifies a finite q such that the infinite density, stream, common potential and all their appropriately weighted derivatives converge uniformly on every closed exterior r>=R>2^(q/6). For leading amplitude epsilon, the threshold is multiplied by |epsilon|^(5/3). A successful smaller q improves a sufficient bound only; it does not identify the true radius.

## Majorant constants and complete argument

The frequency bounds are4j-1 for density and4j for stream. Set h=3, Q=10 and B=4. The uniform bound on the particular Poisson inverse proved in topic169 is

    L=3Q^2/[4(3Q-1)]=75/29.

The common nonlinear constant in topic172 specializes to

    kappa_N = B[2-delta+max(delta,1-delta)](1-delta)(N+1)/(delta N)
            = 16(N+1)/(3N).

Apply the residue-class majorant map Phi of topic172 with these constants and the certified inputs. Its coordinates are the nine look-ahead series, the unknown harmonic series and the ten density residue series. At w=0 the map is c+JY with nonnegative strictly lower triangular J. Thus T=(I-J)^(-1) is the finite nonnegative sum I+J+...+J^19. Put Y0=Tc and G(w,Y)=Y0+T[Phi(w,Y)-Phi(0,Y)].

For an explicitly retained positive rational box B0, verify G(2^(-q),B0)<B0 in every coordinate. Iteration from zero has nonnegative coefficients, is bounded at this positive argument and therefore converges there. The scalar comparison induction of172 bounds every exact future coefficient of the tuned solution by the corresponding majorant coefficient. Since w=z^Q=r^(-6), convergence holds at each strict radius r>2^(q/6). The finite Fourier bandwidth and a strict radius margin permit any fixed number of angular and radial derivatives. The common potential exists without exceptional logarithms for h=3 and is reconstructed in202; its multipliers have at most polynomial growth, so the same strict radius suffices.

The computation also compares the first three coefficient layers of the residue map with an independently indexed direct scalar recurrence. This is an implementation check; the all-order implication is supplied by the proved map and monotone iteration, not by those finite comparisons.

## Evidence and scope

All norm upper bounds are obtained from exact dyadic midpoint/radius records by outward rational rounding. The full rational matrices, boxes, images, maximum coordinate ratios, input hashes and actual times are retained. No claim is admitted if a response or prefix input is missing. Failure of a smaller trial box does not prove that the solution diverges there. Global stationary extension and sharp radii remain outside this result.

## Root4 certificate, 2026-10-31T15:19:35+00:00, V424

The response lower bound is2^(-22). Prefix lengths10,20,30,40 give q=164,131,131,130, respectively. The smallest retained radius exponent is therefore65/3, attained at prefix40. All four saved maps were rebuilt from their exact inputs and every coordinate satisfies strict box invariance. Each case also passes60 direct scalar coefficient checks. The original calculation took2.808 seconds and the separate exact replay0.318 seconds.

## Root1 certificate, 2026-10-31T15:28:28+00:00, V428

The response lower bound is2^(-42). Prefix lengths10,20,30,40 give q=169,139,139,139. The smallest retained exponent139/6 is already attained at prefix20. All four exact maps pass their60 scalar checks and strict20-coordinate box inequalities. Computation2.788 seconds; exact replay0.324 seconds.

## Root2 and root3 certificates

Root2 has a sufficient exponent70/3, V437. Root3, completed2026-10-31T15:57:37+00:00, has prefix10,20,30,40 exponents83/3,45/2,45/2,67/3. Each saved box passed a separate exact replay. Therefore R>2^(70/3)|epsilon|^(5/3) is sufficient for all four branches. The branches need not have this sharp radius.
