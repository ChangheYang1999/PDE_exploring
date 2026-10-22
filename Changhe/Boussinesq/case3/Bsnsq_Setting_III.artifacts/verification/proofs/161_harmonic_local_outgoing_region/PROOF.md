# A harmonic local outgoing region with a nonanalytic boundary at beta two

Status: CONFIRMED by the complete independent proof and manufactured controls, with an actual Opus5.5 written local audit. Broader review requests returned no written text. These are nonprofiles. The harmonic conclusion below is local near each endpoint, not a claim on its full global basin.

## 1. Statement

Fix a0>0 and R0>0. There are smooth whole-plane fields with the following properties:

* The x-reflection parity, ordinary canonical full-plane inverse, U(0)=0, U=O(r^-1), nonnegative bounded temperature vanishing exactly on x=0, and the exact equation (T), W.gradTheta=0, hold, where W=2X+U, U=(-Psi_y,Psi_x), Omega=-DeltaPsi=-curl W.
* Both (T) and (V), W.gradOmega+Omega=Theta_x, hold on the prescribed disk and near each interior point of a compact equilibrium arc through0. The core is exactly Psi=2xy-a0 x³/3, Theta=a0 x², Omega=2a0 x. All residual jets vanish on the arc, and Omega and Theta-M are flat at its two endpoints.
* These are the only equilibria, both endpoints are outgoing, and the strong unstable curve at each endpoint is smooth and does not agree with a regular analytic curve germ through that endpoint.
* Near each endpoint, on the outgoing side of this strong unstable curve and on the curve itself, Omega=0 and Theta=M. Thus (T) and (V) hold there exactly. There is a nonempty open local region all of whose backward orbits stay in that region's small surrounding neighborhood and converge to the endpoint.

Nonetheless (V) fails in every neighborhood of an endpoint and in an unchanged exterior cone. This shows that the corresponding collection of local necessary conditions is insufficient. The construction does not impose (V) on a whole endpoint neighborhood, repair the global residual, give a candidate or decide the beta2 class. The temperature on the equilibrium arc is allowed to have a plateau before the endpoint; strict increase along the whole half-arc is not asserted.

## 2. Preparing the global reference

Use the base and compact shear of156, with the following two permitted choices made explicit. Choose R0+1<A0<A, and let its even nonnegative cutoff rho be positive on |x|<A0 and zero for |x|>=A0. Then F(x)=int_0^|x| 2a0 t rho(t)dt equals a0 x² near the prescribed core, is positive off0, and is the constant M for |x|>=A0. Choose delta>0 with delta<2/45 and much smaller than A-A0 and A-R0, and put, for u>0,

    f_+(u)=exp(-1/sqrt(u)),       f_+(u)=0 for u<=0.

Arrange the horizontal cutoff of156 to satisfy

    chi(r)=1-f_+(r-A)/(2r)       for A<=r<=A+3delta,
    chi=1 for r<=A,             chi=C/r² for r>=2A,
    0<chi<=1,   -1<chi+r chi'<=1,

