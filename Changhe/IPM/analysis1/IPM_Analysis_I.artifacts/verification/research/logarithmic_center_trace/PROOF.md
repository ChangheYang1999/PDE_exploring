# Center normalization is not a closed trace in the weak logarithmic topology

This proof is written before the new finite checks. Its verification status remains OPEN until independent checking, complete actual Claude Opus5.5 review and later own adjudication. It concerns the topology of a center coefficient. It is not a PDE exclusion or a statement about the full linearized graph norm.

## Statement

For x>0 put z=log x, beta=1/2-b, T_b h=x^beta h and

 ||h||Y_(b,s)=||T_b h||H^s(R²_(z,y)).

The Fourier definition has squared weight(1+xi²+eta²)^s. Work with real densities even in x and odd in y. Fix any real b<5/2 and any finite s>=0. Let A>0,D=2A+1 and let

 T=-A x partial_x+D y partial_y-1

have its maximal distributional domain inY. Its graph norm is ||h||Y+||Th||Y. The canonical parameters A=2/k-1,D=4/k-1 are a particular instance.

Let S consist of all smooth compact densities h=x²y a with a smooth even-x/even-y compact factor. Define

 J(h)=a(0,0)=partial_x² partial_y h(0,0)/2,
 Sigma(h)=partial_x partial_y psi[h](0,0),
 -Delta psi[h]=partial_x h, U[h]=(-psi_y,psi_x),

using the canonical full-plane inverse with no added harmonic strain. There exists a sequence h_delta inS,0<delta<=1, such that

 J(h_delta)=1, Sigma(h_delta)=0,
 U[h_delta] is smooth and compactly supported,
 ||h_delta||Y+||T h_delta||Y ->0 as delta decreases to0.  (1)

In particular J is neither continuous nor closable onS intersect ker(Sigma), when that domain is given either the Y topology or the frozen graph topology. No closed scalar-valued linear operator extending these J values can have a domain containing this test class in either ambient space. The zero-J subspace is not closed, even relative toS intersect ker(Sigma); it is dense in that test class for the inherited topology.

This shows that a Banach formulation using only either of these topologies does not supply a closed center-normalization constraint. An additional trace norm, stronger topology, or a smaller domain must be justified separately. No conclusion is drawn about a topology that already controls J, about the full-L graph norm, or about existence of an exact profile.

## Compact-potential construction

Choose an even smooth function chi onR, equal to1 on[-1,1] and0 outside[-2,2]. Such a cutoff is obtained from the smooth step built out of e^(-1/t) for t>0 and0 for t<=0. Set eta(y)=y chi(y), and define

 f_delta(x,y)=-x^4 chi(x/delta) eta(y)/12,
 h_delta=-Delta f_delta.                                (2)

These functions are smooth and compact, with even-x/odd-y parity. Near0, f_delta=-x^4 y/12, hence h_delta=x²y exactly. Therefore J(h_delta)=1.

The factor x²y persists globally. The x derivative term in(2) is x² times a smooth even function of x/delta, times eta(y). The y derivative term is x^4 chi(x/delta) eta''(y)/12. Since chi is even, eta is odd and eta''(y)/y extends smoothly and evenly across0. Indeed for a smooth odd function w, w(y)/y=integral_0^1 w'(ty)dt. This proves h_delta=x²y a_delta with a_delta smooth and even in both variables, and with compact support. Thus h_delta belongs toS.

The stream psi_delta=partial_x f_delta satisfies -Delta psi_delta=partial_x h_delta, has the required odd-odd parity, and is compact. Its velocity is

 U[h_delta]=(-partial_x partial_y f_delta, partial_x² f_delta). (3)

This is the canonical velocity: it obeys the Poisson equation and parity and vanishes at infinity, so the stipulated canonical uniqueness applies. Alternatively a compact smooth potential convolved against the full-plane fundamental solution reproduces f_delta up to a harmless constant, and differentiation gives(3). There is no harmonic xy term. Since f_delta=-x^4y/12 near0,

 Sigma(h_delta)=partial_x² partial_y f_delta(0,0)=0.       (4)

The source is not supported away from the origin, so no interior harmonic-moment expansion is asserted or needed.

## Exact transformed scaling

Put u=x/delta and define the two fixed smooth functions on u>0 by

 H2(u,y)=(partial_u²[u^4 chi(u)]/12) eta(y),
 H4(u,y)=(u^4 chi(u)/12) eta''(y).

