# Near-diagonal localization and a mixed-norm obstruction

Status: CONFIRMED after the theory part's independent 05:54Z review and verifier recheck at 2026-10-31T05:56:21Z. The result localizes the dangerous linear inverse and disproves a natural unrestricted mixed-norm estimate. It does not settle the generated rational IPM series.

## 1. Exact setting and a linear estimate

Fix an integer Q>=3, delta=2/Q and c=Q/(Q-2). Put p_n=1-n delta and P_n=2-n delta. All density modes are odd positive sine frequencies; all stream modes are even positive sine frequencies. Use polynomial coefficients in t=log r and the canonical zero constant at each resonant stream frequency.

For an input a(t)sin(m theta), the upward stream channel at frequency m+1 is

    B_+=-(1/2)(D_t+s)^(-1)a,  s=m+3-n delta,               (1)

when s!=0. This is the exact canceled Poisson factor derived in topic71. For a monomial a_q t^q,

    (D_t+s)^(-1)(a_q t^q)
      =(a_q/s) sum_(h=0)^q (-1/s)^h q!/(q-h)! t^(q-h).    (2)

For q>=1 and |s|>=q/C, where C>0,

    ||(D_t+s)^(-1)(a_q t^q)||_plain
       <= |a_q| (q+1) max(1,C)^q / |s|.                   (3)

This follows from q!/(q-h)!<=q^h. At rational delta=2/Q, every nonzero s has |s|>=1/Q, so the right side is at most Q(q+1)max(1,C)^q|a_q|. For q=0 use |a_0|/|s| directly. Thus the potentially supergeometric loss of this channel is confined to |s|<q/C. By topic71, switching to reciprocal-binomial norms introduces at most an additional factor2^K for polynomials of degree<=K. This is still a geometric bound in the order. At exact s=0, the upward inverse is -(1/2)integral_0^t a, which has no such factorial cascade.

The downward channel, when m>=3, is

    B_-=(1/2)(m-1-P_n-D_t)^(-1)a.                          (4)

Its scalar divisor has magnitude n delta+m-3. For q>=1 within the canonical density degree bound q<=floor((n-1)/Q)-1, this is at least2q+2/Q. Hence this channel is separated from the dangerous diagonal. At a resonant output one may have to subtract its constant to impose the canonical gauge; that costs at most a factor2 in the plain norm. These statements are about the linear map, not a closed nonlinear estimate.

## 2. The exact frequency bookkeeping

For a stream input of order i and frequency l and density input of order j and frequency m, define

    s_G=l+2-i delta,  s_F=m+3-j delta.

At n=i+j the sum-frequency output l+m has

    s_out=s_G+s_F-2.                                      (5)

If m>=l, the difference output m-l has

    s_out=s_F-s_G+2-2i delta;                             (6)

if l>=m, the difference output l-m has

    s_out=s_G-s_F+4-2j delta.                             (7)

Thus two inputs satisfying |s_G|<=eta q_G and |s_F|<=eta q_F have a sum output satisfying |s_out|<=eta(q_G+q_F)+2. A t derivative can lower the output degree by one, requiring one more eta of width. An exact band of width eta q is not automatically invariant. Difference outputs are usually far away when the smaller radial order is comparable to the larger one and the band is narrow, but there is no unconditional difference-frequency exclusion when orders are very unequal. Equations(6)-(7), rather than a heuristic rule, determine the cases.

More seriously, two off-diagonal inputs with opposite signed distances can have a near-diagonal sum output. The next section makes this into an exact Poisson-consistent counterexample.

## 3. Definition of the mixed norm

Fix eta>0. For a density at order n=Qk+r, 1<=r<=Q and k>=1, with degree at most k-1, assign the physical coefficient of t^q sin(m theta) weight

    w_(n,m,q)=q!                  if |m+3-n delta|<=eta q,
               1/binom(k-1,q)    otherwise.                (8)

At q=0 either weight is1, so a different fixed-width classification there has no effect. Sum the weighted absolute coefficients to define M_n. A stream norm may be defined with |m+2-n delta| in the same way. This is the proposed factorial-near, reciprocal-binomial-away norm. Replacing the away weight by1 only strengthens the forthcoming input estimate, since the input monomials have top degree and binomial weight1.

There do not exist constants C_0,C_1>0 such that, for every allowed density input F at a single order i,

    M_(2i)((lambda_(2i)-cD_t)^(-1) J(Poisson_i F,F))
       <=C_0 C_1^i M_i(F)^2,                              (9)

where lambda_n=(n-1)(c-1) and J is the polar IPM coefficient Jacobian. The statement remains false after fixed angular/radial radius losses or any polynomial order damping. It concerns generic allowed inputs, not a full recursion starting from f_1.

