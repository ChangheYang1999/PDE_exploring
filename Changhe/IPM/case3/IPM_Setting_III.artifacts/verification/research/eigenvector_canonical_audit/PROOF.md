# Canonical directional derivative at stored spectral vectors

Written 2026-10-21 before implementation. This result checks finite evaluations of an explicitly encoded field and perturbation. It does not prove an eigenvalue of the continuum operator, time evolution, instability or a profile endpoint.

## Statement, data and notation

For C>1 define c[rho]=psi_xy(0), where -Delta psi=rho_x is the whole-plane parity-preserving sublinear-velocity inverse, U=(-psi_y,psi_x). Set w[rho]=-c[rho]/(C-1), x[rho]=C w[rho], and

F(rho)=w[rho] rho-(x[rho] X+U[rho]).grad rho.

The background B and direction h are explicitly encoded smooth Q fields, represented by local Chebyshev coefficients, stored basis nodes, compactification parameters and angular dimension. Complex h is evaluated as two real fields. Its defining coefficients are never inferred from plotted values. All stored numbers mean their exact binary values; an exact rational affine conversion changes representation without changing the field. A reported compressed eigenvalue lambda is a comparison parameter, not assumed to be a continuum eigenvalue.

## Exact directional formula

Both U and c are linear. For a real parameter z expand F(B+z h). The coefficient of z is exactly

DF(B)h = w[B] h-(x[B] X+U[B]).grad h-U[h].grad B
          -c[h]/(C-1)*(B-C X.grad B).

Indeed, the first product contributes w[B]h+w[h]B, and the transport product contributes -(x[B]X+U[B]).grad h-(x[h]X+U[h]).grad B. Substituting w[h]=-c[h]/(C-1) and x[h]=Cw[h] gives the displayed expression. The quadratic remainder cancels identically in a centered directional difference. Complex linear extension follows by evaluating the real and imaginary parts separately. This argument requires no stationarity assumption on B.

The residual E(X)=DF(B)h(X)-lambda h(X) is the pointwise residual of the actual canonical operator on this explicitly encoded direction. A small residual of a projected coefficient matrix is a different statement. If Jv is exported as a coefficient field, evaluate that field separately and compare it with DF(B)h at the same physical points. Their difference includes projection, inverse approximation and differentiation errors. It cannot be assigned to any one cause without additional evidence.

## Two independent evaluations

First compute density derivatives by scalar Clenshaw evaluation with complex-step radial differentiation and exact angular differentiation. Compute U/r by the independent composite interior Green integral and polynomial-exact exterior Jacobi integral in result176. The full interior tail is included. This evaluation uses neither a producer module nor a differentiation matrix. Repeat its quadrature order at selected points.

Second convert the local Chebyshev rows to global rows by exact rational affine composition. The verifier's separate multiprecision primitive inverse then evaluates density, analytic derivatives, c and U. Its interior primitives use hypergeometric recurrences or complementary power integrals and its exterior primitives are exact finite polynomial integrals. Thus it uses neither the composite quadrature nor the first evaluator's differentiation method. Perform this calculation at two working precisions with the previously documented degree-dependent guard. Precision comparison remains empirical, not an interval certificate.

Reconstruct the producer's exported background, perturbation and Jv from numeric-only files, preserving the stored basis-node array. For the verifier's own vectors, lift the retained coefficient vector using the exact saved finite SVD blocks, or read the saved full coefficient vector. Record hashes and any floating-point basis conversion. Compare selected original Cartesian points, the core radius of the largest sampled perturbation and finite-grid extrema. All maxima are over explicitly stated finite sets. A residual relative to |lambda| times a perturbation norm must also be compared with |Re lambda| times that norm before making any statement about the real growth-rate scale. Even a small residual alone would require operator and spectral control to prove a continuum eigenvalue.

## Dependencies and scope

Dependencies are the independently proved Q representation, exact local-basis conversion in result173, canonical inverse identities and finite-compression scope in results171 and176. The checkpoints and spectral vectors are data, not hypotheses that certify the PDE. Exact binary reconstruction verifies which fields are being evaluated. Neither inverse precision comparison nor numerical eigenvalues supply the decisive YES or NO in PROMPT.md.
