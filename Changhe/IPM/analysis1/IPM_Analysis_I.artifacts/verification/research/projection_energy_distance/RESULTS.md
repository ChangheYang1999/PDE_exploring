# Saved projection scalars: exact arithmetic audit

Written 2026-10-21T20:13:36.723307+00:00. Read PROOF.md and ADDENDUM.md together.

The exact Hilbert-space identity is confirmed. The interpretation of99.5percent captured squared norm as0.5percent relative norm distance is refuted. It instead gives7.07to7.08percent. Four legacy files have saved full-energy ratios above1, so those pairs of numbers cannot be exact orthogonal-projection energy ratios in one consistent full norm.

The frozen version2 threshold diagnostics, recomputed from their exact binary64 energies, lie in the following open intervals. These are intervals for calculations on saved floating numbers, not enclosures of physical projection errors.

| frozen version2 file | relative norm distance, percent | retained columns |
|---|---:|---:|
| Kproj2_M16_s16_NJ0.npz | (1.81764,1.81766) |1866|
| Kproj2_M16_s16_NJ1.npz | (1.81776,1.81779) |1834|
| Kproj2_M16_s16_NJ1_free.npz | (1.76198,1.76201) |1850|

Independent NumPy/Fraction and manual ZIP/NPY/IEEE decoding agree on59 scalar imports. Arb256 and mpmath.iv80 enclose all9 threshold diagnostics and each pair is checked by squaring against the exact rational missing energy. The main threshold rows satisfy the stated decimal boxes. All4 legacy full-energy ratios exceed1. The two exact elementary energy examples pass.

The frozen current first and second stages use compatible cos2_full and dist_rel scalar fields. The earlier source-code objection in PROOF.md was caught by the independent audit and withdrawn in ADDENDUM.md before acceptance. All3 old B outputs name old projection files, and their saved cos2 values match those old files. They do not describe the version2 projections. New B outputs are outside this snapshot and need their own checks.

No Gram matrix, quadrature error, physical projection, image, tail, graph-norm estimate, inverse, or IPM endpoint is certified. The current code clips negative residual energy to zero for display; our arithmetic checks require strictly positive unmodified energy differences and do not rely on that clipping.
