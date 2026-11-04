# Local flat tail models, elliptic indices and the pressure-deficit distinction

Status: independent audit of CO49. The local construction and the index and deficit results below are confirmed. The inference that the deficit forces negative pressure is refuted as an inference. Pressure negativity near every actual T0 point remains open.

## 1. Exact classes and notation

Let 2/5<c<1/2, omega be any finite real number, and write

    Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax,
    L=(1-c)I+omega J, a=1-2c, b=2(1-c),
    p=(1-c)/c, d=p-1=a/c, q=b/a=2p/d.

For a tail velocity V and pressure P2 put W=curl V, k=X.V and S=P2-|V|^2/2. The derivative convention is (DV)_ij=partial_j V_i. Matrix norms in the pressure identities are Frobenius norms.

The local constructions in Sections5-7 assert only the following equations on a proper cone in D=R3 minus{0}:

    V(exp(tA)x)=exp(-tL)V(x),
    P2(exp(tA)x)=exp(-bt)P2(x),
    div V=0, V.W=0, k=0, W.grad S=0,
    -Delta P2=tr((DV)^2),
    grad k=X cross W-aV=0.                         (1)

They do not assert the full stationary Euler momentum equation, global canonical pressure, global extension, or realization as the tail of an original Euler profile.

For statements about actual tails, the exact additional hypotheses are U in C2(R3;R3), P in C1(R3), and, for one finite C,

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1).                     (2)

V and P2 must be the actual leading velocity and canonical pressure tails furnished by the established scattering construction. They satisfy V in C^(1,alpha)_loc(D) and P2 in C^(2,alpha)_loc(D) for every alpha in (0,1). Define

    T0={w in S2: V(w)=DV(w)=0, S(w)=0} intersect supp(W|S2),
    Z=int_D{k=0}, V0=1_Z V, E0=supp(V0|S2).

By A1050-A1057, V0 is C^(1,alpha), its support agrees with the support of curl V0, boundary E0 is contained in T0, and U!=0 implies T0!=empty. All omega-dependent constants are allowed to depend on the fixed omega.

## 2. Planar index theorem with a first-order term

Let O be a connected open subset of an oriented smooth surface, let 0<alpha<1, let beta in C^(1,alpha)(O) be strictly positive, and let D0 be a smooth symmetric positive definite tangent endomorphism. Suppose e in C^alpha and f in C^(2,alpha) solve

    div(beta D0 grad f)+e.grad f=0.                (3)

Then either grad f is identically zero on O, or all its zeros are isolated and have index -n for integers n>=1. The same index holds after multiplication by a continuous positive definite matrix field or by beta. Positive definiteness here includes symmetry; the conclusion also holds for a continuous matrix field whose symmetric part is positive definite, by the same homotopy.

In a smooth oriented chart, divide (3) by its positive scalar coefficient beta and the coordinate density. Its principal second-order matrix is smooth, symmetric and positive definite. All derivatives of beta enter only bounded first-order terms. Choose isothermal coordinates for the inverse of that smooth principal matrix. The principal part becomes a positive scalar multiple of the Euclidean Laplacian; coordinate second derivatives produce only first-order terms. Consequently, after division by that scalar, f solves

    Delta f+B1 f_x+B2 f_y=0                       (4)

on a smaller disk, with B1,B2 bounded. The coordinate maps can be chosen smooth here. One may first use the C^(1,alpha) isothermal coordinates furnished for a Holder metric by Chern's theorem, then bootstrap their weak metric-harmonic equations for this smooth metric. Thus no unproved extra regularity of beta is required for this reduction.

For transparency, the remaining similarity argument is proved in Section3, rather than being treated as an unexplained invocation of a generalized analytic-function theorem.

## 3. Similarity and negative index: a direct proof

Write z=x+iy and w=f_z=(f_x-i f_y)/2. Equation (4) gives

    partial_zbar w=A1 w+A2 conjugate(w),            (5)

with bounded complex coefficients. Define Q=A1+A2 conjugate(w)/w where w!=0 and Q=0 where w=0. Equation (5) implies partial_zbar w=Qw also at zeros of w. Extend Q by zero outside a compact disk contained in the chart, keeping a smaller disk unchanged.

