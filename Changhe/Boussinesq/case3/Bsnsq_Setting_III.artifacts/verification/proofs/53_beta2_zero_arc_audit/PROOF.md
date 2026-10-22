# Beta-two zero-arc dynamics and an analytic-boundary exclusion

Date:2026-10-20. Status: CONFIRMED by independent verifier at 2026-10-20T18:01:37.464056+00:00.
No full smooth-class nonexistence conclusion.

## 1. Statement and previously checked inputs

Let (Theta,Omega,V) be a smooth full-plane B2 profile at beta=2, with
W=2X+V, V=U-U(0), div W=4, Omega=-curl W, and

    W.grad Theta=0, W.grad Omega+Omega=Theta_x.

Assume the given x-reflection parity, Theta(0,y)=0, Theta=x^2+O(r^3)
at0, and the prompt's canonical sublinear velocity. Packet39 places
this whole beta2 class in class A without an added vorticity bound.
Packets33,36,38 give, with smooth angular a,h and a not identically0,

    V=O(r^{1/2}), DV=O(r^{-1/2}), Theta=O(1),
    Omega=O(r^{-1/2}), grad Theta=O(r^{-1}),
    Theta(re)=h(e)+o(1), Omega(re)=r^{-1/2}a(e)+o(r^{-1/2}).

All derivatives have the corresponding scale bounds. Packet45 proves
that the zero component gamma through0 is a compact smooth arc with
paired endpoints p_+,p_-, one on each side of the invariant axis, and
with no other axis intersection. Its transverse eigenvalue is4. At
both endpoints Theta-L and Omega are flat, and DW=4 n tensor n.
Near an endpoint the normal nullcline has reduced scalar field f(s),
where s increases out of gamma and f is flat at0. The alternatives are
additional zeros accumulating, f>0 (outgoing), or f<0 (incoming).
The outgoing alternative has a nonempty open basin on which Theta=L,
Omega=0. These results are dependencies, not new assumptions.

Packet05 with33 supplies the C1 scattering diffeomorphism Phi on the
escape set E, with Phi(phi_tY)=e^{2t}Phi(Y). Its complement K consists
of the bounded forward orbits, is compact, and has zero area. The
zero set Z is compact and contained in K. All negative semiorbits
are bounded by W.radial>=r outside a fixed disk. The ambient flow
is complete because W has at most linear growth.

New conclusions below:
A. Compact alpha- and omega-limit sets contain only equilibria.
B. An incoming endpoint has an orbit in K whose backward limit set
   is disjoint from gamma. In particular Z=gamma forces both endpoints
   outgoing, K=gamma, and every negative orbit converges to one point.
C. In that restricted subclass the orbit directions have the two
   interior-fibre arcs and the two closed endpoint arcs described below.
D. At any outgoing endpoint, its strong unstable curve cannot be real
   analytic as an embedded curve on a neighborhood of that endpoint.

The only extra hypothesis in B-C is Z=gamma; D does not require it.
D is a restricted exclusion. A-C are necessary geometry only.

## 2. An elementary planar return-loop lemma

Let F be a complete C1 field on R2 with div F=c!=0 constant. It has
no invariant Jordan curve. Such a curve's bounded component would be
preserved by every flow map, whereas Liouville's formula multiplies
its finite positive area by e^{ct}.

We use the following planar transversal fact, with its proof included.
Along an injective orbit, successive crossings of a short transversal
all in the same direction are strictly monotone in the transverse
coordinate whenever they have an accumulation point in its interior.
Close the orbit between consecutive crossings with the intervening
transversal interval. The curve is simple: uniqueness makes the orbit
injective, and consecutiveness excludes another crossing of that interval.
The vector field crosses the transversal part consistently into the
bounded side, or consistently out of it, and cannot cross the orbit
part. After the second crossing the trajectory is therefore trapped
on the corresponding side until it leaves through the allowed part
of the transversal. The next crossing must lie strictly beyond the
second in the same transverse order. Otherwise it would cross the
previous orbit or cross the closing segment in the forbidden direction.
This Jordan separation argument repeats at each return. A repeated
point would instead make the orbit periodic, already excluded.

Suppose z is a regular point in an omega-limit set. Choose a C1 flow
box (u,v) with F=partial_u, centered at z, and transversal Sigma={u=0}.
Visits arbitrarily close to z give infinitely many Sigma crossings.
The transversal fact makes their coordinates v_n converge to0, after
restricting to a smaller box. Let D_n be the Jordan domain bounded by
the orbit from (0,v_n) to its next crossing (0,v_{n+1}) and the closing
Sigma interval. Its flux is entirely across that interval, so

    |c| area(D_n)<=C |v_{n+1}-v_n| ->0.               (1)

