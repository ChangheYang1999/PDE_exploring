# High single harmonics at odd resonance periods

Status: PROVED. Independent theory-part review confirmed the argument on 2026-10-31T15:07:01+00:00; V414. This is a support theorem for the tuning response, not a universal incompatibility theorem.

## Exact statement

Let Q be an odd integer at least3, let h be a positive integer coprime to Q with2h<Q, and set delta=2h/Q and c=1/(1-delta). Fix an odd positive integer M and leading density f1(theta)=sin(M theta). Work with the S1 density and S2 stream symmetries and the pure exponent lattice p_n=1-n delta, P_n=2-n delta. Each stream resonance n=kQ has the free term H_(kQ) sin((2hk-2)theta), with k>=1 if h>=2 and k>=2 if h=1.

At a resonant index n=kQ, define sigma_k as the response of the next density compatibility coordinate, the coefficient of sin((2h(k+1)-3)theta) in f_((k+1)Q), to a unit change in H_(kQ). This affine response is determined by f1,...,fQ and g1,...,g_(Q-1), independently of previous tuned harmonics, whenever the branch exists to ordern. The same finite linear response recurrence defines sigma_k even if a previous incompatibility prevents continuation of that branch.

Put

    S_(M,Q) = {Ms+t : s=-Q,-Q+2,...,Q,
                       t=-(Q-1),-(Q-3),...,Q-1}.

Then sigma_k can be nonzero only if at least one of

    2h-1,   4hk+2h-5

belongs to S_(M,Q). In particular, if M>Q+2h-2, then

    sigma_k = 0 whenever 4hk+2h-5 > QM+Q-1.

Equivalently, it vanishes at every integer k>(QM+Q-2h+4)/(4h) in its resonant index range. Thus the uniform nonzero-response hypothesis of the tuned convergence theorem fails for this single-harmonic profile.

If h>=2 and M>Q+2h-4, the first compatibility condition, at orderQ, vanishes automatically. This initial compatibility does not imply the nonzero-response hypothesis or compatibility at all later orders.

## Low-order support

For1<=r<=Q, every signed Fourier frequency of f_r belongs to

    A_r = {Ms+t : |s|<=r, s congruent to r modulo2,
                  |t|<=r-1, t congruent to r-1 modulo2}.

For1<=r<Q, the corresponding g_r support satisfies the same bounds with |t|<=r and t congruent to r modulo2.

The assertion holds at r=1. The density-to-stream Poisson right side shifts every signed frequency by at most1. Its inverse divides each nonresonant Fourier coordinate and hence adds no frequencies. The bilinear density recursion adds a frequency from g_i to one from f_j, where i+j=r; its angular derivatives preserve frequencies. Adding their bounds gives |s|<=r and |t|<=r-1 with the asserted parities. There is no stream resonance belowQ. This proves the induction, including fQ before its stream inverse is taken.

Since Q is odd, s is odd at r=Q, and therefore nonzero. It follows that every signed frequency of fQ has absolute value at least M-(Q-1). For h>=2 the first obstructed density frequency is2h-3. If M>Q+2h-4, the lower support bound exceeds2h-3, proving first compatibility exactly.

## Affine response and its support

Write n=kQ, q=2hk-2, and perturb g_n by H sin(q theta). The first affected density coefficient is f_(n+1). A nonlinear pair containing two affected factors would require a stream index at leastn and a density index at leastn+1, hence total order at least2n+1. Since n>=Q, this is greater than n+Q. Consequently every coefficient through n+Q is affine in H.

Let phi_r be its density coefficient at n+r per unit H. Let v_r be the intermediate stream response at n+r for1<=r<Q. With

    T_(i,j)(g,f) = P_i g f' - p_j g' f,
    lambda_l = (l-1)(c-1), e(theta)=sin(q theta),

collecting the affected pairs gives

    lambda_(n+r) phi_r = T_(n,r)(e,f_r)
        + sum_(a=1)^(r-1) [T_(n+a,r-a)(v_a,f_(r-a))
                            + T_(r-a,n+a)(g_(r-a),phi_a)].

The intermediate Poisson inverses are nonresonant, since their indices lie strictly between consecutive multiples ofQ. This recurrence uses only the listed low-order fields and proves independence from all earlier free harmonics.

Induction in this response recurrence gives the density support

    {epsilon q + Ms+t : epsilon in {-1,1},
       |s|<=r, s congruent to r modulo2,
       |t|<=r-1, t congruent to r-1 modulo2}.

The stream response replaces the bound on t by |t|<=r with parityr. The direct term has this support because e shifts the support of f_r by plus or minusq. Each remaining product adds the appropriate low-order support to an earlier response support. Poisson inversion changes only the same one-frequency shift already accounted for in the stream bound.

At r=Q the positive target density frequency is q+2h-1. An epsilon=1 contribution requires Ms+t=2h-1. An epsilon=-1 contribution requires Ms+t=2q+2h-1=4hk+2h-5. The signed Fourier sets are symmetric, so considering the positive target is sufficient. This proves the finite-set criterion.

If M>Q+2h-2, the lower support bound M-(Q-1) exceeds2h-1, excluding the first possibility. The upper bound on every element of S_(M,Q) is QM+Q-1, so the second possibility is also excluded at the stated large k. This proves eventual exact vanishing.

## Examples and limits

For Q=9,h=2,M=13, S_(13,9) contains neither3 nor23, so sigma3=0. The general large-index bound gives sigma_k=0 for all k>=16. Topic197 computes a nonzero constant obstruction at order36 after the two uniquely determined earlier tunings, and therefore supplies an actual incompatibility example.

For Q=9,h=2,M=15, the criterion first forces sigma4=0 because neither3 nor31 belongs to S_(15,9). A separate finite calculation must determine whether the constant obstruction at order45 also vanishes. Support alone does not settle it.

The proof uses Q odd to exclude s=0. For evenQ, balanced leading frequencies allow s=0, so the asserted lower support bound does not follow. No corresponding even-period vanishing theorem is claimed. No assertion is made about logarithmic expansions, added exponent channels, or compatible branches whose zero response is accompanied by a zero constant obstruction.

## Dependencies

The density/stream recurrence and Poisson inverse are independently derived in topic01. The finite response recurrence is the same affine identity used in topics131 and194. The proof above supplies the full support argument, rather than importing a numerical bandwidth observation. The only quantitative external example is the separately retained exact computation in197.

## Independent review, 2026-10-31T15:07:01+00:00

The theory part checked the low-order support induction, affine response recurrence, carrier alternatives, threshold arithmetic, narrow-band inequalities and even-period limitation. The retained review reports no gap. This promotes the support theorem only; an absent response does not itself prove that the corresponding compatibility constant is nonzero.
