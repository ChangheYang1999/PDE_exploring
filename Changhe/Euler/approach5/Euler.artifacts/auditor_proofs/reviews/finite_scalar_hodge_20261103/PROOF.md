# A finite scalar jet excludes a flat field in the exact planar tail system

Status: independently proved at the precise planar and open-k-zero local-tail scopes below. All nine sections of LIT220 were read. This extends A1244-A1246 by retaining the bounded drift and using a Dirichlet stream potential. Read the explicit coordinate proof A1244 before this argument.

## 1. Planar statement and normalization

Let K be a smooth real symmetric uniformly positive definite2-by-2 matrix on a disk about0, b a smooth vector field, and F,S smooth real fields there. Fix0<eta<1 and assume everywhere

    S div F-eta F.grad S=0, curl(KF)=b.F,              (1.1)

where curl(G)=partial_1 G2-partial_2 G1. Suppose S has a first nonzero homogeneous Taylor polynomial H_l of integer degree l>=1 with

    adj K(0):D2 H_l=0.

If every derivative of F vanishes at0, then F vanishes on a neighborhood of0. No a priori weak equation through0, zero period, or finite weighted energy is assumed. They will be proved from the finite jet.

Set R(x,y)=(-y,x), A=adj K. A fixed invertible linear change normalizes the frozen elliptic form to a multiple of I and makes the transformed leading scalar harmonic. For example in the later divergence equation take x=A(0)^(1/2)z; the transformed matrix is det(A(0)^(1/2))I at0, and division by that constant gives I. The scalar's transformed Hessian has zero ordinary trace. The density transformation for F preserves its weighted divergence. All other coefficients remain smooth. Thus it suffices to carry out the proof with the scalar leading term ordinarily harmonic and A(0)=I after this normalization.

## 2. All nodal fluxes and the central period vanish

The finite harmonic leading term is r^l h(theta), where h is a nonzero sinusoid of frequency l. Its2l simple roots give exactly2l smooth nodal arcs in a sufficiently small punctured disk, by Taylor expansion and the angular implicit function theorem. On every compact punctured annulus, S has a simple transverse zero on each arc.

At each regular nodal point, the undivided equation(1.1) gives F.grad S=0. Smoothness therefore makes the normal component F.n=O(distance) on each compact annulus. The divided flux G=|S|^(-eta)F has separate normal limits zero like distance^(1-eta), and is locally integrable across every arc because eta<1. Flatness of F, together with S comparable to r^l h in nodal coordinates, makes G locally integrable at0 as well. For every N, its integral absolute circle flux is bounded by C_N r^(N+1-l eta). Choosing N large makes this tend to0.

Integrate div G=0 over annular sectors, first passing to their nodal boundaries and then to the inner circle. Both types of limiting flux vanish. Thus div G=0 in distributions on the entire disk. Since curl(RG)=div G, the distributional Poincare lemma gives u in W1,1_loc with grad u=RG. This elementary lemma follows by smoothing RG on smaller disks, integrating the curl-free smooth fields, and passing to a W1,1 limit after fixing the mean. Equivalently the vanishing disk curl and periods give a single-valued primitive. Hence

    grad u=R |S|^(-eta)F, F=-|S|^eta R grad u.        (2.1)

No point source or period has been discarded.

## 3. The potential has zero trace on every nodal arc

On a compact punctured annulus, (2.1) gives normal derivative O(distance^(-eta)) and tangential derivative O(distance^(1-eta)), because the latter is the divided normal component of F. The integrable normal derivative gives continuous matching traces from both sides, and the tangential estimate makes the trace constant along each arc.

To identify their constants at0, use polar coordinates straightening the arcs with bounded distortion. The oscillation along a radius-r section is bounded by

    C_N r^(N+1-l eta) integral |h(theta)|^(-eta) dtheta.

The angular integral is finite. Along any fixed direction away from the nodal rays, integration of the radial derivative gives a finite limit at0 and an arbitrarily high power bound after its subtraction. The displayed angular oscillation gives the same limit uniformly in all directions. Subtract it from u. Then u is uniformly flat in value at0, and every constant nodal trace is zero.

