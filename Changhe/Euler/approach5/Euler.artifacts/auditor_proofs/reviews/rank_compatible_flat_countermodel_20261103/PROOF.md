# Rank-compatible common-flat fields and the missing pressure equation

## 1. Exact scope

Fix0<c<1/2 and any finite real omega. Set p=(1-c)/c>1, a=1-2c>0, b=2(1-c), q=b/a>2, tau=omega/c, J(x,y,z)=(-y,x,0), A=cI-omega J and X=Ax. There exist C-infinity fields V,P2 on a neighborhood G of x0=(1,0,1/c) satisfying every first-order identity listed in Section4, with W=curl V, k=X.V and S=P2-|V|²/2. The set {W!=0,k!=0} is dense. All jets of V,W,k,S,P2 vanish at x0, but x0 is in the support of W. On its infinitely many vortical components S=D_C k^q, with negative D_C whose magnitudes grow faster than every inverse power of distance to x0.

These fields fail both Poisson pressure and full similarity momentum. They disprove only the inference that smoothness, dense vorticity and the listed rank and transport identities bound those constants. They are not Euler profiles, actual asymptotic tails, or counterexamples to the campaign conjecture. Section7 additionally excludes the whole flat vertical-shear ansatz once Poisson and rank are both imposed.

## 2. Smooth gluing with independently diverging component constants

Let beta(t)=exp(4-1/(t(1-t))) for0<t<1 and zero otherwise. Every positive real power beta^r has a smooth zero extension with all endpoint derivatives zero: differentiation produces that exponential times rational functions, and its exponential decay dominates each endpoint pole. In particular beta(1/2)=1.

For j>=1 put ell_j=2^(-j-1), I_j=(ell_j,2ell_j), alpha_j=exp(-4^j). On I_j define

    h(theta)=alpha_j beta((theta-ell_j)/ell_j),
    H(theta)=alpha_j² beta((theta-ell_j)/ell_j)^q.

Reflect both evenly, and give them value zero at0 and every dyadic endpoint. The positive intervals fill(-1/2,1/2) except for these endpoints. At each nonzero interface all one-sided derivatives are zero. For every fixed derivative order n,

    |h^(n)|<=C_n alpha_j ell_j^(-n),
    |H^(n)|<=C'_n alpha_j² ell_j^(-n).

Each bound is o(ell_j^m) for every finite m. Inductively, the difference quotient of the continuous extension of the n-th derivative is zero at0. Thus the extensions are C-infinity and infinitely flat there. On each positive or reflected band,

    H=alpha_j^(2-q) h^q.                              (1)

The coefficient tends to infinity because q>2. Smooth gluing places no matching condition on these constants at the common infinitely flat interfaces.

## 3. Rotating local lift and ambient flatness

Use local cylindrical coordinates rho>0, phi about0 and z>0, and define

    theta=phi+tau log rho, u=rho^(-p)h(theta), V=u e3,
    k=czu, S=-(cz)^q rho^(-pq)H(theta), P2=u²/2+S.       (2)

Choose G as the image of a sufficiently small product box in(log rho,theta,z) about(0,0,1/c). This is a smooth coordinate chart, since rho=exp(s) and phi=theta-tau s. The box can depend on omega; the result is for each finite omega, not a uniform-size neighborhood.

The flow exp(tA) sends rho to exp(ct)rho, phi to phi-omega t and z to exp(ct)z. It fixes theta. Therefore, as long as an orbit segment remains in G,

    X.grad V=-(1-c)V-omega JV,
    X.grad k=-ak, X.grad S=-bS, X.grad P2=-bP2.         (3)

Here JV=0 and cq(1-p)=-aq=-b. Also X.V=czu, exactly as defined. Every derivative of h,H is zero on theta=0 and on each interface. Applying the ordinary Cartesian chain and product rules to(2) proves ambient infinite flatness of V,k,S,P2 there. The same follows for every derivative of W=curl V. This is not merely flatness along the angular curve.

## 4. All first-order identities and dense support

V is vertical and independent of z, so

    div V=0, (V.grad)V=0, W=(u_y,-u_x,0), V.W=0,
    W.grad u=W.grad z=0.

