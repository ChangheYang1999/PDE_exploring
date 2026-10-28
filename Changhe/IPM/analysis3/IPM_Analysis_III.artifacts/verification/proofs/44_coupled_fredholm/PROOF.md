# Coupled Fredholm theorem on the specified strong realization

## Exact statement and scope

This verifies Lemmas C'1 through C'4 and Theorem C' in the theory author's S2_L2_THEORY.md, section 5.2, as read on 2026-10-28. The conclusion is conditional. In particular, this proof does not establish any of the three nonlocal coupling hypotheses below for the modal profile.

Fix ell>1, k=1/ell, D=4ell-1, a=17/4 and eta=5/4. Let V be a globally Lipschitz C1 vector field with div V=2ell, with V1 odd in x and even in y, and V2 even in x and odd in y. Assume V1/x and V2/y have bounded continuous extensions. Let r=|X|, t=log r and

 w(X)=|cos theta|^(-2a) exp(mu(t)),
 mu(t)=-2a t for t<0, mu(t)=-eta t for t>=0,
 R=L2_P(w dX),
 G=L2(exp(-t/2)dt on t<0; exp(27t/4)dt on t>=0).

The subscript P denotes real or complex even-in-x, odd-in-y functions. Set d(t)=V2(0,exp(t))/exp(t). Assume

 0<dmin<=d(t)<=dmax,
 |d-D|+|d'|<=Cminus exp(2t) for t<=0,
 |d-ell|+|d'|<=Cplus exp(-(1-k)t) for t>=0.                 (A)

Set b=D-d-2d', p=b/d, H=exp(-integral_-infinity^t p), sigma=1/4 and kappa=3/8+k. Let omega=exp(-2sigma t) for t<0 and exp(2kappa t) for t>=0. The scalar domain B consists of beta=Hz, where z is locally absolutely continuous, z' is in L2(omega) and z(+infinity)=0. Its norm is

 ||beta||_B^2=|J|^2+||z'||_omega^2+||z-J||_(omega,t<0)^2+||z||_(omega,t>0)^2,
 J=z(-infinity).

All four terms are finite by the Hardy estimates proved in proof 38. Define Gamma by ||gamma||_Gamma=||gamma/(dH)||_omega. Assumption (A) implies that Gamma and G are the same set with equivalent norms. A beta=d beta'+b beta is an isomorphism B->Gamma.

Write E beta=x^2y beta(log r), T=V.grad-1 and

 D_R={h in R:T h belongs to R in distributions},
 ||h||_(D_R)^2=||h||_R^2+||T h||_R^2,
 Z=E B direct-sum D_R,
 Y=E G direct-sum R.

Give the direct sums the Hilbert product norms. They are unique decompositions because the angular factor |cos theta|^(4-2a) of |E beta|^2 w is not integrable unless beta=0 almost everywhere. Let P_J and P_R denote the coordinate projections of Y.

Assume the two lift coefficient bounds

 |q-d|<=M1 cos(theta)^2,
 |2V1/x+V2/y-1-b|<=M0 min(r^2,1) cos(theta)^2, q=V.X/r^2. (L)

