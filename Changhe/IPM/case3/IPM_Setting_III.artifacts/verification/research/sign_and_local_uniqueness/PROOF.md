# Strict sign, source geometry, and conditional local uniqueness

Independent verifier audit, 2026-10-20. The sign theorem is unconditional for an exact primary profile. The uniqueness theorem is conditional on the explicitly stated linear hypotheses. Neither theorem establishes existence or full-class nonexistence.

## 1. Setting and exact statements

Let ell>1 and let rho be a smooth even-x, odd-y density on the plane with a=rho_y(0) nonzero and the primary sublinear density and gradient bounds. Let U be its canonical full-plane IPM velocity, W=ell X+U, and suppose W.grad rho=rho. Write A=2ell-1. The independently proved center relation gives DU(0)=diag(ell-1,1-ell), DW(0)=diag(A,1). In particular div W=2ell and U=o(r).

The following three conditions are equivalent:

1. W has no equilibrium other than the origin.
2. rho(x,y)/(a y)>0 for every y nonzero.
3. Condition2 holds and rho_y(x,0)/a>0 for every real x.

Here the inequality is strict. A weak sign condition is not substituted for it. Under these conditions every nonzero trajectory converges to zero in backward time and escapes to infinity in forward time. The sign of a itself is unrestricted by this theorem.

For any exact primary profile, whether or not these conditions hold, put w(x)=W_1(x,0), g(x)=rho_y(x,0). Then

    w g'=(w'-A)g.                                           (1)

On an interval containing zero on which g is nonzero,

    (w/g)'=A/g,  w(x)=A g(x) integral_0^x 1/g(t) dt.          (2)

A finite-order zero of g away from zero cannot have order1. If its order is m>=2, then w also vanishes there and w'=-A/(m-1). This conclusion makes no assertion about a flat zero.

The conditional nonlinear uniqueness assertion is stated in Section5, after its function spaces and extra hypotheses have been defined.

## 2. Proof of the sign equivalence, including the nonhyperbolic case

The growth bound makes W complete. Outside a fixed circle, W points strictly outward because W.radial=ell r+o(r). Backward trajectories are therefore bounded. If zero is the only equilibrium, the planar limit-set alternative for a bounded orbit with finitely many equilibria leaves an equilibrium, a periodic orbit, or a graph of connecting trajectories. Positive constant divergence excludes a periodic orbit by the divergence theorem on its interior. With just one equilibrium, a nontrivial connecting graph would require a homoclinic connection to the source. No nonconstant trajectory can approach this source in forward time: in a small ball, X.W>=k|X|^2 for some k>0. Thus the backward limit is zero. The same alternatives and the outward estimate show that every nonzero forward trajectory escapes. This is the planar-flow argument also recorded in ../flow/PROOF.md; no finite-equilibrium assumption is imposed on other profiles here, since this paragraph assumes there is precisely one.

On the source basin, the weak source label is

    eta(X)=lim_(t->infinity) e^t y(Phi_(-t)X),
    W.grad eta=eta, eta_y(0)=1, rho=a eta.                    (3)

Its smooth construction and uniqueness were independently established in ../labels/PROOF.md. The strict sign can also be checked directly, without inferring it from a limiting nonnegative quantity. Parity gives W_2=y b(x,y), b(0)=1 and b-1=O(r^2). Along the backward orbit z(t),

    e^t y(z(t))/y(X)=exp(integral_0^t [1-b(z(s))] ds).        (4)

The tail integral converges absolutely, since z(t) approaches the source exponentially. The finite part is finite and real. Consequently eta(X)/y(X) is strictly positive. On y=0 the transverse variational equation has the same positive exponential factor, evaluated on the axis. Its normalized infinite-time limit is finite and strictly positive. Thus eta_y(x,0)>0. This proves condition1 implies condition3. Condition3 implies condition2 immediately.

Suppose now condition2 holds. At any equilibrium the equation gives rho=0, so all equilibria must lie on y=0. If there is a nonzero axis equilibrium, reflection lets us consider a positive one. The smooth function w is positive near zero, w(x)=Ax+O(x^3). Its first positive zero x1 exists and satisfies w'(x1)<=0. At P=(x1,0), parity and constant divergence give

    DW(P)=diag(lambda1,lambda2),
    lambda1=w'(x1)<=0, lambda2=2ell-lambda1>1.               (5)

