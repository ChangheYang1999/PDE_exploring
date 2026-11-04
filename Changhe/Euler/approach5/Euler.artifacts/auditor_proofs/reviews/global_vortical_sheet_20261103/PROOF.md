# The global regular sheet and its vortex fibers

Status: CONFIRMED at the exact scopes below as A770-A774, after full independent reconstruction and postread of B44 and the global-sheet part of coordinator Note52. A775-A776 record literal source corrections. The endpoint rho=-a is excluded explicitly. The argument uses global completeness of the vortex flow, already confirmed in A048.

## 1. Exact statement and inputs

Let 0<c<1/2, omega be finite and real, a=1-2c, kappa=1+c and A=cI-omega J, with J(y1,y2,y3)=(-y2,y1,0). Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+(DU)(Ay+U)+grad P=0,
    U.curl U=0, U(y)=o(|y|) uniformly at infinity.

Set B=Ay+U, W=curl U, g=U.B and H=P+|U|^2/2+(Ay).U. Momentum gives P,H,g in C2. The confirmed identities are

    grad H=B cross W-aU, BH=-ag, WH=Wg=0,
    [B,W]=-kappa W, div B=3c,
    dH wedge dg=0 on {W!=0}.                           (1)

The carrier flow Phi and vortex flow Gamma are complete; completeness of the latter is the substantive input A048, at exactly the uniform-sublinearity scope above. Their commutation law is

    Phi_t Gamma_s=Gamma_(e^(kappa t)s) Phi_t.            (2)

Let p be a vortical carrier equilibrium, and let rho<-a be its normal covector exponent. The confirmed equilibrium inputs A468,A478 give U(p)!=0 and

    spec DB(p)={rho,kappa,mu}, mu=-a-rho>0,
    DB(p)^T grad H(p)=rho grad H(p).

Let M be the connected component through p of

    {H=H(p), grad H!=0, W!=0}.

Then M is exactly W^u(p), the global two-dimensional unstable manifold of the carrier. In particular it is an embedded open disk. It carries the globally defined C2 function

    nu=i_(grad H/|grad H|^2)vol restricted to M,
    f=nu(B,W), psi=-f/mu,
    d psi=i_W nu, B psi=mu psi,
    aU=-(1+mu psi)grad H.                              (3)

The function psi is onto R, is a submersion, and each fiber is one complete vortex line. Its zero fiber is the vortex line L through p. Every nonzero fiber is closed in R3 and properly embedded, so both its vortex-time ends tend to spatial infinity. Exactly one fiber, Z={psi=-1/mu}, is the zero-velocity set on M. Its exact derivative and pressure formulas are in Section6.

If a half of L tends forward to an irrotational carrier equilibrium q, the endpoint identities of Section7 hold. In the target range 2/5<c<1/2, if DW(q)!=0, the local stream function at q has zero Hessian, as in Section8. No such connection is excluded for nonzero omega. No statement here includes rho=-a.

The origin input used for properness is A478: a carrier equilibrium in the vortical closure with zero velocity has an irrotational neighborhood. Equivalently one can use its two separately stated consequences that a vortical carrier equilibrium has nonzero velocity and that U(0)=W(0)=0 gives an irrotational neighborhood in this setting.

## 2. Global scalar and covector laws on M

Near any point of M, the rank identity and the submersion coordinate H give g=G(H) locally with G in C2. Hence g is constant on the connected level component M, and equals g(p)=0. The scalar l=G'(H) is also constant on each local level patch and therefore on M: it is a globally well-defined C1 function l=(grad g.grad H)/|grad H|^2 near M. At p its value is -rho/a. Thus

    g=0, dg=-(rho/a)dH on M,
    B H=0, W H=0,
    Phi_t^*dH=e^(rho t)dH on M.                        (4)

First these flow statements hold while trajectories remain in M. They extend across every finite endpoint: the covector formula preserves grad H!=0, the Cauchy law preserves W!=0, and continuity preserves the level and its connected component. The complete ambient flow therefore restricts to a complete flow on M. For W, the identity WH=0 gives Gamma_s^*dH=dH; it similarly preserves regularity, vorticity, and the component. Thus both complete flows preserve M.

