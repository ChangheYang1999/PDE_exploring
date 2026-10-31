# Coefficient stationarity is a separate hypothesis

Status: proved finite-dimensional non-implications. No saved Euler endpoint is evaluated here.

## Statement, hypotheses and notation

Let m, a and k be positive integers. All spaces below are real Euclidean spaces. For A in R^(m by a), B in R^(m by k), q in R^m and c >= 0, define

M(h,p) = c + ||q + Ah + Bp||^2/2,  h in R^a, p in R^k.

Choose a set I of strictly positive singular values of A and let U_I, V_I and Sigma_I be its left singular vectors, right singular vectors and positive diagonal singular-value matrix. Empty I is allowed. Let H = range(V_I), P = U_I U_I^T and G = V_I Sigma_I^(-1) U_I^T. In the empty case set P=G=0 and H={0}.

At h=p=0 the full joint gradient is (A^Tq, B^Tq). Stationarity in H is equivalent to Pq=0. Full joint stationarity implies Pq=0, but joint nonstationarity does not imply Pq != 0. Even full coefficient nonstationarity A^Tq != 0 need not imply Pq != 0 when positive singular directions were discarded.

For the zero-preserving response h_resp(p)=-GBp, the affine objective difference is

Delta(p) = M(h_resp(p),p)-M(0,p)
         = -q^T PBp - ||PBp||^2/2.

The following three conditions are equivalent:

1. Delta(p) <= 0 for every p in R^k.
2. There exists epsilon > 0 such that Delta(p) <= 0 whenever ||p|| < epsilon.
3. B^T Pq = 0.

Thus Pq=0 is sufficient for all-displacement improvement in this affine model, but it is stronger than necessary. Pq != 0 by itself does not imply that q^T PBp is nonzero for any permitted parameter displacement. This statement concerns the affine model only, with no quantitative claim about a nonlinear remainder.

## Proof

Differentiating the quadratic polynomial gives the stated joint gradient. Its derivative in every direction V_I x vanishes exactly when V_I^T A^Tq=0. The singular-value identities give V_I^T A^Tq = Sigma_I U_I^Tq. Since Sigma_I is invertible, this condition is equivalent to U_I^Tq=0 and hence Pq=0. The empty case is immediate. If A^Tq=0, this equality holds, proving the implication from full joint stationarity.

To disprove its proposed converse inference, take m=2, a=k=1, c=0, A=(1,0)^T, B=(0,1)^T and q=(0,1)^T, retaining the sole singular value of A. Then

M(h,p) = (h^2+(1+p)^2)/2,
Pq=0,  A^Tq=0,  B^Tq=1.

The base is stationary in every coefficient direction but has joint gradient (0,1), which is nonzero. A failing joint stationarity test therefore cannot alone exclude the coefficient-stationary hypothesis.

For failure of the implication from full coefficient nonstationarity after truncation, take m=a=2, k=1, c=0, A=diag(1,1/2), B=0 and q=(0,1)^T, retaining only the singular value 1. Then P=diag(1,0), so Pq=0 while A^Tq=(0,1/2)^T is nonzero.

For completeness, Ah_resp=-PBp. Since P is an orthogonal projector, expanding the squares gives

2 Delta(p) = ||q+Bp-PBp||^2-||q+Bp||^2
           = -2q^T PBp-||PBp||^2.

Put b=B^TPq in R^k. If b=0, this formula gives Delta(p)=-||PBp||^2/2 <= 0 for every p. Condition 3 therefore implies 1, and 1 implies 2.

Conversely suppose b != 0. For any t>0 take p=-tb. The formula becomes

Delta(-tb) = t||b||^2 - t^2||PBb||^2/2.

If ||PBb||=0 it is strictly positive for every t>0. Otherwise it is strictly positive for 0<t<2||b||^2/||PBb||^2. In either case t can also be chosen smaller than epsilon/||b|| for any epsilon>0. There are arbitrarily small displacements with Delta(p)>0, contradicting condition 2. This proves 2 implies 3 and completes the equivalence.

Finally Pq != 0 need not imply b != 0: take A=(1,0)^T, q=(1,0)^T and B=(0,1)^T with the sole singular value retained. Then Pq=(1,0)^T but PB=0 and b=0, so Delta(p)=0 for all p. This proves the remaining non-implication.

## Dependencies and scope

The argument uses only differentiation of a quadratic polynomial, the singular-value decomposition and orthogonal projection. It reproves every identity it needs. The broader saved-QR interpretation and displacement convention are in ../PROOF.md, which remains unchanged.

The distinction corrects the inference in the lead's 2026-10-30T02:05:41Z review: failure of joint stationarity or continued nonlinear optimization does not establish Pq != 0 at a saved base. Such a claim needs a bound or measurement of the retained coefficient projection itself. Even Pq != 0 does not establish B^TPq != 0. This correction leaves the practical selection rule unchanged: evaluate kept and response starts at the same actual parameters and choose by measured iteration-zero objective. Neither candidate is guaranteed to improve by the nonlinear problem.

verification/check_exact_examples.py checks the examples using exact rational arithmetic. No formal build was run, as recorded in formal/README.md. The theorem does not assert Pq=0, Pq != 0 or B^TPq != 0 at any campaign endpoint.
