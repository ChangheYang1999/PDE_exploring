# Converting a residual Jacobian between parameter coordinates

Status: proved conditional finite-dimensional identity. Floating-point implementation checks are separate.

## Statement, hypotheses and notation

Let n and m be positive integers. Put

    O = R^n x (0.4,0.5) x (0,infinity).

Let F:O -> R^m be continuously differentiable. Its first n inputs are the reduced coefficients, including any parameter-dependent expansion into full coefficients in the definition of F. Define Phi:R^(n+2) -> O by

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

No formalization or Lean/Lake build is attempted.
