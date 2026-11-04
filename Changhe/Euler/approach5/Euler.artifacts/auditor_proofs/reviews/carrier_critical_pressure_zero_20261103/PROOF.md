# A positive-pressure zero cannot have pressure gradient parallel to the carrier

Independent audit of LIT292. The off-axis calculation below is new to this audit; the axial case is a dependency already independently proved. The general off-axis zero problem remains open.

## 1. Exact local statement and reductions

Fix 2/5<c<1/2 and omega!=0. Put Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), eta=a/b and kappa=(b+1)/b. Let p!=0 and let V,H be smooth on a neighborhood of p, with H>0. Define W=curl V, E=|V|^2, P2=H+E/2 and Z=DV V+grad P2. Assume

    div V=0, X.V=0, X.grad H=-bH,
    X cross W=aV, W.grad H=0,
    -Delta P2=tr((DV)^2).                                  (1)

Suppose V has exact finite vanishing order N>=2 at p. If p1 in C^1 satisfies

    X.grad p1=-(b+1)p1,
    -Delta p1=2tr(DV DZ) in distributions,
    W.grad(p1-2V.grad P2)=0,                                (2)

then grad H(p) is not parallel to X(p).

The complete axial proof, including arbitrary higher pressure jets, is in the team records. It proves the assertion when p is on the rotation axis. The stronger combined axial theorem, in the team records, excludes any such axial zero. Below p is off axis and we assume grad H(p) is parallel to X(p), to obtain a contradiction.

For completeness, the potential and scalar reductions used here follow from (1)-(2). The vector curl(H^(-eta)V) vanishes: X cross [W-(eta/H)grad H cross V]=0, and its bracketed vector is orthogonal to grad H, whose product with X is -bH!=0. Hence locally V=H^eta grad phi, with phi(p)=0 and X.grad phi=0. The exact order of phi is n=N+1>=3. A local ball is enough; no period or global potential is presumed.

Set tau=p1-2V.grad P2 and theta=tau/H^kappa. Poisson regularity makes p1 smooth locally. From (1), X.grad V=-(1-c)V-omega J V; consequently X.grad E=-bE and X.grad(V.grad P2)=-(b+1)V.grad P2. Thus X.grad theta=0. Also W.grad theta=0 by (1)-(2). The potential formula for W and X.grad H=-bH show grad phi cross grad theta=0. On a surface transverse to X this is the ordinary two-dimensional Jacobian equation.

## 2. Carrier frame and forced second pressure derivatives

Rescale V,H,P2,p1 by H(p)^(-1/2), H(p)^(-1), H(p)^(-1), H(p)^(-3/2). Each term in (1)-(2) has the appropriate common scaling, so assume H(p)=1. Translate p to the coordinate origin and choose an oriented orthonormal frame with e3=X(p)/q, q=|X(p)|>0. In this frame the rotation vector is (-v2,v1,r), and the carrier is

    X_T=(cx+ry,-rx+cy)-z(v1,v2),
    X_3=q+v1x+v2y+cz.                                    (3)

Write v=(v1,v2), J_T(x,y)=(-y,x). Since omega!=0, an off-axis p has v!=0. Otherwise the physical rotation vector and X(p) would be parallel, hence X(p) would lie on the original rotation axis. The transverse block of cI-omega J is invertible, forcing p itself onto that axis.

Our contrary assumption is grad_T H(p)=0. Homogeneity gives H_z=-b/q. The necessary Hessian condition independently proved in the team records (LIT286) is that

    B=3D^2H+(eta/H)grad H tensor grad H

is scalar on X(p)-perp. Since V=DV=0 at p, the Poisson equation gives Delta H(p)=0. Differentiating X.grad H=-bH once then yields

    H_zz=b(b+c)/q^2,
    D^2_T H=t I, t=-b(b+c)/(2q^2),
    H_Tz=bv/q^2.                                          (4)

Thus B_TT=beta I, beta=3t, B_Tz=3bv/q^2 and B_zz=[3b(b+c)+eta b^2]/q^2. No special cubic or quartic pressure values are imposed.

## 3. Cubic pressure and potential terms

