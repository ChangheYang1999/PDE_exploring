# Fourth pressure jet in the exact adjusted axial family

Status: CONFIRMED for the precise LIT289 family and next-scalar system below. General positive-pressure arcs, arbitrary fourth pressure data and unrestricted rotating-profile nonexistence remain OPEN.

## 1. Statement and local analytic family

Fix2/5<c<1/2, any finite real omega, and N>=2 an integer. Set

    A=cI-omega J, Jx=(-x2,x1,0), X(x)=Ax,
    a=1-2c, b=2(1-c), eta=a/b, lambda=b/c in(2,3),
    sigma=omega/c, n=N+1>=3, kappa=(b+1)/b.

Near p=e3, use the analytic orbit chart x=exp(tA)(e3+u e1+v e2). Let phi=f(u,v), H=exp(-bt)h(u,v), V=H^eta grad phi, P2=H+|V|^2/2, W=curl V, Z=DV V+grad P2. Take the unique local analytic solution supplied by the previously proved Cauchy construction with

    div V=0, -Delta P2=tr((DV)^2),
    f(u,0)=u^n/n, f_v(u,0)=0,
    h(u,0)=1-lambda(lambda+1)u^2/4, h_v(u,0)=0.

These exact data are essential. The already verified construction gives k=X.V=0, H>0, XH=-bH, X cross W=aV, W.grad H=0, and an axis orbit of common V,W zeros of exact order N. Its tensor 3D2H+(eta/H)dH tensor dH is isotropic on X-perp there.

Claim. There is no C1 function p1 on a neighborhood of p satisfying

    X.grad p1=-(b+1)p1,
    -Delta p1=2tr(DV DZ) in distributions,
    W.grad(p1-2V.grad P2)=0.

The claim holds at every omega; no small-rotation bound enters.

## 2. Axial Cartesian derivatives and the forced pressure jet

Writing z=x3>0 and w=u+iv, the inverse chart is z=exp(ct) and w=z^-1 exp(i sigma log z)(x1+i x2). Put D=u partial_u+v partial_v, T=-v partial_u+u partial_v, Q=D-sigma T. At z=1, z partial_z phi=-Qf and z partial_z H=-(lambda+Q)h. A second derivative therefore gives

    Delta phi=Delta_T f+Q(Q+1)f,
    Delta H=Delta_T h+(lambda+Q)(lambda+Q+1)h.

All these transverse operators preserve homogeneous degree and angular Fourier mode. In particular rotation changes coefficients within a mode, not its angular order.

Let rho^2=u^2+v^2. The constant Poisson equation and the two Cauchy traces give h2=A2 rho^2, A2=-lambda(lambda+1)/4. The degree-one Poisson equation and zero traces give h3=0; h1 is also zero. At degree two, when n>=4, nonlinear pressure terms have degree at least2n-4>=4. Thus

    Delta_T h4=-(lambda+2)(lambda+3)A2 rho^2.

When n=3, write P=Re(w^3)/3 and v0=grad_T P=(u^2-v^2,-2uv). Then |v0|^2=rho^4 and tr((Dv0)^2)=8rho^2. Hence Delta_T(|v0|^2/2)+tr((Dv0)^2)=16rho^2. Vertical velocity has order n, its horizontal derivatives order n-1, and vertical derivatives preserve transverse order, so no vertical term contributes to this degree-two source. Therefore

    h=1+A2 rho^2+B4(rho^4-Re(w^4))+O(rho^5),
    B4=lambda(lambda+1)(lambda+2)(lambda+3)/64-1_(n=3).

Indeed Delta_T rho^4=16rho^2; subtracting Re(w^4) makes both fourth-order Cauchy traces zero, uniquely fixing the harmonic part. Since lambda>2, B4>7/8 for n=3 and B4>15/8 for n>=4. The nonaxisymmetric fourth term -B4 Re(w^4) is thus nonzero even though the second jet is isotropic.

## 3. Potential jets and the transported scalar's angular restriction

