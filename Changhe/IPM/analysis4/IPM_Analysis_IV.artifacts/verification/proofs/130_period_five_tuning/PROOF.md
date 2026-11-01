# Five-step resonant tuning and the first compatibility polynomial

Status: PROVED. The theory part independently confirmed the block identity and exactly reproduced the period-five obstruction and response formulas in the review dated2026-10-31T10:38Z. V273 records the comparison. The block proof applies to every integer Q>=3; explicit two-mode calculations here use Q=5.

## Exact statement and notation

Let Q>=3 be an integer, delta=2/Q, c=Q/(Q-2), p_n=1-2n/Q and lambda_n=2(n-1)/(Q-2). Density coefficients are odd sine polynomials and stream coefficients are even sine polynomials. Write T(g,f)=-p_f g' f+(p_g+1)g f' for the angular advection of terms whose density orders are the subscripts of g and f. Equivalently use the Cartesian operators X,Y of topic128, so T(g,f)=Xg Yf-Yg Xf with the radial powers included.

The positive-even stream resonances occur exactly at n=kQ, k>=2. At such an order put m=2k-2. The stream equation has a solution without logarithms if and only if the coefficient of sin((m-1)theta) in f_n vanishes. Its remaining freedom is H_n sin(m theta). The zero stream mode at n=Q is absent from the imposed sine symmetry and supplies neither an obstruction nor a free coefficient.

Suppose coefficients are already determined before a resonant order n=kQ, and its compatibility condition holds. Keep all earlier free constants fixed. If H_n changes by h, then for 1<=r<=Q the change of the density coefficient at n+r is exactly h phi_r. Set e=sin(m theta), and let Pi_j be the nonresonant angular Poisson inverse at order j. The response polynomials are

    lambda_(n+r) phi_r
      = T(e,f_r)
        + sum_(s=1)^(r-1) [T(g_(r-s),phi_s)
                           + T(Pi_(n+s) phi_s,f_(r-s))].       (1)

In the first term e occupies stream order n. The fields f_r,g_(r-s) in this formula are the original low-order fields. Thus the next compatibility obstruction, at n+Q, is affine in H_n, with slope

    sigma_k = coefficient of sin((2k-1)theta) in phi_Q.       (2)

Each phi_r is a homogeneous polynomial of degree r in the leading density coefficients, and sigma_k is homogeneous of degree Q. These statements do not assume sigma_k is nonzero and do not prove a uniform lower bound.

For Q=5 and f_1=sin(theta)+b sin(3theta), the first obstruction is

    O10(b) = coefficient of sin(theta) in f_10.

It is an exact rational polynomial in b of degree at most10. A real zero b of O10 gives a pure density/stream prefix through order10, with one free harmonic H10. Whether that prefix extends through order15 requires the affine condition with sigma_2, and infinite convergence requires additional estimates.

## Proof

The Poisson denominator is m^2-(2-2n/Q)^2. For positive even m it vanishes precisely when n=Q(m/2+1), giving the stated resonances. At n=kQ the exponent p_n=1-2k=-m-1. The coefficient forcing stream frequency m is

    [(p_n-m+1) a_(m-1)+(p_n+m+1) a_(m+1)]/2
      = -m a_(m-1).

As m>0, its vanishing is equivalent to a_(m-1)=0. The other stream coefficients have nonzero divisors; the kernel is exactly the one sine harmonic specified above. At n=Q the only zero multiplier has m=0, which is excluded by sine symmetry.

The nonlinear recurrence only uses pairs of positive orders summing to the target order. A change at stream order n therefore leaves every density order at most n unchanged, and can first affect f_(n+1). At a target order n+r with r<=Q, a term involving two affected factors would have total order at least2n+1. Since n>=2Q, this exceeds n+Q. Every change is consequently linear in h. Sorting the terms with one affected factor gives(1): the direct changed stream at order n multiplies f_r; a changed density phi_s multiplies the unchanged low stream g_(r-s); and a changed nonresonant stream Pi phi_s multiplies the unchanged low density f_(r-s). All intermediate orders n+s, 1<=s<Q, are nonresonant, so their Poisson inverses are unique in the sine class. This proves the exact response formula inductively.

The next resonance is n+Q=(k+1)Q, whose forbidden density frequency is2(k+1)-3=2k-1. Extracting it gives(2). The low-order coefficients f_r and g_r are homogeneous of degree r in f_1, and the response formula increases the degree from s to r by multiplication with a low field of degree r-s. Starting with the degree-one phi_1 proves the homogeneity statement.

For the two-mode leading polynomial, no earlier positive-even resonance occurs before order10. Repeated products and divisions by nonzero rational constants give rational polynomials in b, of degree at most their order. Therefore O10 has the asserted form. Its real roots and any further compatibility claims must be checked from the exact polynomial, not from rounded coefficients.

## Completed finite evidence

An independent signed Laurent Cartesian implementation computes orders1through10 in exact rational arithmetic, records every density and stream coefficient, verifies the Poisson identities and symmetry, and extracts O10. Exact real-root isolation and square-free factorization determine all real roots. Subsequent tests may evaluate responses and the order15 obstruction at those roots. Those computations will be recorded separately, with actual execution times and no inference about infinite convergence from finite prefixes.

Dependencies: the elementary Cartesian derivative identities of topics1and119, the exact angular Poisson formula verified in the initial audit, and the stationary equation. No theorem about generic tuning or convergence for Q=3 is assumed to hold for Q=5 without a new proof.

The computation found the exact degree-ten obstruction with six real roots. Its primitive numerator is irreducible modulo11. The generic response has degree5 in b, numerator coefficient gcd (k-1)(2k-1)^2, and a nonzero degree-five limit. Exact finite and symbolic formulas, modular powers and Sturm variations are retained in verification. Topic133 states the resulting proved convergence theorem and its all-k response certificates.

The proof does not use parity of Q. For even Q, the extra indices n=(Q/2)(2j+1) have odd integer P_n and hence cannot resonate with a positive even stream frequency. Every nonzero factored divisor still belongs to (2/Q)Z, so all bounds are unchanged.
