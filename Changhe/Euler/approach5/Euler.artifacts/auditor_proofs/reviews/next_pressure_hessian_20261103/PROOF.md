# Next-pressure obstruction at a positive-pressure finite-order zero

Status: A2107-A2112 CONFIRMED, with the exclusions and open extensions stated at A2113. Source: LIT286. The local necessary condition and its application to the specific C59/LIT285 family are distinguished from the unrestricted profile problem.

## 1. Statement and scope

Fix 2/5<c<1/2 and any finite real omega. Let Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b and nu=b+1. Let p!=0 and let smooth real fields V,P2 be defined on a neighborhood G of p. Set

    E=|V|^2, W=curl V, H=P2-E/2, Z=DV V+grad P2.

The exact local assumptions are

    H>0, div V=0, X.V=0,
    X.grad V=-LV, X.grad H=-bH,
    X cross W=aV, W.grad H=0,
    -Delta P2=tr((DV)^2).

Suppose V has exact order N>=2 at p, meaning all derivatives of orders 0 through N-1 vanish and its order-N derivative is not zero. Suppose a scalar p1 in C1(G) satisfies

    X.grad p1=-nu p1,
    -Delta p1=2tr(DV DZ) in distributions,
    W.grad(p1-2V.grad P2)=0.

Then, for T=X(p)^perp, the symmetric form

    B=3 Hess H(p)+(eta/H(p))grad H(p) tensor grad H(p)

is a scalar multiple of the Euclidean metric on T. No statement is made about its components involving X(p).

This condition excludes every finite-order N>=2 member of the particular positive-pressure Cauchy family described in Section 6. The actual-profile implication requires the separate global hypotheses of Section 7. It does not exclude all smooth reduced tails, all pressure data, or an infinite-order zero.

## 2. Potential and the leading transverse harmonic polynomial

Shrink G when necessary. Since X.grad H=-bH<0, neither X nor grad H vanishes. Taking the vector product of grad H with X cross W gives bH W, using W.grad H=0. Thus

    grad H cross V=(b/a)H W,
    curl(H^(-eta)V)=0.

On a ball choose a smooth potential phi with V=F grad phi, F=H^eta>0. The condition X.V=0 gives X.grad phi=0. Normalize phi(p)=0. Also

    W=eta H^(eta-1)grad H cross grad phi.             (2.1)

Choose a transverse affine plane at p normal to X(p), put orthonormal linear coordinates u,v on it, and extend those coordinates constantly along the smooth nonvanishing X-flow. At p their Euclidean gradients form an orthonormal basis of T. The map x to (H,u,v) is locally invertible because dH(X)!=0 and du(X)=dv(X)=0. Write phi=phi_t(u,v).

Multiplication by the nonvanishing F does not change the exact vanishing order of grad phi. Hence the first nonzero term of phi_t has degree n=N+1. Call it P. The divergence equation becomes

    Delta phi+grad(log F).grad phi=0.

The term of degree N-1 is Delta_T P=0; all coefficient variation, second derivatives of the coordinate map and the first-order term enter later. Thus P is a nonzero real homogeneous harmonic polynomial of degree n in two variables. For a nonzero complex C,

    P(u,v)=Re(C(u+iv)^n), n>=3.                      (2.2)

This is a finite Taylor argument for smooth functions. No analyticity is assumed.

## 3. Centralizer and transverse order of the next scalar

The distributional Poisson equation for p1 has a smooth source, so interior elliptic regularity makes p1 smooth after shrinking G. Put tau=p1-2V.grad P2 and kappa=nu/b>1. The leading equations imply XE=-bE and XP2=-bP2. As vector fields [X,V]=-V, since A+L=I. Consequently

    X(V.grad P2)=-(b+1)V.grad P2,
    X tau=-nu tau.

Therefore theta=tau/H^kappa is X-invariant, and theta=theta_t(u,v). Equation (2.1), W.grad H=0 and the transport equation for tau imply

    Jac(phi_t,theta_t)=0.                            (3.1)

The determinant factor is nonzero because (H,u,v) is a coordinate chart; no division by V or W is used.

