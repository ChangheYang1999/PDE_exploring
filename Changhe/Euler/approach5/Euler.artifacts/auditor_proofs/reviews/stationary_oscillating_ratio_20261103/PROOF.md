# Three stationary flows with flat pressure-ratio oscillation

## 1. Statements and distinct scopes

Write E=|v|^2, H=E/2-P and R=E/H where H>0. The following three existence statements are CONFIRMED.

1. There is a globally smooth bounded stationary incompressible Euler flow, flat on the third axis, with zero helicity and curl v.grad(P-E/2)=0. Near the axis P>0 and 2<R<=4, with liminf R=2, limsup R=4 and infinite transverse logarithmic Dirichlet energy in every small punctured disk.
2. There is such a globally smooth bounded zero-helicity stationary flow with velocity supported in a cylindrical annulus. At its outer cylinder both velocity and pressure are flat and zero outside. Inside a collar, P<0 and 1<=R<2, with liminf R=1, limsup R=2 and infinite logarithmic Dirichlet energy in every small meridional rectangle meeting the cylinder.
3. There is a globally smooth compactly supported stationary flow and pressure, flat at a toroidal support boundary. In its inner collar P<0 and 2/3<R<2, with liminf R=1, limsup R=2 and infinite logarithmic energy in the transverse coordinate rectangles defined below. It has curl v.grad(P-E/2)=0 but strictly positive helicity on that collar.

Each satisfies div v=0 and (v.grad)v+grad P=0. None is a rotating similarity profile for any c>0 and any finite omega, even with a new single-valued pressure. The first two do not decay in the third direction; the last is compact but has nonzero helicity. They do not satisfy the actual coupled-tail assumptions of A1502. The third construction uses Gavrilov's local stationary existence theorem. The first two are elementary. No computation or formal build was used.

## 2. Positive-pressure axis construction

For s>1 set b=4+s^2 sin^2(s) and g=4s+integral_1^s t^2 sin^2(t)dt. The exact primitive is

    t^3/6-t^2 sin(2t)/4-t cos(2t)/4+sin(2t)/8.

Thus g'=b and g=s^3/6+O(s^2), in particular g>=s^3/12 for large s. With rho=e^-s, put I=e^-g and a=sqrt(bI). Then rho I'=bI=a^2. Since I vanishes at0,

    I(rho)=integral_0^rho a(t)^2/t dt.

Every derivative in s of b and g is polynomially bounded. Derivatives of sqrt(b) are also polynomially bounded since b>=4. Each rho derivative adds exponential factors e^s. Hence all derivatives of a/rho and I are bounded by polynomial factors times exp(C_j s-g/2), and vanish faster than any power of rho. The fields

    v=(a/rho)(-x2,x1,0)=a e_theta, P=I

extend smoothly and flatly through the axis.

