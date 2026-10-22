# Canonical face traces after radial homogeneity subtraction

Topic 56. Written before numerical implementation; the actual write time and source snapshot are in evidence/proof_first.json. Status OPEN pending independent proof and constant audits.

## 1. Exact statement and scope

Let 5.5<a<6.5, 2.5<b<3.5 and A=a+b, so 8<A<10. Let D be the real smooth compact functions supported away from both coordinate axes, even in x and odd in y. Put w=|x|^(-2a)|y|^(-2b). For h in D take the canonical full-plane IPM velocity U, with multipliers (xi eta,-xi^2)/(xi^2+eta^2), including its local term. The rectangular orders6,3 mean subtraction of x-degrees0 through5 and y-degrees0 through2. Its nonzero face traces in these orders are

    u_1,0(x), u_1,2(x), u_2,1(x), where u_i,j=partial_y^j U_i(x,0)/j!,
    v_1,1(y), v_1,3(y), v_1,5(y), v_2,0(y), v_2,2(y), v_2,4(y),
    where v_i,l=partial_x^l U_i(0,y)/l!.

The statement below is given for an x trace u_i,j. It also holds for a y trace with a,b exchanged and the normal order j replaced by l. The tangential parity is odd for u_1,j, even for u_2,j; it is even for v_1,l, odd for v_2,l.

Set

    t=A-j-1, sigma=b-j-1/2, beta=A-j-1/2.

In every listed case sigma is positive and noninteger. Write sigma=s+theta with integer s>=0 and0<theta<1, and K=s+1. Let P be the first nonnegative integer of the tangential parity strictly greater than t. Let Lset be all nonnegative integers of that parity less than t. No allowed power equals t in the working window. Set

    c_l,j[h]=partial_x^l partial_y^j U_i(0,0)/(l!j!),
    u^natural_i,j(x)=u_i,j(x)-sum_{l in Lset} c_l,j[h]x^l.          (1)

For I=(-2,-1) union (1,2), fix the explicit intrinsic Sobolev norm

    ||f||_Hsigma(I)^2 = sum_{d=0}^s integral_I |f^(d)|^2
      + integral_I integral_I |f^(s)(x)-f^(s)(y)|^2
                                /|x-y|^(1+2theta) dx dy.         (2)

Define

    ||u||_T(beta,sigma)^2
       =sum_{k in Z} 2^(k(1-2beta)) ||u(2^k .)||_Hsigma(I)^2.     (3)

Then the finite constant C below proves

    ||u^natural_i,j||_T(beta,sigma) <= C ||h||_L2(w).              (4)

Consequently the combination (1) extends uniquely by density from the parity subspace of L2(w) into the completion of (3). It is this renormalized trace combination that extends, not the individual canonical moments, nor a chosen canonical velocity on arbitrary pure-weight data. The result settles this precisely specified annular trace estimate. It does not settle variable coupling, edge transport matching, conormal derivative estimates of (4), or a global inverse.

## 2. Constants and elementary Sobolev estimates

All constants here are explicit. Write

    D_l,j=(l+j+1)!/(2pi),
    Q(a,b)^2=2 B(a+1/2,b+1/2) (2^(2A+2)-1)/(2A+2),
    J_sigma^2=2(s+1)+4+2/((1-theta)(3-2theta)),
    S_sigma^2=s+1+1/(1-theta)+4/theta,
    H_l=max_{0<=d<=min(K,l)} (l!/(l-d)!) 2^(l-d),
    F_j,b=2^(sigma/2) max(2^b/(j! sqrt(2b+1)),
                            2^(-b-1) sqrt(Gamma(2b+1))/j!).

The beta and gamma integrals are their usual positive integral definitions. Their convergence follows from a,b>0. For radial source annuli A_R={R<=|W|<2R}, Cauchy-Schwarz in polar coordinates gives

    ||h 1_A_R||_L1 <= Q(a,b) R^(A+1) ||h 1_A_R||_L2(w).          (5)

Indeed the angular integral of |cos|^(2a)|sin|^(2b) equals2B(a+1/2,b+1/2), and the radial integral is the other factor in Q^2.

For a function smooth on the two intervals of I, with every derivative through K bounded by M there, (2) gives

    ||f||_Hsigma(I) <= J_sigma M.                               (6)

The L2 terms have total bound2(s+1)M^2. Within each component interval, the mean-value theorem bounds the fractional numerator by M^2|x-y|^2. Summing the two unit intervals gives2M^2/((1-theta)(3-2theta)). For the two cross-component rectangles, use numerator<=4M^2 and |x-y|>=2; their contribution is at most4M^2. This proves (6) without extending across the gap in I.

