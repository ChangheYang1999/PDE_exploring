# Exact higher center jets of the finite Q representation

Result96. Written2026-10-21 before the implementation. Scope: exact Taylor coefficients of the saved finite Q density and its canonical full-plane velocity, and the resulting transport residual. This is an evaluator identity, not a profile construction or a convergence theorem.

## 1. Representation and statement

Let ell>1, kappa>1 and L>0. Let B_j be finite real polynomials, j=0,...,M-1, with B_j=0 otherwise. Write

    m0=L*2^(-kappa), z=(r/m0)^2,
    z=s(1-s)^(-2kappa), 0<=s<1, w=1-s,
    rho=y w sum_(j=0)^(M-1) s^j B_j(s) cos(2j theta).

The saved data specify B_j(s) in the Chebyshev basis T_k(2s-1). All rational claims below concern the exact stored binary coefficients and rational ell,kappa,L, without rounding or normalization repair. The letter m0 denotes a physical length, not a moment exponent or an angular index.

The map s->s(1-s)^(-2kappa) is strictly increasing from0 to infinity, with derivative1 at0. Its inverse s(z) is analytic near0, with s(0)=0. Define

    d_0(s)=B_0(s)-s B_1(s)/2,
    d_j(s)=(B_j(s)-s B_(j+1)(s))/2, j>=1,
    G_j(s)=s^j(1-s)d_j(s).

Then the density has the finite sine expansion

    rho=sum_j b_(2j+1)(r) sin((2j+1)theta),
    b_(2j+1)(r)=r G_j(s(z)).                            (1)

Let beta_(j,k) be the coefficient of z^k in G_j(s(z)). It is zero for k<j. It is computed by

    beta_(j,0)=G_j(0),
    beta_(j,k)=(1/k)[u^(k-1)] G_j'(u)(1-u)^(2kappa k), k>=1.  (2)

These are exact rational quantities for rational inputs. In normalized coordinates X=m0 Z, define rho_tilde(Z)=rho(m0 Z)/m0 and psi_tilde(Z)=psi(m0 Z)/m0^2. The density Taylor coefficient of R^(2k+1)sin((2j+1)theta) is beta_(j,k).

Let p_(n,k) be the coefficient of R^(2k+2)sin(2n theta) in the canonical psi_tilde. For n>=1, its first possible coefficient is

    p_(n,n-1)=1/4 int_0^1 (1-s)^(2kappa(n-1))
                     d_n(s)[1+(2kappa-1)s] ds
                   -d_(n-1)(0)/(8n).                  (3)

For k>=n,

    p_(n,k)=-[(k-n+1)beta_(n-1,k)+(k+n+1)beta_(n,k)]
                              /[4((k+1)^2-n^2)].       (4)

There is no resonant division: for k=n-1 the source coefficient vanishes, and(3) gives the canonical harmonic coefficient. Equations(1)-(4), Cartesian polynomial multiplication and differentiation determine every desired finite center jet of rho, psi, U=(-psi_y,psi_x), and R=(ell X+U).grad rho-rho. In particular density and residual through degree7 require stream through degree8.

## 2. Local density coefficients

The angular identity sin(theta)cos(2j theta)=[sin((2j+1)theta)-sin((2j-1)theta)]/2 for j>=1 gives(1), with the j=0 term kept separately. Analytic inversion is applicable because the derivative of s(1-s)^(-2kappa) at0 is1.

