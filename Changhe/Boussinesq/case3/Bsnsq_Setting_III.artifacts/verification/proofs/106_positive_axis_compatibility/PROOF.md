# Independent audit of positive axis compatibility

Written UTC: 2026-10-21T02:05:05.671766+00:00
Status: analytic derivation checked independently; own5 symbolic identities and40 numeric axis/Laplace checks passed. Actual Opus139 full written closure review checked; see response for corrections to its abbreviated density prefactor. This is a compatibility construction, not a B2 profile.

## Statement, scope and notation

For every beta>2 and a0>0, the center and axis subsystem of B2 is compatible with a smooth vorticity Omega odd in x, positive for x>0, with Omega=O(r^(-alpha)), a nonzero continuous homogeneous angular limit and a canonical relative full-plane inverse V=O(r^(1-alpha)), where alpha=1/beta. There are smooth functions b,e,H on the axis with e(0)=0,e'(0)=1,e'>0,H>0, b(y) of the sign of y, and

    b=beta y+V2(0,y), b e'=mu e,
    Omega_x(0,y)=H/e', b H'+(beta/2)H=2a0/e',
    V(0)=0, Psi_xy(0)=c, DW(0)=diag(p,mu),
    p=beta/2-1, mu=3beta/2+1, c=1+beta/2.

This neither solves transport away from the axis nor supplies Theta, a global linearizing chart, or absence of off-axis zeros. In particular, it is not an admissible counterexample to any theorem requiring the full B2 equations.

A separate result below rules out one particular positive-weight contradiction for a hypothetical G+ profile. Its hypotheses are explicitly conditional. It does not exhaust possible integral identities.

## Positive axis data

Put ell=mu/beta=3/2+alpha, tau=(ell-1)/2, m=1/(2ell), kappa=tau(1-m), d=1-tau(1+m), s=(1+alpha)/2. Direct algebra gives

    kappa-m/2=alpha/2>0, 1-d+m/2=s<3/4, 0<d<1.

Choose

    e(y)=y(1+y²)^tau,
    b(y)=mu y(1+y²)/(1+ell y²),
    f(y)=b(y)-beta y=c y/(1+ell y²).

Then e'=(1+y²)^(tau-1)(1+ell y²)>0 and b e'=mu e. For a0=1 define

    H*(y)=(2/mu)(1+y²)^(-tau m)
           int_0^1 u^(m-1)(1+y²u²)^(-kappa) du,
    k(y)=H*(y)/e'(y).

The integrable power u^(m-1), with m>0, permits all y derivatives on compact intervals. Thus H* is smooth, even and positive. For y>0 multiplication by e(y)^m reduces the equation to

    (e^m H*)'=(2/mu)e^(m-1).

Integrating from0 to y, substituting v=yu, gives the stated formula. Reflection and continuity extend the identity to y<=0. In particular H*(0)=k(0)=4/beta.

## Positive Laplace density

For z>=0,

    k(sqrt(z))=(2/mu) A(z) B(z),
    A(z)=(1+z)^d/(1+ell z),
    B(z)=int_0^1 u^(m-1)(1+zu²)^(-kappa) du.

The identity needed here has a PLUS sign:

    A(z)=(1/ell)(1+z)^(-(1-d))
         +((ell-1)/ell²)(1+z)^(-(1-d))/(z+1/ell).       (1)

Let g(t)=t^(-d)e^(-t)/Gamma(1-d). The positive density for A is

    a(t)=g(t)/ell+((ell-1)/ell²) int_0^t g(v)e^(-(t-v)/ell)dv.

Using the gamma integral for each (1+zu²)^(-kappa), followed by Tonelli and v=t/u², gives the density for B:

    bD(t)=t^(m/2-1) Gamma(kappa-m/2,t)/(2Gamma(kappa)).

Therefore rho=(2/mu)(a*bD)>0 satisfies

    k(y)=int_0^infinity e^(-ty²)rho(t)dt.

