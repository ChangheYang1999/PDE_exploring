# Finite-part expansion of the frozen Fourier packets

Date: 2026-10-20. This is a standalone audit of the full local C^N expansion, including its logarithmic qualifications. It concerns the frozen equation only.

## Statement and notation

Use A>1, g>0, q=2(A-1), b=g/q, Q=A+1, h=1+g and a smooth Phi compactly supported away from zero as in ../packet-dyadic-audit/PROOF.md. In particular integral Phi=0 and Phi(-t)=-conjugate(Phi(t)). Let v be exactly the continuous tempered packet defined there. For k>=0 put

    h_k=h+kq,
    c_k=(-1)^k b(b+1)...(b+k-1)/k!, with c_0=1,
    a_k(t)=c_k Phi(t)|t|^(-2b-2k).

For an ordinary multi-index(a,c), write its anisotropic weight as lambda(a,c)=Aa+c. Define the finite set J_k={(a,c): a,c>=0 integers, c odd, lambda(a,c)<=h_k} and

    M_(k,a,c)=2/(a!c!) integral a_k(t)t^a dt.

There is a specific tempered extension E_k of the smooth frequency density

    sgn(eta)|eta|^(-Q-h_k) a_k(xi/|eta|^A), eta!=0,       (1)

defined below by radial finite parts at radius1. Put u_k=FourierInverse(E_k), with inverse factor c_F=(2pi)^-2. Then:

1. Each u_k is smooth away from the origin. For every mu>0,

    u_k(mu^A s,mu y)=mu^(h_k)[u_k(s,y)+log(mu)P_k(s,y)],  (2)

   in distributions, hence pointwise away from the origin, where the real polynomial is

    P_k(s,y)=-c_F sum_(a,c):lambda(a,c)=h_k
                        M_(k,a,c) i^(a+c) s^a y^c.       (3)

   The sum is over nonnegative a and odd positive c. Every monomial has weight h_k. An empty sum is zero.
2. A genuinely homogeneous extension of(1) exists exactly when every resonant moment M_(k,a,c) in(3) vanishes. A change of extension by a distribution supported at zero cannot remove a nonzero logarithmic anomaly. Arbitrary such changes can also introduce polynomial terms of other weights; they need not preserve the precise form(2).
3. For every nonnegative integer N, choose an integer K>=1 with h_K>AN. Then, near the origin,

    v=sum_(0<=k<K) u_k+R_N,       R_N in C^N_loc.          (4)

   The smooth terms included in R_N are not omitted. Formula(4) is a finite-order expansion for each N, not a claim that the infinite series converges.

Pure homogeneity at the leading order does not exclude resonances at later h_k. No inference about an exact coupled profile, a kernel correction, an admissible global perturbation, a family, or either endpoint is made. The definition and positive regularity estimates in the preceding packet proof are dependencies; the finite parts and remainder estimates are proved here.

## Construction of the finite part

Fix k and temporarily write H=h_k and a(t)=a_k(t). For a Schwartz test function phi define

    J_phi(r)=integral a(t)[phi(t r^A,r)-phi(t r^A,-r)]dt.

The Jacobian dxi=r^A dt turns the formal pairing of(1) into integral r^(-H-1)J_phi(r)dr. Let

    C_lambda(phi)=sum_(a,c):Aa+c=lambda, c odd
                        M_(k,a,c) d_xi^a d_eta^c phi(0,0).

Only weights lambda<=H are used below. They form a finite set because A>1. Taylor expansion of phi at zero gives

    J_phi(r)=sum_(lambda<=H) C_lambda(phi) r^lambda
                         +O(r^(H+delta)),   0<r<=1,       (5)

for some delta>0 depending on A,H, uniformly in a fixed finite Schwartz seminorm. For clarity, choose an integer L>H and use the ordinary Taylor polynomial of total degree L-1. Its remainder is O(r^L) because |(tr^A,r)|<=C r on the fixed t support. The finitely many polynomial terms not retained in(5) have weights strictly greater than H. Take delta to be the minimum of L-H and their positive excesses. The two eta signs cancel every even c term. This proves(5) with no assumption that A is rational.

