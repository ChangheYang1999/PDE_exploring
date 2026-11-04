# Global cutoff swirls and the exact pressure information they omit

## 1. Exact kinematic statement

Fix0<c<1/2, omega!=0, p=(1-c)/c>1, a=1-2c, b=2-2c, q=b/a=2p/(p-1)>2, Jx=e3 cross x, A=cI-omega J and X=Ax. Let eta0(t)=exp(-1/t) for t>0 and zero otherwise, and

    chi(s)=eta0(1/4-s²)/[eta0(1/4-s²)+eta0(s²-1/16)].

The denominator is positive. Thus chi=1 for |s|<=1/4, chi>0 for |s|<1/2, and chi=0 for |s|>=1/2, flat at both endpoints. With spherical coordinates r,theta,phi and sigma=-sign omega, define on R3 minus{0}

    V=r^(-p) sigma chi(cos theta)e_phi,
    P2=|V|²/2, S=P2-|V|²/2=0,
    W=curl V, k=X.V.

These are smooth globally away from the origin, including the axis because V vanishes on polar neighborhoods. They satisfy the listed divergence, twisted homogeneity, helicity, scalar transport, rank and irrotational-patch pressure identities, but not the pressure Poisson equation. They have one connected positive-k vortical cone and supported common flat points on its boundary. No pressure satisfying rank can repair the Poisson failure. This is a countermodel to the reduced list, not a full Euler profile or a solution of the complete necessary tail system.

## 2. Curl, homogeneity and the cone

Ordinary homogeneity of degree -p and rotation covariance give

    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x).

