# Axis finite-part compatibility and the topology needed to control it

Status: analytical obstruction and conditional continuity estimate. These results concern the topology of an axis functional, not nonexistence of a profile.

## Definition and hypotheses

For R>0 and g(x)=x^2 a(x)>0 on (0,R], suppose a is continuous at zero, a(0)=1, and a(x)-1=O(x^{1+alpha}) for some alpha>0. Define

D(g,R)=integral_0^R [1/g(x)-1/x^2] dx - 1/R.

The displayed integral is absolutely convergent, since its integrand is O(x^{alpha-1}). By ../local_geometry/PROOF.md, every exact normalized canonical P_2 profile has this rate on the positive axis when g stays positive. If R is a positive-axis source of the exact rescaled field, then D(g,R)=0. The rate is a consequence of the PDE and canonical regularity, not of continuous center factorization alone.

## Discontinuity in natural ambient norms

Let rho_0 be a fixed normalized even-x, odd-y trial that is C^{2,alpha} locally, with positive axis derivative g_0=x^2 a_0 and a_0(x)=1+O(x^2) near zero. X3 has these properties on the axis. Choose a nonzero, nonnegative C^3 radial cutoff chi supported in [1,2]. For 0<delta<1, define

h_delta(x,y)=epsilon_delta x^2 y chi(r/delta), epsilon_delta=delta^{1/2}.

It is zero near the origin, so the exact normalized center factor is unchanged. For F(X)=x^2 y chi(|X|),

h_delta(X)=epsilon_delta delta^3 F(X/delta).

Hence each derivative of order j<=2 has supremum epsilon_delta delta^{3-j} times the fixed corresponding supremum of F. The order-two alpha-Hoelder seminorm is exactly epsilon_delta delta^{1-alpha}[D^2F]_alpha. Thus h_delta tends to zero in C^{2,alpha} for every 0<alpha<1. It also tends to zero in the weighted factor norm sup |h|/[x^2|y|W(r)] for every fixed continuous positive radial W near zero. Its support shrinks to the origin, so it tends to zero in any of the usual fixed polynomially weighted versions of these norms. Its strain is O(epsilon_delta delta^2): in the exact density formula psi[h]_{xy}(0)=(1/pi) integral h(X) sin(3theta)r^{-3} dX from ../canonical_inverse/PROOF.md, substitution X=delta Z gives factors epsilon_delta delta^3, delta^{-3}, and delta^2 respectively. The fixed annular integral is finite.

Nevertheless, write g_delta=g_0+epsilon_delta x^2 chi(x/delta). For fixed R>0 and 2delta<R,

D(g_delta,R)-D(g_0,R)
=-(epsilon_delta/delta) integral_1^2 chi(t)/[t^2 a_0(delta t)(a_0(delta t)+epsilon_delta chi(t))] dt.

The integral tends to C_chi=integral_1^2 chi(t)/t^2 dt>0 by uniform convergence of a_0(delta t) to one and elementary domination. Therefore this difference is asymptotic to -C_chi delta^{-1/2}, and tends to minus infinity. Each member individually has a finite D, because its correction vanishes in a neighborhood of zero. No loss of positivity or normalization is used.

Consequently D is not continuous on the ambient normalized factor-plus-C^{2,alpha} space, even at the explicit X3 axis data. It cannot be bounded by those norms alone. This does not contradict an estimate on exact solutions with a uniform PDE-derived center rate, which is a smaller class.

## An explicit interval illustration

Take chi(t)=256(t-1)^4(2-t)^4 on [1,2] and zero outside. This is C^3 across the support endpoints and 0<=chi<=1. For an axis base g_0=x^2 on [0,1], take 2delta<min(1,R) and epsilon_delta<=1. All listed dyadic examples satisfy 2delta<1; choose any fixed R>=1. Then

-C_chi epsilon_delta/delta
<=D(g_delta,R)-D(g_0,R)
<=-C_chi epsilon_delta/[delta(1+epsilon_delta)].

The constant C_chi is an exact rational plus a rational multiple of log(2), found by expanding the degree-eight polynomial and integrating its coefficients divided by t^2. The accompanying Arb and independent mpmath.iv computation checks these explicit divergence bounds. This illustration uses the exact quadratic axis base locally; the preceding argument proves the same divergence asymptotic for X3 without assuming its coefficients are exactly quadratic.

