# The L2 endpoint of continuation on a carrier quotient

Status: independently confirmed at A2469-A2473; extensions remain OPEN at A2474. The planar assertion is a known theorem, not a novelty claim. The local carrier application is conditional on a square-integrable ratio. No exclusion of the full common-flat system or global Euler profile is asserted.

## 1. Exact statements, conventions and dependencies

Let D be a bounded open disc in C containing zero. Write partial_zbar=(partial_1+i partial_2)/2. Suppose f:D->C is smooth, every derivative of f at zero, including its value, vanishes, and

    |partial_zbar f| <= B |f| almost everywhere on D, B in L2(D).

Then f vanishes identically on D. The coefficient B is measurable and nonnegative. No boundedness, continuity, small norm or regularity of B is assumed. The proof is scalar.

For the application, fix 0<c<1/2 and any real omega. Put Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J, X(x)=Ax and a=1-2c. Let U be open in R3, avoiding zero, and V:U->R3 be smooth. Put W=curl V and suppose

    div V=0, X.V=0, DV X=-LV.                                  (C)

Let sigma:D0->U be a smooth section of X, with D0 a planar disc containing zero and det(sigma_1,sigma_2,X(sigma)) nonzero. Suppose V is flat at x1=sigma(0) and

    |(W.X)(sigma(y))| <= B0(y)|V(sigma(y))| almost everywhere,
    B0 in L2(D0).

Then V vanishes on a neighbourhood of x1. Norms and Lebesgue measure on the section refer to its planar coordinates. Coordinate changes with bounded Jacobians on smaller discs preserve this local condition.

For the final consequence assume the complete common-flat setting (F). Thus G is an X-flowbox, diffeomorphic to D1 times an interval I, with Gamma the central orbit segment, G avoiding zero, and smooth V,S on G satisfying (C) and

    X.grad S=-bS, W.grad S=0, b=2(1-c),
    P=S+|V|^2/2, -Delta P=tr((DV)^2),
    S=0 on Gamma, S<0 on G minus Gamma.

Both V and S are flat at one point x0 in Gamma. Put H=-S and eta=a/b. On every section disc through any point of Gamma, each of

    |W.X|/|V|, |W|/|V|, eta |X| |n.grad log H|,
    n=(V cross X)/(|V||X|),

fails to belong to L2 on every disc about its centre. The first two ratios are assigned zero where V=0. The last is assigned zero on its exceptional set; Section 6 proves that set has measure zero.

Dependencies are the already confirmed quotient reduction C67, A2463-A2465, and the common-flat structure C66, A2404-A2408. The planar proof below supplies the endpoint that was outside C67. It uses the Cauchy kernel, its L2 derivative multiplier, elementary convolution estimates, Sobolev approximation and the distributional Cauchy-Riemann lemma. Section 2 proves the exponential-integrability input directly, so no unread version of the Trudinger theorem is required.

## 2. An elementary exponential-integrability estimate

Fix a bounded planar open set Omega lying in a ball, and choose R larger than its diameter. For u smooth with compact support in Omega, the fundamental solution (2 pi)^(-1) log|x| of the planar Laplacian, integrated once by parts, gives

    |u(x)| <= (1/(2 pi)) integral_Omega |grad u(y)|/|x-y| dy,
    x in Omega.

The formula follows first by deleting a small circle around x, integrating by parts, and taking its radius to zero. Its boundary term is u(x). There is no outer boundary term because u has compact support. The same norm inequality holds for a complex u by taking the norm of its vector representation, or by applying the real Sobolev inequality to |u| by approximation.

Set K_R(x)=1_{|x|<R}/(2 pi |x|). For every p>=2, choose q=2p/(p+2), so 1+1/p=1/2+1/q and 1<=q<2. Young's convolution inequality gives

    ||u||_{Lp(Omega)} <= ||K_R||_{Lq(R2)} ||grad u||2,
    ||K_R||q = (1/(2 pi)) (2 pi R^(2-q)/(2-q))^(1/q).

Here 2-q=4/(p+2), 1/q=1/2+1/p and R^((2-q)/q)=R^(2/p). Consequently there is a finite constant C_R, depending only on R, such that

    ||u||p <= C_R sqrt(p) ||grad u||2, p>=2.                    (1)

