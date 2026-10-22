# Beta-two scattering, weighted production, and canonical moments

Date:2026-10-20. Status: CONFIRMED by independent verifier at 2026-10-20T18:01:37.464056+00:00.
This audits lead beta2d D5-D8. No existence or full nonexistence endpoint.

## 1. Setting and conclusions

Use the full smooth beta2 B2 target, with V=U-U(0), W=2X+V and the
canonical relative kernel K(z)=(z2,-z1)/(2pi|z|^2). Thus div W=4,
Omega=-curl W, W.grad Theta=0, W.grad Omega+Omega=Theta_x. All given
axis conditions and the normalized center jet Theta=x^2+O(r^3) hold.
Packets33,36,38,39 establish smooth angular functions a,h,b and

    V=O(r^{1/2}), DV=O(r^{-1/2}), Omega=O(r^{-1/2}),
    Theta=O(1), grad Theta=O(r^{-1}),
    Omega=r^{-1/2}a+r^{-1}b+O(r^{-3/2}log r),
    Theta=h+O(r^{-1/2}), a not identically0.           (1)

Remainders and their fixed-order derivatives obey the stated scale
bounds. Packet05 supplies the escape-set scattering diffeomorphism
Phi, its area preservation, and its flow conjugacy. Every negative
orbit stays bounded. The complement K of the escape set E has zero
area. No hypothesis on the number of equilibria is imposed except
where explicitly stated in Section7.

The assertions and their proofs are given together below. Angular
coordinate is alpha, e=(cos alpha,sin alpha), eperp=(-sin alpha,cos alpha).
An integral over the full angle circle has measure d alpha.

## 2. Area coordinates and the exact temperature derivative

For Y in E define Phi(Y)=lim_{t->infinity}e^{-2t}phi_tY. On any compact
subset of E, escaping radii satisfy |phi_tY| comparable to e^{2t}
uniformly for large t. Thus DV(phi_tY)=O(e^{-t}). The matrices
M_t=e^{-2t}Dphi_t solve M_t'=DV(phi_tY)M_t. Gronwall bounds them and
the integral of their derivative is finite, uniformly on compact sets.
They converge locally uniformly. Together with the corresponding
uniform function limit this justifies D Phi=lim M_t. Since div W=4,
Liouville's formula gives det M_t=1 and therefore det D Phi=1.
This is an equality of derivatives, not an inference from function
convergence alone.

Put Y_alpha=Phi^{-1}(e(alpha)) and X(t,alpha)=phi_tY_alpha. In scattering
coordinates these are e^{2t}e(alpha). Their positive Jacobian is
2e^{4t}; area preservation gives in the original coordinates

    det(X_t,X_alpha)=2e^{4t}, dX=2e^{4t}dt d alpha.

Inverting the two-column matrix, with X_t=W, gives

    grad alpha=(-W2,W1)/(2e^{4t}),
    Theta_x(X(t,alpha))=-(hprime(alpha)/2)e^{-4t}W2(X(t,alpha)). (2)

The exact representation Theta=h(arg Phi) follows from temperature
transport and the forward limit. No asymptotic differentiation is
being used in(2).

If hprime(alpha)=0, then grad Theta vanishes along the entire orbit
of that direction. There Omega satisfies d Omega/dt=-Omega. Boundedness
on its compact negative semiorbit forces Omega=0 all along that orbit.
In particular

    hprime(alpha)=0 implies a(alpha)=0.               (3)

This holds on the entire circle without the assumption Z=gamma.

Suppose a direction's orbit has backward limit q at an interior point
of the equilibrium arc. The elementary fibre coordinates in45 give
X(t,alpha)-q=O(e^{4t}) and W(X)=O(e^{4t}) as t->-infinity, uniformly
on compact intervals of such directions. Integrating the vorticity
ODE with its factor e^t at both ends gives

    a(alpha)=int_R e^t Theta_x(X(t,alpha))dt
      =-(hprime/2)int_R e^{-3t}W2(X(t,alpha))dt
      =-(3hprime/2)int_R e^{-3t}(X2(t,alpha)-q2)dt.    (4)

The integrands in the last two integrals are O(e^t) at negative
infinity and O(e^{-t}) at positive infinity. They are absolutely
integrable, and integration by parts in t has zero endpoint values.
These unmultiplied integrals are not asserted for a slowly approaching
endpoint-basin orbit. There the separate conclusion is hprime=a=0;
no zero times a divergent integral is written.

