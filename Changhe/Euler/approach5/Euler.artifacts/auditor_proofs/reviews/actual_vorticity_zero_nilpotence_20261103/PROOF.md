# Nilpotent actual vorticity derivatives and flat zeros inside the open scalar-zero set

Status: independent reconstruction of the actual-profile argument in the coordinator's T0 exploratory proof, with a further matrix consequence. The finite-jet index argument in that source is treated separately. All statements retain the actual-profile hypotheses; local formal tails alone need not satisfy the spectral restriction.

## 1. Exact class, maps and conclusions

Fix 2/5<c<1/2 and any finite real omega. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU((cI-omega J)y+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p),
    |DU(y)|<=C(1+|y|)^(-p-1), p=(1-c)/c,
    J(y1,y2,y3)=(-y2,y1,0),

with one finite C. Put A=cI-omega J, B(y)=Ay+U(y), Omega=curl U, a=1-2c, b=2(1-c), kappa=1+c and q=b/a. Let V,P2 be the actual leading tails, W=curl V, X(x)=Ax, k=X.V, S=P2-|V|^2/2 and Z=int{k=0}, all on D=R3 minus{0}.

The confirmed scattering map Xi is a C1 diffeomorphism from the invariant escaping region O onto D. If Phi_t is the original B-flow, its exact identities are

    Xi(Phi_t y)=exp(tA)Xi(y),
    DXi(y) B(y)=A Xi(y),
    W(Xi(y))=DXi(y) Omega(y).                     (1)

The last formula and the C1 regularity of Omega imply differentiability of W at every zero, even though W is not generally C1 on a neighborhood.

The principal conclusions are:

1. At every x0 in D with W(x0)=0, all eigenvalues of DW(x0) are zero and DW(x0)^3=0.
2. If also x0 belongs to Z and V(x0)=0, then DV(x0)=0. Thus an actual nonflat velocity zero inside Z must be vortical.
3. At a flat velocity zero in Z, DW has the possible form X(x0) tensor ell with ell(X(x0))=0; it squares to zero, but need not have been proved zero.

The remaining sections also record precise T0 jets and limited mass estimates. No claim excludes all T0 points.

## 2. Differentiation at a vorticity zero needs only a C1 conjugacy

Suppose W(x0)=0, y0=Xi^(-1)(x0) and T=DXi(y0). Since T is invertible, (1) gives Omega(y0)=0. Taylor expansion of the C1 field Omega, continuity of DXi, and the C1 inverse map give, with h tending to zero,

    W(Xi(y0+h))
      =(T+o(1))(D Omega(y0)h+o(|h|))
      =T D Omega(y0)h+o(|h|).

Also Xi(y0+h)=x0+Th+o(|h|). Consequently W is differentiable at x0 and

    DW(x0)=T D Omega(y0) T^(-1).                  (2)

No second derivative of Xi has been introduced. The entire X-orbit of x0 consists of zeros of W by its exact homogeneity

    W(exp(tA)x)=exp(-t)exp(-omega tJ)W(x).        (3)

Its inverse image is the complete B-orbit through y0, is irrotational at every finite time and has B!=0 there, since DXi B=X!=0. None of this identifies a carrier equilibrium as a backward limit.

## 3. Compact backward original orbits force nilpotence

The original field U is globally bounded, say |U|<=M0. The C1 vector field B has linear growth, so its local flow extends for every positive and negative finite time. This follows directly from the integral equation and Gronwall bounds; no bounded global derivative is required for continuation. Local uniqueness holds because B is C1. The original escaping region is invariant under all finite time shifts.

Write y(t)=Phi_t y0 and x(t)=Xi(y(t))=exp(tA)x0. For t<=0, variation of constants gives

    y(t)=exp(tA)y0-integral_t^0 exp((t-s)A)U(y(s)) ds,
    |y(t)|<=exp(ct)|y0|+(M0/c)(1-exp(ct)).        (4)

The rotation has norm one. Thus the whole backward half-orbit lies in one fixed compact ball. Since U is C2, D Omega is continuous and bounded on that ball.

Differentiate (3) at the zero x0, using Section2 at both endpoints. If L0=DW(x0), then

    DW(x(t))=exp(-kappa t)
              exp(-omega tJ)L0 exp(omega tJ).   (5)

