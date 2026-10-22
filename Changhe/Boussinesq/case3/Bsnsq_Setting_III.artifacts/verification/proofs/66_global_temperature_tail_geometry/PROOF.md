# Positive global-source temperature tail and angular area geometry

Date:2026-10-20. Status:CONFIRMED by the independent verifier with complete arguments below. The counterexample concerns a proposed geometric implication, not the coupled B2 equation. No full endpoint is claimed.

## 1. Setting and dependencies

Let beta>2, nu=1/beta, lambda=(beta-2)/2, mu=(3beta+2)/2, m=1-2nu. Assume a smooth class G B2 profile with a0>0. Thus the complete field W=beta Y+V has only zero0, every nonzero backward orbit tends to0, and every nonzero forward orbit escapes to infinity, as proved in packet48. Its reflection symmetry is (x,y)->(-x,y). Packets33,36,40 give class A bounds and smooth uniform angular tails

    Theta(r e_theta)=r^m h(theta)+O_{C^j(theta)}(r^(m-nu)),
    V=O(r^(1-nu)), DV=O(r^-nu).

Packet48 constructs smooth global area coordinates Xi(Y)=(xi,eta), with Xi(0)=0, DXi(0)=I, xi having the sign of x, and

    Theta=a0 xi^2, W.grad xi=lambda xi,
    W.grad eta=mu eta+kappa xi^k.

The resonant term can be present only if mu=k lambda and k is even. We retain it unless explicitly stating kappa=0. Packet61 gives a smooth area-preserving scattering diffeomorphism Phi of the punctured plane, preserving each half-plane and commuting with reflection, such that

    Phi(phi_tY)=e^(beta t)Phi(Y),
    Phi(Y)=Y+O(r^(1-nu)), DPhi(Y)=I+O(r^-nu).             (1.1)

The inverse satisfies the corresponding first estimate at infinity. To justify that its large arguments have large preimages, first extend Phi continuously by Phi(0)=0. Near the hyperbolic source the radial velocity is between c r and C r for positive constants c,C. Every small Y!=0 reaches a fixed small source circle after a finite time tau_Y, with tau_Y>=(1/C)log(rho/|Y|). By the conjugacy, |Phi(Y)|=e^(-beta tau_Y)|Phi(phi_(tau_Y)Y)|, whose last factor is uniformly bounded on that circle. Hence Phi(Y)->0 uniformly as Y->0. Phi is consequently bounded on each bounded physical set. Thus |Z|->infinity implies |Phi^-1(Z)|->infinity; otherwise a bounded preimage subsequence would have bounded images. Now(1.1) compares the radii of Phi(Y) and Y for large Y, and rearrangement proves the claimed inverse estimate. Packet65 supplies the strictly positive axis constants P_+,P_- and h/cos^2 ->P_+/2,P_-/2.

Dependencies are exactly these proved statements, elementary transport and differentiation, the scalar inverse function theorem, and Taylor expansion. No spectral, elliptic or Hamiltonian existence theorem is invoked in the counterexample.

## 2. Positive tail in all of G, including resonance

For every Y!=0, the temperature has the exact representation

    Theta(Y)=|Phi(Y)|^m h(arg Phi(Y)).                   (2.1)

Indeed temperature transport gives Theta(phi_tY)=e^((beta-2)t)Theta(Y). Divide by e^((beta-2)t) and use the angular asymptotic along phi_tY, whose rescaled position tends to Phi(Y). Since beta m=beta-2, taking t to infinity gives(2.1). The error is O(e^-t), and the continuous angular limit is enough for this argument.

The scalar eigen-coordinate has the exact homogeneous representation in scattering coordinates

    xi(Phi^-1(r e_theta))=r^alpha q(theta),
    alpha=lambda/beta=1/2-nu,                           (2.2)

where q(theta)=xi(Phi^-1(e_theta)) is smooth and periodic. Its sign is the sign of cos theta. There is no resonance qualification for(2.2), since xi is always an exact eigen-coordinate. Comparing Theta=a0 xi^2 with(2.1) gives

    h(theta)=a0 q(theta)^2.                             (2.3)

Consequently h>0 at every nonvertical direction. On the right semicircle q>0; on the left q<0. The only angular zeros of h are the two vertical directions. By packet65 both are exactly quadratic zeros with strictly positive second derivatives.

