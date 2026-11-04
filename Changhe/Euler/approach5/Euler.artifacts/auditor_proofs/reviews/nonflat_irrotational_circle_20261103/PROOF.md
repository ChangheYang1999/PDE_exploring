# Exact nonflat irrotational carrier circles: independent audit

Status: CONFIRMED in A440 after independent hand reconstruction and focused configured-model review. This audits LIT91 and the explicit family in LIT92. These are local Euler solutions outside the global target class.

## 1. Exact statement, including all parameters

Fix an integer k>=1, 0<c<1/2, a real omega, R>0 and C!=0. Write

    a=1-2c, kappa=1+c, d=3c,
    gamma=kappa/k, h=gamma/2, t=c+h,
    D=2c+gamma, b=h R^2, S=r^2-R^2.

On the open subset r=sqrt(x^2+y^2)>0 of R3 define, in the orthonormal cylindrical basis,

    F(r)=-t r+b/r, G(r)=-C S^(k+1)/(2(k+1)),
    U=F e_r+(D z+G)e_z,
    P=-t(t-1)r^2/2-a b log r-b^2/(2r^2)-D(1+D)z^2/2.       (1)

These fields are smooth on this domain and solve the full rotating Euler profile equation, with div U=0. Their vorticity and helicity are

    W=C r S^k e_theta, U.W=0.                                  (2)

For omega!=0 the circle r=R,z=0 is a complete periodic carrier orbit with least period 2pi/|omega|. Its uniform angular probability is ergodic under the full flow, has time-one entropy zero, and has backward ambient Lyapunov spectrum

    (gamma,0,-d-gamma).                                        (3)

Along the circle, D^j W=0 for j<k and

    D^k W[e_r,...,e_r]=k! C R(2R)^k e_theta!=0.                (4)

For k=1, DW has rank one and image equal to the carrier line; consequently D(B cross W)=0. For k>=2 this last derivative vanishes because DW=0. Formula (3) realizes the number kappa/k in the LIT92 necessary spectral list. The k=1 member is exactly LIT91, with spectrum (kappa,0,-d-kappa).

At omega=0, (1)-(2) still solve Euler, but every point on the circle is a carrier equilibrium. The nonstationary measure claim requires omega!=0. The family is not an entire smooth or decaying solution and has no entire sublinear extension as a whole tubular germ. No existence conclusion for the campaign follows.

## 2. Divergence and curl in Cartesian meaning

The horizontal velocity is (-t+b/r^2)(x,y), so it is a smooth Cartesian vector field on r>0. Cylindrical divergence gives

    div U=(rF)'/r+D=-2t+D=0.

The curl has only its azimuthal component,

    W_theta=partial_z U_r-partial_r U_z=-G'=C rS^k.

This proves (2); U has no azimuthal component. For a rotation-equivariant vector field, differentiating U(R_theta y)=R_theta U(y) in theta at zero gives

    (Jy).grad U=JU.

Thus -(omega Jy).grad U+omega JU=0 in Cartesian coordinates. This step includes differentiation of the moving cylindrical basis. It is not obtained by treating cylindrical components as three scalar Cartesian components.

The carrier components are

    B_r=cr+F=-h r+b/r=-h S/r,
    B_theta=-omega r,
    B_z=(c+D)z+G=(d+gamma)z+G.                                (5)

The meridional acceleration can therefore be checked with X=cy+U; its components agree with those of B and it has no azimuthal component.

## 3. Complete momentum calculation

Since F'=-t-b/r^2, direct expansion gives

    (1-c)F+B_r F'
      =t(t-1)r+a b/r-b^2/r^3.                                 (6)

For example, the r coefficient is -t(1-c)+ht=t(t-1), because t=c+h. The r^(-1) coefficient is b(1-c+h-t)=a b. The pressure derivative P_r is the negative of (6). The azimuthal residual is zero by the exact rotation cancellation and P_theta=0.

For the vertical component,

    (1-c)(Dz+G)+B_r G'+((c+D)z+G)D
      =D(1+D)z+(1-c+D)G+B_r G'.                               (7)

Here G'=-C r S^k and hence

    B_r G'=h C S^(k+1)=-2h(k+1)G,
    1-c+D=1+c+gamma=2h(k+1).

The last two terms in (7) cancel. P_z=-D(1+D)z cancels the remaining term. All three momentum components, as well as divergence, have now been checked. There is no pressure normalization premise: (1) is the specified local pressure. An additive constant is harmless.

For k=1, t=(1+3c)/2 and t(t-1)/2=(9c^2-1)/8, recovering the exact LIT91 pressure, including its logarithm. Omitting -a b log r creates the nonzero radial residual a b/r. This is a useful negative control for the supplementary checker.

As a separate curl-level consistency test, q=W_theta/r=C S^k satisfies

    Bq=B_r q'=-2hk q=-kappa q.

It does not replace the full momentum calculation above.

## 4. Vanishing order and complete compact orbit

At r=R,z=0, S=0, G=G'=0, and B_r=B_z=0. Equation (5) gives theta'=-omega. The least positive period is 2pi/|omega| when omega!=0. Along any point of this circle, write a Cartesian displacement in the fixed basis (e_r,e_theta,e_z) at that point. The scalar S has first derivative 2R in the e_r direction and zero in the other directions. Since W=C r S^k e_theta, every derivative of order below k vanishes and its homogeneous degree-k term is

    C R(2R)^k (displacement.e_r)^k e_theta.