For completeness, the coefficient formula(2) follows by a contour change of variable, or purely as an identity of formal power series. If z=s/phi(s), phi(s)=(1-s)^(2kappa), then for k>=1 the residue for [z^k]G(s(z)) becomes

    Res G(s) phi(s)^k s^(-k-1)[1-s phi'(s)/phi(s)] ds.

Subtract the residue of the derivative of G(s)phi(s)^k s^(-k). The residue of any formal derivative is zero. The remaining expression is (1/k)Res G'(s)phi(s)^k s^(-k) ds, proving(2). Expanding the generalized binomial series gives finite rational arithmetic for each requested coefficient. Its j-fold zero also proves beta_(j,k)=0 for k<j.

## 3. The canonical harmonic coefficient

For the density modes in(1), differentiation in x yields the actual Poisson source of frequency2n:

    f_(2n)=(b_(2n-1)'-(2n-1)b_(2n-1)/r)/2
                     +(b_(2n+1)'+(2n+1)b_(2n+1)/r)/2.

The full-plane regular inverse, with no homogeneous strain, can be integrated by parts to give

    P_(2n)(r)=1/2 [r^(2n) int_r^infinity b_(2n+1)(u)u^(-2n)du
                         -r^(-2n) int_0^r u^(2n)b_(2n-1)(u)du].  (5)

At infinity the density is O(r^(1-1/kappa)), and its first derivative is O(r^(-1/kappa)); the exponent lies strictly between0 and1. Both integrals in(5) converge at their indicated endpoints. At0 the density modes vanish to the order2j+1 prescribed by(1). This makes(5) regular. The resulting velocity is O(r^(1-1/kappa)), hence sublinear. Harmonic uniqueness with the specified parities identifies it as canonical. The zero source mode is absent by parity. Additive constants in psi have no velocity and the odd-odd stream convention fixes them.

In normalized radius R=r/m0, the exterior moment at0 is

    int_0^infinity beta_density_(2n+1)(R) R^(-2n)dR
       =1/2 int_0^1 (1-s)^(2kappa(n-1))
                         d_n(s)[1+(2kappa-1)s]ds.        (6)

Indeed R=s^(1/2)(1-s)^(-kappa) and dR/ds=R[1+(2kappa-1)s]/[2s(1-s)]. The powers of s cancel in(6). The second term of(5) contributes -d_(n-1)(0)R^(2n)/(8n). The first contributes one half of(6) times R^(2n). This proves(3). Its integral is a polynomial beta moment, with

    int_0^1 s^h(1-s)^q ds=h!/[(q+1)(q+2)...(q+h+1)], q>-1,

which is rational for rational q. This computation evaluates a full-plane moment; it does not choose an arbitrary local harmonic jet.

## 4. Remaining stream and residual jets

The coefficient of R^(2k)sin(2n theta) in rho_tilde,x is

    (k-n+1)beta_(n-1,k)+(k+n+1)beta_(n,k).

For k=n-1 it vanishes: the first factor is zero and beta_(n,n-1)=0. For k>=n, applying -Delta to R^(2k+2)sin(2n theta) multiplies by -4[(k+1)^2-n^2]. This proves(4).

A homogeneous angular polynomial converts exactly to Cartesian coordinates using

    R^(2k+1)sin((2j+1)theta)
        =(X^2+Y^2)^(k-j) Im(X+iY)^(2j+1),
    R^(2k+2)sin(2n theta)
        =(X^2+Y^2)^(k+1-n) Im(X+iY)^(2n).

The powers are nonnegative in every term used. Differentiation and multiplication of these finite Taylor polynomials give residual coefficients through the desired degree. Terms omitted above degree7 in density and degree8 in stream cannot affect the degree<=7 residual: rho has no constant term, psi begins at degree2, and the linear dilation field only preserves homogeneous degree.

Under the length m0, a density or residual coefficient of degree2k+1 is multiplied by m0^(-2k), and a stream coefficient of degree2k+2 is also multiplied by m0^(-2k). The center slope and strain are unchanged. If 2kappa is integral these physical factors are rational for rational L; otherwise the exact factor is retained symbolically and any displayed decimal is an approximation. No uncertain decimal is relabeled exact.

## 5. Verification and limits

The implementation must compare the cubic output with the independently implemented earlier exact-jet evaluator; verify the full Poisson polynomial through the requested order; test radial fields whose stream follows by direct integration; and check higher exterior moments by adaptive high-precision integration of the original Chebyshev formula. Saved-state coefficients, input hashes, code hashes and actual commands must accompany numerical tables. A finite collection of increasing derivatives does not determine the regularity of a limiting profile, and finite sampled residual values do not control these derivatives. Actual Opus review and manufactured tests are pending at the time of this proof's creation.