For example the boundedness of (p+2)^(1/p) on [2,infinity) and R^(2/p)<=max(1,R) give this directly from the displayed exact norm. The constant is independent of p and u. Approximation in W12, followed by Fatou's lemma for an almost-everywhere convergent subsequence, extends (1) to W12_0(Omega).

For any fixed beta>0 and any family of such u with ||grad u||2<=E, expand exp(beta|u|). For integers k>=2,

    integral_Omega |u|^k <= (C_R E sqrt(k))^k.

The k=0 term is |Omega| and the k=1 term is uniformly bounded by Cauchy-Schwarz and (1) at p=2. The remaining series is bounded by

    sum_{k>=2} (beta C_R E)^k k^(k/2)/k!.

Since k!>=(k/e)^k, its kth root is at most beta C_R E e/sqrt(k), which tends to zero. The series converges. Hence

    sup_{||grad u||2<=E} integral_Omega exp(beta|u|) < infinity  (2)

for every finite beta. For complex u the same conclusion follows from the modulus and |grad|u||<=|grad u| almost everywhere. This is the weak exponential integrability needed below. Neither the sharp constant nor an exponential-square statement is used.

## 3. The L2 Cauchy factor and its weak exponential chain rule

Define alpha=(partial_zbar f)/f where f is nonzero, and alpha=0 elsewhere. The assumed inequality gives |alpha|<=B and partial_zbar f=alpha f almost everywhere, including almost every point of the zero set. Extend alpha by zero outside D and set

    s(z)=(1/pi) integral_D alpha(zeta)/(z-zeta) dA(zeta).

This convolution is well defined as a locally integrable function and belongs to L2 locally: on any bounded observation set only a bounded part of the locally L1 kernel 1/z is needed, and Young's inequality applies to the L2 data.

The identity partial_zbar(1/(pi z))=delta_0 gives partial_zbar s=alpha in distributions. The other complex derivative is the Beurling transform. With Fourier variables (xi1,xi2), its multiplier away from zero is

    (xi1-i xi2)/(xi1+i xi2),

which has modulus one. Plancherel's theorem therefore gives an L2 derivative with norm ||alpha||2. This identity can first be established for smooth compactly supported alpha, by differentiating the Cauchy fundamental solution, and then passed to L2 limits; local L2 convergence of the Cauchy transforms follows from the preceding kernel estimate. It follows that s is in W12 locally.

