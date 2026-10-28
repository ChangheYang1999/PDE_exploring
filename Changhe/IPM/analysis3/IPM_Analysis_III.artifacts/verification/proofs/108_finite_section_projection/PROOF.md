# The truncated-sine finite-section map is not a contraction

## Spaces and the exact map

At a fixed logarithmic radius write a parity-preserving angular function as f(theta). Set p(theta)=cos(theta)^2 sin(theta), and let the angular target space consist of

 f=gamma p+cos(theta)^4 q(theta),
 ||f||_Yang^2=gamma^2+integral_0^(2pi) |cos(theta)|^(-1/2)|q(theta)|^2 dtheta.

The decomposition is unique. Its remainder subspace has gamma=0. Multiplying an angular function by r^3 b(log r), where b is any smooth function supported on a compact radial annulus, gives an element of the actual global target. The common radial weight is omega(t) from proof 98. Normalize b by integral omega b^2=1 to transfer all ratios below to that target exactly.

For N>=2, let P_N retain the raw sine coefficients of sin((2j+1)theta), 0<=j<=N. For a retained coefficient vector G define

 gamma_N=-(1/2) sum_(j=0)^N (-1)^j(2j+1)^2 G_j,
 R_N=G-gamma_N(1/4,1/4,0,...,0).

Let M_N be the matrix of multiplication by cos(theta)^4 from the N-1 sine modes indexed0,...,N-2 to the N+1 retained sine modes. Its columns are linearly independent: multiplication by cos(theta)^4 is injective on trigonometric polynomials and these products have no omitted modes. Put

 q_N=(M_N^T M_N)^(-1) M_N^T R_N,
 Pi_N f=gamma_N p+cos(theta)^4 sum_(j=0)^(N-2) (q_N)_j sin((2j+1)theta).

This is the exact mathematical map implemented by the jet split and Euclidean least-squares division in the current floating finite-section code. It is a projection onto its conforming finite-dimensional range, since it fixes every function in that range. Its coefficient functionals are bounded on Y_ang: p is smooth, and for the remainder each Fourier pairing is controlled by Cauchy-Schwarz against the integrable inverse angular weight. Hence Pi_N is bounded for each fixed N. It is not the orthogonal projection in Y_ang and is not a contraction.

## Exact counterexample at the smallest cutoff

Take N=2 and f=cos(theta)^4 sin(3theta). Its true jet is zero. Its full raw sine coefficients, from index0 to3, are

 (3,6,4,1)/16.

After truncation gamma_2=-49/32 and R_2=(73,97,32)/128. The sole column of M_2 is (2,3,1)/16. Therefore the least-squares quotient is q_2=67/16.

Let M=2 Beta(1/4,3/2), and let H be the normalized cosine quadratic form of proof 98. Since sin(3theta)/sin(theta)=1+2cos(2theta), its moments m_1=-5/7 and m_2=29/77 give

 ||f||_Yang^2=M(69/77),
 ||Pi_2 f||_Yang^2=(49/32)^2+M(67/16)^2.

Even discarding the false jet, the ratio of squared remainder norms is

 (67/16)^2/(69/77)=345653/17664.

Its square root is greater than4.4235. Thus the same defect persists when the finite-section routine discards the extracted jet and keeps only its reconstructed remainder, as in the S_1 calculation.

## Exact counterexample at the current cutoff

For every N>=2 use f_N=cos(theta)^4 sin((2N-1)theta). The only raw coefficient above cutoff N is the coefficient1/16 of index N+1. The full function has zero jet, so the retained vector has false jet

 gamma_N=(-1)^(N+1)(2N+3)^2/32.

Also ||f_N||_Yang^2<=integral |cos(theta)|^(-1/2)dtheta=2 Beta(1/4,1/2)<10.49. Already this proves that the norm of Pi_N is unbounded as N grows.

For N=19, exact rational elimination of M_N^T M_N gives gamma_19=1681/32. Converting both input and output sine quotients to cosine cofactors and using the rational moments gives

 H_input=5978235987187914982121/7551392461129228097953,
 H_output=1694010729887266205844273477683711698357/84319121123535723499366829298300.

The remainder norm ratio is greater than5037.5809. Including the false jet gives a Y_ang ratio greater than5037.6304. The exact quotient coefficients and256-bit directed evaluations are in evidence/check.json. No floating matrix inversion enters this example.

## Consequences for an inverse certificate

A lower bound s for ||Pi_N Lh|| over a chosen finite input space implies only ||Lh||>=s||h||/||Pi_N||. It does not give the same lower bound s for the full image norm. A conforming orthogonal projection avoids this factor; raw truncation followed by least-squares division requires its own norm bound. The counterexample is about the test map, not about the actual singular vectors of the current finite section, and does not prove that those computed singular values are inaccurate by this full factor.

The present floating domain Gram also omits the J and Hardy terms of B. The scalar Hardy theorem of proof 38 gives the valid comparison

 ||z'||_omega <= ||beta||_B <= C_B ||z'||_omega,
 C_B^2=1+1/(2sigma)+1/(2kappa)+max(sigma^(-2),kappa^(-2)),
 sigma=1/4, kappa=k+3/8.

Thus an exact calculation using only the derivative seminorm could be converted using C_B, provided the remainder graph norm were otherwise exact. In the current code the transport image is also truncated and divided by Pi_N, so its graph-norm comparison is a further obligation. Finite radial quadrature and the truncated infinite tails remain separate numerical obligations. The current result is explicitly floating and is not a continuum inverse certificate.

## Tail compensation audit

The inspected snapshot now keeps DKB_j=-k c_j/(3ell+k c_KP) as an Arb enclosure of the exact quotient through image assembly. This repairs the earlier conversion of the compensation coefficient through binary floating point. If the exact coefficient were replaced by a different number with error epsilon!=0, the image would retain a nonzero leading r^(k-3) cofactor. Its squared strong radial integrand grows as exp((2k+3/4)t), so it would fail target membership. This is why an arbitrarily small coefficient error cannot simply be treated as a small strong-target norm error. Correct exact compensation instead leaves the next cofactor order r^(2k-4), whose exponent4k-5/4 is negative for the actual k.

The inspected repair encloses an exactly specified coefficient. It must not be interpreted as permission to replace that coefficient by an arbitrary point of its interval. This proof does not audit every other part of the finite-section assembly.

## Evidence and dependencies

The proof uses only elementary trigonometric multiplication, exact rational linear algebra, proof 38's Hardy estimate and proof 98's angular norm. The code records real execution time and all exact output fractions. The numerical code snapshots are read-only copies in evidence/. No code from those snapshots was executed.
