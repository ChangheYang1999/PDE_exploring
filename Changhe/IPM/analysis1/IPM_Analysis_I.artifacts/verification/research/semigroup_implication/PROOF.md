# Exponential semigroup decay implies a stationary inverse

Topic91. Standalone analytic proof, written before review and regression computations. All spaces may be real or complex. This is a theorem about an explicitly specified generator, not an estimate for the IPM linearization.

## Statement and domain

Let X be a Banach space and L:D(L) subset X -> X the generator of a strongly continuous semigroup S(t), t>=0. Suppose X=M direct-sum N, where M is finite-dimensional and N is closed. Let Q be the bounded projection onto N along M. Assume

 L(D(L) intersect N) subset N.                              (1)

The phrase L-invariant here means exactly(1), with the domain retained. Finite dimensionality of the complementary quotient is essential to the proof below; invariance of M is unnecessary. Suppose K,lambda>0 and

 ||S(t)Q||_(X->X) <= K exp(-lambda t) for every t>=0.        (2)

Then N is S(t)-invariant, its restricted semigroup has generator L_N with domain D(L) intersect N, and L_N is one-to-one and onto N. Its inverse is

 B n = -integral_0^infinity S(t)n dt,  n in N,
 ||B||_(N->N) <= K/lambda.                                 (3)

The integrals are strong (Bochner) integrals, not an assertion of operator-norm measurability of t->S(t). On X, BQ x=-integral_0^infinity S(t)Qx dt and ||BQ||<=K/lambda. Writing the latter operator as L_N inverse without restricting its argument to N is an abuse to avoid.

## Finite quotient closes the invariance gap

Let pi:X->Z=X/N be the quotient map. The vector space Z is finite-dimensional. Since D(L) is dense, pi(D(L)) is a dense linear subspace of Z and therefore all Z. Choose vectors d_1,...,d_m in D(L) whose images form a basis of Z; they give a continuous linear section R:Z->D(L) subset X with pi R=Id. Its continuity into the graph norm also holds, since both R and LR map a finite-dimensional space linearly into X.

If x,y in D(L) have pi x=pi y, condition(1) gives pi Lx=pi Ly. Hence A(pi x)=pi Lx is a well-defined linear map Z->Z, automatically bounded. In particular

 pi Lx=A pi x, x in D(L).                                  (4)

For completeness, the defining generator difference quotient shows that S(t) maps D(L) into itself, LS(t)x=S(t)Lx and t->S(t)x is continuously differentiable for x in D(L). Applying pi and(4) gives a finite-dimensional ODE

 d/dt pi S(t)x=A pi S(t)x, pi S(0)x=pi x.

Multiplication by exp(-tA) and differentiation proves pi S(t)x=exp(tA)pi x. Extend this identity by density and boundedness to every x in X. It follows that S(t)N subset N.

The part domain D(L) intersect N is dense in N: if x_j in D(L) tends to n in N, then y_j=x_j-R pi x_j lies in D(L) intersect N and tends to n. The semigroup restricted to N is strongly continuous, and the difference quotient has an N-limit exactly when its X-limit exists, because N is closed and its norm is inherited. Its generator is therefore exactly L_N, not an unspecified extension.

The projection Q is bounded because N is closed and the finite-dimensional complement maps continuously isomorphically onto X/N. Explicitly Q=Id-R_M pi, where R_M:Z->M is the inverse of pi restricted to M. No assertion that Q commutes with S(t) is needed: on N, Qn=n. If M too is semigroup-invariant, they do commute, but that is a stronger unused fact.

## Constructing and verifying both inverse identities

For n in N, (2) implies ||S(t)n||<=K exp(-lambda t)||n||. Strong continuity gives integrability on finite intervals; the displayed majorant makes the integrals Cauchy in N at infinity. Define B by(3), giving the norm bound.

For T>0 set F_T=integral_0^T S(t)n dt. For h>0 the semigroup law gives

 (S(h)F_T-F_T)/h
 = [integral_T^(T+h) S(u)n du-integral_0^h S(u)n du]/h
 -> S(T)n-n.

Thus F_T is in D(L) intersect N and L F_T=S(T)n-n. Since -F_T tends to Bn and L(-F_T)=n-S(T)n tends to n, closedness of L gives Bn in D(L) intersect N and L_N Bn=n. The generator is closed: one can prove this directly by applying

 S(t)x-x=integral_0^t S(u)Lx du

to a graph-convergent sequence in D(L), passing to the limit, dividing by t, and using strong continuity. Hence no closedness assumption has been added silently.

Conversely, for x in D(L) intersect N the generator derivative identity yields

 B L_N x = -lim_(T->infinity) integral_0^T d/dt S(t)x dt
 =x-lim_(T->infinity)S(T)x=x.

This establishes both inverse identities and uniqueness. If N={0}, the conclusion is the unique operator on the zero space and remains valid.

## Converse and scope for dynamic rescaling

The converse is false even in one dimension: X=N=R, M={0}, L=Id has bounded inverse Id but S(t)=exp(t)Id has no decay estimate with positive lambda. This satisfies all domain and invariance premises except(2). The example L=-Id also verifies the minus sign in(3) directly.

Consequently an approach to the IPM problem that proves exponential decay of a precisely realized linearized semigroup on the complement of modulation directions also proves the stationary inverse on that complement, with constant K/lambda. This is a sufficient route to the missing inverse estimate and is strictly stronger than mere invertibility in general. It does not prove that every conceivable dynamic argument must establish exponential decay, or that stationary invertibility is equivalent to weighted decay. The Banach space, domain, finite-dimensional complement and estimate(2) must still be supplied for the actual IPM operator. None is certified here. This theorem supplies no residual bound, nonlinear stability result or decisive endpoint.