This also follows without naming xi: Phi^-1(e_theta) lies off-axis at every nonvertical angle, and Theta=a0 xi^2 is positive there. Formula(2.1) then gives h(theta)>0. Thus resonance cannot create an interior zero in the temperature tail.

## 3. Uniform two-sided temperature bounds

Define the smooth axis quotient F(Y)=Theta(Y)/x^2 off the axis, extended by F(0,y)=Theta_xx(0,y)/2. There exist constants 0<c<C<infinity, depending on the profile, such that on the whole plane

    c(1+|Y|)^(-1-2nu) <= F(Y) <= C(1+|Y|)^(-1-2nu).     (3.1)

In particular the temperature does not converge to a faster tail along a shrinking angular sector in G.

First, F is strictly positive everywhere. Away from the axis this follows from Theta=a0 xi^2 and xi!=0. On the axis the derivative xi_x is nonzero: the parity-equivariant area map has diagonal derivative there, with determinant1, so neither diagonal entry vanishes. Its sign is positive by continuity along the connected axis and DXi(0)=I. Hence F(0,y)=a0 xi_x(0,y)^2>0. At the center F(0)=a0.

Next define B(theta)=h(theta)/cos^2 theta off the vertical directions and extend it by P_+/2 and P_-/2 there. Packet65 and smoothness show that B is continuous and strictly positive on the full circle. Compactness gives a positive minimum and finite maximum.

For each large r let E_r(theta)=r^-m Theta(r e_theta)-h(theta). The C2 angular expansion gives ||E_r||_{C2}<=C r^-nu. Moreover E_r and E_r' vanish exactly at each vertical direction: the first by the axis condition, the second by reflection symmetry. Taylor's integral formula near each endpoint therefore gives |E_r(theta)|<=C r^-nu dist(theta,axis angles)^2. The ratio of that squared distance to cos^2 theta stays bounded in fixed endpoint neighborhoods. Outside those neighborhoods cos^2 is bounded below. Thus globally

    r^(1+2nu) F(r e_theta)=B(theta)+O(r^-nu)             (3.2)

uniformly, including on the axis by continuous extension. The positive minimum of B proves(3.1) outside a sufficiently large disk. Strict positivity and continuity of F on the remaining compact disk finish the proof. This is an exact-profile conclusion; a numerically positive tail alone does not establish it.

## 3a. A universal vorticity exponent along fixed positive temperature levels

Fix a temperature value T>0 and restrict to the right half-plane. For every sufficiently large positive y and every sufficiently large negative y, the level Theta(x,y)=T has exactly one point with x>0. These points form smooth end graphs x=x_T(y). With p=1/2+nu and delta=min(nu,1-2nu)>0,

    x_T(y)=sqrt(2T/P_+) y^p[1+O(y^-delta)]              at plus infinity,
    x_T(y)=sqrt(2T/P_-) |y|^p[1+O(|y|^-delta)]          at minus infinity,
    Omega(x_T(y),y)=Q_+ sqrt(2T/P_+) y^(-1/2)
                                 [1+O(y^-delta)]       at plus infinity,
    Omega(x_T(y),y)=Q_- sqrt(2T/P_-) |y|^(-1/2)
                                 [1+O(|y|^-delta)]    at minus infinity. (3.3)

The exponent1/2 in the last two formulas is independent of beta. These are far-end graphs only; the whole level curve can have folds at finite y.

Here is a proof with the shrinking-sector issue made explicit. The lower bound(3.1) at any large level point gives x/r=O(r^(-m/2)), since T>=c(x/r)^2 r^m for large r. Thus every such point approaches one of the vertical directions, r/|y|=1+O(|y|^-m), and x=O(|y|^p). On the upper end the smooth angular quotient B=h/cos^2 is even about pi/2, so B=P_+/2+O((theta-pi/2)^2). Formula(3.2) then yields, uniformly at these possible level points,

    F(x,y)=(P_+/2)y^(-1-2nu)[1+O(y^-delta)].

The same formula also holds uniformly for each bounded range of x/y^p. Choosing two constants on either side of sqrt(2T/P_+) and setting x to those constants times y^p gives temperatures respectively below and above T for large y, hence at least one root.

