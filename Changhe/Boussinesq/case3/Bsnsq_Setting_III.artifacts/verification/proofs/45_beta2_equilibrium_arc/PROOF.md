# Beta-two equilibrium arc, flat endpoints, and an outgoing open set

Date:2026-10-20. Status: CONFIRMED by independent derivation and a checked audit
from actual Claude Opus 5.5, returned2026-10-20T16:59:13Z. No full B2 endpoint is claimed.

## 1. Hypotheses and conclusions

Let U,Omega,Theta be smooth full-plane B2 fields at beta2, with
V=U-U(0)=o(r), W=2X+V, div W=4, curl W=-Omega,
W.grad Theta=0, W.grad Omega+Omega=Theta_x. Assume Theta and W2 are even in x, W1 and Omega odd in x,
Theta(0,y)=0, Theta=x^2+O(|X|^3) at0. A general nonzero a0 is reduced
to1 by the already justified signed spatial scaling. No y parity is used.

The connected component gamma of Z={W=0} through0 is a nontrivial
compact smooth embedded arc. Its only intersection with x=0 is0, and
its endpoints p_+,p_- satisfy (p_+)_x>0, p_-=(-p_{+,x},p_{+,y}).
At both endpoints all derivatives of Theta-L of every order and of
Omega of every order vanish, where L=Theta(p_+)=Theta(p_-).
Moreover DW(p)=4n tensor n with n normal to the arc.
Thus Theta cannot be analytic on a connected neighborhood of gamma.
These are partial structural conclusions, not exclusion of smooth fields.

## 2. Arc and flatness proof

Sublinearity gives W.X>=r^2 outside a sufficiently large disk, so Z is
compact. Linear growth gives a complete flow. Parity gives diagonal
DW(0), and its trace is4. Comparing quadratic terms in
W.grad Theta=0 gives 2 W1_x(0)=0. Thus DW(0)=diag(0,4).
The linear vorticity equation then gives Omega=2x+O(r^2). Near0 write
Theta=x^2 H with H(0)=1. The equation W2=0 is a smooth graph y=g(x),
g(0)=g'(0)=0. On it, W1 Theta_x=0 and Theta_x=x[2H+x H_x]!=0 for
small x!=0. Thus this graph is a nontrivial local equilibrium arc.

At any zero, trace DW=4 implies that some component has a nonzero
differential. By IFT, its zero set is a smooth local curve containing Z.
A compact connected nontrivial subset K that is locally contained in a
smooth embedded curve is an arc or circle. Here are details needed to
exclude hidden gaps. Straighten the containing curve in a rectangle
around a point and take a smaller rectangle whose complement meets K.
If two missing points of the straight diameter enclose a point of K,
then the portion between these cuts is a nonempty proper relatively
open and closed subset of K: the horizontal sides miss K and the
vertical cuts were chosen outside K. This contradicts connectedness.
Consequently gaps cannot accumulate on either side of the selected
point with K points between them. Shrinking the rectangle leaves a
full interval or a half interval containing that point. This makes K
a smooth one-dimensional manifold with possible boundary. Finitely
many graph charts on compact K give finite length; arclength continuation
therefore either closes into a circle or ends at two boundary points.
A circle C in Z would enclose positive area D but have
4|D|=int_D div W=int_C W.normal=0. It is impossible. Applying this to
the component through0 gives gamma with two endpoints.

Reflection takes gamma to itself and reverses its horizontal tangent
at0, hence reverses its interval orientation. A decreasing interval
homeomorphism has exactly one fixed point. Reflection's fixed set is
x=0, so gamma meets the axis only at0 and the endpoints are paired as
stated. This does not make either half-arc a graph over x.

At a nonisolated zero p, DW cannot be invertible. Its eigenvalues are
therefore0,4. In fixed linear coordinates(s,z) diagonalizing DW(p), the
linear vector field is(0,4z). If the first nonzero homogeneous Taylor
part of Theta-Theta(p) has degree m>=1, its transport equation gives
4z partial_z P_m=0, hence P_m=c s^m with c!=0. The nullcline of the
second component is z=k(s), k(0)=k'(0)=0. At its points the partial
s-derivative of Theta is mc s^(m-1)+O(|s|^m), nonzero for small s!=0.
Transport on that nullcline therefore makes the first component vanish
as well. A full equilibrium curve extends through p. At an endpoint of
gamma this is impossible, so Theta-Theta(p) is flat. The vorticity
equation at p first gives Omega(p)=0. Any first nonzero Taylor polynomial
Q_m of Omega would solve(4z partial_z+1)Q_m=0; its eigenvalues on
monomials s^i z^j are4j+1, all positive. Thus Omega is flat too.
Omega(p)=0 makes DW(p) symmetric. Its eigenvalues0,4 give the normal
projection formula. Parity equates the two endpoint temperature values.
Analyticity of Theta near gamma would make it locally constant at an
endpoint, then constant on the connected neighborhood by analytic
continuation, contradicting the quadratic center jet.

## 3. Exact geometry on the interior

Parametrize an interior subarc by arclength, with tangent tau, normal
n=(-tau_y,tau_x), and theta(s)=Theta(gamma(s)). Since DW tau=0 and
trace DW=4, write DW=(4n+lambda tau) tensor n. Its curl is-lambda,
so Omega=lambda. Differentiating transport at an equilibrium gives
(DW)^T grad Theta=0, hence

    grad Theta=theta'(tau-lambda n/4).

