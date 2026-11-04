# Circulation on a carrier quotient and Lp continuation

Status: CONFIRMED A2463-A2467 at the exact scopes below; A2468 retains the unproved extensions. These are local results. They neither exclude the full common-flat system nor prove the rotating Euler conjecture.

## 1. Exact hypotheses and conclusions

Let 0<c<1/2, omega be real, Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J, X(x)=Ax and a=1-2c. Let U be an open subset of R3 avoiding zero and V:U->R3 be smooth. Put W=curl V and suppose

    div V=0, X.V=0, DV X=-LV.                                      (C)

Let sigma:D->U be a smooth transverse section, where D is a disc about zero in R2 and det(sigma_1,sigma_2,X(sigma)) never vanishes. No global injectivity is needed; all assertions can be restricted to a local section near each point. Write

    G_ij=sigma_i.sigma_j, m=|X(sigma)|,
    beta_i=X(sigma).sigma_i/m^2,
    g=G-m^2 beta tensor beta,
    j=|det(sigma_1,sigma_2,X(sigma))|,
    epsilon=sign det(sigma_1,sigma_2,X(sigma)).

There are unique smooth v=(v1,v2) and h with V(sigma)=sigma_1 v1+sigma_2 v2+h X(sigma). Define the pulled-back velocity one-form theta=u_i dy_i, where u_i=V(sigma).sigma_i.

The first conclusion is the exact system

    h=-beta.v, u=g v, j=m sqrt(det g),
    div(jv)=(3c-1)j beta.v,                                      (Q)
    partial_1 u2-partial_2 u1
      =epsilon j (W.X)(sigma)/m^2
       +a(V cross X)(sigma).(sigma_1 cross sigma_2)/m^2.           (R)

The metric g is positive definite. If V is flat at x1=sigma(0), and for a finite p>2 there is a nonnegative B0 in Lp(D) such that

    |(W.X)(sigma(y))|<=B0(y)|V(sigma(y))| almost everywhere,       (L)

then V vanishes on a neighbourhood of x1. A bounded coefficient is included by restricting to a smaller disc. The Lebesgue measure in (L) is planar coordinate measure; smooth coordinate changes and smooth positive area densities on compact subdiscs give the same local condition.

For the consequences using pressure, assume the complete setting (F): a connected X-flowbox G0 containing one orbit segment Gamma through x0, smooth V and S satisfying (C),

    X.S=-bS, W.grad S=0, b=2(1-c),
    P=S+|V|^2/2, -Delta P=tr((DV)^2),
    S=0 on Gamma, S<0 on G0 minus Gamma,

and V and S flat at x0. Here G0 avoids zero. Put H=-S and eta=a/b. At each x1 in Gamma, on every transverse section disc through x1, the ratios |W.X|/|V| and |W|/|V|, defined to be zero where V=0, fail to belong to every Lp with p>2 on every disc about the section origin. The same holds for eta|X||n.grad log H| where n=(V cross X)/(|V||X|), with arbitrary values on the measure-zero set where it is undefined. Finally, at each p0 in G0 minus Gamma with V(p0)=0, DV(p0) has eigenvalues lambda,-lambda,0 and Delta H(p0)=4 lambda^2 for lambda>=0. These statements are proved below with their dependencies explicit.

## 2. The exact quotient and circulation equations

Differentiating X.V=0 gives (DV)^T X=-A^T V. The vector identity X cross curl V=(DV)^T X-DV X and L-A^T=aI give

    X cross W=aV,
    W=(W.X)X/|X|^2+a V cross X/|X|^2.                            (1)

The second equality follows by taking X cross the perpendicular part, or by the vector triple product. Its sign is fixed by X cross (V cross X)=|X|^2V.

Let Pi denote orthogonal projection onto X(sigma)^perp. The vectors Pi sigma_1 and Pi sigma_2 are linearly independent, since the section is transverse. Their Gram matrix is g, so g is positive definite. Orthogonality V.X=0 gives h=-beta.v. Taking inner products with sigma_i then gives u=g v, and squaring the determinant after replacing sigma_i by Pi sigma_i gives j^2=m^2 det g.

Locally put Phi(y,t)=exp(tA)sigma(y). Then X=partial_t and [X,V]=DV X-AV=-V. Thus V has coordinate components exp(-t)(v,h). The Euclidean volume density in these coordinates is exp(3ct)j. Its divergence is zero exactly when

    div_y(jv)+(3c-1)j h=0,

which is (Q). This is the previously confirmed A2437 quotient equation, rederived here to fix coordinate order and signs.

For the exterior derivative of theta, mixed derivatives of sigma cancel:

    partial_1 u2-partial_2 u1
      =(DV sigma_1).sigma_2-(DV sigma_2).sigma_1
      =W.(sigma_1 cross sigma_2).