In each open sector u is smooth. On compact punctured annuli it has

    u=O(distance^(1-eta)), grad u=O(distance^(-eta)),
    tangential derivative along a nodal arc=O(distance^(1-eta)).

The weighted energy |S|^eta|grad u|^2=|S|^(-eta)|F|^2 is integrable across the arcs and at0. Derivative bounds near0 may lose fixed powers of r, but flatness supplies arbitrarily many powers and will remove each inner boundary below.

## 4. The elliptic equation, its drift, and nodal coordinates

The identities KR=R adj K and curl(RG)=div G transform the second equation of(1.1) into

    div(|S|^eta A grad u)+|S|^eta beta.grad u=0,
    A=adj K, beta=Rb.                               (4.1)

Indeed curl(KF)=-div(|S|^eta A grad u), while b.F=|S|^eta(Rb).grad u. This fixes the sign.

Apply the explicit A-normal nodal map of A1244. If gamma_j(r) is the outward arclength parametrization of a nodal arc, n_j=R gamma_j', and e_j its initial direction, that map is

    Phi(r e(theta))=r e(theta)+sum chi_j(theta)
      [gamma_j(r)-r e_j
       +r(theta-theta_j)(A(gamma_j(r))n_j(r)-R e_j)].

The cutoffs have disjoint supports and equal1 near each theta_j. Its proof gives Phi-id=O(r^2), D Phi-I=O(r), bounded D2 Phi, positive determinant, and S composed Phi=H_l g with g=1+O(r)>0 and bounded grad g. It is C1,1 at0 and smooth off0. On each ray Phi_r=gamma_j' and Phi_theta=r A n_j.

Writing again u for the pullback, let w=|H_l|^eta. Then

    div(w M grad u)+w beta1.grad u=0,                 (4.2)
    M=g^eta det(D Phi)(D Phi)^(-1)A(Phi)(D Phi)^(-T),
    beta1=g^eta det(D Phi)(D Phi)^(-1)beta(Phi).

M is symmetric elliptic, Lipschitz, I+O(r), and beta1 is bounded. If nu=x/r and tau=Rnu, then tau.Mnu=0 on every nodal ray. In old coordinates, the new angular gradient is proportional to n_j and the new radial gradient annihilates A n_j, which proves this exact orthogonality. Zero Dirichlet traces and all estimates from Section3 survive the change.

## 5. Poincare and the exact energy boundary identity

On each angular sector, u has zero endpoint values. Cauchy-Schwarz in u(theta)=integral u_theta yields

    integral_sector |h|^eta u^2
                 <=C integral_sector |h|^eta |u_theta|^2,

because the integral of |h|^(-eta) is finite. There are finitely many sectors. Integrating in r with the radial weight and using ellipticity gives

    integral_(B_r) w u^2<=C r^2 D(r),
    D(r)=integral_(B_r) w grad u.M grad u.

Let J(r)=integral_(B_r) w u beta1.grad u and I=D-J. Cauchy-Schwarz gives |J|<=CrD. On a sufficiently small disk, D/2<=I<=3D/2.

Multiplying(4.2) by u and integrating gives

    I(r)=integral_(partial B_r) w u F_n,
    F_n=nu.M grad u.                                (5.1)

For completeness, on a compact annulus the weighted conormal w M grad u is bounded at a nodal ray, while u tends to0 like distance^(1-eta). Thus each separate ray boundary term vanishes. The inner-circle term vanishes from flat F and flat u. This is a Dirichlet argument; it does not assert zero Neumann flux for u.

## 6. Surface and Rellich identities with the drift retained

Put mu=nu.Mnu, T=Mnu-mu nu, Z=Mx/mu. Then Z.nu=r, Z=x+O(r^2), DZ=I+O(r). The exact nodal orthogonality and Lipschitz control give |T|<=Cr times angular distance to a ray. Consequently

    div(wZ)=(2+l eta+O(r))w,
    |div_circle(wT)|<=Cw.