But fix a rectangle delta/4<u<delta/2, |v|<epsilon/2 in the outgoing
half of a smaller box. The ONLY part of the boundary of D_n in this
rectangle is the first outgoing horizontal orbit segment v=v_n.
Every other passage would extend backward inside the flow box to
Sigma and give an intermediate crossing, contrary to the choice of
consecutive crossings. The final incoming segment has u<0 and does
not enter this rectangle. Jordan separation puts precisely one side
of v=v_n inside D_n. One of the two rectangles from v_n to either
-epsilon/2 or+epsilon/2 is therefore contained in D_n. Since v_n->0,
its coordinate area has a fixed positive lower bound. The physical
area has the same property, because the chart Jacobian is bounded
below on the smaller closed box. This contradicts(1).

Thus no regular point belongs to a compact omega-limit set. Apply
the same argument to -F for alpha-limit sets. No finiteness, isolation
or local connectedness assumption on the equilibrium set was used.
The regular return-loop argument is the essential step; it is not
an appeal to the equilibrium-free Poincare-Bendixson theorem.

## 3. Interior convergence and incoming endpoint branches

Near a compact interior subarc of gamma, smooth tubular coordinates
(s,eta) give sdot=eta A(s,eta), etadot=eta B(s,eta), with B(s,0)=4.
Choose B>=3. Backward time contracts |eta| at least as e^{-3u}, and
the total tangential variation is at most C|eta_initial|. A sufficiently
small inner chart stays in a larger chart backward. Hence any bounded
negative orbit with an interior arc point in its alpha-limit converges
to a single interior equilibrium. This is also a direct proof of the
local fibre convergence needed here.

For an endpoint, use the standard local C2 center-manifold theorem
for a smooth planar field with eigenvalues0,4: there is a C2 locally invariant curve tangent to the zero eigenspace. In graph coordinates eta=z-H(s), invariance gives eta_dot=d(s,eta)eta with d(0,0)=4, hence d>2 nearby. Every nearby equilibrium therefore has eta=0; in particular the existing zero subarc belongs to this center curve. Only center-manifold existence is used; no small-complete-orbit theorem or uniqueness is needed. In coordinates(s,z) write W=(F,G), the normal nullcline
G(s,N(s))=0, and the chosen center manifold z=H(s). Let
f(s)=F(s,N(s)) and g(s)=F(s,H(s)). Invariance and mean values give

    A(s)(H-N)=Hprime(s)g(s),
    g(s)=f(s)+B(s)(H-N),
    g(s)[1-B(s)Hprime(s)/A(s)]=f(s).                 (2)

Here A(s)->4, Hprime(s)->0 and B is bounded. The bracket is positive,
so the center-manifold field has the same sign as f. If f<0 beyond
the endpoint, that exterior interval is one nonconstant orbit with
forward limit p_+. It cannot arrive in finite time by uniqueness;
a positive limiting s would contradict g<0. Its ambient complete
extension C is in K because its forward orbit is bounded.

The alpha-limit set of C is nonempty, compact and connected, and by
Section2 consists of equilibria. If it met gamma it would be contained
in gamma, since gamma is a connected component of Z. An interior
intersection implies a single limit by the previous chart argument;
without an interior intersection, connectedness makes it one endpoint.
In either case C has a single backward limit q in gamma. If q!=p_+,
the orbit closed by the zero subarc between q and p_+ is an invariant
Jordan curve. If q=p_+, the homoclinic orbit and that endpoint form
one themselves. Indeed an injective orbit with these endpoint limits
extends to an embedded arc, or to an embedded circle when the two
limits coincide; uniqueness excludes a finite meeting with gamma.
Section2 forbids these curves. Therefore alpha(C) is disjoint from gamma.

## 4. The restricted subclass Z=gamma

Accumulating additional zeros are excluded by the subclass hypothesis.
An incoming branch is excluded by Section3, because its nonempty
alpha-limit would be both contained in Z and disjoint from gamma.
Thus both endpoints are outgoing. Every negative orbit has a compact
connected alpha-limit in gamma by Section2. Section3 and connectedness
make it a singleton, including the endpoint cases.

