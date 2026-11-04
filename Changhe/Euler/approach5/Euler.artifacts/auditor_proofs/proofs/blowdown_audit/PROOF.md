# Weak and strong twisted blow-down limits

## Exact hypotheses and statements

Let 2/5<c<1, omega be finite, U,P be C1 whole-space rotating profile data with div U=0, and assume Hb: U is bounded and U(R dot) tends to zero in distributions as R tends to infinity. Define

    A=cI-omega J, Q_s=exp(omega*s*J), alpha=5-2/c>0,
    beta=(1-c)/c, V_s(x)=exp((1-c)*s) Q_s U(exp(s*A)x).

A052 gives E(R)=integral_(B_R)|U|^2=L*R^alpha+O(R^(alpha-1)), L>0 unless U=0. In particular G=sup_(R>0) R^(-alpha)E(R) is finite.

The following claims are confirmed.

1. V_s has a unique weak L2_loc limit V as s tends to infinity. Pairings with compactly supported smooth divergence-free tests converge with error at most C_test*exp(-s). V is divergence-free and has a representative of the form

    V(r*n)=r^(-beta) exp(-(omega/c)*log(r)*J)
                         F(exp((omega/c)*log(r)*J)n),

where F belongs to L2(S2;R3). Its ball energy is L_T*r^alpha, where L_T=norm(F)^2/alpha and 0<=L_T<=L. Convergence is strong in L2_loc if and only if L_T=L. This is C7.

2. Convergence is strong if either

    integral_1^infinity m(r) dr/r < infinity,
    m(r)=sup_(|y|>=r)|DU(y)|,

or, for some finite p>6/5 and all large R,

    norm(Omega)_(Lp(R<|y|<2R)) <= C*R^(3/p-1/c).

An L-infinity version of the latter reduces to any finite p by Holder. Under the first condition, on every fixed annulus a<|x|<b the L2 error is at most

    C_(a,b) [ integral_(a*exp(c*s)/4)^infinity m(r) dr/r
                  +exp(-c*s)+exp(-c*s*(5-alpha)/2) ].

Equivalently R^(-alpha/2) norm(U-V)_(L2(aR<|y|<bR)) tends to zero. This is C8.

3. If integral_(B_R)|Omega|=o(R^(3-1/c)), then V=0. Combined with either condition in statement 2, a nonzero U must have positive limsup of R^(-(3-1/c))*integral_(B_R)|Omega|. This is C9.

All rates and norm statements use exact rotating changes of variables. No pointwise derivative asymptotic follows from Hb alone.

## 1. Weak limit without pressure normalization in the time derivative

Direct differentiation of the profile equation gives

    partial_s V_s=-exp(-s)[div(V_s tensor V_s)+grad p_s],
    p_s(x)=exp((2-2c)*s)P(exp(s*A)x).

The factor exp(-s) is the derivative of physical time t=T-exp(-s). Exact norm scaling gives

    integral_(B_r)|V_s|^2 = r^alpha g(r*exp(c*s)) <= G*r^alpha,
    g(R)=R^(-alpha)E(R).

For a divergence-free compact smooth test psi, the pressure term vanishes by integration by parts, and

    |partial_s integral V_s dot psi|
       <=exp(-s) norm(Dpsi)_infinity G*r^alpha

for a ball B_r containing its support. Integrating to infinity proves convergence with the claimed rate.

The uniform ball bounds give subsequential weak L2_loc limits. If V1 and V2 are two of them, W=V1-V2 is divergence-free and annihilates all divergence-free compact tests. In particular testing against curls shows curl W=0 in distributions. Hence Delta W=0 distributionally and W is a smooth harmonic vector field. The same ball bounds give

    |W(x)| <= C*r^(-3/2)*(r+|x|)^(alpha/2),

by harmonic mean value and Cauchy-Schwarz on B_r(x). Since alpha<3, letting r tend to infinity gives W=0. Thus every subsequence has the same weak limit and the entire family converges. This also avoids any unstated global pressure or de Rham hypothesis.

The identity

    V_(s+sigma)(x)=exp((1-c)*sigma) Q_sigma V_s(exp(sigma*A)x)

passes to weak limits for every fixed sigma. To justify the sphere formula without taking the trace of an arbitrary L2 function on a sphere, introduce log-radius t=log(r)/c and the rotated, rescaled field

    Z(t,n)=exp((1-c)*t) Q_t V(exp(t*A)n).

It is locally L2 in (t,n). The preceding group identity makes it translation-invariant in t, as a distribution. Its t derivative is therefore zero and it equals a single F(n) almost everywhere. This proves the displayed representation and F in L2(S2). Polar integration gives the exact energy L_T*r^alpha. Weak lower semicontinuity and the known limit of the V_s ball norms give L_T<=L. Equality of weak-limit and approximant norms is equivalent to strong convergence on each ball, proving the final assertion of statement 1.