These are the same coefficient estimates as A1245, now with the positive exponent. Define

    H(r)=integral_(partial B_r) w mu u^2,
    B(r)=integral_(partial B_r) w F_n^2/mu.

Differentiating H and using(5.1), then integrating its tangential term by parts, gives

    H'=(1+l eta)H/r+2I+E_H, |E_H|<=CH.               (6.1)

For e=grad u.M grad u use the vector Q=w e Z-2w(Z.grad u)M grad u. Symmetry cancels its second-derivative terms. Its divergence is

    div(wZ)e+w(Z.grad M)_ij u_i u_j
      -2w M_ij u_j(partial_i Z_k)u_k
      -2(Z.grad u)div(w M grad u).

The last term is +2w(Z.grad u)beta1.grad u and is O(r)we. The whole expression is (l eta+O(r))we. On the outer circle Q.nu=rwe-2r w F_n^2/mu. Integrating therefore gives

    D'=(l eta/r)D+2B+E_D, |E_D|<=CD.                 (6.2)

All ray terms really vanish. On an annulus we=O(distance^(-eta)), Z.n=O(distance), and Z.grad u=O(distance^(1-eta)); the last assertion follows by tangency of Z plus the tangential derivative bound. The weighted conormal is bounded. Both terms of Q thus have vanishing ray flux. In(6.1) the endpoint term wT u^2 also vanishes. After these limits, the center limits vanish by the flatness estimates in Sections2-3. No central Muckenhoupt-weight condition or bare reciprocal-weight integrability is used.

Finally J' is its surface integral, so ellipticity and bounded beta1 give

    |J'|<=C sqrt(H D').                              (6.3)

D' here is the nonnegative surface energy itself; no separate derivative estimate has been assumed.

## 7. The modified frequency cannot diverge towards the center

If H(r)=0 at one sufficiently small radius, (5.1) gives I=0 and then D=0. The zero Dirichlet traces make u=0 on the sectors in that disk, and F=0. Otherwise H>0 on every small radius. Set

    N=r I/H>=0, Q0=B/H-I^2/H^2>=0.

The second inequality is Cauchy-Schwarz in(5.1). Differentiating N and using(6.1)-(6.2) gives exactly

    N'=2r Q0+l eta J/H-rJ'/H+O(N).                  (7.1)

In particular the l eta term contains J=D-I, not D. Since |J|<=CrD and D is comparable to I, |J|/H<=CN. Equation(6.2) gives D'/H<=C N/r^2+2B/H for small r. Thus(6.3) yields

    r|J'|/H<=C sqrt(N)+Cr sqrt(Q0)+CN.

Here sqrt(B/H)<=sqrt(Q0)+I/H was used. Absorb Cr sqrt(Q0) into rQ0+Cr, and use sqrt(N)<=N+1. Then

    N'>=-C(N+1).

Hence exp(Cr)(N+1) is nondecreasing, which bounds N from above towards0 by any one outer value. Equation(6.1) then bounds H'/H above by L/r+C for finite L. Integration from r to a fixed outer radius gives H(r)>=c0 r^L. But uniform flatness of u gives H(r)<=C_N r^(1+l eta+2N) for every N, a contradiction. This proves the planar theorem.

## 8. The actual open-k-zero angular system

For the local-tail application, fix2/5<c<1/2 and finite omega. Set p=(1-c)/c, a=1-2c, b0=2(1-c), eta=a/b0, t0=omega/c and X=(cI-omega J)x. Assume V,P2 are smooth on a twisted conical neighborhood of x0!=0 and satisfy twisted homogeneity, div V=0, W=curl V, k=X.V=0 on that whole neighborhood, X cross W=aV, W.grad S=0, S=P2-|V|^2/2, and -Delta P2=tr((DV)^2).

Assume V is flat at x0, S(x0)=0, and S has a finite first nonzero Taylor order there. Then V vanishes on a smaller such neighborhood. These are local hypotheses; an actual global profile supplies them only where its tail is smooth and k vanishes on an open set.