The Cauchy transform

    h(z)=(1/pi) integral Q(zeta)/(z-zeta) dArea(zeta)

satisfies partial_zbar h=Q in distributions. It is continuous and locally Holder of every exponent less than one. Indeed, for a translation of size r, split the integral into the two disks of radius 2r around the evaluation points and their complement. The near part is O(r), and the far difference of kernels integrates to O(r log(1/r)). It also belongs to W^(1,2)_loc. This follows by differentiating in distributions: partial_zbar h=Q and partial_z h is the Fourier multiplier with symbol of modulus one applied to Q. The compactly supported bounded Q belongs to L2, so Plancherel gives the asserted derivative bound. These statements can equivalently be obtained by smooth approximation to Q.

The weak product and chain rules therefore apply to g=exp(-h)w, and give partial_zbar g=0. A continuous distributional solution of this equation is holomorphic: mollify on smaller disks, use the classical equation for each smooth mollification, and pass locally uniformly to the limit. Thus

    w=exp(h)g                                     (6)

locally, with g holomorphic. If w vanishes on an open subset of a disk, g vanishes there and hence on the disk. Overlapping disks and connectedness propagate this alternative to all of O. Otherwise the zeros of g, and hence w, are isolated. At a zero of order n,

    f_x+i f_y=2 exp(conjugate(h)) conjugate(g)

has winding number -n. The exponential of the single-valued continuous h has winding number zero. A coordinate gradient and the metric gradient differ by a positive definite matrix field. The convex homotopy between that field and the identity has no new zeros. This proves the assertion of Section2 and proves local unique continuation for a constant potential. An orientation-preserving change of coordinates preserves this vector-field index.

## 4. Integrating factor and its global limitation

Assume locally k=0 and S!=0, as well as the actual algebraic tail identities

    X cross W=aV, X.S=-bS, W.S=0.

The vector triple product gives

    a V cross grad S=-b S W.

For h=|S|^(1/q), this is W=grad(log h) cross V. Therefore curl(V/h)=0. On a simply connected small ball there is a potential psi with

    V=h grad psi, X.psi=0, div(h grad psi)=0.       (7)

Also a|V|<=|X||W| and |W|<=|grad(log h)||V|. In this open set V and W have the same zeros.

If k=0 and S!=0 on all of D, the closed field V/h has a global potential because R3 minus{0} is simply connected. Each twisted ray meets S2 once and X.psi=0, so the potential has the same range as its restriction to that compact sphere. Its maximum is attained at an interior point of D. The strong maximum principle, applied locally to the positive-coefficient equation in (7), makes psi constant on the connected D. Hence V=0. The coefficient need not be uniformly positive on all of D; local uniform ellipticity suffices. This argument does not apply across S=0.

A separate component fact has a precise scope. If one fixed connected vortical component with k!=0 carries S=D_C|k|^q, then a velocity zero in its closure has S=grad S=0. Here k and grad k are locally bounded, q>1, and the fixed number D_C is finite. At a supported flat zero with S!=0, any nearby vortical nonzero-k points instead satisfy

    |D_C(x)|>=C_alpha |x-x0|^(-q(1+alpha)).         (8)

This uses V=O(|x-x0|^(1+alpha)), k=X.V and a local positive lower bound on |S|. Such points, if present arbitrarily near x0, must belong to infinitely many different components. No uniform bound on the constants D_C is supplied.

## 5. Exact local analytic models for every omega

Fix sigma in {-1,1} and an integer m>=2. There is delta>0 and a real analytic pair (V,P2) on

    C_delta={z=x3>0: x1^2+x2^2<delta^2 z^2}

satisfying (1). V vanishes precisely on the positive axis in this cone, to transverse order m. All those zeros have DV=0 and belong to supp W. On the axis

    S(0,0,z)=P2(0,0,z)=sigma z^(-2p).              (9)

The index of the spherical tangent projection of V at e3 is -m.

Set beta0=omega/c and define twisted coordinates

    u+iv=z^(-1) exp(i beta0 log z)(x1+i x2).

