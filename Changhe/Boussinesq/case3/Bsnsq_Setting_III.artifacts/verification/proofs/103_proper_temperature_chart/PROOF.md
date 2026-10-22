# A proper canonical chart from a certified exponent-three temperature

Written UTC: 2026-10-21T01:37:56.522827+00:00
Status: CONFIRMED by independent proof and numerical tests; actual claude-opus-5-5 review128 completed. Updated 2026-10-21T01:46:56.407222+00:00.
This constructs coordinates and, optionally, a transport-exact auxiliary field. It does not solve the vorticity equation or identify the canonical inverse.

## Statement and hypotheses

Let L>0. Suppose a real temperature has the form Theta=x^2 F with x-even F of class C2 on the plane, and put

    z=(1+(x^2+y^2)/L^2)^(-1/6),
    A=z^(-5)F, B=z^(-5)(2F+x F_x).

Assume there are constants 0<a_*<=a^*<infinity and 0<b_*<=b^*<infinity such that a_*<=A<=a^* and b_*<=B<=b^* everywhere. These hypotheses follow for the finite fields of packet102 if its strict coefficient certificate covers the closed compactified rectangle and the splines have at least C2 regularity. Let s0(q) be any odd C3 function with s0'(0)=0. Set a0=F(0,0)>0 and define

    q(x,y)=x sqrt(F(x,y)/a0).

Then (x,y)->(q,y) is a global C2 diffeomorphism, with inverse x=X(q,y). Define

    S(q,y)=integral_0^y X(q,v)dv+s0(q),
    eta(q,y)=S_q(q,y)=integral_0^y X_q(q,v)dv+s0'(q).                (1)

The map (q,y)->(q,eta) is a global C1 diffeomorphism. The resulting map (x,y)->(q,eta) preserves oriented area, is global and has the reflection parity q(-x,y)=-q(x,y), eta(-x,y)=eta(x,y). Moreover S is odd in q,

    S_qy>0, S_qy(0,0)=1, S_q(0,0)=0, Theta=a0 q^2.         (2)

Both global maps, including their continuous inverses, are proper. No assertion about dynamical linearization is made.

## Proof of the first map

Differentiation and the definitions give

    q_x=(2F+x F_x)/(2 sqrt(a0 F))
        =z^(5/2) B/(2 sqrt(a0 A))>0.                       (3)

In particular, with M=b^*/(2 sqrt(a0 a_*)), one has q_x<=M on the whole plane. At each fixed y, the lower bound for A gives

    |q(x,y)| >= sqrt(a_*/a0) |x| (1+(x^2+y^2)/L^2)^(-5/12).

As x tends to either signed infinity at that fixed y, the right side is asymptotic to a positive constant times |x|^(1/6). Therefore q(x,y) tends to the same signed infinity. Equation(3), continuity and the intermediate value theorem give a unique X(q,y) for every real q,y. The local inverse function theorem, applied at every point and patched by uniqueness, makes X a global C2 function. Thus the first map is a global C2 diffeomorphism. It also yields

    X_q=1/q_x(X(q,y),y)>=1/M>0.                            (4)

Evenness of F makes q odd in x, hence X odd in q. At the center q_x(0,0)=sqrt(F(0,0)/a0)=1.

## Proof of the second map and area identity

The integrals in(1) are over finite intervals. Since X is C2, differentiation under the integral is valid locally and eta is C1. Its derivative at fixed q is

    eta_y=X_q(q,y)>=1/M.

Also eta(q,0)=s0'(q). For fixed q and y>=0 this gives eta>=s0'(q)+y/M; for y<=0 it gives eta<=s0'(q)+y/M. Thus for each fixed q the map y->eta is strictly increasing and onto the real line. The inverse function theorem again produces the unique global C1 inverse. Oddness of X and s0 implies oddness of S and evenness of X_q and eta in q. The normalization in(2) follows from(1) and X_q(0,0)=1.

In mixed coordinates, differentiation gives

    dx wedge dy=X_q dq wedge dy,
    dq wedge d eta=eta_y dq wedge dy=X_q dq wedge dy.

Therefore dq wedge d eta=dx wedge dy. The maps are global homeomorphisms of the plane with continuous inverses; the inverse image of a compact set under either is the continuous image of that compact set by the inverse, hence compact. This proves properness. Finally q^2=x^2F/a0 is exactly the asserted temperature identity.

The assumptions provide more than Theta_x>0. The positive lower bound on the compactified A gives horizontal growth; the finite upper bound on B gives the uniform upper bound in(3). The lower bound on B and upper bound on A are stronger than needed: pointwise B>0 suffices for strict monotonicity. Monotonicity alone would not justify either properness statement.

## What the sign certificate supplies

For a packet102 representation, A=E+rho O and B=E_S+rho O_S. A finite certificate has finitely many leaves. The minimum of their strictly positive exact lower bounds supplies a_*,b_*. The maximum of their finite exact upper bounds supplies a^*,b^*. These bounds include the t=1 edge. The actual input degree and interior knot multiplicities check the needed regularity; the intended degree-five simple-interior-knot fields are C4. The origin-mask argument supplies smoothness near0. Thus no separate far-field sign assumption is needed for a successful full closed-rectangle certificate.

## Optional transport-exact construction and its limits

Assume enough extra regularity for the following derivatives, for example the actual C4 field and a smooth s0. For any beta>2 let p=beta/2-1 and mu=3beta/2+1. In the mixed chart put J=S_qy=X_q and

    V=(mu S_q-p q S_qq)/J,
    W_1=p q J+S_yy V, W_2=V.                              (5)

Then q-dot=pq and eta-dot=mu eta: the first follows by differentiating x=S_y along(5); the second is S_qq p q+J V=mu S_q. The area-preserving coordinate identity gives div W=p+mu=2beta. Alternatively differentiate(5) in the mixed chart and use equality of mixed partials. Since Theta=a0q^2, W.grad Theta=2p Theta=(beta-2)Theta. The origin is stationary by(2). The exact stream of U=W-beta(x,y), expressed in the mixed variables, is

    Psi=2beta S-p q S_q-beta y S_y.                        (6)

Indeed D_x=J^(-1)partial_q and D_y=partial_y-S_yy J^(-1)partial_q. Applying these to(6) gives Psi_x=V-beta y and -Psi_y=W_1-beta x, using 2beta-p=mu. Its center mixed derivative is beta-p=1+beta/2, since S=q y to second order at0. This is the kappa=0 construction. It neither asserts that an arbitrary resonant B2 profile has kappa=0 nor solves the remaining equation for Omega=-Delta Psi.

The free function s0 must not be silently discarded when using this construction as a search representation. At y=0, (5) gives J V=mu s0'(q)-p q s0''(q). Setting s0=0 imposes W2(x,0)=0, an extra invariant-line restriction that the B2 prompt does not supply. It is permissible as a manufactured test or explicitly restricted auxiliary field, but not as a claim of coverage of the full B2 class. Retaining arbitrary s0 avoids that imposed trace. This freedom does not affect either coordinate properness proof.

Even if(5)-(6) are evaluated exactly, the vorticity equation, its center normalization, sublinear velocity, polynomial vorticity and full-plane inverse closure all remain to be checked. The constructed field need not equal the velocity used to obtain the original forced snapshot. A successful coordinate initializer is not a candidate profile.

## Dependencies and evidence

The geometric proof is given in full above. Packet102 supplies exact sign certificates for a particular finite representation. Packet100 independently derives the stream and remaining PDE formulas; equations(5)-(6) were also checked here. Numerical inversion and quadrature tests, if used, are separate from this geometric proof. No formalization, Lean or Lake execution is claimed.
