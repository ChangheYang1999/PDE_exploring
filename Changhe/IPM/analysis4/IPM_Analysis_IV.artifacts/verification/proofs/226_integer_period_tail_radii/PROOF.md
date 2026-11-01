# Tail response bounds for integer-period tuned profiles

Status: PROVED comparison theorem after the independent theory-part review at 2026-10-31T16:42Z. The completed Q4-root2 and Q5-root6 certificates are admitted in V469; the other sampled targets gave no smaller radius.

## Statement

Let Q>=3, delta=2/Q, and c=Q/(Q-2). Let f_1 be a nonzero real odd-sine polynomial of bandwidth B, where B is even. Assume the first compatibility obstruction at order 2Q vanishes and that the uniquely tuned pure density and stream coefficients through the required finite prefix have been certified as in topic 175. Fix M>=2 and N=MQ. Suppose

    d_j >= j ||f_j||_1 for 1<=j<=N,
    e_1=0,
    e_a >= aQ |H_(aQ)| for 2<=a<M.

It suffices for the prefix majorant of topic 175 to assume the response lower bound

    |sigma_k| >= s_M > 0 for every integer k>=M.

Every exact nonnegative box certificate for that majorant at w_0>0 then gives convergence of the tuned density, stream and common-potential series, with all appropriately weighted derivatives, on each closed exterior r>=R>w_0^(-1/2). The potential retains the two finite logarithmic corrections at orders Q and 2Q. An amplitude factor epsilon!=0 multiplies the sufficient radius by |epsilon|^(Q/2). No global stationary extension or optimal radius is asserted.

## Proof

In topic 175 the known polynomials contain all density coefficients through N and the harmonics H_(aQ) for a<M. The unknown harmonic series starts at H_N. Every subsequent tuning step has index n=kQ with k>=M and uses the affine identity

    H_(kQ) = -R_k/sigma_k.

The proof of the harmonic comparison uses the response estimate only to bound this division by 1/s_M. The earlier response values do not enter any unknown coefficient equation: their effect is already included in the certified d_j and e_a. Thus the total-order induction of topic 175, with its unchanged constants L and kappa_N, proves the same coefficient inequalities after replacing its global lower bound by s_M. The residue projection, triangular affine part at zero, nonnegative fixed-point iteration and exact box argument are unchanged. They supply the same geometric coefficient bound. Topic 175's strict exterior ratio then absorbs the derivative factors, and its potential reconstruction and amplitude scaling give the stated conclusions.

The condition M>=2 ensures that the first unknown harmonic is a true positive-frequency stream kernel. At index Q there is no such kernel, which is why e_1=0 is essential. A successful tail certificate cannot replace an unproved finite prefix or a missing compatibility identity.

## Certifying the integer tail

For the two-mode profiles f_1=sin(theta)+b sin(3 theta), use B=4 and the exact algebraic root intervals already certified for Q=4,5,6. Let

    K=max(M,ceil((BQ+2)/2)).

Then 2K-2>=BQ, so the compact response formula of topic 149 is valid for every k>=K. Check the finite indices M<=k<K directly by the full two-carrier Cartesian response. Cover the closed interval

    0<=t<=1/(2K-2)

by rational bisection. Accept a leaf only if its directed response enclosure has absolute lower bound greater than s_M. Discard it only if the exact integer range

    max(K,ceil((1/b+2)/2)) <= k <= floor((1/a+2)/2)

is empty, where [a,b] is the leaf and a=0 means no upper bound. All other leaves must be split or the attempted certificate fails. The complete partition and the dyadic enclosure inequalities are retained and independently replayed. The direct finite responses together with the compact cover prove the entire integer-tail bound. Samples or a limiting response may choose a tentative s_M but are never used in place of this proof.

## Required evidence

The first computations reuse the independently audited prefixes N=40,50,60 for Q=4,5,6 from topics 178,182,186. Each new certificate records its old prefix hash, old and new response bounds, finite checks, compact-cover leaves and exact majorant box. A separate replay verifies the old initial vectors, constants, every leaf interval and integer exclusion, every dyadic lower bound, and the rational image of the new box. It also reevaluates accepted response leaves by directed arithmetic. A candidate radius is admitted only after those checks and independent review of this comparison argument.
