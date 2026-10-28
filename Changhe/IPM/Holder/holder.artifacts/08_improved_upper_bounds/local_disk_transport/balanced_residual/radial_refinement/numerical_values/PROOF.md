# Outward radial residual evaluations

## Statement and status

Fix the real homogeneous Holder seminorm and the two circular principal-value trace-free transforms in ../PROOF.md. Subject to the complete acceptance checks in ../verification/accepted.json with verdict CONFIRMED, the following numerical upper bounds hold for their common norm C_a. The analytic cross-read is frozen in05_team_audit/lead_note33 and accepted as V159.

| a | Upper bound |
| --- | --- |
| 1/1000 | 637.0404730920 |
| 1/100 | 64.0882485032 |
| 1/20 | 13.1842538716 |
| 1/10 | 6.8518145023 |
| 1/5 | 3.7439473709 |
| 3/10 | 2.7740910337 |
| 1/2 | 2.1956570947 |
| 3/4 | 2.6421664049 |
| 9/10 | 5.0112069529 |
| 99/100 | 42.2225497071 |

## Derivation and exact data

Start from the complete transport certificates accepted as V152 in ../../existing_certificates/verification/accepted.json. For each of256 radial rows and17 phases use the exact signed integer masses, unit2^44, exact rational radial endpoints and outward angular variation already retained there. Split each row into8 equal rational subintervals. Evaluate equation(1) of ../PROOF.md at256-bit ball precision. Select the smaller of this upper residual and the accepted aggregate residual for each row.

Sum the new residuals exactly as rational upper endpoints. Subtract from each previous phase total its separately retained old residual upper endpoint, which was the exact summand used to construct that total, and add the new residual upper endpoint. This subtraction is an algebraic replacement of a known summand, not subtraction of an uncertain bound on the true functional. Add the unchanged uniform small-disk bound after multiplying the maximum regular phase cost by sec(pi/64). Round the upper endpoint upward to10 decimal places.

The executable is code/refine_balanced_circle_radial.py. The full retained record is ../verification/independent_audit.json, with row-level selected residuals, phase totals, input hashes and precision. The run completed at2026-10-28T10:55:28.372729+00:00. All256x17 row-phase pairs were processed. Every total weakly improves its V152 predecessor.

The1/1000 value remains weaker than the separately proved small-exponent bound. No diagonal D_a upper bound changes. The analytic theorem is valid for any finite rational row subdivision; the eight subdivisions used here need no optimization hypothesis.
