# Physical variables, canonical pressure, and the terminal Weber formula

## Exact scope and notation

This audits Theory Agent A C29 and in the team records. The scaling identities below require only a C1 field and 0<c<1. The momentum identities require a C2 divergence-free profile U and a C1 pressure P solving

    (1-c)U + omega J U + ((Ay+U).grad)U + grad P = 0,
    A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0).

For every conclusion about the terminal tail, assume additionally 2/5<c<1/2, bounded U, distributionally vanishing velocity dilates as in Theorem T, and the Dini condition

    integral_1^infinity sup_{|y|>=r}|DU(y)| dr/r < infinity.

Decay U(y)->0 implies the required boundedness and dilate condition. Set delta=1-2c, k=(1-c)/c, alpha=3-2k, B=Ay+U. Phi is its complete flow. For terminal Bernoulli formulas choose the canonical pressure P=P_can=sum_ij R_i R_j(U_i U_j), with no additional constant. Theorems S and T, confirmed in A209-A210, give the continuous scattering map S, its compact null zero set K, a C1 volume-preserving diffeomorphism S from the complement of K onto the punctured space, and continuous tails V and Omega_tilde=curl V. They satisfy

    S(Phi_s y)=exp(sA) S(y),
    V(exp(sA)z)=exp(-(1-c)s) exp(-omega sJ)V(z),
    U=V+W, W=o(r^-k) uniformly,
    |U|=O((1+r)^-k), |Omega|=O((1+r)^(-k-1)).

Theorem T does not assert that the full gradient of V is continuous. We use no such assertion. A250 gives W in L2, E(R)-L R^alpha->0, and integral_{B_R}|V|^2=L R^alpha. Constants below may depend on the field, c, omega, and a fixed positive distance from the origin.

## 1. Scaling and particles

Fix T, let s=-log(T-t), Q_s=exp(omega sJ), and put

    u(x,t)=exp((1-c)s) Q_s U(exp(sA)x),
    p(x,t)=exp(2(1-c)s) P(exp(sA)x).

Since exp(sA)=exp(cs)Q_s^T and dt/ds=exp(-s), direct differentiation gives

    grad_x u=exp(s) Q_s DU Q_s^T,
    curl_x u=exp(s) Q_s Omega,
    partial_t u+(u.grad)u+grad p
      =exp((2-c)s)Q_s[(1-c)U+omega JU+(B.grad)U+grad P].

The divergence transforms by the same chain rule. This proves equivalence with Euler, with the stated time interval t<T. Because U is bounded, B has at most linear growth and its C1 flow is complete in both directions.

For X(y,t)=exp(-sA)Phi_s(y), X(y,T-1)=y and

    dX/dt=exp(s)exp(-sA)[B(Phi_s y)-A Phi_s y]=u(X,t).

Also dX/ds=exp(-sA)U(Phi_s y), with absolute bound M exp(-cs). Its integral converges, so X(y,t)->S(y) and |S(y)-y|<=M/c. Thus K consists exactly of the initial particle labels that reach the origin at terminal time. Under Dini, A209 supplies C1 convergence locally off K and det DS=1. No assertion of smooth continuation through the terminal origin is made.

For r(t)=rho exp(cs), rotations preserve the exterior sets and norms. Consequently

    sup_{|x|>=rho}|u|=exp((1-c)s) sup_{|y|>=r(t)}|U|,
    sup_{|x|>=rho}|grad u|=exp(s) sup_{|y|>=r(t)}|DU|,
    sup_{|x|>=rho}|curl u|=exp(s) sup_{|y|>=r(t)}|Omega|.

Changing variables first to s and then to r proves, as an equality of nonnegative extended integrals,

    integral_{T-1}^T sup_{|x|>=rho}|grad u|dt
       =(1/c) integral_rho^infinity sup_{|y|>=r}|DU|dr/r.

Finiteness for one rho implies finiteness for every positive rho: Dini finiteness gives a finite exterior supremum at some radius, and continuous DU is bounded on the intervening compact region. The condition is an integrated exterior Lipschitz bound; it does not invoke a global continuation theorem.

The same supremum formulas show that uniform profile decay is precisely decay of the rescaled exterior velocity. They show that U=O(r^-k) is equivalent to a velocity uniformly bounded away from the origin up to T. For the converse choose rho=1 and s=(log|y|)/c for any |y|>=1. Similarly DU=O(r^(-1/c)) and Omega=O(r^(-1/c)) are equivalent to the respective bounded exterior physical derivatives and vorticity. Bounded gradient is stronger than its time integrability.

Twisted homogeneity and W=o(r^-k) give

    |u(x,t)-V(x)|<=eta(r(t)) |x|^-k, eta(R)->0,

uniformly for |x|>=rho. Thus V is the terminal velocity away from zero. Spatial changes of variables give

    integral_{|x|<rho}|u(x,t)|^2dx
      =exp(-(5c-2)s) E(rho exp(cs)) ->L rho^alpha,
    ||u(t)-V||_2^2=exp(-(5c-2)s)||W||_2^2.

Here 1<k<3/2 ensures local square integrability of V at zero. Neither u(t) nor V need have finite total energy individually.

