# The finite list of first-order invariant-measure identities

## Statement and notation

Let U,P be a C1 exact rotating Euler profile on R3, div U=0, with 0<c<1/2 and omega arbitrary. Write B=cy-omega Jy+U, X=cy+U, M=Jy.U, q=|U|^2/2 and a=1-2c. Let mu be a compactly supported probability invariant under the B flow. All functions below are integrable, and invariance implies integral B.grad f dmu=0 for every C1 f on a neighborhood of the support.

Then

    integral (|X|^2-omega M) dmu=0,
    integral U.B dmu=0,
    integral U.grad P dmu=-(1-c) integral |U|^2 dmu,
    integral y.grad P dmu=integral ((2c-1)y.U+|U|^2) dmu,
    integral X.grad P dmu=-a integral |X|^2 dmu
                              =omega integral partial_theta P dmu.

These are the identities listed in B12. Their finite algebraic interdependence is confirmed. A classification of all first-order moment restrictions is not proved.

## Proof

The exact Bernoulli identity is B.grad H=-a X.B. Integrating and using a nonzero gives integral X.B=0, and X.B=|X|^2-omega M. Invariance with f=|y|^2/2 gives integral y.B=0. Thus integral U.B=integral (X-cy).B=0.

Dot the full momentum equation with U and integrate. The transport term is B.grad q and U.JU=0. This gives the third identity directly. Dot it with y next. Since

    B.grad(y.U)=B.U+y.(B.grad U),
    y.JU=-M,

integration gives integral y.grad P=-(1-c)integral y.U+omega integral M. The first identity and integral y.B=0 imply

    omega integral M=integral |X|^2
                      =c integral y.U+integral |U|^2.

Substitution proves the fourth identity. Add c times the fourth to the third. The result is (2c-1)integral (c y.U+|U|^2), which equals -a integral |X|^2. Finally B=X-omega Jy and invariance with f=P give integral X.grad P=omega integral partial_theta P.

Conversely, assuming the Euler equation, the third identity and the unreduced y-dot identity imply

    integral X.grad P=-(1-c) integral |X|^2+c omega integral M.

Comparison with the fifth identity, and c>0, recovers omega integral M=integral |X|^2. Thus the equivalence is valid within the exact Euler class.

## Limitation of the claimed completeness

The proof uses the full momentum equation, in addition to invariance and the first scalar identity. Those two scalar conditions alone do not supply all its other moments. For example let U=b be any nonzero constant, p=-(cI-omega J)^{-1}b, and mu=delta_p. This measure is B-invariant and X(p)=omega Jp gives |X(p)|^2=omega M(p). Choosing P=0 violates the third displayed identity. This is an example of scalar moment data, not an exact Euler counterexample; it explains where the missing momentum input enters the derivation.

For general smooth test vector fields V, the Euler equation also gives moments of V dot the momentum residual. No argument here classifies these identities or reduces all weighted versions to the displayed scalar relation. It therefore does not establish that every further restriction must use second derivatives or nonlocal information, or that every averaged monotonicity argument has been exhausted. Those universal assertions remain OPEN.

Audit date: 2026-11-02T19:35:29Z. Dependencies: A003, elementary invariant-measure differentiation, and the full momentum equation.