Extend gamma a small amount at both ends by the C2 invariant center
curves. Normal tubular coordinates around this compact extended arc
have etadot=c(s,eta)eta, c>2, after shrinking the tube. This follows
from invariance at eta=0 and transverse derivative4 on gamma; continuity
handles the short extensions. On eta=0 the flow is zero on gamma and
points outward on the extensions. An orbit remaining in the tube for
all positive times must therefore be a point of gamma: any nonzero
normal distance grows until it leaves, and an exterior center orbit
moves outward until it leaves. A bounded positive orbit has omega-limit
in gamma by Section2, hence eventually stays in this tube and must be
an equilibrium. Therefore K=gamma.

For the endpoint classification one can avoid a strong-fibre foliation
theorem. Choose a local C4 center manifold and the unique smooth strong
unstable curve through the endpoint, supplied by the local invariant
manifold theorems for eigenvalues0,4. Straighten these transverse invariant
curves simultaneously to v=0 and u=0, choosing u positive outward.
The regularity suffices to divide the smooth field by each vanishing
coordinate. Their invariance yields

    udot=g(u)+uv c(u,v), vdot=v d(u,v), d>2,          (3)

where c is bounded, g=0 for u<=0 and g>0 for u>0. Indeed udot vanishes
on u=0, and subtracting udot(u,0)=g(u) leaves the product uv times a
bounded function. The sign of u is preserved. In backward time sigma,
|v|<=|v_initial|e^{-2sigma}, and

    (log|u|)prime=-g(u)/u-vc(u,v).

For u<0 the first term is0, so the finite integral of vc gives a strictly
negative limiting u. For u>0 set e(sigma)=-vc and
mu(sigma)=exp(-int_0^sigma e). This factor has a finite positive limit,
and (mu u)prime=-mu g(u)<=0. Also
u(sigma)<=u_initial exp(C|v_initial|/2), so an inner chart stays inside
a larger chart backward. The limit of u exists; a positive limit would
keep (mu u)prime bounded above by a negative constant, impossible.
Thus u tends to0. On u=0 the two nonstationary branches contract to0.
The local backward basin is exactly the exterior side u>0 with those
two boundary orbits. This uses no global restriction on Z.

For u<0 the same integrable logarithmic bound makes the limiting base
coordinate satisfy

    e^{-C|v_initial|/2}|u_initial|
       <=|u_limit|<=e^{C|v_initial|/2}|u_initial|.

Thus on a fixed small transverse section v=+v0 or-v0, convergence of
the interior base point to the endpoint is equivalent to u_initial->0.
This gives the limiting strong directions of the interior-fibre families
by continuity of Phi. Globalization by the complete flow preserves the
local classification. This elementary two-curve argument independently
checks and adopts the local repair supplied in the lead's auditP.

Each interior equilibrium has exactly two nonstationary fibres. They
depend continuously on the base point and smoothly on compact interior
subarcs. Each orbit maps under Phi to a positive radial ray, and two
different complete orbits have different rays. The two interior fibre
families consequently give open direction arcs J_+,J_-. Each endpoint
basin gives an open direction arc with two distinct boundary directions;
its closure is a nondegenerate closed arc I_+, respectively I_-. The
local tubular order and exhaustiveness of the backward limits give the
cyclic, disjoint partition

    S1=J_+ union I_+ union J_- union I_-.

Reflection exchanges I_+ and I_-. Equivariance and injectivity of Phi
make its vertical-axis preimage exactly the vertical axis. The right
half-plane minus the right half of gamma is connected; Phi1 is positive
there, first at large radius and hence everywhere by continuity. Thus
I_+ is compactly contained in the open right semicircle, I_- in the
left; pi/2 belongs to J_+ and3pi/2 to J_-.

Temperature equals the base equilibrium value along each fibre or
endpoint orbit. In the open endpoint basin it is identically L, so
its gradient is zero; the vorticity ODE and boundedness backward imply
Omega=0 there. Continuity extends this to the two boundary orbits.
Taking far-field limits yields h=L,a=0 on I_+ and I_-. All base values
occur along their fibres, so

    Theta(R2)=Theta(gamma)=h(S1).

This does not determine the sign or extremal character of L.

## 5. Analytic endpoint boundary: an independent reflection proof

At any outgoing endpoint, the same local strong-fibre argument makes
the open endpoint basin one side of its strong unstable curve Sigma.
On that side Omega=0, hence curl W=0 and div W=4. Suppose Sigma were
a real analytic embedded curve near the endpoint p. We give a direct
complex reflection proof that avoids an analytic Poisson Cauchy problem.

