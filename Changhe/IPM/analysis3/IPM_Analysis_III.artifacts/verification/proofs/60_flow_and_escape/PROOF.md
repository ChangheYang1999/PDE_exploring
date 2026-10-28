# Conditional quadrant dynamics and compact escape functions

## Exact statements

Let V be a globally Lipschitz C1 vector field on R2, equivariant under
reflection in each coordinate axis. Suppose, for constants ell,A,D>0
and 0<k<1,

    div V=2ell,
    V(x,y)=(-Ax,Dy)+O(|(x,y)|^3) at0,
    V(X)=ell X+O(|X|^k) at infinity.

Let Q={x>=0,y>=0}. Assume additionally

    (Z) the only zeros in Q are0 and P=(p_*,0), p_*>0,
        and P is a hyperbolic repeller.

Then:

1. Every orbit in the open quadrant has alpha-limit P and escapes to
   infinity in forward time.
2. On the x-axis, (0,p_*) flows from P to0 and (p_*,infinity) flows from
   P to infinity. The positive y-axis flows from0 to infinity.
3. If K is any compact subset of R2 containing no zero of V, there is
   phi in C_c^infinity(R2) with V.grad phi>=1 on K. For reflection-invariant
   K, phi can be chosen even in each coordinate. For a compact subset
   of Q avoiding0,P, take its reflection closure to obtain the same
   even function. This third statement only needs C1 global flow,
   div V>0 everywhere, and absence of zeros on K. It does not need (Z)
   outside K or the specified endpoint asymptotics.

All assertions are qualitative. No numerical norm of phi is asserted.
The actual IPM field has the regularity, parity, divergence and endpoint
properties verified in topics01 and52. The certified source box in
proof 15 proves a local repeller. A global verification of (Z) is still
required before applying statements1-2 to the actual field.

## Flow and boundary classification

Global Lipschitz continuity gives a complete unique C1 flow Phi_t. Axis
reflection invariance implies that both axes and each open quadrant are
invariant, for positive and negative time. For sufficiently large R,

    d|Phi_t X|/dt >= (ell/2)|Phi_t X| whenever |Phi_t X|>=R.   (1)

Thus each backward orbit is bounded by max(R,|X|). Once a forward orbit
crosses the sphere of radius R outward it never returns and tends to
infinity. Any forward orbit that does not tend to infinity is bounded.

On the positive x-axis the scalar velocity has no zero except p_*.
Its sign is negative near0 and positive at large x. Continuity and (Z)
make these the signs on the entire intervals (0,p_*) and (p_*,infinity).
The scalar ODE therefore gives precisely the x-axis limits in statement2.
On the positive y-axis its sign is positive near0 and it has no zero;
this proves the y-axis claim. Finite-time arrival at an equilibrium or
escape to infinity is excluded by uniqueness and global Lipschitz growth.

## Excluding recurrent limits

A nonconstant periodic orbit would be a simple closed C1 curve. V is
tangent to it. Applying the divergence theorem to the bounded Jordan
interior gives

    0 = integral_boundary V.n ds = 2ell area(interior)>0,

which is impossible. The same argument excludes any finite simple
separatrix cycle with a nonempty interior, although that stronger fact
is not needed below.

We use the generalized planar limit-set theorem in its precise C1 form:
a nonempty compact alpha- or omega-limit set with finitely many stationary
points is either one stationary point, one periodic orbit, or a union
of stationary points and trajectories whose two limits are stationary
points in that set. See Gerald Teschl, Ordinary Differential Equations
and Dynamical Systems, author version, Theorem7.16, pp223-224. The exact
version inspected is archived with its digest. This is the only planar
limit-set theorem used here.

A repeller cannot belong to the omega-limit of another orbit. To see the
needed local fact, translate P to0 and write V=BX+o(|X|), where B has
positive real parts. Choose a positive definite quadratic form whose
matrix solves B^T H+HB=I. On a sufficiently small ellipsoid the derivative
of X^T H X is strictly positive away from0. An orbit outside that
ellipsoid cannot enter it in forward time; a nonconstant orbit inside
leaves a smaller ellipsoid. Hence P is not in its omega-limit. In
backward time the ellipsoid is attracting. If P belongs to an alpha-limit,
a sufficiently late backward visit enters that trapping neighborhood and
the backward orbit converges to P. Its entire alpha-limit is then {P}.

At0, the local stable manifold is the x-axis and the local unstable
manifold is the y-axis. Indeed the linear rates are -A and D, and the
axes are invariant. Uniqueness of the local hyperbolic stable and
unstable manifolds identifies them with those axes. Consequently an
orbit converging to0 forward must lie on the x-axis, and one converging
to0 backward must lie on the y-axis. There is no nonconstant homoclinic
orbit to0, because it would have to lie on both axes.

Consider an interior orbit. Its alpha-limit is nonempty and compact by
(1). If it contains P it equals {P}, as just proved. Otherwise (Z) leaves
only0 as a possible stationary point. The limit-set theorem, the absence
of periodic orbits, and the absence of a homoclinic orbit to0 imply that
the alpha-limit must be {0}. That would put the orbit on the y-axis, a
contradiction. Its alpha-limit is therefore P.

