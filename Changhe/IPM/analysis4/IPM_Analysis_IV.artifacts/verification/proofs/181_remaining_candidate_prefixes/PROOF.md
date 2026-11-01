# Prefix radii for the remaining Candidate-shaped branches

Status: PROVED for roots 5, 6, 7. All requested branches completed.

## Statement and exact hypotheses

Let delta=4/9 and c=9/5. Use the normalized Candidate-shaped leading profile and exact degree-nine compatibility polynomial of156. For i in {5,6,7}, let b_i be its i-th real root in increasing order, replacing only the coefficient of sin(3 theta). All other normalized coefficients are fixed exact rational numbers. Suppose163 proves a positive all-index response lower bound s_i for this branch.

Independently enclose its unique tuned coefficients through N=36, including H9,H18,H27, by the procedure below. For each prefix N in {9,18,27,36}, form172's residue majorant with its exact rational upper bounds d_j>j||f_j||_1 and e_a>9a|H_(9a)|, B=20, L=243/104, and

    kappa_N=(475/9)(N+1)/N.

If the retained rational vector u satisfies u>=Y0 and G(2^(-q),u)<=u, the density, stream and common potential series converge absolutely and uniformly, with every appropriately weighted derivative, on each closed exterior r>=R>2^(q/4). For leading amplitude epsilon the radius is multiplied by |epsilon|^(9/4).

Let a be the original positive first-harmonic amplitude in156. The exact inequality a^225<2^949 gives a^(9/4)<2^(949/100). Thus restoring Candidate007's amplitude gives the sufficient integer-power radius 2^E, where E=ceil(q/4+949/100). These are compatible modifications at delta4/9, not the unmodified Candidate007 profile or exponent.

## Proof

The exact polynomial and isolating interval156 determine each b_i uniquely. Rational bisection and directed ball arithmetic enclose this root. The independently implemented signed Cartesian recurrence propagates the root interval through every product and Poisson inverse without midpoint resets. Each Poisson equation is checked by second derivatives. At the first resonance, the root polynomial proves compatibility; at later resonances, the harmonic tuned nine orders earlier proves compatibility. The corresponding enclosure must contain zero before that known zero coordinate is projected out.

Two provisional continuations with the current free harmonic zero and one enclose its affine response and constant term. The division is performed only if the response ball excludes zero. The proof145 and all-index bound163 identify this harmonic with the unique exact tuned series. At N=36 the last harmonic is unnecessary: the prefix theorem uses H9,H18,H27 only.

Interval absolute values and upward rational rounding give the stated d_j and e_a. Substitution B=20 into176's B(19/9)(5/4)(N+1)/N yields the displayed kappa_N. The exact projected coefficient identities and the complete rational supersolution inequality then give precisely the hypotheses of172 and174. Their monotone coefficient iteration gives convergence at w=2^(-q), and the strict radius absorbs polynomial losses from any fixed number of derivatives. The common potential has the same strict convergence radius. Homogeneity and the exact amplitude inequality give the restored radius.

Every branch records its full root interval, arithmetic precision, exact dyadic coefficient bounds, response and harmonic enclosures, scalar coefficient checks, supersolution and image, source hashes and actual runtime. A failed finite computation or box search does not prove incompatibility or divergence.

## Completed root5 certificate

At 2026-10-31T13:32:38+00:00, the2048-bit independent prefix through36 passes73165Poisson coefficient checks,1818ordered products,six provisional continuations and four compatibility projections. The propagated exact root interval is never reset. ForN9,18,27,36, the ordinary box q values are208,172,172,172 and adaptive q values are208,172,171,171. All216direct scalar identities and four retained certificates pass. Thus R>2^(171/4)|epsilon|^(9/4) suffices, or R>2^53 after restoring the exact Candidate amplitude. The best q is first attained atN27. Runtime88.04970508115366seconds.

## Completed root 6 certificate

At 2026-10-31T13:47:13+00:00, V352 confirms the following. At 2048 bits, the independent prefix through order 36 passes 73,165 Poisson coefficient checks, 1,818 ordered products, six provisional continuations and four compatibility projections. No midpoint reset is used. For N=9,18,27,36, ordinary box exponents are [203, 168, 167, 167], and adaptive exponents are [203, 167, 166, 166]. All 216 scalar identities and 144 retained box components pass. The uniform response lower bound is 1/8192. Thus R>2^(166/4)|epsilon|^(9/4) suffices, with the best exponent first attained at N=27. Restoring the exact Candidate amplitude gives R>2^51. Actual computation took 90.43590484093875 seconds.

## Completed root 7 certificate

At 2026-10-31T13:56:50+00:00, V363 confirms the following. At 2048 bits, the independent prefix through order 36 passes 73,165 Poisson coefficient checks, 1,818 ordered products, six provisional continuations and four compatibility projections. No midpoint reset is used. For N=9,18,27,36, ordinary box exponents are [222, 176, 176, 176], and adaptive exponents are [222, 175, 175, 175]. All 216 scalar identities and 144 retained box components pass. The uniform response lower bound is 1. Thus R>2^(175/4)|epsilon|^(9/4) suffices, with the best exponent first attained at N=18. Restoring the exact Candidate amplitude gives R>2^54. Actual computation took 90.35046800179407 seconds.
