# Exact exponent audit for the numerical lane's tail majorants

Date: 2026-10-20. Status: conditional derivation; exact enumeration and source closure pending. This result concerns termwise monotonicity of the snapshotted tail majorants, not their computed coefficients or a full residual norm.

## Statement and hypotheses

Use the exact modal density, finite angular projection and canonical normalization in ../modal_repair/PROOF.md. Let k, b_i, b_o be the exact dyadic scalars in the pinned modal JSON. Its inner scalar exponents are

A_i={0,2,4,6,8,10,12,14,b_i},

with polynomial degree0 except for b_i, whose degree is at most6. The exponent0 density is exactly x^2 y, so the exponent0 forcing coefficient is nonzero only at stream mode n=1. Its outer scalar exponents are

alpha_(j,l)=k-3-j(1-k)-2l,
(j,l) in {(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)},

all of degree0, together with exponent -b_o of degree at most6. Every coefficient discussed below is a fixed exact real number or a proved enclosing interval. Let stream modes range over n=1,...,261, with m=2n. No angular or radial term is truncated.

The exact exponent enumeration is intended to prove these parameter-dependent claims:

1. For every positive monomial in the inner residual majorant after removing the exact cubic strain products, division by r^5 gives a nondecreasing function of tau on tau<=-T whenever T>=2. Consequently the same is true after division by m(r)=(r/L)^3[1+(r/L)^2]^((k-3)/2), since r^5/m(r) is increasing for0<k<1. This includes the near-zero upper-Green branch.
2. For every positive monomial in the outer majorant, multiplication by (1+r/L)^delta/m(r) gives a nonincreasing function on tau>=T whenever T>=9 and delta is either1/2 or1/2-k. The exact code's coarse rate test dominates all such monomial rates, including degree12 products, for these parameters.

Here the positive coefficients must arise from the stated algebra before taking absolute values. A generic subtraction from an upper bound is not justified by this theorem. Correct arithmetic import, canonical boundary moments, all zero-denominator treatments and full source/output validation remain separate requirements.

## Scalar monotonicity

For x=-tau>=T>0, an inner monomial divided by r^5 is a constant times x^d exp(-(gamma-5)x). Its logarithmic derivative in tau is gamma-5-d/x, which is nonnegative on the whole tail if

(gamma-5)T>=d.

This condition may have equality for d=0. The analogous condition for division by the leading cubic power is (gamma-3)T>=d. The exact weight contains the additional positive factor [1+(r/L)^2]^((3-k)/2), which is increasing in tau and preserves the conclusion. The stronger r^5 criterion therefore suffices for both norms.

It is false that x^d exp(-beta x) is decreasing for all x>=0 whenever beta>=2. For d=1 it increases up to x=1/beta. Thus the corresponding unrestricted sentence in cert_inner_tail.py is false; the actual cutoff must be checked.

For the outer region put u=exp(t_0+tau)/L. When delta>=0 and0<k<1,

d_tau log[(1+u)^delta/m]=delta*u/(1+u)-(3+k u^2)/(1+u^2)<=delta-k.

A monomial tau^d exp(gamma tau) times this weight is therefore nonincreasing for tau>=T if gamma+d/T+delta-k<=0.

## Forcing and stream exponents

Writing rho=exp(3t)sum Rhat_j(t)sin((2j+1)theta), direct differentiation gives

f_n=exp(2t)[(Rhat'_(n-1)+Rhat'_n)/2+(2-n)Rhat_(n-1)+(2+n)Rhat_n].

Thus a scalar density exponent alpha produces a forcing exponent alpha+2, with one factor exp(2t_anchor). The Green integration multiplies by another exp(2t_anchor) and adds2 to the exponent. A particular stream term therefore has exponent alpha+4, with the same maximal polynomial degree. The two exp(2t_anchor) factors are correct: the stream scales as r^4 when the normalized density Rhat is constant.

For inner particular terms the lower primitive rate is lambda=m+4+alpha>0. The upper primitive rate is mu=4-m+alpha. When mu is separated from zero the stream terms again have exponent alpha+4 and degree no greater than the original degree. The upper boundary transient has exponent m and degree0.

For the exact or near-zero branch write x=-tau. The elementary inequality |exp(mu s)-1|<=|mu||s|exp(|mu||s|) gives

|integral_(-x)^0 exp(mu s)sum_j c_j s^j ds|
 <=sum_j |c_j|x^(j+1)/(j+1)
  +|mu|exp(|mu|x)sum_j |c_j|x^(j+2)/(j+1).

