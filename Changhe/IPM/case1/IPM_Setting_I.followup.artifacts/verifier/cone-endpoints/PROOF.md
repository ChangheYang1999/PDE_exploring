# Source endpoint criteria that use only a closed cone

Date: 2026-10-20. Status: complete local proof and dependency audit. This theorem concerns cones; it does not replace the full-neighborhood hypotheses of the global IPM problem by weaker ones without saying so.

## Domain, hypotheses and statements

Write s=-r<0 and

    C_k(R)={(-r,y):0<r<=R, |y|<=k r} union {(0,0)}.

Regularity C^(n,alpha) on this closed cone means that the derivatives from its interior through order n extend continuously to the cone and vertex, and that derivatives of order n satisfy a uniform alpha-Holder bound there. Smoothness below is required in the open punctured cone. No values at (0,y), y nonzero, are given.

Let A>1 and W=(a,b). Assume on a sufficiently large cone that

    a f_s+b f_y=f, a_s+b_y=A+1,
    W(0)=0, DW(0)=diag(A,1), f_y(0)=g>0,

with a even in y and b,f odd in y. The letter a is a velocity component, not the density factor at the other equilibrium.

For the geometry, write the supplied cone as C_K(R_*), and work on strictly smaller apertures and at depths r<=R_*/2. Choose k_1<k_2<K and 0<c<1/4 with k_1+c<k_2(1-c). A ball of radius c r centered at (-r,y), |y|<=k_1 r, then has (1-c)r<rho<(1+c)r<R_* and |eta|<(k_1+c)r<k_2 rho. It lies strictly inside the supplied punctured cone. Choose the fixed outer section for radial integration at r=R_*/2 and a smaller aperture, so it is compactly inside that cone. Start every working dyadic decomposition at an explicitly smaller radius if necessary. Discarding finitely many initial annuli preserves summability. All endpoint assertions below are local as r tends to zero; no estimate at the supplied outer cap is used.

The following statements hold.

1. Let n>=2 be even, 0<alpha<1, and f,W be C^(n,alpha) on the closed cone. If alpha>1-n/A, then

       |f_(y^(n+1))(-r,0)|<=C r^(alpha-1),
       r^(n/A) f_(y^(n+1))(-r,0) ->0.

   This statement uses transport and divergence, and no curl or full-plane inverse.

2. Let f,W be C^(2,alpha). Put q=4/A and R_j=2^(-j)R. If, on cone annuli in a cone wider than the one used for characteristics,

       d_j=R_j^(q-1) sup_(R_j/2<=r<=R_j, |y|<=2k r)
                       (|D^4f|+|D^4W|),
       sum_j d_j<infinity,

   then r^q f_yyyyy(-r,0)->0. This also uses only transport and divergence.

3. Suppose additionally b_s-a_y=-f_s, 1<A<2, q=4/A, and

       |D^4f|<=C r^(-p_d), |D^5f|<=C r^(-P),
       0<=p_d<q-1, P finite, alpha>3-q

   on a larger cone. Then statement 2 applies. The curl equation is used only for an interior elliptic estimate. No prescribed global inverse, full neighborhood, or fifth-order source normal form is used.

For every odd j=n+1 let H_j be a positive solution of

    a(s,0) H_j'(s)+(j b_y(s,0)-1)H_j(s)=0.

Then H_j(-r) is comparable to r^(-n/A), and each vanishing assertion above is equivalently ell_j=lim [f_(y^j)/j!]/H_j=0. These are constants at the source. They are not the B_j at the distinct normalized center.

For A>n, the strict exponent in statement 1 is necessary for its zero-endpoint conclusion within this cone formulation: an actual coupled cone solution exists at alpha=1-n/A with nonzero endpoint. For statement 3 our examples establish only failure at the simultaneous boundary alpha=3-q and p_d=q-1, when 4/3<A<2. They do not establish individual sharpness of either inequality with the other kept strict.

## Proof of statement 1

