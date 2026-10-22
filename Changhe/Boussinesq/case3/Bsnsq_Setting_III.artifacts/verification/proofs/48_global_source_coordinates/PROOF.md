# Global coordinates for a planar source with transported temperature

Date:2026-10-20. Status: CONFIRMED by independent construction and checked actual Opus37 audit.
This is a structural result, not an exclusion of the global-source class.
The proof replaces the uniqueness-of-linearization argument in the lead's
notes/global_source.md. That uniqueness claim is false at C1 regularity.

## Statement and exact hypotheses

Let beta>2, lambda=(beta-2)/2, mu=1+3beta/2 and p=mu/lambda>3.
Suppose W and Theta are smooth on the plane, with

    div W=2beta=lambda+mu, W=beta X+o(|X|),
    W(-x,y)=diag(-1,1)W(x,y), W(0)=0,
    DW(0)=diag(lambda,mu),
    Theta(-x,y)=Theta(x,y), Theta(0,y)=0,
    Theta=a0 x^2+O(|X|^3), a0!=0,
    W.grad Theta=2lambda Theta.

Assume0 is the only zero of W. Then every nonzero forward orbit escapes
to infinity and every backward orbit converges to0. There is a global
smooth area-preserving diffeomorphism Xi=(xi,eta), tangent to the identity
at0, with xi odd and eta even under x reflection, conjugating W to

    L=lambda xi partial_xi+mu eta partial_eta,

except possibly when p=k is an even integer. In that case there is a
global smooth area-preserving conjugacy to

    L=lambda xi partial_xi+(mu eta+kappa xi^k)partial_eta.    (1)

Here k>=4 and kappa is a real coefficient determined by the local
normal form. There is still a global area-preserving C^{k-1} conjugacy
to the linear field. In every case Theta=a0 xi^2 globally and
{xi=0}={x=0}. The coordinate result needs no vorticity equation.

For an actual B2 profile also impose the exact relations
V=U-U(0), W=beta X+V, Omega=-curl V and W.grad Omega+Omega=Theta_x.
Retain the polynomial source-growth assumption and the canonical relative
inverse convention of the prompt. Let X=(x,y)(xi,eta) be the inverse of the
smooth coordinate map (using model(1) in the resonant case), and put
{f,g}=f_xi g_eta-f_eta g_xi. Then {x,y}=1 and the remaining differential equations and sublinear-growth condition
are precisely

    Omega=-({Lx,x}+{Ly,y}),
    (L+1)Omega=2a0 xi y_eta,
    (L-beta)X=o(|X|).                                (2)

The parities, tangent-to-identity condition and center data must also
be retained. Equations(2) are a reformulation, not a solved equation
for the diffeomorphism X.

## 1. Global source geometry

Smoothness and W=O(1+r) give a complete flow phi_t. On a sufficiently
large circle and outside it, W.X>=beta r^2/2. Every backward orbit
therefore enters a fixed ball and remains bounded. The set K of
bounded forward orbits is contained in that ball: after an orbit exits,
r grows strictly forever. K is closed, since it is the intersection
of closed preimages of the ball for all nonnegative times. Hence K
is compact and invariant.

There are no periodic orbits. A periodic orbit is a Jordan curve;
uniqueness makes its enclosed disk invariant. Its area would be
multiplied by e^{2beta t}, contradicting invariance. Near0 the positive
definite diagonal derivative gives W.X>=c0 r^2. The boundary of a
small ball is crossed strictly outward, so a nonconstant forward
orbit eventually leaves this ball and cannot reenter. Thus0 is not
in the omega-limit set of a nonzero bounded forward orbit. The planar
Poincare-Bendixson theorem would then make that nonempty compact
omega-limit set, which contains no equilibrium, a periodic orbit.
This contradiction proves K={0}.

The alpha-limit set of any backward orbit is nonempty, compact and
invariant, and every point of it has a bounded forward orbit. It is
therefore contained in K={0}. The backward orbit converges to0.

## 2. A smooth weak coordinate and an area coordinate

Near0, divide the even temperature by x^2 to obtain a smooth F with
F(0)=a0 and F/a0>0. Define

    xi=x sqrt(F/a0).

