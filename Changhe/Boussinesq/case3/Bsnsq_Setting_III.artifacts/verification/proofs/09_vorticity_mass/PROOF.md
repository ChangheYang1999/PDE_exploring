# Vorticity mass and finite-integrability obstructions

Status: complete informal derivation. The power-growth mass argument independently audits the lead's referee result. The critical finite-enstrophy extension in Sections 6-7 is a verifier argument independently audited by the actual Claude Opus 5.5 model on 2026-10-20; minor bookkeeping clarifications were incorporated. These are restricted exclusions, not a full NO.

## Statement and hypotheses

Let beta >= 2. Let U, Omega and Theta be smooth on the whole plane and satisfy

    div U = 0, curl U = -Omega,
    W = beta X + U(X) - U(0),
    W.grad Omega + Omega = Theta_x,
    W.grad Theta = (beta-2) Theta,
    U(X) = o(|X|).

Assume Theta(0,y)=0, x-reflection symmetry, and Theta=a0*x^2+O(|X|^3), with a0>0. The signed scaling in research/07_reconstruction_scaling allows this sign and a0=1 without changing beta. Alternatively apply the argument to sign(a0)*Theta and insert that sign before the source flux below; every estimate uses absolute Omega.

Write M(R)=integral_{|X|<R}|Omega(X)| dX and kappa=2-2/beta.

1. If, for some epsilon in (0,1), |U(X)-U(0)| <= C(1+|X|)^(1-epsilon), then M(R) >= c R^kappa for every sufficiently large R. No bound on DU is required.
2. Under this additional power bound, Omega cannot be o(r^(-2/beta)) uniformly in angle. Nor can integral |Omega|(1+r)^(-gamma) be finite for any gamma <= kappa.
3. Under the original hypotheses, including the nonzero temperature patch and U=o(r), Omega is not in L^p(R^2) for any 1 <= p <= beta. In particular finite enstrophy is impossible, including the critical beta=2 case. If Omega is also bounded, membership in any L^p with 0<p<1 is excluded as well.

The conclusions do not exclude the slow natural tails r^(-1/beta) or r^(-2/beta). The radial weighted integral in item 2 is not interchangeable with the single component integral integral |x Omega|/r^2.

## 1. Flow, a positive patch, and a mixed identity

Smoothness and the at-most-linear growth of W give a complete flow phi_t, for all finite positive and negative times. Since div W=2 beta,

    det D phi_t = exp(2 beta t),
    Theta(phi_t X) = exp((beta-2)t) Theta(X).

There is a bounded open patch D of positive area in x>0 with Theta >= a>0. For example take a small neighborhood of a sufficiently small point (x,0), x>0. Every phi_t(D), t>=0, stays in x>0. A crossing of x=0 would contradict the positive transported temperature and the axis condition. Symmetry also makes that axis invariant.

Choose a smooth nondecreasing function f with 0<=f<=1, f(t)=0 for t<=a/4, and f(t)=1 for t>=a/2. Set g(t)=integral_0^t f(q)dq. Then g>=0 on the whole real line, g(0)=0, and g(t)>=t/2 for t>=a. The transition of f occurs in a fixed compact positive interval, so

    b(t)=(2 beta-1)f(t)+(beta-2)t f'(t)

is bounded. Expanding the divergence using both transport equations gives the exact identity

    div[W Omega f(Theta) - g(Theta) e_x] = b(Theta) Omega.       (1)

Indeed div(W Omega f)=(2 beta-1)Omega f+Theta_x f+(beta-2)Theta Omega f', and the derivative of g removes Theta_x f. No integration at infinity has occurred.

## 2. A finite half-box estimate

Choose eta smooth on [0,infinity), nonnegative and nonincreasing, zero for t>=2, with -eta'(t)>=c0>0 for 0<=t<=1. Choose chi smooth, nonnegative, equal to 1 on [-1,1] and zero outside [-2,2]. Define

    h_R(x,y)=eta(x/R)chi(y/R),  x>=0,  R>=1.

This is a smooth test function on the closed half-plane; eta is not asserted to extend by zero smoothly across x=0. Equation (1), integrated by parts on x>0, has no axis boundary term because f(Theta)=g(Theta)=0 there. Thus

    integral g(Theta)(-h_R,x)
      = -integral Omega [f(Theta) W.grad h_R + b(Theta) h_R].  (2)

