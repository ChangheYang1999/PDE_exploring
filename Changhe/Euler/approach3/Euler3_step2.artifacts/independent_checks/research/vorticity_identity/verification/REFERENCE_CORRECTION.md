# Angular reference correction

Recorded 2026-10-29T00:45:56.204549+00:00.

The v1 harness rounds the test points to binary64 inside AngularReference.values, while the evaluator retains long double. The normalized (1,2,3) direction therefore differs between the two sides; degrees8 through18 fail the unchanged2e-16 threshold. All eight full field checks pass, including independent70-digit complex-step Hessians. Preserve v1 as an invalid angular comparison, not a passed qualification.

The v2 harness differentiates the exact rational solid-harmonic polynomials directly, using70-digit Decimal arithmetic and the decimal spellings of the actual long-double coordinates. It does not use the normalized harmonic recurrence for the reference. The numerical tolerance, fields, points, and field tests are unchanged. v2 is registered before execution.
