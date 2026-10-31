# Independent segment-two reduced sensitivity

The saved complete-J_c factors of all four segment-two endpoints reproduce the lead's finite-cutoff calculations. The independent route uses SciPy gesvd and a rectangular Householder complement to the scaled phase generator. The lead uses NumPy SVD and a square projected coefficient block. No production or lead numerical function is imported. The preceding proof is in ../PROOF.md and the comparison plan is SEGMENT2_V5_plan.md.

There are 574 passing audit controls after 58 qualifying controls. The four-factor audit took 75.515780 seconds of actual wall time on CPU35, ending 2026-10-29T16:56:03.436764Z. Factors were read at their frozen producer paths and hashed before and after; their large arrays were not duplicated. Lead JSONs, source and input hashes are captured in artifacts/segment2_sensitivity_v1/captures. The largest compared relative discrepancy is 7.762e-11, in the P1 FREE reduced gradient. All finite-cutoff eta values and audited band shares agree to numerical precision. This is agreement of finite-dimensional computations from saved factors, not a reconstruction of the full physical Jacobian.

| State | sigma_max | eta(1e-8) | eta(1e-6) | scaled full gradient infinity norm / ||r|| | predicted decrease / O1 |
|---|---:|---:|---:|---:|---:|
| P1 FREE | 24.79938726 | 0.84933041 | 0.66514562 | 0.04068556 | 0.14040687 |
| P1 FIXED | 24.58385988 | 0.83353348 | 0.66878691 | 0.02407078 | 0.12960407 |
| P2 FREE | 23.54127096 | 0.61418323 | 0.32397762 | 0.03628460 | 0.05586146 |
| P2 FIXED | 24.00943785 | 0.61818728 | 0.36849767 | 0.03746935 | 0.05687787 |

The reduced systems use the declared coefficient cutoff 1e-12. Their coefficient ranks are 1457, 1457, 1458 and 1457. The two unit-scaled parameter columns have cosine 0.999997620 and 0.999681784 at the FREE endpoints. After eliminating the permitted coefficient image, the remaining column fractions are about 5e-6 for c_l and 2.3e-4 to 2.7e-4 for omega. The exact values, both gradients, condition numbers, eigenpairs in three coordinate conventions, correlations and physical linear steps are in the JSON and CSV.

All four states fail specification7.4(b) and (d) by large margins: eta(1e-8) is above 0.61 against 0.001, the reduced predicted decrease is above 0.055 against 0.0001, and scaled parameter gradients exceed 0.002 against 0.0001. This audit does not alone establish the progress, parameter-oscillation or restart conditions. In particular, the detailed label "incomplete" additionally depends on the separate progress record.

The P1 FREE residual shares are 0.02105780 above 1e-4 sigma_max, 0.18355581 between 1e-4 and 1e-5, 0.46053201 between 1e-5 and 1e-6, and 0.18418479 between 1e-6 and 1e-8. The remaining share inside the stored Q space is 0.00185279. The share outside that space is 0.14881680. The finite bands 1e-5 to 1e-6 and 1e-6 to 1e-8 have computed undamped step norms 4.345915 and 45.747726 in scaled coordinates. This supports the stated distribution of reducible residual; it does not establish nonlinear descent over those steps.

Several prose qualifications are necessary:

- The largest singular value is not 24.8 in every case; the table gives the four different values.
- The quantity 1-||Q^T r||^2/||r||^2 is the share outside the stored Q space. If the Jacobian is rank deficient, the full share outside its exact range also includes components along zero singular values inside Q. Tiny positive floating singular values do not establish exact rank. Threshold-zero eta is reported only as the saved-factor arithmetic.
- The cutoff does affect numerical values: moving the coefficient cutoff from 1e-12 to 1e-8 changes the predicted decrease by 3.03, 5.94, 7.42 and 6.73 percent in the listed order. The P2 FREE and FIXED omega steps decrease by 8.28 and 12.39 percent. The stationarity conclusions above are unchanged; the numbers are not cutoff-invariant.
- The unconstrained P1 linear steps increase c_l by 0.06271431 and 0.06884450. Added to the respective base parameters they exceed 0.5. They are linear-model quantities, not admissible physical parameter updates or limit predictions. Differences between their sizes and past accepted moves do not, by themselves, locate the model's nonlinear validity range.
- The near-zero-band step has no demonstrated numerical accuracy. The first qualification attempt included an overly broad assertion of linear matrix-substitution accuracy for that band in a rank-deficient toy; it failed and is retained. The corrected qualification applies the preceding plan's finite-band restriction without changing the scientific implementation. Dense least squares at the finite cutoff and the rank-deficient reduced-system tests pass.

The line-search mechanism, effects of lagging the closure on actual accepted steps, and nonlinear profile widths remain separate questions. No Euler solution, parameter identification or basis-resolution floor follows from this audit.