The purely azimuthal, rotation-invariant field is divergence free. Writing h(theta)=sigma chi(cos theta), differentiation gives

    W=r^(-p-1)[(h'+cot(theta)h)e_r+(p-1)h e_theta],
    V.W=0,
    k=|omega| r^(1-p)sin(theta)chi(cos theta).

Since p>1, W!=0 precisely on C={r>0,pi/3<theta<2pi/3}, which is connected and is also {k>0}. Every derivative of V,W,k vanishes on its boundary. Direct differentiation of X.V, or the integrated homogeneity, gives grad k=X cross W-aV and X.grad k=-ak. The remaining S transport and rank identities hold because S=0. On every open irrotational patch V=P2=0, so the harmonic-pressure requirement there holds. All supported W zeros are boundary points where V,DV,W,DW,P2,S,k vanish, satisfying the listed pointwise pressure sign conditions.

## 3. Periods and weighted fluxes

On an angular coordinate chart take Phi=-phi/omega. Then

    V/k=grad Phi=-e_phi/(omega rho), X.grad Phi=1,
    integral_(latitude circle)(V/k).dx=-2pi/omega.

Thus the local potential cannot be made single valued on the entire vortical cone. The sphere-tangent projected field is just V, which travels along latitude circles and preserves area. Also V.grad k=0, while X.(W cross V)=a|V|². Hence the two terms in the k-identity cancel exactly. Every smooth F(k,S)V is divergence free and tangent to the same circles. Those particular fluxes supply no contradiction on this model.

The point x0=(sqrt(3)/2,0,1/2) is in supp W, V and S vanish there to infinite order, and positive-k points approach it. The reduced identities therefore do not by themselves exclude the common-flat configuration.

## 4. Full Poisson residual

For a cylindrical azimuthal field U(rho,z)e_phi, the derivative matrix in the orthonormal cylindrical basis is

    [0, -U/rho, 0; U_rho, 0, U_z; 0, 0, 0].

Thus tr((DV)^2)=-2U U_rho/rho. On the cutoff plateau U=sigma r^(-p), so this is2p r^(-2p-2). The radial formula Delta r^lambda=lambda(lambda+1)r^(lambda-2) in three dimensions gives

    -Delta P2=-p(2p-1)r^(-2p-2),
    -Delta P2-tr((DV)^2)=-p(2p+1)r^(-2p-2)!=0.

No numerical residual is used. This is an exact failure on an open set for every p>1.

## 5. No alternative rank-compatible pressure

Any alternative scalar Stilde=Ptilde-|V|²/2 satisfying rank has Stilde=D k^q on connected C, for a single real constant D. On the plateau,

    Ptilde=r^(-2p)[1/2+D|omega|^q sin(theta)^q].

Put lambda=2p(2p-1). Direct angular differentiation yields

    Delta(r^(-2p)sin(theta)^q)
     =r^(-2p-2)[q² sin(theta)^(q-2)
                       +(lambda-q(q+1))sin(theta)^q].

Poisson would make D|omega|^q times the bracket equal the nonzero constant -p(2p+1) for all t=sin(theta) in (sqrt(15)/4,1). Therefore D!=0 and the bracket must be constant. Differentiating and dividing by q t^(q-3) would give

    q(q-2)+(lambda-q(q+1))t²=0

on an interval, impossible since q(q-2)>0. This excludes every such pressure, without translation invariance or an axisymmetric pole theorem. The current parent's scope sentence correctly distinguishes axial rotation symmetry from axial translation invariance; the earlier comparison with LIT234 does not apply.

## 6. The virial remark needs a correction

The parent's Section4 says an origin-centered virial identity would require div(V tensor V+P2I)=0. That necessity is false. The pressure Poisson equation and div V=0 already give div div T=0 for the symmetric tensor T=V tensor V+PI. Write F=div T. On any full ball B_r(y) in the smooth domain, test div F=0 with f=(r²-|x-y|²)/2 and integrate twice. Since f=0 on the boundary, D²f=-I and grad f=-(x-y),

    integral_(B_r(y))tr T=r integral_(dB_r(y))T_nn.

This is exactly A1472. It uses no equation F=0. For instance V=(x,-y,0), P=-|x|²/3 has div V=0 and -Delta P=tr((DV)^2)=2, but F=(x/3,y/3,-2z/3) is nonzero. The ball identity still holds. This polynomial example only checks the logical necessity claim; it is not a decaying tail.

## 7. Exact inner-boundary terms at the excluded origin

On an annulus epsilon<r<R where div F=0, use the same f=(R²-r²)/2. The outward annular normal at its inner sphere is -e_r. Integrating twice gives exactly

    integral_(epsilon<r<R)tr T
      =R integral_(dB_R)T_rr-epsilon integral_(dB_epsilon)T_rr
       -(R²-epsilon²)/2 integral_(dB_epsilon)F.e_r.

The last flux is independent of epsilon by div F=0. It must be retained unless a separate argument removes it. Thus an excluded origin is handled by an annular identity, not by inserting a stronger momentum equation.

For a global smooth twisted-homogeneous V of degree -p and P of degree -2p, F transforms as a vector of degree -(2p+1), with the same axial rotation. Rotation preserves a whole sphere and its radial normal, so its flux scales as epsilon^(1-2p). A constant flux with this scaling is zero for p>1. The inner stress term has size O(epsilon^(3-2p)). In the campaign range1<p<3/2 it tends to zero, and tr T is locally integrable at the origin. Therefore the ordinary origin-centered ball identity follows from Poisson alone in this exact global tail class.

## 8. Angular mean identity and its exponent range

The same annular calculation supplies the angular identity for every p>1, including p=3/2, without an origin integral. Put

    E0=integral_(S2)|V|², R0=integral_(S2)(V.theta)²,
    P0=integral_(S2)P, E_t=E0-R0.

Twisted homogeneity makes the corresponding sphere integrals exact radial powers, since the radial rotations disappear in the integral. With zero residual flux, Section7 gives

    E0+3P0=(3-2p)(P0+R0),
    2p P0+E0=(3-2p)R0,
    integral_(S2)S=-[(3p-2)R0+(p+1)E_t]/(2p).

For p!=3/2, integrate r^(2-2p) and cancel R^(3-2p)-epsilon^(3-2p). At p=3/2 the annular left side is (E0+3P0)log(R/epsilon) and the stress boundary difference is zero, yielding the same formula. Thus nonzero V has strictly negative mean S for every p>1. No helicity or rank identity is needed, only global smoothness, divergence, twisted homogeneity and Poisson. On1<p<3/2 this recovers A591; the annular version extends the mean identity beyond its pressure-uniqueness range.

This is an angular integral statement, not a pointwise pressure sign or a proof excluding positive-k components. The cutoff countermodel has S=0 and nonzero V, so the identity is another exact witness of its omitted Poisson equation.

## 9. Verdict and remaining class

All four current parent sections, the complete nested source and all nine independent sections were read. CO60's countermodel, noncompletion and period/flux obstruction are confirmed. Its necessity claim is valid only in the sense that the listed first-order reduced identities do not suffice: a proof must use some additional full-system information, such as Poisson. It does not rule out every argument stated in a different form. The Section4 virial necessity wording is refuted and replaced by Sections6-8. The global k=0 claim and unrestricted common-flat exclusion remain open. Existing configured model parent comparison is used; its nested extra consultation did not execute and runtime remains unattested. No computation or formal build was used.