## 3. Global scalar resolvent and weighted critical production

Everywhere on R2, integration backward gives

    Omega(Y)=int_{-infinity}^0 e^t Theta_x(phi_tY)dt.  (5)

Its omitted endpoint is e^{-T}Omega(phi_{-T}Y), tending to0 because
the negative orbit is compact. The gradient source is globally bounded
by(1) and smoothness on compact sets, so the integral is absolute.

Let F be C1 on a neighborhood of the compact temperature range. Direct
product differentiation with both transport equations gives

    div(F(Theta) W Omega^4)=4F(Theta)Omega^3 Theta_x.

The volume integrand is O(r^{-5/2}), hence absolutely integrable. On a
large circle the outward flux density satisfies uniformly

    F(Theta)Omega^4(W.e)r ->2F(h)a^4.

The divergence theorem on disks, followed by these justified limits,
proves the finite identity

    int_R2 F(Theta)Omega^3 Theta_x dX
                        =(1/2)int_S1 F(h)a^4 d alpha. (6)

The far-field flux is retained, not set to zero.

For any bounded Borel function g on S1 there is the more resolved identity

    int_E g(arg Phi)Omega^3 Theta_x dX
                        =(1/2)int_S1 g(alpha)a^4 d alpha. (7)

For a fixed direction the exact derivative of e^{4t}Omega(X)^4 is
4e^{4t}Omega^3 Theta_x(X). Its endpoints are0 and a(alpha)^4. Use the
Jacobian in Section2 and Fubini, justified by the absolute volume bound
already checked. No derivative of g, and no extension of g across K,
is involved. The finite signed measure obtained by integrating over
complete orbits is nonnegative; no pointwise sign of its density follows.

For almost every regular value c of h, coarea gives

    int_{Theta=c} Omega^3 Theta_x/|grad Theta| dH1
          =(1/2)sum_{alpha:h(alpha)=c} a(alpha)^4/|hprime(alpha)|. (8)

To justify this, set the ratio to0 where grad Theta=0, and apply coarea
to the absolutely integrable signed density Omega^3 Theta_x. The
critical set of h contributes no measure to the pushforward on the
right of(6), because a=0 there by(3). The circle coarea formula supplies
its displayed density. A regular value has a finite preimage, by
compactness and the inverse function theorem. Comparing the two
pushforward measures proves(8) almost everywhere. It is not a claim
of convergence for every exceptional level.

## 4. Strain, axis velocity, and an absolute characteristic inverse

Differentiating the canonical relative inverse gives

    2=V2_y(0)=(1/pi)int_R2 xy Omega(x,y)/(x^2+y^2)^2 dxdy. (9)

The off-diagonal derivative kernel has no delta term. At0 Omega=O(r),
so the absolute radial integrand is O(1); at infinity it is O(r^{-3/2}).
This makes the distributional derivative an ordinary absolute integral,
or permits differentiation after deleting and then shrinking a small
ball with its Taylor remainder controlled. The strain sign is the
prompt's Omega=-curl V sign.

For each fixed y the axis field is

    W2(0,y)=2y+(1/(2pi))int_R2 x Omega(x,eta)
            [1/(x^2+(y-eta)^2)-1/(x^2+eta^2)]dx d eta. (10)

The two terms must stay combined. Their full vector kernel difference
is O(|y|r^{-2}) at infinity, giving absolute convergence with(1). Both
finite kernel singularities are locally integrable. This is a full-plane
inverse; no wall or horizontal reflection has entered.

For the interior-fibre directions of(4), the identity W(q)=0 implies
W2(X)=2(X2-q2)+V2(X)-V2(q). The last integral in(4) therefore also equals
the integral of e^{-3t}[V2(X)-V2(q)]: integration by parts gives the W2
integral as3 times the displacement integral, while the displayed field
identity gives2 times that integral plus the velocity difference. Hence

    a=-(3hprime/2)int_R e^{-3t}[V2(X(t,alpha))-V2(q)]dt
      =-(3hprime/2)int_R2 Omega(Z) int_R e^{-3t}
              [K2(X(t,alpha)-Z)-K2(q-Z)]dt dZ.        (11)

The order exchange is absolute. For d=|X-q|<=1/2, divide the Z plane
into the O(d) neighborhoods of the two singularities, the intermediate
annuli, and the exterior. Bounded Omega and the O(r^{-2}) kernel
derivative give

    int |Omega(Z)| |K(X-Z)-K(q-Z)|dZ
                              <=C d(1+|log d|).

