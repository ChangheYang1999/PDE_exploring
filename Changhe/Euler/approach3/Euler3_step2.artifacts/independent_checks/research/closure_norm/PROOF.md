# Derivative of the closure target norm

## Statement and hypotheses

Let O be an open subset of R^d, let q_1,...,q_m be fixed positive real numbers, and let G:O -> (R^3)^m be continuously differentiable. Define N(x) = (sum_i q_i |G_i(x)|^2)^(1/2). At any x with N(x)>0 and for any v in R^d,

DN(x)v = sum_i q_i G_i(x) . (DG_i(x)v) / N(x).

If s_i = sqrt(q_i/(4 pi)), the same formula uses q_i=4 pi s_i^2. In general replacing q_i by s_i computes the derivative of a different norm. There are no error constants in these exact finite-dimensional identities.

If C:O -> (R^3)^m is continuously differentiable and lambda is constant, the normalized closure residual r_i=lambda s_i (C_i-G_i)/N has directional derivative

Dr_i v = (lambda s_i/N)(DC_i v-DG_i v) - (lambda s_i/N^2)(C_i-G_i) DN v.

The terms contributed only by the target and its normalization are the terms containing DG and DN. If G is quadratic in one scalar input with all others fixed, its centered difference at any nonzero step whose endpoints lie in O equals that input derivative exactly in real arithmetic. This does not imply the same exactness for N.

## Proof

The finite weighted squared norm is continuously differentiable and its derivative is twice sum_i q_i G_i . DG_i v by the product rule. The square root is continuously differentiable at every positive argument; its chain rule gives the displayed derivative of N. Substitution of q_i=4 pi s_i^2 proves the weight conversion. The product rule applied to N^(-1)(C_i-G_i) proves the closure formula. Finally, if G(t)=A+Bt+Dt^2, subtraction gives G(t+h)-G(t-h)=2h(B+2Dt), so the centered difference equals G'(t). Taking a square root of its squared norm need not preserve polynomial degree and therefore gives no corresponding exactness for N.

## Dependencies and scope

Only the finite-dimensional chain and product rules are used. The statement requires fixed quadrature weights and a positive target norm. Parameter-dependent quadrature weights would add their derivatives. The campaign's sphere grid is fixed in this use. This proof establishes neither numerical differentiation accuracy nor correctness of a pressure source or a saved Euler state. No formal proof has been run.