In coordinates (h,z1,z2) with h=H-H(p), write vol=m dh dz1 dz2. On M, BH=0 and its normal derivative is rho by(4). Since the ambient divergence is 3c,

    L_B nu=(3c-rho)nu=(kappa+mu)nu.                    (5)

The form beta=i_W nu is closed, by WH=0 and div W=0 in the same coordinates. Cartan's formula and the commutator give

    L_B beta=i_[B,W]nu+i_W L_B nu=mu beta,
    L_B beta=d(beta(B))=-df.

It follows that df=-mu beta. Define psi=-f/mu globally, using mu>0. Then d psi=beta, so psi is C2 in surface coordinates and is a submersion because W never vanishes on M. Also beta(B)=-f gives B psi=mu psi. Since B,W are tangent to M, B cross W=f grad H. The first identity of(1) gives the last identity in(3). This constructs the global stream function without assuming simple connectivity or M=W^u(p).

## 3. Why the whole component is the unstable disk

Let S=W^u(p). Locally at p, the H-level is invariant and its tangent spectrum is {kappa,mu}, both positive. The local unstable disk therefore coincides with an open part of M. Complete carrier invariance makes S an open subset of M. Its points remain vortical and regular because they approach p backward and the finite-time laws preserve those properties.

The set S is also invariant under the complete W-flow. Indeed, for x in S and fixed s, (2) gives

    Phi_(-t) Gamma_s x=Gamma_(e^(-kappa t)s) Phi_(-t)x.

As t tends to infinity, Phi_(-t)x tends to p and the vortex time on the right tends to zero. Continuity of the local vortex flow near p implies that the right side tends to p. Hence Gamma_s x belongs to S. Both signs of s are allowed.

Let F be the relative boundary of S in M. It is invariant under both flows, since S is invariant and each flow is a homeomorphism of M. Suppose x in F has f(x)!=0. Then B,W are independent in the tangent plane. The map (t,s) -> Phi_t Gamma_s x is a local surface coordinate map by the inverse function theorem. Its image lies in F by invariance, so F would contain a relative neighborhood of x. But the boundary of an open set has empty interior: every neighborhood of a boundary point meets S, while F is disjoint from S. This is a contradiction. Consequently f=0 on F.

Now suppose x in F at all. Its complete vortex line stays in F. Since W(x)!=0 and f=0, write B(x)=b W(x). Pulling back B along the W-flow and using [W,B]=kappa W gives

    B(Gamma_s x)=(b+kappa s) W(Gamma_s x).              (6)

In particular q=Gamma_(-b/kappa)x belongs to F and is a vortical carrier equilibrium. Its normal rate is the same rho by(4), so A468 gives the tangent spectrum {kappa,mu}. Thus q is a source on M, and a small relative neighborhood lies in W^u(q). Since q is a boundary point, that neighborhood meets S. Any point in this intersection would tend backward both to p and to q, forcing p=q. But p is interior to S and cannot belong to F. This final contradiction proves F empty.

The nonempty set S is therefore both open and closed in connected M, so M=S. The global unstable-manifold theorem gives its intrinsic open-disk topology. Its realization here is embedded: each point has a neighborhood in the regular embedded H-level, and S equals that level component. No properness of the whole sheet is inferred.

This proof uses complete W-flow in(6). A local unstable disk alone, or an incomplete vortex flow, would not establish M=S.

## 4. Range, connected fibers and the zero fiber

At p, f=0 and d psi!=0. Thus psi takes both signs arbitrarily close to p. The complete carrier scaling psi(Phi_t x)=e^(mu t)psi(x), with mu>0, makes its range all of R.

If two points have the same psi value, choose one sufficiently large backward time so that both iterates lie in a fixed product submersion chart around p, with psi as one coordinate. This is possible because M=W^u(p). The new psi values are still equal. Choose both iterates in a smaller product rectangle, so the coordinate interval joining them inside their fiber stays in the chart. Map that interval forward to join the original points inside their original fiber. Every fiber is connected.

