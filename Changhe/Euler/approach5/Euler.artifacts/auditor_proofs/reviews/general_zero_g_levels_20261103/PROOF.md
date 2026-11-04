# Rate gap on regular vortical zero-g levels

Status: CONFIRMED, A536-A537. Independent reconstruction of coordinator CO27. The coordinator's configured model is the primary model; provider runtime is not independently attested. This is a necessary-conditions theorem, not nonexistence.

## 1. Statement and notation

Let 0<c<1/2 and omega be any finite real number. Put

    J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J,
    a=1-2c>0, kappa=1+c, B=Ax+U, W=curl U.

Let U in C2(R3;R3), P in C1(R3) solve the full profile equation

    div U=0,
    ((1-c)I+omega J)U+DU B+grad P=0,
    U.W=0 everywhere, U(x)=o(|x|) uniformly.                 (1)

Define H=P+|U|^2/2+(Ax).U, g=U.B and N=grad H. The exact Lamb identity makes N C1 and hence H C2. On the regular vortical set

    O={W!=0,N!=0},
    lambda=grad g.N/|N|^2,

A413 gives dg=lambda dH. Let Sigma be a connected component of O intersect {H=h} that contains a point with g=0. Then g=0 on Sigma and lambda is a constant lambda0 there.

Under(1), lambda0>=1. On Sigma define f=(B cross W).N/|N|^2. If lambda0=1, f is constant. If lambda0>1, f is a submersion of Sigma, Sigma*={f!=0} is open and dense in Sigma, and escaping forward B-orbits form an open dense subset of Sigma*.

Assume additionally

    2/5<c<1/2, U(x)->0 uniformly, DU=O(|x|^(1/2)).          (2)

Let V,Wstar be the actual scattering tails, Pinf the canonical pressure constant, and

    E(x)=-aV(x)+Ax cross Wstar(x),
    Z_E={w in S2:E(w)=0},
    Y(w)=Wstar(w)-(w.Wstar(w)/c)Aw.

Then

    lambda0 belongs to {1} union [2(1-c)/(1-2c),infinity). (3)

If lambda0>1, h=Pinf and Z_E contains a regular C1 arc tangent to a nonzero Y. Along that arc aV=Aw cross Wstar!=0. In particular, if no such arc exists, every zero-g component has lambda0=1. Totally disconnected Z_E or Y=0 on Z_E are sufficient conditions for this last conclusion, not consequences of(1)-(2).

If the connected component of the closed level {H=h} containing Sigma is compact, lambda0=1 already under(1). Under(2), the same conclusion holds whenever h!=Pinf.

## 2. Exact differential and surface identities

The confirmed identities are

    N=-aU+B cross W, BH=-ag, WH=Wg=0,
    [B,W]=-kappa W,
    beta=U.flat+dH/a, L_B beta=-a beta, L_W beta=0.        (4)

Both B and W have complete flows under(1), by A014 and A048. Write them Phi_t and Psi_s. Their commutation law is

    Psi_s Phi_t=Phi_t Psi_(exp(-kappa t)s).                (5)

The C1 function lambda on O satisfies d lambda wedge dH=0, obtained by differentiating dg=lambda dH. Hence g and lambda are locally constant on every regular H-level, and connectedness makes them constant on Sigma. Since g vanishes somewhere, its constant is zero.

The cross identity N cross U=gW follows from(4) and U.W=0. On Sigma this gives

    B cross W=fN, aU=(f-1)N.                              (6)

There is a useful precaution in differentiating(6): it is initially an identity only on a surface. Extend f to the surrounding regular set by the same quotient. The exact ambient identity is

    U=(f-1)N/a - g(N cross W)/|N|^2.                     (7)

Indeed N.W=0, and applying N cross to(7) gives N cross U=gW; the scalar product with N fixes the parallel coefficient. All quantities in(7) are C1 near Sigma. Taking its curl at g=0, using grad g=lambda0 N and curl N=0, gives

    W=(grad f cross N)/a+lambda0 W,
    (1-lambda0)W=(grad_Sigma f cross N)/a.                (8)

Thus no unproved normal derivative of a surface identity is used. If lambda0!=1, the right side cannot vanish, so f is a C1 submersion. If lambda0=1, grad_Sigma f=0 and connectedness makes f constant.

On Sigma, L_B dH=-a lambda0 dH. Combining this with beta=(f/a)dH and(4) gives

    Bf=mu f, Wf=0, mu=a(lambda0-1).                      (9)

These identities hold also at f=0. The covector transport is

    dH(Phi_t x) DPhi_t(x)=exp(-a lambda0 t)dH(x).          (10)

