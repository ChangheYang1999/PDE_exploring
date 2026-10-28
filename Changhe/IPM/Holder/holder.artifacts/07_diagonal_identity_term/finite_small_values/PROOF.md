# Strict separation at three small positive exponents

Use the real homogeneous Euclidean Hölder seminorm on R^2, the quotient-space singular integrals, and the smooth compact-test suprema defined in `../../01_setup/PROOF.md`. Let C_alpha be the common norm of T_xx and T_xy and D_alpha the norm of R_1^2. Then

| alpha | C_alpha upper | D_alpha lower | D_alpha - C_alpha lower |
|---|---:|---:|---:|
| 1/1000 | 637.0652723887 | 637.3340501785 | 0.2687777898 |
| 1/100 | 64.1129530993 | 64.3702681064 | 0.2573150071 |
| 1/20 | 13.2090680608 | 13.4165946841 | 0.2075266233 |

These are inequalities, not exact norms. The upper bounds are the V045 exterior-circle construction. The lower bounds use the witness and complete integral estimates of `../finite_projection_witness/PROOF.md`, with a=1, rho=1/6, delta=1/24 and R=4096. This is the same construction and the same three-patch 1024-by-1024 Arb160 regular-integral enclosure as `../finite_certified_values/PROOF.md`.

The sufficient seminorm constants are bounded by 1.000000240308, 1.000024085602 and 1.000608619784, respectively. They follow from `../refined_profile_constant/PROOF.md` and the cancellation-free auxiliary inequality in `../positive_profile_bound/PROOF.md`. The latter inequality follows from the midpoint Taylor remainder for t^k on [R,1], where k=1/(1-alpha). The 32768-cell Arb192 enclosure covers the interval between 10^-6 and 1-10^-6, with the previously proved analytic estimates on both omitted endpoints.

For each exponent the regular enclosure is added to the explicit local leading term, both analytic error terms are subtracted, and the identity contribution 1/2 is added. Dividing by the certified positive seminorm upper bound gives the reported lower endpoint, rounded downward to ten decimal places. Every row, common parameter and source hash is checked by `code/combine_finite_projection.py`. The full data are `data/finite_D_lower_a001.json`, `data/finite_D_lower_a01.json` and `data/finite_D_lower_a05.json` relative to the artifacts root.

The independent script `code/check_finite_small_D.py` recomputes the endpoint terms at 90 decimal digits, converts the adverse Arb regular endpoint to an exact rational, and verifies each displayed decimal against the resulting value. An independent 480-by-600 Gaussian quadrature lies in each regular enclosure. This floating comparison checks implementation consistency; the proof uses the interval enclosures and analytic bounds.

The fixed increments converge along the compact smooth approximations from the setup theorem. Thus the same lower bounds hold for the test-function suprema. Exact decimal subtraction proves the final column.
