# Exact supersolutions with independently sized components

Status: PROVED. Independent analytic review of171 and172 was completed by the theory part at2026-10-31T13:01Z. The exact supersolution certificates are confirmed in V325,V326,V330,V332.

## Statement

Let G(w,Y) be the transformed polynomial map of171 or172. Its coefficients are nonnegative, and every term depending on Y has positive degree in w. Suppose a rational w0>0 and a nonnegative rational vector b satisfy b>=Y0 and G(w0,b)<=b componentwise. Then the scalar coefficient series is summable at w0, and the corresponding tuned IPM series has every weighted derivative convergent on each strict exterior r>=R>w0^(-1/(2h)).

The components of b need not have a common ratio to the components of Y0. The earlier choice b=2Y0 is a convenient search family, not a hypothesis of either convergence proof.

## Proof and certificate boundary

Starting with zero, iterate G as a formal power series. Nonnegativity and the supersolution inequality bound each iterate at w0 by b. Every coefficient stabilizes after finitely many iterations because all dependencies on unknown coefficients carry positive w degree. Monotone convergence therefore bounds the sum of the unique nonnegative formal solution by b. The scalar domination and potential reconstruction from171 or172 give the stated exterior conclusion.

An approximate iteration may propose the components of b. Its arithmetic and convergence have no role in the proof. Convert each proposed component to an explicitly retained rational value, check it is at least Y0, and reevaluate the complete polynomial map using exact rational arithmetic. Only the exact componentwise inequality certifies a supersolution. An unsuccessful proposal does not disprove existence of another supersolution or divergence of the IPM series.

The implementation records the input certificate hashes, every retained rational box and exact image, and its actual elapsed time. A reported dyadic exponent is the smallest successful exponent found by this specified search, not an optimal analytic radius. Profile coefficients, Poisson bounds, response bounds and initial-prefix bounds retain their separate certificates and scope.

## Recorded boxes

For the largest two-mode4/9 root, sharp response bound4114 and prefixes9,18,90 give w-exponents147,118,117. The last yields the proposed sufficient radius2^(117/4). The corresponding old-response exponents are171,130,129. The other four two-mode roots give152,146,161,151 with sharp response bounds. Candidate-shaped roots2,3,4 give194,200,198. Every complete rational vector and its exact image are retained in verification. The total search took7.251298449933529 seconds.

## Independent review closure

The theory part independently rederived the scalar domination, every residue projection and the constant-level triangularity at2026-10-31T13:01Z. All exact boxes already passed. The earlier pending status above records the audit chronology; the theorem and these sufficient radii are now PROVED. The167 root interval is propagated through every Cartesian operation and every computed harmonic without a midpoint reset. Thus its prefix bounds contain the exact uniquely tuned coefficients at the exact algebraic root. The65-digit export bounds are treated as enclosing intervals before upward rational rounding.

## Testing an already admitted box at a larger argument

Rebuilding a retained map from its exact rational inputs and checking its stored image is a finite reproducibility check. For that same nonnegative box u, if any component of G(2w,u) exceeds the corresponding component of u, this box fails at 2w. It does not follow that every box fails there. Conversely, if every component remains at most u, the existing theorem admits the same box at 2w and gives a sharper sufficient radius. The replay records this distinction explicitly. No optimality statement follows from a failed search for another box.

## Retained prefix replay at 2026-10-31T13:47:34+00:00

All 103 retained prefix boxes from topics176,178,179,181,182 replay exactly: the rebuilt Y0 and image equal the stored rationals, and each image lies inside its box. The same retained box fails at twice w in all 103 cases. Every input hash matches. Actual map replay took 12.433729719836265 seconds. V353 confirms this finite replay. Failure at twice w concerns only the retained box and cannot exclude other supersolutions.