The small neighborhoods contribute O(d), the annuli O(d|log d|), and
the decaying far field O(d). For |X| large, splitting at radii comparable
to |X|, including its kernel neighborhood, gives a bound C(1+|X|^{1/2}).
On a fibre these bounds are C(1+|t|)e^{4t} at negative infinity and
Ce^t at positive infinity. Their products with e^{-3t} are integrable.
There is no definite sign for the kernel difference in(11).

## 5. Resonance and the normalized velocity constant

Use P=-f, where f is the angular coefficient of the physical stream
Psi in38. Then P solves P''+(9/4)P=a, and

    u0_r=Pprime, u0_theta=-(3/2)P.

Thus P belongs to the negative stream -Psi; this explicitly translates
the alternate stream convention used in the lead source. The physical
kernel and Omega=-curl V have not changed. The second vorticity balance is

    b=-(3/2)P aprime-(1/2)Pprime a+sin(alpha)hprime.

Let b1=(1/pi)int b cos(alpha). Reflection makes int b sin(alpha)=0.
Multiplying by cos and integrating by parts gives

    int b cos=int a Pprime cos-(3/2)int a P sin-int h cos(2alpha).

Using a=P''+(9/4)P in the first two terms gives, respectively,

    (1/2)int (Pprime)^2 sin+(9/8)int P^2 sin,
    (3/2)int (Pprime)^2 sin-(21/8)int P^2 sin.

Therefore, for any constant L,

    pi b1=int sin(alpha)[2(Pprime)^2-(3/2)P^2]
                                      -int (h-L)cos(2alpha). (12)

All integrals are ordinary smooth periodic integrals. No sign is implied.
In the Z=gamma subclass h=L on the endpoint arcs, but neither remaining
term is forced to vanish.

Fix the angular normalization by defining Q orthogonal to the two first
harmonics, solving Q''+Q=b-b1 cos(alpha). Set

    B_b=Qprime e-[Q+(b1/2)cos(alpha)]eperp.

This is exactly B_b in38 after Q=-g. Its angular mean is
-(b1/4)(0,1). The actual velocity expansion is

    V=r^{1/2}u0-(b1/2)log r(0,1)+B_b+C(0,1)
                                             +O(r^{-1/2}log r). (13)

Let Ac=int a cos and define the actual circular cutoff moment

    m(R)=(1/(2pi))int_{|Z|<R} Z1 Omega(Z)/|Z|^2 dZ.

The remainder in(1) is integrable in its radial moment, so the finite
part exists:

    mstar=lim_{R->infinity}[m(R)-(Ac/pi)sqrt R-(b1/2)log R].

Near0 the moment is finite because Omega=O(r). At infinity its remaining
radial integrand is O(r^{-3/2}log r), which is integrable. With the
normalization just fixed,

    C=b1/4-mstar.                                     (14)

Here is an independent finite-cutoff proof. For fixed Z off the circle,
the angular mean of K(Re(alpha)-Z) is0 when |Z|<R and K(-Z) when |Z|>R.
Expand the reciprocal complex function in a convergent geometric series
on either region and average its integer Fourier modes. Integrate first
only over |Z|<M, M>2R. Fubini is valid even near the exceptional circle:
the kernel singularity is locally integrable in the joint variables.
It follows that

    mean_alpha V(Re(alpha))=-m(R)(0,1).

Pass M to infinity using the uniform tail bound C R M^{-1/2} for the
relative integral. The leading velocity mean is -(Ac/pi)(0,1): its
vertical component is Pprime sin-(3/2)P cos; integration by parts and
int a cos=(5/4)int P cos give the factor. Averaging(13) now proves(14).
C is fixed by the whole profile and this normalization. It is not a
free observer velocity. A differently normalized B_b changes its written
constant while leaving V unchanged.

## 6. Independent manufactured checks

verification/algebra.json records exact Laurent-polynomial checks of
(12), the inverse equation for Q, both means of B_b and u0, and the
vanishing sine first harmonic. The independent polynomial test is

    P=(5/9)cos alpha-(3/11)sin2alpha+(2/13)cos5alpha+(1/7)sin6alpha,
    h=cos^2 alpha[1+(2/9)sin alpha+(3/10)sin^2 alpha].

