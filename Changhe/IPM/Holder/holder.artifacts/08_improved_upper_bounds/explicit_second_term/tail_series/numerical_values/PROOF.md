# Directed evaluations with the exact exterior series

## Statement

Use the scalar homogeneous Holder spaces, operator conventions and complete finite and uniform inequalities of ../PROOF.md. Numerical acceptance requires the independent analytic acceptance beside that proof. The previous fixed-radius upper bounds are those of the accepted V209 sharp-deficiency certificate. Its exact rational radii, exponents and reflection choices are retained.

For each finite row replace the old exterior coefficient by

    2^(alpha+1) alpha S_64^+(alpha)/pi.

For each uniform row on 0<alpha<=epsilon=1/100, replace it by

    2^(epsilon+1) S_64^+(epsilon)/pi.

Here S_64^+ is the explicit rational upper bound in the parent theorem. The exact sharp constant terms and all other error terms are unchanged. The optional local reflection is the already accepted quadratic and quartic saving, counted once. Every resulting decimal is an upper bound after the directed computation described below succeeds. This file itself asserts no new decimal.

## Verification

The program code/certify_exact_tail_values.py verifies the V209 certificate, every registered dependency hash, and the new analytic acceptance. It evaluates the same finite rational sum in forward and reversed order with exact Fraction arithmetic. It independently checks the factor monotonicity used in the tail majorant and positivity of the reduction from the old coefficient. The 64-term remainder is retained as an upper bound and is never dropped.

The full original finite or uniform formula is recomputed at 384 bits using the exact rational Catalan enclosure already accepted by V209. Its new tail is evaluated from the exact rational S_64^+. A second evaluation at 768 bits uses the independently grouped original formula and the library Catalan interval, with the same exact rational upper tail. The narrower result must lie inside the first interval. The resulting upper endpoint is rounded upward to ten decimal places by exact rational arithmetic and compared with the prior accepted bound. All source hashes, exact rational tail bounds and evaluation intervals are recorded.

Only the explicitly selected radii are certified. No assertion of radius optimality or of sharpness of the exterior transport plan is made. The certificate proves whole-interval envelopes only for its rows expressly labeled uniform; finite rows remain pointwise in the exponent.