On the unit sphere write zeta=Jw, R_w h=w cross h, v=w.V, Y=V-vw, rho=w.W/c, F=W-rho Aw and h=S|S2. The exact angular identities already audited in A1050-A1057 are

    F=-(a/c)R_w Y, div_S F=a rho,
    F.grad_S h=b0 rho h,
    div_S(D0 Y)+(2-p)t0 zeta.Y=0,
    D0=I+t0^2 zeta tensor zeta.

Thus h div_S F-eta F.grad_S h=0. Since Y=(c/a)R_w F and D0 R_w=R_w adj D0, the last identity is

    curl_S(KF)=b1.F,
    K=adj D0, b1=-(2-p)t0 R_w zeta.

Indeed div_S(R_w G)=-curl_S G and zeta.R_w F=-(R_w zeta).F. This checks the sign and the full drift coefficient (2-p)omega/c=(3c-1)omega/c^2. No rotation term is suppressed.

## 9. Density coordinates match the frozen pressure operator

In oriented sphere coordinates let G be the metric matrix and sqrt(g) its area density. Set Fhat=sqrt(g) times the contravariant components of F and Khat=G K/sqrt(g). Metric self-adjointness makes Khat a symmetric positive matrix. The sphere divergence and curl formulas turn the preceding first-order equations into(1.1) for Fhat, Khat and a smooth vector drift. Direct matrix calculation gives

    adj Khat=sqrt(g) D0 G^(-1).

Indeed det Khat=det K=det D0, and K^(-1)=D0/det D0. Thus the dual elliptic form in the planar theorem is exactly a positive density multiple of the principal form D0 for h.

Since V is flat, the pressure equation and S=P2-|V|^2/2 imply that Delta S is flat at x0. Twisted scalar homogeneity writes

    S(r exp(-t0 log(r)J)w)=r^(-2p)h(w).

At fixed physical angle, r partial_r becomes -2p+t0 zeta.grad_S. The angular principal part of the ordinary Laplacian is Delta_S+(t0 zeta.grad_S)^2, whose second-order form is D0. Its divergence representation differs only by smooth first-order terms. If h has first nonzero term H_l, every lower-order operator term has degree at least l-1; the degree l-2 equation is therefore

    D0(w0):covariant_D2 H_l=0.

For l=1 this condition is automatic. In local density coordinates it is adj Khat(w0):D2 H_l=0. Homogeneity identifies finite angular and ambient orders at the nonzero point. Fhat is flat because F is a smooth multiple of Y. All planar hypotheses now hold, so F=0, then Y=0, and k=0 gives v=t0 zeta.Y=0. Hence V=0 locally, as claimed.

## 10. Exact remaining scope

An infinitely flat supported velocity zero on a smooth open k-zero tail must also have S flat. The theorem does not exclude simultaneous flatness of S and V, nor does it make k zero on a neighborhood of a general supported zero. Smooth extension across a boundary of the open k-zero region is not inferred. There is one further actual-tail corollary using A1198: at a smooth infinitely flat supported velocity zero where the vortical set is dense in a neighborhood, a finite nonzero scalar jet forces k=0 on a neighborhood. Section9 then contradicts support. Thus S must be flat at every such densely vortical point as well. Conversely, a smooth infinitely flat supported point with a finite nonzero scalar jet must lie outside the open set Z and have open irrotational patches accumulating at it. This conclusion uses the exact density hypothesis of A1198, not merely membership in supp W. It is useful for abstract local tails and exterior-only smoothness with a merely C2 original core; global smooth zero-helicity original profiles are already covered by A309 under its hypotheses. Arbitrary helicity and the bare-decay conjecture remain open.

Dependencies: the fully reconstructed explicit nodal map A1244, the exact angular identities A1050-A1057, elementary distributional integration and linear algebra. No external weighted-continuation theorem, numerical calculation, new model client, formal build or prohibited execution is used. A focused comparison through the existing configured model agents remains requested, especially for Sections2-3,7 and9.