It is smooth, odd in x, tangent to x at0. The transport equation gives
W.xi=lambda xi away from the axis; continuity gives the same identity
on it. Use the local variables (u,y)=(xi,y), writing x=x(u,y). Define

    eta0(u,y)=int_0^y [xi_x(x(u,s),s)]^{-1} ds.         (3)

The integrand is smooth near0 and equals1 at0. Thus (xi,eta0) is a
smooth coordinate map tangent to the identity. Its physical Jacobian
is exactly xi_x times (partial_y eta0 at fixed u), hence1. Since
xi_x is even in x, x(-u,s)=-x(u,s), and the integrand in(3) is even
in u. Thus eta0 is even under physical x reflection.

Shrink the image chart to an open box about0, so its vertical slices
are connected. In these coordinates the first component of the vector field is
lambda u. Preservation of area makes its divergence lambda+mu, so
the second component is mu eta0+h(u), with h smooth. The center and
diagonal derivative imply h(0)=h'(0)=0. Reflection makes h even.
No linearization theorem is invoked.

## 3. An explicit triangular normal-form calculation

Replace eta0 by eta=eta0+f(u). This preserves area and keeps the
first coordinate. The new second component is

    mu eta+h(u)+lambda u f'(u)-mu f(u).

Let k=p if p is an integer. If p is an even integer, set kappa equal
to the coefficient of u^k in h; otherwise set kappa=0. If p is an odd
integer, its potentially resonant coefficient is zero because h is
even. We seek

    lambda u f'-mu f=-h(u)+kappa u^k,                (4)

where the last term is omitted when kappa=0.

Choose an integer N>p, subtract the Taylor polynomial of
h_tilde=h-kappa u^k through degree N, and write the remainder as
u^{N+1}b(u), with b smooth by Taylor's integral remainder. For every
nonresonant Taylor coefficient h_j define
f_j=-h_j/[lambda(j-p)]; the resonant coefficient is absent. A smooth
solution of(4) is this polynomial plus

    f_rem(u)=-u^{N+1}/lambda int_0^1 t^{N-p}b(tu)dt.   (5)

The integrand and every u derivative are dominated because N-p>0.
Differentiating t^{N+1-p}b(tu) under its t integral verifies(4)
exactly. Also f is even, f(0)=f'(0)=0, so parity and the tangent map
are preserved. This proves the smooth local normal form(1), and the
linear form when kappa=0.

When kappa!=0, the further shear

    eta_linear=eta-(kappa/lambda)u^k log|u|

(with value0 for the added term at u=0) removes the resonant term.
The identity (u partial_u-k)(u^k log|u|)=u^k proves this directly.
Since k is even and k>=4, this shear is even, area preserving, tangent
to the identity and C^{k-1}. In particular it is C1. This step need
not be smooth; the smooth normal form is the correct alternative.

The even-resonance values are beta=2+8/(k-3), k even>=4. At beta3 and
beta2.5 the ratios p are respectively11 and19, both odd; reflection
eliminates the sole triangular resonance in this construction. This
does not repair a numerical representation's unrelated origin defects.

## 4. Extension to the entire plane

Let Phi_t denote the complete flow of the selected model (linear or
triangular). Every model backward orbit tends to0. In the resonant
case this follows explicitly from u(t)=e^{lambda t}u(0) and
eta(t)=e^{mu t}[eta(0)+kappa u(0)^k t]; as t tends to minus infinity,
both components tend to0. Define for sufficiently large positive t

    Xi(Y)=Phi_t(Xi_loc(phi_{-t}Y)).                  (6)

Choose a small physical disk contained in the local chart with
W.X>0 on its punctured closure. It is backward invariant. The backward
physical orbit enters this disk and stays there after a finite time. Local conjugacy shows that(6) is independent of the chosen
sufficiently large t. Locally about each fixed Y, a common finite t
works, so the asserted regularity follows from finite-time flows.
Both flows have Jacobian e^{2beta t}, and the local coordinate map
has determinant1, so det D Xi=1 globally. Parity also persists.