## Stronger ambient discontinuity

The same cutoff is C^{3,1}, since its fourth derivative is piecewise bounded and its third derivative matches continuously at both endpoints. Thus F is C^{3,1} with compact support. For any fixed 0<beta<1 choose epsilon_delta=delta^theta with beta<theta<1. Then the C^{3,beta} seminorm scales as epsilon_delta delta^{-beta}, which tends to zero, while the finite-part change is asymptotic to -C_chi epsilon_delta/delta, which diverges. The ambient obstruction therefore also holds in every C^{3,beta} topology with beta<1, together with the same factor norm. This remains a statement about arbitrary trial perturbations, not exact solutions.

## Conditional Hoelder continuity with a uniform center rate

Let g_i=x^2 a_i, i=1,2, on (0,R], with a_i>=m>0,

|a_1-a_2|<=epsilon,
|a_1-1|+|a_2-1|<=C x^{1+alpha}, alpha>0.

Then

|D(g_1,R)-D(g_2,R)|
<=m^{-2} integral_0^R min(epsilon,C x^{1+alpha})/x^2 dx
<=m^{-2}(1+1/alpha) C^{1/(1+alpha)} epsilon^{alpha/(1+alpha)}.

For positive C and epsilon, split the integral at d=(epsilon/C)^{1/(1+alpha)} and enlarge the upper endpoint to infinity if necessary. The two terms are C d^alpha/alpha and epsilon/d. If either parameter is zero, the bound follows directly. This proves the stated estimate for all R without requiring d<R. The common rate constant C is essential, as the preceding counterexample shows.

If the endpoints R_1,R_2 also vary in [Rmin,Rmax] with Rmin>0, and g>=m x^2 on that interval, then dD/dR=1/g(R), so the endpoint change is bounded by |R_1-R_2|/(m Rmin^2).

## Quantitative origin rate from an exact axis equation

For an exact profile write A=2c_l-1>0 and w(x)=-Ax+e(x). Suppose |e(x)|<=M x^{2+alpha}, |e'(x)|<=M x^{1+alpha}, and M x^{1+alpha}<=A/2 for 0<x<=r_0. The exact axis identity gives

(log(g/x^2))'=(x e'-2e)/(xw).

Its absolute value is bounded by (6M/A)x^alpha. Since g/x^2 tends to one, integration yields

|log(g(x)/x^2)|<=6M x^{1+alpha}/[A(1+alpha)].

Put C_log=6M/[A(1+alpha)]. Then |g/x^2-1|<=C_log exp(C_log r_0^{1+alpha})x^{1+alpha}, by |exp(u)-1|<=|u|exp(|u|). For two profiles, sum the corresponding constants to obtain C in the continuity estimate. This provides explicit upper and lower rates for the axis factor if M and A are controlled in the intended solution ball. Merely knowing that each exact solution is P_2 does not supply a common numerical M.

## A residual identity and its limitation

Assume the absolute convergence hypotheses for D from the definition. Let g>0 and w be sufficiently regular, let A=2c_l-1, and suppose w(R)=0. Define the differentiated axis residual

E_axis=w g'+(2c_l-w'-1)g.

Assume w(x)/g(x)=-A/x+o(1) at zero and E_axis/g^2 is integrable there. Direct differentiation gives

(w/g)'=A/g-E_axis/g^2.

Integrate from d to R, subtract A/d, and let d tend to zero. The result is

A D(g,R)=integral_0^R E_axis(x)/g(x)^2 dx.

Thus a small sampled axis residual does not control finite-part compatibility without the integrability and weighted integral bound shown here. The identity can be used to audit a future residual norm. No claim of linear invertibility, compactness, or nonlinear closure is made.

## Dependencies and scope

The only imported results are the exact axis equation and normalization, already independently derived, and the local smoothness of the X3 axis factor. All discontinuity and continuity arguments are proved above. The perturbations are admissible ambient trial variations, not exact PDE solutions. This distinction prevents a method-specific obstruction from being misreported as exclusion of the X3 branch.