For uniqueness, the full spatial C2 convergence from packet36 gives Theta_xx>0 in a fixed sufficiently narrow cone around the upper axis, once r is large: the limiting scaled Hessian has Theta_xx=P_+>0 at the unit upper-axis point and is continuous nearby. Since Theta_x(0,y)=0, integration in x gives Theta_x>0 for 0<x<epsilon y there. Every possible large level point lies in this cone by the previous bound. Strict monotonicity in x proves uniqueness, and the implicit function theorem makes the root a smooth graph. The lower end is identical with P_-.

For vorticity define B_Omega=a/cos theta. Its smooth extension at the upper endpoint is Q_+, and it too is even about that endpoint. The uniform C1 angular expansion and a first-order vanishing-factor division give

    Omega(x,y)/x=r^(-1-nu)[B_Omega(theta)+O(r^-nu)].

Thus on the graph Omega/x=Q_+ y^(-1-nu)[1+O(y^-delta)], using B_Omega=Q_++O((theta-pi/2)^2). Substituting the proved x_T asymptotic gives p-1-nu=-1/2. The lower end is the same. No positivity of Omega away from these end regions is presumed.

## 4. Additional angular geometry in the linear normal form

Only in this section and section5 assume kappa=0. Put

    alpha=lambda/beta, gamma=mu/beta, alpha+gamma=2,
    H=Xi composed with Phi^-1.

Both maps preserve area and are smooth on their domains. Their conjugacies give

    H(r e_theta)=(r^alpha q(theta),r^gamma g(theta)),     (4.1)

with smooth periodic q,g. Calculating the polar Jacobian, and dividing by the polar area factor r, yields the exact identity

    alpha q g' - gamma q' g=1.                         (4.2)

At an axis angle q=0. Therefore q' and g are both nonzero there. Since q>0 between -pi/2 and pi/2, its lower endpoint derivative is positive and its upper endpoint derivative is negative. Equation(4.2) implies

    g(-pi/2)<0, g(pi/2)>0.

On the open right semicircle,

    (g/q^(gamma/alpha))'
       =1/[alpha q^(1+gamma/alpha)]>0.                 (4.3)

The quotient tends to minus infinity at the lower endpoint and plus infinity at the upper endpoint. Hence it has exactly one zero. At that zero(4.2) gives g'=1/(alpha q)>0. Reflection gives exactly one further zero in the left semicircle. There are no axis zeros of g. Thus an unqualified global assertion |eta| comparable to r^gamma is impossible: its angular leading coefficient necessarily vanishes in two nonvertical directions. This does not prevent a direction-dependent asymptotic statement.

