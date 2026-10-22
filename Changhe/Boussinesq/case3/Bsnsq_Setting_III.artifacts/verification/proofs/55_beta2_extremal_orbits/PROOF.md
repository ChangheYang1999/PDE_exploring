# Extremal temperature forces a zero-vorticity escaping orbit at beta two

Date:2026-10-20. Status: CONFIRMED by independent verifier at 2026-10-20T18:01:37.464056+00:00.
This is a strict-sign exclusion, not full nonexistence.

## 1. Statement under minimal transport hypotheses

Let W=2X+V be a C1 full-plane field with V=o(|X|), div W=4 and
W1(0,y)=0. Let Theta,Omega be C1 and satisfy

    W.grad Theta=0, W.grad Omega+Omega=Theta_x.

Assume Theta(0,y)=0 and that Theta has a nonzero quadratic center jet
 a0 x^2+O(|X|^3), a0!=0. The full B2 target satisfies all these hypotheses;
this theorem does not require its elliptic inverse or quantitative tails.
Then in the open right half-plane there is a complete nonconstant orbit
which escapes to infinity forward and on which

    Theta=Theta_*, sign(a0)Theta_*>0,
    grad Theta=0, Omega=0.                            (1)

Consequently Omega cannot be strictly positive everywhere on x>0,
strictly negative everywhere there, or everywhere nonzero there.
The analogous reflected orbit exists for the B2 reflection-symmetric
fields. Nonnegative or nonpositive vorticity with zeros is not excluded.

## 2. Compact cross-section and temperature range

Sublinearity gives W.X>=|X|^2 outside a fixed disk B_R. Linear growth
and local Lipschitz regularity make the flow phi_t complete. Every
negative semiorbit is bounded: the reversed flow cannot cross outward
through any circle beyond max(R,|X_initial|). Every forward orbit which
leaves B_R escapes, since rdot>=r outside.

Let K be the set of bounded forward orbits. It is the intersection
over t>=0 of phi_{-t}(closed B_R), hence compact, and is invariant under
the full flow. Indeed a bounded forward orbit cannot be outside B_R
at any time, and any time translate of a bounded forward orbit is
bounded forward. Liouville's formula gives

    |phi_tK|=e^{4t}|K|.

Since phi_tK=K and K has finite area, |K|=0. Thus E=R2 minus K is open
and dense. Each E orbit crosses the circle Sigma=partial B_R exactly
once. Existence follows from forward escape for an inside point and
finite backward entry for an outside point; rdot>=r bounds the time
needed in either direction. Uniqueness follows from strict outward
crossing on Sigma and the impossibility of returning after escape.

The invariant axis cannot be crossed by uniqueness. The open right
half-plane is invariant in both time directions. Thus every E orbit
there crosses precisely the open right semicircle Sigma_+, and
transport gives Theta(E intersect{x>0})=Theta(Sigma_+).

Set sigma=sign(a0). There is a point in E with x>0 and sigma Theta>0:
the quadratic center jet makes this inequality hold on an open set,
and E is dense. Its orbit carries a positive value to Sigma_+. The
continuous function sigma Theta on the CLOSED right semicircle has
a positive maximum M. Its two endpoints lie on the invariant axis,
where Theta=0, so the maximum occurs at an interior point P of Sigma_+.
For all E points in the right half-plane, sigma Theta<=M by transport;
density and continuity extend the inequality to the entire open
right half-plane. Therefore P is a genuine global maximum of sigma
Theta on that open half-plane, not merely an angular maximum.

## 3. Vorticity on the maximum orbit

The entire orbit through P stays in x>0 and has sigma Theta=M by
transport. Every one of its points is consequently a maximum in the
open half-plane, and differentiability gives grad Theta=0 there.
The vorticity ODE along this orbit reduces to d Omega/dt=-Omega.
If Omega(P)!=0, then Omega(phi_{-t}P)=e^t Omega(P) would be unbounded
as t->infinity. Its negative semiorbit lies in a compact ball, on which
the continuous Omega is bounded. Thus Omega(P)=0, and the ODE gives
Omega=0 on the complete orbit. The orbit is nonconstant and escapes
forward because P lies on the strictly outgoing circle. This proves(1).
No sign assumption on Omega was needed in the construction.

## 4. Angular corollary in the actual B2 class

For the full target, packets33,36,39 give a smooth limiting angular
temperature h and nonzero leading angular vorticity a, and the scattering
map Phi from05 is a C1 diffeomorphism conjugating the flow to dilation.
Packet54 proves the exact implication

    hprime(alpha)=0 implies Omega=0 on its whole escaping orbit,
                             and hence a(alpha)=0.    (2)

The conclusion also follows from Section3 at a maximum orbit without
differentiating the scattering map. The scattering limit commutes with reflection, Phi(SY)=S Phi(Y),
because the flow does. This equivariance and injectivity of Phi make Phi1(Y)>0 when x(Y)>0: the flow preserves x>0, so the limit Phi1
is nonnegative; equality would give Phi(SY)=Phi(Y) with SY!=Y.
Consequently the maximum orbit in Section3 has a limiting direction
strictly inside the right semicircle. Its a value is zero.

In particular a cannot be nonvanishing throughout the open right
semicircle. A pure first harmonic a=A cos(alpha), A!=0, is excluded
at beta2 using only its first term. This is stronger at beta2 than
packet52's two-term dipole theorem, and is still a shape restriction.
It does not say a must change sign: a may be nonnegative and have zeros.

For completeness, every value of Theta on R2 occurs on the fixed large
circle: E is dense, transport transfers E values to Sigma, and the
compact set Theta(Sigma) is closed. Thus the temperature is bounded
and attains both extrema on regular escaping orbits, including zero
extrema. The nonzero extremum needed above is forced
by the center jet; no normalization of its sign was silently added.

## 5. Scope and dependency audit

Sections1-3 use only elementary ODE uniqueness, Liouville area change,
compactness, continuity and the two transport equations. They use no
positive-vorticity Biot-Savart sign, no wall, no horizontal reflection,
and no fixed material center. In B2, V=U-U(0) throughout. The center
can have nonzero physical velocity. The inverse and scattering facts
are needed only for the angular corollary, and were independently
checked in the cited packets. There is no numerical certificate or
formalization; the result has a complete informal proof above.

Actual claude-opus-5-5 review45 returned a usable independent audit in44.963618009seconds at18:02:22Z, confirming Sections1-3 and checking the angular corollary with its declared scattering dependencies. The verifier checked the response, explicitly stated equivariance, and adopted the valid stronger range observation. The same strict-sign orbit argument also works independently in the left half-plane without reflection; B2 reflection specifically pairs the two orbits. No weak-sign exclusion follows.
