# Positive-pressure arcs that pass the Hessian test

Status: A2114-A2118 CONFIRMED; the overextension tested at A2119 is REFUTED, and the full next-pressure/global extension remains OPEN at A2120.

## 1. Exact local existence statement

Fix 2/5<c<1/2, a finite real omega, an integer N>=2 and a point p!=0. Let

    Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax,
    L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b,
    q=|X(p)|, e=X(p)/q, T=e^perp,
    d=b(b+c)/(2q^2)>0.

There exist a neighborhood G of p, not containing the origin, and real analytic V,P2 on G with E=|V|^2, W=curl V, H=P2-E/2 and k=X.V, such that

    div V=0, V.W=0, k=0, H>0,
    X.grad V=-LV, X.grad H=-bH,
    X cross W=aV, W.grad H=0,
    -Delta P2=tr((DV)^2).

The full scalar rank identity k grad H=(b/a)H grad k holds, including on the relative support of W. The common zero set of V and W is a single local X-orbit arc Gamma through p. Its complement in G is connected and dense, so the relative support of W is G. Both V and W have exact order N at every point of Gamma.

The pressure values and Cartesian Hessian at p are

    H(p)=1, grad H(p)=-(b/q)e,
    Hess H(p)=(b/q^2)[(b+c)e tensor e
       +omega(e tensor Je+Je tensor e)
       -(b+c)(I-e tensor e)/2].                      (1.1)

Consequently B=3Hess H+(eta/H)grad H tensor grad H restricts to a scalar metric on X(x)^perp at every x in Gamma. At p its scalar is -3d. The five pointwise zero laws in Section 6 hold. This construction does not supply the next scalar p1 or an actual global Euler profile.

## 2. Analytic chart and automatic identities

Choose an orthonormal basis e1',e2' of T and use the map

    F(t,u,v)=exp(tA)(p+u e1'+v e2').                  (2.1)

Its differential at zero has columns X(p),e1',e2' and determinant of absolute value q>0. Hence it is an analytic local coordinate chart. Its inverse coordinates satisfy Xt=1, Xu=Xv=0. At p, grad t=e/q, grad u=e1', grad v=e2'. In particular the chart's t=0 surface is the affine plane p+T with orthonormal Euclidean coordinates u,v.

For analytic functions phi_t,H_t on a transverse neighborhood, H_t>0, put

    phi=phi_t(u,v), H=exp(-bt)H_t(u,v),
    V=H^eta grad phi, P2=H+|V|^2/2.                 (2.2)

Then Xphi=0, XH=-bH, k=0, and differentiating these scalar identities gives XV=-LV. To see the latter directly, X grad phi=-A^T grad phi and b eta=a, so XV=-(aI+A^T)V=-LV. Also

    W=eta H^(eta-1)grad H cross grad phi.             (2.3)

This implies V.W=0 and W.grad H=0. Since grad H.X=-bH!=0 whereas grad phi.X=0, the linear map grad H cross is injective on X-perp. Thus W vanishes exactly where V does. The identity

    grad k-X cross W=A^T V+XV=-aV

gives X cross W=aV. The scalar rank equation is identically zero on both sides. Only divergence and Poisson remain to be solved.

## 3. Analytic Cauchy construction for the remaining equations

Define

    R0=Delta phi+eta grad(log H).grad phi.

Then div V=H^eta R0. The product rule gives

    Delta P2+tr((DV)^2)=R2+H^(2eta)grad phi.grad R0,

where, using E_phi=|grad phi|^2,

    R2=Delta H+(E_phi/2)Delta(H^(2eta))
       +2grad(H^(2eta)).(Hess phi grad phi)
       +H^(2eta)|Hess phi|^2
       -eta H^(2eta)grad phi.grad(grad(log H).grad phi)
       +tr((DV)^2).                                 (3.1)

This follows from Delta(E_phi/2)=|Hess phi|^2+grad phi.grad Delta phi. It removes every third derivative of phi. Expression R2 is analytic in the derivatives of phi,H of orders at most two on H>0, and affine in the second derivatives of H.

Restrict div V=0 and R2=0 to t=0, using (2.2) to eliminate all t derivatives. The coefficient of partial_vv phi_t in div V is H^eta|grad v|^2. It is nonzero near the base data H=1, grad phi_t=0, so this equation solves analytically for partial_vv phi_t in terms of derivatives with at most one v derivative and second u derivatives. It contains no second derivative of H_t. Substitute that expression into R2. The coefficient of partial_vv H_t is |grad v|^2 plus terms quadratic in grad phi. At the base point it equals one. Thus the second equation solves analytically for partial_vv H_t. This is a noncharacteristic analytic second-order Cauchy system. The nonzero coefficients persist on a sufficiently small initial interval.

Choose the analytic Cauchy data

    phi_t(u,0)=u^(N+1)/(N+1), partial_v phi_t(u,0)=0,
    H_t(u,0)=1-d u^2/2, partial_v H_t(u,0)=0.         (3.2)

They are positive in H for small u. The Cauchy-Kovalevskaya theorem gives analytic phi_t,H_t near zero, and H_t stays positive on a smaller neighborhood.

