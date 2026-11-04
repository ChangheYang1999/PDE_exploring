# Final check of the physical singular-set statements

This is a final-phase recheck of existing A475 and its stated combination with A3249. It uses no new theorem direction. The complete existing C comparison and its explicit correction have been checked. A3255 confirms the exact statements below; A3254 remains REFUTED for the original auxiliary path only.

## 1. Exact definitions and statements

Fix 0<c<1, finite real omega and terminal time T. Let U in C1(R3;R3). Define J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, Q_s=exp(omega sJ), and for all x in R3 and t<T set

    tau=T-t, s=-log tau, y=exp(sA)x,
    u(x,t)=tau^(-(1-c))Q_s U(y), G=DU.

Use the Euclidean vector norm and an orthogonally invariant matrix norm. On R3 minus{0}, define Sigma_v and Sigma_I as the sets where the joint terminal limsups of tau^(1-c)|u(x,t)| and tau|Du(x,t)|, respectively, are strictly positive as (x,t)->(x_*,T), t<T. For x_*!=0, define Sigma_L as the set of x_* where Du is unbounded on N times(T-delta,T) for every open neighborhood N of x_* and every delta>0. Infinite limsups are allowed.

These sets are invariant under exp(sigma A) for every real sigma, and Sigma_I is contained in Sigma_L. Each nonempty set therefore contains the complete curve {exp(sigma A)x_*:sigma in R}, crossing every sphere centered at0 and approaching0 and infinity at its two ends. The curve is straight on the rotation axis; away from the axis it rotates when omega is nonzero. This is a twisted dilation curve, not a fluid trajectory.

The exact equivalences are

    Sigma_v empty iff U->0 uniformly at infinity;
    Sigma_I empty iff G->0 uniformly at infinity;
    Sigma_L empty iff |G(y)|<=C(1+|y|)^(-1/c) for some C<infinity.    (1)

The third condition implies Dini integrability integral_1^infinity m(r)dr/r<infinity, m(r)=sup_(|y|>=r)|G(y)|. Dini implies the second condition. Scaling alone does not give either missing converse. No momentum equation, incompressibility, pressure or boundedness of U is assumed here.

If additionally U is in C2, tends uniformly to zero, and with P in C1 solves

    ((1-c)I+omega J)U+G(Ay+U)+grad P=0, div U=0,

with1/3<c<1, A3249 identifies the three derivative premises: G->0, Dini, and the natural bound in the third line of(1). Thus Sigma_I and Sigma_L are empty simultaneously in that profile class. Uniform velocity decay still does not supply those derivative premises.

## 2. The exact transformation and the first two equivalences

Since exp(sA)=exp(cs)Q_s^T, differentiation gives

    Du(x,t)=tau^-1 Q_s G(y)Q_s^T.

For real sigma set x'=exp(-sigma A)x and t'=T-exp(-sigma)(T-t). Then s'=s+sigma and y'=y. The two normalized norms are unchanged and |Du(x',t')|=exp(sigma)|Du(x,t)|. This invertible continuous transformation maps all terminal neighborhoods at x_* to terminal neighborhoods at exp(-sigma A)x_*. Using both signs of sigma proves invariance of each set. If a terminal neighborhood has bounded Du, its normalized gradient tends to zero there, proving the inclusion. The radial identity |exp(sigma A)x_*|=exp(c sigma)|x_*| proves the curve statement without any flow assumption.

If U tends uniformly to zero, then |y|=tau^-c|x| tends to infinity in every joint limit at x_*!=0, proving Sigma_v empty. Replace U by G for the forward gradient implication. Conversely, if either uniform limit fails, choose epsilon>0 and y_n with r_n=|y_n|->infinity and the corresponding norm at least epsilon. Put s_n=log(r_n)/c, t_n=T-exp(-s_n), x_n=exp(-s_n A)y_n. Then |x_n|=1. A subsequence converges to a nonzero x_* by compactness. The corresponding normalized norm at (x_n,t_n) is at least epsilon, putting x_* in the required set. A fixed spatial point was not assumed along this sequence.

## 3. Local gradient bounds, the natural rate and Dini

The natural bound gives |Du(x,t)|<=C tau^-1|y|^-1/c=C|x|^-1/c for x!=0, hence Sigma_L is empty. Conversely, if Sigma_L is empty, every point of the unit sphere has one neighborhood and terminal time interval with a finite Du bound. A finite subcover supplies a common bound M and interval on the sphere. For large y, use s=log|y|/c and x=exp(-sA)y on that sphere. The chain rule gives |G(y)|<=M|y|^-1/c. Compact continuity supplies the global(1+|y|) bound.

The resulting m(r)<=C r^-1/c is Dini because c>0. Conversely, Dini and monotonicity of m force m finite eventually and m(r)->0. Compact continuity then makes m finite at every positive radius. This gives the second line of(1).

There is also an exact extended-real identity for every rho>0:

    integral_(T-1)^T sup_(|x|>=rho)|Du(x,t)|dt
       =(1/c)integral_rho^infinity m(r)dr/r.

For s in[0,infinity), the linear map x->exp(sA)x takes the exterior of radius rho onto that of rho exp(cs); the supremum equals exp(s)m(rho exp(cs)). The substitution dt=exp(-s)ds cancels that factor, and r=rho exp(cs) proves the identity, including the infinite case. Thus Dini is a time-integrated exterior gradient bound, not by itself a uniform terminal gradient bound for arbitrary profiles.

## 4. Local-domain version and the PDE interface

If the self-similar formula is given only for |x|<rho and T-t<delta0, it suffices to assume Du is uniformly locally bounded up to T near every point of one sphere |x|=b with0<b<rho. Compactness gives a common bound M and interval there. Given large y, set s=log(|y|/b)/c and x=exp(-sA)y. Then |x|=b and |G(y)|<=M b^(1/c)|y|^-1/c. This uses only points in the stated physical domain and asserts no physical invariance outside it.

For the additional PDE statement in Section1, uniform U decay implies boundedness and distributional blow-down by dominated convergence. The exact C2/C1 hypotheses and1/3<c<1 therefore allow A3249. Combining its derivative equivalences with(1) proves the claimed emptiness equivalence, and failure gives a whole twisted dilation curve in Sigma_I and hence Sigma_L. These are possible singular-set shapes under a conditional failure, not an exclusion of the curves and not an Euler singularity construction. The limits are joint in space and time; separate limits at every fixed spatial point have not been substituted.

The complete106-line A475 source was freshly read and is captured. The separate PDE dependency is A3249. No diagnostic or formal build was used.
