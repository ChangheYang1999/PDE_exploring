# Normalization and global geometry of an actual regular nodal surface

Status: A810-A818 CONFIRMED as necessary conditions under the exact global hypotheses below. Exclusion and existence of these surfaces remain OPEN, A819. This independent audit combines LIT181 and LIT182, keeping the nonparallel premise separate.

## 1. Hypotheses, notation and statements

Let 2/5<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c and p=(1-c)/c. Assume U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)   (1)

for a finite constant C. These are explicit global helicity and derivative premises. They have not been obtained from bare velocity decay. The equation makes P C2. Normalize by its actual constant limit Pinf and set

    B=Ax+U, Omega=curl U,
    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2, g=H-Q=U.B.

Write Phi_t for the complete B flow and Gamma_s for the complete Omega flow. Let K be the compact null set of forward-bounded B points, E=R3 minus K, D=R3 minus{0}, and Xi:E->D the actual C1 volume-preserving scattering diffeomorphism. Define K_Omega={y:Gamma_s y belongs to K for every s in R}, O=R3 minus K_Omega. Let V,P2 be the canonical actual tails, W=curl V, k(z)=(Az).V(z), S=P2-|V|^2/2. Section2 constructs a C1 function L on O extending k composed with Xi.

Let M be any nonempty connected component of

    {y in O:L(y)=0, dL(y)!=0, Omega(y)!=0}.             (2)

Then M is an embedded C2 surface invariant under both complete flows, meets E, and on M

    H=Q=g=0, dH=dL!=0, dQ=0, dg=dH.                   (3)

There are spatial constants b and f on this component such that

    b!=0, f=1+ab, U=b grad H, B cross Omega=f grad H.  (4)

For the oriented form nu(v,w)=grad H.(v cross w)/|grad H|^2 on its tangent plane,

    Gamma_s^*nu=nu, Phi_t^*nu=exp(kappa t)nu.          (5)

If f=0, B=tau Omega and tau(Gamma_s y)=tau(y)+kappa s. Each complete vortex line on M crosses one carrier equilibrium and cannot recur within M. If f!=0, M is closed and properly embedded in R3. In that case there are T>0 and a C1 diffeomorphism j:(R/TZ) times R -> M with

    B=partial_theta+kappa zeta partial_zeta,
    Omega=partial_zeta.                              (6)

The unique periodic carrier orbit is C0=j((R/TZ) times{0}), and K intersect M=C0. Every other point escapes forward, every backward B limit is exactly C0, and every complete Omega line is proper and escapes to spatial infinity in both infinite time directions. On each sign of zeta there are finite constants0<m_sign<=M_sign with

    m_sign |zeta|^(c/kappa)<=|Xi(j(theta,zeta))|
                           <=M_sign |zeta|^(c/kappa). (7)

Consequently the corresponding tail W arcs have one finite-time endpoint at the removed origin and one infinite-time endpoint at infinity. They need not have two finite core ends.

For any actual regular vortical tail node k(z)=0, dk(z)!=0,W(z)!=0, the inverse image lies on a component(2), and

    S(z)=0, V(z)=b grad k(z)!=0.                       (8)

The same b applies when the inverse images lie on the same original component. No assertion of global connectedness of the nodal set is made.

## 2. Scattering, C1 convergence and extension across excursions

Under(1), B has linear growth and Omega is bounded, so both C1 fields have complete flows. The scattering and tail theorems A209-A210,A538-A539 apply: the natural derivative bound has the required Dini integral. They give

    Xi Phi_t=exp(tA)Xi, Xi_*Omega=W,
    u_t(z)=exp((1-c)t)R_t U(exp(tA)z)->V(z),
    p_t(z)=exp(2(1-c)t)(P(exp(tA)z)-Pinf)->P2(z),
    R_t=exp(omega tJ),                               (9)

with the last two convergences in C1loc(D). Define z_t(y)=exp(-tA)Phi_t(y). Then z_t->Xi in C1loc(E). To recall the derivative check, its variational matrix solves a linear equation with coefficient R_t DU(Phi_t y)R_t^T. On compact subsets of E the trajectories eventually escape uniformly, and the natural derivative bound makes that coefficient integrable in time with uniformly small tails. The fundamental matrices converge uniformly; equivariance handles the finite initial interval. Thus no derivative of a merely pointwise limit is taken.

The exact identity

    h_t(z):=exp(at)H(exp(tA)z)
            =(Az).u_t(z)+exp(-t)(p_t(z)+|u_t(z)|^2/2)

proves h_t->k in C1loc(D). The images z_t of any compact subset of E eventually lie in a fixed compact annulus. The ordinary C1 chain rule therefore yields

    exp(at)H(Phi_t y)->k(Xi(y)) in C1loc(E).           (10)

