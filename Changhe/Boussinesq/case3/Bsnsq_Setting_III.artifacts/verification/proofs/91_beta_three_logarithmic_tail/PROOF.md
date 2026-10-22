# The beta-three third-source resonance and the next scalar terms

Written: 2026-10-20T23:53Z. Status: complete independent derivation, own 30 exact Cartesian checks PASS; actual Opus 5.5 checked section 4 in a written audit and corrected its initial double-counted logarithm after a follow-up. The independent lead review remains pending.
This is a necessary finite-order asymptotic statement for exact class A profiles. No existence or nonexistence endpoint is claimed.

## 1. Statement and notation

Assume a smooth exact class A Setting B2 profile with beta=3 and the canonical relative inverse K(Z)=(Z_2,-Z_1)/(2 pi |Z|^2), as defined in packet90. In particular Omega is odd and Theta is even in x, Theta vanishes on the vertical axis, V(0)=0, and the center temperature normalization is nontrivial. We use exactly the prompt convention: V=(-Psi_y,Psi_x), -Delta Psi=Omega, and omega_t+u.grad omega=theta_x. With tau=-t this is partial_tau omega=u.grad omega-partial_x theta. If a momentum equation is used, its buoyancy in this convention is -theta e_2. Put s=m=1/3. The already proved finite-order dependencies of packets36,38,90 give

    Omega=omega_0+omega_1+omega_2+o(r^-1),
    Theta=theta_0+theta_1+theta_2+o(r^-1/3),
    V=u_0+u_1+o(r^1/3),

with all spatial derivatives on rescaled annuli. Here omega_j has degree -(j+1)/3, theta_j has degree (1-j)/3, and u_j=K_rel omega_j for j=0,1. The coefficients omega_1,theta_1,omega_2,theta_2 are the exact transport expressions in packet90. The leading angular coefficients are smooth and nonzero. Write

    omega_2(r e(theta))=r^-1 A_2(theta),
    alpha=(1/pi) integral_0^(2 pi) A_2(theta) cos(theta) dtheta.

Oddness in x eliminates the angular mean and the first sine harmonic of A_2. Let g be the unique smooth periodic function orthogonal to both first harmonics satisfying

    -(g''+g)=A_2-alpha cos(theta).

Define the smooth vector-valued angular function

    B(theta)=-g' e+g e_perp
                   +(alpha/2)(cos(theta)sin(theta),-cos(theta)^2).

There is a uniquely determined real constant C such that

    w_2(X)=-(alpha/2) log|X| e_2+B(theta)+C e_2,
    V=u_0+u_1+w_2+O_Cj(r^-1/3 log r).                    (1)

For each fixed finite derivative order j, define

    Q_omega=w_2.grad omega_0+u_1.grad omega_1
                                      +u_0.grad omega_2-partial_x theta_2,
    Q_theta=w_2.grad theta_0+u_1.grad theta_1+u_0.grad theta_2,
    omega_3=Q_omega/3-(alpha/6)partial_y omega_0,
    theta_3=Q_theta/3-(alpha/6)partial_y theta_0.           (2)

Then

    Omega=omega_0+omega_1+omega_2+omega_3+O_Cj(r^-5/3 log r),
    Theta=theta_0+theta_1+theta_2+theta_3+O_Cj(r^-1 log r). (3)

The degree -4/3 logarithmic part of omega_3 and degree -2/3 logarithmic part of theta_3 are respectively

    -(alpha/6) log r partial_y omega_0,
    -(alpha/6) log r partial_y theta_0.                  (4)

Both logarithmic coefficients are nonzero functions if alpha is nonzero. Whether alpha is nonzero for any exact profile is not decided. If alpha=0, the displayed big-O estimates remain valid, though they need not be sharp.

## 2. A borderline inverse estimate improves the scalar remainder

Let eta=Omega-omega_0-omega_1. The initial scalar expansion and core smoothness give

    |eta(X)| <= C min(|X|^-2/3,|X|^-1).