Let T=c(x partial_x+y partial_y)-r(-y partial_x+x partial_y). For a scalar F with X.grad F=-dF, restriction to z=0 gives

    F_z=-(d+T)F/(q+v.x),
    F_zz=[v.grad_T F-(d+c+T)F_z]/(q+v.x).                   (5)

Both denominators stay nonzero on a sufficiently small neighborhood. Apply (5) to H and differentiate the second identity transversely at p. Using (4),

    q grad_T H_zz = t v-(b+2c)H_Tz-r J_T H_Tz-H_zz v,
    dvec:=grad_T H_zz
      =-b[(5b+7c)v+2r J_T v]/(2q^3).                       (6)

This checks the sign of the tilt and the transverse rotation term directly from the carrier.

Because V vanishes to order n-1, the Poisson equation and P2=H+E/2 give Delta H=O(|(x,y,z)|^(2n-4)). Hence its value and first derivatives vanish at p. Set w=x+iy and rho^2=x^2+y^2. The surface pressure and potential expansions are

    h=H(x,y,0)=1+t rho^2/2+h3+O(rho^4),
    f=phi(x,y,0)=P+f_(n+1)+O(rho^(n+2)),
    P=Re(Kw^n)/n, K!=0.

The leading potential is independent of z by X.grad phi=0 and is harmonic by incompressibility. Its complex phase K is arbitrary. Since Delta_T h3=-dvec.x,

    h3=-rho^2(dvec.x)/8+h3h,                               (7)

where h3h is any harmonic cubic.

Using (5) with d=0,

    [phi_z]_n=-TP/q,
    [phi_zz]_(n-1)=v.grad_T P/q.

In div(H^eta grad phi)=0, the pressure-gradient contribution has order n, because grad_T H vanishes at p and phi_z starts in degree n. Therefore the degree n-1 equation is

    Delta_T f_(n+1)=-v.grad_T P/q.                         (8)

Its harmonic part remains free. The vertical-vertical Hessian contribution in (8) is essential and is absent in the axial specialization.

## 4. The scalar side has no tested term

On z=0 the smooth theta satisfies Jac(f,theta)=0. Subtract its constant term. If its first nonzero homogeneous term has degree j, its Jacobian with P vanishes. On each sector between the regular nodal rays of P this homogeneous polynomial is a constant multiple of |P|^(j/n). For 0<j<n, a nonzero coefficient fails C^1 regularity at the bounding nodal ray. For n<j<2n it fails C^2 regularity. At j=n, smooth matching across adjacent rays gives one global real multiple of P. Subtracting that multiple of f and repeating yields

    theta=theta(p)+C f+O(rho^(2n)), C real.                 (9)

In particular the first and second derivatives of theta-theta(p) vanish at p, since n>=3. The next-pressure source vanishes at p, whereas

    Delta(H^kappa)(p)=kappa(kappa-1)b^2/q^2>0.

Thus (2) applied to tau=H^kappa theta forces theta(p)=0. This ordering is needed: the Jacobian equation removes the lower derivatives before the constant term is tested.

Carrier transport extends the surface Taylor remainder in (9) to order 2n in all three variables. This follows from the smooth local transverse flow coordinates for the nonvanishing carrier (3), requiring no global completeness. Consequently

    tau=C H^kappa phi+O(|(x,y,z)|^(2n)).

The exact divergence-based product identity is

    Delta(H^kappa phi)
      =(2kappa-eta)H^(kappa-1)grad H.grad phi
       +kappa H^(kappa-1)phi Delta H
       +kappa(kappa-1)H^(kappa-2)phi|grad H|^2.

At z=0, its terms start in degree n: grad_T H=O(rho), grad_T phi=O(rho^(n-1)), phi_z=O(rho^n). The Taylor remainder has Laplacian order at least 2n-2>n-1. Hence the degree n-1 part of -Delta tau is identically zero.

## 5. Complete source coefficient and contradiction

Expanding Z and P2 in (2) gives

    -Delta tau=R_lin+R_cub,
    R_lin=2Delta(V.grad H)+2tr(DV D^2H),
    R_cub=Delta(V.grad E)+2tr(DV D(DV V))+tr(DV D^2E).

The cubic part has order at least 3n-6>n-1. Substituting V=H^eta grad phi and differentiating incompressibility reduces the linear part to

    R_lin=2H^eta[D^2phi:B+grad phi.C_H],
    C_H=(2eta/H)(D^2H)grad H
       +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H
       +grad Delta H.