Take D' compactly contained in D, and a smooth compactly supported cutoff chi in D equal to one on a neighbourhood of D'. Let s_j be standard mollifications, converging to s in W12 on a neighbourhood of supp chi and almost everywhere along a subsequence. The functions chi s_j have uniformly bounded W12 norm and fixed bounded support. Estimate (2), applied to their moduli, gives

    sup_j integral_{D'} exp(beta |s_j|) < infinity

for every finite beta. The same integrability holds for s by Fatou. For every finite r>=1, using a larger exponential power gives uniform integrability of |exp(-s_j)|^r. Almost-everywhere convergence and Vitali's theorem imply

    exp(-s_j) -> exp(-s) strongly in Lr(D').

Fix 1<q<2 and choose finite r with 1/q=1/r+1/2. Holder's inequality, strong L2 convergence of grad s_j, and strong Lr convergence of the exponentials give

    exp(-s_j) grad s_j -> exp(-s) grad s in Lq(D').

For example split the difference into exp(-s_j)(grad s_j-grad s) and (exp(-s_j)-exp(-s))grad s. The first factor in the first product is uniformly bounded in Lr. The two terms then tend to zero in Lq. Passing the smooth derivative identity to the limit proves

    exp(-s) in W1q(D'),
    grad exp(-s)=-exp(-s) grad s, 1<q<2.                         (3)

This justifies the unbounded exponential factor; a bounded Sobolev chain rule alone would not suffice at p=2.

## 4. Holomorphy and the contradiction with a flat zero

Since f is smooth, (3) and the product rule give F=exp(-s)f in W1q locally, with

    partial_zbar F=exp(-s)(partial_zbar f-alpha f)=0.

This is a distributional identity. The distributional Cauchy-Riemann lemma gives a holomorphic representative F on D. For completeness, applying partial_z to the equation makes F a distributional harmonic function; the harmonic Weyl lemma makes it smooth, after which the Cauchy-Riemann equation makes it holomorphic. The factors and identities hold almost everywhere, which suffices.

Here is a direct integral end to the proof. If F is nonzero, its Taylor series at zero has a first term z^m G(z), with m>=0, G holomorphic and G(0) nonzero. There are r0,d>0 for which |G|>=d on |z|<r0. Consequently

    integral_{|z|<r} |F|^2 >= pi d^2 r^(2m+2)/(m+1), 0<r<r0.

Flatness of f gives |f(z)|<=C_N |z|^N for every integer N on a sufficiently small fixed disc. Since exp(-s) belongs to L2 there, the opposite estimate is

    integral_{|z|<r} |F|^2
       <= C_N^2 r^(2N) integral_{|z|<r0} |exp(-s)|^2.

Choose N>m+1 and send r to zero. This contradicts the lower bound. Hence F=0 on D by the holomorphic identity theorem, and f=0 almost everywhere and therefore everywhere by continuity.

The submitted C68 proof uses circle means instead of this final integral comparison. That end is valid as well. Let w=Re s in W12(B_r0) and let M(rho) be its circle mean for almost every rho. Smooth approximation on annuli, followed by a diagonal subsequence, and radial Cauchy-Schwarz give

    |M(rho')-M(rho)| <= (2 pi)^(-1/2) ||grad w||_{L2(B_r0)}
                                      sqrt(log(rho'/rho))        (4)

for almost every pair 0<rho<rho'<r0. Indeed differentiate the smooth circle mean, use angular Cauchy-Schwarz, and integrate with weights rho^(1/2) and rho^(-1/2). For Sobolev functions, L1 convergence on each fixed annulus yields almost-everywhere convergence of means along a subsequence; a countable exhaustion supplies (4).

If F=z^mG is nonzero, f=exp(s)F and the estimate with N=m+1 force w(z)<=C+log|z| almost everywhere near zero. Thus M(rho)<=C-log(1/rho). Fixing an admissible rho' in (4) gives the lower bound M(rho)>=M(rho')-C' sqrt(log(rho'/rho)), a contradiction as rho tends to zero through admissible radii. This independently checks C68 Step 4.

## 5. Transfer from the planar assertion to the carrier

The exact quotient geometry, already proved in A2463, is recalled to specify the coefficient being controlled. On a relatively compact section let

    m=|X(sigma)|, beta_i=X(sigma).sigma_i/m^2,
    g_ij=sigma_i.sigma_j-m^2 beta_i beta_j,
    j=|det(sigma_1,sigma_2,X(sigma))|=m sqrt(det g).

Write V(sigma)=sigma_i v_i-(beta.v)X(sigma) and theta=sigma^*(V.dx)=u_i dy_i. Then g is positive definite, u=gv, and

    div(jv)=(3c-1)j beta.v,
    d theta=[epsilon j(W.X)/m^2+q2(v)] dy1 wedge dy2,
    epsilon=sign det(sigma_1,sigma_2,X(sigma)),

where q2(v)=a(V cross X).(sigma_1 cross sigma_2)/m^2 is a smooth linear expression in v. The first relation is equivalent to

    d(*_g theta)=[(3c-1)beta-d log m](v) dA_g.

Use smooth orientation-preserving isothermal coordinates z on a smaller section neighbourhood and then restrict to a disc in those coordinates. Write theta=alpha1 dz1+alpha2 dz2 and f=alpha1-i alpha2. Both changes of coordinates and all metric comparisons have bounded coefficients on this smaller region. The two displayed exterior-derivative equations give

    2 partial_zbar f=div(alpha)-i curl(alpha),
    |partial_zbar f| <= (C1+C2 B0(y(z))) |f|.

The coefficient is in L2 because the coordinate disc is bounded and the Jacobian of the map from y to z is bounded. Smooth flatness of V transfers to f. The planar assertion therefore makes theta, v and V zero on a smaller section. Along a local X-orbit,

    V(exp(tA)x)=exp(-tL)V(x).

The inverse function theorem for (y,t)->exp(tA)sigma(y) extends the zero section to an open neighbourhood of x1. Only finite local times are used. Completeness of V trajectories, pressure normalization, decay at infinity and any energy or boundary identity are absent from this argument.

## 6. Ratio non-integrability in the complete common-flat setting

The confirmed C66 conclusions under (F) are: the flat set of V is exactly Gamma, V and W have the same zeros, and every zero off Gamma lies locally on one isolated X-orbit segment. In particular V cannot vanish on a nonempty open subset of G. The pressure equation is essential to that previous conclusion: if V were zero on G, then S=P would be harmonic with an interior maximum zero and would contradict S<0 off Gamma.

Let sigma be any section through a point of Gamma. If B=|W.X|/|V|, set to zero at velocity zeros, belonged to L2 on some section disc, the required inequality would hold there also at almost every zero, since W=0 whenever V=0. The carrier continuation result would make V vanish on a nonempty open set. This contradicts C66. Thus B is not in L2 on any disc about the centre.

If |W|/|V| belonged to L2 on such a disc, shrink further so that the closure is contained in it and in the section domain. On this smaller disc |X(sigma)| is bounded and B<=|X(sigma)| |W|/|V|. This gives the same contradiction. This restriction is necessary: a smooth section need not have bounded coefficients up to its open-domain boundary.

Off Gamma, the identities X.grad H=-bH, W.grad H=0 and X cross W=aV give

    W=eta grad(log H) cross V.

Where V is nonzero, taking the X component yields

    |W.X|/|V|=eta |X| |n.grad log H|.

The inverse image of Gamma under a transverse section is locally discrete. By C66 the off-Gamma velocity zeros are also locally discrete when intersected with the section. Each of these two sets is countable in the second-countable section domain; the second may accumulate at the first. Their union has measure zero. Assigning zero to the last expression at these points therefore preserves its equality almost everywhere with B and its failure to belong to L2.

For orientation, the full section gradient grad_y log(H o sigma) also cannot belong to L2 on a punctured disc. If it did, apply the smooth version of (4) on annuli with its total finite gradient norm. Positivity off the centre and H(sigma(0))=0 imply H(sigma(y))<=C|y| near the centre, so its logarithmic circle means are at most C'-log(1/rho), contradicting (4). This observation alone does not control the particular directional component in the preceding ratio.

## 7. Source audit, attribution and exact scope

The submitted C68 source, all its steps and remarks, was read in full. The proof above confirms its assertions (a)-(c), including the circle-mean argument. Two routine qualifications inherited from C67 have been supplied explicitly: shrink before using coefficient bounds, and define the logarithmic-normal expression on its countable exceptional set. The useful exponential chain rule is stated for 1<q<2. The submission's notation "every q<2" need not include non-Sobolev exponents to prove anything here.

The actual published manuscript by Yifei Pan and Yuan Zhang, "Unique continuation for d-bar with square-integrable potentials", New York Journal of Mathematics 29 (2023), 402-416, was obtained from the journal. All fifteen printed pages, including the proof of Theorem 1.1, were read. Its Theorem 1.1 covers H1_loc vector-valued functions in one complex variable, a locally L2 potential and infinite-order vanishing defined by local L2 integrals. A smooth scalar flat function satisfies its hypotheses: Taylor's theorem gives |f(z)|<=C_N |z|^N for all N, hence the required integral vanishing. Thus C68(c) is also a special case of that published result. The proof in Sections 2-4 is independently scalar and does not claim the vector-valued theorem.

Example 3.3 in that manuscript checks sharpness on the Lebesgue scale: for any 0<p<2 choose 0<epsilon<(2-p)/p and take f(z)=exp(-|z|^(-epsilon)), extended by zero at zero. It is smooth and flat, and

    |partial_zbar f|/|f|=epsilon/(2 |z|^(epsilon+1)) in Lp(D1),

while f is not zero. The smooth flat extension follows since every derivative is bounded by a polynomial in 1/|z| times exp(-|z|^(-epsilon)); the radial integral is finite exactly when p(epsilon+1)<2. This example concerns the planar step only, and is not a carrier or full-(F) counterexample.

The manuscript's Theorem 4.3 separately addresses scalar potentials C/|z|, using Pan1992 Lemma7. This was read as a published statement, but that earlier lemma has not been read in this review and no new C/|z| application is certified here. In particular the failure of L2 alone is not asserted to be the only possible continuation criterion.

The elementary exponential estimate removes reliance on a GT book theorem whose exact edition and statement were not obtained. Failed public retrieval attempts are recorded honestly. There was no numerical experiment, formal build or timing surrogate. Existing configured model C and coordinator file comparisons provide the cross-model exchange; actual provider execution is not independently attested.

This audit closes only the L2 endpoint named in A2468. It neither derives an L2 upper bound from (F), excludes (F), bounds accumulating zero indices, proves infinite flatness of actual tails, upgrades tail regularity, nor settles the decay-only rotating conjecture. All those extensions remain OPEN.