For a function on the whole real line, with unitary Fourier convention, Plancherel and translation give

    ||f|_I||_Hsigma(I) <= S_sigma ||f||_Hsigma(R),                (7)

where the right side is the Fourier norm with multiplier(1+xi^2)^(sigma/2). To check the fractional term, extend its integration to R2 and then apply Plancherel to translations. The resulting constant is integral_R |exp(iv)-1|^2 |v|^(-1-2theta)dv. Bounding the numerator by v^2 on |v|<=1 and by4 otherwise gives1/(1-theta)+4/theta. Each of the s+1 ordinary derivative terms is bounded by the same Fourier Hsigma norm. Density extends this inequality to that space.

For1/4<=r<=4, Fourier change of variables gives

    ||f(r .)||_Hsigma(R) <= r^(-1/2)max(1,r^sigma)||f||_Hsigma(R)
                         <= 2*4^sigma ||f||_Hsigma(R).          (8)

## 3. Partial Fourier trace with bounded normal support

Suppose h vanishes in a strip around y=0 and is supported in |y|<=2. For xi!=0 let alpha=|xi|. The one-dimensional Green function for alpha^2-partial_y^2 is exp(-alpha|y|)/(2alpha), as checked by its derivative jump. Differentiation gives the two x-Fourier trace kernels of absolute value

    alpha^(j+1) exp(-alpha|y'|)/(2j!).                            (9)

The odd velocity component has an extra unit imaginary factor and a sign of y'; these do not affect the bound. Weighted Cauchy-Schwarz in y' gives at high frequency

    |u_hat_i,j(xi)| <= [2^(-b-1)sqrt(Gamma(2b+1))/j!]
                 alpha^(-sigma) ||h_hat(xi,.)||_L2(|y|^-2b),

because integral_R exp(-2alpha|y|)|y|^(2b)dy=2Gamma(2b+1)/(2alpha)^(2b+1). For alpha<=1, use the support restriction in the integral instead and alpha^(j+1)<=1 to obtain coefficient2^b/(j!sqrt(2b+1)). Since(1+alpha^2)^(sigma/2)<=2^(sigma/2)max(1,alpha^sigma), integration in xi proves

    ||u_i,j||_Hsigma(R) <= F_j,b ||h||_L2(|y|^-2b).              (10)

This is an inhomogeneous bound with its low-frequency part explicitly controlled; no arbitrary representative of a homogeneous trace is used. For h supported in1<=|W|<2, |x|<=2 and a>0 further give

    ||h||_L2(|y|^-2b) <= 2^a ||h||_L2(w).                       (11)

For y traces, interchange coordinates, including the comparable-radius factor2^b F_l,a. The six normal orders l=0,1,2,3,4,5 have sigma=a-l-1/2 in the respective intervals(5,6),(4,5),(3,4),(2,3),(1,2),(0,1). The second IPM component becomes, after partial Fourier in y, minus the identity plus the positive exponential kernel alpha exp(-alpha|x|)/2; the identity and all its normal derivatives vanish on the trace for our data. The mixed component again has the odd exponential kernel. Thus (9)-(11) with the exchanged weights remain valid, without assuming rotational invariance of the IPM symbol.

## 4. Radial source blocks: small target radius

Let the source lie in A_R and the target have x=r z, z in I. If r/R<=1/8, then |r z|<=R/4 and the kernel stays at distance at least3R/4 throughout its x Taylor segment. The off-zero vector kernel satisfies

    K2+i K1=(x+i y)^(-2)/(2pi),
    |partial_x^l partial_y^j K_i(W)| <= D_l,j |W|^(-2-l-j).       (12)

Formula (12) follows by direct complex differentiation; it includes both scalar components with the same constant. The local velocity term contributes nothing off the source or to these traces.

Parity makes (1) exactly the ordinary Taylor remainder of order P, with its forbidden-parity coefficients zero. Differentiating d times in the rescaled target variable z gives, for d<=P, the Taylor remainder of order P-d of the dth derivative. Its bound is

    r^P 2^(P-d)/(P-d)! * (D_P,j/j!) (3R/4)^(-2-j-P) ||h||_L1.

For d>P, the polynomial vanishes after differentiation; use instead

    r^d (D_d,j/j!) (3R/4)^(-2-j-d) ||h||_L1,

and(r/R)^d<=(r/R)^P. Combining (5),(6), and the target prefactor r^(1/2-beta)=r^-t proves

    r^-t ||u^natural_i,j(r .)||_Hsigma(I)
       <= C_near (r/R)^(P-t) ||h||_L2(w),                       (13)
    C_near=(Q J_sigma/j!) max_{0<=d<=K}
          [2^max(P-d,0)/max(P-d,0)!]
          D_max(P,d),j (4/3)^(2+j+max(P,d)).

Every scale and factorial is retained; P-t>0.

## 5. Radial source blocks: large target radius

If R/r<=1/8, the primary trace kernel on either component of I is at distance at least3r/4 from the source. Using (5),(6),(12) and differentiating through order K gives

    r^-t ||u_i,j(r .)||_Hsigma(I)
       <= (Q J_sigma/j!) max_{d<=K} D_d,j(4/3)^(2+j+d)
                         (R/r)^(A+1) ||h||_L2(w).              (14)

Separately, the corner coefficient has the genuine moment bound for this single radial annulus

    |c_l,j[h]| <= [Q D_l,j/(l!j!)] R^(t-l) ||h||_L2(w).          (15)

The polynomial c_l,j r^l z^l has Hsigma(I) norm at most J_sigma H_l |c_l,j|r^l. If Lset is nonempty let mu=t-max(Lset)>0; if it is empty put mu=A+1. Since A+1>=mu and t-l>=mu for l in Lset, (14)-(15) give

    r^-t ||u^natural_i,j(r .)||_Hsigma(I)
       <= C_far (R/r)^mu ||h||_L2(w),                            (16)
    C_far=Q J_sigma [max_{d<=K} D_d,j(4/3)^(2+j+d)/j!
                       +sum_{l in Lset} H_l D_l,j/(l!j!)].

The moment bound (15) is only on one annulus. It does not bound that moment on the full global pure weight. Its role in (16) is coupled to the opposite-end remainder (13).

## 6. Comparable radii

For1/4<=r/R<=4, first set R=1 by homogeneity. Use (7)-(11) on the primary trace and (15) with R=1 on each Taylor polynomial. Since r^-t<=4^|t|, r^l<=4^l, this gives

    r^-t ||u^natural_i,j(r .)||_Hsigma(I)
       <= C_mid ||h||_L2(w),                                    (17)
    C_mid=4^|t| [2*4^sigma S_sigma 2^a F_j,b
                  +Q J_sigma sum_{l in Lset}4^l H_l D_l,j/(l!j!)].

For completeness the rescaling is exact: H(W)=h(RW) has norm R^(A-1)||h||_L2(w); u_i,j[h](Rx)=R^-j u_i,j[H](x), and c_l,j[h]R^l=R^-j c_l,j[H]. Thus the prefactor r^-t cancels R^(A-1-j)=R^t, leaving precisely (17) at r/R. No additional aspect-ratio or support constant is hidden.

## 7. Global annular sum and all nine traces

Partition the source into radial annuli A_(2^p). Each block preserves parity. For initial h in D there are finitely many nonzero blocks, and each remains supported a positive distance from the axes. Smooth approximation inside those annuli justifies the trace estimates if needed; equivalently the off-axis kernels and the weighted Fourier bound define the block traces directly. The squared source norms sum to ||h||_L2(w)^2.

For d=k-p, equations (13),(16),(17) give the l1 sequence

    C_near 2^((P-t)d), d<=-3;
    C_mid, |d|<=2;
    C_far 2^(-mu d), d>=3.

Minkowski for the sum of shifted l2 sequences proves (4), with

    C=C_near 2^(-3(P-t))/(1-2^(-(P-t)))
                  +5 C_mid+C_far 2^(-3mu)/(1-2^-mu).             (18)

This proves both infinite tails; no finite-annulus sampling is used. Cutoffs away from the axes and infinity followed by smooth approximation prove density of D in the parity subspace of L2(w). The bounded trace combination therefore extends to its stated completion. Source and target regions cover the full plane and full axis except null sets.

The required subtracted powers in the whole working window8<A<10 are:

| trace | tangential powers in Lset | P |
|---|---|---|
| u_1,0 | 1,3,5,7 | 9 |
| u_1,2 | 1,3,5 | 7 |
| u_2,1 | 0,2,4,6 | 8 |
| v_1,1 | 0,2,4,6 | 8 |
| v_1,3 | 0,2,4 | 6 |
| v_1,5 | 0,2 | 4 |
| v_2,0 | 1,3,5,7 | 9 |
| v_2,2 | 1,3,5 | 7 |
| v_2,4 | 1,3 | 5 |

All the normal orders satisfy the positivity of sigma needed above. Across the nine traces the subtracted coefficients have odd total degree at most7. Coefficients beyond the rectangle have total degree3,5 or7. This does not make them separately continuous on the global pure weight.

## 8. Rectangular subtraction and resonance

For a compact source away from0, a first remaining nonzero tangential coefficient c_p,j gives u_remainder(x)=c_p,j x^p+O(x^(p+1)) near0. Its annular norm has terms proportional to 2^(2k(p-t)) as k tends to minus infinity. It diverges when p<=t. Nonzero such coefficients occur in D: use a radial bump away from0 times an angular cutoff away from the axes times the nonzero coefficient kernel, followed by the required parity. The kernel has that parity, so the resulting moment is a positive integral of its square up to a nonzero constant. This is a constructive existence argument, not a sampled coefficient.

For the original rectangular orders6,3, the first remaining powers and the resulting whole-window verdicts are:

| trace | p | p+j+1 (j is normal order) | verdict for8<A<10 |
|---|---|---|---|
| u_1,0 | 7 | 8 | unbounded |
| u_1,2 | 7 | 10 | bounded by(4), identical natural subtraction |
| u_2,1 | 6 | 8 | unbounded |
| v_1,1 | 4 | 6 | unbounded |
| v_1,3 | 4 | 8 | unbounded |
| v_1,5 | 4 | 10 | bounded by(4), identical natural subtraction |
| v_2,0 | 3 | 4 | unbounded |
| v_2,2 | 3 | 6 | unbounded |
| v_2,4 | 3 | 8 | unbounded |

At a resonance t=l of the allowed parity with a nonzero coefficient, retaining that power makes the inner annular sum diverge. Subtracting it makes the outer sum diverge: the actual compact-source trace decays like |x|^(-2-j), whereas the polynomial x^l has constant normalized size at every large annulus. Removing higher powers makes that divergence worse. Thus no global polynomial subtraction of this form resolves the resonant coefficient. For IPM parity the nonzero total corner degrees l+j are odd, so these resonances occur when A is an even integer. This last observation concerns the trace topology; it is no exclusion of a PDE solution.

## 9. Dependencies and verification plan

This is a standalone informal proof using the exact IPM multiplier and kernel, Fourier Plancherel, elementary Taylor and Cauchy-Schwarz estimates, and explicitly evaluated positive integrals. The partial Fourier derivation is independently reproduced rather than inferred from a homogeneous trace theorem. Topic37 supplies a separately audited comparison but is not needed for the proof. The lead's T2 sketch is the claim under review, not a premise.

Implementations will independently enumerate the subtraction lists and both dyadic tail exponents, check kernel/factorial and scaling identities, and enclose every constant used in any public numerical bound with Arb and a separate mpmath.iv arrangement. All data, code and review are to be pinned in evidence/. No numerical constant is certified by this pre-code document alone.

## 10. Positive-integral verification, before implementation

For the independent numerical method the beta factor is its Euler integral
B(p,q)=integral_0^1 t^(p-1)(1-t)^(q-1) dt, with p,q>1 here. The integrand increases up to (p-1)/(p+q-2) and decreases afterward, as its logarithmic derivative shows. On each rational mesh interval its minimum is the smaller endpoint value and its maximum is the larger endpoint value, also including the critical-point value if that point belongs to the interval. The interval width times these values gives rigorous lower and upper Riemann sums. The endpoint values at0 and1 are zero. No quadrature error estimate or floating mesh is needed.

For Gamma(z), z>1, use the positive integral t^(z-1)exp(-t) on[0,T], with rational T>z-1. This integrand increases to z-1 and then decreases. The same endpoint/critical-point rule gives a rigorous enclosure on every rational subinterval. For the remaining tail put t=T+v. Since log(1+v/T)<=v/T,

    0<=integral_T^infinity t^(z-1)exp(-t)dt
       <= T^(z-1)exp(-T)/(1-(z-1)/T).

Add this upper tail and zero lower tail. Outward interval elementary powers and exponentials, combined with exact rational comparisons, preserve every rounding direction. Arb special-function values form the first computation, while these positive Riemann sums form the second, independently arranged computation. Every finite dyadic sum is combined with its exact geometric remainder. These methods enclose constants in(18); they do not supply an application-specific coupling constant.
