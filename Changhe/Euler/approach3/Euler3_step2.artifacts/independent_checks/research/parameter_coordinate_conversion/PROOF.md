# Converting a residual Jacobian between parameter coordinates

Status: proved conditional finite-dimensional identity. Floating-point implementation checks are separate.

## Statement, hypotheses and notation

Let n and m be positive integers. Put

    O = R^n x (0.4,0.5) x (0,infinity).

Let F:O -> R^m be continuously differentiable. Its first n inputs are the reduced coefficients, including any parameter-dependent expansion into full coefficients in the definition of F. The same F is used in both coordinate systems, including the same discretization, layout, active set and every quantity held fixed, such as a frozen closure target or weight. A coordinate change does not authorize changing any of these choices. Define Phi:R^(n+2) -> O by

    Phi(a,z_c,z_w) = (a,0.4+0.1 sigmoid(z_c),exp(z_w)),
    sigmoid(t) = 1/(1+exp(-t)).

At z=(a,z_c,z_w), put c=0.4+0.1 sigmoid(z_c), w=exp(z_w) and

    d_c = 0.1 sigmoid(z_c)(1-sigmoid(z_c)),
    d_w = exp(z_w).

Both constants are strictly positive. If J_z = D(F composed with Phi)(z), then J_x=DF(Phi(z)) is obtained by leaving the coefficient columns of J_z unchanged, dividing its c column by d_c, and dividing its w column by d_w.

## Proof

The coefficient components of Phi are the identity. Its c component depends only on z_c and has derivative d_c; its w component depends only on z_w and has derivative d_w. Thus DPhi(z) is the diagonal matrix diag(I_n,d_c,d_w). The chain rule gives J_z=J_x DPhi(z). Strict positivity makes this matrix invertible. Right multiplication by diag(I_n,1/d_c,1/d_w) proves each stated column formula.

## Dependencies and scope

The proof uses the ordinary chain rule and the elementary derivatives of the exponential and sigmoid. It assumes differentiability of F at a fixed discretization and fixed active set. It does not establish that assumption for the sampled numerical residual.

The verifier uses this identity to compare the unchanged production worker's optimizer-coordinate Jacobian with physical-coordinate finite differences. The worker is called in its native coordinates with its actual parameter map. Its two parameter columns are then divided by the recorded chain factors. Its coefficient columns are tested in native optimizer coordinates. No full-coefficient derivative is substituted.

In floating arithmetic, the map to optimizer coordinates and back need not return the exact input. The numerical wrapper records that discrepancy and stops if its maximum component error, divided by max(1,absolute input component), exceeds 1e-14. This is a separately declared consistency check, not an error bound for the mathematical identity or a replacement for the registered finite-difference gates.

For the reviewed worker, the completion map has the form H(B)=B+C+E: C is the target correction, independent of the input matrix B, and E adds a pattern correction only to the two parameter columns. Hence column j of H(B) depends only on column j of B. Replacing other input columns by zero leaves selected output columns unchanged. This source-specific fact permits the selected-column experiment; it does not hold for an arbitrary helper that mixes columns. The first reviewed worker hash and its correction implementation are recorded in verification/COLUMN_SEPARABILITY_v1.json. The gpu_v1p1 worker is bound separately in verification/COLUMN_SEPARABILITY_v2.json: its helper text and AST are identical to the first reviewed helper, and the complete Problem source is unchanged. This extends the same conditional column-separability argument to that exact source. It supplies no numerical derivative result by itself.

A comparison obtained by dividing a native worker column by its chain factor and then multiplying it back is only a conversion consistency check. It is not independent evidence for that derivative. Separate physical and optimizer autodiff evaluations of J_cw do supply an independent chain-rule comparison.

No formalization or Lean/Lake build is attempted.