## 2. A pressure bound with exact hypotheses

Lemma. If U is C1, |U(y)|<=C(1+|y|)^-k, DU is bounded, and 1<k<3/2, then

    |P_can(y)|<=C'(1+|y|)^(-2k) log(2+|y|).

This assertion about the Riesz expression does not need the profile equation. Set f=U_i U_j. Then |f(z)|<=C(1+|z|)^(-2k), |Df(z)|<=C(1+|z|)^-k, and f belongs to Lq for every q>3/(2k), in particular L2. The order-zero Riesz product consists of a constant multiple of f and a principal-value kernel K with spherical mean zero and |K(w)|<=C|w|^-3.

For R=|y|>=2 put ell=R^-k. On |z-y|<ell subtract f(y). This part is at most

    C R^-k integral_0^ell dr = C R^(-2k).

On ell<=|z-y|<R/2, use |f(z)|<=C R^(-2k); the radial kernel integral is bounded by C log(R/ell). On |z-y|>=R/2 and |z|<=2R, use

    C R^-3 integral_{|z|<=2R}|f(z)|dz <= C R^(-2k),

where 2k<3 is essential. Finally, for |z|>2R, |z-y|>=|z|/2 and direct radial integration again gives C R^(-2k). The local multiple of f obeys the same bound. On bounded y, the local C1 subtraction and integrable far kernel bound the pressure uniformly. This proves the lemma, without a claim that the logarithm is optimal.

Dini implies bounded DU, so the lemma applies to the stated profile class. With H=P_can+|U|^2/2+(Ay).U and tau=(Ay).V it gives

    H=tau+(Ay).W+O(r^(-2k)log r),
    H-tau=o(r^(1-k))

uniformly at infinity. Physical pressure satisfies sup_{|x|>=rho}|p(x,t)|<=C_rho(1+s) for s>=0. Indeed its bound is C |x|^(-2k)log(2+exp(cs)|x|); the supremum of |x|^(-2k)log(2+|x|) on |x|>=rho is finite. Therefore (T-t)p tends uniformly to zero away from the origin.

## 3. Bernoulli and Weber formulas

Let e_phys=|u|^2/2. Direct scaling yields

    exp(delta s)H(exp(sA)x)=(T-t)(p+e_phys)+(Ax).u.

Along X, the profile identity B.grad H=-delta U.B becomes

    d/dt[(T-t)(p+e_phys)+(AX).u]=delta(p-e_phys).

An independent Euler check uses D_tu=-grad p, D_te_phys=-u.grad p, and

    (T-t)partial_t p=2(1-c)p+(Ax).grad p,
    (Au).u=c|u|^2.

The pressure-gradient terms cancel and the remaining terms are delta(p-e_phys). This differential identity holds for any profile pressure constant. Its terminal limit below does not.

If y is outside K, X(y,t)->S(y)!=0, u(X,t)->V(S(y)), and (T-t)(p+e_phys)(X,t)->0. Hence

    kappa(y):=lim_{s->infinity}exp(delta s)H(Phi_s y)
             =(A S(y)).V(S(y))=tau(S(y)).

Since |Phi_s y| is comparable to exp(cs) for large s, the pressure lemma and velocity bound show

    exp(delta s)|(P_can-|U|^2/2)(Phi_s y)|
       <=C_y(1+s)exp(-s).

The equality delta-2kc=-1 gives the exponent. This proves absolute convergence and the exact identity

    H(y)=kappa(y)-delta integral_0^infinity
                    exp(delta s)(P_can-|U|^2/2)(Phi_s y)ds.

Equivalently,

    phi(y):=(H(y)-kappa(y))/delta
      =integral_{T-1}^T (e_phys-p)(X(y,t),t)dt.

At finite t, differentiating u_i(X,t) partial_j X_i gives the Weber identity

    X_t^*(u.dx)-U.dy=d phi_t,
    phi_t=integral_{T-1}^t(e_phys-p)(X(y,t'),t')dt'.

On compact subsets outside K, the integrand bound above is uniform, so phi_t converges uniformly to phi. The left side converges uniformly as a one-form because X_t->S in C1 and u->V uniformly away from zero. Passing to the limit distributionally, and then using continuity of the limiting one-form, gives phi in C1 and

    U.dy-S^*(V.dz)=-d phi.

This passage does not differentiate V. Subtracting V yields

    W=Z-grad phi, Z=DS^T(V composed with S)-V.

If one replaces P_can by P_can+C, the finite-time differential identity remains valid, but H increases by C and exp(delta s)H acquires C exp(delta s). Its finite terminal coefficient and absolutely convergent formula require removing this constant. The pressure normalization is therefore part of the theorem, not an optional convention.

## Scope and dependencies

A209-A210 supply only the explicitly listed scattering and tail inputs. A250 supplies the energy defect. The pressure lemma and all changes of variables are proved here. These statements are conditional physical interpretations and estimates, not a profile exclusion. The formulas for the terminal coefficient use the Dini scattering conclusions, not merely a rate bound for U and bounded DU by themselves. A claim about pressure work integrated from the remote past, outside the submitted formulas, should retain its exact convergence qualification; no absolute pressure-gradient work estimate along each particle is inferred here.
