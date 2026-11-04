# Negative-gradient carrier germs with one additional compatible order

## 1. Statement and scope

Fix 0<c<1/2 and an integer n>=4. Set a=1-2c, b=2(1-c), eta=a/b, kappa=(b+1)/b and m=n-4. Define

    P=(1179m+4565)a^3+(3117m+11889)a^2+(2709m+10071)a+963m+3555,
    Q=(690m+3278)a^3+(1581m+7623)a^2+(1134m+5580)a+243m+1215,
    v^2=3(a+1)^2 P/(2Q), v>0.

All coefficients of P,Q are positive, so v is real and nonzero. On a sufficiently small neighborhood G of 0 let

    X=(cx-vz, cy, 1+vx+cz).

There exist real analytic H>0, phi and p1, with H(0)=1 and (H_x,H_y)(0)=(-v,0), such that, writing

    V=H^eta grad phi, W=curl V, E=|V|^2,
    P2=H+E/2, Z=(DV)V+grad P2,

one has the exact equations

    XH=-bH, Xphi=0, div V=0, -Delta P2=tr((DV)^2),
    Xp1=-(b+1)p1, W dot grad(p1-2V dot grad P2)=0,

and the finite residual condition

    R:=Delta p1+2tr(DV DZ)=O(|(x,y,z)|^(n+1)).       (1)

The common zero set of V and W is a single X-orbit arc through 0. Both fields have exact transverse order n-1; W is nonzero off the arc and its relative support is G. The residual has order at least n+1 transverse to every point of a smaller arc.

The rotation vector is (0,v,0). Indeed, with A=cI-[(0,v,0) cross], A(v,0,c)/(c^2+v^2)=e3, so X is the translate of Ax about an off-axis point. This chooses v as a function of c,n. The statement neither treats every prescribed rotation magnitude nor solves R=0 identically. It is a local analytic leading-system construction with finite next-scalar compatibility, not an Euler profile.

## 2. Explicit finite jets and the degree n-1 cancellation

On z=0 write w=x+iy, rho^2=x^2+y^2, g=-v, and gvec=(g,0). Set

    h33=b(b+c)+vg, t=-h33/2+eta g^2/6,
    T=diag(t-eta g^2/3,t),
    u=-(b+c)gvec+b(v,0),
    d=-(b+2c)u+T(v,0)-h33(v,0),
    A3=eta g^3(2eta+3)/36.

Prescribe the pressure section through degree three by

    h3=1+gx+(x,y)T(x,y)^T/2-rho^2(d1 x+d2 y)/8
         +(A3/6)Re(w^3).                         (2)

Transport fixes H_z=-b, H_zz=h33, H_Tz=u and grad_T H_zz=d at 0. The transverse Laplacian of (2) has constant term -h33 and linear term -d dot (x,y). These cancel the corresponding H_zz terms. Thus the full Delta H has no constant or linear term. The transverse restriction of

    B=3 Hess H+(eta/H) grad H tensor grad H

at 0 is 3t I2. Choose the leading potential phi=Re(w^n)/n on the section. Its Hessian is trace free, so all source residual degrees below n-1 vanish.

The degree n-1 source has just the frequencies n-1 and n-3. The lower coefficient is

    (n-1)[12A3-eta g^3(1+2eta/3)]=0.

The higher coefficient R0 is real because all jets are invariant under y to -y. Explicitly R0 is twice

    -3t(eta g+v)-(3/2)(n-1)d1
    +eta g(n-1)(-h33-g^2/2)-2nc(3u1-eta b g)
    +(3h33+eta b^2)v
    +[2eta(T gvec-bu)+eta^2(g^2+b^2)gvec]_1.

Since 2kappa-eta=(5-2c)/b>0 and g is nonzero, the real scalar

    C_n=-R0/[(2kappa-eta)g]

is well defined. Set

    p1=2V dot grad P2+C_n H^kappa phi.             (3)

The added scalar has degree n-1 Laplacian coefficient C_n(2kappa-eta)g, so it cancels the higher coefficient. This accounts for the entire homogeneous residual at that degree. At zero axial rotation there is no extra imaginary condition forcing the earlier positive-gradient choice.

## 3. All degree n coefficients