For any smooth radial a, cylindrical differentiation gives div v=0, (v.grad)v=-a^2 e_rho/rho and curl v=(a'+a/rho)e3. Here grad P=a^2 e_rho/rho, proving stationary momentum. The velocity and curl are orthogonal, and curl v annihilates every scalar independent of x3, including P-E/2.

Cut off a smoothly between rho=e^-2 and e^-1, with the cutoff flat at its endpoints. Define the global pressure by the same integral from0 using the cut-off a. Velocity vanishes outside the outer cylinder and pressure is constant there. Both are smooth and bounded. The unchanged inner primitive is I, so the following exact local formulas survive.

## 3. Positive-pressure ratio and its energy

Here E=bI, H=(b/2-1)I and R=2b/(b-2), giving 2<R<=4. At s_n=n pi, b=4 and R=4. At s=pi/2+n pi, b tends to infinity and R tends to2. These and the bounds give the exact limsup and liminf.

Furthermore

    (log R)'_s=-2b'/[b(b-2)],
    integral_(rho<epsilon) |grad log R|^2 dx1 dx2
       =2pi integral_(log(1/epsilon))^infinity |(log R)'_s|^2 ds.

For large n use I_n=[s_n+1/(2s_n),s_n+1/s_n]. If t=s-s_n, then sin t>=t/2, cos t>=1/2, s_n<=s<=2s_n, b<=8, and

    b'=2s sin^2s+2s^2 sin s cos s>=s_n/4.

Thus |(log R)'_s|>=s_n/96. The interval width is1/(2s_n), so its integral is at least s_n/18432. The disjoint interval contributions have divergent sum. Both numerator and denominator are smooth flat functions; their ratio need not extend continuously or have finite logarithmic energy.

## 4. Negative-pressure zero-helicity cylinder

Near the inner side of rho=1 set delta=1-rho, s=log(1/delta), rho(s)=1-e^-s and

    b=2e^-s/rho+s^2 sin^2s, g=integral_1^s b(t)dt,
    I=e^-g, L=e^s b=2/rho+e^s s^2 sin^2s,
    a=sqrt(rho L I), v=a e_theta, P=-I.

Now I_delta=L I and P_rho=I_delta=a^2/rho, so the stationary identities of Section2 apply. The first term in b is integrable as s tends to infinity, while the same oscillatory primitive gives g>=s^3/12 eventually. The prefactor rho L=2+rho e^s s^2 sin^2s is bounded below by2. Each derivative of it or its square root is at most an exponential times a polynomial. The e^-g/2 factor dominates every derivative and every power of delta. Thus the field and pressure extend smoothly and flatly by zero through rho=1.

Choose a cutoff supported in a smaller collar with rho>rho1>1-e^-1 and equal to1 near rho=1. After multiplying a by this cutoff define

    P(rho)=-integral_rho^1 a(t)^2/t dt for rho<1,
    P=0 for rho>=1.

It agrees with -I in the outer collar, is constant in the inner cylinder where velocity is zero, and gives globally smooth bounded fields. In particular the axis causes no coordinate singularity. Zero helicity and the scalar vorticity identity hold everywhere.

Put A=rho L/2=1+(rho/2)e^s s^2 sin^2s. Then E=2AI, H=(1+A)I and R=2A/(1+A). Thus 1<=R<2. At s_n=n pi it equals1, and at s=pi/2+n pi it tends to2. On the exterior zero side H=v=0; the ratio is asserted only on the active side.

## 5. Cylinder logarithmic energy

In any meridional rectangle of positive z-length crossing rho=1, the energy equals that length times

    integral_0^epsilon |(log R)'_delta|^2 ddelta
       =integral_(log(1/epsilon))^infinity e^s |(log R)'_s|^2 ds.

Let epsilon_n=e^(-s_n/2)/s_n and I_n=[s_n+epsilon_n/2,s_n+epsilon_n]. For all large n, rho>=1/2, s<=2s_n, e^s<=e e^s_n and elementary sine bounds give

    1<=A<=1+2e,
    A'>=rho e^s s^2 sin s cos s
       >=e^(s_n/2)s_n/16.

The other derivative terms are nonnegative on these intervals. Since (log R)'=A'/[A(1+A)], it is at least C e^(s_n/2)s_n for one fixed C>0. Multiplying its square by e^s and the interval width gives a contribution at least C^2 e^(3s_n/2)s_n/2. The sum diverges. A smooth nonsingular change of transverse coordinates preserves divergence of this energy through uniform metric comparison.

## 6. Gavrilov source and compact modulation

The actual seven-page arXiv1810.08020v1 manuscript was read in full, including the analytic ODE, partial differential construction, local minimum, flow formulas, modulation and energy relation. Its cited local existence theorem provides smooth stationary u,p off a circle, in a small tubular neighborhood, such that

    div u=0, (u.grad)u=-grad p, u.grad p=0, |u|^2=3p.

The transverse minimum of p is nondegenerate and zero on the circle. Thus sufficiently small positive pressure levels are smooth tori and grad p is nonzero near each. The field itself need not be smooth on the omitted circle. No regularity of that unmodulated field there is assumed. The source existence theorem, including its analytic ODE theorem, remains an explicitly cited dependency.

If chi is a smooth function of p and Q'=chi^2, direct differentiation shows div(chi u)=0 and ((chi u).grad)(chi u)=-chi^2 grad p=-grad Q. Fix a sufficiently small regular level p0>0, set delta=p0-p, s=log(1/delta), K=2/(3p0), and

    b=K e^-s+s^2 sin^2s, g=integral_1^s b,
    I=e^-g, L=e^s b=K+e^s s^2 sin^2s,
    chi=sqrt(LI), P=-I, v=chi u.

Since I_delta=LI, P_p=chi^2. The modulation identity gives stationary Euler. Exactly the derivative estimates in Sections2 and4 prove smooth flat extension through the outer level p=p0; L>=K keeps all square-root denominators controlled.

Cut off chi toward a smaller positive p1, keeping it unchanged near p0 and zero below p1. Set Q(p)=-integral_p^p0 chi(t)^2dt. It is constant below p1 and zero above p0. Extend its inner constant through the inner solid torus, set v=0 there, and extend both fields by zero outside the outer torus. Flat endpoints make the patches smooth. Both fields have compact support in R3 and velocity is nonzero immediately inside the outer torus. The additive pressure gauge is fixed by zero on the outer side.

## 7. Compact ratio, energy and scalar transport

On the outer collar E=3pLI, H=(1+3pL/2)I and R=2A/(1+A), A=3pL/2. Restrict to p0/2<p<p0. Since L>=K, A>1/2 and 2/3<R<2. At s_n=n pi, A=p/p0 tends to1 and R tends to1. At the half-period sequence A tends to infinity and R tends to2. The lower bound A>=p/p0 also proves liminf R>=1, so these two limits are exact.

Choose local coordinates (delta,z1,z2) at any point of the outer torus, and fix one tangential coordinate. The resulting smooth transverse two-dimensional rectangle has a uniformly comparable metric and area density. Since R depends only on delta, its logarithmic Dirichlet energy is bounded below by a positive multiple of integral e^s |(log R)'_s|^2ds. On the same narrow I_n as Section5,

    K<=L<=K+4e,
    L'>=e^(s_n/2)s_n/4,
    A'=(3/2)(e^-s L+pL')>=C0 e^(s_n/2)s_n.