Use f_j=partial_y^j f, and similarly for a,b; put D=a partial_s+b partial_y and h=f_1/a. Taylor estimates and parity on the cone give

    a=As+O(r^2), b=y(1+O(r)),
    a_s=A+O(r), b_1=1+O(r), f_1=g+O(r), f_s=O(|y|).

All estimates follow along vertical segments and radial segments contained in the cone. Shrink R so that a is negative off the vertex. Set K=f_n-h a_(n-1). Differentiating the transport equation n times and using the derivative of divergence gives

    (D+n b_1-1)K=F,
    F=(a_1 a_(n-1)/a-a_n)(f_s+b h)
       -sum_(k=1)^(n-1) binom(n,k) a_k partial_s f_(n-k)
       -sum_(k=2)^(n-1) binom(n,k) b_k f_(n+1-k)
       +(a_s-(n-1)b_1)h a_(n-1).                    (1)

For completeness, D h=(1-b_1-a_s)h-(a_1/a)(f_s+b h) follows by one differentiation. Also D a_(n-1)=-a b_n+b a_n because divergence is constant. In D(f_n-h a_(n-1)), the two terms containing b_n f_1 cancel; the remaining product and binomial terms are exactly (1). Only smooth interior points are used in this computation.

Let c=a_n(0), lambda=g c/A. Holder continuity gives

    a_(n-1)=c y+O(|y|r^alpha), h=g/(As)+O(1).

For T=K+lambda y/s, therefore,

    |T|<=C(|y|^alpha+|y|r^(alpha-1)).                 (2)

In each binomial product of (1), parity puts a factor O(|y|) in one factor, with the derivative needed for this bound of order at most n. The terms with a_n and h a_(n-1) have leading sum (A-n)lambda y/s; all their remainders are O(|y|r^(alpha-1)). The remaining product a_1 a_(n-1)(f_s+b h)/a is O(|y|^3/r^2)=O(|y|). Since

    (D+n b_1-1)(y/s)=(n-A)y/s+O(|y|),

we have

    (D+n b_1-1)T=O(|y|r^(alpha-1)).                 (3)

Here no Taylor polynomial at a point outside the cone has been used.

Choose theta with

    (1-alpha)/(n-1+alpha)<theta<1/(A-1).

This is possible exactly when alpha>1-n/A. Let eta=|y|/r and follow a backward characteristic for time t_0=theta log eta. Inside the larger cone, the equations for its depth R(t) and height Y(t) give

    d log R/dt=A+O(R), d log|Y|/dt=1+O(R).

As R decreases backwards, the accumulated errors have absolute value at most C r. Consequently R(t) and |Y(t)| are uniformly comparable to r e^(At) and |y|e^t. With delta=1-theta(A-1)>0, throughout this time interval

    |Y(t)|/R(t)<=C eta^delta.

Choose the starting angular bound eta_0 sufficiently small that C eta_0^delta is less than the available cone aperture. This proves, by continuation up to a hypothetical first exit, that the whole characteristic segment stays in the larger cone. The segment need not stay in the narrower cone of its starting point.

The integrating factor in (3) is comparable to e^((n-1)t). Applying (2) at t_0 yields boundary terms bounded by

    C |y|^alpha e^((n-1+alpha)t_0),
    C |y|r^(alpha-1)e^((n-A(1-alpha))t_0).

The first is at most C|y|r^(alpha-1), since alpha+theta(n-1+alpha)>1. The second has the same bound, since n-A(1-alpha)>0. The integral of the right side of (3) is bounded by

    C |y|r^(alpha-1) int_(t_0)^0 e^((n-A(1-alpha))t)dt
       <=C' |y|r^(alpha-1).

Thus |T| has that bound. Subtracting the correction in its definition gives |f_n(-r,y)|<=C|y|r^(alpha-1). For fixed r>0 the solution is smooth at the axis point, so division by y and the limit y->0 give statement 1. Finally a(s,0)=-Ar+O(r^2) and j b_y(s,0)-1=n+O(r). The equation for H_j becomes d log H_j/d r=-n/(Ar)+O(1), whose integration proves H_j(-r)=c_j r^(-n/A)(1+O(r)), c_j>0. The strict exponent gives the claimed zero limit.

