# Positive axis tails and their angular matching

Date:2026-10-20. Verdict:CONFIRMED by the independent verifier under the hypotheses stated below. This is a necessary-condition theorem, not an existence or nonexistence endpoint.

## 1. Exact setting and dependencies

Let beta>=2, nu=1/beta, m=1-2nu, a0>0, lambda=(beta-2)/2 and mu=(3beta+2)/2. Let a smooth full-plane B2 profile satisfy

    W=beta Y+V, div W=2beta, -curl V=Omega,
    W.gradTheta=(beta-2)Theta,
    W.gradOmega+Omega=Theta_x,
    DW(0)=diag(lambda,mu),
    Theta=a0 x^2+O(|Y|^3), Omega_x(0)=4a0/beta.

Here Y=(x,y), Theta is even in x, Omega is odd in x, V_1 is odd in x, and V_2 is even in x. Also Theta(0,y)=0. Assume the prompt's sublinear canonical velocity and polynomial source bounds, or directly class A. Packets33,36,40 then give, uniformly at large radius,

    V=O(r^(1-nu)), DV=O(r^-nu),
    Omega(r e_theta)=r^-nu a(theta)+O_{C^j(theta)}(r^-2nu),
    Theta(r e_theta)=r^m h(theta)+O_{C^j(theta)}(r^(m-nu)),       (1.1)

for each fixed finite j, with smooth periodic a,h and e_theta=(cos theta,sin theta). The full spatial version of these expansions was proved in packet36; the angular version through j=2 already suffices below. In particular a vanishes on the two vertical directions; h and h' vanish there. We do not differentiate a mere C0 asymptotic.

Set b(y)=W_2(0,y). The assertion on the upper half-axis assumes b(y)>0 for every y>0. Its lower-half-axis version assumes b(y)<0 for every y<0. Each is a separate hypothesis; either can hold without a statement about equilibria off the axis. In class G, beta>2 and the center is the only zero of W, so both hold.

Dependencies: the exact axis equations independently derived in packet27, the class A derivative expansions in packet36, scalar integrating factors, and the elementary flow representation of vorticity. The last positivity statement additionally uses the complete global-source dynamics and the scattering bijection from packets48 and61.

## 2. Statement

Under the upper-half-axis hypothesis there exist P_+,Q_+>0 such that

    Theta_xx(0,y)=P_+ y^(-1-2nu)[1+O(y^-nu)],
    Omega_x(0,y)=Q_+ y^(-1-nu)[1+O(y^-nu)]                 (2.1)

as y tends to plus infinity. Under the lower hypothesis the corresponding statements hold with |y| and P_-,Q_->0 at minus infinity.

The constants also determine the smooth angular limits at the corresponding vertical direction:

    a(theta)/cos theta -> Q_+ at theta=pi/2,
    a(theta)/cos theta -> Q_- at theta=-pi/2,
    h(theta)/cos^2 theta -> P_+/2 at theta=pi/2,
    h(theta)/cos^2 theta -> P_-/2 at theta=-pi/2.           (2.2)

All these are two-sided angular limits. Thus a'(pi/2)=-Q_+, a'(-pi/2)=Q_-, and h''(plus or minus pi/2)=P_+ or P_-. In particular the vorticity tail is strictly positive just inside either admissible endpoint of the right semicircle, and the temperature tail has a strictly positive quadratic zero there.

Finally, if the profile is in G and Theta_x>=0 on x>0, then

    Omega(Y)>0 for every x>0,
    a(theta)>0 for every -pi/2<theta<pi/2.                (2.3)

There is no exclusion of G or of the full target in these assertions.

## 3. Axis equations and positivity

Put A(y)=Theta_xx(0,y)/2 and q(y)=Omega_x(0,y). Write W_1=x C(x^2,y). The axis divergence equation gives C(0,y)=2beta-b'(y). Expanding the two transport equations at their first nonzero x orders gives exactly

    b A'=[2b'-(3beta+2)]A,
    b q'+[(2beta+1)-b']q=2A.                            (3.1)

The center limits are A(0)=a0>0 and q(0)=4a0/beta>0. On a positive branch, choose a sufficiently small y0>0 where both are positive. The first equation is a scalar homogeneous ODE with continuous coefficient on every compact subinterval of the branch, and hence A remains positive. A positive integrating factor for the second equation shows that its weighted q is strictly increasing from y0 because 2A/b>0. Hence q remains positive as well. Letting y0 be smaller proves both signs on the entire branch. No sign of Omega at off-axis points is used.

For the lower branch set s=-y, bbar(s)=-b(-s), Abar(s)=A(-s), and qbar(s)=q(-s). Direct substitution into(3.1) gives exactly the same two equations with bars and s, with bbar>0 and the same positive center limits. This removes any ambiguity about the orientation of the lower-axis integrating factor.

## 4. Nonzero tail constants

On the upper branch, the class A bounds imply

    b(y)=beta y[1+O(y^-nu)], b'(y)=beta+O(y^-nu).