For exact leading-system solutions the product rule gives

    R=Delta(C_n H^kappa phi)
      +2H^eta[Hess phi:B+grad phi dot C_H]+R_cub,
    C_H=(2eta/H)Hess H grad H
        +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H
        +grad Delta H,
    R_cub=Delta(V dot grad E)+2tr(DV D((DV)V))+tr(DV Hess E).

The least order of R_cub is 3n-6>n. The exact pressure equation gives Delta H=O(rho^(2n-4)); its terms in C_H cannot affect degrees through n. Thus H through degree four and phi through degree n+2 determine every coefficient under review.

For completeness the following finite recurrence defines them and the high coefficient J without an unprinted fitted formula. Treat w and its conjugate wb as independent coefficient variables. For a transported scalar F of weight d0 define on the section

    T0=c(w partial_w+wb partial_wb),
    Nz(F)=-(d0+T0)F/(1+vx),
    Nzz(F)=[v partial_x F-(d0+c+T0)Nz(F)]/(1+vx),
    L(F)=4partial_w partial_wb F+Nzz(F),
    I(w^i wb^j)=w^(i+1)wb^(j+1)/[4(i+1)(j+1)].

These are obtained by differentiating XF=-d0F once in z, so they include the normal derivatives and mixed Hessians. Begin with (2); append -I applied to the degree-two part of L(h3) as the quartic trace, with zero free quartic harmonic. Start with w^n/(2n); successively subtract I of the degree n-1 and degree n parts of

    L(phi)+eta H^{-1} grad H dot grad phi.

Use these jets in the preceding residual formula. Its degree n holomorphic-half contribution is

    J w^n+K w^(n-1)wb+L0 w^(n-2)wb^2.             (4)

The real polynomial is this expression plus its conjugate. Terms can change the leading angular frequency by at most four, since the coefficients have degree at most two and there are at most two derivatives. The recurrence also directly checks that no other band remains. For n=4 the last monomial is real and its contribution doubles; the corresponding response doubles too.

The exact coefficient identities are

    K=v^2[-P/(96(a+1))+v^2 Q/(144(a+1)^3)],
    L0=v^4(2c-1)(5c-4)(6c-5)(n-1)/[96(c-1)^3].  (5)

The retained symbolic calculation uses symbolic c,n rather than interpolation at finitely many orders. Its rational identities are replayed and checked against imported indexed JSON. Positivity of imported numbers alone is not enough; agreement with the finite recurrence in (5) is checked separately. By the selected v^2, K=0 exactly.

## 4. The two remaining free coefficients are nondegenerate

Add alpha Re(w^(n+1))/(n+1) to the potential section and beta Re(w^4)/24 to the pressure section, recomputing their trace corrections using the leading equations. The pressure change contributes only the last band, with holomorphic-half coefficient 3(n-1)beta. This follows by contracting the two harmonic Hessians in 6 Hess(phi_leading):Hess(beta Re(w^4)/24); products with pressure gradients first affect a higher degree. Choose

    beta=-v^4(2c-1)(5c-4)(6c-5)/[288(c-1)^3].      (6)

For the potential change, the degree n source is exactly the previous degree n-1 computation with n replaced by n+1. Its lower band is zero by the same A3 identity. The high response is therefore

    Tstar=(C_n-C_(n+1))(2kappa-eta)g
         =-v[-228c^3+656c^2-612c+184+(20c-19)v^2]/[4(c-1)].

After substituting the selected v^2, the exact identity is

    Tstar/v=(11a+15)N/Q,
    N=m(90a^4-159a^3-906a^2-981a-324)
       +1134a^4+1759a^3-903a^2-2601a-1053.

For 0<a<1, the coefficient of m is strictly negative: replace 90a^4 by at most 90a^3. The part independent of m is at most

    1990a^2-2601a-1053 <= -611a-1053 < 0,

using a^4,a^3<=a^2 and a^2<=a. Thus Tstar<0. In particular

    alpha=-2J/Tstar                               (7)

is a finite real number. The high coefficient becomes J+alpha Tstar/2=0. The new alpha and beta have no joint contribution through degree n: their first mixed Hessian contraction has degree n+1. A harmonic potential term of degree n+2 contracts to zero with B_TT(0)=3t I and can be chosen zero. Equations (5)-(7) cancel every degree n coefficient. All coefficients through n now vanish.