For completeness, a finite endpoint cannot cause a B-orbit in Sigma to lose W!=0 or N!=0: Cauchy transport preserves the former and(10) preserves the latter, since DPhi_t is invertible at finite times. The scalar g remains zero. Continuity then extends the orbit within the same connected level component. The identical argument for W uses WH=Wg=0 and Psi_s^*dH=dH. Thus Sigma and Sigma* are invariant under both complete flows.

A521, whose hypotheses are exactly(1), gives lambda0>=1. This proof does not use CO27 to reprove A521 or its equilibrium input A496.

## 3. The forward alternative for lambda0>1

Fix q in Sigma*, and put q_t=Phi_t q. Then f(q_t)=exp(mu t)f(q), with mu>0. Uniform sublinearity implies x.B>=c|x|^2/2 outside a ball. Consequently every forward orbit either remains bounded or eventually escapes to infinity; an unbounded orbit cannot repeatedly return from outside that ball.

Suppose this orbit is bounded. Its omega-limit K is nonempty, compact, connected and invariant under the full B-flow. Formula(6) gives

    |N(q_t)|=a|U(q_t)|/|exp(mu t)f(q)-1| ->0.

Since grad g=lambda0 N along the orbit, K lies in Crit(H) intersect Crit(g). On that critical set, the identity H-g=P-|U|^2/2 gives grad P=DU^T U. Hence along every orbit in K,

    BU=-(1-c)U-omega JU-DU^T U.                           (11)

This is a linear ODE in U along the orbit. If U vanished at a point of K, it would vanish on the complete orbit through that point, and B=Ax there. Boundedness of that full orbit then forces the point to be zero. A478 would give W=0 in a neighborhood of zero, because U(0)=0 and all its global helicity-free hypotheses hold. But q_t, whose vorticity never vanishes, accumulates there. This is impossible.

Thus U is nonzero on K, with a positive minimum of its norm by compactness. On K, B cross W=aU!=0. The confirmed critical-saturation theorem A511 applies: the complete W-saturation of K is unbounded. This conclusion does not say that K itself is unbounded or that every W-half-line through q escapes.

## 4. Dense escaping points

Escape is open: an escaping orbit crosses an outward sphere in finite time, and continuous dependence preserves such a crossing. Suppose some nonempty relatively open patch of Sigma* consists entirely of forward-bounded points. Take a closed coordinate disk inside it. For positive integers m, let

    E_m={x in the disk: |Phi_t x|<=m for every t>=0}.

Each E_m is closed, since it suffices to test rational nonnegative times, and their union is the disk. Baire's theorem supplies a relative open smaller patch P on which the same bound m holds for every forward time. Choose q in P and its omega-limit K.

For any z in K choose t_n->infinity with Phi_(t_n)q->z. Fix any finite real s. For all sufficiently large n, Psi_(exp(-kappa t_n)s)q lies in P. By(5),

    |Psi_s Phi_(t_n)q|
       =|Phi_(t_n) Psi_(exp(-kappa t_n)s)q|<=m.

Continuity at the fixed W-time s gives |Psi_s z|<=m. This holds for every z in K and every real s, contradicting Section3's unbounded W-saturation. Thus escaping points are dense in Sigma*. Equation(8) makes Sigma* itself dense in Sigma.

## 5. The target rate and the nonzero zero-tail arc

Under(2), the confirmed A498/A476/A477 chain supplies natural U and DU bounds. A516 and the scattering arguments A518 apply to every escaping orbit. Write

    Q_t=exp(omega tJ), v_t=exp(-tA)q_t,
    M_t=exp(-tA)DPhi_t(q), G(t)=exp((1-c)t)Q_t N(q_t).

They give v_t->v!=0, M_t->M with det M=1, and

    G(t)->E(v),
    G(t)-E(v)=O(exp(-t)).                                 (12)

For the second line one uses the target pressure bound in A516 and the exact covector ODE, as in A518; no equilibrium assumption enters that calculation.

Formula(6) gives the exact identity

    G(t)=a u_t(v_t)/(exp(mu t)f(q)-1),                     (13)

where u_t is the rescaled velocity. The numerator is bounded, so E(v)=0. Meanwhile the cross-product transport is

    exp((1-c)t)Q_t(B cross W)(q_t)
          =M_t^(-T)(B cross W)(q).

Its limit is Av cross Wstar(v), and the right side is nonzero because f(q)!=0, N(q)!=0 and M is invertible. The limiting Lamb identity therefore gives

    aV(v)=Av cross Wstar(v)!=0.                           (14)

Consequently the numerator in(13) has a nonzero limit. For sufficiently large t,

    C_q exp(-mu t)<=|G(t)|<=C exp(-t).

This forces mu>=1, exactly(3).

The level value follows because H(q_t)=h, whereas A516 implies H(x)->Pinf at infinity: its leading term (Ax).V has magnitude O(r^(1-p)) with p=(1-c)/c>1. Thus h=Pinf.

