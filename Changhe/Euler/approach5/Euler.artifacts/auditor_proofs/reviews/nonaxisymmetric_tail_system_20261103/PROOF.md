# Exact angular equations for a globally degenerate twisted tail

Status: CONFIRMED as A557 after complete source and independent proof postreads. This is an exact reduction, not a nonexistence theorem.

## 1. Statement and scope

Let 1/3<c<1/2, p=(1-c)/c in (1,2), a=1-2c, t=omega/c for any finite real omega, Jx=(-x2,x1,0), A=cI-omega J and D=R3 minus {0}. Suppose V is locally Lipschitz on D, W=curl V has a continuous representative and P2 is C1 on D. Assume

    V(exp(vA)x)=exp(-(1-c)v) exp(-omega vJ)V(x),
    P2(exp(vA)x)=exp(-2(1-c)v)P2(x),
    div V=0, Ax cross W=aV,
    -Delta P2=partial_i partial_j(V_i V_j),
    div(SW)=0, S=P2-|V|^2/2.                       (1)

Divergence and Poisson equations are distributional. No extension through the spatial origin is assumed.

Put z=cos(theta), s=sin(theta), w=1-z^2, chi=phi+t log r, alpha=1/w+t^2 and d=(2-p)t. There are 2pi-periodic locally Lipschitz functions F,H and a C1 function u on the angular cylinder such that

    V=r^-p[tF e_r+(H/s)e_theta+(F/s)e_phi],
    P2=r^-2p u, e=(t^2 F^2+(H^2+F^2)/w)/2, h=u-e.   (2)

The exact system is

    H_z=alpha F_chi+dF,
    2p h(F_z+H_chi/w)-(p-1)(F h_z+H h_chi/w)=0,
    (w u_z)_z+alpha u_chichi+t(1-4p)u_chi
                       +2p(2p-1)u=-tr(M^2),        (3)

with M given in Section 3. The first two equations hold almost everywhere, the third distributionally. Conversely (2)-(3) imply (1) if the reconstructed Cartesian fields extend with precisely the stated regularity across the polar axis, and their actual curl is continuous there.

If omega is nonzero, every nonzero V satisfying (1) has both strictly positive and strictly negative azimuthal components on every centered sphere. On each simply connected angular patch where h never vanishes there is a C1 local potential f with locally Lipschitz first derivatives satisfying

    F=b f_chi, H=-w b f_z, b=|h|^beta,
    beta=(p-1)/(2p),
    (w b f_z)_z+partial_chi(alpha b f_chi)
                                      +d b f_chi=0. (4)

No global single-valued potential, nodal transmission, tail classification or profile exclusion follows from this statement.

## 2. Homogeneity and divergence

The angle chi is unchanged by x -> exp(vA)x: the radius multiplies by exp(cv) and the physical azimuth decreases by omega v. Vector components in the spherical frame therefore have radial factor r^-p and arguments (z,chi). The equation Ax cross W=aV implies Ax.V=0. Since Ax=r(c e_r-omega s e_phi), the radial component equals t s times the azimuthal component. Define F=s v_phi and H=s v_theta to obtain (2).

The radial derivative of an angular function is t/r times its chi derivative; the polar derivative is -s times its z derivative. The divergence is

    div V=r^(-p-1)[(2-p)tF+t^2F_chi-H_z+F_chi/w].

This proves the first equation of (3). Boundedness of the Cartesian field on each sphere gives F,H=O(s) at both poles, uniformly in chi. It does not give O(w) in the nonsymmetric case. The converse must check Cartesian extension rather than impose an unjustified stronger scalar pole rule.

## 3. Actual derivatives, curl and pressure

In the orthonormal spherical frame, M=r^(p+1)DV has entries

    [ -ptF+t^2F_chi,    -tsF_z-H/s,                 (tF_chi-F)/s;
      (-pH+tH_chi)/s,   (p-1)tF-alpha F_chi-zH/w,  (H_chi-zF)/w;
      (-pF+tF_chi)/s,   -F_z-zF/w,                F_chi/w+tF+zH/w ]. (5)