Also H,Q are globally bounded and tend uniformly to zero at infinity. This follows from actual pressure decay, p>1 and the factors in their definitions.

The full equations and zero helicity give

    grad H=-aU+B cross Omega, BH=-ag,
    Omega.H=Omega.Q=0, [B,Omega]=-kappa Omega,
    Phi_t Gamma_s=Gamma_(exp(kappa t)s)Phi_t.          (11)

For two endpoints y,Gamma_s y in E, equation(11) makes their H values after Phi_t equal for every t. Equation(10) shows that k composed with Xi agrees at those endpoints, even if the connecting vortex segment meets K. By definition O is the union of Gamma translates of E. Define L(y) by moving y to any such endpoint in E and using k composed with Xi there. Endpoint agreement proves independence of the choice. A fixed admissible time works on a neighborhood, so L is C1. Its exact laws are

    L Gamma_s=L, L Phi_t=exp(-at)L.                   (12)

The second follows from(9), the homogeneity of k and(11). K_Omega is compact and invariant under both complete flows. For Phi invariance use(11) and the full Phi invariance of K. This also proves the asserted invariance of O.

## 3. Recurrence is used on open sets, not on the surface

A413 proves three-dimensional almost-everywhere topological recurrence of Gamma_1 and excludes every nonconstant periodic Gamma orbit. Its hypotheses are satisfied by(1). Briefly, the bracket and backward radial trapping bound images of bounded sets under Gamma_s by a ball of radius O((1+|s|)^((c+epsilon)/kappa)). Choose epsilon>0 with3(c+epsilon)<kappa. Disjoint translates of a positive-volume wandering set would grow linearly in count but fit in a ball of sublinear volume growth. This proves conservativity and recurrence in a countable basis. A periodic vortex orbit would shrink under backward carrier transport to arbitrarily short periods inside one compact set where DOmega is bounded, contradicting the elementary positive lower bound for periods of a C1 field there.

Two C1 first integrals F1,F2 on an open invariant set must therefore have dependent gradients wherever Omega!=0. Otherwise in a small flowbox their pair is a local diffeomorphism on the two-dimensional transversal. Choose a recurrent point in a smaller positive-volume box where this pair is injective on the transversal. Its sufficiently close integer-time returns have the identical transversal coordinate, since both first integrals are unchanged. If a return has local time offset delta_j->0 and global time n_j->infinity, Gamma_(n_j-delta_j) fixes the point. This is a forbidden nonzero period. This local argument requires no Sard theorem and no recurrence on a prescribed zero set.

Apply it on O to (H,L) and (Q,L). Near each point of(2), submersion coordinates give H=h(L) and Q=q(L), with C1 scalar functions. Both fields preserve the set(2): (12) and invertible flow differentials preserve nonzero dL, and the vorticity Cauchy formula preserves nonzero Omega. Each finite orbit segment stays in one connected component, so both full flows preserve M. Every M meets E because it is Gamma-invariant and O is the Gamma saturation of E. Connectedness makes H and Q single constants on M. A forward-escaping point in M intersect E, together with their decay at infinity, makes both constants zero.

## 4. Ambient covector normalization

In a local submersion chart write l=L. Equations(11)-(12) give

    q(l)=h(l)-l h'(l).                               (13)

Because h(0)=q(0)=0 and h is C1, q(l)/l=h(l)/l-h'(l)->0. The C1 function q therefore has q'(0)=0, proving dQ=0 on M.

Write dH=eta dL there. In each chart eta=h'(0), so it is constant along that local part of M. Overlapping charts agree on an interval of L values around0, and hence have the same derivative at0. Thus eta is one constant on connected M. Fix y in M intersect E and pull back the identity along Phi_t:

    exp(at)d(H composed with Phi_t)(y)=eta dL(y).

The C1 limit(10) makes the left side tend to dL(y). As dL(y)!=0, eta=1. This proves(3) as ambient covector identities. In particular no tangential derivative has been mistaken for an ambient one. Near M, H=h(L) with h'(0)=1; H=0 and L=0 define the same local regular surface. H C2 therefore improves M from C1 to C2.

## 5. The spatially constant normal multiplier

B and Omega are tangent to M, so their cross product is normal. Equation(11) then makes U normal as well. Define f by B cross Omega=f grad H. This is C1 on M, even at points where the fields are dependent, and the Lamb identity gives U=((f-1)/a)grad H.

The form nu in(5) is C1. Gamma preserves ambient volume and dH, so it preserves nu. On M, dH=dL and(12) give Phi_t^*dH=exp(-at)dH. Ambient volume scales by exp(3ct), hence its quotient by the transverse covector gives Phi_t^*nu=exp((3c+a)t)nu=exp(kappa t)nu. Explicitly choose a transverse vector v0 with dH(v0)=1 and tangent vectors v,w; their three-dimensional volume and the transformed dH(v0) give exactly this factor.