By (2) at y(t), this matrix is similar to D Omega(y(t)). Therefore every eigenvalue of exp(-kappa t)L0 has modulus bounded by one fixed bound for |D Omega(y(t))|, for all t<=0. If L0 had a nonzero complex eigenvalue lambda, its modulus exp(-kappa t)|lambda| would diverge as t tends to minus infinity, since kappa>0. This is impossible. All three eigenvalues are zero, and Cayley-Hamilton yields L0^3=0.

This argument bounds eigenvalues, not norms of the similarity matrices. DXi and its inverse may become unbounded along the backward orbit. Nilpotence does not imply L0=0. It is valid for each finite omega without a small-rotation assumption.

## 4. Nonflat irrotational velocity zeros inside Z are impossible

Suppose x0 belongs to Z, V(x0)=W(x0)=0. Put X0=X(x0), L0=DW(x0), M=DV(x0), and ell0=|X0|>0. The field V is C1. Curl V=0 at x0 makes M symmetric; div V=0 makes it trace free. Velocity homogeneity gives

    M X0=-((1-c)I+omega J)V(x0)=0.                (6)

Since k=0 on a whole neighborhood, the exact identity grad k=X cross W-aV reduces there to X cross W=aV. Differentiate it at x0. Section2 supplies the needed pointwise derivative of W, and W(x0)=0 removes the derivative of X. Hence

    X0 cross L0=aM.                              (7)

Differentiating (3) along the X-orbit of its zero gives L0 X0=0. Choose an oriented orthonormal frame with e3=X0/ell0. Equations (6)-(7) imply block forms

    M=[[M_E,0],[0,0]],
    L0=[[C,0],[ell,0]],
    C=-(a/ell0) J2 M_E,
    J2=[[0,-1],[1,0]],                           (8)

where M_E is a real symmetric trace-free 2 by 2 matrix and ell is a row. Write M_E=[[s,t],[t,-s]]. The matrix -J2 M_E=[[t,-s],[-s,-t]] is also symmetric trace free. Its eigenvalues are plus and minus sqrt(s^2+t^2). Thus the eigenvalues of L0 are

    0, +(a/ell0)sqrt(s^2+t^2),
       -(a/ell0)sqrt(s^2+t^2).

Section3 requires all of them to vanish. Since a>0, s=t=0, proving M=0. This consequence needs the open k=0 premise and the actual scattering map; it is not a local formal-tail theorem.

With M=0, (7) says that every column of L0 is parallel to X0. Therefore L0=X0 tensor ell1 for a covector ell1. The condition L0 X0=0 gives ell1(X0)=0, so L0^2=0. A nonzero rank-one nilpotent matrix is algebraically possible; no realized actual example is claimed and its exclusion remains open.

## 5. Pressure and vorticity jets at a general T0 point

Now suppose only that x0 is an actual T0 point: V(x0)=DV(x0)=S(x0)=0 and x0 belongs to supp W. It need not belong to Z. Write

    g=grad P2(x0), H=D2P2(x0), L0=DW(x0).

For every 0<alpha<1 the actual regularity gives V(x0+h)=O(|h|^(1+alpha)) and DV(x0+h)=O(|h|^alpha). Thus DV(x)^T V(x)=O(|h|^(1+2alpha))=o(|h|). It follows that grad S is differentiable at x0 with derivative H, even without a C2 neighborhood for S. The exact pressure equation and transport give

    P2(x0)=0, grad S(x0)=g,
    g.X0=0, tr H=0,
    H X0=-(bI+A^T)g.                             (9)

The last identity is obtained by differentiating X.grad S=-bS at the point, including the A^T g term. If g=0, H annihilates X0. Either H=0 or its eigenvalues are mu,-mu,0 with mu!=0; its quadratic form restricted to X0-perp is a saddle. If g!=0, S has a regular zero surface. These alternatives alone do not violate the local pressure-deficit lemma.

Also

    L0 X0=0, tr L0=0, L0^T g=0,
    D2k(x0)h=X0 cross L0 h.                      (10)

The first assertion follows from (3). Nilpotence gives the trace assertion independently. It also follows by integrating div W=0 over a small ball and using W(x0+h)=L0 h+o(|h|); the normalized flux is (4pi/3)tr L0. Such flux identities for the continuous distributionally divergence-free W follow by smooth convolution and uniform convergence on compact sets. Expanding W.grad S=0 to first order gives L0^Tg=0. Finally differentiate grad k=X cross W-aV using the zero values and DV(x0)=0.

