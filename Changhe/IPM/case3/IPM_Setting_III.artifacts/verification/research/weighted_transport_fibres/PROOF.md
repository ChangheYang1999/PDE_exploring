# What transport identities with weights in (r, rho) actually imply

Verifier result 159. Independent informal argument written 2026-10-21 before the supporting exact checks. This audits the lead's proposed 3.70 and A.3.70; it does not assume the external analysis or lead review is correct.

## 1. Statement and exact hypotheses

Let rho be a real C-infinity function on R^2, even in x and odd in y, with a=rho_y(0)!=0 and |rho|+(1+r)|grad rho|<=C(1+r)^gamma for some0<gamma<1. Let U be its canonical velocity: div U=0, curl U=-rho_x, the induced parities and U=o(r). Fix ell>1, and set p=1/ell, W=ell X+U, U_r=U.X/r and E=W.grad rho-rho. No transport equation is assumed in claims A and B below.

A. For every Phi in C_c^infinity((0,infinity) x R), evaluated at (r,rho(X)),

    integral [2ell Phi+(ell r+U_r) Phi_r+rho Phi_s] dX
        = -integral E Phi_s dX.                                    (1)

The left side vanishes for every such Phi if and only if the signed locally finite measure obtained by pushing E dX forward under X -> (r,rho(X)) is zero. At regular values of rho on a circle, this condition states that the sum of E/|rho_theta| over the fibre is zero.

B. If this condition holds, then E is identically zero on some disc about the origin. At every radius r>0, the pushforward of E(r,theta)dtheta under theta -> rho(r,theta) must vanish, including any measure carried by critical levels. At regular levels it is the indicated sum. No conclusion E=0 everywhere is proved here without further information about angular fibres.

C. For an exact primary profile, let Theta be its smooth nonzero far-field trace, rho/r^p -> Theta, and U=O(r^p). These facts follow from the prior full-class far-field theorem (lead3.23, independently checked), rather than being extra assumptions on that profile. For beta>0 define

    M(alpha,beta)=integral r^alpha |rho|^beta dX,
    V(alpha,beta)=integral r^(alpha-2)(U.X)|rho|^beta dX.

If -2-beta<alpha<-2-beta p, both integrals converge absolutely and

    V = ((2+alpha)ell+beta) M/(-alpha) < 0.                         (2)

At alpha_e=-2-beta p, M diverges, V converges absolutely, and

    alpha_e V = ell integral_0^(2pi) |Theta|^beta dtheta.           (3)

D. Each identity (2), at any one fixed pair (alpha,beta) in its strip, is satisfied by some smooth canonical density that is not a profile. The same is true of (3) at any one beta. They can all be chosen from the family in Section5 with identical ell, a, strain and trace. The parameter satisfying one identity may differ from the parameter satisfying another. No member of this family satisfies all compactly supported identities (1), because its residual is nonzero arbitrarily near the origin. Existence of a non-profile satisfying the whole family (1) globally is not settled.

## 2. Compactly supported weights and the pushforward condition

The support of Phi in its radial variable lies in a compact annulus. Thus Phi(r,rho) is smooth and compactly supported away from0. The chain rule and div W=2ell give

    div[W Phi(r,rho)]
      =2ell Phi+(ell r+U_r)Phi_r+(rho+E)Phi_s.

Integration proves (1). All integrals here are ordinary finite integrals on a compact annulus, so no limit at infinity is involved.

Call the pushforward signed measure nu. The vanishing condition is integral Phi_s dnu=0. On any relatively compact radial interval J, rho is bounded, so nu has bounded support in s. To see directly that nu=0, take any compact test Psi supported over J. Choose a smooth eta(s) of integral1 supported beyond that bounded s-support and beyond the s-support of Psi. Set

    Phi(r,s)=integral_(-infinity)^s [Psi(r,t)-eta(t) integral_R Psi(r,v)dv] dt.

Its integrand has integral0, so Phi is smooth and compact in (r,s), and integral Phi_s dnu=integral Psi dnu. Therefore nu annihilates every Psi. Conversely nu=0 immediately gives the identities. This explicitly removes the otherwise possible distribution independent of s.

The condition holds on every circle, not only almost every radius. For each smooth compactly supported chi(s), the function F_chi(r)=integral E(r,theta)chi(rho(r,theta))dtheta is continuous for r>0. Testing nu=0 against products eta(r)chi(s) shows integral eta(r)r F_chi(r)dr=0. Thus F_chi(r)=0 for every r>0. Since this is true for every chi, the full signed image measure on each circle is zero. Conversely, zero image measure on every circle implies nu=0 by radial integration. Critical levels can carry a singular part of this image measure, so regular-fibre sums alone do not in general express the whole condition.

