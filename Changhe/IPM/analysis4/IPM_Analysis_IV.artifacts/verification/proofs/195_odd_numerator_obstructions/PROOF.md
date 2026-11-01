# Finite odd-numerator obstructions for the single sine profile

Status: PROVED for the stated finite set; V389, 2026-10-31T14:33:38+00:00.

## Exact statement

Let p range over the primes 5,7,11,13,17,19,23, and let a be an odd integer with 3<=a<p. Set delta=a/p, c=p/(p-a), and f_1(theta)=sin(theta). Use the pure stationary density/stream recursion with no additional exponent channels. For each of these37 pairs, the first stream resonance is at n=2p. The coefficient kappa_(p,a) of sin((2a-3)theta) in f_(2p) is nonzero. Consequently no pure density/stream series with this f_1 and c can pass this resonance. This is an algebraic obstruction to the stipulated series; it is not a divergence theorem for a logarithmic or enlarged expansion.

For these finite pairs, the p-adic valuation of kappa lies in{-2,-1,0}, and valuation0 occurs only for(p,a)=(11,5). No all-prime formula is asserted.

## Notation and exact recurrence

Put p_n=1-na/p, P_n=p_n+1, and lambda_n=(n-1)a/(p-a). Represent each physical sine polynomial by -i times the real Laurent polynomial F(z)=sum_m f_m(z^m-z^(-m))/2, z=exp(i theta). Define

X_q(z^m)=((q+m)z^(m-1)+(q-m)z^(m+1))/2,
Y_q(z^m)=((q+m)z^(m-1)-(q-m)z^(m+1))/2.

Cartesian derivatives are X and iY on the Laurent expression and lower q by1. Thus the exact density recurrence is

F_n=lambda_n^(-1) sum_(i+j=n)[X_(P_i)G_i Y_(p_j)F_j-Y_(P_i)G_i X_(p_j)F_j].

The stream coefficient is obtained by dividing the coefficient of z^m in X_(p_n)F_n by m^2-P_n^2. Every division prior to the first resonance is nonzero. The independent implementation uses exact rational Laurent products, and separately checks -X X G_n+Y Y G_n-X F_n=0 at every prior order.

## Complete argument

Since p is prime and0<a<p, a and p are coprime. A stream resonance requires n a/p to be an even integer at least4. Because a is odd, this holds exactly when n is a multiple of2p, and the first such order is2p. There P_(2p)=2-2a=-2(a-1), so the resonant sine frequency is m=2(a-1).

The forcing at this frequency is[(P_(2p)-m)f_(2p,m-1)+(P_(2p)+m)f_(2p,m+1)]/2=-2(a-1)kappa_(p,a). Hence compatibility is equivalent to kappa_(p,a)=0. All previous density coefficients and nonresonant stream coefficients are uniquely fixed by f_1. Adding a free harmonic at order2p cannot cancel nonzero forcing in the kernel of the Poisson operator.

The finite computation listed in verification/checks.json enumerates exactly the37 pairs, performs only exact rational arithmetic in the preceding recursion, and records kappa and its forcing coefficient as rational numbers. Checking that each numerator is nonzero proves all37 incompatibilities. Integer divisions by p in each numerator and denominator prove the stated valuations. Clearing p^4 and reducing the resulting rational number modulo p^6 independently supplies the six p-adic digits of positions-4 through1. Equality with the separately produced table is an additional cross-check, not the proof of nonvanishing.

## Dependencies and scope

The Cartesian derivative identities and stationary signs were independently established in topic01. The exact Laurent engine and rational recursion were developed in topics21 and24 independently of the theory part's sine/cosine product implementation. This argument reuses that engine but recomputes every pair. It relies on exact integer/rational software arithmetic, not on floating-point digit separation. The source table and both implementation snapshots are retained. The result concerns only the stated37 pairs and the single sine leading profile; other profiles, larger primes, logarithmic expansions, and the original stored Candidate007 parameter are outside its conclusion.

## Verification

For p in {5,7,11,13,17,19,23} and odd 3<=a<p, every first resonance is n=2p and every kappa is nonzero. The valuations have counts {-2: 17, -1: 19, 0: 1}; valuation zero occurs only at (11,5). All 222 p-adic digits agree with the theory part. The computation took 156.71484271530062 seconds. Exact coefficients and forcing values are retained in topic195. The numerical experiments also reports an independent exact agreement.

CONFIRMED. Each of these 37 pure density/stream series is algebraically obstructed at its stated first resonance. No universal odd-numerator formula, logarithmic divergence or conclusion for the original stored parameter follows.
