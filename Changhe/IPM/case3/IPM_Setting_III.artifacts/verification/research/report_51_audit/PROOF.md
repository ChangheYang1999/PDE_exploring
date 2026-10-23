# Audit of frozen draft 51: weighted transport identities

Verifier result 161. Written 2026-10-21 before the final source comparison. The audited report has SHA256 c429b12a93f678de7dcbac7fe8f2bdb13c1b5549ee387dd3161569aef147d732. The mathematical statements are those of Section 3.70 and Appendix A.3.70. This audit checks the changed passages against the independent argument in result 159, including the critical-level qualification that the first version of that argument had omitted from one sentence.

## Statement and hypotheses

Let rho be smooth on the full plane, even in x and odd in y, with a=rho_y(0) nonzero and the sublinear weighted first-derivative growth bound of the primary class. Let U be the canonical divergence-free velocity, with curl U=-rho_x, the induced parities and U=o(r). Set ell>1, p=1/ell, W=ell X+U, and E=W.grad rho-rho. For compactly supported smooth Phi(r,s), supported away from r=0, integration of div[W Phi(r,rho)] gives

    integral [2ell Phi+(ell r+U_r)Phi_r+rho Phi_s]dX
      =-integral E Phi_s dX.                                     (1)

All left sides vanish if and only if the full pushforward of E dX by X -> (r,rho(X)) vanishes. This is equivalent to zero image measure of E(r,theta)dtheta on every circle, including critical levels. It forces E=0 on a disc near the origin. These assertions require no transport equation as a hypothesis.

For an exact primary profile, write M=integral r^alpha|rho|^beta and V=integral r^(alpha-2)(U.X)|rho|^beta. For beta>0 and -2-beta<alpha<-2-beta p,

    V=[(2+alpha)ell+beta]M/(-alpha)<0.                            (2)

At alpha=-2-beta p, M diverges but V converges absolutely and

    alpha V=ell integral |Theta|^beta dtheta.                    (3)

Here the smooth nonzero far-field trace Theta and U=O(r^p) follow from the previously audited full-class theorem for exact profiles. Finally, each individual identity (2) or (3) can hold for a smooth canonical non-profile with the same ell, a, center strain and trace. The parameter can depend on the chosen identity. The statements do not produce a non-profile satisfying all of (1), or any actual profile.

## Pushforward, critical levels and every radius

The chain rule proves (1) on a compact annulus. If nu is the pushforward measure, the zero left side says partial_s nu=0. On every relatively compact radial interval, nu has bounded support in s. For any compact test Psi, choose a smooth eta of integral one supported outside this s-support and the s-support of Psi. The compact test

    Phi(r,s)=integral_-infinity^s [Psi(r,t)-eta(t)integral Psi(r,v)dv]dt

then has integral Phi_s dnu=integral Psi dnu, so nu=0. This rules out a nonzero distribution constant in s. Conversely nu=0 implies (1) with zero left side.

For each smooth compact chi(s), F_chi(r)=integral E(r,theta)chi(rho(r,theta))dtheta is continuous for r>0. The identity against eta(r)chi(s) implies r F_chi(r)=0 distributionally, hence pointwise. Therefore the circle pushforward vanishes at every radius. This elementary continuity argument supplies the passage to every r in the main statement; the appendix already proves its regular-pair counterpart. At a regular pair (r,s), the finitely many inverse branches are smooth and the image measure has smooth density r sum E/|rho_theta|. It vanishes pointwise there. Critical levels may carry a singular image measure, so just checking regular sums is insufficient in general. The revised draft explicitly requires that singular part to vanish.

Parity yields rho_theta=x(a+O(r^2)). At small r each intermediate level consists of two regular points mirrored across x=0. E is even in x, so their contributions to the sum are equal. The zero sum forces E=0 off the y-axis, and continuity fills the entire disc.

## The power-weight limit and its scope

For an exact profile, use h_epsilon=(rho^2+epsilon^2)^(beta/2) on a compact annulus. Direct differentiation gives

    div(W r^alpha h_epsilon)
      =[(2+alpha)ell+beta]r^alpha h_epsilon
        +alpha r^(alpha-2)(U.X)h_epsilon
        -beta r^alpha epsilon^2(rho^2+epsilon^2)^(beta/2-1).