At p, (C_H)_T=-2eta b^2 v/q^3. Write vC=v1+i v2 and dC=dvec_1+i dvec_2. The degree n-1, angular mode n-1 is Re(K R w^(n-1)), with

    R=2[-beta vC/q-(3/2)(n-1)dC
        -(2n/q)(c-ir)(3b vC/q^2)
        +B_zz vC/q-2eta b^2 vC/q^3].                       (10)

There are exactly five contributions here: the trace of f_(n+1) from (8); the particular cubic pressure (7); both mixed Hessian entries; phi_zz contracted with B_zz; and the constant transverse C_H term. In particular the mixed contribution has factor two.

The cubic contraction can be checked without selecting n or K. Write Re(Kw^(n-2))=F_re, Im(Kw^(n-2))=F_im. Then D^2_T P=(n-1)[[F_re,-F_im],[-F_im,-F_re]]. Contracting it with 3D^2_T[-rho^2(dvec.x)/8] gives -(3/2)(n-1)Re(K dC w^(n-1)), as in (10).

Every free jet is accounted for. The harmonic cubic h3h contracts to angular mode |n-3|, different from n-1. The free harmonic part of f_(n+1) has zero trace against beta I. Higher mixed B entries multiply derivatives of order at least n-1 and contribute above degree n-1. Higher C_H entries do likewise. The transverse linear part of H^eta is zero, and its preceding source term is beta Delta_T P=0. No unchosen potential or pressure coefficient can cancel the tested mode.

Substitution of (4) and (6) into (10) gives the exact identity

    R=b vC[A_n+6i(5n-1)r]/(2q^3),
    A_n=b(15n+3)-3c(n+1)-4eta b
       =30n+2-(33n+1)c
       =(27n+3)/2+(33n+1)(1/2-c)>0.                       (11)

Here b>0, q>0, n>=3 and vC!=0. Thus R!=0 for every real r. Since K!=0, Re(KR w^(n-1)) is a nonzero real harmonic polynomial. This contradicts Section 4 and proves the off-axis assertion. Together with the independently proved axial case, it proves Section 1.

## 6. Actual-profile consequence and exact limitations

Let an actual profile have U in C^2(R^3), P in C^1(R^3), satisfy full rotating momentum and divergence, and obey U.curl U=0 globally. Assume both natural bounds

    |U(y)|<=C(1+|y|)^(-p0),
    |DU(y)|<=C(1+|y|)^(-p0-1), p0=(1-c)/c.

Suppose its leading pair V,S is smooth near p!=0, with k=X.V=0 and S>0 on an open neighborhood, and V(p)=0 with p in supp curl V. The supportedness premise excludes a locally identically zero branch. The independently checked LIT288 local unique continuation result gives finite vanishing order. The actual pointwise law gives DV(p)=0, hence N>=2. The full next scalar is supplied by A647-A648 when c!=3/7 and by the averaged A653-A654 at c=3/7 and omega!=0. Set H=S and apply Section 1. Then grad S(p) cannot be parallel to X(p). On the axis the stronger LIT290-LIT291 result excludes the zero itself.

This does not exclude general off-axis positive-pressure zeros with a transverse pressure gradient. It does not cover S=0, boundary points of the open k=0 region, unsupported zeros, or tails lacking the smoothness hypothesis. No helicity or quantitative decay condition has been derived from velocity decay alone. The global nonexistence question remains open.

## 7. Independent verification record

All seven source sections, both source scripts and their JSON outputs, and all seven sections of this proof were read. The source's four Cartesian checks are evidence for its derivation, not the parameter-uniform proof. Their 24.63498761318624 actual seconds were not rerun or attributed to this agent.

Our independent symbolic check reconstructs the differentiated pressure jet, the cubic Hessian contraction with formal real and imaginary amplitudes, the transverse C_H vector, the complete coefficient (10), the Euler-parameter simplification and the positive decomposition (11). All remainders are exactly zero; see in the team records and in the team records for the actual elapsed time and execution environment. No sampled values of c or n are used. The uniform proof is the order analysis and positive factor above. Source snapshots and hashes are retained in the team records. No formal build was run.
