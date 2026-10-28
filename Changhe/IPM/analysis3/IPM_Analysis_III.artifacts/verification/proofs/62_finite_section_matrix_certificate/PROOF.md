# Independent matrix certificate for the exported S0 section

## Scope and exact conditional claim

Fix the archived S0 export: 169 ordinary columns and one TAU column,
12 output modes, 69 scalar test splines, and the exact metadata saved
beside this proof. The first and last test splines are inactive and are
removed algebraically. Suppose the exported intervals enclose the
stated exact trial-column Gram entries and operator pairings.

This proof and calculation verify a lower bound for the finite projected
operator from those intervals. They do not independently certify every
exported entry against the original density. That remaining input
hypothesis is explicit. Neither this result nor its input hypothesis
would provide a complement inverse: the S0 realization has the already
proved infinite-dimensional obstruction of proof 36.

## Reconstructing the finite problem

Let G_rem be the exported ordinary-column Gram, multiplied on each
angular block by 1+(2m)^2. The J row is a scalar coordinate of weight1;
the TAU coordinate also has weight1. From the exact metadata k and
strain enclosures form

    D=3/k+k c_KP,
    d_j=-k c_j/D, including c_TAU for the last column.

The domain Gram is

    G=diag(G_rem with the J entry1,1_TAU)+d d^T.             (1)

Its mathematical definition uses correlated exact strains. Interval
arithmetic enlarges the set by allowing independent occurrences; this
is conservative. The denominator must exclude zero.

For each output mode N, append TAU's pairing vector to the ordinary
pairings and add the compensation d_j times the KP pairing vector.
Call the resulting matrix B_N. Let H be the common test Gram and
w_N=1+(2N+1)^2. Pairings already include this angular weight. The
squared projected norm is therefore

    sum_N x^T B_N^T H^(-1) B_N x / w_N.                    (2)

The inactive tests are set to zero in every B_N and decoupled in H,
with their diagonal entries replaced by1. This is exactly equivalent
to deleting those rows and columns from the true test space.

## Independent whitening and interval inversion

Using the exact dyadic midpoints, compute approximate Cholesky factors
of G and H in high-precision arithmetic. Choose the dyadic midpoints
of their inverse-transpose entries as exact real matrices T and S.
Both are triangular and have nonzero diagonal, hence are invertible.
They need not be exact Cholesky inverses.

All subsequent operations use ball arithmetic. Set

    G_1=T^T G T, H_1=S^T H S, C_N=S^T B_N T.

The checks ||G_1-I||_infinity<1 and ||H_1-I||_infinity<1 prove both
underlying symmetric Grams positive definite. Invert the well-scaled
H_1 in ball arithmetic and form

    K_1=sum_N C_N^T H_1^(-1) C_N / w_N.                    (3)

This differs from the numerics team's approximate-inverse lower matrix:
here the transformed test Gram is directly inverted with a certified
interval result. Equation (3) is exactly the congruence of (2).

For a positive dyadic s, let M=K_1-s^2 G_1. Pick an ordinary floating
Cholesky factor L of its midpoint as an exact dyadic matrix. The final
ball computation is

    E=L^(-1) M L^(-T)-I.

If ||E||_infinity<1, every exact symmetric M enclosed is positive
definite: its spectral perturbation is bounded by that norm. This
proves the projected singular value is at least s. Floating arithmetic
only chooses T,S,L and s; every accepting inequality is verified using
exact dyadic choices and outward ball arithmetic.

## Input and output checks

The code snapshots metadata, matrix export and the reported certificate,
records their digests, and independently decodes each four-integer ball
as midpoint m*2^e plus radius r*2^er. It performs no import of the
numerics team's certification code. The source-file hash is checked
against the original-data identity in the metadata when available.
A report stores the exact rational s, every accepting norm and the
status of each positive-definiteness test. Failure of any test leaves
this certificate open. Successful matrix tests remain conditional on
the exported entry enclosures stated at the beginning.

Arithmetic correctness of Python integers, mpmath's approximate choices
and Arb's interval operations is a computational dependency; the
approximate choices themselves are validated by the final interval
tests. No sampled singular value is used as a proof.