The last term is bounded by C epsilon^beta for 0<beta<=2 and by C epsilon^2 for beta>2. Thus it tends uniformly to zero, and the other terms converge uniformly. This proves the distributional identity even on an arbitrary zero set.

At zero, both radial integrands are O(r^(alpha+beta+1)); at infinity they are respectively O(r^(alpha+beta p+1)) and O(r^(alpha+(beta+1)p)). The stated strip makes both integrable. The radial flux is R^(alpha+2)integral |rho|^beta(ell+U_r/R)dtheta. It tends to zero at both ends inside the strip, yielding (2), whose coefficient is negative. At the endpoint the M coefficient is exactly zero on each finite annulus. Its outer flux tends to ell integral |Theta|^beta and its inner flux to zero. V remains integrable since its exterior radial exponent is p-2<-1. Nonzero Theta makes M diverge logarithmically. This proves (3) without multiplying a divergent integral by zero.

## The non-profile family and the complete cubic residual

Take a=4(ell-1), a fixed nonzero nonnegative smooth f supported in 1<r<2, A_t=a r(1+r^2)^((p-1)/2)+t f, I_t=integral_0^r s^2 A_t(s)ds, rho_t=A_t sin(theta) and psi_t=-I_t sin(2theta)/(2r^2). Differentiation verifies the Poisson equation, smoothness at zero, the parities and sublinear velocity. The canonical uniqueness theorem identifies this stream. Its a, strain -a/4=1-ell and trace a sin(theta) are independent of t.

The angular integration identity integral cos(2theta)|sin(theta)|^beta=-beta S_beta/(beta+2) gives

    V_t=-beta S_beta/(beta+2) integral r^(alpha-3) I_t |A_t|^beta dr.

After division by t|t|^beta, the r<1 portion tends to zero; on [1,2] dominated convergence gives the strictly positive radial integral integral r^(alpha-3)I_f f^beta before the displayed negative prefactor. On r>2, A_t=A_0 and I_t=I_0+t I_f(2), so the contribution is O(1+|t|). The two exterior exponents at the endpoint are p-2 and -5, both integrable. Inside the strip M_t=O((1+|t|)^beta). Thus V_t minus the right side of (2) takes opposite signs at the two infinities. At the endpoint, alpha V_t minus the fixed right side of (3) does so as well. Continuity and the intermediate value theorem give a parameter for each chosen identity, with no simultaneous assertion.

Write A=a r+b r^3+O(r^5), b=a(p-1)/2, near zero. Then psi=-a xy/4-b xy(x^2+y^2)/6+O(r^6). Independent Cartesian differentiation gives the cubic residual coefficients

    [x^2 y]E=2ell b,       [y^3]E=(8-2ell)b/3.

Since r^3 sin(theta)=x^2 y+y^3 and r^3 sin(3theta)=3x^2 y-y^3, the sin(theta) and sin(3theta) coefficients are respectively 2b=a(p-1) and ab/6=a^2(p-1)/12. Consequently

    E=r^3[a(p-1)sin(theta)+a^2(p-1)sin(3theta)/12]+O(r^5),

exactly as in draft 51. The latter coefficient is nonzero, so every family member fails the PDE near zero. The annular parameter never changes this local conclusion.

## Audit verdict, evidence and limitation

Section 3.70 and Appendix A.3.70 are CONFIRMED with all stated hypotheses. The new timeline and changed summary were read in full. In the Section 6 summary, add “compactly supported smooth” before “weights Phi”: without the reference to 3.70, the literal statement for all weights is too broad because noncompact weights can have nonzero or infinite boundary flux. This is a scope clarification in the summary, not a defect in the theorem or appendix.

The earlier result 159 Statement B had the same incomplete regular-level wording as the first proposed draft. It has been repaired to include critical-level mass and the every-radius continuity argument, with its original version preserved. The additional full cubic coefficient check and prior independent Cartesian/polar checks all pass (1661 exact finite checks). The revised proof has SHA256 5b6867527883dd0be82fd8b3045fc89ab2c47181db75b6da4c97f06879cc16c1. These arithmetic checks support, but do not replace, the integral argument above. The actual Opus 5.5 lead hand review and the external audit were read and their claims checked independently. No existence or nonexistence endpoint follows.