## 2. Dini control implies strong convergence

Fix K={a<|x|<b}, put R=exp(c*s) and D_R={aR<|y|<bR}. Exact scaling yields

    norm(partial_s V_s)_(L2(K))
       =R^(-alpha/2) norm(U dot grad U+grad P)_(L2(D_R)).

The first term is at most C*m(aR). For pressure, A031 applies under Hb and identifies its gradient with the canonical pressure gradient. Choose a smooth radial cutoff chi equal to one on aR/2<|y|<2bR, supported in aR/4<|y|<4bR, with |Dchi|<=C/R. The near pressure is the double Riesz transform of chi*(U tensor U). Its gradient L2 norm is bounded by

    C [R^(-1) norm(U)_infinity + m(aR/4)] E(4bR)^(1/2).

Here the transform commutes with the derivative, its L2 multiplier is bounded, and differentiating the tensor contributes U times DU. These are compactly supported H1 tensors, so no derivative at infinity is assumed.

For the remaining source, the differentiated pressure kernel has magnitude at most C|y-z|^(-4). The inner part |z|<=aR/2 is separated from D_R by aR/2; the outer part |z|>=2bR has |y-z|>=|z|/2. Using E(r)<=G*r^alpha and summing dyadic outer shells, its pointwise gradient is bounded by C*R^(alpha-4). The sum converges because alpha<3<4. Its L2(D_R) norm is consequently at most C*R^(alpha-5/2).

After normalization this gives

    norm(partial_s V_s)_(L2(K))
       <= C [m(aR/4)+R^(-1)+R^((alpha-5)/2)].

Integrating in s, with dr/r=c ds, proves the asserted annular Cauchy estimate and rate. The limit is the already unique V. Uniform small-ball bounds G*r^alpha, with alpha>0, extend strong annular convergence across the origin. Hence L_T=L. Twisted homogeneity gives the exact identity between this annular error and R^(-alpha/2)norm(U-V)_(L2(D_R)), including its rotation factors.

## 3. Natural vorticity control implies compactness

The curl scales as

    curl V_s(x)=exp(s) Q_s Omega(exp(s*A)x).

Thus the stated shell estimate bounds curl V_s in Lp on every fixed annulus. The fields are divergence-free and uniformly L2 there. An interior div-curl estimate on nested annuli K' compactly contained in K gives

    norm(DV_s)_(Lp(K'))
       <= C [norm(curl V_s)_(Lp(K))+norm(V_s)_(L1(K))].

This form follows by localizing the curl source in the fundamental-solution formula, applying the Lp singular-integral estimate for its derivative, and using interior harmonic estimates for the remainder. It is valid for 1<p<infinity. The L1 term is bounded by the L2 bound and finite annulus volume. In particular V_s is uniformly W1,p on smaller annuli. For p>6/5 the local Sobolev exponent exceeds two, so the embedding into L2 on a further smaller annulus is compact. At p=6/5 it is only continuous and this proof would fail, which explains the strict hypothesis.

Every sequence has a strongly convergent annular subsequence; weak uniqueness identifies its limit with V. The whole family therefore converges strongly there, and the small-ball estimate again extends the convergence across zero. This proves statement 2 under the second hypothesis.

## 4. Vorticity lower-growth consequence

Curl commutes with distributional limits. On each ball,

    norm(curl V_s)_(L1(B_r))
       =exp((1-3c)*s) integral_(B_(r*exp(c*s))) |Omega|.

The growth assumption in statement 3 makes this tend to zero. Hence curl V=0 and div V=0 on all of R3. The harmonic mean-value argument from Section 1 gives V=0 because its ball growth exponent is alpha<3. Under statement 2, this contradicts L_T=L>0 for any nonzero profile. This proves C9 with all its extra hypotheses retained.

## 5. Critical endpoint and limits of the conclusion

At c=2/5, A054 gives U in L2. Exact scaling preserves the total L2 norm, while the norm outside any fixed ball of positive radius tends to zero. Thus V_s tends to zero strongly away from the origin and weakly in L2 on all of R3. For every bounded continuous test f,

    integral f(x)|V_s(x)|^2 dx
       =integral f(exp(-s*A)y)|U(y)|^2 dy
       -> f(0) norm(U)_2^2

by dominated convergence, so the energy measures converge to norm(U)_2^2 delta_0. This does not prove U=0 at the endpoint.

The weak limit may be zero when L>0; strong convergence is not proved under Hb alone. Nor does existence of a formal or weak tail prove that every tail is compatible with the nonlinear identities or that far-field arguments can never yield an obstruction. Such universal claims require additional analysis. The main target remains open.