At a regular pair (r,s), the one-dimensional change-of-variables formula on the circle gives the density

    r sum_(rho(r,theta)=s) E(r,theta)/|rho_theta(r,theta)|

with respect to dr ds. A regular fibre on a compact circle is finite. On a small neighborhood of each regular pair these inverse branches and the displayed density are continuous. Hence zero measure gives zero density there pointwise, not merely almost everywhere. No assertion about individual points on critical fibres is needed.

## 3. Why the condition becomes the PDE near the origin

Parity gives rho_x=x g for smooth g, rho_y=a+O(r^2), and y g=O(r^2): rho_x is odd in x and in y. Thus

    rho_theta=-y rho_x+x rho_y=x(a+O(r^2)).

On a sufficiently small disc the second factor has the fixed sign of a and magnitude at least|a|/2. On each arc x>0 or x<0 of a circle, rho is strictly monotone; its only angular extrema lie on x=0. Each value strictly between them has exactly two preimages, related by x -> -x. Canonical parity makes W_1 odd in x and W_2 even in x, while rho_x is odd and rho_y even, so E is even in x. The two terms in the regular-fibre sum are equal and their common denominator is nonzero. Their zero sum forces E=0 at both points. This covers the punctured disc off the y-axis. Smoothness extends the conclusion to the axis and origin.

This uses the nonzero first derivative and parity, not an unproved global monotonicity or a sign assumption on rho away from the origin.

## 4. Power weights, the zero set and boundary fluxes

For an exact profile, W.grad rho=rho. Even when beta<1, the identity W.grad|rho|^beta=beta|rho|^beta holds distributionally. Indeed, on a compact annulus use h_epsilon=(rho^2+epsilon^2)^(beta/2). Its derivative along W is beta rho^2(rho^2+epsilon^2)^(beta/2-1). This converges pointwise to beta|rho|^beta, including at rho=0, and is bounded by beta h_epsilon. Dominated convergence applies to both sides on the annulus. No hypothesis on the measure or regularity of the zero set is used.

Multiplying by r^alpha and using div W=2ell gives

    div(W r^alpha |rho|^beta)
      =[(2+alpha)ell+beta]r^alpha|rho|^beta
          +alpha r^(alpha-2)(U.X)|rho|^beta.                       (4)

Near0, rho=O(r), U=O(r), and U.X=O(r^2). After angular integration and the area factor r dr, both right-hand integrands are bounded by a constant times r^(alpha+beta+1). At infinity, M has radial bound r^(alpha+beta p+1); V has radial bound r^(alpha+beta p+p). These exponents give absolute convergence in the stated strip, and V also at alpha_e since its exponent is p-2<-1.

The outward flux through the circle of radius R is

    F(R)=R^(alpha+2) integral |rho(R,theta)|^beta(ell+U_r/R)dtheta.

Near0 it tends to0 when alpha+beta+2>0. At infinity it tends to0 inside the strip. Integration of (4) over annuli, or equivalently smooth radial cutoff approximation, gives (2). Here alpha<0, M>0 and (2+alpha)ell+beta<0, so V<0. At alpha_e the coefficient of M is exactly0; integrating on finite annuli is therefore legitimate despite M diverging. The inner flux still tends to0, and the outer flux tends to ell integral|Theta|^beta. This proves (3). Nonzero Theta makes that angular integral positive and M's radial integrand asymptotic to a positive constant times r^(-1), proving its divergence. All uses of a far-field trace in this paragraph are for exact primary profiles or for the explicit family below.

## 5. A family attaining each individual identity

Let a=4(ell-1)>0. Fix f>=0 smooth, nonzero and compactly supported in1<r<2. Define

    A_t(r)=a r(1+r^2)^((p-1)/2)+t f(r),
    rho_t=A_t(r)sin(theta),
    I_t(r)=integral_0^r s^2 A_t(s)ds,
    psi_t=-I_t(r)/(2r^2) sin(2theta).                              (5)

These densities are smooth at0 because f vanishes there and the base equals a y(1+r^2)^((p-1)/2). They have the required parities and sublinear growth with exponent p. Put B=-I/(2r^2). Direct differentiation using I'=r^2 A gives

    -(B''+B'/r-4B/r^2)=(A'-A/r)/2,

