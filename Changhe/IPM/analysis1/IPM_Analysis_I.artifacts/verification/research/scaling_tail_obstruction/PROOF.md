# Exact nonmembership in the stored Fminus tail class

Written 2026-10-21T21:36:20.053018+00:00, before this topic's numerical checker. Status: conditional analytic theorem; the finite coefficient checks below must pass and receive actual independent review before acceptance.

## Statement, data and scope

Let t=log r and let Phi_m(theta)=cos(theta)^2 sin(theta) cos(2m theta). A real density has the finite expansion rho=r^3 sum_(m=0)^259 a_m(t) Phi_m(theta). For t>=t0 suppose

 a_m(t)=A_m exp(lambda(t-t0))+sum_q p_(mq)(t-t0) exp(lambda_q(t-t0)),

where the sum is finite, every p is a polynomial, every lambda_q<lambda, and lambda!=-2. Define K=rho-partial_t rho, with theta fixed. Let A be nonzero. Let B be a finite angular vector, padded with zeros to a common dimension if necessary. Let Fminus(A,B,lambda) consist of all finite angular functions whose radial coefficient vectors have the form

 g(t)+alpha*t*A*exp(lambda(t-t0))+beta*B*exp(lambda(t-t0)),

where alpha,beta are real constants and exp(-lambda(t-t0))g(t) tends componentwise to zero. The actual finite lower-growth column spans and their homogeneous join-constrained subspaces are subsets of this class when they have the stated tails. The compactly supported J column does not change this tail property.

If D=A_0 B_1-A_1 B_0 is nonzero, then K is not in this class. This theorem will be applied to the EXACT DYADIC interpretation of the frozen A0 and Bm arrays in research/saved_vector_external_constraints/sources/c2gram2_M16_s16_p4_H1m_NJ1_rowsH1q_vec.npz, SHA4fd4ff818efd62aa03cb4392d8d56dcaf8f948188962fc1133c38c561099ba2e. All260 A entries will be compared with the leading Aout column in data_exact/modal_v2.json, SHA57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6. The other stored trial exponents and the finite tail correction have strictly smaller rates; this will be checked exactly.

There are two rate conventions. In exact mathematics lambda=k-3 and -2-lambda=1-k. The source executable computes binary64 rates, so its literal-real interpretation instead uses lambda=fl(k-3) and factor -2-lambda. They need not equal the preceding exact values. The proof covers each convention separately, after checking their rate gaps and nonzero factor. No equality of a stored rounded join correction to the exactly joined normalized trial is asserted. This result concerns the stated stored-tail trial and Fminus recipe, not X3 or an unidentified historical runtime.

The stored Bm recipe is finite and rounded. It is not silently replaced by the exact coefficient vector of (sum A_m cos(2m theta))*cos(2theta). The source does not fill Bm[260], although the exact product generally has coefficient A_259/2 there. Both vectors have the same low-index formula before rounding. A separate exact determinant for the ideal full cosine product can be reported, but it is a separate application. The free class with extra pure leading tails is outside the asserted nonmembership result.

## Proof

Since partial_t rho=r^3 sum_m(3a_m+a'_m)Phi_m, the radial coefficients of K are -2a_m-a'_m. Differentiating the displayed finite exponential-polynomial expansion gives

 exp(-lambda(t-t0))(-2a-a')=(-2-lambda)A+o(1).

Indeed any polynomial and its derivative times exp((lambda_q-lambda)(t-t0)) tend to zero because lambda_q-lambda<0. This can be seen from the exponential power series: for delta>0 and a polynomial of degree d, exp(delta*s)>= (delta*s)^(d+1)/(d+1)! for s>0, so s^d exp(-delta*s) tends to0.

The finite angular functions Phi_m are linearly independent. A zero finite linear combination vanishes after division by cos(theta)^2 sin(theta) on an open arc where this factor is nonzero. The resulting cosine polynomial is zero on that arc. It is a polynomial in cos(2theta), by the recurrence C_0=1,C_1=x,C_(m+1)=2xC_m-C_(m-1); an open arc avoiding critical points gives an interval of x-values, so the polynomial is identically zero. Its nonzero highest leading coefficient then forces every coefficient to vanish. Thus equality of the functions forces equality of their radial coefficient vectors.

If K belonged to the class, the preceding asymptotic expansion would yield

 (-2-lambda)A=alpha*t*A+beta*B+o(1).

Divide by t and let t tend to infinity. The left side and beta*B/t tend to zero, hence alpha*A=0. Since A!=0, alpha=0. Taking the limit in the original identity gives (-2-lambda)A=beta*B. The two low coordinates have determinant (-2-lambda)D=0, contrary to lambda!=-2 and D!=0. This proves the theorem. The argument uses no closure of the class and makes no assertion about distance to its span or closure in a norm.

## Source interpretation and finite verification

The frozen c2_fminus source has lower function columns supported at or below t0, or outer rates q!=0, and two exceptional columns KP and TAU. On t>=t0 its cutoff_pieces appends exactly [t0,1] in the shifted variable t-t0 for KP and [1] for TAU. These equal t and1. The KP and TAU sums use all260 trial indices. The stored Bm has261 slots but its final slot is zero. No finite row weights, column rescalings, whitening, constraints or retained eigendirections enlarge the underlying finite span.

The new checker will decode every A0/Bm/k/t0 entry independently from ZIP/NPY bytes and IEEE754 integers, and compare with a second NumPy+as_integer_ratio path. Exact Fraction and fmpq arithmetic will compute the determinant independently. Arb and mpmath.iv will enclose it separately and certify a stated strictly positive decimal interval by exact endpoint comparisons. The vector and source bytes are pinned. The exact mathematical rates and binary64 source rates will each be tested for strict ordering, including the outer correction. An independent integer nearest-even rounding routine will check the source's elementary dyadic rate and Bm operations, without importing or executing the numerics lane's modules. The full ideal cosine-product coefficient vector will be derived by the cosine product identity and checked by an independent signed-frequency scatter.

Passing establishes only this exact tail-class obstruction for the explicitly identified stored data and recipes. It neither proves an inverse/coercivity estimate nor a positive distance from any section, a defect of an ideal projection, admissibility or normalization, or an IPM endpoint. The prior referee text is a proposal to audit, not evidence for the determinant.