If Xi(Y1)=Xi(Y2), flow backward into the local chart and use its
injectivity to get Y1=Y2. Conversely any model point Z flows backward
into the open image of the local chart. Apply the local inverse there
and flow forward physically to obtain a preimage of Z. Thus Xi is
onto and is a global diffeomorphism. Transport propagates the local
identity Theta=a0 xi^2 to every Y. Since the axis is invariant and
xi has the sign of x near0, the zero-set and parity assertions follow.

## 5. Why the stated uniqueness argument cannot be used

Even for the linear model, the maps

    (u,v)->(u,v+D |u|^p), D real,

are C1 area-preserving conjugacies tangent to the identity, because
|e^{lambda t}u|^p=e^{mu t}|u|^p. They preserve both required parities.
For noninteger p>3 they are already C1 examples contradicting uniqueness
of normalized C1 eigen-coordinates. No uniqueness was needed in(3)-(6).
This counterexample does not refute uniqueness under a more restrictive
smooth nonresonant normalization; it refutes the C1 claim used in the
lead note as written.

## 6. Curl reformulation and an exact algebra check

The area condition gives partial_x g={g,y}, partial_y g={x,g} for
physical scalar fields pulled back to the model coordinates. Since
W composed with X equals LX and curl(beta X)=0, the task convention
Omega=-curl W gives exactly the first equation of(2). Also
Theta_x={a0 xi^2,y}=2a0 xi y_eta; conjugacy gives the other two.
A global diffeomorphism is proper, so |Xi| tending to infinity is
equivalent to |X| tending to infinity in the last condition.

For the linear model, the shear

    x=xi, y=eta+4a0 xi^2/[beta(beta+6)]

is area preserving and gives

    W1=lambda x, W2=mu y-2a0 x^2/beta,
    Omega=4a0 x/beta, Theta=a0 x^2.

Direct substitution verifies both transport PDEs and the center data.
Its relative velocity has linear and quadratic growth, so it violates
the sublinearity condition in(2). This checks the signs and the factor
in the lead's example without claiming an admissible profile.

## 7. Far-field positivity in the global-source class

This section is conditional on the already established class-A estimates and
scattering conclusions from packets14 and33. On a sufficiently large
exit circle, a0^{-1}Theta is positive away from its two axis points.
The angular scattering map is a circle diffeomorphism fixing the two
axis directions, and the rescaled radial limit rho is positive.
Temperature transport gives, with m=1-2/beta,

    A(theta_infinity)=Theta(Y_exit) rho(Y_exit)^{-m}.

Thus a0^{-1}A is positive exactly off the axis and vanishes exactly
at its two directions. Positivity of a finite-radius temperature
alone would not imply this limit statement; the scattering map and
its nondegeneracy supply the missing step.

Each level xi=s!=0 is the image of the connected proper line
{(s,eta):eta in R}. It has two unbounded ends. On either end Theta is
constant while r tends to infinity, so uniform far-field asymptotics
force every limiting angle to be an axis direction. This last
conclusion uses m>0 and does not apply at beta2.

Dependencies: elementary planar flow geometry and Poincare-Bendixson,
Taylor's integral remainder, local inverse function theorem, exact
area Jacobians, and packets14/33 only for Section7. No formal proof
assistant or numerical solver is used.

## 8. Review record

Actual Opus37 returned a detailed audit on2026-10-20 at17:27:04Z
(claude-opus-5-5,180.325190seconds). The verifier checked its response.
Sections1-6 were confirmed; a box restriction for h, an explicit
backward-invariant disk and the exact relative-velocity/PDE convention
were added. Section7 depends on the existing scattering results, which
the reviewer did not receive; the verifier separately checked those
dependencies against packets14 and33. The review supplies no new
nonexistence conclusion.

The Poincare-Bendixson form used in Section1 was checked against
Harald Hanche-Olsen, The Poincare-Bendixson theorem, TMA4165,
version2007-01-16, Theorem1: a compact forward orbit of a locally
Lipschitz planar field whose omega-limit contains no equilibrium has
a periodic omega-limit. In Section1 the source argument removes0
from that limit before this theorem is applied. The note explicitly
warns against using this conclusion when equilibria remain in the
limit set. No such extension is made here.