Physical fields at t=-tau are u_tau=tau^2 V(tau^-3 z), omega_tau=tau^-1 Omega(tau^-3 z), theta_tau=tau Theta(tau^-3 z). Thus

    |omega_tau-omega_0-tau omega_1|
                          <= C min(tau |z|^-2/3,tau^2 |z|^-1). (5)

Apply the relative inverse to (5). On any compact annulus the evaluation-point singularity, far exterior, and compact set away from zero contribute O(tau^2). The subtraction singularity near zero is bounded by

    integral_0^c min(tau rho^-2/3,tau^2 rho^-1) d rho
                         <= C tau^2 (1+|log tau|),

as is seen by splitting at rho=tau^3. Hence

    u_tau-u_0-tau u_1=O_Cj(tau^2(1+|log tau|)).           (6)

For j=0 the estimate is the kernel split. For higher derivatives use the local interior Poisson estimate on nested compact balls away from zero: the vorticity remainder in (5) has the local O_Ck(tau^2) bound for every finite k from packet90, explicitly |partial^k eta(X)|<=C_k r^(-1-k) for large r; physical rescaling makes this O_Ck(tau^2) on every compact annulus. Its velocity has the C0 bound (6) on a slightly larger annulus. The div-curl equation gives the same bound in every local Cj norm.

The exact physical equations are partial_tau omega_tau=u_tau.grad omega_tau-partial_x theta_tau and partial_tau theta_tau=u_tau.grad theta_tau. Their right sides minus omega_1+2tau omega_2 and theta_1+2tau theta_2 are O_Cj(tau^2(1+|log tau|)), using packet90's third scalar expansion and (6). Integrating from zero gives

    omega_tau=omega_0+tau omega_1+tau^2 omega_2+O_Cj(tau^3(1+|log tau|)),
    theta_tau=theta_0+tau theta_1+tau^2 theta_2+O_Cj(tau^3(1+|log tau|)). (7)

In profile variables, the remainders are respectively O_Cj(r^-4/3 log r) and O_Cj(r^-2/3 log r). All statements concern sufficiently small tau or sufficiently large r, so 1+|log tau| and log r are interchangeable for these estimates. No time derivative of velocity is assumed.

## 3. Exact determination of the logarithmic inverse and its constant

Choose a smooth radial cutoff chi that is zero for r<=1 and one for r>=2. Set

    zeta=Omega-omega_0-omega_1-chi(r)r^-1 A_2(theta),
    L_chi=lim_(R->infinity) [integral_0^R chi(rho)/rho d rho-log R].

By (7), zeta=O(r^-4/3 log r) at infinity and O(r^-2/3) near zero. Therefore its ordinary inverse U_zeta(X)=integral K(X-Y)zeta(Y)dY is absolutely convergent at every X, including zero. The elementary inner/middle/exterior split gives U_zeta(re)=O(r^-1/3 log r), with all scaled derivative estimates by local elliptic regularity. By parity U_zeta(0) is vertical. Each relative source piece is separately absolutely convergent, so linearity gives V-u_0-u_1-K_rel[chi(r)r^-1 A_2]=U_zeta-U_zeta(0).

The remaining cutoff source chi(r)r^-1 A_2 is exactly the same radial Poisson problem as packet38 section5, with its symbol b there replaced by A_2 here. For clarity, its first cosine stream coefficient is

    P_1(r)=(alpha/2)[r^-1 integral_0^r rho chi(rho) d rho
                               -r integral_0^r chi(rho)/rho d rho].

It solves the radial Poisson equation, is regular at the center and has zero linear stream there. At r>=2 it equals

    -(alpha/2)r log r+alpha(1/4-L_chi/2)r+O(r^-1).

All other angular modes have exterior particular stream r g(theta) and decaying homogeneous corrections. Smoothness of A_2 gives convergent derivative mode sums; the exterior velocity correction is O_Cj(r^-2) or smaller. The mode solution is the canonical relative inverse by the same negative curl, divergence, sublinear growth and zero value at zero; the harmonic difference is constant and vanishes. Combining the source pieces proves (1), with

    C=alpha(1/4-L_chi/2)-[U_zeta(0)]_2.                 (8)

