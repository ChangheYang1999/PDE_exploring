# Off-axis first next-pressure compatibility

## 1. Exact theorem and scope

For every 2/5<c<1/2, omega!=0, point p off the rotation axis, and integer N>=2, the following real analytic local germs exist. Put Jx=e3 cross x, X(x)=(cI-omega J)x, a=1-2c, b=2(1-c), eta=a/b, kappa=(b+1)/b, n=N+1. On a sufficiently small neighborhood G of p there are analytic V,H,p1 with H>0 such that, writing W=curl V, E=|V|^2, P2=H+E/2 and Z=DV V+grad P2,

    div V=0, X.V=0, XH=-bH,
    X cross W=aV, W.grad H=0,
    -Delta P2=tr((DV)^2),
    Xp1=-(b+1)p1, W.grad(p1-2V.grad P2)=0.

The zero sets of V and W are one local X-orbit arc Gamma. Both fields have exact order N there and their relative vorticity support is all G. The restriction of B=3Hess H+(eta/H)grad H tensor grad H to X-perp is scalar on Gamma, while grad H has nonzero transverse component there. The remaining residual

    R=Delta p1+2tr(DV DZ)

vanishes to transverse order at least N+1 along Gamma. In particular R=O(|x-p|^(N+1)) near p. No assertion R=0, no actual asymptotic tail and no global Euler profile is included.

## 2. Cartesian pressure data and analytic realization

Use an oriented orthonormal frame centered at p, with third vector X(p)/q, q=|X(p)|>0. Rotate the transverse basis so that

    X=(cx+ry-vz, -rx+cy, q+vx+cz), v>0.

The strict inequality v>0 follows from p being off axis and omega!=0. The number r may have either sign or be zero. Set

    Dn=8b eta(n-1)+12b(3n-1)+18c(n-1)>0,
    g=6b(5n-1)v/(q Dn)>0.

At the center prescribe H=1, (H_x,H_y,H_z)=(g,0,-b/q). Differentiating XH=-bH gives

    h33=b(b+c)/q^2+vg/q,
    t=-h33/2+eta g^2/6,
    T=diag(t-eta g^2/3,t),
    u=(-(b+c)gvec-r J_T gvec+b vvec/q)/q,
    d=(-(b+2c)u-r J_T u+T vvec-h33 vvec)/q,

where gvec=(g,0), vvec=(v,0), J_T(x,y)=(-y,x), T=Hess_T H, u=H_Tz and d=grad_T H_zz. In particular tr T+h33=0 and 3T+eta gvec tensor gvec=3t I.

On z=0 prescribe through degree three

    h=1+gx+(1/2)(x,y).T(x,y)
       -rho^2(d1 x+d2 y)/8+(A3/6)Re(w^3)+O(rho^4),
    w=x+iy, rho^2=x^2+y^2,
    A3=eta g^3(2eta+3)/36.

These data are realized, rather than merely assumed to be compatible. The analytic chart F(s,x,y)=exp(s(cI-omega J))(p+x e1'+y e2') has invertible derivative at zero. With its inverse coordinates, put phi=f(x,y), H=exp(-bs)h(x,y), V=H^eta grad phi. Then Xphi=0 and XH=-bH give the cross-product identities and exact vector transport XV=-[(1-c)I+omega J]V. Only divergence and Poisson remain.

Define F0=Delta phi+eta grad(log H).grad phi. An exact product expansion gives

    Delta(H+|V|^2/2)+tr((DV)^2)=F2+H^(2eta)grad phi.grad F0,

    F2=Delta H+(|grad phi|^2/2)Delta(H^(2eta))
       +2grad(H^(2eta)).(Hess phi grad phi)
       +H^(2eta)|Hess phi|^2
       -eta H^(2eta)grad phi.grad(grad(log H).grad phi)
       +tr((DV)^2).