Here is the needed polynomial assertion with its proof. If P is (2.2), R is homogeneous of degree 1<=j<=n and Jac(P,R)=0, then R=0 for j<n, whereas R is a constant multiple of P for j=n. On a sector where P!=0, Euler homogeneity and parallel gradients give dR=(jR/(nP))dP. Thus R=C_sector |P|^(j/n). The nodal rays of a nonzero two-dimensional harmonic polynomial are simple away from the origin. For 0<j/n<1, a nonzero sector constant would make a transverse first derivative unbounded on such a ray. A polynomial cannot have that behavior, so every constant is zero. For j=n, R is proportional to P on any sector, and the polynomial identity extends globally, including its sign.

Apply this assertion inductively to successive homogeneous terms of (3.1). The constant term of theta_t has zero derivative. Once its positive-degree terms below j vanish, the first possible Jacobian term is Jac(P,R_j); terms of phi_t beyond P multiply only a derivative of a vanished lower term. Hence

    theta_t=theta0+C0 P+O(|(u,v)|^(N+2)).             (3.2)

All positive-degree terms 1 through N vanish. Smooth Taylor remainders have the derivative bounds used below.

## 4. The constant term and the Laplacian of tau

At p, V=DV=0. Since Delta P2=-tr(DV^2) and P2=H+|V|^2/2, one has Delta H(p)=0. Differentiating the divergence equation in Section 2 gives the exact product identity

    Delta V=Hess phi grad F
        +[(Delta F)I-F Hess(log F)]grad phi.          (4.1)

Indeed, the two product terms Hess phi grad F in Delta(F grad phi) lose one copy to F grad Delta phi. Since grad phi(p)=Hess phi(p)=0, (4.1) gives Delta V(p)=0. The Laplacian product rule then gives Delta(V.grad P2)(p)=0. The next Poisson source vanishes at p as well, so Delta tau(p)=0.

All first and second derivatives of theta vanish at p by N>=2 and (3.2). Therefore

    0=Delta tau(p)
      =theta0 kappa(kappa-1)H(p)^(kappa-2)|grad H(p)|^2.

The factor multiplying theta0 is positive. Thus theta0=0. The first possible Taylor term of tau has degree n=N+1 and is H(p)^kappa C0 times P on the orthogonal projection to T. It is a harmonic polynomial in ambient Euclidean coordinates. Applying Delta to the smooth Taylor expansion yields

    Delta tau(x)=O(|x-p|^N).                         (4.2)

Neither tau=0 near p nor unique continuation is needed or asserted.

## 5. Extracting the Hessian condition

Write h=x-p and let phi_n(h) be P on the orthogonal projection to T. Then

    grad phi=O(|h|^N),
    Hess phi=Hess phi_n+O(|h|^N),
    DV=F(p)Hess phi_n+O(|h|^N),
    P2=H+O(|h|^(2N)),
    Z=grad H+O(|h|^(2N-1)),
    DZ=Hess H+O(|h|^(2N-2)).                         (5.1)

In particular Delta[V.grad(P2-H)]=O(|h|^(3N-3)), which is O(|h|^N) for every N>=2. Formula (4.1) and the ordinary product rule give, at degree N-1,

    Delta(V.grad H)
      =Hess phi_n(grad F(p),grad H(p))
        +2F(p)Hess phi_n:Hess H(p)+O(|h|^N).

Terms containing grad phi or one extra factor of h have higher order. Also

    2tr(DV DZ)=2F(p)Hess phi_n:Hess H(p)+O(|h|^N).

Substitute p1=tau+2V.grad P2 into its Poisson equation and use (4.2). Divide the resulting degree N-1 equation by the nonzero factor -2F(p). Since grad F(p)/F(p)=eta grad H(p)/H(p), the result is

    Hess phi_n:B=0.                                  (5.2)

This independently fixes the coefficient 3 in B. Two copies of Hess H come from the product Laplacian and one from the Poisson source after moving it to the same side.

The matrix Hess phi_n annihilates X(p) and is trace free on T. Its two trace-free components are real and imaginary multiples of C(u+iv)^(n-2). Since n-2>=1, those two real polynomials are linearly independent. Equation (5.2) therefore annihilates each trace-free component of B on T, proving the theorem. This last argument fails at N=1, which is excluded from the statement.