They obey X.u=X.v=0. Seek F(u,v)>0 and Psi(u,v), and put

    f=z^(-d) F(u,v), psi=Psi(u,v),
    V=f grad psi, S=sigma f^q,
    P2=sigma f^q+f^2|grad psi|^2/2.                (10)

Then X.f=-af, X.psi=0 and aI+A^T=L imply the stated velocity homogeneity. S and |V|^2 both have scalar weight -b. The cone is invariant for every real flow time since the transverse rotation preserves the ratio sqrt(x1^2+x2^2)/z. Real powers and log z are analytic for z>0, so this defines a real analytic construction on the whole cone once F and Psi are analytic on a disk.

Before imposing any differential equation,

    W=grad f cross grad psi, V.W=0,
    W.grad S=0, k=0, X cross W=aV.                (11)

It remains to impose div V=0 and the pressure equation. On z=1 these are the two equations

    D=f Delta psi+grad f.grad psi=0,
    E=Delta(sigma f^q)
      -f grad psi.curl(grad f cross grad psi)
      +2|sym D(f grad psi)|^2=0.                  (12)

They have scalar homogeneity weights, so their vanishing on z=1 implies their vanishing throughout the cone. They are second-order equations in F,Psi: explicitly

    curl(grad f cross grad psi)
      =grad f Delta psi-grad psi Delta f
       +D2f grad psi-D2psi grad f.

There is no unaccounted third derivative.

## 6. Noncharacteristic calculation and analytic existence

Prescribe analytic data along v=0:

    F(u,0)=1, F_v(u,0)=0,
    Psi(u,0)=u^(m+1), Psi_v(u,0)=0.               (13)

At (u,v,z)=(0,0,1), all prescribed lower derivatives of Psi vanish since m>=2. Regard T=Psi_vv and R=F_vv as the two unknown second derivatives. Direct Cartesian differentiation of (10) gives

    grad f=-d e3, Delta f=R+d(d+1),
    grad psi=0, D2psi=T e2 tensor e2.

Thus at this jet,

    D=T,
    E=sigma q [R+d(d+1)+(q-1)d^2]+2T^2
     =sigma q [R+d(2p+1)]+2T^2.                  (14)

The identity qd=2p was used only in the last equality. The compatible jet is T=0, R=-d(2p+1), and the Jacobian of (D,E) in (T,R) is diag(1,sigma q), which is invertible for either sigma. The analytic implicit function theorem therefore gives a normal form

    (Psi_vv,F_vv)=Fcal(u,v,Psi,F,
                          Psi_u,F_u,Psi_v,F_v,
                          Psi_uu,F_uu,Psi_uv,F_uv)

near that jet. The right-hand side is analytic. The Cauchy-Kowalevski theorem for a system solved for its highest normal derivatives applies to the analytic data (13). Shrinking its neighborhood to a disk ensures F>0. This proves local analytic existence and then (10) defines the pair on C_delta. Neither the invertible Jacobian nor the construction requires omega to be small or nonzero.

For the pressure check, div V=0 yields Delta V=-curl W. The identity

    |DV|^2+tr((DV)^2)=2|sym DV|^2

then gives Delta P2+tr((DV)^2)=E. Hence (12) is exactly the claimed pressure Poisson equation once D=0. It is not the complete stationary momentum equation.

## 7. Velocity order, support and local index

For the constructed F, the first equation (12) is a linear second-order equation in Psi. At (u,v)=(0,0) its principal matrix is the identity, and it has no zeroth-order term. If a Taylor term of Psi of degree n<m+1 were its first nonzero term, that term would be a planar homogeneous harmonic polynomial with zero value and zero v derivative on v=0, by (13). The identity partial_vv=-partial_uu recursively determines such a polynomial from those two data, so it must vanish. At degree m+1 the same recursion gives

    Psi(u,v)=Re(u+iv)^(m+1)+O((u^2+v^2)^((m+2)/2)).  (15)

Its leading planar gradient has norm (m+1)(u^2+v^2)^(m/2). The analytic error in that gradient is O((u^2+v^2)^((m+1)/2)), so the only zero on a sufficiently small disk is its center. The map x->(u,v) has rank two, hence these are exactly the zeros of grad psi and of V. Formula (15) gives transverse order exactly m. Differentiating in z as well still gives DV=0 on the axis. Equation (11), with a>0, implies W!=0 wherever V!=0. Thus every axis point is in supp W. Equation (9) follows from F(0,0)=1 and V=0 there.