A regular fiber of the submersion is an embedded one-manifold, tangent to the nonzero W. Each connected fiber is thus a single W-orbit. Near p the zero fiber is the local vortex line through p. Any other point of that fiber flows backward into this neighborhood and hence into L. The Cauchy law preserves L under the B-flow, or equivalently use(2) and Phi_t p=p. Thus the global zero fiber is exactly L.

A fiber cannot be a circle. A circle in the open disk M bounds a compact disk inside M. A differentiable function constant on its boundary either is constant on the disk or has an interior extremum with different value; either case contradicts d psi!=0. This argument concerns the topology of M, not a compact filling in ambient three-space. It follows that every fiber is a copy of R, and completeness of the W-flow parametrizes it for all vortex times.

## 5. Bounded stream values cannot approach a critical H point

Suppose x_j in M tends to a finite point r and psi(x_j) stays bounded. If grad H(r)=0, (4) and continuity of the complete finite-time flow imply grad H(Phi_t r)=0 for every real t. The scaled psi values remain bounded for each fixed t. Passing to the limit in aU=-(1+mu psi)grad H gives U(Phi_t r)=0 for every t. Hence

    Phi_t r=e^(At)r,
    |Phi_t r|=e^(ct)|r|.

The backward limit is zero. Invariance and closedness of closure(M) imply 0 in closure(M), and continuity gives U(0)=0. The origin is therefore a zero-velocity carrier equilibrium in the vortical closure. The stated A478 input gives an irrotational neighborhood, contradicting M subset {W!=0} and 0 in its closure. Thus grad H(r)!=0.

For the version of A478 separated into two inputs, W(0)=0 can also be checked directly. If r=0, nonzero W(0) contradicts the nonzero-velocity condition at a vortical equilibrium. If r!=0, along e^(At)r the velocity vanishes, so DU B=0, while grad H=0 implies B cross W=0. Since B=Ae^(At)r!=0, DU W=0 there. The vorticity equation reduces to W'=(-I-omega J)W; its norm is e^(-t)|W(r)|. Boundedness near zero forces W(r)=0, then W vanishes on the orbit and at zero. The same origin-neighborhood contradiction follows.

For a fixed nonzero value r0, let x_j in {psi=r0} tend to r. The preceding lemma gives grad H(r)!=0. If W(r)=0, the continuous local formula f=(B cross W).grad H/|grad H|^2 would give f(r)=0, contradicting f(x_j)=-mu r0!=0. Hence r is in the regular vortical level. A connected component is relatively closed in that level, so r belongs to M and psi(r)=r0. The fiber is closed in R3.

A closed embedded copy of R in R3 is properly embedded: its intersection with a compact set is compact in the subspace topology, and its inverse parameter map is continuous. The complete W-flow on the nonzero field identifies R in vortex time homeomorphically with the fiber. Both time ends therefore leave every compact spatial set. This proves the claimed escape of every nonzero fiber. It gives no such conclusion for L, whose finite ambient endpoints may be irrotational points outside M.

## 6. The unique zero-velocity line and its exact matrix

By(3), U vanishes on M exactly when psi=-1/mu. This is one nonempty, complete, proper line Z by Sections4-5. Along it,

    DU W=0, DU^T W=0.

The first equation differentiates U=0 along the line; the second differentiates U.W=0 at a point where U=0. Using dg=-(rho/a)dH and U=0 gives DU^T B=-(rho/a)grad H. The identity DU v-DU^T v=W cross v and grad H=B cross W on Z then give

    DU B=(mu/a)grad H.                                 (7)

Put w=|W|, let e1=B^perp/|B^perp| for the projection onto W-perp, and let e2=grad H/|grad H|. These are orthogonal unit vectors since grad H=B cross W!=0. The zero row and column in the W direction, (7), its transpose version, and tr DU=0 yield

    DU restricted to W-perp=(w/a) [[0,-rho],[mu,0]],
    spec DU={0, +(w/a)sqrt(-rho mu), -(w/a)sqrt(-rho mu)},
    -Delta P=tr((DU)^2)=-2rho mu w^2/a^2>0.            (8)

