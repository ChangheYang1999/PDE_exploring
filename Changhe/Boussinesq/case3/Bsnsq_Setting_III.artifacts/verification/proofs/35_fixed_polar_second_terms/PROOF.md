# Fixed-polar second terms from local Boussinesq continuation

Date: 2026-10-20. Status: CONFIRMED by the independent verifier and the checked actual Claude Opus5.5 review23. The verifier separately retrieved and checked the exact external theorem; Opus reviewed its transcribed statement.
This is a far-field necessary theorem for the exact power-decay class A, not a YES or NO endpoint.

## 1. Statement, notation and dependencies

Let beta>=2 and let (Theta,Omega,V) be a nontrivial smooth B2 class A profile,
with V the anchored whole-plane relative inverse, V(0)=0. Put

    s=1/beta, m=1-2s, e(theta)=(cos theta,sin theta),
    e_perp(theta)=(-sin theta,cos theta),
    K(Z)=(Z2,-Z1)/(2pi |Z|^2).

By packets17,18,23 and33 there are angular functions a and h such that

    Omega(r e(theta))=r^-s[a(theta)+o(1)],
    Theta(r e(theta))=r^m[h(theta)+o(1)]                     (1)

uniformly in theta, a is continuous and nonzero, and h is C1. Also

    |Omega|<=C(1+r)^-s, |V|<=C(1+r)^(1-s),
    |DV|<=C r^-s, |grad Theta|<=C r^-2s                     (2)

outside a fixed ball. Define on the punctured plane

    omega0(z)=|z|^-s a(arg z), theta0(z)=|z|^m h(arg z),
    u0(z)=integral [K(z-y)-K(-y)]omega0(y)dy.              (3)

Then, for every finite 1<q<infinity,

    a in W^{1,q}(S1), h in W^{2,q}(S1),
    u0 in W^{2,q}_loc(R2 minus{0}).                        (4)

Let u0r=u0(e).e, u0t=u0(e).e_perp, and define

    b(theta)=u0t(theta) a'(theta)-s u0r(theta)a(theta)
             -partial_x theta0(e(theta)),
    d(theta)=u0t(theta) h'(theta)+m u0r(theta)h(theta).     (5)

Here a' is the weak angular derivative, so b in every finite Lq, while d is
continuous. The conclusions are

    Omega(r e(theta))=r^-s a(theta)+r^-2s b(theta)
                         +o_{Lq(S1)}(r^-2s),             (6)
    Theta(r e(theta))=r^m h(theta)+r^(m-s)d(theta)
                         +o_{C0(S1)}(r^(m-s)).            (7)

The same u0 is homogeneous of degree1-s. In particular these formulas specify
the next terms in ordinary polar coordinates, not only along W trajectories.
They do not assert uniform convergence of the next vorticity coefficient,
C1 regularity of a, a higher power series, or a velocity next term.

The only external theorem used below is Chae and Wolf, *Removing Type II
singularities off the axis for the 3D axisymmetric Euler equations*,
arXiv:1712.07434v6, Section2 Theorem2.1, printed page7. Its concluding
paragraph on printed page26 was also checked, but is not needed for this application. The source is stored as
`verification/literature/1712.07434v6.pdf` at the lane root, SHA256
4cf4a48ece2eaa76e1abbd8b3ee6efe2a0f6595e2de7bf9026dbe59358314027.
The exact local generalized Boussinesq theorem, rather than a global finite
energy criterion, is used. Its hypotheses are checked below. The source
proof is a mathematical dependency, not a theorem proved afresh here.

## 2. Physical rescaling on annuli

For t=-tau, 0<tau<=1, define

    u(t,z)=tau^(beta-1)V(tau^-beta z),
    omega(t,z)=tau^-1 Omega(tau^-beta z),
    theta(t,z)=tau^(beta-2)Theta(tau^-beta z).              (8)