which is precisely the sin(2theta) coefficient of rho_x. The stream is smooth at0: I/r^4 has a smooth expansion in r^2 there. At infinity B=O(r^(p+1)), B'=O(r^p), and the annular perturbation adds only a decaying r^(-2) stream. The resulting velocity is sublinear and has the required parities. It is canonical: a difference from any other canonical velocity is globally harmonic and sublinear, hence constant by the mean-value gradient estimate on arbitrarily large balls; the parities eliminate that constant.

Near0, A=a r+b r^3+O(r^5), b=a(p-1)/2, and B=-a r^2/8-b r^4/12+O(r^6). Thus rho_y(0)=a, psi_xy(0)=-a/4=1-ell, and every t has trace Theta=a sin(theta). All of these are exact, t-independent data.

Let S_beta=integral_0^(2pi)|sin(theta)|^beta dtheta. Integrating the derivative of cos(theta)sin(theta)^(beta+1) on(0,pi) and using reflection gives S_(beta+2)=(beta+1)S_beta/(beta+2). Consequently

    integral cos(2theta)|sin(theta)|^beta dtheta
        =-beta S_beta/(beta+2).

Since U_r=I r^(-3)cos(2theta),

    V_t=-beta S_beta/(beta+2)
          integral_0^infinity r^(alpha-3) I_t(r)|A_t(r)|^beta dr.   (6)

On1<r<2, division by t|t|^beta and dominated convergence gives the limit

    V_t/(t|t|^beta) -> -beta S_beta/(beta+2)
         integral_1^2 r^(alpha-3) I_f(r) f(r)^beta dr <0.           (7)

The limit is strictly negative: f is positive on some interval, and I_f becomes positive within that interval. On r<1 the numerator is independent of t. On r>2, A_t=A_0 and I_t=I_0+t I_f(2), so the contribution is O(1+|t|), which is negligible after this division for beta>0. These exterior integrals converge both in the strip and at the endpoint. This justifies the global limit, including nonintegral beta and negative t.

Inside the strip, M_t=O((1+|t|)^beta), and M_t and V_t are continuous in t by domination on compact t-intervals. Thus V_t-C_(alpha,beta)M_t has opposite signs as t tends to the two infinities, where C_(alpha,beta)=((2+alpha)ell+beta)/(-alpha). The intermediate value theorem gives (2) for some t. At the endpoint, alpha_e V_t-ell integral|Theta|^beta likewise takes opposite signs, giving (3) for some t. No statement that the same t works for two different weights is made.

## 6. None of these densities is a profile

For any radial A and B in (5), direct polar differentiation gives

    E=sin(theta)[ell r A'-A+AB'/r
                       +(AB'-2BA')cos(2theta)/r].                (8)

Using the expansions above,

    (AB'-2BA')/r=(ab/3)r^3+O(r^5)
                =a^2(p-1)r^3/6+O(r^5).

This coefficient is nonzero since a>0 and p<1. The other radial bracket in (8) is (2b(ell+2)/3)r^3+O(r^5). Since sin(theta)cos(2theta)=(sin(3theta)-sin(theta))/2, the complete cubic residual is

    E=r^3[a(p-1)sin(theta)+a^2(p-1)sin(3theta)/12]+O(r^5).

The sin(3theta) coefficient is nonzero and cannot be canceled by the sin(theta) term. The annular perturbation is zero near0, so the argument applies to every real t. By Section3 these densities also cannot satisfy all the compactly supported identities (1).

## 7. Dependencies, verification and verdict

Dependencies: existence and uniqueness of the canonical inverse in the growth class; smooth nonzero trace and U=O(r^p) for exact primary profiles from the already audited full-class far-field result; elementary divergence, coarea and dominated convergence arguments. The pushforward and non-profile claims need no profile existence assumption. Exact code checks the radial Poisson identity, Cartesian versus polar residual, cubic Fourier coefficient, algebraic endpoint exponents and angular integration recurrence. These are supporting arithmetic checks, not a substitute for the integral arguments above.

Verdict of the mathematical audit: CONFIRMED proposed3.70 and A.3.70 under the stated hypotheses. The continuity step after the regular-fibre coarea statement is written explicitly here; it fills an implicit routine passage in the draft, not an additional assumption. No NO or YES endpoint follows. The external small-beta asymptotics and punctured-plane example are outside this audit and outside the proposed3.70.

Scope repair, 2026-10-21: the original sentence in Statement B said that only the regular-fibre sums were required globally. That omitted possible mass on critical levels. Statement A already required the full pushforward measure to vanish. Statement B and Section2 now state and prove the full every-radius condition. The original blanket confirmation of that wording was too broad; the current claim includes the correction. The full cubic residual is also displayed. All earlier versions are preserved under verification/d51_scope_repair.