Let theta=i_Omega nu. The two-dimensional Cartan identities give

    d_M theta=0,
    L_B theta=i_[B,Omega]nu+i_Omega L_Bnu=0.

Thus d_M(theta(B))=0. Since theta(B)=nu(Omega,B)=-f, f is constant on the connected surface. Setting b=(f-1)/a proves(4)-(5) apart from b!=0. This proves a spatial constant, not just constancy on individual vortex lines.

If b=0, U vanishes identically on M. Its derivative along every tangent vortex curve gives DU Omega=0 there. Also B=Ax on M, so its complete orbit through y is exp(tA)y. Vorticity transport reduces on it to

    d_t Omega(Phi_t y)=-(I+omega J)Omega(Phi_t y),
    |Omega(Phi_t y)|=exp(-t)|Omega(y)|.

As t->-infinity the point exp(tA)y tends to0 but the last norm diverges, contradicting continuity of Omega near0. Hence b!=0.

If f=0, Omega never vanishes on M, so B=tau Omega with tau=(B.Omega)/|Omega|^2 in C1. The bracket in(11) gives Omega.tau=kappa. Completeness proves the affine time law and the unique carrier-equilibrium crossing. Strict affine change of the continuous tau rules out recurrence within M. This is compatible with ambient almost-everywhere recurrence because M has zero three-dimensional measure. If f!=0, the two fields are independent everywhere on M.

## 6. Actual tail values

For a regular vortical tail node z, equation(9) and dL=D Xi^T dk put y=Xi^(-1)z in a component M. Q(Phi_t y)=0, and the actual scalar limit exp(2(1-c)t)Q(Phi_t y)->S(Xi y) gives S(z)=0. Along this orbit U=b grad H. Multiplying by exp((1-c)t)R_t gives

    u_t(z_t(y))=b grad h_t(z_t(y)),

since a+c=1-c and D exp(tA)^T=exp(ct)R_t. Both sides converge on the compact annulus from Section2. Therefore V(z)=b grad k(z), nonzero because b and dk are nonzero. This proves(8).

## 7. No critical covector can occur in the ambient closure

For the remaining sections assume f!=0. Put Cbar=closure_R3 M. Every finite-time flow homeomorphism preserves this closed set. Continuity extends U=b grad H, B cross Omega=f grad H and dg=dH from M to Cbar. The last equality is ambient and continuous. Differentiating the global BH=-ag along a complete B orbit in Cbar gives

    Phi_t^*dH=exp(-at)dH.                             (14)

This is just uniqueness for a linear covector ODE along the orbit. No derivative of an identity restricted to a surface is taken.

Suppose grad H(y)=0 at a point of Cbar. Equation(14) makes grad H, and hence U, zero along its complete B orbit. That orbit is exp(tA)y and tends backward to0. Closedness and invariance imply0 in Cbar and U(0)=0. A478 applies: under local zero helicity, the Lamb and vorticity equations and rank on the open vortical set, a zero-velocity origin has an irrotational neighborhood. The global rank premise is supplied by A413, without a density assumption. All hypotheses hold here. This contradicts0 in the closure of M, whose every point is vortical. Consequently

    grad H!=0 on Cbar, and Cbar subset Reg={B cross Omega!=0}. (15)

Only backward convergence of this orbit was used, not boundedness of its full orbit. The local A478 proof and its original configured-model comparison were reread in full for this step.

## 8. Removing the joint core and proving properness

If Cbar intersect K_Omega were nonempty, it would be a compact set invariant under both complete flows and contained in Reg. Through any point it would contain a small plaque {Phi_t Gamma_s y:|s|,|t|<delta}, a genuine two-dimensional plaque because the two fields are independent.

A118 excludes such a plaque in any compact full-Phi-invariant subset of Reg. Its relevant argument is short: on a compact regular invariant set, the exact bracket and covector laws give a hyperbolic splitting for Phi, with expanding Omega direction, neutral B direction and one contracting transverse direction. Saturating a small span(B,Omega) plaque by local strong stable curves gives, by their continuous dependence and local uniqueness, a continuous injective parametrization of an open three-dimensional box. Invariance of domain makes its image open. Every point in that image tracks a forward-bounded orbit of the compact set and is forward bounded. This contradicts the nullity of K. Thus the compactness premise is applied to Cbar intersect K_Omega, not to M itself.

Therefore Cbar is disjoint from K_Omega and lies in O. Continuity of L and dL there gives L=0 and dL=dH throughout Cbar. Together with(15) this places Cbar in the regular nodal set(2). A connected component is closed relative to that set; since M is that component, Cbar=M. The surface is thus closed in R3. It was already an embedded surface, with its subspace topology, so intersection with an ambient compact set is compact in its manifold topology. This proves properness.

