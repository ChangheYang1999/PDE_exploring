# Actual audit result and limits

2026-10-21T16:54Z. check_v2 passed at16:48:02Z. It independently reconstructed192 exact relative changes from the saved binary64 inputs, with384 enclosing calculations split between Arb384 bits and mpmath.iv140 decimal digits. All336 decimal rounding cells in the captured summary contain the corresponding exact values. Forty-eight saved maximum triples were checked against the printed table. The1100 grid-point checks use floating elementary functions and establish only diagnostic membership in the reported grids and regions.

The follow-up check_supplement_v2 passed at16:53:22Z. It checked24 more exact ratios with48 interval enclosures, the three explicit source axis assignments, the chronological source caveats, the derived rational p, both normalization columns, and six zero-source far maxima at the outermost grid point. Two initial failed programs remain beside the successful versions. The primary failure was conversion of a flint rational to Fraction; the supplementary failure was an incorrect expected equality count. Neither failed run produced an accepted output.

| Variant | Largest absolute relative change of24 stored maxima |
|---|---:|
| extent1e5 L, altered nominal step | approximately0.00390482 |
| extent1e7 L, altered nominal step | approximately0.07879325 |
| extent1e11 L, same nominal step | approximately1.17546125e-9 |
| half-step shift | approximately0.01499595 |
| fit window0.5 decades | approximately1.17546125e-9 |
| fit window2 decades | approximately2.47143440e-6 |
| one-power source fit | approximately0.44827538 |
| zero exterior source | multiplier range approximately21.3515 to2892.435 |

The one-power absolute relative changes range from approximately0.296% to44.828%. The saved two-resolution and sampling/window family, excluding the two changed-power closures, puts the r in[2,10] absolute lobe maxima between approximately5.61068922e-5 and6.98428923e-5. These are ranges across saved observations, not error bars.

The near-center r<=0.1 Nf maxima illustrate the normalization-column distinction:

| File | Stored c_l column | Recomputed identity c_l column | Computed c |
|---|---:|---:|---:|
| baseline | 2.64238975786e-10 | 2.32672812320e-11 | 15.726087821661109 |
| zero exterior source | 6.84171119519e-7 | 2.17221055647e-10 | 15.726058699527437 |
| one-power source fit | 1.58230497844e-10 | 2.32810289747e-11 | 15.726087826176837 |

Each entry is a saved regional maximum. Its location can differ between columns. This table does not measure degree3 cancellation pointwise or bound higher terms. PROOF establishes that cancellation algebraically under its normalized-center hypothesis.

For td05, exactly22 of24 stored maxima and22 of24 identity maxima equal baseline. The other two are the1000<=r<=1000L Nv maximum at the last-bit scale and the far Nv maximum at about1.18e-9 relative scale. For ext1e11 there are23 exact equalities per column, with only the far Nv maximum changed. For a fixed column those far changed scalars coincide exactly across the two files. The computed c values for baseline, td05, td20 and ext1e11 coincide exactly as binary64 values. The cause of these coincidences is not independently established. Their equality as saved data is not a bound on the canonical inverse error.

The analytic four-power expansion is CONFIRMED under its stated exact formula. The exterior-source and leading-degree cancellation identities are CONFIRMED. Arithmetic consistency of the saved summary is CONFIRMED at the stated rounding-cell precision. The density-cutoff description is REFUTED as a source interpretation. Historical execution provenance, physical maxima, quantitative asymptotic remainder, source fit conditioning and accuracy, continuum residual enclosures, admissible-space inverse and every decisive IPM endpoint remain OPEN.
