# A nonzero scalar cannot accompany a supported infinitely flat velocity zero

## 1. Exact local theorem

Fix 0<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, X=Ax, a=1-2c>0, b=2(1-c)>0, p=(1-c)/c>1 and eta=a/b in (0,1). Let x0!=0. On a short flow tube about x0, let smooth real V,P2 satisfy

    div V=0, W=curl V, S=P2-|V|^2/2, k=X.V,
    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    P2(exp(tA)x)=exp(-bt)P2(x),
    -Delta P2=tr((DV)^2), W.grad S=0,
    grad k cross grad S=0 on {W!=0}.

Homogeneity is required only for short flow segments contained in the tube. Assume V(x0)=DV(x0)=0, S(x0)!=0 and x0 in supp W. Then k=0 on some full neighborhood of x0. If in addition V vanishes to infinite order at x0, these hypotheses are inconsistent: V must be zero on a smaller neighborhood, contradicting support.

No density of vorticity, regular patch boundary, finite patch count, axisymmetry or initial open-k-zero premise is used. No separate helicity assumption is required for this local statement. On the k-zero neighborhood, the geometric identity X cross W=aV itself implies V.W=0.

At the target range 2/5<c<1/2, combining this theorem with A1288-A1291 removes the premise S(x0)=0 from the finite-scalar-order exclusion. Every smooth supported infinitely flat velocity zero has S infinitely flat as well, including its value at the point. This strengthens the prior statement, which assumed the point already belonged to T0.

## 2. A strict coefficient at a second-order velocity zero

The exact pressure identity implies

    Delta S=-tr((DV)^2)-|DV|_F^2-V.Delta V.

Therefore Delta S(x0)=0. Scalar homogeneity gives X.grad S=-bS. Since X0!=0 and S(x0)!=0, grad S(x0)!=0. Shrink to a connected ball D about x0 on which S has no zeros, and put g=|S|^eta. Then

    Q=Delta g/g
      =eta[S Delta S-(1-eta)|grad S|^2]/S^2.

At x0 the right side is strictly negative. By continuity, Q<0 throughout a smaller ball D. This uses only V=DV=0 at the point, not infinite-order flatness.

Vector differentiation and velocity homogeneity give

    grad k=X cross W-aV, X.grad k=-ak.

Contracting the rank identity with X yields k grad S=(b/a)S grad k on the vortical open set. Thus f=k/g has grad f=0 there, and every positive-order derivative of f vanishes on its closure.

## 3. A full neighborhood with k=0

Let O=int_D{W=0}. On O, Delta V=-curl W=0, and direct differentiation gives

    Delta k=X.Delta V-2omega W3=0.

On D minus O, all positive derivatives of f vanish, so Delta k=Qk. At a boundary point of O, continuity from O gives Delta k=0. Since Q<0, k=0 there. Then f=0 there, and all derivatives of k vanish because every positive derivative of f already vanishes.

Define K=k on O and K=0 on its complement. This is a C^2 harmonic function on D. At an arbitrary boundary point, the zero jets of k through order2 and Taylor's formula give twice differentiability of the extension with zero derivatives, and continuity of the second derivatives. No boundary regularity is needed.

Since x0 belongs to supp W, D contains a nonempty vortical open set. K is zero on that open set, so harmonic analyticity and continuation along overlapping balls give K=0 throughout connected D. Consequently k=0 on O, while grad f=0 on its complement. Thus grad f=0 everywhere on D. Because f(x0)=0, it follows that f=k=0 on D.

This proves the first assertion of Section1, including the case of arbitrarily many irrotational patches. If support is omitted, the alternative that a whole neighborhood is irrotational must be retained.

## 4. Ordinary ellipticity on the transverse disk

Choose a smaller spherical transverse disk through the flow ray of x0 and a short flow interval whose tube lies in D. A positive fixed dilation may place the base point on the unit sphere; composing V,P2 with it preserves the local identities. Write tau=omega/c, zeta=Jn, v=n.V, Y=V-vn, rho=n.W/c and F=W-rho An. Let R_n h=n cross h. The verified angular identities on k=0 are

    v=tau zeta.Y, F=-(a/c)R_n Y,
    div_S F=a rho, F.grad_S h=b rho h,
    div_S(D0Y)+(2-p)tau zeta.Y=0,
    D0=I+tau^2 zeta tensor zeta,

where h is the restriction of S. They follow from the exact radial homogeneity, div V=div W=0, X cross W=aV and W.grad S=0. All coefficients are smooth and D0 is strictly positive for every finite omega.

In coordinates on the disk with metric G and area density sqrt(g_metric), put Fhat=sqrt(g_metric)F_components and Khat=G adj(D0)/sqrt(g_metric). The two first-order equations become

    div(|h|^(-eta)Fhat)=0,
    curl(Khat Fhat)=bhat.Fhat,

where Khat is symmetric positive and bhat is smooth; its angular version is -(2-p)tau R_n zeta. Since h is nonzero, these coefficients have no singularities.

On a simply connected disk there is a smooth stream u with grad u=R |h|^(-eta)Fhat, where R(s,t)=(-t,s). Thus Fhat=-|h|^eta R grad u. The second equation becomes

    div(A1 grad u)+b1.grad u=0,
    A1=|h|^eta adj(Khat), b1=|h|^eta R bhat.                     (1)

A1 is smooth, symmetric and uniformly positive. If V is infinitely flat at x0, Fhat and grad u are infinitely flat at the disk center. Subtract u(0) to make u itself infinitely flat. It remains to prove ordinary elliptic continuation at that point. A full-disk proof follows because the nodal-sector Poincare inequality from A1290 is not appropriate here.

