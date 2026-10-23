# Canonical harmonic moments on radial shells

Result98. Written2026-10-21 before its implementation. This is an exact evaluator identity for canonical density-stream pairs. It does not assert that any saved density solves the transport equation. The signed contributions below must not be called absolute moments or bounds on the absolute integrand.

## 1. General identity and endpoints

Let rho be a smooth even-x, odd-y density on the plane, with the primary sublinear density and gradient bound of exponent0<gamma<1. Write b_(2j+1)(r) for its odd sine coefficients, using the convention rho=sum_j b_(2j+1)(r)sin((2j+1)theta). Angular integration and differentiation give the frequency2n coefficient of rho_x:

    f_(2n)(r) = [b_(2n-1)'-(2n-1)b_(2n-1)/r
                    +b_(2n+1)'+(2n+1)b_(2n+1)/r]/2, n>=1.     (1)

Indeed d_x=cos(theta)d_r-sin(theta)d_theta/r and the elementary sine product identities give exactly these adjacent frequencies. For0<lo<hi<infinity, direct integration by parts in(1) gives

    I_(2n)(lo,hi) := int_lo^hi r^(1-2n) f_(2n)(r) dr
      = [r^(1-2n)(b_(2n-1)+b_(2n+1))]_lo^hi/2
                              +2n int_lo^hi b_(2n+1)(r)r^(-2n)dr. (2)

The first derivative term involving b_(2n-1) is an exact derivative. The remaining adjacent mode gives the factor2n in(2). Smoothness at0 implies b_(2j+1)=O(r^(2j+1)) and f_(2n)=O(r^(2n)), so the original integrand in(2) is O(r) there. The density and gradient bound implies f_(2n)=O(r^(gamma-1)) at infinity, where the integrand is O(r^(gamma-2n)). Thus the global source moment converges absolutely for every n>=1. Each boundary in(2) has a limit at0 and infinity; at0 only the leading coefficient of b_(2n-1) remains, while at infinity both vanish.

The regular, sublinear-velocity full-plane Green formula for source frequency2n is

    P_(2n)(r)=[r^(-2n) int_0^r u^(2n+1) f_(2n)(u)du
                   +r^(2n) int_r^infinity u^(1-2n) f_(2n)(u)du]/(4n). (3)

Differentiation verifies -[P''+P'/r-(2n)^2P/r^2]=f_(2n). The first term is O(r^(2n+2)) at0. Consequently, if H_(2n) is the coefficient of r^(2n)sin(2n theta) in the canonical stream Taylor expansion,

    I_(2n)(0,infinity)=4n H_(2n).                         (4)

Formula(3) has sublinear velocity, and parity plus harmonic uniqueness fixes the canonical gauge. In particular, if psi=c xy+q1 x^3 y+q2 xy^3+O(r^6), then

    I_2=2c,  I_4=q1-q2.                                  (5)

The frequency6 moment gives12 times the harmonic degree6 stream coefficient. No local normalization can replace that global moment.

## 2. Finite Q representation

Use the representation of result96:

    m0=L 2^(-kappa), r=m0 s^(1/2)(1-s)^(-kappa), w=1-s,
    rho=y w sum_(j=0)^(M-1) s^j B_j(s) cos(2j theta),
    d_0=B_0-s B_1/2, d_j=(B_j-s B_(j+1))/2 for j>=1,
    b_(2j+1)=r w s^j d_j(s), B_j=0 outside0,...,M-1.

Here L>0, kappa>1 and each B_j is a polynomial. These finite formulas are smooth on the whole plane and have sublinear growth exponent1-1/kappa. Fix n>=1, set q=2kappa(n-1), and write the finite polynomial

    H_n(1-w)=d_n(1-w)[2kappa+(1-2kappa)w]=sum_k h_k w^k.

Define another polynomial

    E_n(w)=[d_(n-1)(1-w)+(1-w)d_n(1-w)]/2
                            -n sum_k h_k w^k/(q+k+1),
    P_n(s)=(1-s)^(q+1) E_n(1-s).                         (6)

There is no zero denominator because q>=0. Substitution in(2) gives the exact shell identity

    I_(2n)(lo,hi)=m0^(2-2n)[P_n(s(hi))-P_n(s(lo))].       (7)

To verify every factor, the boundary term in(2) is

    m0^(2-2n) w^(q+1)[d_(n-1)(s)+s d_n(s)]/2.

Also d r/ds=r[1+(2kappa-1)s]/[2s(1-s)], so the integral term in(2) is

    n m0^(2-2n) int_(s(lo))^(s(hi)) (1-s)^q H_n(s)ds.

Integrating its finite expansion in w proves(6)-(7), including the sign from ds=-dw. Since q+1>0, P_n(1)=0. At the origin P_n(0)=E_n(1). Therefore

    I_(2n)(0,infinity)=-m0^(2-2n) E_n(1),
    I_(2n)(r,infinity)=-m0^(2-2n) P_n(s(r)).              (8)

These formulas include both the unresolved core and the infinite exterior, without a finite-box boundary condition. They also telescope over every partition. They agree with result96 because

    -E_n(1)=n int_0^1 (1-s)^q d_n(s)[1+(2kappa-1)s]ds
                                                  -d_(n-1)(0)/2
            =4n p_(n,n-1).

For exact rational input coefficients and kappa the polynomial E_n and the last normalized total are rational. General endpoint powers and physical scale factors are retained symbolically; their displayed numerical values are multiprecision approximations. In particular, the stored binary kappa must not be replaced by a nearby rational with a smaller denominator.

## 3. Scaling, verification, and scope

Under the genuine profile scaling rho_lambda(X)=lambda rho(X/lambda), b_lambda(r)=lambda b(r/lambda) and f_lambda(r)=f(r/lambda). A radial substitution gives

    I_(2n),lambda(lo,hi)=lambda^(2-2n) I_(2n)(lo/lambda,hi/lambda).

The strain moment n=1 is invariant. For n>=2 a comparison at fixed physical radii and a comparison on rescaled radii answer different questions and must be labeled separately.

The independent implementation must: compare(7) with adaptive integration of(1), computing the source by direct differentiation of the original Chebyshev density modes; compare the total with result96; test telescoping and both endpoints; and report sensitivity to working precision. Polynomial cancellation at high radial degree requires additional precision. The sum of absolute signed shell contributions is only a lower bound on the integral of the absolute source weight; no equality is implied. Neither these moments nor finitely many Taylor coefficients establish convergence to a finite-regularity or smooth profile.

Dependencies: elementary Fourier identities, the canonical radial Green formula with its displayed endpoint estimates, and the finite Q representation of result96. Verification evidence and actual independent model review are pending at creation.
