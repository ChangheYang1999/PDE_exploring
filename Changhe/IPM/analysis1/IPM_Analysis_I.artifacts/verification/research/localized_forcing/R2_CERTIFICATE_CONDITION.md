# A sufficient finite condition for the angular r2 sum

Written before its checker. Assume binary64 round-to-nearest with gradual
underflow, no overflow and a positive addition tree containing each term
once. Put u=2^-53 and eta=2^-1074. Let 1<=n<=4096. The finite nonnegative
binary64 inputs are x_i,y_i. Let p_i=RN(x_i y_i), let shat be their
computed positive sum, and put A=succ(RN(1+(n+1)u)). Then

 shat >= (1-u)^(n-1) sum_i p_i
       >= (1-u)^n sum_i x_i y_i - n eta/2
       >= (1-nu) sum_i x_i y_i - n eta/2.                 (1)

The first inequality uses the path length at most n-1 and nonnegativity.
The second uses p_i >= (1-u)x_i y_i-eta/2 and discards the factor
(1-u)^(n-1)<=1 on the negative absolute error. Binary64 additions have no
absolute underflow term because their exact subnormal result is an
integer multiple of eta. Bernoulli gives the last inequality.

Successor rounding near1 gives A>=1+(n+1)u. Hence

 A(1-nu)-1 >= u[1-n(n+1)u].                              (2)

The allowed n satisfy n(n+1)u<1/2. If the ACTUAL computed sum satisfies

 shat >= n eta/u = n 2^-1021,                            (3)

then (2) implies [A(1-nu)-1]shat >= n eta/2. Rearranging
(1) shows A shat >= sum_i x_i y_i. Thus succ(RN(A shat)),
the frozen r2 expression, is an outward bound. The successor of a
rounded nonnegative finite product is at least its exact value, also
in the subnormal range.

This is a sufficient input condition, not a claim about the unsaved
actual r2 values. For the source n=523 the threshold is exactly
523*2^-1021, which is a normal binary64 number and can be tested exactly.
Only195 different sums need this test: thirteen radial cells and fifteen
pairs i+j<=4. They repeat over the sixteen angular cells, since epsSup
and remfac depend only on ci,i,j and the shared width w. The actual
source assignments must be checked before using that count.

The generic counterexample in POSITIVE_SUMS.md remains valid when(3)
fails. Alternatively the conservative explicit additive allowance
already proved there can be used in a new calculation. We do not adopt
an unproved claim that n eta/2 alone is a sufficient added allowance
through an unspecified sequence of rounded operations. No actual r2
or physical forcing certificate is accepted by this lemma alone.
