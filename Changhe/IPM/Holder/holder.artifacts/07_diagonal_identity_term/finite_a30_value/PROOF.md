# Certified projection lower bound at alpha = 3/10

For the real homogeneous Euclidean Holder seminorm and the quotient-space operator R_1^2 defined in ../../01_setup/PROOF.md,

    D_(3/10) >= 2.7212438248.

Take the finite projection witness of ../finite_projection_witness/PROOF.md with a=3/2 and rho=3/14. The extended admissibility theorem ../finite_projection_extended/PROOF.md applies because rho=a/7<1 and alpha=3/10<=1/2. Its sufficient seminorm is at most K_(3/10)<=1.026981110219 by ../positive_profile_bound/PROOF.md and its certificate.

Use delta=3/56 and R=4096. The analytic local and tail formulas remain those of the finite witness. The nonsingular quadrant integral is enclosed with three logarithmic radial patches, 1024 radial and 1024 angular cells on each. The code certify_finite_projection_extended.py is the original certified integrator with only the admissible parameter range, rho, delta and normalizer label changed; the original hashed file is preserved. The interval for the regular integral is [1.559895518757313... +/- 0.0587].

Add the local leading term, subtract the local loss and tail bound, and add 1/2 for the identity term. Division by the positive K upper bound gives the stated downward-rounded decimal. The combiner checks exact coverage of all3072 rows and all source hashes. The independent code/check_finite_D_a30.py recomputes the endpoint terms with 90-decimal arithmetic and checks a separate 480-by-600 Gaussian integral against the regular enclosure. Its adverse-endpoint recomputation is above 2.72124383918, hence above the displayed certified lower bound.

Finally the compact smooth approximation theorem from the setup preserves the fixed increment, so the inequality also holds for the requested smooth compact-test supremum. This value improves the previously certified D lower bound at this exponent. It does not prove strict separation from C, whose present upper bound is larger.