Substituting (1) and X.(sigma_1 cross sigma_2)=epsilon j gives (R). Its last term is a smooth linear form applied to v, because V(sigma)=sigma_i v_i-(beta.v)X(sigma). Thus (R)'s only independent vorticity source is W.X. Neither a pressure equation nor an energy identity has entered.

## 3. Reduction to one complex first-order equation

Restrict to a relatively compact disc in D. All metric coefficients, their required derivatives and their inverses are bounded there; m and j are bounded below by positive constants. The metric dual of theta is v. With the orientation dy1 wedge dy2 and the Hodge star of g,

    d(*_g theta)=div(sqrt(det g)v) dy1 wedge dy2.

Since j=m sqrt(det g), equation (Q) becomes

    d(*_g theta)=q1(v) dA_g,
    q1=(3c-1)beta-d log m.

Equation (R) becomes d theta=(epsilon j (W.X)(sigma)/m^2+q2(v))dy1 wedge dy2, for a smooth one-form q2.

A smooth positive metric in two dimensions has orientation-preserving local isothermal coordinates z=z1+i z2, centered at zero, with g=lambda(z)(dz1^2+dz2^2), lambda>0. Shrink to relatively compact coordinate discs, so the coordinate map and inverse have bounded derivatives and nonzero Jacobians. The local existence theorem is the one stated by Chern on printed page772; its Holder metric hypotheses are satisfied here. Smoothness follows from the smooth uniformly elliptic coordinate equation, or its usual elliptic regularity bootstrap.

Write theta=alpha1 dz1+alpha2 dz2 in these coordinates. The Hodge star on one-forms is conformally invariant in dimension two, with *theta=-alpha2 dz1+alpha1 dz2. Set f=alpha1-i alpha2. Then

    2 partial_zbar f
      =(partial_1 alpha1+partial_2 alpha2)
       -i(partial_1 alpha2-partial_2 alpha1).

The two real brackets are the coefficients of d(*theta) and d theta. The smooth changes of coordinates and the invertible metric give |V(sigma)|<=C|v|<=C'|u|<=C''|f|. Consequently (L) gives

    |partial_zbar f|<=K(z)|f|,                                  (2)
    K=C1+C2 B0(y(z)) in Lp

on a smaller coordinate disc Delta. The Lp property follows from bounded Jacobians. Constants may depend on the particular section, field and smaller disc; no uniform smallness is required.

## 4. Similarity principle and the flat-zero conclusion

Define alpha=(partial_zbar f)/f where f is nonzero and zero elsewhere. Inequality (2) implies partial_zbar f=alpha f almost everywhere, including almost every point where f=0, and |alpha|<=K. Extend alpha by zero outside Delta and put

    s(z)=1/pi integral_Delta alpha(zeta)/(z-zeta) dA(zeta).

For compactly supported Lp data with p>2, this Cauchy transform is bounded and continuous, belongs to W1p locally, and partial_zbar s=alpha in distributions. Boundedness follows directly from Holder's inequality since p/(p-1)<2 and |z-zeta|^-1 is locally integrable to that power. Holder continuity has exponent 1-2/p. The other weak derivative is the Beurling transform, bounded on Lp. The exact versions used are Bojarski's Theorems1.1-1.2 and equations(1.3),(1.5)-(1.6),(1.9)-(1.12), read in the primary translation archived in the earlier reverse-ratio review.

The bounded Sobolev chain rule and the product rule give F=exp(-s)f in W1p locally and partial_zbar F=0 in distributions. Weyl's lemma for this operator makes F holomorphic. This also follows from Bojarski Theorem1.1. Since f and s are continuous, the holomorphic representative equals F everywhere.

Flatness of V at sigma(0) implies |V(sigma(y))|<=C_N|y|^N for every integer N. Smooth multiplication and a local coordinate map with bounded derivative and inverse transfer this estimate to f. Since exp(-s) is bounded, |F(z)|<=C'_N|z|^N for every N. A holomorphic function with this estimate has every Taylor coefficient zero, so F and f vanish on Delta. The invertible transformations give V(sigma)=0 on a smaller section.

Along each local X-orbit, dV(exp(tA)x)/dt=-LV(exp(tA)x), hence V(exp(tA)x)=exp(-tL)V(x). The inverse function theorem for Phi at (0,0) now extends the zero section to an open neighbourhood of x1. Only finite local times are used. There is no completeness assumption on V's characteristic flow and no use of a global X-flowbox.

This proves the continuation statement. The proof does not cover p=2: the bounded Cauchy factor used in the flatness step has not been established at that endpoint.