Assume the bounded multiplier

 kappa_w=1+ell+(mu'/2)q+a tan(theta) V.grad(theta)

satisfies the following margin for a specified bounded nonnegative measurable function bplus:

 m=essinf(kappa_w-bplus)>0.                               (M)

For the IPM application bplus=(|grad rho|-partial_y rho)/2. Let C be the renormalized coupling, initially on a suitable dense class,

 C h=[U[h]+chi0(c[h]/3)X].grad rho,

where chi0 is a fixed smooth radial cutoff equal to1 near0. The hypotheses on its extension are:

 (E0) C extends to a bounded linear operator Z->Y.
 (EJ) P_J C:Z->G is compact.
 (EG) P_R C restricted to D_R extends to a bounded linear operator C_R:R->R. For every epsilon>0 there is a compact K_epsilon:R->R such that

 Re<C_R h,h>_R <= integral (bplus+epsilon)|h|^2w + Re<K_epsilon h,h>_R

for all h in D_R.

Then Lren=T+C:Z->Y is Fredholm of index0. For every epsilon in (0,m),

 (m-epsilon)||h||_R <= ||P_R Lren h||_R+||K_epsilon h||_R, h in D_R. (1)

The strain functional

 c[E beta+h]=(1/4)integral_R exp(2t)beta(t)dt
                 +(1/pi)integral_R2 sin(3theta)r^(-3)h(X)dX        (2)

is absolutely convergent and bounded on Z. Consequently, if zeta belongs to Y, then Lred=Lren+c[.]zeta:Z->Y is Fredholm of index0 as well. Either operator is an isomorphism if and only if it is injective. These conclusions do not give a numerical inverse norm.

## The pure transport endpoint and its core

Topics38 and43 give A:B->Gamma and T_R:D_R->R as isomorphisms. For clarity the ingredients used here are explicit. The scalar inverse is

 A^(-1)gamma=-H(t)integral_t^infinity gamma(s)/(d(s)H(s))ds.

Since bplus>=0, (M) implies kappa_w>=m>0. The global flow Phi_s of V gives the strongly continuous group S_s h=exp(-s)h(Phi_s) on R. Change of variables gives ||S_s||<=exp(-m s) for s>=0. Its generator equals the maximal distributional T_R: pairing the weak equation with transported compactly supported tests gives S_s h-h=integral_0^s S_u(T h)du, and the difference quotient converges in R. Hence

 T_R^(-1)f=-integral_0^infinity S_s f ds, ||T_R^(-1)||_(R->R)<=1/m.

This also proves closedness of the maximal domain. The integral is a Bochner integral.

The theory author's core assertion is valid. First use smooth even angular cutoffs that vanish when |cos theta|<epsilon and equal1 when |cos theta|>2epsilon. Because V.grad theta=O(cos theta), their transport derivatives are uniformly bounded and supported on shrinking angular sets. Both the lost h and T h terms tend to zero by dominated convergence in R. Next cut off r near0 and infinity using cutoffs smooth in log r. Their transport derivatives are uniformly bounded because q is bounded, and again the error tends to zero. Finally use ordinary Friedrichs mollification on a compact set away from x=0 and0. There V is C1 and w is bounded above and below, so the standard mollifier commutator tends to zero in L2: its kernel contains the bounded difference quotient of V and converges to the local div V correction. This gives graph convergence. Symmetrization preserves the parity class. The radial knot causes no difficulty because w is locally Lipschitz and bounded on that compact set.

For this core integration by parts gives Re<T h,h>_R=-integral kappa_w|h|^2w. The multiplier is bounded, so graph approximation extends this identity to all D_R. There is no boundary contribution at the axis or at the radial knot.

The exact lift identity is

 T(E beta)=E(A beta)+Err beta,
 Err beta=x^2y cos(theta)^2[a1 beta'+a0 beta],
 a1=(q-d)/cos(theta)^2,
 a0=(2V1/x+V2/y-1-b)/cos(theta)^2.

It holds first locally in the weak sense and then in Y. The radial weight is precisely that of G. Thus

 ||Err beta||_R<=sqrt(Ia)[M1||beta'||_G+M0||min(exp(2t),1)beta||_G],
 Ia=2 B(1/4,3/2).

Both scalar terms are bounded by ||beta||_B, as shown in proof 43: H is bounded and H'=O(exp(2t)) at the left end; H^2 exp(27t/4) is comparable to omega at the right end. The operator T has block form [A,0;Err,T_R], so it is an isomorphism. This is the required endpoint, on the same domain used throughout the homotopy.

For the actual finite modal field, the qualitative finiteness in (L) follows from its verified endpoint expansions and its finite angular regularity. On compact annuli evenness in x and two angular derivatives make the quotients bounded. Near0, V=(-A0 x,Dy)+a cubic polynomial+O(r^5 log r), with the same order after two angular derivatives. Here A0=2ell-1 and -2A0+D-1=0. It follows that a1=-(A0+D)+O(r^2), while a0=O(r^2). At infinity V=ell X+O(r^k), with its angular derivatives, giving a1,a0=O(r^(k-1)). This proves existence of finite constants M0,M1; it does not certify their numerical sizes. The O(r^4 log r) remainder in V1/x is harmless in an O(r^2) bound. Any claim of a log-free higher remainder would require a separate argument.

## Bounded strain and exact constant

Cauchy-Schwarz in R proves the second term in (2) is absolutely integrable, with sharp norm on the parity subspace

 c_R=(1/pi)[Istrain(1/(2a-4)+1/(4-eta))]^(1/2),
 Istrain=integral_0^(2pi)|cos theta|^(2a)sin(3theta)^2dtheta.

The kernel divided by w belongs to R and has the same parity, so this is also the functional norm. Its radial integral is 2/9+4/11=58/99. From sin(3theta)=sin(theta)(4cos(theta)^2-1),

 Istrain=2[16 B(3/2,a+5/2)-8 B(3/2,a+3/2)+B(3/2,a+1/2)].

The accompanying independently executed Arb code encloses both Ia and c_R at384 and768 bits, verifies overlap, and proves

 6.99215347811231949457290557304298510315401320381766176750
    < Ia <
 6.99215347811231949457290557304298510315401320381766176753,

 0.20756986610668143480705395943043232139891409606278751321
    < c_R <
 0.20756986610668143480705395943043232139891409606278751324.

In particular c_R<0.207570; the six-digit decimal is an upper bound, not an exact equality.

For the jet term there is a useful quantitative representer. Put

 F(t)=exp(2t)H(t), Q(s)=integral_-infinity^s F(t)dt.

Assumption (A) gives Q(s)=O(exp(2s)) at the left end. Since H(t)=O(exp(-(3-k)t)) and k<1, F is integrable at the right end, so Q is bounded there. Consequently Q/sqrt(omega) is in L2(R). If v=z', then z(t)=-integral_t^infinity v(s)ds. Tonelli followed by Cauchy-Schwarz, applied first to absolute values, proves

 integral |F(t)z(t)|dt <= integral |v(s)|Q(s)ds
                         <=||v||_omega ||Q/sqrt(omega)||_2.

Fubini is therefore justified and

 c[E beta]=-(1/4)integral_R v(s)Q(s)ds,
 |c[E beta]|<=(1/4)||Q/sqrt(omega)||_2 ||z'||_omega.

This supplies a norm bound rather than merely a separate endpoint limit for each beta. Together with c_R it proves (2) and its boundedness on Z.

## The coupled homotopy and the index

Set S_s=T_R+s C_R:D_R->R for0<=s<=1. Use the fixed graph norm of T_R. These are bounded operators between Hilbert spaces, and the path is norm continuous because C_R is bounded on R. Fix epsilon in (0,m). The energy identity and (EG) give

 Re<-S_s h,h> >= (m-epsilon)||h||_R^2-||K_epsilon h||_R||h||_R.

Here kappa_w-s bplus>=kappa_w-bplus>=m uses bplus>=0. Dividing by ||h|| proves (1) at s=1 and gives the corresponding estimate for every s. Moreover

 ||T_R h||<=||S_s h||+||C_R|| ||h||.

It follows that a fixed finite constant C, independent of s, satisfies

 ||h||_(D_R)<=C(||S_s h||_R+||K_epsilon h||_R).              (3)

The map K_epsilon:D_R->R is compact, being the composition of the bounded inclusion D_R->R and a compact operator on R.

For completeness, (3) implies finite kernel and closed range. If the kernel had infinite dimension, an orthonormal sequence in its graph norm would have a subsequence with convergent K_epsilon images. Applied to differences, (3) would make this subsequence convergent in graph norm, a contradiction. For the closed range, work in the graph-orthogonal complement of the finite kernel. If no coercive bound there existed, unit vectors h_n in that complement would satisfy S_s h_n->0. A subsequence of K_epsilon h_n converges, so (3) makes h_n converge in graph norm to a unit vector in both the kernel and its orthogonal complement, again a contradiction. Thus each S_s is upper semi-Fredholm.

A separate adjoint estimate is unnecessary here, because the whole path has this property. The relevant index fact has a short proof. For any upper semi-Fredholm operator S:D->R, split D=N direct-sum Nperp and R=M direct-sum Mperp, where N=ker S is finite and M=ran S is closed. The block S:Nperp->M is an isomorphism. For every sufficiently close operator this block remains invertible. Elementary invertible block operations reduce that nearby operator to this isomorphism plus a Schur-complement map from finite-dimensional N to Mperp. If Mperp is infinite-dimensional, no such nearby operator can be Fredholm; a finite-dimensional map cannot have finite-codimensional range there. If Mperp is finite-dimensional, every nearby operator is Fredholm, with index dim N-dim Mperp. Thus within the upper semi-Fredholm set, the Fredholm set is both open and closed, and the index is locally constant. The connected path S_s starts at the isomorphism T_R. Every S_s is therefore Fredholm of index0.

In the jet/remainder coordinates,

 Lren = M+K1,
 M=[A,0;Err+P_R C E,S_1],
 K1 h=E P_J C h.

The lower off-diagonal block is bounded by (E0) and (L). It need not be compact. The first diagonal block is an isomorphism; the second is Fredholm of index0. The exact factorization

 M=[1,0;(Err+P_R C E)A^(-1),1] [A,0;0,S_1]

proves M is Fredholm of index0. K1 is compact by (EJ), so Lren has the same index. Formula (2) then makes c[.]zeta a bounded rank-one operator for every zeta in Y, which proves the statement for Lred. The open mapping theorem supplies a bounded inverse once injectivity is established, but no explicit bound is provided by this argument.

## The actual bordered vector and scope of normalization

The theory author's vector is zeta=(ell gfar-k yKP)/d_border, where d_border is the nonzero scalar denominator of the tail elimination, distinct from the function d(t). Its membership follows at the scope of proof 39 if the cutoffs and columns are those of Proposition B:

 gfar=(1-chi0) X.grad rho-k Phihat,
 yKP=Lfix KP+(c[KP]/3)chi0 X.grad rho-ell Phihat.

Near0, gfar vanishes and yKP=x^2y O(r^2), since the linear strain cancels. At infinity both have order at most r^(2k-1)(1+|log r|), with a smooth angular x^2y cofactor. Subtracting the axis cofactor leaves another cos(theta)^2 factor. The remainder's angular squared power is8-2a=-1/2, and its far radial squared power is4k-5/4<0 for the actual k<5/16. The jet G norm has the same far power. Near0 the radial squared power is12-2a=7/2>0. Thus zeta belongs to Y. This is membership, not a certified Y norm.

The cancellation must be built into C. The separate local term c[.]chi0 X.grad rho/3 does not take values in Y, as the annular counterexample in proof 41 proves. It cannot be imported as a bounded Y-valued perturbation of the radial Lfix realization.

Finally, J is a continuous coordinate on Z. For arbitrary weighted L2 remainders, this statement alone does not assert classical pointwise Taylor differentiability at0. An application requiring a classical x^2y leading expansion needs the corresponding regularity of its solution. The nonlinear iteration and derivative-loss problem are not settled by this linear theorem.

## Dependencies and verdict

Dependencies: topics01 (signs and strain), 31 (tail elimination), 38 (scalar Hardy space), 39 (residual membership), 41 (normalization obstruction), 43 (pure transport). The numerical angular constants use only exact rational parameters and Arb special functions, not values copied from another team.

Verdict: CONFIRMED as the fully stated conditional theorem. (E0), (EJ), (EG), the actual positive axis rate, the actual positive global margin, injectivity and a numerical inverse bound remain open until separately verified. The qualitative lift bounds follow from the verified modal expansions; their numerical constants remain uncomputed.
