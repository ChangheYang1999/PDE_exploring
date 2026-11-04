# Rotation-invariant invariant probabilities

## Statement

Let U in C2(R3;R3), P in C1(R3) be an exact divergence-free rotating Euler profile, B=cy-omega Jy+U, X=cy+U. Let c differ from 1/2 and omega be nonzero. Let mu be a compactly supported probability invariant under both the B flow and every rotation exp(theta J). It suffices that the flow is defined on its compact support; bounded U guarantees a global flow. Then X vanishes on supp mu. Every orbit in the support is either a zero of B on the rotation axis or a horizontal circle centered on that axis, with period 2pi/|omega| and U=-cy along it.

For 0<c<1/2, without assuming rotation invariance, every compactly supported B-invariant probability satisfies

    omega integral partial_theta P dmu=(2c-1) integral |X|^2 dmu<=0.

Equality holds exactly when X=0 on its support.

## Proof

The Bernoulli and angular-momentum identities, integrated against mu, give

    integral |X|^2 dmu=omega integral (Jy.U) dmu,
    integral partial_theta P dmu=(2c-1) integral (Jy.U) dmu.

These follow from the full momentum equation, not from an independent bracket eigenfield. They imply the displayed torque relation. Rotation invariance and compact support allow differentiation of

    integral P(exp(theta J)y) dmu(y)=integral P(y) dmu(y)

at theta=0. Thus the pressure-torque integral is zero. Since 2c-1 is nonzero, the integral of |X|^2 is zero. Continuity gives X=0 on the support, which is invariant under the B flow. There B=-omega Jy, so uniqueness of the ODE gives the asserted rotating circles or fixed axis points. U=-cy follows directly from X=0.

## Scope

This confirms Theory Agent C C17 and Proposition 3.1. It does not produce a rotation-invariant B-invariant probability for an arbitrary profile. Averaging a B-invariant measure over rotations need not preserve B invariance when B is not rotation equivariant. Thus the proposition does not settle the positive-entropy case.

If a nonzero torque is expressed using angular Fourier coefficients, one can use Fejer sums of the continuous angular derivative of P on a compact set. Their uniform convergence justifies passage to a possibly singular measure and implies some nonzero angular mode pairs nontrivially with that measure. No unqualified interchange of an infinite Fourier series and a singular integral is necessary.

Audit date: 2026-11-02T19:37:03Z. Dependencies: A003, A018, A104 and elementary flow invariance.