Both integrals defining this constant converge in the stated senses. If chi changes by a compactly supported radial delta chi, then delta L_chi=integral delta chi/rho and delta[U_zeta(0)]_2=-(alpha/2)integral delta chi/rho. These changes cancel in (8). Thus C is independent of the auxiliary cutoff. The normalization that g has no first harmonics fixes its decomposition with C. An observer gauge cannot alter it because V is already fixed.

## 4. Integrating the next exact physical right side

The logarithmic velocity obeys

    w_2(lambda z)=w_2(z)-(alpha/2)log(lambda)e_2.

Consequently (1) becomes, locally in every Cj norm off zero,

    u_tau=u_0+tau u_1+tau^2[w_2+(3alpha/2)log(tau)e_2]
                                      +O_Cj(tau^3(1+|log tau|)). (9)

Substitute (7) and (9) into the exact physical equations. Terms of order tau^0 and tau^1 are already matched. The next terms are

    partial_tau omega_tau=omega_1+2tau omega_2
        +tau^2[Q_omega+(3alpha/2)log(tau)partial_y omega_0]
        +O_Cj(tau^3(1+|log tau|)),
    partial_tau theta_tau=theta_1+2tau theta_2
        +tau^2[Q_theta+(3alpha/2)log(tau)partial_y theta_0]
        +O_Cj(tau^3(1+|log tau|)).                      (10)

The Q functions depend only on z, not tau. Products involving the log velocity and a first scalar correction are O(tau^3(1+|log tau|)); all remaining remainders have that bound as well, after using one further spatial derivative from (7). Integrate using

    integral_0^tau t^2 log(t) dt=tau^3[log(tau)/3-1/9].

The scalar expansions are therefore

    omega_tau=omega_0+tau omega_1+tau^2 omega_2
        +tau^3[Q_omega/3+(alpha/2)log(tau)partial_y omega_0
                                      -(alpha/6)partial_y omega_0]
        +O_Cj(tau^4(1+|log tau|)),

and the identical formula with theta in place of omega. Restrict to the unit circle and set tau=r^-1/3. The log(tau) term is exactly the log(r) part of Q/3, since w_2(re)=w_2(e)-(alpha/2)log(r)e_2. Homogeneity of every other term gives (2)-(4), with the remainders stated in (3).

As a direct check of the nonlog correction, put L_omega=3X.grad+1. All nonlog terms of Q_omega have degree -4/3, and its log coefficient is -(alpha/2)partial_y omega_0. Hence

    L_omega Q_omega=-3Q_omega-(3alpha/2)partial_y omega_0,
    L_omega[Q_omega/3-(alpha/6)partial_y omega_0]=-Q_omega.

The same calculation uses L_theta=3X.grad-1 and degree -2/3 for temperature. This verifies both signs and the additional -(alpha/6) term without time integration.

## 5. Nonvanishing and finite endpoint scope

Since the leading homogeneous temperature is smooth across the vertical axis away from zero, has degree 1/3, vanishes on that axis and is nonzero, partial_y theta_0 is not identically zero. Otherwise theta_0 would be c_+ x^(1/3) and c_- |x|^(1/3) on the two half-planes and smoothness at each nonzero axis point would force both constants to vanish. Likewise a nonzero smooth homogeneous omega_0 of degree -1/3 cannot be independent of y. Thus if alpha!=0 both coefficients in (4) are nonzero.

At beta=3 a finite final-interval polynomial in z=(L^2/(r^2+L^2))^(1/6), multiplied by the given exterior envelopes and sqrt(1-z^6) factors, generates powers r^(-j/3-2n) and no logarithms. Such an exact nontrivial class A field would therefore have to satisfy alpha=0. This is a necessary radial endpoint compatibility condition even when smooth arbitrary angular coefficients are allowed. It supplies no lower bound on the residual of a refining sequence. Neither alpha=0 nor alpha!=0 is established for the open class. The theorem makes no all-orders expansion claim, and it does not turn the numerical representations into profiles.

