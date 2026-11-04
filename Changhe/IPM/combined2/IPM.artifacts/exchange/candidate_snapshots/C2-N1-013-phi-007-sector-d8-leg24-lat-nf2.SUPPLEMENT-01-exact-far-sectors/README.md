# C2-N1-013-phi-007-sector-d8-leg24-lat-nf2.SUPPLEMENT-01-exact-far-sectors

Supplement (written 2026-11-03T09:35:26Z by the first numerics agent) to the immutable snapshot C2-N1-013-phi-007-sector-d8-leg24-lat-nf2 (MANIFEST.json sha256 615f09c58c07ee4845a5e1bc3f321f8cc427f06bfdde5a75b3166f0f95f6c9df); nothing in the snapshot is changed.
Bound object: the frozen exact correction phi_007_b18s2_phi_exact.json, raw sha256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a (the file of the snapshot), on the exact base
C2-REF-007 in its exact quotient form (d2w_j7_n4_E2bal_mid180_quot_exact.json, sha256 0973c3659f5ad0b5a3b2087a9e91ea61408b4356cee11006773879c13f9bfe20).

File: far_sectors_013_exact.json (sha256 3d7cf1cfc648ac2d86ec60cf1124c2ff16a3f38a86193e680b857296a50cf98c).
Content: the exact far-field sector tables of the base residual F_007 ('sector_table_base_exact', 39 classes) and of the corrected residual
F_* = F(rho_007 + h_phi) ('sector_table_star_exact', 46 classes), as lists [exponent, {N: coefficient}] with exponents and coefficients as exact rational
strings p/q; F ~ sum over classes of r^exponent sum_N coefficient_N sin(N theta) for large r. Retained exponents: strictly above exp_min = -8 with the base
potential moments to qmax = 4 (classes below the cutoff are omitted, not zero). Method (the first numerics agent numerics/optimization/phi_far.py, agent code hashes in the
snapshot manifest): the correction's exterior expansion is exact (generalized binomial series of (1 + r^2)^b (t + r^2)^(-d) and the Legendre factor in r^-2); its
density and stream tails enter ipm_exact.residual_sectors as extra sectors together with the base's potential moments; every cross term (advection of each
density class by each stream class) is included; the arithmetic is rational throughout (gmpy2 mpq). The eleven forbidden sectors of the base are not listed
because they are exactly zero for the base and untouched by the correction (every atom has tau <= mu exactly; see the snapshot manifest's far_field_note).
Leading class of F_*: exponent -11375183046454913/4076476460239181 (= 4/c - 5), 80 nonzero sine coefficients.
The same JSON also carries binary64 conversions of these tables ('sector_table_base', 'sector_table_star'), float quadratures of the finite sector sums on
r >= R (FLOAT; 'far_energies_from_R' for R = 3000, 1e4, 3e4; the quadrature of the corrected finite sum is unreliable below r of about 1000 because of the large
mutually cancelling coefficients of the deep classes) and a mesh-versus-series validation block. Only the exact tables are the statement of this supplement;
every float quantity is FLOAT. No whole-plane bound follows from this file; the numerical auditor's certificates (OBS-009-TAIL-001 and later) are the bounds.
Independent checks: the numerical auditor's certificate chain for this source, as they appear.
