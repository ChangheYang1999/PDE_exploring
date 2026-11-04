# A constrained maximum for scalar transport in a sector

## Exact statement

Let 0<theta1<theta2<pi/2 and let D be the closed planar sector with radius r>=0 and angle theta in [theta1,theta2]. Let W be continuous on D and C1 on an open neighborhood of each nonzero point of D. Suppose W(0)=0, W>=0 on D, W tends uniformly to zero as r tends to infinity in D, and

    sup_(r>0) W(r,theta2)>sup_(r>0) W(r,theta1).        (1)

Let b be a C1 vector field on a neighborhood of D without its vertex. Let S and R be continuous on that neighborhood and suppose

    b.grad W+W-S=R.                                   (2)

Assume b.e_theta>0 on the upper ray theta=theta2, where e_theta=(-sin theta,cos theta). Then W attains a positive maximum on D. Every maximum point z0 is nonzero, finite, and off the lower ray. At every such point,

    R(z0)>=W(z0)-S(z0).                               (3)

In particular (2) with R=0 cannot hold if W(z0)>S(z0) at some maximum. More generally it cannot hold if R(z0)<=epsilon<W(z0)-S(z0). No uniqueness or strict isolation of the maximum is required. No global completeness, divergence, pressure, derivative-decay or integrability premise is used.

## Proof

The strict inequality (1) and nonnegativity give a positive value m on the upper ray. Continuity at the vertex and uniform decay at infinity give 0<rho<R0 such that W<m/2 for r<rho or r>R0. The continuous function on the compact annular sector rho<=r<=R0 attains a maximum M>=m. This is a global maximum. Equation (1) implies M>sup_r W(r,theta1), so no maximum is on the lower ray or vertex.

At an interior maximum differentiability gives grad W=0 and (2) gives equality in (3). At an upper-ray maximum z0, the unique local b-trajectory z(t) with z(0)=z0 has angular derivative b(z0).e_theta/|z0|>0. Consequently z(t) lies inside D for all sufficiently small negative t; its radius remains positive. Maximality gives W(z(t))<=W(z0). Dividing the nonpositive numerator by t<0 and taking t upward to zero gives b.grad W(z0)>=0. Equation (2) now gives (3). The stated contradictions follow directly.

Equivalently, one can use one-sided directional derivatives at the upper boundary. The local trajectory proof records explicitly which time direction enters D. The opposite boundary orientation would not yield the required sign.

## Exact application to Zhang Proposition 2.3(i)

In the actual arXiv:2306.09515v5 manuscript, pages20-23, the upper-half-plane Boussinesq profiles satisfy

    (V+(1-alpha)z).grad W+W-partial_x(H^2)=0,
    W=partial_y V1-partial_x V2.

Take b=V+(1-alpha)z, S=partial_x(H^2), R=0. The source assumes V1<0 and V2>0 throughout the open first quadrant. Hence on either sector ray

    b.e_theta=-V1 sin theta+V2 cos theta>0.

The radial similarity drift contributes zero to this expression. Its tail assumption W=r^(-1/(1-alpha))f with bounded f and alpha<0 gives uniform decay on the sector. Oddness of V1 in x implies partial_y V1(0,0)=0, and the boundary condition V2(x,0)=0 implies partial_x V2(0,0)=0. Thus W(0)=0. The source explicitly supplies nonnegativity, (1), and W(z0)>partial_x(H^2)(z0) at a global maximum. Every premise of the theorem holds, so no such exact profile exists.

This verifies that exact-profile implication without relying on the source's signed large-power integral limits. Exclusion of an asymptotically self-similar scenario requires a separate proof that its exact limit satisfies these premises. The dimension-reduction and compactness steps producing such a limit are not audited here.

## Scope and evidence

The source parameter conditions are alpha<0, 0<beta<-alpha and 2beta=1-alpha. Therefore alpha<-1 and its meridional similarity length exponent is 1-alpha>2. The upper-half-plane forcing, boundary, signs and sector-maximality assumptions differ from the campaign's whole-space Euler hypotheses. This is not a counterexample or a Liouville theorem for 2/5<c_l<1/2, and no arbitrary-rotation extension follows.

The complete submitted LIT85 proof was independently reconstructed. The actual Zhang proposition, its proof and related remarks were read from the retained manuscript. The full seven-page Chen-Hou clarification was also read. Source bytes, extracts and scope audit are retained in [the source review](auditor_proofs/reviews/chen_hou_zhang_20261103/PROOF.md). Only elementary local C1 ODE existence and constrained differentiation enter this proof. No computation is needed for the mathematical assertion.
