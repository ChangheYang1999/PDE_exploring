# Paired and parallel regular vortical tail nodes

## 1. Exact hypotheses and the prior sheet theorem

Assume 2/5<c<1/2, omega in R, U in C2(R3;R3), P in C1(R3), and

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1),

where Jx=e3 cross x, A=cI-omega J, p=(1-c)/c, a=1-2c, kappa=1+c and C is finite. These global helicity and derivative hypotheses remain throughout. They are not consequences of bare decay in this proof.

Put B=Ax+U and Omega=curl U, with complete flows Phi,Gamma. Let K be the compact forward-bounded carrier core, E=R3 minus K, K_Omega the points whose complete Gamma line is contained in K, and O=R3 minus K_Omega. The actual scattering diffeomorphism Xi:E to R3 minus{0} is C1, preserves ambient volume, intertwines Phi with exp(tA), and pushes Omega to W=curl V. The actual tail V is C1. Set k(z)=(Az).V(z), and let L on O be the C1 extension of k composed with Xi.

The confirmed sheet theorem A810-A818 applies to every connected component M of {L=0,dL!=0,Omega!=0}. With the pressure limit Pinf fixed, put

    H=P-Pinf+|U|^2/2+(Ax).U, Q=P-Pinf-|U|^2/2, g=U.B.

M is an embedded regular H-level surface invariant under both complete flows. On M,

    H=Q=g=0, dH=dL, dQ=0,
    U=b grad H, B cross Omega=f grad H, f=1+ab,

where b is one spatially constant nonzero number. On Xi(M intersect E), V=b grad k. Here b is the sheet multiplier, distinct from any notation elsewhere for 1+c.

For f!=0, A815-A818 give a properly embedded annulus with global coordinates (theta,zeta) in (R/TZ) times R, T the least period of its unique carrier cycle, and

    B=partial_theta+kappa zeta partial_zeta, Omega=partial_zeta.

Its intersection with K is exactly zeta=0 and both open halves are in E. For f=0, A814 gives B=tau Omega and Omega.tau=kappa. These precise conclusions, not an assumed return property of a null surface, are the inputs below. The full independent proof in the team records and the endpoint proof cited in Section 7 were reread.

## 2. Exact parallel tail trajectories

Take f=0 and z0 in Xi(M intersect E). Then V=-grad k/a and Az cross W=0 on that tail surface. Since Az0 and W(z0) are nonzero, put tau0=(Az0).W(z0)/|W(z0)|^2. Homogeneity gives

    W(exp(tA)z0)=exp(-kappa t)exp(tA)W(z0),
    A exp(tA)z0=exp(kappa t)tau0 W(exp(tA)z0).

Consequently, with actual W time s,

    z(s)=exp((log(1+kappa s/tau0)/kappa)A)z0,
    |z(s)|=|z0|(1+kappa s/tau0)^(c/kappa),

on the entire interval 1+kappa s/tau0>0. Differentiation gives z'=W(z), with no extra time change. W need only be continuous here: any differentiable solution pulled back by the C1 Xi inverse solves the C1 Omega equation, so uniqueness follows from that equation. The displayed solution fills its maximal interval in punctured space. At one finite endpoint it reaches the removed origin; at the other, actual W time and radius are both unbounded. No passage through the origin is asserted.

## 3. Two angular curves from a nonparallel annulus

Let f!=0 and j be the annular parametrization in Section 1. Each complete B orbit in a fixed sign half meets zeta=epsilon, epsilon=+-1, once. For q(theta)=Xi(j(theta,epsilon)), define

    pi(z)=exp(-(log|z|/c)A)z, gamma_epsilon(theta)=pi(q(theta)).

Each scaling orbit meets S2 once. The theta direction on the original section is transverse to B since its zeta component there is kappa epsilon. Xi preserves this transversality, and the kernel of D pi is the A direction. Thus gamma_epsilon is an immersion. If two points have the same image, their inverse points are on the same B orbit, so the once-only crossing gives equality. Compactness then makes this a C1 embedded circle.

At every point, k=0, W!=0 and dk!=0 by the sheet theorem and the invertible differential of Xi. At k=0, dk!=0 implies grad_T(k|S2)!=0: a radial grad k would have nonzero pairing with Az unless it vanished, whereas Az.grad k=-ak=0. Hence each embedded circle is an open and closed subset of the local regular angular zero set, and is an entire connected component. The two circles are distinct since their scaling-invariant tail surfaces are disjoint. Conversely, continuation of any nonparallel regular vortical angular component lifts into the same connected original sheet and hence into one of these two circles.