Define

    <E_k,phi> = integral_0^1 r^(-H-1)
                  [J_phi(r)-sum_(lambda<=H)C_lambda(phi)r^lambda]dr
              +integral_1^infinity r^(-H-1)J_phi(r)dr
              +sum_(lambda<H) C_lambda(phi)/(lambda-H).   (6)

The first integral converges by(5); the second converges by Schwartz decay in eta=r. Both are controlled by finitely many Schwartz seminorms, so this defines a tempered distribution. If phi is supported away from zero, its origin jets vanish and(6) is the ordinary pairing with(1). Thus E_k is an extension. Its reality follows from the symmetry of a(t) and the paired eta signs; Taylor subtraction and its real coefficients preserve that symmetry.

An equivalent formula, useful for checking signs, is

    <E_k,phi>=lim_(epsilon->0) [integral_epsilon^infinity
                  r^(-H-1)J_phi(r)dr
              -sum_(lambda<H) C_lambda(phi)epsilon^(lambda-H)/(H-lambda)
              +C_H(phi)log(epsilon)],                    (7)

where C_H=0 if the weight H does not occur. Integrating each subtracted power on(epsilon,1) proves equivalence to(6). In particular the sign of the logarithmic term is specified.

## Scaling and the resonance obstruction

Set delta_mu(xi,eta)=(mu^A xi,mu eta) and phi_mu=phi composed with delta_mu. Then J_(phi_mu)(r)=J_phi(mu r) and C_lambda(phi_mu)=mu^lambda C_lambda(phi). Substituting t=mu r in(7), including its subtraction terms, gives exactly

    <E_k,phi_mu>=mu^H[<E_k,phi>-log(mu)C_H(phi)].          (8)

Let Res_k be the distribution phi mapped to C_H(phi). The Fourier transform of u_k composed with delta_mu is the distribution phi mapped to <E_k,phi_mu>. Hence(8) gives(2) with P_k=-FourierInverse(Res_k). Since the functional d^alpha phi(0) is(-1)^|alpha|d^alpha delta_0 and the inverse transform of d^alpha delta_0 is c_F(-iX)^alpha, this is exactly(3). Thus the sign and Fourier factors in(3) are checked, not left implicit.

The monomials in(3) are linearly independent. Therefore P_k=0 exactly when all the indicated moments vanish. In this case(8) says E_k is homogeneous and supplies the required extension.

Conversely, two distributional extensions of(1) differ by a distribution supported at the frequency origin. Such a distribution is a finite linear combination of derivatives of delta_0, hence its inverse transform is a polynomial. One justification of this elementary structure fact is that a compactly supported distribution has finite order; after subtracting a test function's Taylor jet through that order and using shrinking cutoffs at its support point, it annihilates the remainder. Its action therefore factors through a finite jet.

Suppose adding a polynomial p(X) to u_k removed the anomaly. For all mu>0 it would have to satisfy

    p(delta_mu X)-mu^H p(X)=-mu^H log(mu)P_k(X).           (9)

Compare the coefficient of each monomial of weight H. The left side is zero in those coefficients, since mu^H-mu^H=0. The right side is nonzero for some mu if the corresponding coefficient of P_k is nonzero. Thus(9) is impossible when P_k!=0. This also explains why nonresonant polynomial changes do not cancel resonant logarithms. No classification of all solutions of the frozen equation is used.

## Smoothness away from the origin

The high-frequency part of E_k admits a dyadic partition with radial pieces chi(2^-n r), apart from finitely many smooth compact-frequency transition terms. The exact anisotropic homogeneity of the density(1) makes each inverse piece

    2^(-h_k n) G(2^(An)s,2^n y),