F0 and F2 involve only second derivatives of f,h, and F2 is affine in second derivatives of h. On s=0, F0 solves for f_yy and then F2 solves for h_yy. At the center both required principal coefficients are one, because H=1 and grad phi=0. Analytic noncharacteristic solvability persists on a small initial interval. Prescribe f(x,0)=x^n/n, f_y(x,0)=0, and h,h_y on y=0 from the displayed cubic polynomial. The analytic Cauchy theorem yields convergent f,h. Divergence and Poisson propagate off the section by their exact similarity weights.

Induction in the divergence equation gives f=Re(w^n)/n+O(rho^(n+1)). Therefore V has order n-1=N, and Delta H=O(rho^(2n-4)). Its value and first derivatives vanish at p. The prescribed H_xx,H_xy and the trace fix H_yy as in T. The cubic trace is Delta_T h3=-d1 x-d2 y; the prescribed two Cauchy traces then fix exactly the stated cubic. Thus the analytic solution has every jet used below.

## 3. Exact residual reduction

Set tau=C H^kappa phi and p1=2V.grad P2+tau for a real C to be chosen. Homogeneity gives Xp1=-(b+1)p1: both V.grad P2 and H^kappa phi have that weight. Since W is perpendicular to grad H and grad phi, the other scalar transport law also holds exactly.

Expanding the residual gives

    R=Delta tau+Rlin+Rcub,
    Rlin=2H^eta[Hess phi:B+grad phi.C_H],
    C_H=(2eta/H)(Hess H)grad H
       +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H
       +grad Delta H,
    Rcub=Delta(V.grad E)+2tr(DV D(DV V))+tr(DV Hess E).

To check Rlin, expand 2Delta(V.grad H)+2tr(DV Hess H). The product rule produces 2Delta V.grad H+6DV:Hess H+2V.grad Delta H. Substitute V=H^eta grad phi and Delta phi=-eta grad(log H).grad phi. The Hess phi terms give exactly B; the remaining terms give C_H. This derivation uses the full divergence equation and retains the two mixed Hessian entries.

Every cubic term has order at least 3n-6, which is greater than n-1 for n>=3. Also Delta H=O(rho^(2n-4)), so its gradient term cannot contribute at degree n-1. At degree n-2, the only possible term is the scalar transverse Hessian of H contracted with the trace-free Hessian of Re(w^n)/n; it vanishes. Consequently the first test is precisely the complete degree n-1 transverse polynomial of Rlin+Delta tau.

## 4. All angular bands of the first test

Let P=Re(w^n)/n. On z=0, scalar transport implies

    phi_z=-(c Euler-r J_T.grad)P/q+O(rho^(n+1)),
    (phi_zz)_(n-1)=v P_x/q,
    Delta_T f_(n+1)=-(eta g+v/q)P_x.

Put beta=3t, BT=3u-eta b gvec/q, B33=3h33+eta b^2/q^2 and

    CH=2eta(T gvec-bu/q)+eta^2(g^2+b^2/q^2)gvec.

For zeta_C=zeta1+i zeta2, the coefficient of Re(R0 w^(n-1)) in Rlin is

    R0=2[-beta(eta g+v/q)-(3/2)(n-1)d_C
         +eta g(n-1)(-h33-g^2/2)
         -(2n/q)(c-ir)BT_C+B33 v/q+CH_C].          (1)

Here the first term comes from the trace of f_(n+1), the second from the cubic particular pressure, the third from the linear gradient outer product, and the last three from the mixed, vertical and C_H entries. An arbitrary harmonic part of f_(n+1) has zero contraction with beta I and cannot affect (1).

For clarity, the entire lower band is also checked. Write Rm=Re(w^(n-2)) and Im=Im(w^(n-2)). The linear part of eta H^(-1)grad_T H tensor grad_T H is

    eta [[(2g T11-g^3)x, g T22 y], [g T22 y,0]].

Its contraction with Hess_T P uses

    x Rm=(Re(w^(n-1))+rho^2 Re(w^(n-3)))/2,
    y Im=(rho^2 Re(w^(n-3))-Re(w^(n-1)))/2.

