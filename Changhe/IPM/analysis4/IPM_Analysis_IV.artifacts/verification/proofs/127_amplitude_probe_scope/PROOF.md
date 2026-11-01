# What an amplitude-perturbation probe can certify

Status: logical audit of a numerical inference. The counterexample below is exact; finite measurements of the actual K30 probe are recorded separately.

## Claim being tested

The c=3 recurrence with fixed edge cutoff K is homogeneous in the leading amplitude a: in exact arithmetic its order-n coefficient is a^n times the coefficient at a=1. The same holds for positively homogeneous coefficient norms with a>0. Numerics compared two binary64 runs, at a=1 and a=1+10^(-10), by subtracting n log10(a) from each perturbed log norm. Close agreement tests sensitivity to this perturbation.

It does not, by itself, prove that the computed coefficient or norm is accurate, nor exclude roundoff as the source of an observed departure from a different recurrence.

## Exact counterexample to the inference

Let the exact target at order n be x_n(a)=a^n x_n(1). Choose any numbers e_n, however large relative to x_n(1), and suppose a numerical procedure returns

    xhat_n(a)=a^n[x_n(1)+e_n].

The normalized outputs xhat_n(a)/a^n agree exactly for every a, although the normalized error is e_n and may be arbitrary. For positive targets the same example applies to log norms. Such shared errors can represent a consistently perturbed recurrence, omitted channels, or a systematic numerical error. Therefore agreement alone cannot place a rigorous bound on their size. It is not necessary that every possible systematic error arise in the particular implementation to disprove the proposed logical implication.

A stronger binary example also explains why merely changing amplitude does not guarantee independent rounding patterns: for exactly representable powers of two, binary floating-point scaling commutes with each homogeneous operation while all intermediates remain normal and finite. The chosen amplitude 1+10^(-10) is not such a power; this observation is explanatory and is not an assumption about the actual run.

## Appropriate conclusion for the observed probe

If the measured normalized discrepancies are much smaller than the multi-decade K30/full difference, the probe is empirical evidence against an error mechanism strongly sensitive to this amplitude perturbation. Call it a sensitivity check. A rigorous finite conclusion requires, for example, sufficiently narrow independently checked interval enclosures for both recurrences at the relevant orders. A higher-precision repeat is additional empirical evidence unless its error is certified. Neither kind of finite comparison proves infinite convergence or divergence.

The audit does not assert that the observed K30 departure is false or caused by roundoff. It rejects only the inference that one amplitude probe has rigorously excluded that cause.