Dependencies: packets36,38 and90 as explicitly listed, the absolutely convergent relative inverse, elementary radial Poisson inversion, local interior elliptic estimates, exact physical transport, and homogeneity. No external regularity or analyticity assumption is added.

Verification scope (2026-10-21T00:05:12.982662+00:00): check_beta_three_log_tail.py completed 30 exact checks in 11.039964847 seconds. The three angular manufactures have alpha=64/45, 6824003/138738600, and 12853/693693. They are not profiles. Opus100 returned no written text because max_tokens was reached. Opus101 checked the integration but introduced an extra spatial logarithm; Opus102 explicitly withdrew it after the scaling and Euler identities above were supplied. Opus102 also withdrew an unjustified claim that higher remainders cannot contain higher powers of logarithms. Neither written review is an audit of the entire inverse argument in sections 2-3.

## 6. A smooth manufactured inverse with a known constant

This independent test is an inverse identity, not a solution of the transport system. Let A,B,alpha,D,G be arbitrary real constants, q=r^2, and set

    Psi=A x[(1+q)^(1/3)-1]+B x[(1+q)^(1/6)-1]
                      -(alpha/4)x log(1+q)+D x q/(1+q)+G x y/sqrt(1+q).

It is globally smooth and odd in x, and V=(-Psi_y,Psi_x) vanishes at zero. Its leading stream terms are A r^(5/3)cos(theta) and B r^(4/3)cos(theta), its third source is r^-1[alpha cos(theta)+3G cos(theta)sin(theta)], and its nonlog first-mode constant in (1) is exactly

    C=D-A-B.

Indeed each subtracted '-1' contributes a stream term -A x or -B x, D x q/(1+q)=D x+O_Cj(r^-1), and the logarithmic term equals -(alpha/2)x log r+O_Cj(r^-1). The last term is r G cos(theta)sin(theta)+O_Cj(r^-1). All higher-order derivatives have these exterior expansions by direct differentiation. The complete source is

    Omega=-sum_(a,w) w x[8a(1+q)^(a-1)+4q a(a-1)(1+q)^(a-2)]
           +alpha x(q+2)/(1+q)^2-8D x/(1+q)^3
           +3G x y(q+2)/(1+q)^(5/2),
    (a,w)=(1/3,A),(1/6,B).

For any cutoff chi of section3, the angular first-mode reduction gives

    [U_zeta(0)]_2=A+B+alpha(1/4-L_chi/2)-D,

so (8) reproduces C. To verify this independently, write the source as cos(theta) times a radial coefficient plus the mode2 contribution. The latter integrates to zero in U_2(0). For either power term let P(r)=r[(1+r^2)^a-r^(2a)]. Its first-mode source remainder is -(P''+P'/r-P/r^2). Its radial integral is -[P'+P/r]_0^infinity=2, since 0<a<1/2; multiplication by w/2 contributes w. For the logarithmic term,

    integral_0^R r(r^2+2)/(1+r^2)^2 dr
                 = [log(1+R^2)-1/(1+R^2)+1]/2,

whose difference from log R tends to1/2. Subtracting chi/r gives the displayed alpha contribution. Finally integral_0^infinity -8D r/(1+r^2)^3 dr=-2D, whose half is -D. Every remainder integral here is absolutely convergent. This proves the value of C and its cutoff independence without numerical cancellation at a large radius. Negative curl and divergence of the displayed V are exact differential identities. The same sublinear harmonic uniqueness used earlier identifies V with the full-plane canonical relative inverse.

The numerical test uses a separately implemented Cartesian Duffy square integral and a compactified square exterior, at several orders and core sizes; it compares against the explicit derivatives of this Psi. Cutoff moments and asymptotic extraction are supplementary floating-point consistency checks, not interval certificates or existence evidence.
