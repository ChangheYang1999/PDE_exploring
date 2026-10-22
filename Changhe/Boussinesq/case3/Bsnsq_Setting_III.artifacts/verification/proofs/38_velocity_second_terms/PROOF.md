# Velocity second terms and the beta-two logarithmic resonance

Date:2026-10-20. Status: CONFIRMED by the independent verifier after two actual Opus5.5 exchanges.
These are necessary asymptotics of a hypothetical exact class A profile,
not an existence or nonexistence endpoint.

## 1. Hypotheses, notation and statement

Assume a smooth exact B2 profile in the power-decaying class A, with
beta>=2, the canonical relative inverse V=U-U(0), and the nontrivial
center data. Explicitly, Omega is odd and Theta is even under
(x,y)->(-x,y), and Theta=0 on the axis. Put s=1/beta and m=1-2s. Use standard polar coordinates
X=r e(theta), e=(cos theta,sin theta), e_perp=(-sin theta,cos theta).
The inverse kernel is K(z)=(z2,-z1)/(2pi|z|^2), and

    V(X)=int [K(X-Y)-K(-Y)] Omega(Y) dY.

Packets33 and36 give smooth a,h,b,d on the circle, a not identically0,
with

    Omega(r e)=r^-s a+r^-2s b+o_Cj(r^-2s),
    Theta(r e)=r^m h+r^(m-s)d+o_Cj(r^(m-s))             (1)

for every finite j. Here Cj(S1) denotes angular derivatives. The
corresponding scaled-annulus statement means that each Cartesian
derivative of a remainder gains one additional factor r^-1, uniformly
on annuli whose inner and outer radii are fixed multiples of r. Define homogeneous functions

    omega0(X)=r^-s a(theta), theta0(X)=r^m h(theta),
    u0=K_rel omega0,
    omega1=u0.grad omega0-partial_x theta0,
    theta1=u0.grad theta0.

Then omega1=r^-2s b and theta1=r^(m-s)d. Let f be the unique smooth
periodic solution of

    -[f''+(2-s)^2 f]=a.                                (2)