where G is a fixed Schwartz function. Indeed, after frequency dilation, the amplitude is one fixed smooth compactly supported function separated from both coordinate axes. Repeated integration by parts gives, for all a,c,L>=0,

    |d_s^a d_y^c [2^(-h_k n)G(2^(An)s,2^n y)]|
      <= C_(a,c,L) 2^((Aa+c-h_k)n)
                         (1+2^(An)|s|+2^n|y|)^(-L).

If a compact set has Euclidean distance at least d>0 from the origin, the last parentheses are at least C_d 2^n, since A>1. Choosing L>Aa+c-h_k+1 makes the series of the indicated derivatives uniformly summable there. The low-frequency part of E_k has compact support as a distribution, and its inverse transform is smooth, as justified in the next section. Thus every u_k is smooth away from the origin. This proves the smoothness assertion in statement1 independently of the finite-order remainder argument.

## High-frequency expansion and the C^N remainder

Write r=|eta| and t=xi/r^A. The exact packet density is

    sgn(eta) r^(-Q-h) Phi(t)|t|^(-2b)
                                (1+t^(-2)r^(-q))^(-b).   (10)

Taylor's formula with integral remainder for z mapped to(1+z)^(-b) gives, for r>=1,

    (10)=sum_(0<=k<K) sgn(eta)r^(-Q-h_k)a_k(t)
                                       +error_K.         (11)

Here t stays in a fixed compact set separated from zero. After setting r=2^n u with u in a fixed compact subinterval of(0,infinity), multiplying error_K by2^((Q+h_K)n), and expressing it in the scaled frequency variables(zeta,nu)=(2^(-An)xi,2^(-n)eta), every derivative of every fixed order is uniformly bounded in n>=0. To verify this directly, factor z^K from the integral remainder. The residual function of z is smooth on0<=z<=C and all its derivatives there are bounded; on the scaled support z=t^(-2)2^(-qn)u^(-q), while |t| and u have positive lower bounds. The two sign branches are separated from nu=0. Composing with their smooth coordinate maps gives the asserted uniform bounds.

Take a smooth radial cutoff chi_hi(r) that is zero for r<=1 and one for r>=2. Decompose its remainder in(11) into dyadic radial pieces. Each inverse piece has the form

    2^(-h_K n) G_n(2^(An)s,2^n y),

with G_n uniformly Schwartz. This follows by integration by parts on the fixed compact scaled frequency support, as in the preceding packet proof. Every ordinary derivative of total order at most N is bounded by C 2^((AN-h_K)n). Since h_K>AN, the series of these derivatives converges uniformly. Thus the high-frequency remainder has continuous ordinary derivatives through order N.

For each k, the distribution E_k-chi_hi E_k has compact frequency support. Its inverse transform is smooth, indeed entire: on its compact support the exponential and every derivative have uniformly convergent power series, to which the finite-order distribution can be applied. The low-frequency part of the exact packet has the same property. Finally, chi_hi E_k is multiplication of the ordinary density(1) by chi_hi, because its support avoids the origin. Subtracting sum_(k<K)E_k from the exact packet therefore leaves the C^N high-frequency remainder just proved plus a smooth low-frequency term. Fourier inversion proves(4).

## Scope and verification record

For each N, q>0 ensures that a finite K with h_K>AN exists. This provides every requested finite differentiability remainder, including resonant cases. The weighted smooth jets and the polynomial logarithmic terms are explicit parts of the statement, so the expansion does not justify dropping them in an axis trace. The all-order normalized trace result is separately proved by direct dyadic estimates in the preceding packet proof and need not be deduced from(4).

No numerical candidate parameter is used. No Lean source or numerical experiment is required for this analytic argument. The actual Claude Opus 5.5 review completed at2026-10-20T22:57:38Z and is retained in verification/. It independently confirmed the finite parts, signs, Fourier factors, resonance obstruction and remainder estimates. It requested the explicit off-origin smoothness argument now given above. The verifier checked the compact-set lower bound and derivative summability directly. Status: CONFIRMED for the stated frozen equation and finite-order expansion; all coupled and endpoint conclusions remain OPEN.
