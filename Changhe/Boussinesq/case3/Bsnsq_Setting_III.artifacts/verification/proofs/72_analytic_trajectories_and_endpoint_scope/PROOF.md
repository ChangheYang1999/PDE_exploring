# Analytic time trajectories do not force analytic closure at an equilibrium

Date:2026-10-20. Status: CONFIRMED elementary counterexample, independently derived. This is a scope result, not a Boussinesq profile or exclusion.

## Statement and notation

There exists a complete C-infinity planar vector field of constant divergence4 such that every trajectory is real analytic in time on the entire real line, but the invariant curve consisting of all points converging to one equilibrium in backward time is a smooth nonanalytic embedded curve through that equilibrium. Analyticity at each finite time therefore does not imply that a trajectory's closure at its infinite-time limiting equilibrium is an analytic curve.

Here real analyticity means local convergence to the Taylor series at every real parameter value. A real analytic embedded curve through a point has a regular real analytic parametrization near that point. No uniform complex-time neighborhood extending to infinite real time is assumed.

## Construction and complete proof

Define phi(s)=exp(-1/s^2) for s nonzero and phi(0)=0. Each derivative away from0 is a polynomial in1/s times exp(-1/s^2), and thus tends to0 at0. Repeated extension by0 proves phi is C-infinity and every derivative at0 vanishes. Since phi(s)>0 for s nonzero, it is not analytic at0.

In coordinates (s,n), define

    B(s,n)=(4s,4s phi'(s)).

The second component is8 s^-2 exp(-1/s^2) when s is nonzero, extended by0 at s=0. It and every derivative extend smoothly. The field has div B=4 because its second component is independent of n. It satisfies B(0,n)=0 for every n, and DB(0,n)=diag(4,0).

For initial data (s0,n0) the explicit flow is

    s(t)=s0 exp(4t),
    n(t)=n0+phi(s0 exp(4t))-phi(s0).

Differentiating gives s'=4s and n'=4s phi'(s), so this solves the initial value problem. Smooth local uniqueness identifies it with the flow. The expression is defined for every finite real t, proving completeness. For s0 nonzero, s(t) never vanishes at finite time and the formula is a composition of real analytic functions there, hence analytic at every real t. For s0=0 it is constant and analytic as well.

As t tends to minus infinity the orbit tends to (0,n0-phi(s0)). Consequently the set of initial points converging to (0,0) is exactly

    Gamma={(s,phi(s)):s in R}.

This is an invariant C-infinity embedded curve tangent to the s-axis at0. It is the strong unstable curve associated with the positive eigenvalue4: its nonconstant orbits approach0 at the positive linear rate in backward time, and the transverse equilibrium label n-phi(s) is constant.

If Gamma were real analytic as an embedded curve near0, take any regular analytic parametrization gamma(t) through0. Its tangent is horizontal and nonzero. Therefore its s-coordinate has nonzero derivative at0 and has a local real analytic inverse. The n-coordinate written as a function of s would then be real analytic. That function is phi(s), which has all zero Taylor coefficients at0 and is strictly positive nearby. This contradiction proves nonanalyticity of Gamma at0.

This does not contradict analytic trajectories: no nonconstant orbit reaches the equilibrium at finite time. It disproves the claimed passage from analytic finite-time trajectories to an analytic curve containing the limiting equilibrium, even with smoothness, completeness and constant positive divergence.

## Relation to the B2 open step

At a beta=2 flat endpoint, the audited local arguments in packets45,53,54 exclude an analytic strong unstable boundary curve through the endpoint. They do not establish that the curve must be analytic. A theorem asserting only finite-time analyticity of particle trajectories cannot fill that gap by itself, as the preceding example shows. An application would additionally need the right PDE, full-plane growth class, and an analytic continuation statement at the limiting equilibrium. The similarity flow W and the physical particle velocity are different vector fields and their time variables must also be distinguished.

The example B is NOT asserted to solve Euler or Boussinesq, have a canonical sublinear relative inverse, obey the marked B2 center jet, or have only one equilibrium. Its role is exactly the elementary implication refuted above. In particular B-2(s,n) has an affine part, so it is outside the prompt's velocity class. No conclusion about existence of a beta=2 profile follows.

## Dependencies and verification evidence

Only elementary differentiation, smooth flat-function estimates, ODE uniqueness and the one-dimensional real analytic inverse theorem are used. The full informal proof was written before any optional computation. No Lean or other formal build is run. The primary-text scope audit for the Euler trajectory result and the separate Zhang/Chen-Hou discussion is in ../../verification/literature_20261020T2100/SCOPE_AUDIT.md. That audit does not serve as a proof of either cited PDE theorem.
