# No terminal temperature plateau at an outgoing beta-two endpoint

Status: CONFIRMED by the complete independent argument and72 exact/numerical controls. Two actual Opus5.5 requests supplied no written audit; no external endorsement is claimed. This is a local necessary condition for profiles, not a full beta-two exclusion.

## 1. Exact statement

Let N be a neighborhood of p in the physical profile plane. Let W, Theta and Omega be C-infinity on N and satisfy

    div W=4, Omega=-curl W,
    W.grad Theta=0,
    W.grad Omega+Omega=partial_x Theta.                (1)

Suppose p is the endpoint of a nontrivial smooth arc gamma of equilibria, DW(p) has eigenvalues0,4, and the endpoint is outgoing. Precisely, in oriented tangent-normal coordinates (s,z), with p=(0,0), the normal nullcline z=k(s) is smooth, contains gamma for -epsilon<s<=0, and the reduced tangential component f(s)=W_s(s,k(s)) is zero there and strictly positive for0<s<epsilon. Thus locally no other equilibrium lies beyond p. These are the outgoing alternative of45 and53, or lead4.7(iv).

Then Theta restricted to gamma is not constant on any terminal subarc ending at p. In particular there is no epsilon0>0 such that

    Theta(gamma(s))=Theta(p) for -epsilon0<s<=0.       (2)

No vorticity sign, temperature sign, reflection, canonical inverse, far-field assumption or global condition Z=gamma is used in this local theorem. It applies to every outgoing endpoint of a full smooth beta2 B2 profile because those profiles supply exactly(1) and the endpoint geometry. It does not address incoming endpoints or accumulating additional zeros.

A useful stronger formulation of the same contradiction is that, under(2), equations(1) would force Theta constant, Omega zero and W real analytic on a full neighborhood of p, and then force the zero arc to continue through p. Thus an outgoing endpoint cannot be present.

## 2. Backward containment and local limits

The required finite-regularity invariant-curve input is explicit: a smooth field with spectrum{0,4} admits a local C4 center manifold and a local C4 strong unstable curve, tangent to the respective eigenspaces. Only existence of those two transverse curves is needed. Their hypotheses and source statements are recorded in53, verification/INVARIANT_MANIFOLD_SOURCES.md. This is a standard theorem dependency, not a claim proved numerically here. All subsequent estimates are supplied below.