This uses the allowed relative representative and a stationary material
center at zero in that observer frame. It does not require that the original
unsubtracted Biot-Savart center integral converge. Direct differentiation,
using the exact B2 equations, gives

    omega_t+u.grad omega=partial_x theta,
    theta_t+u.grad theta=0, div u=0,
    partial_2 u1-partial_1 u2=omega.                      (9)

For example d_t[tau^-1 Omega(tau^-beta z)]
=tau^-2[Omega+beta X.grad Omega], while
u.grad omega=tau^-2 V.grad Omega. These sum to tau^-2 Theta_x,
which equals partial_x theta. The signs in(9) therefore agree with the
negative-curl convention of the prompt.

On every compact annulus separated from0, equations(1)-(2) imply uniform
bounds on |u|, |Du|, |omega| and |grad theta| up to t=0. They also imply
locally uniform limits omega->omega0 and theta->theta0. This includes beta=2:
the gradient bound cancels the tau^-2 factor in grad_z theta and gives
O(|z|^-1) on an annulus, independent of tau.

The kernel scaling K(lambda z)=lambda^-1 K(z), with the absolutely convergent
relative integral, gives the exact identity

    u(t,z)=integral [K(z-y)-K(-y)]omega(t,y)dy.            (10)

There is a global majorant valid for all y!=0 and 0<tau<=1:

    |omega(t,y)|<=C |y|^-s.                              (11)

Indeed tau^-1(1+tau^-beta|y|)^-s<=|y|^-s, since beta s=1.
For fixed z!=0 the kernel in(10) times |y|^-s is integrable. Near y=0,
the singular term is O(|y|^-1-s), locally integrable because s<1.
Near y=z it is a locally integrable inverse distance with bounded |y|^-s.
At infinity the subtracted kernel is O(|z|/|y|^2), integrable against |y|^-s
because s>0. Dominated convergence proves u(t,z)->u0(z).

This convergence is uniform for z in a compact annulus. For a detailed
uniform argument, delete a small ball around0, a small ball around each z,
and a sufficiently large exterior region. The deleted contributions are
uniformly bounded by C epsilon^(1-s), C epsilon, and C R^-s, respectively,
using the positive distance of the compact annulus from0. On the remaining
compact set, omega converges uniformly and the kernels are uniformly
integrable. Let the deletion parameters tend to their limits after t->0.
Alternatively the uniform annular Du bound and pointwise convergence imply
uniform convergence on compact subsets by a finite net. Consequently u
extends strongly continuously to t=0 in L2 on every ball away0, so it meets
the weak L2 continuity required by the local theorem.

Changing variables y=lambda v in(3) gives
u0(lambda z)=lambda^(1-s)u0(z), since omega0(lambda v)=lambda^-s omega0(v).
All integrals here are absolute, so this change of variables is legitimate.

## 3. Exact use of the local continuation theorem

Theorem2.1 treats on B1 x(-1,0) the system

    theta_t+a(y)u.grad theta=0,
    w_t+a(y)u.grad w=b(y).grad theta, div u=0,
    partial_2 u1-partial_1 u2=d(y)w+e(y).u,

with C2 coefficients. For 2<q<infinity it assumes
(u,theta) continuous in time into W2q before0, w continuous into W1q
before0, u weakly continuous into L2 through0, and finiteness of

    integral_-1^0 (-t)||grad theta(t)||_infinity dt,
    integral_-1^0 ||u(t)||_infinity dt.                   (12)

It concludes u,theta continuous through0 into W2q on every smaller ball.
In the application here, negative curl u=omega, so continuity of u in W2q
already gives continuity of omega in W1q. The proof's final paragraph gives
the same fact for its more general coefficient system.

Choose any closed ball B(z0,R) disjoint from0, and rescale it to B1 by
z=z0+R y. Set the new velocity to u(t,z0+R y)/R and leave theta and omega
unscaled in amplitude. Then the coefficients of the displayed system are

    a=1, b=(1/R,0), d=1, e=0.