For the arc statement, a short W-segment through q lies in Sigma* and remains escaping. The C1 scattering map sends it to a Wstar-integral curve, by M W=Wstar(v). Along this curve(14) holds, so Wstar is not parallel to Av. Normalize by the linear A-flow to the unit sphere:

    pi(x)=exp(-sigma(x)A)x, sigma(x)=log|x|/c.

Its differential sends Wstar to a positive scalar multiple of Y. This follows from the twisted homogeneity of Wstar and D sigma(x)Wstar=(x.Wstar)/(c|x|^2). The scalar is nonzero. Equation(14) implies Y!=0. Thus the normalized curve is a regular C1 arc in Z_E tangent to Y, with the nonzero equality in the statement. The full scattering image being all punctured space does not make this arc a global E=0 statement.

## 6. Compact levels and carrier equilibria

If the closed connected H-level component containing Sigma is compact, every forward orbit in Sigma is bounded. The connected set K of Section3 and all its W-orbits remain in that same component, since WH=0. This contradicts unbounded saturation whenever lambda0>1. Hence lambda0=1. Under(2), h!=Pinf similarly excludes lambda0>1 by Section5.

At a vortical equilibrium p, write u=U(p)!=0 and F=DB(p), with F^T u=rho u. Then grad g(p)=rho u and N(p)=-au, so lambda0=-rho/a. Section5 recovers rho=-a or rho<=-2(1-c). The bound rho<=-a under(1) is a consistency check, since A521 itself already uses A496.

Now suppose p is an irrotational carrier equilibrium in the closure of {W!=0}, with u=U(p)!=0, F=DB(p), K=DW(p)!=0 and F^T u=rho u. A scalar component of W has nonzero differential near p; its zero set is a C1 hypersurface containing {W=0}. Hence the vortical set is dense in a sufficiently small box. The continuous identity dg wedge dH=0 extends throughout the box. Since N(p)=-au!=0, regular H coordinates give g=G(H) there, and G'(H(p))=-rho/a. The whole local level S={H=H(p)} has g=0 and constant lambda=-rho/a.

There are two possibilities. If S has vortical points arbitrarily close to p, Section5 applies to their zero-g components. Thus rho<=-a under(1), and under(2) rho=-a or rho<=-2(1-c). In the strict lower case H(p)=Pinf.

Otherwise W=0 on S near p, so K annihilates T_p S=u^perp. The helicity derivative gives K^T u=0. Write K=w u^T/|u|^2 with w perpendicular to u. The exact linearized bracket FK-KF=kappa K and F^T u=rho u imply

    Fw=(rho+kappa)w.                                      (15)

This is a restriction, not a construction of such a germ. In the first A469 spectral family {rho,rho+kappa,-a-2rho}, the needed eigenvalue is listed already. In its second family {rho,(-a-rho)/2,(1+4c-rho)/2}, it can be one of the two plane eigenvalues only at rho=-1 or rho=-a/3. These follow by solving the two linear equalities in(15). In the currently open second-family range rho<=-2a, the exceptional separating value is rho=-1. No conclusion is drawn when K=0.

## 7. Flat periodic neighborhoods and limitations

For a nonconstant periodic orbit Gamma in the closure of the vortical set with W=DW=0 and nonzero U, the confirmed periodic identities give g=0, N=-aU and lambda=-rho/a on Gamma, where rho is its covector rate. These identities can also be checked locally: continuity extends dg=lambda dH and d lambda wedge dH=0 to Gamma; periodicity of H and g'=-a lambda g forces g=0; then B lambda=0. Thus lambda is constant around the orbit.

The ambient quotient defining lambda is continuous on a tubular neighborhood. If rho>-a, its values near Gamma remain below1, so A521 forbids any regular vortical g=0 point there. Under(2), the same conclusion holds when -2(1-c)<rho<-a, since the nearby values lie strictly in the gap in(3). This excludes zero-g points in a neighborhood, not all vortical points, and not Gamma itself as a witness. Points with g!=0 remain outside the conclusion.

Every assertion retains global zero helicity. The rate improvement and tail statements retain the derivative screen or the equivalent confirmed natural bounds. Separating irrotational levels, K=0, strict lower rates, critical pressure-deficit zeros and general nonzero-g vortical points remain open. No unconditional C2 coverage or arbitrary-omega nonexistence follows.

## 8. Dependencies and verification

The new argument is the extension from an equilibrium level to an arbitrary regular zero-g component. Its confirmed inputs are A014,A048,A413,A478,A511,A521 for Section1, and A516-A518 with their natural-bound chain for Section5. The complete coordinator source Section26 was read and compared. Equation(7) supplies the ambient differentiation justification missing from a bare reference to a surface curl formula. No computation is required.