## 4. A Poisson-consistent witness

First suppose0<eta<2. For an integer k large enough depending on Q and eta, put

    i=Qk+1,  q=k-1,  h=4k-3,
    F(t,theta)=t^q[sin(theta)+sin(h theta)],
    P=P_i=2-2k-2/Q,  p=P-1.                               (10)

Both density modes are off the band: their signed distances are4-2k-2/Q and2k-2/Q, whose absolute values exceed eta(k-1) for sufficiently large k because eta<2. They respect S1 symmetry, the generic bandwidth2i-1 and the density degree bound. Therefore M_i(F)=2.

Let G be the exact polynomial Poisson inverse of F. The order i is nonresonant. Its top-degree stream coefficients at frequencies2 and h+1 are

    b_L=-1/[2(P+2)],  b_H=-1/[2(P+h+1)].                   (11)

There is also a channel at h-1. The top-degree Jacobian coefficient at output frequency h+2=4k-1 is contributed only by the two cross products in(11). Since every D_t term lowers the degree, at degree2q it is exactly

    T= [b_H(P-p(h+1))+b_L(Ph-2p)]/2
      =-[ -2P^2+(h-1)^2 P+4(h+1)]
          /[4(P+h+1)(P+2)].                              (12)

For k>=4, P<-2, P+h+1=2k-2/Q>0, and

    2P^2>4(h+1).

The last inequality follows from |P|>2(k-1) and (k-1)^2>=2k-1 for k>=4. Consequently the numerator in brackets is negative and its magnitude is larger than(h-1)^2|P|. It follows that

    |T| >= (h-1)^2/[4(h+1)].                              (13)

Indeed |P+h+1|<=h+1 and |P+2|<|P|. In particular no cancellation removes this coefficient.

At output order n=2i=2Qk+2, the target frequency has signed distance

    (4k-1)+3-n delta=2-4/Q,                               (14)

which is bounded independently of k. The output degree is2q=2k-2. It lies in the near band for all sufficiently large k, and is below the allowed maximum2k-1. Inverting lambda_n-cD_t leaves the top coefficient T/lambda_n. Therefore the norm of the left side in(9) is at least

    (2k-2)! |T|/lambda_n
      >=(2k-2)! (4k-4)^2/[4(4k-2)lambda_(2Qk+2)].        (15)

The prefactor after the factorial has a positive limit depending only on Q. The right side of(9) is4C_0 C_1^(Qk+1), so(15) contradicts it. Elementary factorial growth suffices: the last k-1 factors of(2k-2)! are at least(k-1)^(k-1). Fixed strip/radius losses contribute at most an exponential in k, and fixed polynomial damping does not remove this contradiction.

The same witness works if the away region carries the plain coefficient weight. It also shows why the linear localization(3) cannot by itself close the proposed mixed norm: this nonlinear forcing enters the dangerous band from two off-diagonal frequencies.

## 4.1 Any positive band-width factor

The restriction eta<2 is unnecessary. For any fixed eta>0, keep i,h,P from(10), but choose

    q=floor((k-1)/(1+eta)).                                (16)

Then0<=q<=k-1 and eta q<k-1. For k>=4, both input distances have absolute value larger than k-1, so both are outside the band. The input norm is now2/binom(k-1,q)<=2. The exact top-degree coefficient T in(12) is unchanged, since it depends on the radial exponents and angular frequencies, not on the log degree. The target degree is2q and its distance remains2-4/Q, so the output enters the near band once k is large. Its norm is at least (2q)!|T|/lambda_(2i).

As k tends to infinity, q/k tends to1/(1+eta)>0. Hence(2q)! still exceeds every exponential in k, and(9) fails for every eta>0. This also handles arbitrarily wide fixed bands. The construction uses only lower log degrees when the band is wide, and respects the same generic degree and bandwidth bounds.

## 5. Scope and verification

The witness is Poisson-consistent at its input order. It does not supply the preceding coefficients required by the nonlinear IPM recurrence, so it is not a divergence example for the actual generated sequence. Recurrence-specific correlations or a different nonlocal weight could still control that sequence. The confirmed fixed-deficit theorems remain compatible with this obstruction.

Independent exact Cartesian differentiation checks the full Poisson identity, the coefficient T, and the stationary inverse at finite Q,k. Separate integer/rational checks verify the two channel formulas, off-band membership, output-band membership and factorial lower bound. The all-order proof is equations(10)-(15), not the finite test.

The arbitrary-width extension was checked separately at18 exact witnesses, eta=1/4,1,3/2,3,10,100 and three growing log degrees each. Input/output band membership and the exact Cartesian coefficient all pass. The certificate is verification/general_width_checks.json; actual runtime3.2344310991466045 seconds.