Here all convolutions are on the positive half-line. At zero, a(t)~t^(-d)/(ell Gamma(1-d)), while bD(t)~Gamma(alpha/2)t^(m/2-1)/(2Gamma(kappa)). The beta integral, after rescaling the convolution variable by t, gives

    rho(t)~C_beta t^(s-1), C_beta>0.                    (2)

The factors are bounded above by these powers near zero and have exponential tails times polynomial factors. Splitting their convolution at t/2 proves the same exponential-tail bound for rho. Consequently rho has all nonnegative integer moments and rho(t)<=C t^(s-1) globally.

## Positive vorticity invisible to the axis velocity

For t>0 let

    K_t=x³ T^(-3/4) exp(-w), T=1+4tx²,
    z=4tx²/T in[0,1), w=ty²/T>=0.

Differentiating gives

    Delta K_t=x T^(-3/4)exp(-w) P(z,w),
    P=6-11z+(21/4)z²+z(15-14z)w+4z²w².              (3)

The constant polynomial decreases on[0,1] and is at least1/4; the other coefficients are nonnegative. Also K_tx(0,y)=0 and (Delta K_t)_x(0,y)=6exp(-ty²). Define

    U=(1/6)int_0^infinity K_t rho(t)dt.

The finite moments justify all derivatives on compact sets. Hence U is smooth and odd in x, Delta U>0 for x>0, U_x(0,y)=0, and (Delta U)_x(0,y)=k(y).

For completeness the required estimates are uniform in angle, not just on fixed rays. Direct first derivatives and (3), using 0<=z<=1, show

    |grad K_t|<=C r²(1+tr²)^(-3/4),
    0<Delta K_t<=C x(1+tr²)^(-3/4) for x>0.            (4)

Indeed each extra factor is a fixed polynomial in w times powers of x/r and y/r bounded after using w=ty²/T; for example the y derivative has x³ ty/T=x(4tx²/T)y/4. Absorb every polynomial in w into exp(-w), and use T+ty² comparable to1+tr². Combining (2)-(4), since0<s<3/4, gives for r>=1

    |grad U|<=C r^(2-2s), Delta U<=C x r^(-2s).

Restricting the t integral to[r^(-2),2r^(-2)] gives the reverse inequality Delta U>=c x r^(-2s), uniformly for x>0. Positivity and compactness give on the whole plane

    c x(1+r²)^(-s)<=Delta U<=C x(1+r²)^(-s).           (5)

At x=0 the quotient extends continuously with value k(y)>0, justifying the compact lower bound. On substituting t=v/r² in (3), domination by v^(s-1)(1+v)^(-3/4) gives a uniform continuous angular limit for r^alpha Delta U. To see uniformity explicitly: on a fixed v interval the density factor converges uniformly and the angular integrand is continuous; the two v tails are uniformly small by the common integrable bound. Restricting v to[1,2] proves positivity on the open right semicircle.

## Adding the center strain

Set

    psi_a=cxy/[1+ell(x²+y²)],
    j(y)=4c ell y(3+ell y²)/(1+ell y²)^3,
    psi_c=psi_a+j(y)x³/[6(1+x²)^3].

Direct differentiation gives

    -Delta psi_a=4c ell xy(3+ell r²)/(1+ell r²)^3,
    (psi_c)_x(0,y)=f(y), (-Delta psi_c)_x(0,y)=0.       (6)

The first vorticity in(6) is bounded by C x(1+r²)^(-3/2). For the correction, its x factor h=x³/[6(1+x²)^3] obeys |h''/x|<=C(1+x²)^(-3), |h/x|<=C(1+x²)^(-2), while |j|<=C(1+y²)^(-3/2), |j''|<=C(1+y²)^(-5/2). Each product is bounded by C(1+r²)^(-3/2). Thus

    |-Delta psi_c|<=C x(1+r²)^(-3/2), x>0.

Choose a finite A>0 large enough that (5) dominates this bound, and set

    Psi=psi_c-AU, Omega=A Delta U-Delta psi_c, a0=A.