Consequently

    [2b'-(3beta+2)]/b=-(1+2nu)/y+O(y^(-1-nu)),
    [b'-(2beta+1)]/b=-(1+nu)/y+O(y^(-1-nu)).             (4.1)

The error is absolutely integrable at infinity. Integrating the logarithmic equation for positive A proves

    A(y)=C_A y^(-1-2nu)[1+O(y^-nu)], C_A>0.

The constant is strictly positive because it is the product of a positive finite starting value and the exponential of a convergent real integral. It cannot vanish by cancellation.

Choose a positive solution q_h of the homogeneous second equation, for example normalized by q_h(y0)=1. The second estimate in(4.1) gives

    q_h(y)=C_h y^(-1-nu)[1+O(y^-nu)], C_h>0.

Write q=q_h R. Then

    R'=2A/(b q_h)>0,
    R'=O(y^(-1-nu)).                                   (4.2)

Thus R increases to a finite positive limit R_infinity, with R_infinity-R(y)=O(y^-nu). In particular this limit is at least R(y0)>0. Taking P_+=2C_A and Q_+=C_h R_infinity proves(2.1). The barred equations give the lower constants by exactly the same proof. No beta>2 division was used; this argument includes beta=2.

## 5. Matching the angular limits directly

For the upper axis, polar differentiation at (0,r), r>0, gives the exact identity

    Omega_x(0,r)=-r^-1 partial_theta Omega(r e_theta)|_(theta=pi/2).

For the lower axis it gives the same expression with a plus sign at theta=-pi/2. The j=1 expansion(1.1), followed by(2.1), therefore yields

    -a'(pi/2)=Q_+, a'(-pi/2)=Q_-.

Since a itself vanishes at both endpoints, first-order Taylor expansion and the corresponding derivatives of cos theta prove both limits for a in(2.2). This argument is valid on either half-axis under its own hypothesis and does not require G. It also avoids differentiating an orbit integral.

For temperature, the exact second polar differentiation formula on either axis is

    Theta_xx(0,plus or minus r)
       =r^-1 Theta_r(r e_theta)+r^-2 Theta_thetatheta(r e_theta)

at its endpoint. The first term is zero because Theta vanishes identically on that axis for all positive r. By the j=2 expansion(1.1),

    r^(2-m) Theta_xx(0,plus or minus r)
       =h''(plus or minus pi/2)+O(r^-nu).

Since 2-m=1+2nu, comparison with(2.1) identifies h''=P_+ or P_-. Both h and h' vanish at the endpoint by the axis condition and reflection parity. Second-order Taylor expansion proves h/cos^2 -> P/2. These derivative identifications use uniform derivative estimates already proved for exact profiles, not an assumption of termwise differentiability for approximate numerical fits.

## 6. Positivity under the additional horizontal monotonicity assumption

Suppose now that the profile is in G and f=Theta_x>=0 on the open right half-plane. The smooth factorization Theta=x^2 F(x,y), with F even in x and F(0)=a0>0, follows from smoothness, parity and Theta(0,y)=0. It gives f=x[2F+xF_x]>0 in a sufficiently small neighborhood of0 with x>0.

The axis is invariant, and uniqueness of the smooth flow preserves each open half-plane for every finite time. Every backward orbit in G tends to0. Hence along any orbit starting with x>0, f is nonnegative for all times and strictly positive for all sufficiently negative times. Since Omega is bounded and the backward orbit tends to0, integrating the vorticity equation gives

    Omega(Y)=integral_(-infinity)^0 e^s f(phi_sY)ds>0.    (6.1)

The boundary term e^-T Omega(phi_-T Y) tends to zero by smoothness near0. Integrability follows there from boundedness, independently of its sign.

The full-orbit amplitude is

    A_tr(Y)=integral_(-infinity)^infinity e^s f(phi_sY)ds.

It converges: the negative tail is bounded by a constant times e^s, while at positive times phi_sY escapes with radius comparable to e^(beta s), and gradTheta=O(r^-2nu) makes the positive tail O(e^-s). The integrand is nonnegative and positive on a nonempty interval, so A_tr(Y)>0 on the right half-plane. The previously established scattering identity is

    a(arg Phi(Y))=|Phi(Y)|^nu A_tr(Y).

The smooth scattering map Phi maps that half-plane onto itself: its global bijectivity on the punctured plane, reflection equivariance, and preservation of the sign of the first coordinate imply this. Each direction in the open right semicircle has a preimage there. Thus a is strictly positive in every such direction, proving(2.3).

## 7. Audit, diagnostic scope and nonclaims

This packet independently checks lead notes/draft_4_21.md as read at the timestamp in verification/source.json. Parts(a)-(c) are confirmed. Part(b) can be strengthened by removing G when the corresponding part(a) half-axis hypothesis holds; the existing C1 angular expansion gives a shorter proof. The additional temperature angular limit follows from C2. The lead's orbit-factorization proof also works: the quotient integral is continuous with an integrable uniform majorant, and at xi=0 the transverse difference quotient differentiates only the vanishing prefactor. There is no need to assume differentiability of that quotient integral.

For a candidate, the positive scaled axis limits and their angular matching are necessary under absence of additional axis zeros. A basis that builds these powers and quotient continuity in by construction can satisfy the matching without solving the PDE. Positivity failures are decisive only after checking the relevant branch assumption, normalization and numerical accuracy. These identities do not establish numerical convergence, a full-plane inverse, or a profile.

The proof was written before its small exact-algebra verification script. No teammate solver code was reused. Actual Opus5.5 availability during this shift is recorded separately; the two immediately preceding requests64 and65 returned no audit text and provide no endorsement of this packet. The independently reviewed inverse exchanges62 and63 did return actual model claude-opus-5-5 text. No substitute model is claimed.