This is a real diagonalizable saddle matrix, not a symmetric or rotation-free matrix. Its off-diagonal entries differ because -rho-mu=a>0. In particular its antisymmetric part encodes the nonzero vorticity. The eigenvalues in(8) are those of DU, not those of the symmetric strain tensor S=(DU+DU^T)/2. The latter has eigenvalues 0 and plus or minus w(-a-2rho)/(2a); these differ strictly from the nonzero eigenvalues in(8), since the squares differ by w^2/4.

## 7. Endpoint ordering and the exact improper strain integral

On M, U is normal and B tangent to the level. Thus B=(Ay)^tangent and U=-(Ay)^normal. Along each carrier orbit in M,

    |B|^2=(c/2)d|y|^2/dt-omega(Jy).dy/dt,
    P=H(p)+|U|^2/2.                                    (9)

Suppose a half of L connects p backward to an irrotational carrier equilibrium q forward. A540 and A658 give U(q)!=0 and the same rate rho. At both ends U=-Ay. If omega=0, integrate the first identity in(9); nonnegativity justifies monotone passage to both ends and proves

    integral_(-infinity)^infinity |B|^2 dt
      =(c/2)(|q|^2-|p|^2)>0,
    P(q)-P(p)=(c^2/2)(|q|^2-|p|^2)>0.                 (10)

For finite nonzero omega the finite-time identity remains exact, but no sign is assigned to the angular integral. No separate absolute convergence of that integral is asserted at a nonhyperbolic endpoint. The pressure difference is always (|U(q)|^2-|U(p)|^2)/2, simply from the common level.

On L the exact covector law A673 gives d log|U|/dt=rho-c-n.(sym DU)n. Since both endpoint velocities are nonzero, integrating this derivative on each tail proves convergence as an improper, not necessarily absolutely convergent, integral:

    log(|Aq|/|Ap|)
      =integral_(-infinity)^infinity (rho-c-n.(sym DU)n)dt. (11)

It supplies no lower bound on rho without further strain information.

## 8. The second stream jet at a nonflat endpoint

For this endpoint clause assume 2/5<c<1/2 and DW(q)!=0. The endpoint classification A658-A659 gives the nonflat first-family data, including hyperbolicity and rho<-kappa. The exact local endpoint result A543 then applies: the regular H-level is invariant near q because the vortical set is dense there; it has a C2 stream function psi_q with psi_q(q)=0, d psi_q(q)=0 and B psi_q=mu psi_q. Its tangent eigenvalues are lambda=rho+kappa<0 and eta=-a-2rho>0, with lambda+eta=mu+kappa. Choose linear eigenvector coordinates. Write Q=D2 psi_q(q), C=diag(lambda,eta). The second-order expansion uses only C2 psi_q and the first derivative of B:

    C^T Q+Q C=mu Q.

The coefficients of Q11,Q12,Q22 are respectively 2lambda-mu<0, lambda+eta-mu=kappa>0, and 2eta-mu>0 because eta=mu+kappa-lambda>mu. All vanishings force Q=0.

This is the Hessian of the local surface stream function, not an assertion that all ambient derivatives of W vanish. Noninteger orders above two remain consistent with a C2 surface scalar. Neither an exact local Euler germ nor a global profile is constructed by this jet calculation.

## 9. Scope and verification

The strict rho<-a premise is essential throughout the global stream construction and the source-on-the-level argument. The lower witness window rho<=-2a satisfies it, but the source's original broader rho<=-a wording does not. No endpoint rho=-a conclusion is certified by this proof.

The new global-sheet argument precedes, and therefore does not assume, connected fibers or disk topology. Properness uses A478 after this construction. The full sheet may still be nonproper, and a zero fiber may still have finite irrotational endpoints. No velocity derivative bound, tail expansion, pressure normalization or density premise was added.

The proof uses previously confirmed equilibrium, completeness and origin results, exact differential identities, elementary surface topology and the finite-dimensional unstable-manifold construction. No computation or formal build is used. A focused comparison of Section3 by the existing configured-model team is requested through working files; no new model client or agent is requested, and provider runtime is not independently attested.
