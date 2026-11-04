# Strain must dominate vorticity near the common flat orbit

## 1. Exact statement

Let 0<c<1/2 and omega be real. On R3 set Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b. Let x0 be nonzero and G a smooth X-flowbox about an orbit segment Gamma through x0. Suppose V and S are smooth on G and satisfy

    div V=0, W=curl V, k=X.V=0,
    X.grad V=-LV, X.grad S=-bS,
    grad k=X cross W-aV, W.grad S=0,
    P=S+|V|^2/2, -Delta P=tr((DV)^2).

Assume S<0 on G minus Gamma, S=0 on Gamma, and V,S vanish to infinite order at x0. All norms below are Euclidean or Frobenius. If mu>=0 and lambda=eta sqrt(4mu+2)<1, then every neighborhood of x0 contains a point where

    |sym DV|^2>mu |W|^2.

In particular tr((DV)^2)>0 arbitrarily close to x0 for every stated c and omega. For 2/5<c<1/2, the stronger inequality |sym DV|^2>(17/2)|W|^2 occurs arbitrarily close to x0. These are local conclusions under every displayed equation and strict sign assumption. They do not exclude a common flat point.

## 2. Transport and a punctured transverse disc

A is invertible, since det A=c(c^2+omega^2)>0. Put n0=X(x0)/|X(x0)| and take the plane Pi through x0 normal to n0. The map Phi(sigma,t)=exp(tA)sigma is a diffeomorphism from a sufficiently small plane disc times a time interval into G and into any prescribed ball about x0. Its central line is Gamma locally. Shrink the disc so that it meets Gamma only at x0. This follows either from this flowbox, or from |exp(tA)x0|=exp(ct)|x0|, which prevents another far-time intersection arbitrarily close to x0.

Write E=|V|^2 and H=-S. The transport equations imply XE=-bE and XH=-bH. Thus E and H each acquire the factor exp(-bt) along Phi, and R=E/H is invariant under X off Gamma. V vanishes on Gamma by the linear V transport and V(x0)=0. Therefore P=0 on Gamma. On the punctured transverse disc D', H is strictly positive.

Suppose toward a contradiction that |sym DV|^2<=mu|W|^2 on a ball about x0 containing the smaller flowbox. Every subsequent curve stays inside this ball.

## 3. Gradient control and positivity of E

Taking grad S cross (aV)=grad S cross (X cross W), and using W.grad S=0 and X.grad S=-bS, gives

    W=eta grad(log H) cross V.

The identity |DV|^2=|sym DV|^2+|W|^2/2 and the assumed strain bound therefore give

    |grad E|<=2|DV||V|<=lambda |grad(log H)| E.        (1)

On compact subsets away from Gamma the coefficient on the right is bounded. Gronwall along segments shows that the positive set of E is both open and relatively closed in the connected punctured disc D'. For example, along a segment of length ell in a compact disc, E at its endpoint is at least exp(-C ell) times its positive starting value. Hence E is positive everywhere on D', or zero everywhere there.

The zero alternative, transported through Phi, gives V=0 on an open neighborhood of x0. The Poisson equation then gives Delta S=0 there. A smooth harmonic function that vanishes to infinite order at x0 vanishes on the connected neighborhood, contradicting S<0 off Gamma. Consequently E>0 on D'. No division by E has been made before this conclusion.

## 4. Pointwise projection estimate

Set u=grad log H and w=grad log R, initially as ambient gradients restricted to D'. Then

    u.X=-b, w.X=0, |u+w|<=lambda |u|.

Here lambda>0 because eta>0 and mu>=0. Let Xhat=X/|X|, beta=b/|X| and let n be a unit vector with epsilon=|n-Xhat| satisfying

    epsilon<=min(1/2,(1-lambda^2)/(6lambda)).

The vector Z=u-[(u.n)/(X.n)]X is tangent to the plane normal to n. Indeed X.n=|X|(1-epsilon^2/2)>0. From (u+w).Xhat=-beta follows beta<=lambda|u|. Put nu=(1-epsilon^2/2)^(-1). For epsilon<=1/2, 1<=nu<=1+epsilon^2<=2. Direct expansion gives

    u.Z=|u|^2-nu beta^2+nu beta u.(n-Xhat).

The lower bound is at least [1-lambda^2-3lambda epsilon]|u|^2, and hence at least (1-lambda^2)|u|^2/2. Dropping the negative term in the same formula gives u.Z<=(1+lambda)|u|^2. Since w.X=0,

    w.Z=w.u<=-(1-lambda)|u|^2.

With gamma=(1-lambda)/2>0, the resulting estimates are

    u.Z>=(1-lambda^2)|u|^2/2,
    (w+gamma u).Z<=-(1-lambda)^2|u|^2/2.              (2)

All constants are pointwise algebraic. No sample check is used.