All integrals in (2) have compact support. The bracket on the right is bounded independently of R because |W|<=C(1+r), |grad h_R|<=C/R, and its support lies in B_(3R). The left side is nonnegative everywhere and dominates (c0/R) integral_{Q_R} g(Theta), where Q_R=(0,R) times (-R,R). Therefore

    integral_{Q_R} g(Theta) <= C R M(3R).                    (3)

The sign of Omega is unrestricted. Negative temperature outside the chosen transported patch is harmless because g=0 there.

## 3. Exact mass exponent under a power velocity bound

Write V=U-U(0). The power bound gives, for z=1+|phi_t X|,

    z' <= beta z + C z^(1-epsilon).

Applying the inequality to z^epsilon and integrating proves |phi_t X|<=C_D exp(beta t), uniformly for X in D and t>=0. Increase C_D so that phi_t(D) is contained in Q_(R_t), where R_t=C_D exp(beta t).

On this patch Theta>=a exp((beta-2)t)>=a. Its area is exp(2 beta t)|D|. Hence

    integral_{Q_(R_t)} g(Theta)
      >= (a|D|/2) exp((3 beta-2)t)
      = c R_t^(3-2/beta).

Combine with (3) and rename 3R_t as R. As t varies over [0,infinity), 3R_t covers every sufficiently large radius. This proves M(R)>=c R^kappa.

## 4. Decay and radial weighted consequences

Uniform Omega=o(r^(-2/beta)) implies M(R)=o(R^kappa), by splitting off a fixed ball and integrating r^(1-2/beta) outside it. This contradicts Section 3.

Suppose integral |Omega|(1+r)^(-gamma)<infinity. If gamma<=0, M(R) is bounded. If gamma>0, first fix R0 so that the weighted integral outside R0 is less than any chosen eta>0. Then

    M(R) <= M(R0) + eta(1+R)^gamma,  R>=R0.

It follows that M(R)=o(R^gamma). For gamma<=kappa this again contradicts the lower bound. This implication needs no assertion about angular pointwise tails.

## 5. L^p below the critical exponent, and above two at the critical exponent

Under the weaker assumption V=o(r), for every rho>0 one still has

    |phi_t X| <= C_(D,rho) exp((beta+rho)t).

Repeat Sections 2-3 with R_t=C_(D,rho)exp((beta+rho)t). It gives

    M(R) >= c_rho R^kappa_rho,
    kappa_rho = (3 beta-2)/(beta+rho)-1,
    kappa_rho -> kappa as rho decreases to zero.             (4)

If Omega is in L^1, this contradicts bounded M for small enough rho. If 1<p<beta and Omega is in L^p, Holder's inequality gives M(R)<=C R^(2-2/p). Since 2-2/p<kappa, choose rho small enough that kappa_rho>2-2/p. Equation (4) is a contradiction. No boundedness of Omega is used.