## 6. The particular positive-pressure Cauchy family

The confirmed C59/LIT285 construction, A2086-A2089, takes p=e1, r=|x|, sigma=omega/c, lambda=b/c>2 and

    pi=exp(sigma log r J)x/r, u=pi2, v=pi3,
    H=r^(-lambda)H_t(u,v), phi=phi_t(u,v),
    V=H^eta grad phi, P2=H+|V|^2/2.

Its analytic Cauchy data are

    phi_t(u,0)=u^(N+1)/(N+1), partial_v phi_t(u,0)=0,
    H_t(u,0)=1, partial_v H_t(u,0)=0.

For each finite N>=2 the leading equations hold, and V and W have exact order N along the local X-orbit arc through p. Those previously confirmed conclusions remain valid.

On x3=0, H=r^(-lambda) and partial_3 H=0. Differentiating these exact identities at p gives

    H=1, grad H=(-lambda,0,0),
    H11=lambda(lambda+1), H22=-lambda,
    H12=H13=H23=0.

Delta H(p)=0 follows from the leading Poisson equation and V=DV=0, so H33=-lambda^2. The orthogonal pair g=(sigma,1,0), e3 spans T, with |g|^2=1+sigma^2. Direct substitution into B gives

    B(g,g)-(1+sigma^2)B(e3,e3)
      =lambda[3(lambda-1)+(6lambda+3+eta lambda)sigma^2]>0.

This cannot hold for a scalar metric restriction. Thus no member of this Cauchy family admits the next scalar with all hypotheses of Section 1. The argument uses the pressure data shared by the entire family, not a selected higher velocity coefficient or a numerical test.

## 7. Transfer to actual profiles, including the resonant exponent

For this implication assume a global full profile U in C2(R3;R3), P in C1(R3), satisfying

    div U=0, LU+DU(Ay+U)+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p0),
    |DU(y)|<=C(1+|y|)^(-p0-1), p0=(1-c)/c,

for a finite C. Let V,P2 be its actual leading velocity and canonical leading pressure. If they coincide locally with a pair of Section 6, they are smooth on that neighborhood and satisfy the leading local hypotheses.

For c!=3/7, the previously confirmed next-coefficient theorem A647-A648 supplies p1 in C1,alpha with the stated homogeneity, distributional Poisson source and transport of tau. Its source is 2tr(DV DZ), since both V and Z are divergence free. The transport identity comes from the weak first correction of the exact vorticity flux; it does not require an assumed pointwise expansion of every derivative or a division by W. The full independent reconstruction was reread for this audit.

At c=3/7 and omega!=0, A653-A654 supplies the period-averaged scalar with these same three identities. The proof first eliminates the axisymmetric logarithmic coefficient. Averaging over 2pi/|omega| then gives the scalar; unaveraged pressure convergence is not needed here. The complete independent resonant proof was reread. At omega=0, the nonrotating Liouville theorem, rechecked at A2045-A2047, already excludes any nonzero global profile in this class. These alternatives cover every target c and every finite omega.

This transfer uses canonical pressure normalization, helicity zero and both natural bounds explicitly. Bare velocity decay does not supply those assumptions. The local proof contains no integration at infinity and no claim about global characteristic completeness; those issues belong to the cited actual-tail theorems.

## 8. Verdict limits and evidence

The necessary Hessian condition and exclusion of this specific Cauchy family are independently confirmed after the final reading recorded with the ledger. The local leading models still satisfy their original equations. Their exclusion as actual tails is conditional on the global class in Section 7. Other pressure Cauchy data may satisfy the Hessian condition, and infinite-order zeros are outside the Taylor argument. No unrestricted arbitrary-helicity nonexistence theorem follows.

The verification manifest pins the submission, the arc construction audit and both actual next-scalar reconstructions, together with their original sources. No numerical or symbolic computation was needed. No formal proof is claimed. Existing configured model collaboration proceeds through the coordinator and theory-working files; provider execution is not independently attested. No new model client or agent was used.