Composing(4.1) with Phi and using(1.1) gives uniformly in angle

    xi(Y)=r^alpha q(theta)+O(r^(alpha-nu)),
    eta(Y)=r^gamma g(theta)+O(r^(gamma-nu)),
    xi_x(Y)=r^(alpha-1)[alpha cos theta q(theta)-sin theta q'(theta)]
                          +O(r^(alpha-1-nu)).          (4.4)

For the derivative estimate, each component of H is ordinarily homogeneous of the displayed degree. Its first and second derivatives are therefore bounded by the corresponding powers of r on annuli. In DH(Phi(Y))DPhi(Y), the shift of its argument contributes O(r^(alpha-2) r^(1-nu)) to the first row, and DPhi-I contributes O(r^(alpha-1-nu)). This proves the third line with the stated error. No derivative of a C0 remainder or logarithmic resonance is used. For X=Xi^-1, detDX=1 gives y_eta(Xi(Y))=xi_x(Y).

Equation(4.2) alone does not force the leading bracket in(4.4) to be positive. The following global punctured-plane example proves this limitation.

## 5. Explicit counterexample to geometric horizontal monotonicity

Choose any 0<alpha<1 and gamma=2-alpha. Define the increasing angle lift

    theta0(u)=u+(alpha-gamma) sin(2u)/4.

Its derivative is alpha cos^2 u+gamma sin^2 u>0, and theta0(u+2pi)=theta0(u)+2pi. Let u(theta) be its global smooth inverse. Then

    H0(r e_theta)=(r^alpha cos u(theta),r^gamma sin u(theta))

is a smooth area-preserving diffeomorphism of the punctured plane onto itself, preserving the two half-planes and commuting with reflection. Its determinant is1 since

    [alpha cos^2 u+gamma sin^2 u]u'=1.

For global bijectivity, given (xi,eta)!=0 solve

    xi^2 r^(-2alpha)+eta^2 r^(-2gamma)=1.

The left side strictly decreases from infinity to zero, so there is a unique r>0, smoothly depending on the point by its nonzero radial derivative. The normalized pair determines u modulo2pi and then theta uniquely modulo2pi. Reflection follows from theta0(pi-u)=pi-theta0(u).

Now choose an even integer M and 0<epsilon<1, and define

    f(theta)=theta+(epsilon/M)sin(M theta),
    T(r e_theta)=r/sqrt(f'(theta)) times e_(f(theta)).

Since f'=1+epsilon cos(M theta)>0, this is another global smooth punctured-plane diffeomorphism. It is ordinarily homogeneous of degree1 and has determinant1: the polar area Jacobian is [1/f']f'=1. Even M gives f(pi-theta)=pi-f(theta), so it has the same parity and preserves half-planes. The composition H=H0 composed with T is therefore a global smooth area-preserving weighted-homogeneous diffeomorphism of exactly the kind used in(4.1). Its angular functions are

    q=(f')^(-alpha/2) cos u(f(theta)),
    g=(f')^(-gamma/2) sin u(f(theta)).                   (5.1)

For an explicit negative bracket set beta=3, alpha=1/6, gamma=11/6, epsilon=1/2, M=98, theta*=pi/4. At that point,

    f'=1, f''=-49, f=pi/4+1/196,
    q'/q=49/12 - tan u/[alpha cos^2 u+gamma sin^2 u],    (5.2)

where u=u(f(theta*)). We have pi/3<u<5pi/12. Indeed

    theta0(pi/3)=pi/3-5sqrt(3)/24 < pi/4+1/196,
    theta0(5pi/12)=5pi/12-5/24 > pi/4+1/196,

and theta0 is strictly increasing. The inequalities follow already from 3<pi<4 and 5sqrt(3)>8. On this interval tan u<2+sqrt(3)<4 and

    alpha cos^2 u+gamma sin^2 u >=(11/6)(3/4)=11/8.

It follows from(5.2) that

    q'/q > 49/12-32/11=155/132 > 1/6=alpha.

Since q>0 at theta*,

    alpha cos(theta*)q-sin(theta*)q'
       =(q/sqrt(2))(alpha-q'/q)<0.                     (5.3)

This is an exact strict inequality, not an inference from a sampled plot. All-circle smoothness, parity, area and global bijectivity have been proved explicitly. The example is smooth on the punctured plane, as required for H; it is not asserted to extend smoothly through0, to arise from a B2 profile, or to satisfy the coupled vorticity equation. Its sole role is to refute a deduction of the horizontal sign from the angular area geometry alone. It does not refute an additional sign theorem that could use the full PDE.

## 6. Scope and verification

The positive temperature tail and two-sided bound(3.1) hold for all G, including the triangular resonance. The eta homogeneity and angular area identity are only in the smooth linearizable case. The counterexample addresses precisely the geometric hypotheses in section5, not the existence of an admissible flow with that asymptotic map.

The proof was written before its own numerical check of the explicit angle inverses and the negative bracket. Those checks are diagnostic, while the determinant and sign arguments above are exact. No numerics-lane code is used. Actual Opus request65, made before the explicit counterexample was found, returned model claude-opus-5-5 but NO_AUDIT_TEXT/refusal; it supplies no review or endorsement. Earlier written Opus inverse reviews62/63 remain documented independently. No unavailable review is counted as mathematical evidence.

Actual Opus66 returned model claude-opus-5-5 at19:52:30Z with a written audit of sections1-3, but the final paragraph was cut off by max_tokens. Its explicit initial verdict accepted the representation, angular positivity and two-sided bound. The verifier checked the argument and adopted its substantive clarification: forward escape is now explicit, and the source-circle estimate proves Phi extends continuously at0 before using the inverse infinity estimate. The redundant source-basin citation was removed. Its suggested global distance-to-axis inequality is correct but optional; the original neighborhood proof is retained. The statement that determinant1 is stronger than necessary is not a defect, since area preservation is a granted hypothesis.

Opus67 was a follow-up with those repairs and the new level-curve section3a. It returned actual claude-opus-5-5 at19:53:50Z with NO_AUDIT_TEXT/refusal. Therefore section3a and the angular counterexample have the complete independent verifier proof but no written Opus audit. The unavailable follow-up is not counted as endorsement or a mathematical objection.