The negative curl relation is unchanged since one spatial derivative
cancels the division by R. All these coefficients are C-infinity.
At every t<0 the original profiles are smooth on compact sets, so the
required time continuity in Sobolev spaces follows directly from(8).
The endpoint weak continuity was proved after(11), and(12) follows from
the uniform annular bounds on u and grad theta. The theorem therefore
applies on every such ball and gives

    u(t)->u0 in W2q_loc, theta(t)->theta0 in W2q_loc,
    omega(t)->omega0 in W1q_loc                           (13)

as t increases to0. The limiting functions agree with(3) by their already
established uniform limits. No assumption about global energy, global
Sobolev norms, or regularity at z=0 is made.

Homogeneity and a polar-coordinate change on 1<|z|<2 give(4). More
explicitly, the distributional angular derivative is z_perp.grad omega0.
Multiplying by r^s and averaging over 1<r<2 against a smooth radial function
of integral1 shows that a has an Lq weak derivative. Applying this argument
twice to theta0 gives the W2q assertion for h. The theorem applies for every
q>2. Lower finite q follow on the compact circle by inclusion. Sobolev
embedding gives a in C^alpha for every alpha<1, h in C^{1,alpha} for every
alpha<1, but does not imply a in C1.

For a fixed q>2, (13) and the two-dimensional Sobolev embedding also give
u(t)->u0 and theta(t)->theta0 in C^{1,alpha} on smaller annuli, for every
0<alpha<1-2/q. These convergences will control the circle characteristics.

## 4. Temperature second term

Write u_tau(z)=u(-tau,z), theta_tau(z)=theta(-tau,z). Equation(9) becomes

    partial_tau theta_tau=u_tau.grad theta_tau.

The right side converges uniformly on compact annuli to u0.grad theta0,
by(13) and Sobolev embedding. Integration from a positive epsilon to tau,
followed by epsilon->0, is justified by its uniform bound and the uniform
limit theta_epsilon->theta0. It yields

    theta_tau=theta0+tau u0.grad theta0+o(tau)

uniformly on compact annuli. On the unit circle tau=r^-s and
Theta(r e)=r^m theta_tau(e); the polar derivative of theta0 is
m h e+h' e_perp. This proves(7) and the formula for d.

## 5. A circle equation avoids an unjustified trace of the time derivative

Put f(tau,theta)=omega_tau(e(theta)), and let
u_r(tau,theta)=u_tau(e).e, u_t(tau,theta)=u_tau(e).e_perp,
g(tau,theta)=partial_x theta_tau(e). For tau>0 these are smooth. The exact
scaling identity

    omega_tau(rho e(theta))=rho^-s f(tau rho^-s,theta)

gives, on rho=1,

    partial_rho omega_tau=-s f-s tau partial_tau f.

Since partial_tau omega_tau=u_tau.grad omega_tau-partial_x theta_tau,
we obtain the exact scalar circle equation

    (1+s tau u_r)partial_tau f-u_t partial_theta f
         =-s u_r f-g.                                   (14)

For sufficiently small tau its denominator is positive and bounded away
from zero. Set

    c_tau=-u_t/(1+s tau u_r),
    k_tau=-(s u_r f+g)/(1+s tau u_r).

Thus partial_tau f+c_tau partial_theta f=k_tau. Equations(1),(13) imply

    c_tau -> c0=-u0t in C1(S1),
    k_tau -> k0=-s u0r a-partial_x theta0(e) in C0(S1).    (15)

Here the C1 convergence of c_tau uses u convergence in C1 on annuli;
k_tau needs only the uniform convergence of f and grad theta. The
continuous dependence of k_tau on f causes no difficulty, since it is
being evaluated along the already existing exact solution.