This gives the high term in (1) and, after the outside factor two, the low coefficient -eta g^3(n-1)(1+2eta/3). The particular cubic -rho^2(d.x)/8 has Hessian contraction -(n-1)d.grad P/2, so it contributes only to the high band. The harmonic cubic (A3/6)Re(w^3) has Hessian A3[[x,-y],[-y,-x]]; contracting with Hess_T P and multiplying by six gives

    12(n-1)A3 rho^2 Re(w^(n-3)).

Thus the entire low coefficient is (n-1)[12A3-eta g^3(1+2eta/3)]=0. For n=3 its mode is the radial polynomial rho^2; the same cancellation applies. There are no omitted angular bands, since these are the full contractions of linear matrix coefficients with Hess_T P.

## 5. High-band cancellation and uniform residual order

Direct substitution of the real Cartesian data in (1) gives

    Im R0=-r[qg Dn-6b(5n-1)v]/(2q^3).

The chosen g makes this zero for every r. Independently, the product rule and divergence give

    Delta(H^kappa phi)
      =(2kappa-eta)H^(kappa-1)grad H.grad phi
       +kappa H^(kappa-1)phi Delta H
       +kappa(kappa-1)H^(kappa-2)phi|grad H|^2.

Its degree n-1 term is (2kappa-eta)g Re(w^(n-1)). Since g>0 and 2kappa-eta>0, the real choice

    C=-R0/[(2kappa-eta)g]

cancels the high band. Section4 cancels the only other band. All lower degrees vanished in Section3, so R=O(rho^n) on the section.

Both terms in R have scalar weight three. Indeed p1 has weight b+1, and b+1+2c=3. The vector Z has weight 2-c with the same rotational covariance as V; DV and DZ then have weights one and two, and their trace product has weight three. Hence

    R(F(s,x,y))=exp(-3s)R(F(0,x,y)).

This proves transverse order n=N+1 all along the arc, as well as the stated Euclidean order at p. It proves no exact residual equation at higher order.

## 6. Zero sets, support and transported pressure test

The gradient of P=Re(w^n)/n has norm rho^(n-1), while the gradient remainder has order rho^n. On a smaller punctured section grad f never vanishes, and its only zero is the center. Multiplication by H^eta and the invertible chart preserve this exact order. Moreover

    W=eta H^(eta-1)grad H cross grad phi.

Because X.grad H=-bH!=0 and X.grad phi=0, the map grad H cross is injective on X-perp. Thus W has exactly the same zero set and order as V. The complement of the central arc is dense in the product flowbox, proving relative supp W=G.

The Hessian and divided gradient outer product defining B have the same conformal rotational covariance. X-perp rotates under that covariance. The scalar restriction of B and nonzero transverse pressure gradient at p therefore persist along Gamma. On the arc N>=2 gives V=W=DV=DW=0, k=0,H>0, so the previously checked five pointwise zero laws hold. None is promoted to a sufficient condition for a global profile.

## 7. Exact verification and independent scope

The complete seven-section submitted proof, the earlier six-section analytic foundation, the source plan, full checker and both helper files, logs, result and initial failure record were read. No source helper was imported or executed here. The independent checker reconstructs the Cartesian Hessian and mixed derivatives directly, checks nine symbolic remainders, and checks the two displayed rational triples for n=3,4. Every remainder is zero. Its actual runtime was0.7180421678349376seconds on CPU55, nice19, OMP1. The source's separate Cartesian reconstruction reports12.868327816948295seconds; it was inspected but not rerun.

The low-band and all-degree arguments are the algebraic derivations in Sections3-5; the two finite reconstructions do not replace those arguments. The source's initial namespace failure occurred before mathematical checks and gives no failed mathematical example.

This local construction verifies the limit of the first two pressure tests in the general off-axis class. A full next-pressure scalar, higher compatibility conditions, extension to a global tail or profile, and the unrestricted nonexistence theorem remain open. Existing configured model coordinator/theory collaboration receives this audit through files; actual provider execution is not independently attested.
