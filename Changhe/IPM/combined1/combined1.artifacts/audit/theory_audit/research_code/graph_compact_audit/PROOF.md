# Audit of graph-compact repairs and approximate-inverse floors

## Exact setting

Let Y be the complex Hilbert space in the audited dyadic framework, with 0<a<2, finite positive Rw, c>0 and beta=1+c-ca>0. Let L be a closed densely defined realization containing the compact smooth tests of the audited far-field theorem. Assume that theorem's finite-angular background decay hypotheses. For every real xi it supplies e_N in D(L) such that

    ||e_N||Y=1, e_N converges weakly to0 in Y,
    (L-lambda)e_N ->0 in Y, lambda=-beta+i c xi.

The present audit checks the three extensions R1 to R3 in the frozen T2 review. It also distinguishes an approximate-inverse norm from an effective inverse bound. No numerical spectrum is used.

## Graph-compact perturbations

Suppose K:D(L)->Y is linear and compact for the graph norm. Then A=L+K on D(L) is closed, and the same lambda admits the same normalized singular sequence for A. Moreover A-lambda does not have both closed range and finite-dimensional kernel.

First, K is L-bounded with relative bound zero. If, for some epsilon>0, no constant C gave

    ||Ku||<=epsilon||Lu||+C||u||,

normalize a contradicting sequence in graph norm. Its Y norm tends to0 while its K norm stays bounded away from0. The Hilbert graph space has a weakly convergent subsequence. Since the graph of L is a closed linear subspace of Y x Y, its weak limit with first coordinate0 has second coordinate L0=0. The subsequence is weakly null in graph norm, so compactness of K forces its K image to converge strongly to0, a contradiction. A relative bound below1 makes the graph norms of L and A equivalent and proves A is closed.

The sequence(L e_N) is weakly null because L e_N=lambda e_N+o(1). Thus e_N is weakly null in the graph space and K e_N->0. Consequently(A-lambda)e_N->0. If A-lambda had closed range and finite-dimensional kernel, its restriction to the Y-orthogonal complement of the kernel would have a bounded inverse onto its range, by the bounded inverse theorem in graph norm. Subtracting the kernel projections, which tend to0 because e_N is weakly null, contradicts the normalized singular sequence. This proves the asserted failure of upper semi-Fredholmness, without relying on a convention for naming an essential spectrum.

This confirms T2 R1. A conclusion about a different space or a noncompact principal perturbation would require a new argument.

## Approximate left inverses

Let A be as above. Let B:Y->Y be bounded and assume on D(A) that

    I-B(z-A)=C+E,

where C is compact from the graph space D(A) to Y and E is bounded on Y with ||E||<=kappa<1. Choose xi=Im(z)/c. Graph norms of A and L are equivalent, and e_N is graph-weakly null for A. Therefore C e_N->0 and

    1-kappa-o(1)<=||B(z-A)e_N||
       <=||B||(|Re z+beta|+o(1)).

If Re z+beta is nonzero, this yields

    ||B|| >= (1-kappa)/|Re z+beta|.                       (1)

If it is zero, no such B,C,E exist. This proves T2 R2 with an explicit graph convention. At z=0,xi=0 the tests are real, so no complexification is needed for the stationary floor, confirming R3.

## What (1) does not certify

An inverse modulo a compact operator is not necessarily an inverse. On any infinite-dimensional Hilbert space choose a nonzero finite-rank orthogonal projection P, A=-beta I+beta P and B=-I/beta. Then I-BA=P is compact, while A has the nontrivial kernel ran P. A separate finite-dimensional invertibility check remains necessary.

Also, decreasing ||B|| by increasing its defect does not improve an actual invariant-ball threshold. For A=-beta I, B=-epsilon I/beta with0<epsilon<1 has ||I-BA||=1-epsilon and exactly attains(1). The iteration for Ah+f=0 is

    h -> h-B(Ah+f)=(1-epsilon)h+epsilon f/beta.

Its norm estimate preserves a ball of radius r only when ||f||/beta<=r. The factor epsilon cancels. Thus ||B||||f||<=r alone is not an invariant-ball certificate with nonzero defect.

More generally, if D=I-BA is bounded with ||D||<1, the standard corrected left inverse has bound ||B||/(1-||D||), not ||B||. For an actual bounded inverse the original far-field floor1/beta still applies. T2 section5 is a valid weaker necessary comparison only if its displayed closure conditions are independently established with the stated K_H. It must not be read as a proof of a residual-threshold gain by1/(1-kappa).

## Review acceptance and a range correction

The frozen T2 review independently confirms the weakly-null and compact-perturbation extension of T4-124, with the exact reviewed proof hash. Its direct harmonic-mode argument also independently verifies the canonical velocity vanishes inside the support of the first-mode test. The extension is therefore eligible for AUDITED status under the campaign's rules.

The row a=1/2 in the review's table already lies in0<a<2 and is covered by the exact Y theorem and its envelope bound. It need not be called heuristic when it means that same Y. The a=0 row lies outside the stated framework and is not certified by this theorem alone. Neither table row is a proof about a different norm.

## Dependencies and scope

Dependencies are the audited far-field normalized sequence, Hilbert weak compactness, closed graph subspaces, compact operators and the bounded inverse theorem. All additional arguments are supplied above. No conclusion is made that a candidate profile fails to exist. The result concerns the specified realizations and the precise defect identity, not an arbitrary Newton or finite-rank implementation.