A and1+A are uniformly bounded there. The lower bound of Section5 applies and gives divergence on every such smaller rectangle.

The stationary Lamb identity is u cross curl u=grad(p+|u|^2/2)=(5/2)grad p. Dotting with curl u yields curl u.grad p=0. Also curl(chi u)=chi curl u+chi' grad p cross u, which annihilates grad p. Since P-E/2 is a function of p, the scalar vorticity identity is valid. It does not imply zero helicity.

## 8. Exact nonzero helicity of the compact example

Normalize the circle radius to1. The source formulas on printed p5 read

    u_rho=p_z/rho, u_z=-p_rho/rho, u_theta=B(p)/rho.

Its functions give B(p)=sqrt(p)(1+O(p)), with an analytic expansion multiplying sqrt(p) for p>0. Indeed its H(alpha)=6alpha(1/psi'(alpha)+2psi(alpha)) has leading4alpha, p=alpha/4 and B=sqrt(H(4p))/4. The poloidal part of curl u is -B' times the poloidal part of u. The Lamb identity fixes the remaining component, giving

    curl u=-B' u+(5/2)rho e_theta,
    u.curl u=-3p B'+(5/2)B=sqrt(p)+O(p^(3/2))>0

for sufficiently small positive p. Multiplication by chi yields v.curl v=chi^2 u.curl u. It is strictly positive throughout the active collar. This is an actual failure of the zero-helicity hypothesis, not an unverified possibility.

## 9. Failure of the full profile equation for all rotation rates

For either cylinder swirl, rotational equivariance gives (Jx.grad)v=Jv. Subtract stationary momentum from the rotating profile equation. The resulting vector to be balanced by a new pressure gradient is

    [(1-c)a+c rho a'] e_theta.

Its circulation on each complete circle is 2pi rho times its coefficient, so any globally single-valued new pressure forces that coefficient to vanish. For the positive-pressure axis example,

    rho a'/a=(b-b'/b)/2=2 at s=n pi,

and the coefficient is (1+c)a!=0 for every c>0. For the negative-pressure cylinder example, the coefficient vanishing throughout the collar would force a=C rho^(-(1-c)/c), whose smooth vanishing at rho=1 forces C=0. This contradicts a>0 inside. As a further target-range check, at s=n pi its coefficient is (1-2c)a. Both swirl fields keep nonzero speed along every vertical line at an active radius, so fail whole-space decay. Their boundary or axis amplitudes also violate twisted homogeneity.

For the compact stationary example, subtracting stationary momentum and taking curl under a hypothetical profile equation yields

    Omega+(cx-omega Jx).grad Omega+omega J Omega=0.

Along x(t)=e^(ct)e^(-omega tJ)x0 this integrates to Omega(x(t))=e^-t e^(-omega tJ)Omega(x0). For every x0!=0 the trajectory leaves the compact support at a finite positive time, forcing Omega(x0)=0. Continuity gives the same at0. A divergence-free, curl-free compactly supported field has harmonic components and is zero, contradicting the construction. This obstruction holds for every c>0 and all finite omega, independently of the pressure gauge.

## 10. Consequence and unresolved problem

These examples refute a general inference of finite logarithmic ratio energy from smooth flatness, incompressibility, scalar vorticity compatibility, bounded positive ratio and stationary momentum. The first two retain zero helicity. The third retains compact spatial support. Their different favorable properties cannot be combined as properties of one field.

None has all the actual twisted-homogeneity, coupled scalar, rank and isolated-orbit assumptions of A1502. None realizes the negative incompressible endpoint R<=2/3 on a full neighborhood. The endpoint question, the actual coupled continuation problem and the main smooth decaying rotating-profile conjecture remain OPEN.
