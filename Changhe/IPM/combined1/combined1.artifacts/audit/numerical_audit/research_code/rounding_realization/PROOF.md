# Exact candidate versus its binary64 coefficient realization

## Statement and notation

Let a finite potential be written as chi=sum_i a_i g_i, with exact rational coefficients a_i and real smooth generators g_i. Fix its exact exponent c. Define the recorded binary64 realization by replacing a_i with the exact rational value b_i of the stored binary64 coefficient field, leaving the mathematical generator and c unchanged. This is a different exact function chi_b; it is used only to isolate the effect of coefficient conversion. Neither floating point field evaluation errors nor quadrature errors enter this comparison.

For each point X and multiindex alpha,

    partial^alpha(chi_b-chi_a)(X)=sum_i (b_i-a_i) partial^alpha g_i(X).       (1)

The density rho=-partial_y Delta chi and velocity u=(-chi_xyy,chi_xxy) are linear in chi, so their differences obey the corresponding formulas. The residual F=(cX+u).grad rho-rho is quadratic in the coefficients. With e=rho_b-rho_a and v=u_b-u_a,

    F_b-F_a=(cX+u_a).grad e+v.grad rho_a+v.grad e-e.                       (2)

Both identities are exact, by linearity and multiplication. In particular, exact cancellations in a far-field moment are not implied by small coefficient errors. A rounded realization can have a nonzero forbidden sector even when the exact published candidate has every required sector zero.

## Origin, far field and function-space consequences

For the single-scale mono/leg family, the exact canonical conversion and sector formulas in ../candidate_audits/PROOF.md apply to both coefficient vectors. Compare the exact center strain, leading potential moments and residual sectors. The first nonzero residual term r^alpha A(theta), with nonzero finite trigonometric polynomial A, is not in L2 at infinity if alpha>=-1, provided it is the leading term of a convergent asymptotic expansion. This is the polar integral of r^(2alpha+1). The finite single-scale family has the required convergent expansion for r>1, and the strictly lower powers cannot cancel its nonzero leading angular coefficient.

This statement is about the rounded realization. It never changes the mathematical status of the exact input candidate. A finite-box diagnostic of the rounded realization is also not, merely from this fact, inaccurate on its finite box. Its pointwise discrepancy must be measured separately.

## Independent point comparison and conditioning

All b_i are imported as exact numerator/denominator pairs from binary64, rather than decimal strings with an unspecified rounding rule. The Cartesian Taylor evaluator in ../multiscale_generators/PROOF.md encloses the fields of both exact functions at rational points. Taking their interval difference encloses the pointwise conversion error. If cancellation makes this enclosure wide, increase arithmetic precision before drawing a conclusion. No cancellation is enforced by a numerical tolerance.

A componentwise condition estimate for a nonzero scalar linear functional L is sum_i |a_i L(g_i)|/|L(chi_a)|. This can diagnose cancellation at a point or in a moment, but it is not itself an error bound for a nonlinear residual or a global norm. The present audit reports exact conversion identities and direct point discrepancies; it does not infer a rigorous whole-plane norm discrepancy from a finite sample.

## Scope and evidence

The code records both input and output hashes, all exact constraint comparisons, the leading rounded residual sector, and the exact points tested. This tests the recorded coefficient realization only. It does not assert that every optimizer or diagnostic actually used that field; such a claim requires checking its loader. The immutable snapshot remains the exact rational candidate.
