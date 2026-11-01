# A spectral support test for eventual vanishing of tuning responses

Status: PROVED. Independent theory-part review confirmed the argument on 2026-10-31T15:07:01+00:00; V414. This is a limitation of the nonzero-response tuning hypothesis, not a universal incompatibility theorem.

## Exact statement

Let Q>=3 and h>=1 be coprime integers with2h<Q. Set delta=2h/Q and c=1/(1-delta). Let f1 be a nonzero real finite odd-sine polynomial. Let Lambda be its signed Fourier support, a finite nonempty symmetric set of odd integers. For a positive integer r, write rLambda for the set of sums of exactly r elements of Lambda, allowing repetition. Define

    E_r = {-r,-r+2,...,r},   E_0={0},
    K = QLambda + E_(Q-1),   L=max{|m|:m in Lambda}.

At a resonant stream index n=kQ, let sigma_k be the affine response of the next compatibility coordinate to a unit change in the free stream amplitude. Its carrier frequency is q=2hk-2, and the next density compatibility frequency is q+2h-1. The index range is k>=1 if h>=2 and k>=2 if h=1.

Then sigma_k can be nonzero only if at least one of

    2h-1,   4hk+2h-5

belongs to K. Consequently, if2h-1 is absent from K, then

    sigma_k=0 for every integer k>(QL+Q-2h+4)/(4h)

in the resonant index range. In particular its absolute values have zero infimum, so the uniform nonzero-response hypothesis fails. This conclusion concerns the formally defined response even if an earlier compatibility obstruction prevents an actual branch from reaching the indicated index.

If Q is odd and every positive supported frequency lies in an interval[M-W,M+W], with M positive odd, W nonnegative even and M>W, a sufficient condition for this eventual vanishing is

    M > Q(W+1)+2h-2.

When h>=2, the weaker inequality M>Q(W+1)+2h-4 already makes the first compatibility condition at orderQ vanish automatically.

For even Q and nonempty Lambda, the support test2h-1 absent from K can never hold. This does not prove nonvanishing responses at even Q; it only states a limitation of this support test.

## Proof of the frequency sets

For1<=r<=Q, the nonresonant recursion gives

    supp(f_r) contained in rLambda+E_(r-1),
    supp(g_r) contained in rLambda+E_r  for r<Q.

The first density inclusion holds by definition. The density-to-stream right side is a sum of multiplication by cos(theta) or sin(theta) and angular differentiation, hence shifts each frequency by plus or minus1. The nonresonant inverse changes coefficients but not their frequencies. Thus the stream inclusion follows from the density inclusion.

In the density recurrence, a product with indices i+j=r has one stream factor and one density factor. Angular differentiation preserves frequency. Their supports add to

    iLambda+E_i+jLambda+E_(j-1) = rLambda+E_(r-1).

Here E_a+E_b=E_(a+b), since all intermediate integers of the prescribed parity occur. Summing products can only remove frequencies by cancellation. This proves the induction. The density coefficient f_Q is computed before taking its potentially resonant stream inverse, so no compatibility assumption is needed for these inclusions.

## Proof for the affine response

Perturb g_n by H sin(q theta), n=kQ. The first affected density is f_(n+1). A product containing two affected factors has total order at least n+(n+1)>n+Q. Therefore all density coefficients through n+Q are affine in H. Their coefficients phi_r at order n+r satisfy

    lambda_(n+r) phi_r = T_(n,r)(e,f_r)
      + sum_(a=1)^(r-1) [T_(n+a,r-a)(v_a,f_(r-a))
                          +T_(r-a,n+a)(g_(r-a),phi_a)],

where lambda_l=(l-1)(c-1), e=sin(q theta), T_(i,j)(g,f)=(2-i delta)g f'-(1-j delta)g' f, and v_a is the nonresonant stream inverse of phi_a. Every intermediate index n+a,1<=a<Q, is nonresonant. This equation follows by collecting precisely the products with one affected factor. It also shows that the response depends only on the low-order fields used above.

Inducting in this equation gives

    supp(phi_r) contained in {-q,q}+rLambda+E_(r-1),
    supp(v_r) contained in {-q,q}+rLambda+E_r  for r<Q.

The direct term has exactly the required containment; the two sums use the already proved low-order containments. At r=Q, reaching the positive target q+2h-1 from the positive carrier requires2h-1 in K. Reaching it from the negative carrier requires2q+2h-1=4hk+2h-5 in K. Symmetry of the support sets handles the negative target too. This proves the two alternatives.

Every element of K has absolute value at most QL+Q-1. Once the fixed first alternative is absent and the positive second offset exceeds this bound, neither alternative can occur. Solving that strict inequality gives the claimed threshold in k.

## Narrow bands and the parity limitation

Suppose Q is odd and the positive frequencies are in[M-W,M+W]. A sum of Q signed supported frequencies can be written M s+e, where s is an odd integer and |e|<=QW. Hence |M s+e|>=M-QW. Adding E_(Q-1) shows that every element of K has absolute value at least M-QW-Q+1. Under M>Q(W+1)+2h-2, this lower bound exceeds2h-1. The fixed response alternative is therefore absent. For h>=2, applying the weaker inequality to the first compatibility frequency2h-3 proves its automatic vanishing.

If Q is even, symmetry and nonemptiness of Lambda allow Q/2 cancelling pairs, so0 belongs to QLambda. Since2h<Q, the positive odd integer2h-1 is at most Q-3, and lies in E_(Q-1), whose entries are odd. Thus2h-1 belongs to K. The sufficient support-gap condition is impossible in this case. Cancellations of actual coefficients may still produce response zeros; this argument does not address them.

## Examples and limits

For delta=4/9, every nonzero leading profile supported on sin(31theta), sin(33theta), sin(35theta) has M=33,W=2,Q=9,h=2. Since33>29, its tuning responses eventually vanish. Its first compatibility is automatic since33>27. With L<=35, the uniform safe threshold is k>=41. This provides a finite-dimensional family on which the nonzero-response hypothesis cannot hold. It does not assert a later incompatible constant obstruction for every profile in that family.

For a single harmonic, W=0 and Lambda={-M,M}; the statement reduces to topic198. Topic197 supplies actual later incompatibilities for sin13 and sin15 by separate exact computation. The present support theorem makes no assertion about logarithmic expansions, additional radial exponents, or the convergence of a compatible branch with zero responses.

## Dependencies and verification

The proof uses only the independently derived Poisson and nonlinear recurrences, their S1/S2 Fourier symmetries, and the displayed finite affine index argument. It needs no numerical growth assumption, asymptotic fit, or formal-to-convergent inference. Adjacent verification files should record independent review and any exact finite support checks.

## Independent review, 2026-10-31T15:07:01+00:00

The theory part checked the low-order support induction, affine response recurrence, carrier alternatives, threshold arithmetic, narrow-band inequalities and even-period limitation. The retained review reports no gap. This promotes the support theorem only; an absent response does not itself prove that the corresponding compatibility constant is nonzero.