Write the center manifold as z=H(s). In coordinates eta=z-H(s), invariance gives eta'=d(s,eta)eta, d(0,0)=4. Hence every nearby equilibrium lies on this center curve. In particular the existing zero arc does. Its tangential field g(s)=W_s(s,H(s)) has the same sign as f(s) beyond p. Indeed, mean values and invariance give

    A(s)(H-k)=H'(s)g(s),
    g(s)=f(s)+B(s)(H-k),
    g(s)[1-B(s)H'(s)/A(s)]=f(s),                    (3)

where A(s)->4, H'(s)->0 and B is bounded. The bracket is positive after shrinking the chart.

Straighten the center and strong unstable curves simultaneously to V=0 and U=0, with U positive outward. This C4 change of coordinates is a local diffeomorphism because the curves are transverse. Invariance, division by the vanishing coordinates and(3) give

    U'=g(U)+UV c(U,V),  V'=V d(U,V),
    d>2, |c|<=C,  g(U)=0 for U<=0, g(U)>0 for U>0.  (4)

For the first equation, subtract its value g(U) on V=0. The remainder vanishes on V=0 and also on U=0, so two Hadamard divisions give UV c. C4 regularity is more than sufficient for bounded c and locally Lipschitz coefficients. The coordinate orientation can be chosen so the zero subarc is exactly {V=0,U<=0} locally.

As long as a backward orbit stays in a rectangle |U|,|V|<r,

    |V(t)|<=|V(0)|exp(2t) for t<=0.

Define

    w(t)=U(t) exp[-int_0^t V(s)c(U(s),V(s))ds].       (5)

Signs of U cannot cross0. When U<0, w is a nonzero constant. When U>0, w'>0 in forward time, so w decreases backward and is bounded below by0. Also

    int_{-infinity}^0 |Vc|dt<=C|V(0)|/2,
    |U(t)|<=|U(0)|exp(C|V(0)|/2).                    (6)

Choose |V(0)|<r/2 and |U(0)|<(r/2)exp(-Cr/2). These bounds prohibit a first backward exit from the rectangle. Standard continuation in a compact subrectangle makes all such backward orbits complete within the chart. The integral in(5) converges and its exponential has a positive finite limit.

For U<0 the limit of U is strictly negative and V->0. For U=0 both coordinates tend0. For U>0, w has a nonnegative limit and hence U has a nonnegative limit. If it were U_*>0, then U'->g(U_*)>0, contradicting convergence as t->-infinity. Thus U->0. Every initial point in a sufficiently small full neighborhood therefore has a backward limit on the local zero arc, with all intermediate points remaining in N. Taking r smaller ensures all these limiting points lie on the terminal subarc in(2).

These local estimates use only the outgoing geometry. They do not require a global flow, a scattering map, boundedness of all global trajectories, or the absence of other remote equilibria.

## 3. The two transports and analyticity

Assume(2), writing M=Theta(p). Along a backward orbit from the small neighborhood just constructed, the first transport in(1) and continuity at its limiting equilibrium imply Theta(X)=M. Thus Theta is identically M on a full neighborhood N1 of p. Its physical Cartesian derivative partial_x Theta is therefore zero there.

Shrink again to a full neighborhood N2 whose backward orbits remain in N1, using the same containment estimates. The second transport in(1) gives for tau>=0

    Omega(phi_{-tau}X)=exp(tau)Omega(X).

All these orbits remain in a compact chart, and Omega is bounded there. Hence Omega(X)=0 for every X in N2. This is a conclusion on an open two-sided neighborhood, not merely on the outgoing basin or its boundary.

For a C2 planar field, the identities for divergence and curl give

    Delta W1=partial_x(div W)-partial_y(curl W),
    Delta W2=partial_y(div W)+partial_x(curl W).

Since div W=4 and curl W=-Omega=0, both components are harmonic on N2 and thus real analytic there. Rotate the physical plane to the tangent-normal coordinates; rotations preserve analyticity. The normal derivative of W_z at p is4, so the analytic implicit-function theorem gives an analytic normal nullcline z=k_an(s) through p. Uniqueness makes it the original smooth k(s) on a smaller neighborhood. The function

    F_an(s)=W_s(s,k_an(s))

is real analytic and is zero for all small negative s because these points are equilibria. The identity theorem in one variable implies F_an(s)=0 for all small positive s as well. This contradicts the required strict positivity of f(s). Equivalently the equilibrium component continues through p, contrary to it being an outgoing endpoint. This proves the theorem.

## 4. Application and precise limitations

For a full smooth B2 profile at beta2,45 gives the arc through the marked center and53 supplies the local outgoing alternative and invariant-curve framework. The theorem applies at each outgoing endpoint, even when additional remote equilibria exist. It imposes no strict monotonicity or finite-order departure from the endpoint temperature. The restriction of Theta to the arc may still tend flatly to M without being constant on any terminal interval, and it may oscillate. No such behavior is excluded here.

The construction161 deliberately chooses F=M on a terminal arc segment. Its harmonic local outgoing side and nonanalytic strong unstable boundary are consistent with this theorem because its vorticity equation fails in every full endpoint neighborhood. This theorem therefore identifies one precise reason that161 cannot be repaired within the same plateau geometry. It does not show that an endpoint with nonconstant flat temperature cannot satisfy both PDEs locally, and does not decide the full beta2 or broad B2 problem.

Numerical controls, if supplied, test formulas only. The proof rests on the stated invariant-manifold theorem, elementary scalar estimates, the exact transports and harmonic analyticity. No finite set of samples can establish the plateau obstruction.

Written UTC 2026-10-21T11:51:07.732062+00:00, before controls and review.

## 5. Analyticity obstruction at either endpoint

Added UTC 2026-10-21T11:58:11.182087+00:00, as an explicit lemma for the lead draft. Assume only that W is smooth near p, divW=4, the connected equilibrium component gamma has p as an endpoint of a smooth nontrivial arc, and DW(p) has kernel tangent to the arc and normal eigenvalue4. Then W cannot be real analytic on any neighborhood of p. No outgoing hypothesis or transport equation is needed for this assertion.

Indeed in orthonormal tangent-normal coordinates the normal component has nonzero normal derivative4. If W were analytic, its normal zero set would be a regular analytic curve through p, by the analytic implicit-function theorem. Every equilibrium near p lies on this curve, and gamma contains one of its half-arcs. The tangential component restricted to the analytic curve is a real analytic function of its parameter and vanishes on this half-interval. It vanishes on the whole smaller interval. The analytic curve therefore consists of equilibria on both sides of p and belongs to the same connected component as gamma. This contradicts the hypothesis that p is an endpoint of that component.

In B2, U=W-2X, so U and W have the same local analyticity. If Omega vanishes identically near p, divU=0 and curlU=-Omega=0 make U harmonic by the two Cartesian identities in section3, and hence analytic, which has just been excluded. Thus Omega cannot vanish on a full neighborhood of either endpoint, even if it is incoming or the local reduced field has accumulating zeros beyond it. If such additional zeros instead continued the component through p, the assumed endpoint itself would already be absent.

This lemma supplies draft4.7(xii)(a). It does not assert analyticity across the nonanalytic strong-unstable boundary in161. Together with sections1-3 it supplies the draft's outgoing plateau obstruction.