Use oriented Euclidean coordinates with p=0 and write z=x+iy. Let
w=W1-i W2. Direct differentiation gives

    partial_bar_z w=(div W+i(partial_y W1-partial_x W2))/2=2.

Consequently f(z)=w(z)-2 bar_z is holomorphic on the basin side, smooth
to Sigma. Let q(s) be a regular real analytic complex parametrization
of Sigma. Its holomorphic extension has nonzero derivative and is a
local conformal chart. Write qstar(z)=overline(q(bar_z)), a holomorphic
function. In the corresponding half-neighborhood define

    H(z)=[f(q(z))+2 qstar(z)] qprime(z).               (4)

This is holomorphic. On the real axis qstar(s)=overline(q(s)), so
H(s)=w(q(s))qprime(s). Because W is tangent to Sigma, this quantity
is real: if the complex physical vector is W1+iW2=k(s)qprime(s)
with k real, the product is k|qprime(s)|^2. Schwarz reflection therefore
extends H holomorphically through the real axis. One elementary
justification is to define its lower-half extension by conjugate
reflection, then use continuity and vanishing integrals across the
real line in Morera's theorem. This supplies a single holomorphic
extension, not an assumption of analytic boundary data for W.

Solve(4) for the holomorphic f and reconstruct w=f+2 bar_z. It gives a real analytic
extension Wtilde across Sigma. The extension agrees with W only on
the basin side. All jets agree at p, however, by smoothness and the
one-sided agreement of all derivatives.

Choose fixed tangent-normal coordinates(s,t) for gamma at p, with s
pointing outward. The analytic IFT applied to Wtilde_t (whose t
derivative is4) gives an analytic nullcline t=Ntilde(s). The reduced
analytic function Wtilde_s(s,Ntilde(s)) has the same Taylor series as
the smooth actual reduced field f of Section1. That series is zero,
since the actual field vanishes on the interior zero subarc. Thus the
analytic reduced function is identically zero. Its analytic zero arc
continues to s>0, which lies in the open basin side because Sigma is
transverse to the tangent axis. There Wtilde=W, so W would have zeros
inside the open basin of nonconstant orbits. This is impossible.

Therefore Sigma is not analytic near p. This proof needs no global
Z=gamma hypothesis. It excludes a straight boundary fibre, and more
generally an analytic germ of the entire strong unstable curve. It
does not exclude a curve which is smooth and nonanalytic at p, or
an orbit which is analytic only at its regular points away from p.

## 6. Audit scope and external dependencies

The planar return-loop argument, backward trapping, sign comparison,
Jordan exclusions and complex reflection are written out above. The
local C4 center manifold and the unique local strong unstable curve are the
standard invariant-manifold inputs, with the required spectral gap
explicitly checked. Their existence does not give analytic regularity.
No flat-function unique-continuation principle has been used.

The lead source astra/beta2d/PROOF.md D1-D4 is independently confirmed
subject to the stated invariant-manifold inputs. The new complex
argument independently verifies its analytic-boundary conclusion and
avoids its Cauchy-Kovalevskaya construction. Remaining scattering,
critical, inverse, resonance and axis formulas will be audited in a
separate packet. This remains a partial result, not an endpoint.

Actual Opus42 returned no written audit after213.909803330seconds
on2026-10-20T17:52:23Z (claude-opus-5-5, output budget exhausted).
It supplies no endorsement. The final endpoint argument above uses
only two local invariant curves and scalar estimates, replacing the
strong-foliation input in the version submitted to that unavailable review.

Actual claude-opus-5-5 review46 returned a usable audit in60.017312447seconds at18:02:37Z. It confirmed the two-curve basin calculation and holomorphic reflection argument, under the explicitly supplied smoothness and local-manifold inputs. Its review did not cover the global circle partition. The verifier checked every suggestion, disambiguated the repeated equation number, and retains its own proof of the remaining statements.

The chosen center graph contains nearby equilibria by the direct eta equation above. Exact finite-regularity source statements were actually downloaded and read at18:31Z: Wiggins Section10.1 Theorem5 and preceding local-stable statement, and Deng Lecture Note7 Theorems2-3. See verification/INVARIANT_MANIFOLD_SOURCES.md for files, hashes, exact application and the Deng TLS limitation. Earlier unsupported web-retrieval claims remain withdrawn. These are explicit standard theorem dependencies, now checked against source text.