The vorticity equation on Z is Omega=Theta_x and becomes

    lambda[1-theta' tau_y/4]=theta' tau_x.            (1)

No division by the bracket is justified in general. Equation(1) gives
lambda=0 at a critical point of theta, but neither a sign condition
nor monotonicity along the arc.

Straighten a compact interior subarc to z=0. The field factors as
s'=z A(s,z), z'=z B(s,z), with B(s,0)=4. In a sufficiently small strip
B>2. The equation ds/dz=A/B is a regular smooth scalar ODE across z=0,
so it defines smooth transverse fibers labelled by their point on the
arc. Backward time contracts z and each fiber tends to its labelled
equilibrium. This proves the local interior fiber statement without
assuming a global foliation or extending it across an endpoint.

## 4. An elementary outgoing wedge beyond an endpoint

This proves the outgoing part of lead E1 directly, without presuming
smooth unstable fibers across the endpoint. At an endpoint p use
orthonormal coordinates(s,z) with s tangent and increasing beyond
gamma, z normal. The linear field is(0,4z). Let z=k(s) be the nullcline
of the normal component, k(0)=k'(0)=0. The arc occupies s<=0 nearby.
Put t=z-k(s), and write the original tangential and normal components as

    W_s=f(s)+b(s,t)t, W_z=a(s,t)t,                    (2)

where a(0,0)=4, b(0,0)=0. Since f vanishes along the arc for s<=0,
f is infinitely flat at0; only f(0)=f'(0)=0 is needed below. Z here is
exactly t=0,f(s)=0. Thus either such zeros accumulate from s>0,
or f has a fixed nonzero sign on some(0,epsilon). Consider the
outgoing case f>0 there.

We construct a nonempty open set whose backward trajectories tend to p.
In backward time u, equations(2) become

    ds/du=-f(s)-b(s,t)t,
    dt/du=-a(s,t)t+k'(s)[f(s)+b(s,t)t].              (3)

For s>0 set rho=t/f(s). Its exact derivative is

    d rho/du=(-a+k'b)rho+k'+f' rho(1+b rho).         (4)

Choose a fixed eta>0 and shrink epsilon and the strip so a>=3,
|b|eta<1/2, and k',f' are small enough that the right side of(4)
is negative at rho=eta and positive at rho=-eta. This is possible
because k'(0)=f'(0)=0, with bounded b. The wedge

    N={0<s<epsilon, |t|<eta f(s)}

is then backward invariant: its two curved sides point inward by(4),
its upper s-boundary points inward by(3), and
-f(s)*3/2 <= ds/du <= -f(s)/2. Since f is smooth and f(0)=0,
f(s)<=C s near0. Gronwall prevents reaching s=0 in finite backward
time. As u tends to infinity s decreases to0, since a positive limit
would have f bounded below and contradict (3). Also t=rho f(s)->0.
Every such trajectory remains in a compact small neighborhood and tends
to p. Completeness rules out any other finite-time loss.

Transport gives Theta=L on all of N. Since N is open, Theta_x=0 there.
For Y in N its entire backward trajectory stays in N, so the vorticity
equation gives Omega(phi_-u Y)=e^u Omega(Y). Smooth boundedness in the
compact neighborhood forces Omega(Y)=0. Let
O=union_{u>=0}phi_u N. Backward invariance of N makes O invariant in
both time directions; it is open and nonempty. The same transport
formulas give Theta=L, Omega=0 on O. Hence U is harmonic there by
div-curl, but no analyticity elsewhere follows.

The open set O contains escaping trajectories. Otherwise every forward
trajectory starting in a fixed bounded small open subset of N would
remain in the common large disk beyond which radial velocity is outward.
Its image area grows as e^(4u), impossible within that disk. An escaping
orbit and openness give an open interval of launch points on a large
circle in O. The established C1 exterior scattering map sends these
to a nonempty open angular interval. At beta2 the leading temperature
and vorticity coefficients on it are respectively L and0. This is
consistent with a nonzero vorticity tail on other angles.

To compare this intrinsic sign with lead E1's finite-regularity center
curve, write that invariant curve as z=h(s), tangent to the kernel.
The normal equation and factorization(2) give
W_z(s,h)=A_h(s)[h(s)-k(s)]=h'(s) f_c(s), A_h->4.
The tangential equation gives
f_c=f+B_h[h-k]=f+B_h h' f_c/A_h. Hence
f=f_c[1-B_h h'/A_h], whose bracket tends to1. Their signs agree near p.
The outgoing-wedge conclusion thus covers the stated outgoing center
flow case. The present proof requires no choice of a center curve to
establish the result. In the negative-sign case, no new conclusion is
claimed here beyond the nullcline sign; and accumulating zeros remain
allowed. Reflection gives the same classification at the other endpoint.

Dependencies: elementary ODE existence, IFT, Taylor expansion, compact
one-dimensional topology, divergence theorem, and for the final angular
sentence the previously verified exterior scattering theorem33. No
numerical evidence is used. Source R1-R4 and interior-fiber proof were
independently rederived; the outgoing wedge argument is new here.