Both c and partial_theta c extend jointly continuously to the closed
interval [0,tau0] times S1 by(15), so the characteristic equation is
uniformly Lipschitz in its angular variable through parameter0.
Let B_tau(theta) be the angle at parameter0 of the characteristic of c
which is at theta at parameter tau. Uniform boundedness and convergence
of c in C1 imply

    B_tau(theta)=theta-tau c0(theta)+o(tau)
               =theta+tau u0t(theta)+o(tau)              (16)

in C1(S1). To see this without any time differentiability of c, write the
characteristic integral equation, use its displacement O(tau), and
integrate c_v-c0=o(1) uniformly for 0<=v<=tau. Its derivative equation
uses the same argument with partial_theta c_v; Gronwall bounds all
Jacobians uniformly and proves the derivative part of(16).

Integrate(14) from epsilon to tau on each characteristic. Let epsilon->0
using f(epsilon)->a uniformly and the uniform bound on k. The resulting
formula and(15) give

    f(tau,theta)=a(B_tau(theta))+tau k0(theta)+o_C0(tau).  (17)

The remainder in the integral is uniform because the characteristics
move O(tau), k_v->k0 uniformly and k0 is uniformly continuous. Formula(17)
does not yet justify differentiating a pointwise: a is only W1q.

## 6. Composition of a W1q function with a small circle diffeomorphism

For a in W1q(S1), and C1 diffeomorphisms B_tau satisfying(16),

    [a o B_tau-a]/tau -> u0t a' in Lq(S1).               (18)

Here is a proof of the required strong derivative. Work with periodic
lifts for small tau and write h_tau=B_tau-id. The interpolation maps
id+v h_tau, 0<=v<=1, are C1 diffeomorphisms with uniformly bounded
Jacobians and inverse Jacobians because ||h_tau'||_infinity=O(tau):
1+v h_tau' >=1-C tau>0, and the periodic lifts have degree one.
For any smooth periodic a,

    [a(theta+h_tau)-a(theta)]/tau
       =(h_tau/tau) integral_0^1 a'(theta+v h_tau)dv.

This converges uniformly to u0t a'. The same formula for a W1q function
holds almost everywhere by absolute continuity. A change of variables
bounds the Lq norm by C||a'||_Lq uniformly in tau. Approximate a in W1q by
smooth periodic functions. The uniform operator bound and
||u0t a'||_Lq<=C||a'||_Lq permit the approximation error to be taken to
zero after the smooth limit. This proves(18).

Combining(17)-(18) yields

    f(tau)=a+tau[u0t a'-s u0r a-partial_x theta0(e)]+o_Lq(tau).

Finally omega_tau(e)=tau^-1 Omega(tau^-beta e), so with tau=r^-s
we have Omega(r e)=r^-s f(tau). This proves(6). The formula for b is exactly
(u0.grad omega0-partial_x theta0) on the unit circle, interpreted in Lq.
The argument works for every finite q; no uniform convergence of a' is
asserted.

## 7. Limits and open extensions

The result relies on the exact equations and the power-decay inverse
class. It does not validate any numerical candidate. It gives a concrete
next-term test in angular Lq and a uniform temperature test. At beta=2 the
vorticity second exponent is -1; its velocity inverse can contain a
logarithmic resonance, as in packet19. Constant relative-velocity terms
and noninteger powers can also enter later velocity or transport
corrections. Nothing above differentiates u in time or assumes an
all-orders expansion. A uniform second vorticity term, smoothness of a,
and an all-orders fixed-angle expansion remain open here.


## Audit record

Actual requested `us.anthropic.claude-opus-5-5`, returned `claude-opus-5-5`,
review23 completed2026-10-20T16:06:14.594576Z in92.43894seconds with a visible
written audit and end_turn. The verifier independently rechecked all advice.
The explicit angular orientation, closed-interval flow regularity and
Jacobian positivity were added. The curl identity removes the dependency on
the source proof's final paragraph. Opus did not access the PDF; the verifier
checked that theorem statement and its precise coefficients separately.
The relative representative V is exactly the field in B2, so the physical
rescaling(8) requires no change to the stationary equations or fitted drift.