In Z, (10) reduces to the rank-one form in Section4. Outside closure Z the stronger already confirmed A1005-A1008 theorem gives L0=0 and D Omega(y0)=0. Neither statement licenses vanishing of D Omega at every arbitrary T0 point.

## 6. Shrinking-neighborhood joint mass under the additional N premise

Assume N: k=0 implies W=0 on D, equivalently the open-zero velocity piece V0 vanishes. Let x0 in S2 be a supported flat velocity zero, and let K=k restricted to S2. For an angular neighborhood O define

    M_tau(O)=integral_(O intersect {|K|<tau, |S|<tau^q}) |W| dA.

Here N gives W(x0)=0 because k(x0)=X0.V(x0)=0. The stronger DW(x0)=0 follows by extending the proof of A1007 with N explicitly, as follows. If D Omega(y0)!=0, choose a component of the original C1 vorticity with nonzero differential. Its submersion box has two connected vortical half-boxes whose union is dense. Under Xi their images are connected, vortical, and by N have k!=0. The scalar relation gives S=D_+|k|^q on one image and S=D_-|k|^q on the other, with two finite constants. Continuity extends the bound |S|<=C|k|^q to the full image neighborhood. Since |k|<=C_X|V|, V(x0)=0, q>2 and W(x0)=0, the full-ball pressure lemma A1006 forces V=0 on a smaller ball. Its curl then vanishes there, contradicting D Omega(y0)!=0 through the invertible pushforward. Therefore D Omega(y0)=0, and Section2 gives DW(x0)=0.

This proves the needed extension at every V zero under N, including a possible boundary point of Z. It uses N on a whole neighborhood and does not assert the same at a general T0 point without N. The earlier theorem was stated outside closure Z because that region supplies N locally automatically.

Pointwise differentiability gives sup_(B_r(x0) intersect S2)|W|=o(r). Spherical area is O(r^2), so, uniformly in tau,

    M_tau(B_r(x0) intersect S2)=o(r^3).           (11)

Consequently M_tau(B_(C tau^(1/3))(x0) intersect S2)=o(tau) for every fixed finite C. This does not imply o(tau) on any fixed neighborhood and does not exclude concentration on a more slowly shrinking scale.

For a fixed O, dominated convergence gives M_tau(O)=o(1): the limiting set lies in {K=0}, where W=0 by N. No sharper fixed-neighborhood rate follows from this argument.

## 7. Exact componentwise mass and the needed uniform domination

The nonempty vortical set on the sphere has countably many open connected components C_j. Under N, each has k!=0 and the confirmed scalar relation

    S=D_j |K|^q.

Set a_j=min(1,|D_j|^(-1/q)), with a_j=1 if D_j=0, and

    mu_j(t)=integral_(O intersect C_j intersect {|K|<t}) |W| dA.

Since the complement of these components has W=0, the strict sublevel inequalities give the exact identity

    M_tau(O)=sum_j mu_j(a_j tau).                 (12)

Suppose, as extra conditions, mu_j(t)=o(t) for each j and there are one common t_*>0 and finite constants A_j>=0 with mu_j(t)<=A_j t for all 0<t<t_* and sum_j a_j A_j<infinity. Then each summand mu_j(a_j tau)/tau tends to zero and is bounded by a_j A_j. Dominated convergence for a countable series gives M_tau(O)=o(tau).

Neither individual o(t) nor the summable domination follows from (11). Applying a termwise limit to infinitely many components without this control would be invalid.

## 8. Scope, dependencies and verification

The main nilpotence result uses the established actual C1 scattering conjugacy, global C2 regularity, bounded U, linear-carrier growth and exact tail scaling. It does not need a uniform bound on DXi along backward time and does not assert that the backward limit is one equilibrium. The new exclusion in Section4 additionally needs k=0 on an open neighborhood. It leaves the rank-one nilpotent flat derivative and general T0 obstruction open.

Primary exploratory source: in the team records, all four sections read, including its pointwise jets, nilpotence proof, finite-order index argument and componentwise mass condition. The source was generated in the coordinator's existing the external referee (a second model) consultation; no independent successful model runtime is inferred from that fact. The coordinator agent is configured model, and this additional matrix consequence is transmitted for focused comparison through the shared agent notes. Provider runtime remains unattested.

Dependencies already audited here: in the team records for differentiability and the two-side proof extended under N in Section6; in the team records for the actual class and T0; the previously confirmed scattering construction identified by A516 and A530-A531. Formal verification is not claimed.
