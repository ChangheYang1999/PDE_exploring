# Direct-sum arithmetic follow-up

## 2026-10-29T02:07:33.805714+00:00: direct-sum audit arithmetic follow-up

The v1 ring audit failed its unchanged 1e-10 relative-vector tolerance at the two most polar rings of the smallest radius (2.21e-10 and 2.33e-10). All volume aggregates, norm comparisons and FFT driver checks passed. Preserve that failure. The direct trigonometric sums include a large constant co-rotating velocity whose exact derivative is zero. Recompute the same 15 rings after subtracting their azimuthal mean, using long-double rotation and integer powers of the normalized unit-complex direction instead of repeated binary64 trigonometric calls. In exact arithmetic this leaves every nonzero Fourier coefficient and derivative unchanged on a resolved uniform grid. No threshold is changed, and saved field values remain binary64. This follow-up tests numerical cancellation in the audit, not the pressure or a new field.