Moreover

    u_rho=rho^(-p-1)(-ph+tau h'),
    u_phi/rho=rho^(-p-1)h'.

If h>0 these two derivatives cannot both vanish: h'=0 leaves -ph nonzero. At a zero of h both are zero. Thus {W!=0}={u>0}={k!=0}, a dense union of connected product bands. On the j-th band(1) yields

    S=-alpha_j^(2-q)k^q.                              (4)

Consequently W.grad k=W.grad S=0, k grad S=qS grad k and grad k cross grad S=0. At interfaces all jets vanish, so these identities continue everywhere.

For completeness, the vector identities follow directly without invoking rank. In Cartesian coordinates

    X=(cx+omega y,cy-omega x,cz),
    X cross W=(cz u_x,cz u_y,cp u),
    grad k=(cz u_x,cz u_y,cu).

The third component of the cross product uses the horizontal part of(3). Since cp-a=c,

    grad k=X cross W-aV, grad k cross V=kW.             (5)

Equations(3)-(5), divergence, helicity and both vorticity transport identities are exactly the proposed first-order system. Each component constant in(4) is a single negative number; connectedness of the product band is explicit.

## 5. Exact low-pressure sequence

Let theta_j=3ell_j/2 and x_j=(cos theta_j,sin theta_j,1/c). For large j these points belong to G and distinct bands. Since beta(1/2)=1,

    V(x_j)=alpha_j e3, k(x_j)=alpha_j,
    S(x_j)=-alpha_j², P2(x_j)=-alpha_j²/2,
    -D_Cj=exp((q-2)4^j).

Their distance to x0 is2sin(theta_j/2), comparable to ell_j. Thus for every finite m>=0,

    log((-D_Cj)|x_j-x0|^m)=(q-2)4^j-O_m(j)->infinity.

This proves the superpolynomial divergence and the exact pressure-to-energy ratios. Neither an open irrotational patch nor a nonflat interface is used.

## 6. Pressure and momentum fail exactly

The matrix DV has only its third row potentially nonzero and its third column zero, hence(DV)²=0. Poisson would require Delta P2=0. Fix any horizontal point with u>0 in a band and put d=alpha_j^(2-q)>0. Along its vertical interval,

    P2=u²/2-dc^q z^q u^q,
    Delta P2=A0-B0z^q-C0z^(q-2),
    C0=dc^q q(q-1)u^q>0.

Here A0 and B0 depend only on the fixed horizontal point. If this vanished on an interval, differentiation and multiplication by z^(3-q) would give qB0 z²+(q-2)C0=0 identically. The constant term is nonzero. This is impossible for every real q>2, including integer values. Any ball meeting u>0 contains such a horizontal point and vertical interval. Thus Poisson fails as a local PDE on every such ball, although it vanishes on the flat sheets and may vanish at isolated other points.

In full similarity momentum, the linear term, X transport, nonlinear transport and rotation sum to zero by(3) and(V.grad)V=0. The residual is therefore grad P2. At every u>0 point,

    partial_z P2=qS/z<0.

It fails everywhere in the nonzero region. Keeping only first-order tail identities has discarded a genuine equation.

## 7. A stronger obstruction to repairing this vertical-shear ansatz

Here is an independent general statement. Let G be a connected neighborhood in rho,z>0, V=u(x,y)e3 be smooth with the same twisted homogeneity X.grad V=-(1-c)V, and let P2 be smooth. Suppose k=czu, S=P2-u²/2 satisfy k grad S=qS grad k and Delta P2=0. If x0 is a supported infinite-order zero of u, then V=0 on G. In particular, no nontrivial supported common-flat example of this vertical form can satisfy both rank and Poisson.

On any sufficiently small connected ball where u!=0, k has fixed nonzero sign. The rank identity implies

    grad(S/|k|^q)=0,

so S=D|k|^q for a constant D there. Along any vertical interval in this ball, the preceding calculation applies with an arbitrary real D. Distinct powers of z force D=0, since q(q-1)(q-2)|u|^q is nonzero. Hence P2=u²/2 on the entire open set {u!=0}.

Take points of this open set converging to x0. Every derivative of P2 equals the corresponding derivative of u²/2 at those points. Smoothness and infinite flatness of u imply that every derivative of P2 at x0 is zero. A harmonic function with all jets zero is identically zero on a connected domain: on a ball use its convergent harmonic Taylor expansion, obtained from the Poisson formula on a smaller concentric sphere, then continue through overlapping balls. Thus P2=0 on G. The equality P2=u²/2 on {u!=0} makes that set empty.

This argument does not assume dense vorticity or negative component constants. It uses only a supported infinitely flat velocity zero, the vertical geometry, rank and Poisson. It does not extend to general vector fields, for which tr((DV)²) need not vanish.

## 8. Dependencies and conclusion

The seven source sections were read completely and copied with a hash. All identities above were reconstructed independently. The all-rotation local shear construction A1338-A1342 explains the geometry, but the proof here includes its required differentiations. No numerical computation, formal build or new model client was needed.

The complementary examples have distinct missing equations: LIT227 retains Poisson and fails rank; LIT230 retains full local momentum and fails rank; LIT232 retains rank and fails Poisson and momentum. None satisfies the complete actual-tail system. The unrestricted common-flat case and the arbitrary-helicity whole-space conjecture remain open. Section7 is an additional independent result to compare through the existing configured model agents; provider runtime is unattested.
