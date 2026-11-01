# Exact period-nine response identity and factor audit

Status: CONFIRMED in V567. The proof was written before computation; every listed exact identity passed on2026-10-31. The independent reconstruction confirms the theory part's algebraic proof of response nonvanishing.

## Statement, notation and dependencies

Let delta=2/9, c=9/7 and f_1=sin(theta)+b sin(3theta), with b a real parameter. Use the already independently computed zero-harmonic prefix f_1,...,f_9 and g_1,...,g_8 from267. For integer k>=2, let sigma_k(b) denote the coefficient of sin((2k-1)theta) in the change of f_(9k+9) caused by a unit free harmonic sin((2k-2)theta) in g_(9k). The affine response uses the recurrence01; no later solution coefficients enter it. For k>=19 write its formal rational expression as S(k,b).

This check independently reconstructs S from Cartesian derivatives over Q(k), and checks the factor and limiting-polynomial assertions of the separate producer formula. It also reconstructs every small response sigma_k for2<=k<=18. If the identities pass, every response is a nonzero polynomial of degree at most9 and its limit is nonzero of degree9. At each of the ten roots of the irreducible degree18 compatibility polynomial from267, the response and its limit are nonzero. Therefore the response infimum there is positive. Explicit lower bounds and convergence radii remain those of267; this check does not improve them.

## Independent response calculation

Represent a homogeneous Fourier field by its radial exponent q and signed frequencies m=a k+d. The Cartesian rules are those proved in119: X sends a term to m-1 and m+1 with coefficients (q+m)/2 and(q-m)/2; Y is the derivative in y divided by i and has the corresponding opposite sign at m+1. Encode sine terms by signed coefficients plus or minus one half. Then the Jacobian is Xg Yf-Yg Xf. The stream inverse solves -XXg+YYg=Xf and is checked coefficient by coefficient.

Put n=9k, E=r^(2-2k)sin((2k-2)theta), U_0=V_0=0. For1<=r<=9 calculate

    U_r = [7/(2(n+r-1))] [J(E,f_r)
             +sum_(1<=s<r)(J(V_s,f_(r-s))+J(g_(r-s),U_s))],

and, when r<9, let V_r be the Poisson inverse of U_r. The response is the designated sine coefficient of U_9. Its b degree is at most9 by induction on r. All calculations use exact rational functions in k. For k>=19 the carrier2k-2 is at least36. At step r the frequency offsets are bounded by4r-1, so no final density frequency changes sign, and intermediate inversions have no zero-frequency identification. Full signed frequencies avoid folding in any case. The computed denominators are explicitly checked to have no integer zero in this range.

Compute the expression at ten distinct rational b values. Lagrange interpolation is an exact identity because the degree is at most9. The monic least common multiple D of the ten reduced denominators is also the minimal common denominator of the interpolated b coefficients: evaluation and interpolation use rational linear combinations in both directions. Store these coefficients over D, not an expanded unnecessarily large expression.

## Producer factor assertions

Reconstruct the monic claimed denominator D0 from its displayed linear factors, including multiplicity, and its displayed numerator coefficient gcd G0 from the displayed roots and multiplicities. Compare G0 with the independently decoded printed polynomial. Let G be the gcd of the independently reconstructed numerator coefficients over D. Verify exactly

    D = D0/gcd(D0,G0),
    monic(G) = G0/gcd(D0,G0).

Equivalently the lifted numerator S D0 is polynomial in k,b and its b-coefficient gcd is G0. This checks the claimed degree and all roots without retaining the massive lifted numerator. Scalar normalizations of D0 and the numerator do not affect these statements. The displayed leading limiting polynomial is checked coefficient by coefficient against the rational limit of the independently reconstructed expression.

For the small integer carriers2<=k<=18, calculate actual signed integer frequencies, allowing collisions to combine, and interpolate from the same ten b values. This verifies the stated degree and nonzero leading coefficient at each small k. At k=19,...,24 calculate with actual integer frequencies and compare with the generic rational expression. These are additional implementation checks; the formal identity and degree proof, rather than a finite sample, establish the all-index formula.

## Nonvanishing conclusion

All numerator-gcd roots of the large-carrier formula are outside the integer range k>=19. Thus no specialized large-carrier numerator polynomial in b is identically zero. The small responses and the limit are separately checked nonzero. A rational polynomial of b degree at most9 cannot vanish at a root of the irreducible rational degree18 polynomial. Each response there is nonzero, and its nonzero limit bounds the tail away from zero. A finite initial minimum then gives a positive all-index infimum.

This is an exact algebraic and source-comparison check. It depends on the already admitted prefix267, the signed calculus119 and the degree argument149. Finite decimal evaluations, if added later, have separate scope. No floating-point fit is used in the nonvanishing proof.