The leading planar gradient in (15), viewed as a complex vector, is (m+1) conjugate(u+iv)^m and has winding number -m. On the sphere near e3 the gradient of the restricted potential differs from this coordinate gradient by a positive definite matrix. The spherical tangent projection of V equals the positive scalar f times that sphere gradient. Its index is therefore -m, unchanged by the higher-order error.

These are first-derivative-flat zeros, not infinite-order vanishing. They lie where S!=0 and therefore are not T0 points. They provide no actual global profile counterexample. In particular the global obstruction of Section4 excludes an extension preserving k=0 and S!=0 everywhere, but does not exclude all other kinds of extension.

## 8. The deficit near actual T0 points

Under (2), if w0 belongs to T0, then for every real epsilon<1/4 every neighborhood of w0 contains a point with

    S<-epsilon |V|^2.                             (16)

Consequently w0 belongs to the closure of {S<0}.

Here is the exact local input A1006. If v is divergence-free and C^(1,alpha) near 0, pi solves -Delta pi=partial_i partial_j(v_i v_j), v(0)=curl v(0)=0, and s=pi-|v|^2/2 obeys

    s(x)-s(0)>=-epsilon |v(x)|^2

on a full ball, where 0<=epsilon<alpha/(2(1+alpha)), then v vanishes on a smaller ball. The input uses the full pressure Poisson equation and its spherical average, not a pointwise pressure sign. Its independent proof is in the dependency cited in Section12.

At w0, V=DV=0, so in particular V=W=0, and S(w0)=0. Since w0 is in supp W, V cannot vanish on any full neighborhood. Choose alpha<1 with epsilon<alpha/(2(1+alpha)), possible for each 0<=epsilon<1/4. The contrapositive of the local input proves (16). For negative epsilon use any larger nonnegative epsilon below 1/4. To obtain a sphere-neighborhood statement from a full ball, project nearby points to S2 along twisted rays. This projection is continuous near w0 and S and |V|^2 have the same positive scaling factor. The inequality is preserved. Choosing a positive epsilon gives S<0 at the resulting points. No conclusion at epsilon=1/4 is asserted.

## 9. Why this does not prove negative pressure

Since P2=S+|V|^2/2, (16) gives only

    P2<(1/2-epsilon)|V|^2.

For epsilon<1/4 the displayed right-hand side is positive at a nonzero velocity point. It does not imply P2<0. The following exact polynomial example shows that even a local steady-Euler solution with a supported flat zero can have the asserted strict deficit and nonnegative pressure everywhere.

On R3 write r2=x1^2+x2^2 and set

    v=r2(-x2,x1,0), pi=r2^3/6, s=pi-|v|^2/2=-r2^3/3.

Then div v=0, curl v=(0,0,4r2), v= Dv=0 on the entire x3 axis, and that axis lies in supp(curl v). Direct differentiation gives

    (v.grad)v=-r2^2(x1,x2,0),
    grad pi=r2^2(x1,x2,0).

Thus it is an exact smooth stationary Euler pair and satisfies the pressure Poisson equation. Off the axis s=-(1/3)|v|^2<-epsilon|v|^2 for every epsilon<1/4, while pi>=0 everywhere and pi=0 on the axis.

This refutes the proposed implication from the local deficit, even with the local Euler and support hypotheses. It is not a counterexample in class (2) and does not have the required negative twisted homogeneity. Therefore the assertion that P2 is negative arbitrarily near every actual T0 point remains OPEN. The final pressure-negativity sentence of CO49(c) must be removed or supported by a separate argument using additional actual-tail information. The deficit and closure conclusions are unaffected.

## 10. Index carried near T0 in the full-support branch

Under (2), suppose E0=S2. Then every sufficiently chosen neighborhood of the compact set T0 has total vector-field index at least 2 for

    Y(w)=V0(w)-(w.V0(w))w.

More precisely, for every open O containing T0, there is a compact region N contained in O, containing T0 in its interior, with smooth boundary on which Y is nonzero, and

    index(Y,N)>=2.                                (17)