There is no angular resonance since 3/2<=2-s<2. The leading velocity
is u0(r e)=r^(1-s)[-f'e+(2-s)f e_perp].

If beta>2, the next velocity term is also a homogeneous relative inverse:

    u1=K_rel omega1,
    V(r e)=r^(1-s)u0(e)+r^(1-2s)u1(e)
                                      +o_Cj(r^(1-2s)). (3)

It is obtained from the unique smooth periodic solution g of
-[g''+(2-2s)^2g]=b, by u1(e)=-g'e+(2-2s)g e_perp.
Here1<2-2s<2, so there is again no resonance.

At beta=2, define

    b1=(1/pi) int_0^{2pi} b(theta) cos theta dtheta.

The sine first harmonic is zero by x reflection. Let g be the unique
smooth periodic function orthogonal to both first harmonics satisfying

    -(g''+g)=b-b1 cos theta.

There is a uniquely determined scalar C such that

    V(r e)=r^(1/2)u0(e)-(b1/2)log r (0,1)
                          +B_b(theta)+C(0,1)
                          +O_Cj(r^-1/2 log r),          (4)

where

    B_b=-g'e+g e_perp
                 +(b1/2)(cos theta sin theta,-cos^2 theta).

The coefficient C is fixed by the canonical inverse and the whole
profile. It is not a free fitted drift. The logarithm may have zero
coefficient; no claim that b1 is nonzero is made.

At beta=2 the remainders in(1) improve to

    Omega=r^-1/2 a+r^-1 b+O_Cj(r^-3/2 log r),
    Theta=h+r^-1/2 d+O_Cj(r^-1 log r).                 (5)

All estimates hold for sufficiently large r and every fixed j, with
profile-dependent constants. They assert no convergent all-orders
series and no finite-energy or bounded-data blowup construction.

## 2. Homogeneous inverse and physical rescaling

For0<sigma<1 and a smooth angular coefficient q, the relative inverse
of r^-sigma q is absolutely integrable at Y=0, at Y=X and at infinity.
Near0 its subtraction term is bounded by C |Y|^-1-sigma, with radial
integral int_0^1 rho^-sigma d rho. At infinity the kernel difference
is O_X(|Y|^-2), giving int_1^infinity rho^-1-sigma d rho. Scaling the
absolutely convergent integral shows that the velocity is homogeneous
of degree1-sigma. The corresponding stream has degree2-sigma and
its angular equation gives(2) or its sigma=2s version. Uniqueness also
follows because two such velocities have entire harmonic difference
in the distributional sense, sublinear growth and zero value at0.
The singularity of the source at0 is locally integrable; no point mass
is added by the homogeneous stream since2-sigma>1.

For tau>0 define physical fields at t=-tau by

    u_tau(z)=tau^(beta-1)V(tau^-beta z),
    omega_tau(z)=tau^-1 Omega(tau^-beta z),
    theta_tau(z)=tau^(beta-2)Theta(tau^-beta z).

The exact equations are

    partial_tau omega_tau=u_tau.grad omega_tau-partial_x theta_tau,
    partial_tau theta_tau=u_tau.grad theta_tau.         (6)

From36, all three fields converge in every spatial Cj norm locally
off0 to u0,omega0,theta0, and

    omega_tau=omega0+tau omega1+o_Cj(tau),
    theta_tau=theta0+tau theta1+o_Cj(tau).              (7)

The kernel scaling gives u_tau=K_rel omega_tau exactly. Uniform global
bounds from(1), enlarged on the smooth core, imply

    |Omega(X)-omega0(X)|
                    <=C min(|X|^-s,|X|^-2s), X!=0.

Consequently, writing rho=|z|,

    |omega_tau(z)-omega0(z)|
                    <=C min(rho^-s,tau rho^-2s).        (8)

This estimate is global in z and is the input for the inverse limits.

## 3. Second velocity term for beta>2

Now2s<1. Divide(8) by tau and use the bound C rho^-2s.
The relative-kernel product is absolutely integrable at0 and infinity
by section2 and near a fixed z!=0 by local boundedness. On compact
annuli, dominated convergence and(7) give

    (u_tau-u0)/tau -> K_rel omega1=u1

uniformly. Uniformity can be proved by splitting small balls around0
and around the evaluation point, a large exterior, and a compact
remaining region. Their first, second and exterior contributions are
uniformly small; convergence is uniform on the remaining region.

Convergence also holds in every spatial Cj norm locally off0. One
way to justify this without differentiating a singular kernel is the
interior Poisson estimate: any div-curl field v satisfies
Delta v=(partial_2 omega,-partial_1 omega). On nested compact balls,
its W^{k+2,p} norm is bounded by its local Lp norm and the W^{k,p}
norm of this source. Apply that estimate to
(u_tau-u0)/tau-u1. The velocity converges uniformly and its vorticity
converges in every local Cj by(7), so the required Sobolev norms tend
to zero and embedding gives the claim. Cover compact annuli by finitely
many balls. This proves(3) after tau=r^-s and scaling.

## 4. Borderline inverse estimate at beta=2

Here s=1/2 and(8) becomes

    |omega_tau-omega0|<=C min(rho^-1/2,tau rho^-1).

For z in a compact annulus, split the relative inverse into a small
fixed ball about Y=0, a small ball about Y=z, the far exterior, and
the remaining compact set. The last three parts are O(tau). In the
ball about0 the only borderline factor is K(-Y), and its radial
bound is

    int_0^c min(rho^-1/2,tau rho^-1) d rho
                                       <=C tau(1+|log tau|).

Split the integral at rho=tau^2 to obtain this inequality directly.
Thus

    ||u_tau-u0||_C0(K)<=C_K tau(1+|log tau|).           (9)

The interior Poisson estimate used in section3, together with the
O_Cj(tau) vorticity bound in(7), upgrades(9) to every fixed local Cj
norm. Equation(6),(7) and(9) therefore imply

    partial_tau omega_tau-omega1=O_Cj(tau(1+|log tau|)),
    partial_tau theta_tau-theta1=O_Cj(tau(1+|log tau|)).

Integrate from0 to tau; the integral of sigma(1+|log sigma|) is
O(tau^2(1+|log tau|)). This proves(5), including the corresponding
spatial derivative bounds on rescaled annuli. No time derivative of
u_tau is used or assumed in this argument.

## 5. Separating the resonant inverse from the integrable remainder

Choose a smooth radial cutoff chi, zero for r<=1 and one for r>=2.
Define, on the plane away from0,

    eta(X)=Omega(X)-omega0(X)-chi(r) r^-1 b(theta).

By(5), eta=O(r^-3/2 log r) at infinity, with all corresponding spatial
derivative bounds; near0, eta=O(r^-1/2). Hence its ordinary velocity
integral

    U_eta(X)=int K(X-Y) eta(Y) dY

converges absolutely, including at X=0. Splitting into |Y|<r/2,
r/2<|Y|<2r, and |Y|>2r proves

    U_eta(r e)=O(r^-1/2 log r).                         (10)

For the inner piece use r^-1 int_{|Y|<r/2}|eta|=O(r^-1/2 log r),
for the middle piece use |eta|<=C r^-3/2 log r and the integrability
of K over a ball of size r, and for the exterior use
int_{2r}^infinity rho^-3/2 log rho d rho. A fixed neighborhood of0
contributes only O(r^-1) to the first piece. Derivative versions of
(10) follow by the same local Poisson estimate on scaled annuli.
Thus K_rel eta=-U_eta(0)+O_Cj(r^-1/2 log r).
By parity, U_eta(0) is vertical.

The remaining source chi(r)r^-1 b is inverted mode by mode, solely
to obtain an analytic expansion. This does not replace the verifier's
independent Cartesian inverse for numerical candidate checks.
For all harmonics k>=2 the exterior particular stream is r g(theta);
regular-core matching adds decaying exterior harmonics. Their velocity
sum is O_Cj(r^-2) or smaller after r>=3, because b is smooth and chi
is fixed. There is no mean source by x reflection.

For the first cosine harmonic the relative stream coefficient is
exactly

    P1(r)=(b1/2)[r^-1 int_0^r rho chi(rho)d rho
                         -r int_0^r chi(rho)/rho d rho].             (11)

It solves the radial Poisson equation and has P1/r tending to0
at the origin, implementing V(0)=0 for this mode. Define

    L_chi=lim_{R->infinity}[int_0^R chi(rho)/rho d rho-log R].

For r>=2, direct evaluation of(11) gives

    P1(r)=-(b1/2) r log r
                  +b1(1/4-L_chi/2)r+O(r^-1).

The full mode construction is the canonical relative inverse: its
velocity is smooth across the cutoff core, has the prescribed div-curl,
vanishes at0, and grows at most logarithmically. The integral K_rel of
this source is also O(log r), by a direct kernel split. Their difference
is an entire harmonic sublinear vector field, hence a constant, and
its value at0 is zero. Smoothness of b and the fixed cutoff ensure
convergence of the mode sum, with all fixed derivatives; for r>=3
the exterior corrections are bounded by convergent series with factors
(2/r)^k times rapidly decreasing Fourier coefficients.

The first term means Psi=-(b1/2)x log r, whose exact velocity is

    (b1/2)(cos theta sin theta,-log r-cos^2 theta).

This verifies the sign and the angular term in(4). The r term in
P1 is a vertical constant fixed by the core and the relative inverse.
Combining the three source pieces gives(4), with

    C=b1(1/4-L_chi/2)-[U_eta(0)]_2.                    (12)

The integral in(12) is absolutely convergent. It is a formula for a
profile-dependent constant, not an independently adjustable gauge.

## 6. Cutoff independence and scope

If chi changes by a compactly supported radial dchi, then
L_chi changes by int dchi/rho. The corresponding eta changes by
-dchi(r) r^-1 b. By angular integration,

    delta[U_eta(0)]_2=-(b1/2) int dchi(rho)/rho d rho.

This exactly cancels the change of the first term in(12). Thus C
is independent of the auxiliary cutoff. The fixed normalization of
g (orthogonal to the first harmonics) specifies the decomposition
between B_b and C unambiguously.

The logarithm is forced only if the computed coefficient b1 is
nonzero. Its absence would be an additional compatibility relation,
not a consequence of x reflection. None of these asymptotics proves
that any smooth angular data are realized by an exact global B2
profile, or that the remaining class is empty.

Dependencies: confirmed packets33 and36, the absolutely convergent
relative inverse, elementary homogeneous Poisson inversion, local
interior elliptic estimates, and the exact physical transport equations.
No extra decay, analyticity or global Sobolev assumption is added.

## 7. External audit and a numerical extraction convention

Actual Opus26 returned claude-opus-5-5 with a written audit agreeing
with all formulas and the remainder argument, conditional on33 and36.
The verifier checked its suggestions and made the canonical mode-sum
identification, explicit parity and derivative notation more explicit.
One referee criticism is rejected: the mean angular mode DOES vanish
by x-reflection oddness, since b(pi-theta)=-b(theta). It was not excluded
because of resonance. The k0 mode would be nonresonant without parity,
but it is absent here. Actual Opus27 explicitly withdrew that objection after the verifier supplied the change-of-variables proof. The second source has the needed parity: u0_1 is x-odd, u0_2 is x-even, partial_x omega0 is x-even, partial_y omega0 is x-odd, and partial_x theta0 is x-odd. Thus omega1 and b are x-odd.

The angular mean of B_b is -(b1/4)(0,1), not zero. Consequently extracting
C from the angular mean of V-r^(1/2)u0+(b1/2)log r(0,1) requires adding
b1/4 to its vertical component. This follows directly from the normalized
first-harmonic-free g and the mean of cos^2 theta.
