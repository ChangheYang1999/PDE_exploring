# Exact classification of a finite paired-exponent cutoff

## Statement

Let I be a finite nonempty index set. For each i in I let h_i and l_i be finite real numbers. Their sum is an exact real sum, not a floating-point addition. Let t be a real implemented threshold and let theta be a mathematical threshold with theta in [theta_lo,theta_hi]. Define

    E = max(|t-theta_lo|, |t-theta_hi|),
    B = max_i |l_i|,
    d = min_i |h_i-t|.

If d > B+E, then for every i,

    h_i < t  if and only if  h_i+l_i < theta.

All inequalities are strict. In particular there is no equality ambiguity under the hypothesis. If theta = log(epsilon), epsilon>0, the right side is equivalent to exp(h_i+l_i)<epsilon by strict monotonicity of the real exponential. This statement concerns the predicate selecting contributions; it does not bound their eventual effect on a residual.

## Proof

For every i, the interval hypothesis gives |theta-t|<=E, so

    |l_i-(theta-t)| <= B+E < |h_i-t|.

If h_i-t>0, adding l_i-(theta-t) cannot change its positive sign. The same inequality preserves a negative sign when h_i-t<0. Equality h_i=t is excluded by d>0. Thus h_i+l_i-theta has the same sign as h_i-t. This proves the equivalence. The exponential statement follows from exp being strictly increasing and exp(log(epsilon))=epsilon.

## A rational enclosure for the threshold used here

Set z=9/11. For an integer N>=1 define the rational numbers

    L_N = 2 sum_(k=0)^(N-1) z^(2k+1)/(2k+1),
    R_N = 2 z^(2N+1)/((2N+1)(1-z^2)).

Then L_N < log(10) < L_N+R_N. To prove this, integrate the finite geometric identity

    1/(1-s^2) = sum_(k=0)^(N-1) s^(2k) + s^(2N)/(1-s^2)

from 0 to z and multiply by 2. The integral on the left is log((1+z)/(1-z))=log(10). The last integrand is positive; since s<z on the integration interval, replacing its denominator by 1-z^2 gives the strict upper bound R_N. Consequently

    -250(L_N+R_N) < log(10^(-250)) < -250 L_N.

Every endpoint and E can be represented exactly as a rational number. No floating evaluation of log or exp is needed for this enclosure.

## Computing d from stored floating-point high words

Partition I into h_i<t and h_i>=t. Let h_minus be the largest high word in the first set when nonempty, and h_plus the smallest in the second set when nonempty. Then d is the minimum of the existing distances t-h_minus and h_plus-t. Binary64 comparison and min/max select actual stored high words without arithmetic approximation. Convert the selected high words and t to exact rational numbers before subtracting. The same applies to B: absolute value and maximum select a stored magnitude exactly for finite inputs. A program must check finiteness and the full intended index set.

## Dependencies and scope

This is an informal real and rational arithmetic proof using finite extrema, the triangle inequality, the finite geometric identity, integration and strict monotonicity of exp. The finite scan supplies the hypotheses; it is not part of this proof. In the Euler application the scan must include every active K1/K2 argument, every auxiliary exponential factor, every registered stencil point, and the exact source and geometry used by the qualifier. It must preserve the paired words rather than substitute a recomputed real formula. Equality of argument construction and subsequent record bindings are separate obligations. No continuum pressure error, derivative accuracy, or exact Euler solution follows.