We give the needed unstable trajectory explicitly, including lambda1=0. In coordinates z=(xi,zeta) centered at P write z'=diag(lambda1,lambda2)z+N(z), N(0)=DN(0)=0. After a smooth local cutoff, N is globally Lipschitz with arbitrarily small constant epsilon, while unchanged on a sufficiently small ball. Choose 1<kappa<lambda2 and work in the complete space of continuous z(t), t<=0, with norm sup e^(-kappa t)|z(t)|. For small fixed b0 nonzero set

    xi(t)=integral_(-infinity)^t exp(lambda1(t-s)) N_1(z(s)) ds,
    zeta(t)=exp(lambda2 t)b0
             -integral_t^0 exp(lambda2(t-s)) N_2(z(s)) ds.  (6)

The two integral operator bounds are epsilon/(kappa-lambda1) and epsilon/(lambda2-kappa). Choosing their sum below1 gives a contraction. Its fixed point has norm at most C|b0| and satisfies zeta(0)=b0. For small b0 its whole backward trajectory lies where the cutoff has not changed N, so it is a trajectory of the original W. This argument only needs lambda1<kappa; it remains valid at lambda1=0. In particular |z(t)|<=C|b0|e^(kappa t).

Since rho(P)=0 and rho is C1 nearby, |rho(P+z(t))|<=C e^(kappa t). Along this trajectory rho(P+z(t))=e^t rho(P+z(0)). Hence

    |rho(P+z(0))|<=C e^((kappa-1)t) ->0 as t->-infinity.

But zeta(0)=b0 is nonzero, contradicting condition2. No additional equilibrium exists. The equivalence is proved.

## 3. Axis identity and zeros

Differentiate W.grad rho=rho in y on y=0. The parity identities rho=0, rho_x=0, W_2=0 give

    w g'+(partial_y W_2)g=g.

Since partial_y W_2=2ell-w', this is (1). Dividing where g is nonzero proves the first identity in (2); w(0)=0 supplies its integral constant.

At a finite-order zero x1 of order m>=1, g=g_m(x-x1)^m+o(|x-x1|^m), g_m nonzero. If w(x1) were nonzero, the two sides of (1) would have different lowest orders. Therefore w(x1)=0. Comparing the next coefficient yields m w'(x1)=w'(x1)-A, so (m-1)w'=-A. Order1 is impossible and the stated formula follows for m>=2. Flat zeros are outside this coefficient argument. Section2 handles them under its strict global sign assumption without assigning them a finite order.

## 4. Weighted spaces and an exterior regularity lemma

Fix a smooth radial partition into a compact core and dyadic annuli r~2^j. Define C_q^{k,alpha} by the local C^{k,alpha} norm on the core plus

    sup_(j>=0) 2^(-q j) ||f(2^j .)||_(C^{k,alpha}(fixed annulus)),

where 0<alpha<1 and 0<q<1. Define E_nu^s using the square sum of the rescaled H^s norms with weights 2^(-nu j), together with the core H^s norm. Equivalent smooth cutoffs give equivalent norms. All density spaces carry even-x, odd-y parity. If q<nu and k>=s, then C_q^{k,alpha} embeds continuously in E_nu^s by a convergent geometric square sum. The corresponding assertion at equal weights is false for arbitrary functions.

The canonical velocity is bounded on both C_q^{k,alpha} and E_nu^s for weights between0 and1. On adjacent annuli this is the localized order-zero singular-integral estimate. For separated annuli central oddness permits subtracting K(-Y) for far input and K(X) for compact input. The resulting geometric bounds are given explicitly in ../integer_sobolev_conjugation/PROOF.md. The same decomposition with the usual local Holder estimate proves the Holder version. This inverse includes no harmonic strain.

Exterior lemma. Suppose an exact profile already belongs to C_q^{k,alpha} for some q<1. Then, with p=1/ell, both rho and U belong to C_p^{k,alpha}. This is an extra-regularity implication, not a proof that every primary profile belongs to the first space.