If T0=S2, take N=S2 and use the global Euler index 2. The assertion does not assign an isolated index to every point of a possibly nonisolated T0.

To prove the other case, recall the classification already confirmed in A1054. All zeros of Y outside T0 are isolated of negative index: where S!=0 this follows from Sections2-4 applied to the local potential; where S=0 and W0!=0 it is the actual-profile saddle theorem A1020; where S=0, W0=0 and DV0!=0, the symmetric trace-free transverse linearization gives index -1. A remaining flat S=0 zero belongs to T0, because full support implies it lies in supp W0. The obliqueness X(w).w=c>0 ensures that a zero of Y is a zero of V0.

The isolated zeros outside T0 form a countable set, since S2 is second countable. Choose a smooth cutoff phi equal to 1 near T0 and supported in O. Choose a regular value t in (0,1) avoiding the values of phi at those countably many zeros. Then N={phi>=t} has smooth boundary, contains T0, and Y is nonzero on its boundary. The closed exterior S2 minus interior(N) has finitely many zeros, since it is compact and disjoint from T0, its boundary contains no zeros, and all its remaining zeros are isolated. Define index(Y,N) by any small interior perturbation with isolated zeros while preserving the nonvanishing boundary data; equivalently use the relative local degree. Additivity and the Poincare-Hopf theorem on S2 give

    index(Y,N)=2-sum_{zeros outside N} index(Y,zero)>=2.

This proves (17), including accumulation of exterior zeros at T0. It does not prove a positive isolated T0 index, nor exclude the entire set T0.

## 11. Audit conclusions and collaboration

CO49(a) is confirmed with the stated interpretation of positive definite and the elementary similarity proof above. CO49(b) is confirmed as a construction of local analytic tails satisfying exactly (1). CO49(c)'s deficit and closure statements are confirmed. Its pressure-negativity inference is refuted as an inference and the stronger actual-profile statement remains open. CO49(d)'s neighborhood-index conclusion is confirmed in the precise sense of (17), with the actual hypotheses (2) and E0=S2.

The coordinator's Section2 is a received focused comparison of all nine sections of LIT201. It agrees with A1050-A1057. The coordinator explicitly did not rederive one displayed drift coefficient; my earlier independent reconstruction did, and Section2 above only needs a bounded first-order coefficient. The coordinator is configured with the primary model; provider runtime is not independently attested. The nested local-construction source states that its attempted second-model consultation failed before invocation, so it is not counted as another model review. The pressure-sign counterargument is transmitted through this agent's notes for the existing coordinator to address.

No helicity removal, derivative-bound removal, endpoint theorem, T0 exclusion or nonexistence under the original bare-decay hypotheses follows from this audit. No numerical computation was needed.

## 12. Dependencies and verification

- CO49: in the team records, all five sections read and checked; exact snapshot in the team records.
- Local analytic source: in the team records, all three sections read and checked; exact snapshot in the team records.
- A1006: in the team records, Section3, for the pressure-deficit rigidity on a full ball.
- A1050-A1057: in the team records, for the actual-tail class, extension, index classification, and T0 necessity.
- A1018-A1021: in the team records, for the actual-ray lift, quotient spectrum and saddle proof.
- S. S. Chern, *An elementary proof of the existence of isothermal parameters on a surface*, Proceedings of the American Mathematical Society 6 (1955), 771-782, DOI 10.1090/S0002-9939-1955-0074856-1. The primary manuscript's printed pages772 and782 establish the Holder-metric existence and C^(1,alpha) coordinate regularity used before smooth elliptic bootstrapping. Retrieved primary PDF and text are in the team records, with retrieval provenance and hash. The proof above uses a smooth principal matrix after division by beta.
- Explicit standard dependencies: analytic implicit function theorem, Cauchy-Kowalevski for an analytic system solved for highest normal derivatives, local elliptic regularity, strong maximum principle, weak Sobolev product and chain rules, Plancherel, holomorphic identity theorem, Sard's theorem, and Poincare-Hopf with index additivity. Their exact uses and premises are identified above; no new formal verification is asserted.

All mathematical verification was by hand. Source hashes and the full post-read record accompany this proof.
