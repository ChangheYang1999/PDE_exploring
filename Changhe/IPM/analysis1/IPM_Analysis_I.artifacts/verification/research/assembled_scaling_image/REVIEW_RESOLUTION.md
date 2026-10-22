# Response to the preparation review

UTC 2026-10-21T21:06:07.881705+00:00. This mandatory supplement narrows and specifies the implementation statement. The first preparation review returned OBJECTIONS before seeing frozen input metadata or computation code. No result was accepted by that review.

1. The saved Z exists: evidence/source/KC_assembled_image_all260.npz, with its exact hash in frozen_inputs.json. That artifact was inspected and frozen before computation. Its img_assembled is Z and img_direct is D. The code also compares D against img_K in the explicitly frozen KprojB2_M16_s16_NJ1_img.npz. The source c2_Kproj.py does not write this extra archive, so no claim is made that its merge function produced Z. All results are explicitly pairings of these saved arrays. Numerical agreement with JSON is a bounded discrepancy, not historical producer identity.

2. No floating accumulation order is assumed. S is the exact rational sum; Z is a separate fixed binary64 array. The audit quantifies Z-S. It does not infer an accumulation error bound or exact PDE error from that discrepancy.

3. The 42 piece labels and Mout are read from their own arrays, then checked for nonempty integer ranges and contiguous complete coverage. Nodes, weights and D are independently read by NumPy/Fraction and a manual ZIP/NPY/IEEE/fmpq decoder. In addition to exact-value agreement, a supplemental check requires matching raw IEEE payload bytes of t and w in all 42 pieces and the two complete archives, and matching direct-image bytes between the archives. Source NaN and infinity are rejected; subnormals and signed zero have their usual exact-real meanings. Positive weights and positive differences are tested explicitly before any norm or ratio.

4. All 46 inputs were copied, hashed and compared to their sibling originals before computation. The frozen input list is immutable once acceptance occurs.

5. The two exact paths use different libraries and encodings: Fraction.from_float on NumPy values, and explicit sign/exponent/mantissa decoding to fmpq. All 784560 partial-image entries and each of 18680 exact sum entries are compared. The supplemental check also compares exact positive row coefficients in the two rational libraries. Both outward engines then evaluate the complete quadratic forms independently: Arb by node weights, iv by reverse-order edge trapezoids. This is already a valid enclosure proof; exact evaluation of the entire rational quadratic sum is not necessary. The reviewer's proposed requirement that both methods evaluate every Q exactly would be a different sufficient approach, not a mathematical gap in two complete outward evaluations of the finite sums. Each algorithm follows the proved finite rational expression and all rounding is outward. The independent comparison never promotes overlap alone into proof: validity rests on each outward construction.

6. Every max norm is computed exactly from dyadic arrays. The JSON fields use Z where compared, not S. Both discrepancy families are shown separately. Norm of the difference divided by reference norm is distinct from the relative difference of norm values.

7. The exact sum of the saved c entries is a literal-data diagnostic only, with no claim about the physical strain functional. There is no angular tail or continuous radial-domain estimate. Only 467 nodes and 40 stored columns are covered.

Manufactured formula checks and malformed parser/range examples will supplement the full data computation. These tests alone cannot prove the full finite computation.