On z=1, div(H^eta grad phi)=0 is

    Delta_T f+Q(Q+1)f
      +eta h^-1[grad_T h.grad_T f+((lambda+Q)h)(Qf)]=0.

The lowest term is P=Re(w^n)/n. The next term of degree n+1 is harmonic with zero Cauchy traces, hence zero. At degree n,

    Delta_T f_(n+2)=-Q(Q+1)P-eta[2A2 nP+lambda QP].

The right side has only angular mode n. The degree-n+2 potential can contain a harmonic component of mode n+2; it is not set to zero here.

If p1 existed, the smooth right side of its distributional Poisson equation would make p1 smooth by local elliptic regularity. Put tau=p1-2V.grad P2 and theta=tau/H^kappa. The previously verified next-scalar reduction gives Xtheta=0, Jac(f,theta)=0 on the transverse section, theta(0)=0 and theta_n=C P for some real C. The zero constant follows from the nonzero value of Delta H^kappa at p; the lower positive degrees follow from the same homogeneous centralizer argument used next.

Subtract C f. If its first remaining homogeneous Taylor term R_j has n<j<2n, then Jac(P,R_j)=0. Euler's identity and Jac(P,R_j)=0 imply on each regular nodal sector that R_j=C_sector |P|^(j/n). The normal derivative of P does not vanish at a regular nodal ray away from the origin. Since1<j/n<2, a nonzero coefficient makes the second normal derivative unbounded approaching that ray. A polynomial cannot do this. Every coefficient is zero. The analogous first-derivative argument excludes0<j<n. Thus, with differentiated smooth remainders,

    theta=C f+O(rho^(2n)),
    Delta tau=C Delta(H^kappa phi)+O(rho^(2n-2)).

The X-invariance ensures that z derivatives preserve the transverse remainder order. Since2n-2>n for n>=3, only the displayed main term matters at degree n. Using the weighted potential equation,

    Delta(H^kappa phi)
      =(2kappa-eta)H^(kappa-1)grad H.grad phi
        +kappa H^(kappa-1)phi Delta H
        +kappa(kappa-1)H^(kappa-2)phi|grad H|^2.

At degree n every term has angular mode n. The needed pressure jets are radial A2 rho^2 and H_z(0)=-lambda; phi_z starts as -QP. The middle product starts at degree3n-4>n because Delta H=O(rho^(2n-4)). Thus the degree-n part of -Delta tau has no mode |n-4|.

## 4. Exact linear source identity

Let E=|V|^2 and F=H^eta. Substituting p1=tau+2V.grad P2 into its Poisson equation gives

    -Delta tau=R_lin+R_cub,
    R_lin=2Delta(V.grad H)+2tr(DV D2H),
    R_cub=Delta(V.grad E)+2tr(DV D(DV V))+tr(DV D2E).

This follows simply by expanding Z=DV V+grad H+grad E/2; no term is dropped. Differentiating div(F grad phi)=0 yields

    Delta V=D2phi grad F+[(Delta F)I-F D2(log F)]grad phi.

Inserting it into the product Laplacian and collecting the three Hessian contractions gives

    R_lin=2F[D2phi:B+grad phi.C_H],
    B=3D2H+(eta/H)grad H tensor grad H,
    C_H=(2eta/H)(D2H)grad H
          +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H
          +grad Delta H.

For an explicit coefficient check, the gradient coefficient before simplification is (Delta F/F)grad H-D2(log F)grad H+3D2H grad F/F+grad Delta H. Here Delta F/F=(eta/H)Delta H+eta(eta-1)|grad H|^2/H^2 and D2(log F)=eta D2H/H-eta grad H tensor grad H/H^2. Their sum is exactly C_H. In particular the tensor coefficient is3, and the last squared-gradient coefficient is eta^2.

## 5. The cubic exceptional case and the new mode