The identities hold by their proofs for arbitrary smooth data; this
finite test is a check of implementation and signs only.

A separate smooth kinematic manufacture is

    Psi=x{A[(1+r^2)^{1/4}-1]+(D/2)log(1+r^2)},
    A=2/7, D=-3/5, V=(-Psi_y,Psi_x), Omega=-Delta Psi.

It has V(0)=0 and a canonical sublinear whole-plane inverse, but is not
a B2 solution. It has a=-(5A/4)cos, b1=-2D, C=-A and
mstar=A-D/2. These exact constants follow by differentiating Psi and
expanding its circular velocity mean. A separately evaluated radial
moment, sampled angular velocity mean, and the verifier's Cartesian
Duffy/infinite-exterior inverse are compared in moment_manufacture.json.
The moment finite part is tested at increasing finite radii, not treated
as exact there. No candidate is validated by this manufacture.

## 7. Axis consequences under the weaker single-axis-zero hypothesis

Suppose only that W has no zero on the invariant axis other than0.
This follows from Z=gamma, but no global zero-set restriction is needed
for this section. Write B(y)=W2(0,y), A(y)=Theta_xx(0,y)/2 and
q(y)=Omega_x(0,y). The exact divided equations are

    B Aprime=(2Bprime-8)A,
    B qprime+(5-Bprime)q=2A,                         (15)

with Bprime(0)=4, A(0)=1 and q(0)=2. The single-zero hypothesis and
outgoing tail imply B>0 on y>0 and B<0 on y<0. Its axis orbits tend
backward to0. The scalar first equation has no zero crossing, so A>0.
Moreover

    Aprime/A=-2/y+O(|y|^{-3/2}),

and therefore A(+-s)=A_+- s^{-2}(1+O(s^{-1/2})) with A_+>0 and A_->0.
The positivity notation means each constant A_+, A_- is strictly
positive. This follows by integrating the absolutely integrable error
in log(A y^2), separately on the two half axes.

Along either axis orbit the second equation has variation of constants

    q(y(t))=int_{-infinity}^t 2A(y(s))
       exp[-int_s^t(5-Bprime(y(u)))du]ds >0.          (16)

Its past coefficient tends to1 and q stays bounded, so the omitted
endpoint vanishes; the past integral is exponential. Positivity of
5-Bprime everywhere is not required.

In fact q has strictly positive leading tail constants as well. On
y=s>0 let I(s)=exp(int_{s0}^s(5-Bprime)/B). Then
I(s)=c s^{3/2}(1+O(s^{-1/2})), c>0, and

    (I q)prime=2I A/B >0,

whose right side is O(s^{-3/2}). Thus Iq increases to a finite strictly
positive limit. The substitution Bminus(s)=-B(-s), Aminus(s)=A(-s),
qminus(s)=q(-s) gives precisely the same equations. Consequently

    q(+-s)=q_+- s^{-3/2}(1+O(s^{-1/2})), q_+>0 and q_->0. (17)

In(17) each named constant is strictly positive.

The C2 scaled-annulus convergence of Theta gives directly
Theta_xx(0,+-r)=r^{-2}hsecond(alpha_+-)+o(r^{-2}), since h=0 and
hprime=0 at the vertical angles by parity and the axis condition.
Similarly C1 convergence of Omega gives
q(r)=-r^{-3/2}aprime(pi/2)+o(r^{-3/2}) and
q(-r)=r^{-3/2}aprime(3pi/2)+o(r^{-3/2}). Compare(17) to obtain

    h(pi/2)=h(3pi/2)=0,
    hsecond(pi/2)=2A_+>0, hsecond(3pi/2)=2A_->0,
    aprime(pi/2)=-q_+<0, aprime(3pi/2)=q_->0.         (18)

This supplies a separate proof of the lead's axis signs, without
differentiating an infinite orbit integral. It shows a is positive
just inside the right half-plane next to both vertical directions.
It gives no sign between these neighborhoods.

## 8. Scope and dependencies

Equations(2)-(14) hold in the full beta2 target, with(4) and(11) limited
to interior-fibre directions. Equations(15)-(18) require only the stated
single-axis-zero hypothesis. The Z=gamma subclass from53 satisfies it.
None of the critical, moment or sign identities excludes that entire
subclass. No divergent integral has been split or discarded. Formal
sources are absent because Lean/Lake execution is prohibited; verification
contains the independently generated algebra and inverse checks.
