# Physical IPM scaling and the unavoidable unbounded far field

Status: independently checked. Date: 2026-10-20.

## Exact statement

Assume an exact nonzero smooth profile on the plane satisfies

    (ell X+U).grad rho=rho, U=(-psi_y,psi_x), -Delta psi=rho_x,
    ell>1, U=o(r), rho even in x and odd in y,
    |rho|+(1+r)|grad rho|<=C(1+r)^gamma, 0<gamma<1.

For the primary assertion also assume a0=rho_y(0)!=0. Put p=1/ell, alpha=1/(ell-1), beta=ell/(ell-1). For any fixed real T and t<T set tau=T-t, X=Z/tau^beta, and

    varrho(t,Z)=alpha*tau^alpha*rho(X),
    u(t,Z)=alpha*tau^alpha*U(X),
    Psi(t,Z)=alpha*tau^(alpha+beta)*psi(X).

These are smooth local-in-space solutions of the physical whole-plane IPM equations

    partial_t varrho+u.grad_Z varrho=0,
    u=(-Psi_z2,Psi_z1), -Delta_Z Psi=varrho_z1.

For a primary profile,

    varrho_z2(t,0)=alpha*a0/(T-t),              (1)

so its absolute value diverges as t tends to T from below. This is a conditional implication from an exact profile, not a proof that one exists.

Every nonzero exact profile in this growth class, and every varrho(t,.) at a finite t<T, is unbounded and fails to belong to Lq(R2) for every finite q>0. Thus this construction cannot by itself supply bounded or compactly supported initial density. The conclusion is stronger than saying that the admissible class merely allows unbounded density.

Let rho_infinity(R,theta)=R^p Theta_0(theta), with the nonzero angular limit proved in ../nonzero_far_field/PROOF.md, and rho_infinity(0)=0. Then

    varrho(t,.) -> alpha*rho_infinity

locally uniformly on the physical plane as t tends to T. The limit is locally Holder-p. Its leading far-field amplitude is independent of time. No convergence of gradients away from the origin is asserted under the primary hypotheses alone.

## Direct equation check

The elementary exponent identities are beta=alpha+1, beta=ell*alpha and beta*p=alpha. Differentiation at fixed Z gives

    partial_t varrho=alpha*tau^(alpha-1)
                        [-alpha*rho+beta*X.grad rho],
    u.grad_Z varrho=alpha^2*tau^(2alpha-beta)*U.grad rho.

Since 2alpha-beta=alpha-1, their sum equals

    alpha^2*tau^(alpha-1)*[(ell X+U).grad rho-rho]=0.

The spatial gradient of Psi is alpha*tau^alpha times the profile gradient of psi. Its Laplacian and the first derivative of varrho both acquire alpha*tau^(alpha-beta), so the Poisson equation holds with the stated sign. Finally alpha-beta=-1 gives (1). All formulas use the same full-plane canonical velocity, with no harmonic addition.

More generally, for any approximate canonical pair the physical transport defect is exactly alpha^2*tau^(alpha-1) times the profile residual at X. A small sampled profile residual therefore is not an exact physical solution.

## Nonzero tails and lack of finite Lq norms

The far-field theorem gives uniform convergence r^(-p)rho(r,theta)->Theta_0(theta), with Theta_0 continuous and nonzero. There is a closed angular arc of positive length and a number c>0 on which |Theta_0|>=2c. Uniform convergence gives |rho(r,theta)|>=c*r^p on that arc for all sufficiently large r. Consequently the integral of |rho|^q dominates a positive constant times integral_R^infinity r^(pq+1)dr, which diverges for every q>0. The same lower bound proves unboundedness. The physical dilation and multiplication at any fixed positive tau preserve these conclusions.

The leading physical amplitude equals

    alpha*tau^alpha*(R/tau^beta)^p Theta_0
       =alpha*R^p Theta_0,

because beta*p=alpha. Thus no time slice in this exact similarity family becomes bounded at spatial infinity. Localization or stability arguments would be additional work.

## Limiting physical profile

The uniform far-field limit implies convergence of varrho to alpha*rho_infinity uniformly on any compact physical annulus bounded away from zero. The global estimate rho=O((1+r)^p), already proved together with the canonical p-growth, gives

    |varrho(t,Z)|<=C_alpha*(tau^alpha+|Z|^p).

This proves uniform smallness on a small physical ball when tau is small. Combining the ball and annular estimates establishes local uniform convergence on the whole plane.

To check Holder-p regularity, choose an angular exponent q with p<q<1. The angular theorem gives Theta_0 in C^q. For two points X,Y with |X-Y| at least half their larger radius, homogeneity bounds their value difference by C|X-Y|^p. Otherwise their radii are comparable, radial power differences are bounded by C|X-Y|^p, and their angular difference is at most C|X-Y|/r. The angular contribution is bounded by

    C*r^p*(|X-Y|/r)^q <= C*|X-Y|^p,

since |X-Y|<r and q>p. This proves the asserted local Holder-p bound, including the origin. The proof makes no derivative-asymptotic claim.

For completeness, for every 0<q<1 the established angular-scattering estimate gives rho(r,theta)-r^p Theta_0(theta)=O(r^(p-q*(1-p))). On a fixed physical annulus, the corresponding error in varrho is O(tau^q), because beta*(1-p)=1. The constant can depend on the annulus and q. This rate is not a C1 estimate and cannot be differentiated without further hypotheses.

## Scaling covariance and scope

The genuine profile scaling rho_lambda(X)=lambda*rho(X/lambda) produces varrho_lambda(t,Z)=lambda*varrho(t,Z/lambda). It leaves the center gradient (1) unchanged, just as it leaves a0 and ell unchanged. This provides a direct check that a gauge representative cannot alter the invariant blowup coefficient alpha*a0.

Dependencies are the defining PDE, elementary differentiation, the canonical scaling theorem, and the separately proved nonzero/Holder far-field results. No bounded-data or compact-support blowup theorem, no primary numerical endpoint, and no assertion about existence is established here.