This proves the ambient derivative formula (4). Derivatives of r and of the basis multiply a vanishing lower power and do not change this first nonzero term. When k=1, the other columns of DW vanish, so its image is R e_theta=R B for nonzero omega. At W=0,

    D(B cross W)v=B cross DW(v),

which is therefore zero; it is also zero when k>=2.

In cylindrical coordinate variations around the orbit,

    partial_r B_r=-2h=-gamma,
    partial_z B_z=d+gamma,
    partial_r B_z=G'(R)=0, partial_z B_r=0,
    partial_r(theta')=partial_z(theta')=0.

Thus the forward variational rates are (-gamma,0,d+gamma). The coordinate-to-Cartesian linear map along the circle is periodic, bounded and has bounded inverse; its angular scaling is the fixed positive number R. Therefore it changes no Lyapunov exponent. Reversing time gives (3). Equivalently the forward period multipliers are exp(-gamma T),1,exp((d+gamma)T). More directly, put Q(s)=exp(-omega s J) and M=cI+DU(p0)=diag(-gamma,0,d+gamma) in the initial orthonormal frame. Equivariance gives DB(Q(s)p0)=Q(s)(M-omega J)Q(s)^T. Differentiating Q(s)exp(sM) proves the exact Cartesian formula D Phi_s(p0)=Q(s)exp(sM). In contrast, the pointwise radial-angular block DB(p0) has characteristic polynomial zeta^2+gamma zeta+omega^2 and does not have exponents -gamma and0 when omega!=0.

Invariance under the full carrier flow on the circle is invariance under all angular rotations. The uniform probability is full-flow ergodic. Its time-one map is a rotation, possibly rational; no time-one ergodicity is asserted. A partition into finitely many intervals has only linearly many endpoints after n iterates, so its entropy rate is zero. Such interval partitions generate the Borel sigma algebra under refinement, proving metric entropy zero.

## 5. Exact global failures and the distinction between germs and jets

Because b>0, F behaves as b/r near the axis. Its Cartesian horizontal vector has magnitude asymptotic to b/r, so it has no continuous, hence no C2, extension there. The b/r contribution is a line source, with limiting flux 2pi b per unit axial length through small cylinders; b=gamma R^2/2 is forced by B_r(R)=0 within this ansatz. At fixed r, U_z grows linearly in z. At z=0 it grows as a nonzero constant times r^(2k+2). Thus U is not uniformly sublinear and does not tend to zero at infinity.

The radial carrier equation integrates exactly:

    r(s)^2=R^2+(r(0)^2-R^2)exp(-gamma s).

For 0<r(0)<R it reaches r=0 at the finite negative time

    s=-(1/gamma) log(R^2/(R^2-r(0)^2)).

Every trajectory starting at r>=R is complete in both time directions: the displayed radius stays positive and finite on finite time intervals, and z solves a linear ODE with continuous forcing G(r(s)). A trajectory with 0<r<R is complete in forward B-time but reaches the axis at the stated finite backward B-time. Compact-orbit Lyapunov theory does not require completeness of the surrounding punctured domain.

A frozen-vorticity trajectory keeps r,z fixed and has angular speed C S^k. For every fixed r!=R it is a nonconstant closed circle with period 2pi/(|C| |S|^k). Such circles are contained in every full sufficiently small tubular neighborhood of the carrier circle. For a global C2 velocity and C1 pressure the profile equation makes grad P C1, hence P C2, meeting A014's written regularity. The confirmed A014 vortex-period theorem forbids a nonconstant closed frozen-vorticity orbit in a global C2 uniformly sublinear Euler profile with 0<c<1/2. It follows that no entire profile in that class can agree with (1) on a whole such tubular neighborhood, regardless of changes elsewhere.

This use of A014 alone does not exclude a finite jet, since matching finitely many derivatives need not preserve any closed vortex line. A separate A413 consequence in in the team records is proposed to exclude these particular finite jets in the globally helicity-free class: it additionally uses the differentiated rank identity on closure{W!=0}. That proposal is pending focused review and is not needed to establish the local family or the whole-germ obstruction. Its companion proposed harmonic repair changes the higher velocity jet while preserving U, DU and W at the chosen point and passes the rank test; neither proposal is a spectral exclusion. Neither argument excludes every possible local realization of the same Lyapunov spectrum, and neither constructs a global profile.

## 6. Evidence and scope of this audit

Sections2-5 are independent hand calculations, completed before running any checker. They treat all integers k>=1 and all real omega, with the nonstationary claim restricted to omega!=0. The supplied k=1 symbolic checker was copied into this agent and passed every required identity and the missing-log negative control in the real interval 2026-11-03T02:57:34.307782Z to 02:57:35.425585Z. Its exact residual test is supplementary. In particular its named azimuthal_rotation_cancellation entry evaluates the tautology -omega F+omega F and supplies no evidence. The actual rotation check is the Cartesian equivariance calculation in Section2; omitting omega JU leaves the nonzero residual -omega JU. The focused review independently reconstructed full Cartesian residuals and this negative control. Its computational outputs are corroboration, not a substitute for the written all-parameter proof. The precise question, expected identities and missing-log negative control are in the team records. The source proofs and immutable hashes are retained beside it.

Dependencies: elementary cylindrical differentiation and ODEs; A014 only for the global whole-germ obstruction. LIT90/LIT92 supply the context for calling the rate exceptional or resonant, not the existence proof. The current conjecture remains open.
