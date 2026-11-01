# The stored rational parameter and the scope of the prime-denominator theorem

Status: CONFIRMED by exact integer arithmetic, V382 and V384. No new compatibility result is claimed.

## Exact statement

Candidate007 has stored c=4076476460239181/2251799813685248 and therefore delta=A/D with A=1824676646553933 and D=4076476460239181. These integers are relatively prime, A is odd, and

D=127 * 114599 * 280091797.

The numerator factors as A=3 * 883 * 5737 * 6133 * 19577. All five numerator factors are prime.

All three denominator factors are prime. The first positive order for which n delta is an even integer at least4 is n=2D=8152952920478362.

## Complete argument

Subtracting the denominator of c from its numerator gives A. The Euclidean algorithm verifies gcd(A,D)=1. Since A is odd, gcd(A,2D)=1. Consequently nA is divisible by2D if and only if n is divisible by2D. At n=2D, n delta=2A>=4, so this is the first true stream resonance. Multiplying the three displayed factors proves the factorization; testing divisibility by every integer through the floor of the square root of each factor proves their primality. The finite check uses only exact integer arithmetic.

TheoremP in the theory part's section10.1 assumes a prime denominator p and an even numerator a<p, with first resonance at p. The stored parameter satisfies neither that denominator hypothesis nor the even-numerator hypothesis. Substituting the factor127 for the full denominator cannot repair the proof: for an order i divisible by127, the displayed denominators D(2j+2)-iA and D(2j-2)+iA are both divisible by127. The assertion that all these denominators are units modulo127, used for every i below the first resonance in TheoremP, therefore fails already at i=127. Likewise, the density multiplier (n-1)A/(D-A) vanishes modulo127 at n=128 because D-A is a unit modulo127. Those orders are far below the stored first resonance.

These facts only identify missing hypotheses in a proposed direct application of TheoremP. They do not prove that a more elaborate prime-adic argument is impossible, and they do not prove compatibility or incompatibility at the stored resonance. That coefficient remains OPEN.

## Dependencies

The exact extracted parameter was already independently verified in the initial Candidate007 audit. The factorization was proposed by the theory part in its note headed14:10Z. The original source is read-only. A local exact arithmetic replay and hashes are retained alongside this proof.

## Numerator replay, 2026-10-31T14:27:44+00:00

The exact arithmetic replay at 2026-10-31T14:25:56Z verifies both products and all eight prime factors. For numerator factors 3, 883, 5737, 6133, 19577, the exhaustive trial-division counts are 0, 28, 74, 77, 138. Every possible divisor through the integer square root is tested. The replay took 0.0021844152361154556 seconds. The first-resonance and theorem-scope conclusions above are unchanged. Full results are in verification/checks.json.