The equations propagate away from the section. Under exp(tA)=exp(ct)R_t with R_t=exp(-omega tJ), the divergence residual has weight one. The residual Delta P2+tr(DV^2) has weight two, since V and P2 have their exact covariance, a+2c=1 and b+2c=2. Divergence vanishes on the section, hence throughout the chart, so R0 vanishes identically and its derivative term in (3.1) is zero. R2=0 on the section therefore makes the Poisson residual zero there, and its covariance makes it zero throughout. This proves all the leading equations for convergent analytic fields.

## 4. Leading harmonic term, exact orders and zero sets

At the origin of the transverse coordinates the principal part of the phi_t equation is partial_uu+partial_vv; it has no zeroth-order term. Induct on the homogeneous degree of its Taylor expansion. All lower terms before degree N+1 vanish: at each such degree the first possible term is harmonic and has zero value and normal derivative on v=0 by (3.2), hence is zero. At degree N+1, the two Cauchy traces select the harmonic polynomial

    phi_t(u,v)=Re((u+iv)^(N+1))/(N+1)
                  +O(|(u,v)|^(N+2)).               (4.1)

Coefficient variation cannot contribute at the first nonzero order. The gradient of the polynomial in (4.1) has norm |(u,v)|^N. The gradient remainder is O(|(u,v)|^(N+1)). Shrink the transverse neighborhood so it is less than half the leading magnitude away from zero. Then grad phi_t vanishes precisely at (0,0).

Take G to be the image of a product of a small interval in t and a small transverse square. Equation (2.2) gives {V=0}=Gamma={F(t,0,0)}. Equation (2.3) and its injectivity give {W=0}=Gamma. Removing the center from the transverse square leaves a connected dense set, so G minus Gamma is connected and dense. This proves the relative-support assertion without asserting any field outside G.

At each point of Gamma the leading transverse gradient tensor has exact degree N, and its pullback by the rank-two coordinate map remains nonzero of that degree. Multiplication by H^eta preserves it. The injective linear map in (2.3) preserves its nonzero leading tensor as well. Thus both V and W have exact order N everywhere on the arc. Equivalently their covariance under the invertible linear flow propagates the same order from p.

## 5. Cartesian Hessian and covariance of the test

Because the t=0 section is an affine Euclidean plane, the Cauchy data give at p

    H=1, grad H restricted to T=0,
    Hess H(e1',e1')=-d, Hess H(e1',e2')=0.

The second equality uses partial_v H_t(u,0)=0 along the entire initial interval. Homogeneity gives grad H=-(b/q)e. Differentiate XH=-bH in Cartesian coordinates:

    (Hess H)X=-(bI+A^T)grad H.

With A^T=cI+omega J this yields

    (Hess H)e=(b/q^2)[(b+c)e+omega Je].              (5.1)

Since N>=2, V=DV=0 at p. Poisson and P2=H+|V|^2/2 imply Delta H(p)=0. The e,e entry in (5.1) equals b(b+c)/q^2=2d, because e.Je=0. The remaining transverse diagonal entry must therefore be -d. Equation (5.1) fixes all mixed entries with e. These data give precisely (1.1). The transverse part of grad H tensor grad H vanishes, so B restricted to T is -3d times the metric.

From scalar homogeneity and the linear Euclidean similarity flow,

    grad H(exp(tA)x)=exp(-(b+c)t)R_t grad H(x),
    Hess H(exp(tA)x)=exp(-(b+2c)t)R_t Hess H(x)R_t^T.

The gradient outer product divided by H has the same second weight. Thus B has the same covariance. Also X(exp(tA)p)=exp(ct)R_t X(p), so its perpendicular plane is R_t T. The scalar-metric condition propagates all along Gamma, with scalar -3d exp(-(b+2c)t). No axis or small-omega assumption was used. When p is off the rotation axis, a smaller chart avoids that axis.

## 6. Pointwise laws and the precise countertest

Here are the five pointwise laws being tested, with support understood relative to G.

1. At a supported common zero of V and W, H>=0; if DW!=0 there, then H=0.
2. At a common zero with DW!=0, DV=0 and DW=X tensor ell for a nonzero covector ell with ell(X)=0.
3. At any zero of W, the matrix DW is nilpotent.
4. At a supported common zero in the interior of {k=0}, DV=0.
5. At a supported zero of W with range DW contained in the line R X, one has k<=0, and k=0 implies H>=0. At a supported zero of W with k>0 or with k=0,H<0, one has V!=0 and rank DW=1.

On Gamma, V=W=DV=DW=0, k=0 and H>0. Every conclusion whose premises hold is satisfied. Statements requiring DW!=0, k>0 or H<0 have false premises. Away from Gamma the zero premises fail. In particular the construction respects the complete five-law list rather than just its nondegenerate portions.

This proves that the isotropy condition of A2110, together with all the leading local equations and those five laws, does not exclude a positive-pressure arc of any prescribed finite order N>=2. It does not prove compatibility with the complete next-pressure equations: no p1 is constructed. It does not establish the existence of a global natural tail, a global Euler profile, or an infinite-order example. The earlier C59/LIT285 pressure data fail the Hessian test; the changed data here pass it. Both findings coexist.

Dependencies are the classical local analytic inverse function and Cauchy-Kovalevskaya theorems, the complete product expansion (3.1), and elementary harmonic polynomial and Cartesian calculations written above. The previously confirmed signed reduction A2086-A2089 provides an independently checked comparison. No numerical computation or formal build was needed. Source hashes are retained in the team records.
