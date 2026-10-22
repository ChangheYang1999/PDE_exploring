# Smoothness of the escape conjugacy away from the trapped set

Date:2026-10-20. Status: CONFIRMED after independent proof and actual Claude Opus 5.5 review.
This is a regularity corollary of the already proved local continuation
estimates. It is not an existence or nonexistence endpoint.

## 1. Exact statement and dependencies

Let beta>=2 and let a smooth full-plane B2 profile satisfy the prompt's
sublinear canonical-velocity and polynomial-tail hypotheses. Write
V=U-U(0), W=beta X+V. The defining B2 incompressibility equation gives
div U=div V=0 and div W=2beta. Let phi_t be the complete flow of W. Let E be
its forward escape set. Packets33 and39 prove that

    Phi(Y)=lim_{t->infinity} e^{-beta t} phi_t(Y)

is a C1 diffeomorphism E onto R2 minus0, detDPhi=1, and
Phi(phi_tY)=e^{beta t}Phi(Y). Packet36 Section6 proves that

    u_tau(z)=tau^{beta-1}V(tau^{-beta}z)

converges in every spatial C^j norm on compact subsets of R2 minus0 as
tau decreases to0. In particular all such norms are bounded locally
uniformly through tau=0. Only this proved velocity consequence is needed
below. No time derivative of u_tau is presumed bounded.

Then Phi and its inverse are C-infinity on their open domains. The
functions t(Y)=beta^{-1}log|Phi(Y)| and local branches
alpha(Y)=argPhi(Y) are C-infinity on E, with

    W.grad t=1, W.grad alpha=0.

No smoothness or extension through the trapped set is asserted. In
particular this result does not remove a resonant obstruction to smooth
linear coordinates at the source itself.

## 2. A finite-time representation

Fix Y0 in E, q=Phi(Y0)!=0, and rho>0 so that the closed ball
B(q,4rho) avoids0. Put tau=e^{-t} and

    z(tau,Y)=tau^beta phi_{-log tau}(Y).

Direct differentiation, with no equation for a pressure, gives

    partial_tau z=-tau^{beta-1}V(tau^{-beta}z)=-u_tau(z).  (1)

Since z(tau,Y0) tends to q, choose tau0>0 so small that
z(tau0,Y0) lies in B(q,rho), and M tau0<rho, where
M bounds |u_tau| on B(q,4rho) for 0<=tau<=tau0. Such an M is finite
and can be chosen first on a fixed sufficiently small time interval by
packet36, then tau0 is decreased. By continuity of the finite-time flow,
z(tau0,Y) lies in B(q,2rho) for all Y in a neighborhood N of Y0.
A solution of (1) starting there at tau0 moves at most M tau0<rho
before time0, so it remains in B(q,3rho). The bound is justified up to
the first possible exit and therefore excludes that exit. Uniform local
Lipschitz continuity gives uniqueness at positive times and the bounded
velocity gives an endpoint at tau=0. These nearby trajectories have nonzero
scattering limits, so N lies in E. Denote its endpoint
map, from time tau0 to0, by H. On N,

    Phi(Y)=H(tau0^beta phi_{-log tau0}(Y)).               (2)

Indeed (1) has the same finite positive-time solution as the original
rescaled orbit, and its time0 value equals the defining scattering limit.

## 3. Spatial derivatives of the endpoint map

The coefficient u_tau is continuous through0 in every spatial C^j norm
on the ball. At positive times the map H_epsilon from tau0 to epsilon
is smooth in its initial position. Its first derivative J satisfies
J'=-Du_tau(z)J. Uniform bounds and Gronwall bound J on the entire finite
time interval. Its derivative in tau is also bounded, so J has a uniform
limit on compact initial-position sets as epsilon decreases to0.

Inductively, the order-n derivative J_n satisfies a linear equation

    J_n'=-Du_tau(z)J_n+P_n,

where P_n is a finite sum of products of derivatives D^k u_tau with
2<=k<=n and lower flow derivatives. The preceding induction bounds every
factor uniformly; Gronwall bounds J_n, and its equation bounds its time
derivative. Thus J_n converges uniformly as well. These statements are
local in the initial position and for each finite n separately. If the
C^j convergence statement initially supplies different small intervals
for different j, smoothness on the remaining compact positive-time
interval supplies bounds up to the same fixed tau0, for each j separately.
No common bound over all derivative orders is needed. Passing
to the limit in the fundamental theorem of calculus on short line
segments shows that the uniform limits are the corresponding derivatives
of H, successively. Therefore H is C-infinity. Formula(2) proves that Phi
is smooth near Y0. The point Y0 was arbitrary in E.

Because div_z u_tau=0, the first derivative equation also gives
partial_tau detJ=0 and detDH=1. Alternatively this is already supplied by
the C1 scattering theorem. The finite-time inner map in(2) has determinant

    tau0^{2beta} exp(2beta(-log tau0))=1.

Hence detDPhi=1. Its already proved global bijectivity and the smooth
inverse function theorem imply a smooth global inverse. The formulas
for t and alpha and their transport equations follow by differentiating
the exact conjugacy.

## 4. Scope

This argument requires only continuity in time with uniform spatial
smoothness of u_tau. It does not assert smoothness in tau at0. In
particular a tau log tau correction to the velocity at beta2 is compatible
with the proof. It also gives no estimate uniform in derivative order,
no analytic regularity, and no control approaching the trapped set.

The C1-only proofs in packets54,58,59 remain valid and useful under their
weaker explicitly stated inputs. Once packet36 is invoked, use of higher
spatial derivatives of the scattering coordinates on compact subsets of
E is legitimate. This provides no new exclusion of flat extrema or
plateaus.

## 5. Verification record

The informal argument was written directly from the exact rescaling
identity and independently checked derivative equations. No numerical
test, formal proof assistant or numerics-lane implementation is required.
Actual Bedrock review opus_reviews/60_smooth_scattering returned
claude-opus-5-5 on 2026-10-20T19:02:02.642807Z after 37.029313 seconds.
It checked the rescaled ODE, localization, spatial derivative induction,
determinant and inverse, and found no substantive gap. Its requested
explicit div V=0 hypothesis has been added from the defining B2 equation;
its observation that the local representation also proves N subset E is
now stated. The unnecessary phrase uniqueness through tau=0 was removed.
The verifier independently checked each suggestion before adoption.