## 5. A trace estimate and the frequency energy

Consider a smooth real solution u of div(A1 grad u)+b1.grad u=0 on a planar disk, with A1 symmetric positive and b1 smooth. A fixed linear coordinate change and scalar normalization give A1(0)=I. Write A=A1=I+O(r), with bounded first derivatives, and b=b1. For small centered disks B_r define

    mu=nu.Anu, H=integral_(partial B_r) mu u^2,
    D=integral_(B_r) grad u.Agrad u,
    J=integral_(B_r) u b.grad u, I=D-J,
    B0=integral_(partial B_r) (nu.Agrad u)^2/mu.

Integration by parts in the equation gives I=integral_(partial B_r)u nu.Agrad u. The ordinary trace estimate is

    integral_(B_r)u^2<=C r H+C r^2 D.                           (2)

For a direct proof, write u(s theta)=u(r theta)-integral_s^r partial_r u(t theta)dt, and apply Cauchy-Schwarz with weights t and 1/t. Integration in s ds and theta is finite because integral_0^r s log(r/s)ds=r^2/4. Uniform ellipticity then gives (2).

Hence |J|<=C sqrt(r H D)+C rD. Young's inequality and a smaller radius give

    |J|<=D/2+C rH,
    I>=D/2-C rH,
    rD/H<=2N+C r^2, N=rI/H>=-C r^2,                           (3)

whenever H>0. This replaces the sector Dirichlet estimate; u(0)=0 alone is not used as a false full-disk Poincare condition.

## 6. Full-disk frequency differential inequality

Differentiating H and integrating the tangential term from A nu-mu nu around the circle gives

    H'=H/r+2I+O(H).                                           (4)

Indeed A nu-mu nu=O(r) and its tangential derivative is bounded, while the radial derivative of mu is bounded. There are no side boundaries.

For the energy identity use Z=Ax/mu. It has Z=x+O(r^2), DZ=I+O(r), and Z.nu=r. Apply the divergence theorem to

    (grad u.Agrad u)Z-2(Z.grad u)Agrad u.

The terms containing second derivatives of u cancel. The derivatives of A and the errors in DZ contribute at most C rD in the volume identity, and the equation div(Agrad u)=-b.grad u contributes the same bound. Its circle flux is rD'-2rB0. Dividing by r gives

    D'=2B0+O(D), |J'|<=C sqrt(H D').                           (5)

The latter is circle Cauchy-Schwarz. D' is the nonnegative circle energy.

Set Q0=B0/H-I^2/H^2>=0 by the boundary flux formula. Differentiate N=rI/H using (4)-(5):

    N'=2rQ0-rJ'/H+O(rD/H)+O(|N|).

From (3), rD/H<=2N+C r^2. Also

    r|J'|/H<=C r sqrt(D'/H)
              <=C r sqrt(Q0)+C|N|+C sqrt(r(N+C r^2)).

Choose a small radius so N>=-1/2. Absorb C r sqrt(Q0) into rQ0+C r, and bound the remaining terms by C(N+1). It follows that

    N'>=-C(N+1).                                               (6)

Every inequality is on ordinary full disks with smooth coefficients. No singular weight or missing central integrability assumption is present.

## 7. Infinite order forces zero

If H(r)=0 at a small radius, then u has zero boundary trace. Formula (2) reduces to integral u^2<=C r^2D, giving |J|<=C rD. The flux I is zero, so D=J and D=0 for sufficiently small r. Thus u is zero inside that disk.

Otherwise H>0 at every small radius. Equation (6) makes exp(Cr)(N+1) nondecreasing, so N is bounded above as r decreases to0. From (4), H'/H<=C0/r on a sufficiently small interval. Integration from r to a fixed small radius gives H(r)>=C1 r^C0 for some C1>0. Infinite flatness of u supplies an upper bound of every polynomial order, a contradiction.

Therefore u vanishes near the center. Its gradient and Fhat vanish there, and F=-(a/c)R_nY with v=tau zeta.Y gives V=0 on the transverse disk. Homogeneity extends zero to a full neighborhood of x0. This contradicts x0 in supp W and proves Section1.

## 8. Combined scalar-flat conclusion and its exact scope

For the target local range 2/5<c<1/2, let V have an infinitely flat zero x0 in supp W under the same smooth local identities. If S(x0)!=0, the theorem just proved gives a contradiction. Therefore S(x0)=0. If S has a finite nonzero Taylor order, A1288-A1291 gives a contradiction even with arbitrary accumulating irrotational patches. Consequently every derivative of S at x0 vanishes.

Thus the condition S(x0)=0 need not be imposed separately when concluding common V/S flatness at a smooth supported infinitely flat velocity zero. C49's still-open strict-positive-pressure branch at a general C^1 T-flat point does not include a smooth infinitely flat velocity zero. This result retains the full scalar rank and pressure identities and does not establish continuation when both V and S are flat.

For actual HF/natural profiles, tail smoothness on the chosen neighborhood and the exact previously verified identities are still required. No global original smoothness, symmetry, density or arbitrary-helicity conclusion has been added. The global conjecture remains open.

## 9. Verification and comparison

The strict Q sign and harmonic zero extension are independent extensions of A1288-A1289 to the case of a nonzero scalar value. The angular first-order equations were checked at their exact coefficients in A1262 and A1290. Sections5-7 provide the complete ordinary elliptic frequency argument, with a trace estimate that explicitly accounts for the absence of nodal Dirichlet sides. No external unique-continuation theorem, numerical experiment or formal build is used. Existing configured model agents are requested to compare this proof, especially Sections3 and5-7; provider runtime remains unattested and no new client or agent is launched.
