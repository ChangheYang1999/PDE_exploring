# Bessel multipliers preserve a differentiated power tail

Status: new analytic lemma, OPEN pending an independent theory review. This fills the unproved Bessel-factor sentence in T2's the review of T4-094, addition A4. It does not certify any numerical coefficient.

## Exact statement

Let f be a smooth scalar function on R2. Suppose that for a real e and every multi-index nu there is a finite C_nu with

    |partial^nu f(X)| <= C_nu <X>^(e-|nu|),
    <X>=(1+|X|^2)^(1/2).                                 (1)

Define J^s=(1-Delta)^(s/2) as a Fourier multiplier on tempered distributions. For every s>=0 and every nu,

    partial^nu(J^s f-f)=O(<X>^(e-|nu|-2)).                 (2)

For s=0 the left side is zero. If additionally, for some d>0, f has a differentiated asymptotic expansion

    f(r,theta)=r^e H(theta)+O(r^(e-d)),                    (3)

with smooth H, then J^s f has the same leading term, with differentiated error of order r^(e-min(d,2)).

Suppose for an integer k>=0 the tensor D^k(r^e H) is not identically zero. For every positive locally bounded weight w that is bounded above and below on compact sets and comparable to r^p at infinity,

    ||w D^k J^s f||_2 < infinity  iff  p < k-1-e.        (4)

The exact endpoint p=k-1-e diverges logarithmically. The nonzero tensor hypothesis is necessary; a polynomial leading term may be annihilated by D^k.

## The heat representation for 0<s<2

Write alpha=s/2 in(0,1). Elementary integration by parts gives for lambda>=0

    (1+lambda)^alpha-1
      =[alpha/Gamma(1-alpha)]
        int_0^infinity exp(-t)(1-exp(-lambda t))t^(-1-alpha)dt. (5)

To verify the constant, integrate the difference of exp(-t) and exp(-(1+lambda)t) against t^(-1-alpha). Boundary terms vanish at both endpoints. The remaining integral is Gamma(1-alpha)[(1+lambda)^alpha-1]/alpha.

Under(1), the heat convolutions exist pointwise. Formula(5), first on Schwartz test functions and then by distributional duality, yields

    J^s g-g=c_alpha int_0^infinity exp(-t)
                          (g-exp(t Delta)g)t^(-1-alpha)dt,
    c_alpha=alpha/Gamma(1-alpha).                         (6)

The bounds below show absolute pointwise convergence with all derivatives, and justify exchanging the integrals against Schwartz tests. Thus(6) defines the same smooth function as the tempered-distribution multiplier. No asymptotic assertion is inferred from the multiplier's low-frequency Taylor series alone.

## A polynomially weighted heat bound

Fix nu, set g=partial^nu f, beta=e-|nu|-2 and b=|beta|. By(1) there is M with |Delta g(X)|<=M<X>^beta. The elementary Peetre inequality is

    <X+Z>^beta <= 2^(b/2)<X>^beta<Z>^b.                  (7)

For beta>=0 this follows from <X+Z>^2<=2<X>^2<Z>^2. For beta<0 apply the same inequality to X=(X+Z)-Z and invert.

Put C_b=2^(b/2+max(b/2-1,0)). The two-dimensional Gaussian with density (4pi t)^(-1)exp(-|Z|^2/(4t)) has b-th radial moment (4t)^(b/2)Gamma(1+b/2). Together with (1+u)^(b/2)<=2^max(b/2-1,0)(1+u^(b/2)), this proves

    |exp(t Delta)Delta g(X)|
      <=M C_b <X>^beta [1+(4t)^(b/2)Gamma(1+b/2)].       (8)

The heat equation, justified by differentiating the Gaussian convolution, gives

    exp(t Delta)g-g=int_0^t exp(tau Delta)Delta g dtau.

Substitute(8) into this identity and then into(6). Every resulting scalar integral is finite. More explicitly,

    |J^s g-g| <= M C_b c_alpha <X>^beta
       [Gamma(1-alpha)
        +4^(b/2)Gamma(1+b/2)Gamma(1+b/2-alpha)/(1+b/2)].   (9)

All gamma arguments are positive. This proves(2) for0<s<2, with an explicit coefficient. The same calculation for all nu justifies smoothness and commutation with derivatives.

## General s and the membership threshold

For s=2m+sigma, m a nonnegative integer and0<=sigma<2,

    J^s f=(1-Delta)^m J^sigma f.

The sigma result gives J^sigma f=f+g, where all derivatives of g decay two powers faster than the corresponding derivatives of f. Expanding the finite polynomial(1-Delta)^m shows that J^s f-f is a sum of derivatives of f of orders at least2 and of derivatives of g of nonnegative even orders. Each has the bound in(2). This also covers sigma=0 directly.

Apply(2) to the differentiated expansion(3). The nonzero leading derivative tensor is homogeneous of degree e-k. Its angular norm is continuous and is bounded below by a positive number on some open angular interval. The error in that tensor decays by min(d,2)>0. Hence on that interval, for all large r,

    |D^k J^s f| >= c r^(e-k).

The global upper bound has the same power. After multiplying by w^2 and the polar Jacobian r, the tail integral is comparable above and below to int r^(2(p+e-k)+1)dr. It converges precisely when its exponent is below-1. Smoothness gives the finite compact-region contribution, proving(4).

## Scope for the campaign

For a finite canonical rational-power profile or residual, the required differentiated polynomial bounds follow once the exact first surviving sector and its nonzero angular coefficient are established. Then a Bessel gain s>0 does not remove an inadmissible far-field sector. Conversely it does not introduce a new leading far-field sector. The result applies to the same scalar function and canonical full-plane multiplier; it does not compare norms under a finite-box discretization.

Dependencies: elementary gamma integration, Gaussian moments, the heat equation identity, distributional Fourier duality, and the stated global derivative bounds. No existence, spectrum, or nonlinear mapping theorem is invoked.