## 9. Affine leaf classification selects the annulus

The complete fields span TM. Their joint action orbits are open in M by the inverse function theorem and partition it. Connectedness therefore makes M one full affine-group orbit. A143 classifies it with its intrinsic leaf topology as a plane or an annulus. To recall the essential point, the simply connected affine group acts by (s,tau).y=Phi_s Gamma_tau y. Its stabilizer in Reg is closed and discrete, and has trivial intersection with the pure-vortex translation group because periodic vortex orbits are impossible. Projection to the carrier-time factor is injective, so the stabilizer is abelian. A nontrivial element can be conjugated by a vortex translation to a pure carrier-time element; its centralizer is exactly the carrier subgroup. The stabilizer is therefore trivial or cyclic generated by a positive carrier time T. The resulting coordinates are(6), with theta real in the plane case and modulo T in the annular case. Since this particular leaf is embedded, its intrinsic action topology and its manifold topology agree; the orbit map is a local diffeomorphism into that manifold.

Every negative-time B orbit has compact ambient closure by the outward radial drift outside a large ball. Properness makes this a compact subset of M in its intrinsic topology. In the plane coordinates theta(t)=theta(0)+t tends to negative infinity, impossible on a compact set. Hence the annular case is forced.

Equation(6) now gives theta(t)=theta0+t mod T and zeta(t)=exp(kappa t)zeta0. Every backward limit is exactly C0, and C0 is the sole periodic carrier orbit with least period T. If zeta0!=0, a bounded positive orbit would have compact closure in M, contradicting the unbounded zeta coordinate. An unbounded positive B orbit eventually crosses the large sphere on which x.B>=c|x|^2/2, then stays outside and tends to infinity. Thus K intersect M=C0, with genuine forward escape for all other points.

## 10. Proper vortex lines and exact tail time

In(6) each original vortex line has constant theta and zeta running at unit speed over R. It crosses C0 once. This is a proper line in the parameter cylinder, and the proper embedding of M makes it a proper line in R3. Its radius therefore tends to infinity at both infinite vortex-time ends. Both components zeta>0 and zeta<0 lie in E. Xi maps them to distinct connected components of the corresponding regular vortical tail nodal set: inverse images of connected regular tail pieces stay within the same original component M, and within one of these two signs. The converse follows from invertibility of the differential and vorticity pushforward.

For either sign epsilon, the compact circle j(theta,epsilon) lies in E. The continuous positive |Xi| there has a positive minimum and finite maximum. With t=log|zeta|/kappa, the exact coordinate flow gives

    j(theta,zeta)=Phi_t j(theta-t,epsilon).

Scattering equivariance and skewness of J now give(7). This is uniform in theta for each sign and valid for every nonzero zeta.

Finally Xi_*Omega=W means that Xi(j(theta0,zeta)) is parametrized by the actual W flow time zeta, up to an additive constant. Its maximal interval is(0,infinity) or(-infinity,0). At the finite end, (7) forces the point to the removed origin. At the infinite end it goes to infinity only at infinite vortex time. Every intermediate time is legitimate because the original line is complete and Xi is C1 on E. No carrier-time or angular reparametrization has replaced vortex time.

## 11. Scope and dependency audit

A209-A210 and A538-A539 supply the actual C1 limits under the explicit natural gradient bound. A413 supplies open-set recurrence and rank without density. The C1 two-integral argument is repeated here. A478 supplies separation from vorticity at a zero-velocity origin, with its exact local rank hypothesis. A118 supplies only the compact regular plaque restriction; no attractor existence theorem is needed. A143 supplies only intrinsic affine-leaf classification; properness is proved separately before it is used to infer ambient compactness. All these source arguments were reread at their applicable scopes.

Neither the parallel branch nor the periodic annulus is globally excluded for arbitrary nonzero omega. For omega=0, the previously proved periodic-carrier circulation identity excludes the nonconstant cycle, but does not resolve the parallel branch through this argument. No Euler profile realizing either branch has been constructed.

The regular surface and its tail cone have zero three-dimensional measure. Consequently three-dimensional almost-everywhere recurrence and finite core arrival cannot be restricted to them by assertion or by a coarea statement for almost every scalar level. The necessary annular geometry gives one finite and one infinite end, conditional on the branch existing. It is not an unconditional counterexample to a surface-return theorem, because existence of this branch remains open. No finite conditional surface area has been assumed or inferred.

The full LIT181 and LIT182 submissions are retained with hashes. This audit is the independent mathematical comparison; continuing collaboration uses the existing configured model agents, whose provider runtime is not independently attested. No new model client, computation or formal build was used.