## Proof of statement 2

We provide the characteristic and annular argument to specify exactly where regularity is used. On the smaller cone use (1) with n=4, now with K=f_4-h a_3 and without subtracting a vertex fourth derivative. At depth r in annulus N, put

    M=C r^(1-q) sum_(|j-N|<=2)d_j.

This bounds D^4(f,W) on suitable balls of radius c r and vertical segments to the axis. Such balls lie in the larger cone if c is a small fixed positive number. The pair has uniformly bounded second derivatives by the closed-cone regularity.

If q>2, a Taylor estimate for a second derivative along an interior segment of length t<=c r gives |D^3(f,W)|<=C(t^(-1)+Mt). Choose t=min(c r,M^(-1/2)), with t=c r if M=0. Thus third derivatives are bounded by L=C(r^(-1)+sqrt M), and L^2<=C(r^(-2)+M). If 0<q<=2, integrate fourth derivatives along rays from a fixed outer cone section. The contribution of annulus j is at most C R_j^(2-q)d_j. This is summable, and the third derivatives on the fixed compact outer section are bounded. Thus take L=C in this case.

Parity and these bounds give |a_3|+|f_syy|<=C|y|M, |b_2|+|f_2|<=C|y|L, and |b_3|+|f_3|<=CL. Substitution in (1) gives

    |F|<=C|y|(M/r+L^2), |K|<=C r^(1-q)d_N,            (4)

where a bounded number of neighboring d_j can replace d_N without changing any conclusion.

Follow a backward characteristic from (-r,y) to its first lateral exit |Y(T)|=k R(T) from the smaller cone. This occurs at finite negative time for y nonzero, since d log(|Y|/R)/dt=1-A+O(R)<0. As y->0 for fixed r, T->-infinity and R(T)->0. Let J(t)=exp(int_0^t(4b_y-1)dt). Since Aq=4,

    d/dt log[J(t)|Y(t)|/|y| (r/R(t))^q]=O(R(t)),
    J(t)|Y(t)|/|y|<=C(R(t)/r)^q.                     (5)

The errors are integrable because int_T^0 R(t)dt<=C r. Integrate (D+4b_y-1)K=F from T to zero. By (4), (5) and the exit equation, the boundary contribution divided by |y| is at most C r^(-q)d_(N(T)), which tends to zero by summability. The forcing integral after division by |y| is bounded by C r^(-q) times

    sum_(j>=N-3)d_j+r^(q-2), q>2;
    sum_(j>=N-3)d_j+r^q,     0<q<=2.

Indeed, each depth annulus takes bounded characteristic time; its M contribution is a bounded number of neighboring d_j. The other integrands are R(t)^(q-2) or R(t)^q, respectively, and have finite integrals with the stated bounds. The correction |h a_3|/|y| is at most C r^(-q) times neighboring d_j. Let y->0 at fixed r. Smoothness at the open axis point gives the same two bounds for r^q|f_5(-r,0)|. Both tend to zero. This proves statement 2 for every A>1, equivalently every 0<q<4.

The argument uses only interior balls, vertical segments, rays and characteristics in the larger closed cone. The compact outer section is also within that cone. It requires no extension across s=0.

## Proof of statement 3

Divergence and curl imply Delta a=f_sy and Delta b=-f_ss. For a point Z=(-r,y) of a smaller cone choose ell=c r so that B_ell(Z) lies in the larger cone and has comparable depths. For a derivative of order two of either velocity component, subtract its value at Z and call the resulting function u. It solves Delta u=G, where G is a signed fourth density derivative. On the ball,

    |u|<=C ell^alpha, |G|<=M, |grad G|<=L,
    M<=C r^(-p_d), L<=C r^(-P).

We need the elementary logarithmic Poisson estimate

    |D^2u(Z)|<=C[ell^(alpha-2)
                         +M(1+log(2+ell L/M))].          (6)