Direct differentiation of(2) gives exactly

 h_delta(x,y)=delta² H2(x/delta,y)+delta^4 H4(x/delta,y). (5)

The subscript denotes the power of delta, not a Sobolev order. Explicitly

 H2=u²[chi+(2/3)u chi'+(1/12)u² chi'']eta,
 H4=(u^4 chi/12)eta''.

Set a=5/2-b>0, w=log u and F_j(w,y)=e^(beta w)H_j(e^w,y). The coordinate named a here is a constant exponent, distinct from the center factor a_delta. Equation(5) becomes

 T_b h_delta(z,y)
   =delta^a F2(z-log delta,y)+delta^(a+2) F4(z-log delta,y). (6)

Each F_j belongs toH^N(R²) for every fixed integer N. To prove this, note that u ranges over(0,2] on the support and y over[-2,2]. Near u=0, every mixed derivative partial_w^p partial_y^q F2 equals u^a times a bounded smooth function of u,y. For F4 the power is u^(a+2). Repeated partial_w=u partial_u preserves these powers. Their squared integrals with dwdy=dudy/u are finite because a>0. On u bounded away from0 all derivatives are smooth with compact support. The weak derivatives agree with these classical derivatives on the whole(w,y) plane, since w has no finite left boundary. The integer Fourier derivative characterization proves H^N membership. For any finite s>=0 choose N>=s and use (1+xi²+eta²)^s <= (1+xi²+eta²)^N.

Translation in w is unitary on every H^s, directly from its unimodular Fourier multiplier. Applying the triangle inequality to(6) therefore gives

 ||h_delta||Y <=delta^a(||F2||H^s+delta²||F4||H^s).       (7)

The constants are fixed after b,s and chi are fixed. Both powers tend to0.

## Frozen graph convergence

Conjugating T by the weight gives

 T_b T T_b^(-1)=Q=-A partial_z+D y partial_y+A beta-1.    (8)

This formula follows by differentiating x^(-beta)F(log x,y). It holds first on smooth functions and then distributionally. The operator Q commutes with translation in z. Moreover QF2 andQF4 belong toH^s: the preceding derivative estimates apply after one extra w or y derivative; multiplication by y is bounded on their common compact y support, and the product rule gives the same estimates for all derivatives.

Apply(8) to(6). It gives

 ||T h_delta||Y <=delta^a(||QF2||H^s+delta²||QF4||H^s).  (9)

Thus every h_delta is in the maximal domain of T, and(7),(9) prove(1). There is no high-order regularity assumption on the numerical background in this proof; T is the explicitly frozen model only.

## Failure of closability and of a closed normalization constraint

A linear functional is closable only if every domain sequence converging to0 whose images converge has image limit0. Here h_delta tends to0 in either ambient norm, but J(h_delta)=1. More explicitly any closed operator agreeing with J on these tests would contain the graph limit(0,1), impossible for a linear map because it must send0 to0. This proves the asserted nonclosability and nonexistence of such a closed extension.

Let h1 denote(2) at delta=1. Then h_delta-h1 lies inS intersect ker(Sigma) intersect ker(J), converges to-h1 in either topology, and J(-h1)=-1. Hence the zero-J subspace is not closed. More generally for any h inS intersect ker(Sigma), the functions h-J(h)h_delta have J=0 andSigma=0 and converge to h. This proves relative density in that test class, without asserting density of the strain-zero class in the entire Y space.

The affine class J=1 is likewise not closed because h_delta lies in it and tends to0. This is a topological warning about imposing a(0)=1 or a correction coefficient0. It does not make those pointwise constraints mathematically inconsistent; it shows only that these two specified norms do not close them.

## Verification scope

The construction, scaling and convergence hold for all real b<5/2 and all finite s>=0. No bound is claimed at b=5/2, where even the transformed leading term fails its zeroth axis integral. No full-L graph convergence is claimed. The actual strain rank-one bound from result204 does not control J, and these tests have Sigma=0 exactly.

Two separate finite algebra methods will check the Laplacian and compact-velocity formulas, the exact two-term scaling, conjugation(8), and the center coefficient and strain. Such checks do not prove all Sobolev orders or closability; those conclusions follow from the complete argument above. No interval enclosure, heavy computation, spectral result, inverse or PDE endpoint is supplied.
