# Independent audit of the uniform finite-family bound

The proof and two numerical programs have been checked by the independent verifier. The lead independently rederived the power counts, monomial distance, dilation estimate, cylinder transfer and constants, and reported CORRECT at07:41Z. Its notes are in the read-only lead filework/audit_v106_notes.md. The per-generator origin-cancellation wording was clarified accordingly.

1. The displayed generator family is smooth at the origin because k>=m. Its stream function is canonical by parity and subquadratic growth.
2. The third/fourth derivative degree bounds76/77 give residual degree153 and w degree154. These bounds come from the derivative recurrence rather than a sampled fit.
3. Exactly eight compactified exponents precede7delta/2. The primary and descendant constraints cancel them. The exact rational exponent makes the finite powers distinct.
4. The first remaining coefficient comes only from the six stationary leading branches. The independent program recovers the original860 coefficients from the read-only state131 source, checks the leading branch, checks every lower stationary residual sector, and recomputes the complete first remaining angular vector. It agrees exactly with the independently computed A2 annular vector.
5. The Cauchy-Gram distance is derived by its rational Mellin transform. Exact rational Gram-Schmidt on three unrelated power sets agrees with its product formula.
6. Increasing-order Gram-Schmidt makes dilation triangular. Every matrix entry and the Frobenius sum were checked exactly on the same three unrelated sets.
7. The log-radius Poisson problem uses the true Dirichlet norm, pi times the cylinder energy. The inverse kernel is positive and bounded on L2 for every m>=1. Endpoint decay puts the present g in H1.
8. The change of variable to w=(1-u)u^-2 H has measure factor1/2. Differentiating sqrt(u(1-u))w gives the coefficient2u-1 and the term-2u(1-u)w'. This verifies both factors in the norm inequality.
9. Orthogonal sine energies add, so all70 leading modes can be combined. No unrepresented higher mode can reduce the energy.
10. Independent384-bit and512-bit computations agree. They use different rational representations and different summations for the dilation norm. The lower bounds Hminus>2.67750e-7, N_U>0.00013376 and ratio>210 are strict ball comparisons.
11. All five supplied exact candidates A2,A3,A4,A5,Mpen fit the support and affine constraints. Their source-specific coefficient magnitudes never enter the uniform bound.
12. The conclusion is a uniform failure of one sufficient unweighted residual threshold. It is not a weighted norm estimate, a theorem of nonexistence, or a claim about larger radial degree or additional stationary branches.

Evidence: muntz_bound.py/json/log and audit_algebra.py/json/log. Every imported source and proof hash is in the latter record.