## 5. Analytic realization without solving the full next equation

The analytic flow chart of X is a diffeomorphism near the section because X(0)=e3. In its inverse coordinates (s,x,y), set H=e^{-bs}h(x,y) and phi=f(x,y). The transport equations are then exact. Put

    F0=Delta phi+eta grad(log H) dot grad phi,
    E2s=Delta H+(1/2)|grad phi|^2 Delta(H^(2eta))
        +2grad(H^(2eta)) dot (Hess phi grad phi)
        +H^(2eta)|Hess phi|^2
        -eta H^(2eta)grad phi dot grad(grad(log H) dot grad phi)
        +tr((DV)^2).

Direct expansion gives Delta P2+tr((DV)^2)=E2s+H^(2eta)grad phi dot grad F0. Both F0 and E2s are second order in f,h. The apparent third derivatives of phi have canceled. On the section solve F0=0 for f_yy. At the center its coefficient is one. Substitution into E2s leaves a coefficient one for h_yy, because H=1 and grad phi=0 there. The remaining coefficients are analytic, and the implicit function theorem puts the system in analytic Cauchy normal form near that jet.

Choose analytic Cauchy values f,f_y,h,h_y on y=0 whose finite jets are the restrictions of the constructed section polynomials. The recurrences in Sections2-4 are exactly the finite compatibility equations of this normal form. Successive uniqueness of its formal Taylor coefficients therefore retains H through degree four and phi through degree n+2. Higher Cauchy coefficients can be chosen arbitrarily. The analytic Cauchy theorem supplies a genuine local solution; shrink the neighborhood to retain H>0. The scalar equations propagate from the section by their similarity weights, since the flow derivative is a positive dilation times a rotation. This gives exact divergence and pressure equations throughout G.

The leading transverse gradient of phi has norm rho^(n-1), while all remaining terms have higher order. It has just one zero on a sufficiently small section. Transport gives the single zero arc. Since XH=-bH is nonzero and Xphi=0, grad H and a nonzero grad phi cannot be parallel. The exact formula

    W=eta H^(eta-1) grad H cross grad phi

then proves the asserted common zero set, exact transverse orders and full relative support. It also gives X cross W=aV, W dot grad H=0 and W dot grad phi=0.

Finally V dot grad P2 has scalar weight b+1; H^kappa phi has the same weight. Thus (3) satisfies both scalar transport equations exactly. The residual R has scalar weight 3 because b+1+2c=3 and the tensor contraction has the same weight. Its section order n+1 therefore propagates along the arc. Smooth equivalence of the flow coordinates and Euclidean coordinates proves (1). At no stage is the residual assumed zero beyond the displayed finite order.

## 6. Audit evidence and limits

The entire submitted six-section proof, its sign checker, the sparse recurrence, all-band extraction, reduction and sign scripts, Cartesian checker and its helper functions were read. The all-band recurrence and exact coefficient certificate were replayed in this agent, passing in 104.05262109078467 actual seconds from 2026-11-03T21:14:35.157399+00:00 to 2026-11-03T21:16:19.210023+00:00 on CPU55, nice19, OMP1. All twelve rational identities vanished and no extra band remained. The source Cartesian check independently differentiates the original three-dimensional expression at the single algebraic point c=9/20,n=4; its passing result corroborates the general algebra but cannot by itself establish the all-n statement. The recurrence replay reuses the reviewed sparse engine and is not described as a second independent implementation.

The analytic Cauchy argument above, the normal-derivative recurrence and the strict sign inequalities provide the mathematical reasoning beyond the computational identities. No numerical root, sample or small residual is promoted to a proof. Source files and exact JSON data are hash-pinned in the team records. One source Cartesian output had absolute dependency prefixes; the retained copy removes only those prefixes and registers its original source hash and normalized hash. The mathematical entries are unchanged.

LIT296's earlier positive-gradient obstruction and this negative-gradient construction are compatible. This result confirms the importance of that earlier hypothesis; it does not refute the earlier theorem. Arbitrary prescribed rotation magnitude, vanishing of the full residual, extension to a global tail or a smooth decaying profile, and the unrestricted nonexistence conjecture remain OPEN. No pressure normalization at infinity or completeness of nonlinear characteristic flow is asserted.