To prove it, write t=log r. Beyond a uniformly outward circle put V=W.e_r, Q=W.e_theta. Along an orbit parametrized by t,

    dtheta/dt=Q/V,  d tau/dt=r/V,

where tau is the original flow time. The C^{k,alpha} norms, on unit t cylinders, of Q/V and r/V-p are O(exp(-(1-q)t)). Their norms are integrable over the half-cylinder. Differentiating the angular ODE successively, and applying the integral inequality at each order, gives uniformly bounded C^{k,alpha} angular flow maps and their inverses. The first angular derivative is the exponential of the integral of a bounded integrable coefficient, so it is uniformly bounded away from zero. Higher derivative equations have that same linear coefficient and integrable lower-order products. Differences prove the Holder bounds. The integrated travel-time correction H=tau-p(t-t0) has the same bounds. Transport then gives

    rho(e^t,theta)=exp(p(t-t0)) exp(H(t,beta)) rho(e^t0,beta),

where beta is the initial angle reconstructed by the inverse flow. All rescaled C^{k,alpha} norms are bounded, proving rho in C_p^{k,alpha}; the canonical inverse gives the velocity claim. The bounds are uniform for a family with bounded initial C_q^{k,alpha} norms and ell bounded away from1, because the exterior starting circle and the integrable coefficient bounds can be chosen uniformly.

## 5. Conditional local uniqueness modulo scaling

Let rho_* be an exact primary profile with ell>1, a nonzero, p=1/ell, and suppose it has no equilibrium other than zero. Assume additionally all symbol bounds

    |partial^beta rho_*|+|partial^beta U_*|<=C_beta r^(p-|beta|)

outside a fixed circle. These bounds now follow for every exact primary profile from ../local_ipm_continuation/PROOF.md (result32). They are retained in the display to show the estimates used below.

Choose p<q<nu<1 and an integer s>2. In E=E_nu^s define

    P0 h=W_*.grad h-h,
    M h=U[h].grad rho_*, G=X.grad rho_*,
    L(h,delta)=P0 h+M h+delta G,
    X0={h in E:P0 h in E}, with its graph norm.

Assume the following full linear assertion at this order:

    L:X0 x R -> E is Fredholm of index1,
    ker L=span{(g_sc,0)}, g_sc=rho_*-X.grad rho_*.            (7)

This includes closed range and the specified graph domain. A principal-symbol calculation or a small coefficient-matrix singular value is not a substitute. Under these assumptions there is a neighbourhood of rho_* in C_q^{s+1,alpha} in which every exact primary profile is a positive spatial rescaling of rho_*. Therefore ell and a are locally unchanged. The same statement holds in a sufficiently small C_nu^{s+1,alpha} neighbourhood, still restricted to exact profiles.

Proof of the strict-weight version. The generator g_sc is nonzero. Otherwise Euler homogeneity and smoothness at zero give rho_*=a y, which violates the primary growth condition. Choose a fixed point X0 with g_sc(X0) nonzero and the functional l(h)=h(X0). It is continuous on E. Index1 and the one-dimensional kernel make L surjective. Its restriction to l(h)=0 is a Banach-space isomorphism from that graph slice to E. The inverse bound implies

    ||h||_E+|delta|<=C ||L(h,delta)||_E,  l(h)=0.            (8)

A nearby density can be placed on this slice by a unique nearby dilation S_lambda rho(X)=lambda rho(X/lambda). The derivative at the reference profile and lambda1 of its value at X0 is g_sc(X0), nonzero. Local C1 closeness preserves its sign; the intermediate value theorem gives the root and |lambda-1| bounded by the initial norm error. Dilations near1 are uniformly bounded on the weighted Holder space. Strong continuity on the fixed smooth background follows by differentiating in lambda using one additional background symbol derivative. Thus the sliced density remains close in the required norm; this step does not assume strong continuity for every function in a big Holder space.

Write h=rho-rho_* and delta=ell_rho-ell after this dilation. Subtract the exact equations:

    L(h,delta)=-(U[h]+delta X).grad h.                      (9)