The last term is zero if M=0. To prove it, rescale to the unit disk, so the source bounds are ell^2M and ell^3L. Multiply the source by a smooth cutoff supported in that disk and equal to one on its central three quarters, and convolve with log|X|/(2pi). The potential itself is bounded by C ell^2M. The remaining function is harmonic on the central disk; differentiating its smooth radial mean-value representation twice bounds its second derivative by its supremum. For the potential's second derivative, the principal-value kernel has size C|X|^(-2) and zero angular mean, besides a bounded delta term. On radius delta subtract the central source value and use its gradient, giving C delta ell^3L. Outside that radius use the source bound, giving C ell^2M(1+log(1/delta)). Choose delta=min(1/8,M/(M+ell L)) and rescale back. This proves (6), including its scaling and the harmless contact term.

The function x[1+log(2+B/x)] is increasing in x>0 and B>=0. Consequently actual upper bounds for M and L may be substituted even if M is much smaller than its bound. Formula (6) gives

    |D^4W|<=C[r^(alpha-2)+r^(-p_d)(1+|log r|)].

Therefore on dyadic cone annuli

    d_j<=C[R_j^(q+alpha-3)+(1+j)R_j^(q-1-p_d)].        (7)

Both exponents are positive under the stated strict inequalities, so the sum converges and statement 2 gives the endpoint. All cutoff convolutions and harmonic averages above are confined to one ball inside the cone. No global inverse is prescribed or used. This proves statement 3.

## Critical examples and precise sharpness

Use the fully proved construction in ../higher-source-cone/PROOF.md. That theorem gives, for any odd m>=3, A>1 and g>0, an actual analytic coupled solution on a cone with

    f=g y+v, W=(As,y)+V,
    q_m=(m-1)/A, p_m=m-q_m,
    G_m=C r^(-q_m), C nonzero,
    |D^h(v,V)|<=C_h r^(p_m-h), V(-r,0)=0.

Its exact regularity, including failure of the next stronger Holder exponent, is proved there by the leading homogeneous term; it is not inferred from a truncated series. It uses a freely selected local velocity, not a canonical full-plane inverse.

For even n and A>n choose m=n+1. Then p_m=n+alpha_* with alpha_*=1-n/A in (0,1). This pair is C^(n,alpha_*) on every smaller closed cone and has

    r^(n/A) f_(y^(n+1))(-r,0)=(n+1)! C nonzero.

It satisfies transport, divergence and curl. Thus the zero conclusion in statement 1 fails at equality even with curl imposed. The trace bound in statement 1 does not fail for this example: the trace exactly has size r^(alpha_*-1). Sharpness here refers to the zero endpoint.

For 4/3<A<2 choose m=5. Then p_m=5-q in (2,3), so alpha_*=3-q. On every fixed nontrivial smaller cone annulus the fourth and fifth density derivative suprema are comparable to r^(1-q) and r^(-q), respectively. The upper bounds follow from the construction; lower bounds follow from a nonzero fourth angular derivative on a fixed small nonzero ray and the exact fifth derivative on the axis. Thus p_d=q-1 and P=q, while r^q G_5=C nonzero. The associated d_j are bounded above and below by positive constants. This disproves a version of statement 3 in which both strict inequalities are replaced by equality together. It says nothing about a version in which only one becomes an equality while the other remains strict.

## Dependency and scope audit

The proofs above spell out all local steps of ../source-estimates/PROOF.md, ../weighted-source/PROOF.md and ../density-source/PROOF.md on closed cones. Their original applications to global IPM use additional arguments to supply these cone hypotheses, including local velocity regularity and transport propagation from the normalized center. Those implications are separate dependencies of that application. They are not ingredients of statements 1-3 once the cone hypotheses are assumed.

No full-neighborhood extension, far-field matching, center normalization, coefficient identity for c_l or simultaneous cancellation of center B_3,B_5,B_7 is proved by the cone examples. Thus these sharp local criteria do not answer YES_inf, NO_inf or isolation of the published candidate. The word sharp is confined to the exact cone statements just proved.