## 5. Consequences in the common-flat setting

We use C66, confirmed A2404-A2408 at the exact setting (F): the flat set of V in G0 is precisely Gamma; V and W have the same zeros; every zero off Gamma lies locally on one isolated X-orbit segment, with a finite transverse vanishing order. Those statements were separately proved using the scalar and pressure equations and are not consequences of (C) alone.

Fix x1 in Gamma and a section sigma. Suppose B=|W.X|/|V|, with zero assigned where V=0, belongs to Lp on some disc about zero. At every zero of V, W=0 by C66, so inequality (L) holds almost everywhere with B0=B. The continuation statement gives V=0 on an open subset of G0. This contradicts C66's flat-set description, since Gamma has empty interior. Hence B is not in Lp on any such disc.

If instead C=|W|/|V| belonged to Lp on such a disc, restrict to a smaller disc whose closure is contained in it and in D. There |X(sigma)| is bounded and B<=|X(sigma)|C, contradicting the preceding conclusion. This restriction avoids an unsupported boundedness claim on a section all the way to its open-domain boundary.

Off Gamma, X.grad H=-bH and W.grad H=0, while X cross W=aV. These identities imply

    W=eta grad(log H) cross V.                                  (3)

For verification, substitute V=(X cross W)/a and use grad H cross (X cross W)=X(grad H.W)-W(grad H.X)=bH W. Thus, where V is nonzero,

    |W.X|/|V|=eta |X| |n.grad(log H)|,
    n=(V cross X)/(|V||X|).

The exceptional section points have measure zero. The inverse image of Gamma under a transverse section is discrete locally. Every off-Gamma zero of V also belongs to a single isolated orbit segment locally, by C66; transversality makes its inverse image locally discrete among section zeros. A discrete subset of a second-countable planar domain is countable. The union of these two exceptional sets is therefore countable, even when off-Gamma zeros accumulate at Gamma. The expression involving n and log H can be assigned zero there without changing any Lp conclusion.

This supplies the short missing zero-set detail in the submitted proof of (d). It is a qualification of how its almost-everywhere identity is read, not a new hypothesis.

## 6. Jets at off-orbit zeros and finite-order compatibility

Let p0 lie in G0 minus Gamma and V(p0)=0. C66 gives W(p0)=0, so M=DV(p0) is symmetric. The transport equation gives MX(p0)=0, while div V=0 gives tr M=0. Since X(p0) is nonzero, M has eigenvalues lambda,-lambda,0, lambda>=0. Therefore tr(M^2)=|M|_F^2=2lambda^2. Moreover H=|V|^2/2-P, so at p0

    Delta H=|DV|_F^2+V.Delta V+tr((DV)^2)=4lambda^2.

If lambda>0, the restriction of M to X(p0)^perp is an invertible symmetric trace-free map. Its determinant is negative and its linear planar index is -1. If lambda=0, M=0 and no first-jet exclusion follows.

For comparison with A2426, the continuation proof without the flatness step gives f=exp(s)F with F holomorphic. A nonzero F has isolated zeros of finite integer order N. Continuity and nonvanishing of exp(s) give the same order as a leading homogeneous complex term for f; the conjugate field (alpha1,alpha2) has local degree -N. The smooth positive metric and orientation-preserving coordinates do not change this local index. Off Gamma, (3) bounds |W| by a constant times |V| on compact neighbourhoods, so the coefficient required here is bounded. This recovers the already confirmed finite-order structure; it is not a new bound on the orders across distinct zeros.

## 7. Source comparison, dependencies and open scope

The full submitted C67 source, all six sections of the existing model C quotient comparison, C66's previously confirmed scope and the specified primary analytic passages were read. The quotient sign, vorticity decomposition, Hodge-star sign and complex conjugation agree. Two small repairs were requested: include the off-Gamma section-zero set in the almost-everywhere argument, and shrink an arbitrary section disc before bounding |X|. Section5 above makes both explicit. The submitted residual checks were not rerun and are not used as proofs.

The mathematical dependencies are elementary smooth vector calculus, the exact local quotient A2437, smooth isothermal coordinates, the explicitly identified Cauchy-transform and Weyl results, ordinary Sobolev calculus, finite local ODE uniqueness, and C66 at its full pressure-dependent scope. The statements concern every real omega. Pressure normalization does not enter the local continuation theorem; (F) fixes the local scalar P=S+|V|^2/2 for its additional consequences.

No L2 endpoint, exclusion of (F), control of shrinking-circle degrees, common-flat-orbit nonexistence, or whole-space Euler conclusion follows. The scalar equation and Poisson equation are not silently dropped when applying C66. Conversely, their presence does not turn the necessary failure of an Lp ratio bound into a contradiction.