On each rescaled annulus the product rule puts all derivatives of U[h] in H^s and all needed derivatives of grad h in L-infinity. Physical grad contributes a factor2^(-j). The weighted Holder bound gives a factor2^(qj), so since q<1 the coefficient is uniformly small. Summing and using boundedness of U on E gives

    ||U[h].grad h||_E<=C ||h||_(C_q^{s+1,alpha}) ||h||_E.

Also ||X.grad h||_E<=C||h||_(C_q^{s+1,alpha}) because q<nu. Consequently

    ||(U[h]+delta X).grad h||_E
       <=C ||h||_(C_q^{s+1,alpha})(||h||_E+|delta|).         (10)

There is no claim that this quadratic term maps a ball of E into E without the stronger derivative norm. Membership h in E follows from the strict-weight embedding. Equation(9), together with boundedness of M and G in E, then proves P0h in E before applying (8). Combining (8)-(10) and taking the sliced neighbourhood small proves h=0 and delta=0. Undo the scaling. Both ell and rho_y(0) are invariant under it.

For the equal-weight version, choose p<bar_p<nu. The strain is continuous in C_nu^{s+1,alpha}, by its cancellation formula and the strict sublinear weight. Hence nearby exact profiles have p_rho<bar_p and their weighted norms are uniformly bounded. Section4 upgrades them uniformly to C_bar_p^{s+1,alpha}. Let M0 be a common bound, including the background and the small dilations, and let epsilon=||h||_(C_nu^{s+1,alpha}). Annular norms obey

    2^(-nu j)||h(2^j .)||_(C^{s+1})
          <=min(epsilon,M0 2^(-(nu-bar_p)j)).

Splitting the square sum at the first j where the second term is below epsilon gives

    ||h||_E+||X.grad h||_E
          <=C epsilon sqrt(1+log(M0/epsilon))=:omega(epsilon)->0. (11)

The product estimate for U[h].grad h used only q<1, so it remains valid with q=nu. The delta term is bounded by |delta|omega(epsilon). Equation(9) again proves graph membership. Now (8) bounds its left side by C(epsilon||h||_E+omega(epsilon)|delta|), which is absorbed. This proves the second version. No existence theorem, differentiable nonlinear inverse, or simple-kernel assertion is supplied by this argument.

## 6. Far-field coefficient is not an ambient continuous slice

Fix smooth angular Theta of the density parity with Theta(pi/2)=1 and let chi(r)=0 near0, chi(r)=1 for r>=2. For q>p the smooth functions

    f_R(X)=chi(|X|/R)|X|^p Theta(arg X)

satisfy ||f_R||_(C_q^{k,alpha})<=C R^(p-q)->0, while lim_(y->infinity)y^(-p)f_R(0,y)=1. Thus the leading axis coefficient is not continuous on the ambient weighted space at fixed p. This does not invalidate its exact scaling law or the global reporting normalization on exact profiles. It explains the compact point slice used above.

## 7. Dependencies, review, and scope

The independent inverse, origin, source-label and flow proofs are in this lane's corresponding topic folders. The weighted integer domain proof is ../integer_sobolev_conjugation/PROOF.md. The subsequently confirmed ../conditional_integer_fredholm/PROOF.md supplies the Fredholm and index portion of (7) on exactly this dyadic Sobolev graph space for even s>=4 above its explicit source threshold. Its metric norm is equivalent to the dyadic norm in Section4, and its maximal graph domain uses the same P0. No transfer of Fredholmness to a Holder space is needed: the nonlinear neighbourhood, not the linear realization, is measured in the stronger Holder norm. The only remaining linear hypothesis at those orders is kernel simplicity. The lead's claims audited are referee/iso1/PROOF.md, Propositions3.1,8.1,8.2 and its far-field-slice example, read in full. The arguments above were reconstructed independently and the endpoint lambda1=0 checked directly. The lead is actual Opus5.5; findings and limitations are exchanged through lane-local notes. No additional model response is claimed for this proof.

Verdicts: strict-sign equivalence and axis identities CONFIRMED; the nonlinear inference from (7) and the stated regularity hypotheses CONFIRMED conditionally; existence of a background meeting (7) and the simple-kernel claim OPEN. The symbol bounds are now CONFIRMED for exact primary profiles by result32. Composition with result30 supplies the Fredholm part of (7) under Hdyn at its allowed even orders. No YES or NO endpoint follows.