Every term of R_cub has lowest possible transverse degree3N-3=3n-6. For n>=4 this exceeds n. When n=3 only v0 from Section2 enters degree three. Direct polynomial differentiation gives

    v0.grad rho^4=12rho^2 P,  Delta_T(rho^2P)=16P,
    Dv0 v0=2rho^2(u,v),
    Delta_T(v0.grad rho^4)=192P,
    2tr(Dv0 D(Dv0 v0))=48P,
    tr(Dv0 D2(rho^4))=48P.

For example Dv0 is trace-free and (u,v).Dv0(u,v)=6P, which immediately gives the last two contractions. The sum is288P, purely mode three. Vertical components have strictly higher degree in these contractions. Hence R_cub never supplies mode |n-4| at degree n.

It remains to identify every possible contribution of the pressure fourth harmonic to R_lin. Its transverse Hessian has degree2, its mixed Hessian degree3 and its vertical Hessian degree4. Grad_T phi begins at degree n-1, its transverse Hessian at n-2, mixed Hessian at n-1 and vertical Hessian at n. Thus the sole degree-n contribution of H4_nonax=-B4 Re(w^4) is

    6 D2_T P:D2_T H4_nonax.

Its transverse Laplacian is zero; its vertical Laplacian starts at degree4, so grad Delta H also contributes only above n. The gradient products, variations in F, and all mixed or vertical Hessians likewise have degree greater than n. All other pressure coefficients that can enter at degree n are axisymmetric and preserve mode n, including arbitrary sigma terms. The sole possible contribution of f_(n+2) is its transverse Hessian contracted against the constant scalar transverse part of B. It is a multiple of Delta_T f_(n+2), which has mode n. The free harmonic mode n+2 therefore contributes zero. Higher potential degrees cannot enter.

The trace-free Hessian of Re(w^j) is represented by j(j-1)w^(j-2), and the Frobenius contraction of two such matrices is twice the real part of one representative times the conjugate of the other. Consequently the new contribution equals

    -144 B4(n-1) Re(w^(n-2) conjugate(w)^2)
      =-144 B4(n-1)rho^n cos((n-4)theta_ang).

It is nonzero since B4>0. Its angular mode |n-4| differs from n for every n>=3. This includes n=3, where the new mode is1, and n=4, where it is radial mode0. There is no division by n-4 and no exceptional omega.

## 6. Contradiction and actual-profile transfer

Section3 allows only mode n on the degree-n left side of -Delta tau=R_lin+R_cub. Section5 allows only mode n in R_cub and produces a nonzero mode |n-4| in R_lin. Fourier independence on each small transverse circle contradicts the identity. Hence no p1 with the three stated equations exists for the exact family of Section1.

For application to actual profiles, retain the full global hypotheses: U in C2(R3), P in C1(R3), rotating Euler momentum, div U=0, zero helicity U.curl U=0, and both bounds

    |U(y)|<=C(1+|y|)^(-p0),
    |DU(y)|<=C(1+|y|)^(-p0-1),  p0=(1-c)/c.

If its leading pair agrees locally with this analytic family, the established tail construction gives a next scalar off c=3/7, and its averaged version gives the same required equations at c=3/7 for omega!=0. At omega=0 the already verified ordinary-profile Liouville theorem excludes the decaying profile. These are the precise A647-A648 and A653-A654 dependencies. Thus the family is excluded as such an actual tail, with every global premise retained.

This does not invalidate the leading LIT287 construction. The obstruction uses its exact fourth pressure data. Changing those data can remove this mode but is not shown to solve the remaining next equations. Off-axis members, arbitrary positive-pressure arcs and the unrestricted conjecture remain open.

## 7. Verification record

All six source sections and all seven independent sections were read. The Cartesian chart, pressure coefficient and positivity, polynomial-centralizer remainder, exact C_H identity, three exceptional cubic contractions, every relevant mixed-derivative order and the free harmonic potential term were checked by hand. All are finite algebraic or local smooth arguments; no numerical computation was needed. The actual-tail conclusions use precisely the earlier confirmed hypotheses and resonance treatment. Source and dependencies are pinned in the team records. Existing agent-file model collaboration was used; no new model client or independent runtime attestation is claimed.