It remains to consider p=beta. First let beta>2. Define K(Z)=(Z_2,-Z_1)/(2 pi |Z|^2). If p>2 and p'=p/(p-1), the difference K(X-Y)-K(-Y) belongs to L^(p') in Y. Near Y=0 and Y=X this follows from p'<2; at infinity it follows from the O(|X|/|Y|^2) cancellation and p'>1. Scaling gives the exact norm estimate

    ||K(X-.)-K(-.)||_(p') <= C_p |X|^(1-2/p).

The absolutely convergent relative integral against Omega therefore defines V_*(X) with this power bound. It has div V_*=0 and curl V_*=-Omega in distributions. Local smoothness follows by separating a local smooth density from the nonsingular tail. Both U and V_* have sublinear growth, so U-V_* is an entire harmonic vector field of sublinear growth and is constant. Since V_*(0)=0, U-U(0)=V_*. Thus the power hypothesis of Section 3 holds with epsilon=2/p.

When p=beta>2, the finite L^p norm implies M(R)=o(R^(2-2/p)): separate a fixed interior ball, apply Holder only to the tail, and make its L^p norm arbitrarily small. This contradicts Section 3. The remaining critical case is beta=p=2.

## 6. A velocity estimate from finite enstrophy and sublinear growth

Assume temporarily Omega is in L^2, for any beta>=2. We prove

    ||DU||_2 = ||Omega||_2,
    ||U-U(0)||_(L^2(B_R)) <= C R(1+log R),  R>=2.            (5)

These assertions use only the whole-plane div-curl equations, smoothness and U=o(r). They do not require pointwise bounded Omega.

Here are the distributional details. U is tempered by its growth bound. Restrict the Fourier distributions to the open set of nonzero frequencies. There the div-curl equations can be solved by multiplication by smooth functions of frequency, and determine the Fourier transform of DU. The matrix A with multipliers

    A_(1j): xi_j xi_2/|xi|^2,
    A_(2j): -xi_j xi_1/|xi|^2

applied to Omega belongs to L^2 by Plancherel, and the sum of the squares of these four multipliers is 1. The Fourier transform of DU-A is supported at zero, so DU-A is a polynomial matrix P. This last step uses the elementary distribution theorem that a distribution supported at one point is a finite sum of derivatives of the point mass.

For any smooth compactly supported scalar test function h and h_R(X)=R^(-2)h(X/R),

    <D_j U_i,h_R> = -R^(-1) integral U_i(RZ) D_j h(Z)dZ -> 0.

To see the limit uniformly near Z=0 as well, use |U(X)|<=eta|X|+C_eta, then let R tend to infinity and eta decrease to zero. Also |<A,h_R>|<=||A||_2||h||_2/R ->0. Hence <P,h_R>->0 for every h. A nonzero polynomial cannot have this property: its pairing is a polynomial in R, and a test function can be chosen with nonzero moment against its highest homogeneous part. Therefore P=0 and the first assertion of (5) follows.

Let m_R be the mean of U on B_R and M=||DU||_2. Poincare's inequality gives ||U-m_R||_(L^2(B_R))<=C R M. Comparing m_R and m_(2R) on B_R gives |m_(2R)-m_R|<=C M. Sum over dyadic radii to obtain |m_R|<=C(1+log R). These two estimates prove the second assertion of (5), including the harmless constant U(0).

Dependencies of this paragraph are Plancherel's theorem, the elementary Fourier transform identities for distributions, the point-support distribution theorem, and Poincare's inequality on a ball. Their hypotheses are explicitly satisfied above. No Calderon-Zygmund L^p theorem with p!=2 is needed.

## 7. Finite enstrophy controls a positive fraction of the transported patch

The pointwise bound with any fixed 0<rho<beta gives phi_t(D) contained in B_(C exp((beta+rho)t)), with C increased to be at least 2. Thus (5) applies also at early times. Define Z_t(X)=exp(-beta t)phi_t(X). By the flow equation,

    d Z_t/dt = exp(-beta t) V(phi_t X).

The exact flow Jacobian, followed by (5), yields

    ||d Z_t/dt||_(L^2(D))
      = exp(-2 beta t) ||V||_(L^2(phi_t D))
      <= C exp((-beta+rho)t)(1+t).

This bound is integrable in t. The integral version of Minkowski's inequality therefore proves sup_(t>=0)||Z_t||_(L^2(D))<=C_D. Choose K sufficiently large. Chebyshev's inequality shows that, for every t, a subset D_t of D of area at least |D|/2 satisfies |Z_t(X)|<=K.

The image phi_t(D_t) lies in the open box Q_((K+1) exp(beta t)), has area at least exp(2 beta t)|D|/2, and has Theta>=a exp((beta-2)t). Apply (3) to this subset exactly as in Section 3. It follows that M(R)>=c R^kappa for all large R, now derived under finite enstrophy instead of a power bound on V.

But finite enstrophy implies M(R)=o(R), by Holder on a small L^2 tail and a fixed interior ball. Since kappa>=1 for beta>=2, this is a contradiction. This handles the outstanding beta=p=2 case and proves finite-enstrophy exclusion for the entire beta>=2 range.

Combining Sections 5 and 7 proves item 3 for 1<=p<=beta. If Omega is bounded and 0<p<1, then |Omega|<=||Omega||_infinity^(1-p)|Omega|^p, so L^p would imply L^1 and is excluded too.

## Audit scope and remaining gap

The mixed identity and exact mass exponent under a power velocity bound independently confirm Proposition 2 in the lead's referee answer. The radial weighted consequence removes the derivative-decay hypothesis from that part of the scattering-based restricted theorem. Sections 6-7 and the unrestricted L^p conclusion are verifier extensions. The actual Claude Opus 5.5 model independently confirmed Sections 6-7; its report and model metadata are in opus_reviews/02_critical_enstrophy. The minor clarifications about Fourier restriction, early-time radii and an open box have been incorporated and checked. The physical B2 equations in PROMPT.md impose exactly U=o(r), the stated axis condition and the temperature transport sign used here. The signed scaling has a separate complete proof in research/07_reconstruction_scaling. No conclusion excludes L^p when p>beta.

No sign of Omega, global sign of Theta, global source basin, angular asymptotic expansion, finite box, or vanishing boundary flux at infinity is assumed. The estimates never establish a full NO for smooth profiles with nonintegrable vorticity tails. They leave that main branch open.