This inequality holds for all x>=0, even if the branch is chosen because |mu|T<1/2 at the cutoff. After multiplication by exp(-mx), the first family has stream exponent m and degrees1,...,d+1. The second has exponent m-|mu| and degrees2,...,d+2; it vanishes exactly when mu=0. This is the correction that must be included in a rigorous exponent audit.

For the exact inputs and2<=T<=3, the near-zero possibilities are alpha in{2,4,...,14} with n=(alpha+4)/2, and alpha=b_i with n=27. The putative alpha=0,n=2 case has zero forcing and is absent. All remaining nonzero forcing terms are separated from this branch. For larger T the n=27 branch may eventually change; its nonresonant representation still has the already listed particular and transient exponents. Our audit checks both representations, so monotonicity does not depend on where that switch occurs.

## Inner residual exponents and the cubic removal

A density term has exponent3+alpha_R. Both polar velocity factors in the residual reduce the stream exponent by2. Hence every stream-density product has residual exponent

gamma=stream_exponent+1+alpha_R,

and degree the sum of its two polynomial degrees. Linear residual terms other than the cubic have exponent3+alpha_R and the density degree. In particular the possible degree12 and degree14 products are included by pairing every admissible stream monomial with every density monomial.

For n=1 the upper transient is exactly2c exp(2t), where c is the canonical strain of the same density. Indeed its coefficient is the full integral integral_0^infinity f_1(s)/s ds=2c. Its contribution to each of the nonnegative scalar velocity majorants Pabs and Qabs is |c|/2. The cubic density has radial-derivative Wiener norm3r^3/2 and angular-derivative Wiener norm r^3. Accordingly the product majorant contains the explicit nonnegative component

2[(|c|/2)(3r^3/2)+(|c|/2)r^3]=(5/2)|c|r^3.

Subtracting this identified component from that same expanded majorant leaves a nonnegative sum of all remaining products. The actual cubic residual is (3c_l-1-c)rho_0, and is zero under exact normalization. This justifies the particular cubic subtraction only after proving that the canonical c and transient refer to the same exact trial. Interval evaluation of the subtraction can lose correlation but still encloses the resulting exact real expression. Neither overlap of two c intervals nor a small numerical normalization defect proves the exact identity needed for W/r^5.

The remaining transient products have exponent m+1+alpha_R; the sole case m=2,alpha_R=0 is the removed cubic. The exact finite audit checks gamma-5-d/2>=0 for every remaining monomial. Degree0, exponent5 terms are constant after division by r^5 and are allowed. This establishes the stated inner monotonicity condition without trusting the false general sentence in the source comment.

## Outer residual exponents and the conservative rate test

For outer alpha_F, the particular stream exponent is4+alpha_F. Every upper Green rate4-m+alpha_F is strictly negative, ensuring convergence at infinity. Every lower rate m+4+alpha_F must be nonzero for the displayed primitive formula; the exact audit checks this. The lower moment also has a transient exponent -m. No polynomial logarithm is omitted when these denominators are nonzero.

The outer linear leading term cancels exactly because c_l k=1. All other linear residual terms have exponent3+alpha_R and the corresponding degree. Particular products have exponent5+alpha_F+alpha_R; lower-transient products have exponent1-m+alpha_R. The correction-correction products have exponent5-2b_o and degree up to12. Their normalized rate is at most

5-2b_o+12/T+delta-k.

The coarse source test uses a line5-b_o+6/T+delta. Its excess over the degree12 rate is b_o+k-6/T, positive for the exact parameters and T>=9. The same coarse line also bounds the two mixed correction-leading products; the leading product line2k-1+delta-k bounds all products of the degree0 outer terms. Transient products decay faster. The exact enumerator checks every family and the dominance of the aggregate coded maximum, rather than relying on this prose alone.

For the given exponents the binding normalized rate is k-1+delta. It is negative for both stated delta values. The omitted explicit degree12 line therefore does not invalidate the monotonicity conclusion for these parameters. It remains an undocumented coverage step until proved as above. A source that emits a claimed tail bound when its monotone_ok flag is false must still be rejected; this theorem only applies when its hypotheses have actually been checked.

## Scope and dependencies

Dependencies: exact modal representation and matching, canonical Green formula, symbolic normalization, elementary exponential-polynomial integration, and the finite exact enumeration in code/check_exponents.py. Source snapshots and hashes are in evidence/source_snapshot.json. This result does not accept any stored numerical tail bound, coefficient enclosure or normalization import. It does not cover derivative residuals or provide a linear inverse. It gives no YES or NO endpoint for IPM Analysis I.
