# Complete two-engine C2 repair audit

2026-10-21. All selected 90 M16 and187 M24 radial columns have degree7 on their first piece and distinct support starts. Their 2216 pieces lie strictly inside -5<t<9. Quintic corrections therefore preserve their nonzero leading first-piece coefficients and give 90 and187 independent C^{2,1} radial functions. Including angular modes gives 1440 and4488 independent compact-annular functions, respectively.

Both exact engines check all4432 value traces, all4432 first-derivative traces and all4432 second-derivative traces. All13296 endpoint jet values agree with their prescribed shared targets. At both support endpoints all three target jets are exactly zero. Both engines agree on all13296 rational correction coefficients and all4432 exact polynomial integrals. Every repaired coefficient is stored in evidence/compute.json and is independently reconstructed in evidence/independent.json. The sources are the frozen metadata from the earlier jump audit, not mutable numerics-lane output.

| Strict upper bound | M16 | M24 |
| --- | ---: | ---: |
| Single-column broken norm of C2 repair minus raw column, divided by raw broken norm | 1.1482e-14 | 3.3788e-14 |
| Single-column X distance from the C0 repair, divided by the C0 repair's X norm | 1.993e-14 | 5.9465e-14 |

Each displayed decimal is an exact rational, strictly rounded upward. The first row holds for every single angular mode, including modes beyond the finite reported collections. The extremal computed upper ratios occur at zero-based source columns50 and95. The second row applies to topic132's exact C0 repair of the same raw column and same angular mode, with the same weight parameters. It is a true X distance. All entries are ratios of norms, hence square roots of energy integrals; they are not the same relative bound on squared energy.

The first engine solves a physical-width 3-by-3 rational linear system after fixing the left three jets, integrates polynomial convolutions exactly, and encloses increasing endpoint weights with Arb512. The second uses a NumPy-free restricted metadata reader, independent binary64 bit decoding, explicit unit-width quintic Hermite functions and the exact Hilbert moments integral_0^1 s^(i+j)=1/(i+j+1). It evaluates the weights with mpmath.iv120 via exp/log. All36 Kronecker endpoint identities of the six Hermite functions are checked exactly. Both interval engines verify the same strict public ceilings. No floating root or outward direction is assumed from a printed decimal.

The resulting factors vanish near the origin and preserve its normalization when added to a density. They are C^{2,1}, and thus C^{2,alpha}_loc for0<alpha<1, rather than necessarily smooth. Under topic135's explicit background hypotheses their operator images have local H1 regularity. Nothing here bounds the difference of operator images in a global norm; the older C0 repair may not even have an H1 image.

The exact new family is usable as a mathematical trial family, but no old matrix, eigenvalue truncation, floating whitening, quadrature or singular value has been transferred to it. The inverse problem and both IPM endpoints remain OPEN.