with chi<1 for r>A. This can be done without an unproved interpolation constraint. On the short interval where the displayed target is prescribed, set

    e(r)=[f_+'(r-A)-f_+(r-A)/r]/[4 chi(r)].

For delta small this is smooth, flat at A, and in(0,1): f_+' / f_+=1/[2(r-A)^(3/2)]>1/r, and f_+' tends to0 at A. Extend e smoothly with values in(0,1] until it becomes identically1 before2A, and put e=0 for r<=A. Define chi(r)=exp[-2 int_A^r e(s)/s ds]. On the prescribed short interval it equals the target by uniqueness of its first-order linear equation and the common value1 at A. Everywhere chi+r chi'=chi(1-2e), giving the required bounds and the C/r² exterior. Extend chi evenly in its argument.

All global proofs in156 remain valid with these choices. Specifically, F' is supported where chi=1, so the base thermal equation holds. The bound -1<chi+I chi'<=1 and |p0(y)|<=2|y| makes the vertical base drift have the sign of y, hence the only base zeros are [-A,A] times{0}. The shear carries these exactly to gamma={(x,F(x)/4): |x|<=A}. The ordinary inverse and strip/cone decay proofs depend on the same C/I² exterior and do not require F'>0 up to A. The exact band formulas of156, W=(0,4y-F(x)), Theta=F(x), Omega=F'(x), remain valid on |x|<A. In particular (V) is still exact along every interior arc neighborhood, including its new constant-temperature portions.

Near p=(A,M/4), use u=x-A and Y=y-M/4. The shear is a constant translation because F=M there. Within the disk of radius3delta,

    W_old=(v(u), [4-v'(u)]Y),  Theta=M,
    v(u)=f_+(u),
    Psi_old=Q-Yv(u)+constant,  Q=2xy-Mx.                    (1)

The reference has the same explicit nonzero far-cone residual as156 and positive vorticity in the core and negative vorticity in that cone. These properties will be kept.

## 3. A flat holomorphic perturbation

Choose angles pi/2<theta0<theta1<pi and a smooth even angular cutoff kappa that is1 for |arg z|<=theta0 and0 for |arg z|>=theta1. On |arg z|<theta1, z=u+iY, use the principal square root and define

    f(z)=exp(-1/sqrt(z)),
    P(z)=z int_0^1 exp[-1/sqrt(tz)]dt.                     (2)

The last formula is the primitive with P'=f and limit0 at the vertex: integrating f along the radial segment gives it; differentiating z int_0^1 f(tz)dt yields int_0^1 d_t[t f(tz)]dt=f(z). The endpoint at t=0 vanishes. It is holomorphic in the sector. Since Re(z^-1/2)>=cos(theta1/2)|z|^-1/2>0, P, f and every fixed derivative vanish faster than every power of |z| uniformly on closed subsectors that include the support of kappa. Thus

    H(u,Y)=kappa(arg z) Im P(z), H(0,0)=0

extends to a C-infinity function on a disk by setting it to0 outside the sector; it is flat at0. Derivatives of the angular cutoff cost fixed powers of |z|^-1, absorbed by the exponential. It is odd in Y, by conjugation symmetry. No holomorphic continuation through the vertex or through the negative real axis is asserted.

Let zeta be a smooth radial cutoff equal1 for r<=delta and0 for r>=2delta. Define the compact local stream correction

    dPsi_+(x,y)=zeta(r)[Yv(u)-H(u,Y)].                     (3)

It is smooth and flat at p. Use dPsi=dPsi_+(x,y)-dPsi_+(-x,y) globally, with disjoint endpoint supports. Put Psi_new=Psi_old+dPsi and keep Theta unchanged. This is a direct stream correction, not a claim of area-preserving conjugacy. Its support lies where the old Theta is exactly the constant M, so (T) remains exact there and outside. The correction is compact and odd in x. Consequently its ordinary Biot-Savart inverse is J grad dPsi, which proves canonical inversion with no new harmonic velocity, unchanged U(0), unchanged core and unchanged exterior.

## 4. Exact endpoint formulas and zero set

Inside r<delta, (1)-(3) give

    Psi_new=Q-H+constant.

Where |arg z|<theta0, H=Im P and the Cauchy-Riemann equations give the exact field

    W_new=(Re f(z), 4Y-Im f(z)),     Omega_new=0.          (4)

In a neighborhood of the negative real axis H=0, so W_new=(0,4Y), Omega_new=0. Each point of the negative real arc u<0 therefore has an open neighborhood where the correction vanishes and the old exact equations hold.

Throughout the endpoint disk, including the radial transition, the perturbation of W_old is flat at p and odd in Y in its second component. Shrinking delta if needed, its C1 norm and that of v are small enough that

    W_new,2=Y d(u,Y),                 d>3.               (5)

This follows from Hadamard's integral formula for the odd component and the bound on its Y derivative; derivatives of zeta at scale delta are dominated by flatness. On Y=0, the correction's first derivative vanishes: for u>0, kappa=1 and partial_Y H=f(u)=v(u); for u<0, kappa=0 and v=0. The term from differentiating zeta vanishes because Yv-H=0 there. Thus

    W_new,1(u,0)=f_+(u).                                  (6)

Equations(5)-(6) show that the new zeros in each support disk are exactly Y=0,u<=0. All other points are unchanged. Hence the full equilibrium arc and the outgoing center branch are retained, with no added stagnation points. Every endpoint jet of W_new agrees with that of (0,4Y); Omega and every residual jet are flat there. Interior arc neighborhoods and the core keep both equations exactly.

## 5. The strong unstable curve and the local outgoing side

Here the strong unstable graph can be constructed directly, without a manifold-existence theorem. Write a(u,Y)=W_new,1(u,Y) and W_new,2=Y d(u,Y), where d>3. The function a is flat at(0,0). On the cusp |u|<=Y², every fixed derivative of

    A(u,Y)=a(u,Y)/[Y d(u,Y)]       (Y!=0)

is O(|Y|^N) for every N: derivatives of the reciprocal cost only fixed inverse powers of |Y|, absorbed by flatness. On the Banach ball of continuous graphs g with g(0)=0 and norm sup_(Y!=0)|g(Y)|/Y²<=1, set

    (Tg)(Y)=int_0^Y A(g(t),t)dt.

The integrand extends continuously by0 at t=0. For a sufficiently small fixed interval [-r,r], |A|<=C|t|² makes T map the ball into itself, since |Tg(Y)|<=C|Y|³/3. The bound |partial_u A|<=C|t|² gives

    ||Tg-Th|| <= (Cr³/5)||g-h||.

Thus T is a strict contraction after shrinking r. Its fixed graph solves g'=A(g(Y),Y) away from0 and is invariant. The estimates for A first show g and g' vanish faster than every power at0. Repeated differentiation of g'=A(g,Y), using those same bounds on all derivatives of A, then shows inductively that each derivative of g extends continuously by0 at0 and is flat. Hence g is C-infinity and flat.

Along this graph, Y'=Yd(g(Y),Y), with d->4, so the backward exponential rate is4. The coordinate argument below shows that every neighboring orbit outside the graph either converges to a different equilibrium or approaches p with horizontal exponential rate0. Thus this graph is exactly the local strong unstable curve; its existence, smoothness and meaning are all established here.

The graph lies in the sector |arg z|<theta0 for small |Y| because g(Y)=O(Y²). In particular Omega=0 on the graph and in an open neighborhood of each of its nonzero points. It is not an analytic germ. Otherwise its flat Taylor series would imply g=0 near0, but the vertical line is not invariant:

    W_new,1(0,Y)=exp[-1/sqrt(2|Y|)] cos[1/sqrt(2|Y|)]      (Y!=0),

which is not identically zero on any punctured interval. The same conclusion holds on both branches, and reflection supplies the left endpoint.

For completeness the local basin conclusion can be checked by an explicit smooth-coordinate argument. Straighten the strong unstable graph with U=u-g(Y), V=Y. The center line remains V=0, and the vector field is

    U'=f_+(U)+UV c(U,V),     V'=V d_tilde(U,V), d_tilde>3.  (7)

Indeed the first remainder vanishes on U=0 by invariance of the graph and on V=0 by(6), so two applications of Hadamard's formula factor UV; c is bounded. Backward, |V(-t)|<=|V(0)|exp(-3t) for t>=0 while the orbit is in this neighborhood. For U>0,

    w(t)=U(t)exp[-int_0^t V(s)c(U(s),V(s))ds]

has positive forward derivative f_+(U) times the positive exponential. The exponential factor stays bounded above and below backward, since int|V| is finite. Trapping does not need to be assumed. In a coordinate rectangle |U|,|V|<=r where |c|<=C and d_tilde>3, while a backward orbit remains there,

    |V(t)|<=|V(0)|exp(3t),
    |U(t)|<=|U(0)|exp(C|V(0)|/3)       (t<=0).

For U>0 the second bound follows because w is positive and decreases backward; for U<0 it follows because w is constant. Signs cannot cross U=0, an invariant curve. Initial values |V(0)|<r/2 and |U(0)|<(r/2)exp(-Cr/3) therefore never reach the rectangle boundary backward. Standard local ODE continuation makes these backward solutions complete in that rectangle.

Now w decreases backward to a nonnegative limit. The exponential factor also has a positive limit. A positive limit for w would imply U->U_*>0 and U'->f_+(U_*)>0, incompatible with convergence as time tends to minus infinity. Thus U->0 for U>0. On U<0, w is a nonzero constant and U tends to a strictly negative value. This proves that the outgoing side is U>0 locally and every sufficiently small backward orbit limits on the arc. For U>0, (log U)'=f_+(U)/U+Vc tends to0 backward, so log U(t)/t->0; these orbits do not approach p exponentially. This proves the strong-unstable characterization used above.

Every sufficiently small point with U>=0 lies in the harmonic sector: u=U+g(Y)>=g(Y), with g(Y)=O(Y²); a negative u is therefore negligible compared with |Y|. Equations(4) and Theta=M prove both equations on this local outgoing side and its boundary. Only local portions whose backward orbits remain near p are claimed. The field can have nonzero vorticity farther along the same global orbits.

## 6. Why every endpoint neighborhood still has a residual

The function H is flat at0, zero on an open negative-axis sector and not identically zero in any disk. Its Laplacian cannot vanish on any full disk: if it did, harmonic analyticity and its zero Taylor series would force H=0 there. Thus Omega_new=Delta H is nonzero arbitrarily close to p, in the angular transition outside the outgoing sector.

Suppose (V) held on some full neighborhood of p. Temperature is the constant M there. Choose a smaller coordinate neighborhood such that all backward orbits stay in the assumed neighborhood, as supplied by(7). Along them (V) gives

    Omega_new(phi_(-t) X)=exp(t) Omega_new(X).

The backward limit lies on the local zero arc, where Omega is bounded (and zero). Hence Omega_new(X)=0 throughout the smaller neighborhood, contradicting the preceding paragraph. Therefore the vorticity residual is nonzero in every endpoint neighborhood, even though it is zero on the local outgoing region, near every interior arc point, and to every order on the whole arc. The unchanged far-cone formula156 independently shows failure of the global equation.

## 7. A global invariant outgoing set still has nonzero vorticity

This strengthens the scope statement by constructing, at each endpoint, a particular nonempty open invariant set O of endpoint orbits on which Omega is not identically zero. It does not claim that the locally harmonic region extends globally.

Consider the right endpoint. Section5 gives an open local outgoing neighborhood N containing a center-line point (u0,0) with0<u0<delta, all of whose backward orbits tend to p. Let O be its full flow-saturation, union over all real times t of phi_t N. The global vector field is smooth and at most linear at infinity, so this flow is complete. Thus O is nonempty, open, invariant in both time directions, and every orbit in O has backward limit p. The exact global thermal equation makes Theta=M throughout O.

The line Y=0 is invariant from u0 to u*=5delta/2, with W1(u,0)=f_+(u)>0 throughout0<u<3delta, including the radial correction annulus. This follows from the oddness of the stream correction in Y and its cancellation of Yv-H to first order along the positive real line: H_Y(u,0)=f_+(u)=v(u). Equivalently the exact formulas in section4 give the same center-line speed across the cutoff. The time integral int_(u0)^(u*) du/f_+(u) is finite because u0>0. The image of N at that finite time is an open neighborhood of (u*,0), contained in O.

Since u*>2delta, the correction vanishes in a neighborhood of (u*,0). For small nonzero Y in the last open neighborhood, section2 therefore gives

    Omega(u*,Y)=f_+''(u*) Y,
    f_+''(u)=exp(-1/sqrt(u)) (1-3sqrt(u))/(4u^3).

Our allowed choice delta<2/45 gives u*<1/9, so f_+''(u*)>0. Consequently Omega is nonzero at points in O. If(V) held identically on O, Theta=M there would make Omega(phi_(-t)X)=exp(t)Omega(X); boundedness at the backward limit p would force Omega=0 on O. This is a contradiction. Thus(V) does not hold identically on this chosen O. Reflection constructs the corresponding O at the left endpoint.

The conclusion is existential for the two constructed invariant open sets, each obtained from a local neighborhood containing a center-line point. No assertion about every arbitrarily selected invariant subset of the global basin is needed or made. In particular it is compatible with exact harmonicity on the local outgoing side established in section5.

## 8. Dependencies and scope

The global reference uses the elementary construction156 with the two choices in section2; the proof above explicitly checks the changed hypotheses. Canonical inversion is the same compact-stream identity as in156, and all exterior failure formulas are unchanged. The strong unstable graph is obtained by the explicit contraction in section5; its all-order flatness, exponential characterization and backward containment are proved there. Only elementary ODE continuation, the contraction theorem and harmonic analyticity are used. No numerical evidence is a premise.

This does not prove that (V) can hold on a whole endpoint neighborhood. In fact it fails there. The construction specifically separates a harmonic local outgoing side from the adjacent region of interior fibers. It gives no global harmonic basin, no nonzero-temperature profile, no compact residual and no full YES or NO.

Written UTC 2026-10-21T11:29:21.019448+00:00, before code or controls.

Revision UTC 2026-10-21T11:41:42.119696+00:00: supplied a direct contraction proof for the smooth strong unstable graph and quantitative backward containment; preserved the initial proof with the controls.

Extension UTC 2026-10-21T12:19:42.518370+00:00: supplied the global flow-saturation argument and exact nonzero-vorticity witness at u*=5delta/2. No numerical premise, new PDE solution or full endpoint is claimed.