If its forward orbit were bounded, its omega-limit would be nonempty and
compact. It cannot contain P. The same limit-set alternatives would make
it {0}, putting the orbit on the x-axis. This is again impossible.
Therefore the forward orbit is unbounded, and (1) makes its radius tend
to infinity. This proves statement1.

## A compact escape function by separation

This argument is independent of the orbit classification above. The empty K case is trivial. Let K
be nonempty, compact and contain no zero of V. In the real Banach space C(K), set

    S={ (V.grad f)|K : f in C_c^infinity(R2) },
    P_+={g in C(K): min_K g>0}.

S is a linear subspace; it need not be closed. Suppose S does not meet
the open convex cone P_+. Geometric Hahn-Banach separation supplies a
nonzero continuous functional L on C(K) annihilating S and nonnegative
on P_+. Annihilation follows because S is a linear space, and positivity
on every nonnegative continuous function follows by adding epsilon times
the constant1 and taking epsilon to0. In particular L(1)>0. The Riesz
representation theorem, followed by normalization, gives a probability
measure mu supported in K satisfying

    integral V.grad f dmu=0 for every f in C_c^infinity(R2).  (2)

The same identity holds for C_c^1 functions by compactly supported C1
mollification. For f in C_c^1 and fixed t, f o Phi_t is C1 and compactly
supported, because Phi_t is a homeomorphism of R2. The flow identity
D Phi_t(X)V(X)=V(Phi_t X) therefore gives

    d/dt integral f(Phi_t X)dmu(X)
       = integral V.grad(f o Phi_t)(X)dmu(X)=0.

Differentiation under the integral is valid on the compact support of
mu, locally uniformly in t. Thus (Phi_t)_*mu=mu for every real t. The
closed support S_mu of mu is nonempty, compact and invariant under the
whole flow. For example, if X belongs to S_mu and Phi_t X did not, an
open zero-measure neighborhood of Phi_t X would pull back to an open
zero-measure neighborhood of X, which is impossible.

Choose X in S_mu. Its forward limit set is nonempty, compact and contained
in K, and hence contains no stationary point. The planar limit-set
theorem gives a periodic orbit. Positive divergence excludes that orbit.
This contradiction proves S meets P_+. Take f giving a positive minimum
m on K, and put phi=f/m. This proves V.grad phi>=1 and phi is smooth,
compactly supported, and bounded.

For axis symmetries, replace K by its union of the four reflections if
necessary. It still contains no zero by equivariance. Apply the previous
argument there and average phi over the four reflections. For any such
reflection R, equivariance gives

    V(X).grad(phi o R)(X) = (V.grad phi)(R X).

Each summand is at least1 on the reflection closure of K. The average
retains the inequality and is even in x and y. Smoothness across the
axes follows from the ordinary smooth averaging, with no reflection
extension regularity assumption. This proves statement3.

## What does not follow

Condition (Z) cannot be inferred just from positive divergence and the
specified origin, source and far-field data. For instance, choose an
interior point Q_* away from those fixed neighborhoods. Add a compactly
supported Hamiltonian vector field near Q_* whose value cancels V(Q_*).
Its first derivative can also be prescribed as any trace-zero matrix:
for a scalar quadratic Hamiltonian this is exactly J times a symmetric
matrix. Since trace DV(Q_*)=2ell, choose that trace-zero correction so
the new derivative is ell times the identity. This creates a hyperbolic
repeller at Q_* while preserving divergence. Reflect the four disjoint
bumps equivariantly. The perturbation is zero near the axes, the original
fixed points and infinity. All the stated endpoint and parity hypotheses
survive, but (Z) fails. Other zeros needed by index constraints are not
excluded; their presence only strengthens the counterexample. This is
a logical independence example, not a perturbation of the selected
modal data used for a theorem about that data.

The escape proof gives no sign of V.grad phi outside K. Thus multiplication
of a global energy weight by exp(N phi) adds (N/2)V.grad phi to the scalar
energy coefficient on K, but may decrease it elsewhere. The comparison
of the old and new L2 norms also costs factors determined by N and the
oscillation of phi. A high-regularity theorem must control these effects,
its nonlocal terms and its variable-order commutators. The escape
statement alone proves none of these estimates. It supplies neither
numerical constants nor a uniform high inverse.

## Dependencies and status

Dependencies: global C1 flow for a globally Lipschitz C1 vector field;
local hyperbolic stable/unstable manifold uniqueness; the precisely
stated planar limit-set theorem; Hahn-Banach separation and the Riesz
representation theorem. Their applications and all problem-specific
steps are given above. Proof 52 verifies the actual field's endpoint and
regularity hypotheses; proof 15 supplies only a local source result.

Statements1-2 are CONFIRMED under (Z). Statement3 is CONFIRMED on compact
sets avoiding zeros without assuming (Z) elsewhere. Actual global (Z),
a globally compatible derivative-level weight and the high inverse are
OPEN. A numerical grid of the vector field is not a proof of (Z).