The same b and least carrier period T belong to both circles. No endpoint at a critical or irrotational angular point is possible on a nonparallel component. This compactness statement concerns the nonparallel branch alone.

## 4. Conditional area, flux and collar periods

On M let N=grad H and define nu_M(v,w)=N.(v cross w)/|N|^2 for tangent vectors. On the tail sheet define nu_tail similarly with grad k. Since Xi preserves ambient volume and Xi^*dk=dH on M intersect E,

    Xi^*nu_tail=nu_M.

Indeed choose any transverse vector v0 with dH(v0)=1. Conditional area evaluated on two tangent vectors is ambient volume evaluated on v0 and those vectors. Its image has dk(DXi v0)=1, so ambient volume preservation proves the equality without an extra Jacobian factor.

On the annulus, nu_M(B,Omega)=f, hence

    j^*nu_M=f dtheta wedge dzeta, j^*(i_Omega nu_M)=-f dtheta.

The inverse image of either angular circle is obtained from zeta=epsilon by flowing for the periodic function t(theta)=-log|q(theta)|/c. Its resulting theta coordinate is theta+t(theta), of winding number one. It need not be a graph in that new coordinate. It follows that the integral of i_W nu_tail around the compatibly oriented angular circle equals -fT.

For a unit tangent v along the circle let n=grad_T(k|S2)/N_T, N_T=|grad_T(k|S2)|, and define epsilon0 by w cross v=epsilon0 n, w in S2. Since grad k.Aw=0,

    Aw cross v=epsilon0(c/N_T) grad k.

Writing W=alpha Aw+beta v and using W.w=c alpha gives

    (i_W nu_tail)(v)=epsilon0 (W.w)/N_T.

Thus both angular circles have the same nonzero absolute flux

    |integral_gamma (W.w)/|grad_T(k|S2)| dl|=|f|T.

The collar-period equality is the independently confirmed C43 result A846. It can also be checked directly. In a C1 collar with coordinate u=k|S2, write the pulled-back V.dx as F du+G dv. On u=0 its tangential coefficient G vanishes because V=b grad k. The integral of G/u around the periodic v coordinate is constant on each side since V.dx/k is closed there. Stokes on the strip from zero to u gives integral G equal to the integral of radial vorticity times the oriented spherical area. Dividing by u and using continuity gives the same signed flux limit from both sides. C1 approximation of the collar justifies Stokes at this regularity. The absolute period is therefore |f|T, on both sides of each circle. No argument here makes this nonzero number vanish.

## 5. The parallel product and possible equilibrium-curve boundary

Suppose f=0 and set tau=B.Omega/|Omega|2 on M. The affine law tau(Gamma_s y)=tau(y)+kappa s shows that every vortex line has exactly one carrier equilibrium. Let P0={B=0} intersect M and use zeta=tau/kappa. Then

    j:P0 times R -> M, j(q,zeta)=Gamma_zeta(q)

is a C1 diffeomorphism, with inverse

    y -> (Gamma_(-tau(y)/kappa)y, tau(y)/kappa).

Indeed tau has nonzero differential along Omega, so its zero set P0 is a C1 embedded one-dimensional manifold without boundary; the displayed inverse verifies all global identifications. Connectedness of M implies that of P0. It is a circle or a copy of R, and the product fields are Omega=partial_zeta, B=kappa zeta partial_zeta. At q in P0, Aq=-U(q), so |q|<=||U||infinity/c. Boundedness does not imply compactness.

Write Cbar for the ambient closure of M. Continuity gives U=-grad H/a, H=g=0 and dg=dH there. Cbar is invariant under both complete flows. Differentiating BH=-ag along its trajectories yields Phi_t^*dH=exp(-at)dH. If grad H vanished at one point of Cbar, U would vanish along its whole carrier orbit, which would be exp(tA)y and tend backward to the origin. This would give U(0)=0 with the origin in the closure of the everywhere-vortical M. The origin-separation theorem A478 gives an irrotational neighborhood of that origin and contradicts this. Thus grad H and U are nonzero on Cbar.

If q belongs to closure(P0) intersect O, then B(q)=0. Omega(q)=0 would make q a fixed vortex point lying in K and hence in K_Omega, impossible in O. Therefore Omega(q)!=0. Continuity of L on O gives L(q)=0 and dL(q)=dH(q)!=0. Connected components are closed relative to this regular nodal set, so q belongs to M and therefore P0. We have proved

    P0 is closed relative to O,
    closure(P0) minus P0 is contained in K_Omega,
    grad H and U are nonzero on closure(P0).