Then Omega>0 for x>0 and its r^(-alpha) angular limit is that of A Delta U. The axis velocity is f and the axis derivative of Omega is A k. With H=A H*, all stated axis identities hold. Here a0=A is defined by the axis source coefficient in bH'+(beta/2)H=2a0/e', equivalently a0=beta Omega_x(0,0)/4 because k(0)=4/beta. No globally transported temperature is claimed. The derivatives at the origin give the stated center matrix. The velocity V=grad-perp Psi has sublinear growth and V(0)=0.

The canonical relative kernel K(Z)=(Z2,-Z1)/(2pi|Z|²) converges for this Omega: subtraction gives O(|X||Y|^(-2-alpha)) at infinity, integrable in2D. The usual three-region split gives its velocity O(1+r^(1-alpha)). Both this inverse and V have the same distributional curl and divergence. Their difference is an entire harmonic vector field with sublinear growth. Interior derivative estimates on balls of radius R give derivative O(R^(-alpha)); sending R to infinity makes the field constant. Normalization at0 removes that constant. Thus V is exactly the canonical relative inverse, with no affine freedom.

For an arbitrary prescribed a0>0 rescale with L=A/a0:

    Psi_L(X)=L²Psi(X/L), Omega_L(X)=Omega(X/L),
    V_L(X)=L V(X/L), b_L(y)=L b(y/L),
    e_L(y)=L e(y/L), H_L(y)=H(y/L)/L.

All the equations and center strain are preserved and the axis source coefficient becomes A/L=a0. This proves the stated compatibility proposition.

## Scope of a positive transport-weight test

This part assumes a hypothetical G+ profile with a proper smooth area-preserving global linearizing chart (xi,eta), DZ(0)=I, xi_x>0, Theta=a0 xi², Omega>0 for x>0, Omega=O(r^(-alpha)), and V=O(r^(1-alpha)). These are additional assumptions, not properties of the construction above.

On x>0 write xi=e^(pt), eta=z e^(mu t). Area is p e^(2beta t)dt dz. Let f(z)>=0 be smooth, compactly supported and nonzero, and w=e^(-lambda t)f(z). As t->-infinity, the center expansion Omega~(4a0/beta)e^(pt) holds uniformly on compact z sets. Properness and sublinearity imply r comparable to e^(beta t) for large t, uniformly on such sets: a common sufficiently large radius is reached, and dr/dt=beta r+O(r^(1-alpha)); the equation for r^alpha gives both exponential bounds. The upper bound Omega=O(e^(-t)) and monotonicity of e^t Omega, whose derivative is e^t Theta_x>0, give matching positive lower bounds on the compact z set. Therefore

    int_{x>0} Omega w < infinity iff 2beta-1<lambda<2beta+p.

For these lambda the two time boundary terms vanish. Integration on finite time cylinders, then monotone convergence of the positive source, gives

    (lambda+1-2beta) int Omega w = int Theta_x w>0.

This coefficient is positive everywhere the integral is finite. At either excluded endpoint a nonzero boundary contribution or divergence occurs. With H=Omega/xi, its tails are constant and e^(-beta t/2); the identical argument gives

    int H w < infinity iff 3beta/2<lambda<2beta,
    (lambda-3beta/2)int H w=2a0 int xi_x w>0.

These conditional identities exclude one attempted sign contradiction only. They say nothing about sign-changing weights, weights with noncompact trajectory-label support, or other identities using the off-axis inverse and transport simultaneously.

## Dependencies and verification

Dependencies: product and chain rules; elementary gamma/beta integrals; positive Tonelli and dominated convergence; harmonic interior derivative estimates; the explicitly stated hypothetical chart properties in the final section. No existing solver code is used. Own symbolic and value-only numerical checks are stored in verification. The source being audited is lead/astra/gplus1/PROOF.md, read only; the missing plus sign in its displayed Laplace decomposition is a transcription error, not an alternative multiplicative identity.
