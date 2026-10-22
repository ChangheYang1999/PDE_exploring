# Positive sums and the remaining underflow condition

Written before its checker. The binary64 scalar hypotheses are exactly
those in MULTIPLICATION_LEMMA.md: round to nearest, gradual underflow,
finite inputs and no overflow. Put u=2^-53 and eta=2^-1074. A positive
sum is evaluated by a tree containing each term once; no BLAS behavior
is inferred. The source-level tree assumption must still be checked for
an application that invokes an undocumented library kernel.

For binary64 inputs, addition has no absolute underflow error: if its
exact result is subnormal, that result is an integer multiple of eta and
is exactly representable. Multiplication can have error eta/2. A positive
sum of n leaves has path length at most n-1. For 1<=n<=4096 put
A_n=succ(RN(1+(n+2)u)). Direct binary64 spacing gives

 1+(n+2)u <= A_n <= 1+(n+5)u.

Bernoulli and elementary rational arithmetic give

 A_n(1-u)^(n+1) >= [1+(n+2)u][1-(n+1)u] >= 1,
 A_n n/(1-(n-1)u) < n+1.                                  (1)

These inequalities can also be checked exactly for every allowed n.

Consider z_i=M_i H_i W_i with M_i>=0 and 0<=H_i,W_i<=1, all binary64.
If the source evaluates v_i=RN(RN(M_i H_i)W_i), expanding the two
multiplications gives v_i >= (1-u)^2 z_i-eta. Subsequent sum factors
amplify each absolute error by at most1/(1-(n-1)u). Thus, for the computed
sum shat, (1) gives

 A_n shat >= sum_i z_i-(n+1)eta.

An outward product by A_n and an outward addition of (n+2)eta therefore
bound the exact positive sum. This proves BiTM.sup_crude, after adding
its already bounded remainder outward. Its n equals117 here.

For BiTM truncation the order is different: w_i=RN(H_i W_i), then
v_i=RN(M_i w_i). It is sufficient that each nonzero exact H_i W_i is
normal, so the first multiplication has only relative error. There is
then just one absolute eta/2 error per leaf, which the preceding more
conservative allowance covers. The actual finite power tables must be
checked against this normal-product condition. Setting kept entries to
zero only decreases the nonnegative sum. Its full table size is425.
Together with the full coefficient lemma, the resulting truncation
bound encloses every discarded monomial on the stated rectangle.

All later BiTM remainder operations are successors of nonnegative
products and sums, so their exact Leibniz bound follows, including
underflow. If P+e and Q+d are the input models, it is

 |P d|+|Q e|+|e d|+discarded polynomial bound.

Consequently the whole BiTM product is valid under the stated scalar
hypotheses, finite checked weight conditions, and valid input models.
It does not validate the input models or Bernstein matrix kernels.

The r1 modal remainder sum has another useful special case. It multiplies
nonnegative binary64 radii by exact positive integers (2N+1)^j, j<=4.
If such a product is subnormal, it is exactly representable. Hence there
is no absolute multiplication underflow error. With n=523 terms, each
leaf has at most n rounded operations. Its factor
succ(RN(1+(n+1)u)) suffices since

 [1+(n+1)u](1-u)^n >= [1+(n+1)u](1-nu) >=1.

The actual native integer powers must be verified exactly, rather than
assuming an accuracy specification for an arbitrary power routine.

In contrast, the r2 sum uses arbitrary nonnegative products, with no
additive allowance. As an all-input theorem this is false. Take n=523,
each first factor eta and each second factor1/2. Every product is the
exact tie eta/2 and rounds to zero. The sum and inflated sum are zero;
the one final successor returns eta. The true sum is523eta/2>eta.
This is a counterexample to a generic rounding assertion, not to the
actual forcing data. The actual r2 sums need either finite independent
checks or a proved input condition making the surplus inflation absorb
underflow. None of the saved forcing rows contains these per-mode inputs.
A safe generic alternative is an explicit outward additive underflow
allowance. No producer file is changed by this audit.