No independent-field plaque exists in this branch to exclude that possible boundary by the nonparallel proof.

## 6. Escape sets and all parallel angular components

Define P_epsilon={q in P0:Gamma_epsilon q belongs to E}, epsilon=+-1. These are open. At a carrier equilibrium,

    Phi_t Gamma_zeta q=Gamma_(exp(kappa t)zeta)q.

Hence every fixed-sign open vortex half-line is one complete carrier orbit. It lies in E precisely when q belongs to P_epsilon. Every q in P0 belongs to O, the union of Gamma translates of E, and q itself is in K. At least one nonzero Gamma parameter must therefore reach E, proving P_plus union P_minus=P0. If both escape sets are nonempty they overlap by connectedness of P0. Neither set is required to be all of P0.

For each connected component I of P_epsilon, the map

    q -> pi(Xi(Gamma_epsilon q))

is an injective C1 immersion into the regular vortical angular zero set. Transversality proves immersion as in Section 3; equality of projections and the unique equilibrium crossing prove injection. It is a local diffeomorphism of one-dimensional manifolds, hence a homeomorphism onto its image. To check that it fills the whole component, lift any connected continuation by Xi inverse. That lift remains in one regular original component M, its zeta coordinate cannot cross zero in E, and its q coordinate remains in one component of P_epsilon. The displayed projection therefore recovers all of it. This proves the claimed component correspondence without a properness assumption on M.

If such an angular component is compact, its inverse I is compact and is open in the connected one-dimensional manifold P0. It is also closed there, hence I=P0. Thus P0 is a circle and the entire corresponding sign escapes. This argument makes no assertion about the opposite sign beyond the escape cover. A parallel regular angular component may otherwise be a noncompact arc.

On an escaping half,

    |Xi(Gamma_zeta q)|=|zeta|^(c/kappa)|Xi(Gamma_epsilon q)|.

The parameter zeta is original vortex time. The tail trajectory reaches the origin at finite time as zeta tends to zero, and infinity at infinite time. Together with A818 for the annular branch and Section 2, every regular vortical tail nodal trajectory has one finite origin endpoint and one infinite spatial endpoint. This is compatible with almost-everywhere volume return because these nodal surfaces have zero three-dimensional measure.

## 7. A nonescaping parallel half

If q is not in P_epsilon, its entire sign half-line is in compact K. At q, dH=-aU, dg=dH and B=0 imply DB(q)^T U(q)=-aU(q). Thus its covector rate is exactly rho=-a. All hypotheses of the confirmed bounded-half theorem A658-A659 hold. The full twelve-section proof in the team records, including the separate rho=-a boundary extension, was reread.

That theorem gives convergence to one carrier equilibrium qstar, with

    B(qstar)=Omega(qstar)=0, D Omega(qstar)=0,
    grad H(qstar)=-aU(qstar)!=0,
    DB(qstar)^T U(qstar)=-aU(qstar).

It needs no finite-equilibrium or surface-isolation hypothesis. To specify the delicate flatness input: a hypothetical nonzero first vorticity jet at rho=-a has either two positive tangent carrier eigenvalues, excluded by the bounded-half index, or ambient spectrum {-a,0,kappa}. In the latter case the differentiated Cauchy bracket allows D Omega to map only the center eigenline to the kappa eigenline. A convergent surface trajectory lies on its center curve, while Omega=constant exp(-kappa t)B along it. Local Lipschitz continuity of B forces |Omega|/|x-qstar| to zero, killing this last possible first-jet entry. This is first-order flatness only. It excludes neither the endpoint nor the whole sheet.

## 8. Verification and open conclusions

LIT183 and LIT184 pass at the exact hypotheses above. Both full sources, the A810-A818 proof, C43 and the A658-A659 proof were read and compared. Their statements concern necessary geometry, not existence. The conditional area factor is f, with no missing c or a factor, and both time parametrizations are actual vortex time.

The nonparallel branch has a paired compact geometry; the parallel branch has a bounded equilibrium curve closed only relative to O and two open escape sets. The possibility of missing points in K_Omega and of one nonescaping sign remains open. No surfacewise recurrence has been inferred from volume recurrence. Critical nodes, open zero regions, nonzero helicity and removal of the derivative premise remain unresolved. No computation or formalization was required. Existing configured model agent comparison continues, with provider runtime unattested and no new client or agent.