## 5. A bounded-ratio sequence from the pressure equation

For completeness, a positive semidefinite C1 tensor T on a ball in dimension d, with div div T=0, infinite-order flatness at its center, and alpha h I<=T<=beta h I for constants 0<alpha<=beta and h>=0, must vanish. To see this, integrate n.T(rn)n over the unit sphere to obtain A(r), and integrate tr T-n.Tn to obtain B(r). Radial divergence and the zero center flux give

    A'(r)=[B(r)-(d-1)A(r)]/r<=K A(r)/r,
    K=(d-1)(beta/alpha-1).

Thus A(r)>=(r/r1)^K A(r1) for 0<r<r1. Infinite-order flatness forces A(r1)=0. Positivity and the comparison inequalities give T=0. The flux at the center is zero because div T is bounded; no condition at infinity is used. This is the fully rechecked tensor lemma A1610.

If liminf R>2 as x approaches x0 off Gamma, then R>=Rl>2 on a small punctured neighborhood. For

    T=V tensor V+P I,

its eigenvalues obey (1/2-1/Rl)E I<=T<=3E I/2. The inequalities extend to Gamma because V=P=0 there. Divergence freedom and the Poisson equation imply div div T=0. Smooth flat V,S make T infinitely flat. The preceding lemma gives V=P=S=0 nearby, a contradiction. Therefore liminf R<=2.

Choose y_j off Gamma approaching x0 with R(y_j)<3. The inverse flowbox writes y_j=Phi(sigma_j,t_j), where sigma_j approaches x0 through D'. Invariance gives R(sigma_j)<3, while H(sigma_j) approaches zero. This step supplies the sequence on the same transverse disc on which the flow below is defined.

## 6. The flow contradiction and its continuation

Shrink the transverse disc so that n0 and X(y)/|X(y)| satisfy the bound in Section4 everywhere. Use n=n0 there and let Z be the resulting smooth tangent vector field. Let Xmax be a finite bound for |X| on its closed surrounding ball. By beta<=lambda|u| and (2),

    Z(log H)>=(1-lambda^2)b^2/(2lambda^2 Xmax^2)>0,
    Z(log R+gamma log H)<=0.                         (3)

Choose a fixed smaller circle C centered at x0 in the disc. For large j, sigma_j is inside C. A forward Z-trajectory from sigma_j cannot approach x0, because H increases and H(x0)=0. If it never meets C, it remains in the compact set bounded by C where H>=H(sigma_j)>0. This is a compact subset of the smooth vector field's domain, so maximal-curve continuation makes the trajectory exist for all positive time. The strictly positive uniform rate in (3) then makes log H unbounded on this compact set, a contradiction. It follows that the trajectory reaches C at a point z_j.

Put F=log R+gamma log H. By (3),

    F(z_j)<=log 3+gamma log H(sigma_j),

whose right side tends to minus infinity. On C both E and H are positive, so F is continuous and has a finite lower bound. This is impossible. The assumed strain inequality cannot hold on any neighborhood, proving Section1. The argument uses only compact continuation for each trajectory, not completeness on a punctured domain.

## 7. Constants, corollary and unresolved cases

For mu=1/2, lambda=2eta<1 because 0<c<1/2. The identity tr((DV)^2)=|sym DV|^2-|W|^2/2 proves the strict positive-trace conclusion. At c=2/5, eta=1/6, and eta decreases with c since eta'=-2/b^2. For 2/5<c<1/2, mu=17/2 gives lambda=6eta<1. Neither endpoint c=0 nor the equality lambda=1 is covered by the flow estimate.

C60's mean-pressure trichotomy remains true. In its cases (d1) and (d3), C60 already supplies points with negative trace arbitrarily close to x0. Combining this with the new unconditional positive-trace conclusion gives both signs in those two cases. In case (d2), only the positive-trace conclusion follows without another premise. The hypothesis tr((DV)^2)<=0 on a whole neighborhood, previously open in the first part of A2133, is now excluded in the exact setting of Section1, for all omega and without a period hypothesis.

A neighborhood with tr((DV)^2)>=0, or trace changing sign in every neighborhood, is not excluded. Nor does the argument cover arbitrary zero sets of S, S>0, nonflat zeros, equality lambda=1, or the unrestricted global profile problem. No pressure normalization freedom is introduced: P is the specified S+E/2 throughout.

## 8. Verification and collaboration record

The complete C61 source, complete C60 dependency, and all six sections of the retained tensor foundation were read. The proof above independently checks each identity, the center flux, positivity before logarithms, projection constants, transverse transport of the ratio sequence, and compact continuation. No computation or source sample checker is needed or executed. The exact source copies and SHA256 hashes are in the team records.

This review exchanges findings through the existing configured model coordinator and theory agents and the submitted C-working file. The actual provider runtime is not independently attested.
