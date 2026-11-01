# Exact period-ten response identity and factor audit

Status: PROVED in V585, admitted 2026-10-31T21:14:43+00:00, within the exact scope below.

## Statement, notation and dependencies

Let delta=1/5, c=5/4 and f_1=sin(theta)+b sin(3theta), with b a real parameter. Use the zero-harmonic prefix, to be independently verified in281, f_1,...,f_10 and g_1,...,g_9 from281. For integer k>=2, let sigma_k(b) denote the coefficient of sin((2k-1)theta) in the change of f_(10k+10) caused by a unit free harmonic sin((2k-2)theta) in g_(10k). The affine response uses the recurrence01; no later solution coefficients enter it. For k>=21 write its formal rational expression as S(k,b).

This check independently reconstructs S from Cartesian derivatives over Q(k), and checks the factor and limiting-polynomial assertions of the separate producer formula. It also reconstructs every small response sigma_k for2<=k<=20. If the identities pass, every response is a nonzero polynomial of degree at most10 and its limit is nonzero of degree10. At each real root of the irreducible degree20 compatibility polynomial from281, the response and its limit are nonzero. Therefore the response infimum there is positive. Explicit lower bounds and convergence radii are not supplied by this symbolic check; a qualitative convergence implication will require the general tuned convergence theorem with all its hypotheses.

## Independent response calculation

Represent a homogeneous Fourier field by its radial exponent q and signed frequencies m=a k+d. The Cartesian rules are those proved in119: X sends a term to m-1 and m+1 with coefficients (q+m)/2 and(q-m)/2; Y is the derivative in y divided by i and has the corresponding opposite sign at m+1. Encode sine terms by signed coefficients plus or minus one half. Then the Jacobian is Xg Yf-Yg Xf. The stream inverse solves -XXg+YYg=Xf and is checked coefficient by coefficient.

Put n=10k, E=r^(2-2k)sin((2k-2)theta), U_0=V_0=0. For1<=r<=10 calculate

    U_r = [4/(n+r-1)] [J(E,f_r)
             +sum_(1<=s<r)(J(V_s,f_(r-s))+J(g_(r-s),U_s))],

and, when r<10, let V_r be the Poisson inverse of U_r. The response is the designated sine coefficient of U_10. Its b degree is at most10 by induction on r. All calculations use exact rational functions in k. For k>=21 the carrier2k-2 is at least40. At step r the frequency offsets are bounded by4r-1, so no final density frequency changes sign, and intermediate inversions have no zero-frequency identification. Full signed frequencies avoid folding in any case. The computed denominators are explicitly checked to have no integer zero in this range.

Compute the expression at eleven distinct rational b values. Lagrange interpolation is an exact identity because the degree is at most10. The monic least common multiple D of the eleven reduced denominators is also the minimal common denominator of the interpolated b coefficients: evaluation and interpolation use rational linear combinations in both directions. Store these coefficients over D, not an expanded unnecessarily large expression.

## Exact factor and limiting checks

Factor the minimal common denominator D and the gcd G of the interpolated numerator coefficients over the rationals. Reassemble every factor and its multiplicity exactly. The intended certificate consists entirely of linear factors; if another factor occurs, no all-index conclusion is drawn until it is handled separately. For every rational root, check directly that it is not an integer at least21. Therefore D and G are both nonzero at all integer carriers in this range.

Extract the limiting response from the leading coefficients after checking that no numerator degree exceeds the denominator degree. This is a rational polynomial in b; it must be nonzero. Independently compare the theory part's displayed factorization by cancelling the common denominator/numerator factor, and compare every coefficient of its limiting polynomial when that output becomes available. These producer comparisons are separate from the internal exact certificate.

For the small integer carriers2<=k<=20, calculate actual signed integer frequencies, allowing collisions to combine, and interpolate from the same eleven b values. This verifies the stated degree and nonzero leading coefficient at each small k. At k=21,...,26 calculate with actual integer frequencies and compare with the generic rational expression. These are additional implementation checks; the formal identity and degree proof, rather than a finite sample, establish the all-index formula.

## Nonvanishing conclusion

All numerator-gcd roots of the large-carrier formula are outside the integer range k>=21. Thus no specialized large-carrier numerator polynomial in b is identically zero. The small responses and the limit are separately checked nonzero. A rational polynomial of b degree at most10 cannot vanish at a root of the irreducible rational degree20 polynomial. Each response there is nonzero, and its nonzero limit bounds the tail away from zero. A finite initial minimum then gives a positive all-index infimum.

This is an exact algebraic and source-comparison check. It depends on the finite prefix of281 after its verification and admission, the signed calculus119 and the degree argument149. Finite decimal evaluations, if added later, have separate scope. No floating-point fit is used in the nonvanishing proof.

## Completed verification

The eleven exact Cartesian Q(k) calculations give b degree10, minimal denominator degree109, numerator degree109, and numerator-coefficient gcd degree3. Every denominator and coefficient-gcd factor is exactly reconstructed and has no integer root at least21. All19 small responses at k2..20 and the limiting polynomial have degree10; six actual-integer calculations k21..26 agree with the generic formula. Every response and its limit is nonzero at all fourteen irreducible degree20 compatibility roots, so each root has a positive all-index response infimum. The computation took831.582083seconds.

The symbolic nonvanishing and its qualitative exterior-convergence implication are PROVED. The potential reconstruction follows132 and the mandatory first logarithm follows283. This entry supplies no numerical lower bound, explicit radius or full comparison with the theory part response; those are separate checks.
