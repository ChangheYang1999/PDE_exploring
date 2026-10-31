# Qualification plan before implementation

Implement a separate Cartesian long-double spatial evaluator with radial derivatives through order three and exact-polynomial angular derivatives through order three. Preserve all already-qualified evaluators. Use the exact endpoint polynomial formula for far radial amplitudes. Reconstruct the stable linear velocity and its first derivative with the true third radial derivative; a second-order radial jet with an invented zero third derivative is insufficient for that first derivative.

Test third-order angular entries against exact rational polynomials at the origin, axes and ordinary points. Test the velocity, supplied first and second derivatives against 70-digit independent differentiation of the existing scalar field definition on manufactured and saved inputs, including the origin and a far point. Require relative norm error <=2e-13 for each nonzero U, DU, D2U, Omega and DOmega; at an identically zero quantity use the maximum norm over that quantity's full tested point set as the scale. This scale must be recorded.

Test curl(LU) against the direct 70-digit identity. At far points use the same 2e-6 nonlinear scaling as the prior stable-linear qualification, with |U|^2/r^2 for a curl quantity. At ordinary points use relative error <=2e-13. Record source versions and every failure. Test symmetry of D2U and the divergence and its gradient. These are implementation qualifications, not a uniform error estimate.

Only after this passes, use the pressure-independent residual at fresh origin, near-axis, centered-core and far points. No Tier verdict follows from the evaluator qualification or the partial diagnostic.

Implementation detail registered 2026-10-29T00:42:58.280348+00:00, before execution: use two complex steps (1e-20 times max(R0,r), and half that) in70-digit arithmetic to differentiate the independent DU formula; require Hessian-reference agreement1e-30 relative. Test field radii0,0.7,256,65536 R0. Angular third derivatives through degree18 use the prior2e-16 degree-maximum tolerance.