For example, the middle entry before incompressibility is -H_z-zH/w+tF. The trace is zero. Antisymmetrizing gives the actual curl

    W=r^(-p-1)[(-F_z-H_chi/w)e_r
          +(p-1)F e_theta/s
          +(-(p-1)H/s+tH_chi/s+tsF_z)e_phi].        (6)

Taking the cross product with Ax in (6) gives c(p-1)V=aV using the first equation of (3). Thus the converse has the full vector degeneracy identity, not just its radial scalar consequence.

For a locally Lipschitz divergence-free V,

    partial_i partial_j(V_i V_j)=tr((DV)^2)

holds distributionally. Local mollification preserves divergence and makes the smooth identity applicable; gradients converge in every finite local Lq space and their products in local L1. This proves the identity without pointwise second derivatives of V.

The radial part of the scalar Laplacian on r^-2p u is the operator

    (-2p+t partial_chi)(1-2p+t partial_chi),

while the spherical part is (w partial_z)_z+partial_chichi/w. Their sum is exactly the pressure operator in (3), including the drift t(1-4p). The computation passes to distributional tests for C1 u.

There is no lost axis distribution in the converse. N=DV V+grad P2 is locally bounded and div N=0 off the axis. A cutoff excluding a tube of radius epsilon in a fixed compact set has gradient L1 norm O(epsilon); its contribution against N tends to zero. Thus div N=0 across the axis. Divergence of V is an ordinary almost-everywhere derivative at the stipulated regularity. The continuous vector identity extends across the axis. Since W is an actual curl, div W=0; multiplication by locally Lipschitz S gives div(SW)=W.grad S by mollifying S and using finite-Lq gradient convergence. Hence the scalar equation also extends.

## 4. Scalar compatibility and projected vortex direction

The spherical gradient of S=r^-2p h is r^(-2p-1) times

    (-2p h+t h_chi, -s h_z, h_chi/s).

Its dot product with (6) cancels both mixed t terms and gives the second equation of (3). Along a W-curve the two angular velocities are

    z'=-(p-1)r^(-p-2)F,
    chi'=-(p-1)r^(-p-2)H/w.

Consequently the projected direction is T=(F,H/w), up to a nonzero common scalar, and the equation becomes

    T.grad h=beta^(-1) h div T,
    div T=F_z+H_chi/w.                              (7)

This exact two-dimensional identity includes all angular modes.

## 5. Flux and local potential

Divergence zero makes the flux through any two centered spheres equal. Homogeneity makes it r^(2-p) times the unit-sphere flux. Since p<2, that flux is zero. When t is nonzero it follows that

    integral_-1^1 integral_0^(2pi) F(z,chi) dchi dz=0.

A continuous F with one weak sign would vanish identically. The first equation of (3) would then give H_z=0 almost everywhere. Local Lipschitz regularity and continuity make H independent of z at every chi; H=O(s) at the poles gives H=0. Thus a nonzero V requires both strict signs, transferred to every sphere by the twist. The test is consistent with the A514 kinematic tail and alone excludes nothing in that sign-changing class.

Where h is nonzero, b=|h|^beta and 1/b are locally Lipschitz. The weak chain rule in (7) gives

    partial_z(F/b)+partial_chi(H/(wb))=0.

The locally Lipschitz one-form -(H/(wb))dz+(F/b)dchi is closed. On a simply connected patch, path integration, justified first by local mollification, gives a C1 potential with locally Lipschitz derivatives. Substitution into the divergence equation proves (4). Its principal matrix is diag(wb,alpha b), bounded and positive definite on each compact subset of the patch. Zeros of h and possible nonzero periods prevent any automatic global maximum argument.

## 6. Dependencies and verification

The complete LIT143 source was read and all formulas above were independently derived. The proofs need no computation, imported regularity theorem or finite mode truncation. For a full target globally helicity-free profile with natural bounds, A530-A531 and A533-A539 supply the pressure, scalar compatibility and regularity; an additional global E=grad((Ax).V)=0 assumption supplies Ax cross W=aV. A534 only gives a proper open cone in one case, and does not supply this global assumption.

The existing configured-model in the team records agent comparison is continued through the shared files, including coordinator Note59's use of this exact angular system. No new client or agent is used and no focused new reply is presumed.
