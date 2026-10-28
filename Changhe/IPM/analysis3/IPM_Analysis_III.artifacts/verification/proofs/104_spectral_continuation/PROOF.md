# Spectral continuation and the obstruction from a free cubic jet

## Abstract conditional theorem

Let Z and Y be Banach spaces, and let T,C:Z->Y be bounded linear maps. Let X_H and Y_H be Banach spaces continuously embedded in Z and Y respectively. All maps below use these same embeddings, so that equality in Y_H implies equality in Y. Suppose C:X_H->Y_H is bounded, with norm c. Let J_s:X_H->Y_H be a bounded linear shift map, with norm j_s. Set

 D_H={h in X_H:T h belongs to Y_H},
 ||h||_D=||h||_X_H+||T h||_Y_H,
 L=T+C.

Assume the following statements for some omega>=0 and M>=1.

1. For every lambda>omega, T-lambda J_s:D_H->Y_H is bijective, and its inverse has Y_H->X_H norm at most M/(lambda-omega).
2. Put lambda_*=omega+1+2Mc. There are C_1<infinity, a Banach space W and a compact K:X_H->W such that, for every h in D_H and 0<=lambda<=lambda_*,

 ||h||_X_H<=C_1||(L-lambda J_s)h||_Y_H+||Kh||_W.       (1)

Then L:D_H->Y_H is Fredholm of index0. If the low map L:Z->Y is injective, the high map is bijective. If the low map has a bounded inverse with norm K_L and K factors as K' composed with the inclusion X_H->Z, then

 ||L^(-1)||_(Y_H->X_H)<=C_1+||K'|| K_L iota,             (2)

where iota is the norm of Y_H->Y. The high inverse is exactly the restriction of the low inverse. This theorem is conditional: none of its hypotheses about the actual variable-order spaces is supplied by the abstract argument.

The choice lambda_*=omega+2Mc is also valid when c>0. Adding1 avoids the endpoint lambda_*=omega when c=0.

## Proof

First D_H is complete. A Cauchy sequence converges to h in X_H and its T images converge to f in Y_H. The embedding in Z and continuity of T:Z->Y imply T h_n->T h in Y. The embedding Y_H->Y also implies T h_n->f in Y, hence T h=f. The original sequence converges in the graph norm. The embedding D_H->X_H is continuous, so K is compact on D_H.

Write R_lambda=(T-lambda J_s)^(-1). The equation gives

 ||T R_lambda f||_Y_H<=||f||_Y_H+lambda j_s M/(lambda-omega)||f||_Y_H.

Thus the given inverse is bounded into D_H, not merely into X_H. At lambda_*,

 L-lambda_* J_s=(I+C R_lambda_*)(T-lambda_* J_s),
 ||C R_lambda_*||<=Mc/(1+2Mc)<1/2.

The Neumann series proves that this endpoint is an isomorphism.

For A_lambda=L-lambda J_s, the triangle inequality and (1) give

 ||h||_D <= [1+(1+c+lambda j_s)C_1]||A_lambda h||_Y_H
                       +(1+c+lambda j_s)||Kh||_W.         (3)

An estimate of this form implies finite-dimensional kernel and closed range. To verify both assertions, the unit ball in the kernel is relatively compact: compactness of K, followed by (3) for differences, makes every sequence have a convergent subsequence in D_H. A normed space with compact unit ball is finite dimensional. Choose a closed complement D_1 to this finite-dimensional kernel. If the restriction of A_lambda to D_1 were not bounded below, there would be unit vectors h_n in D_1 with A_lambda h_n->0. Extracting a K-convergent subsequence and applying (3) to differences would give a norm limit h in D_1 with norm1 and A_lambda h=0, a contradiction. Boundedness below on D_1 proves closed range. Hence every A_lambda is upper semi-Fredholm.

The path lambda->A_lambda is norm continuous as a path in B(D_H,Y_H), because J_s is bounded on X_H. The extended index is locally constant on the semi-Fredholm set, including index -infinity. Therefore its value on the connected parameter interval is the endpoint value0. In particular no infinite-codimensional range occurs along this path, and L is Fredholm of index0. The semi-Fredholm perturbation theorem used here is stated for Banach spaces in Le Quang Chu, "Duality and Kato's theorem on small perturbations", Bulletin of the AMS82 (1976), pp896-898, opening paragraph, with its original reference to Kato, Journal d'Analyse Mathematique6 (1958), pp261-322. The later family formulation is also explicit in Berkani, arXiv:2010.13327, Theorems2.2 and2.6. Both statements were checked directly during this audit.

For the Hilbert spaces intended in the application the index step has an elementary block proof. At a fixed upper semi-Fredholm operator A, split the domain as ker(A) plus its orthogonal complement and the target as range(A) plus its orthogonal complement. A restricts to an isomorphism between the second domain component and range(A). A sufficiently small perturbation preserves this invertible block. Eliminating the off-diagonal blocks leaves a map from the finite-dimensional ker(A) to range(A)^perp. Its index is dim ker(A)-dim range(A)^perp, independent of that finite block, with value -infinity if the latter dimension is infinite. This proves local constancy directly.

Since D_H embeds in Z, a high null vector is a low null vector. Low injectivity and high index0 imply high bijectivity. The equation is the same in Y, so uniqueness identifies the high solution with the low solution. Apply (1) at lambda=0, then ||Kh||<=||K'||||h||_Z and the low inverse estimate, to obtain (2). The graph norm of the high inverse is also bounded, using ||T h||_Y_H<=||f||_Y_H+c||h||_X_H. This completes the proof.

## Why the physical identity is not an admissible shift for the actual free-jet spaces

Use the actual spaces of topics38 and43, with a=17/4, G=L2(e^(-t/2)dt for t<0; e^(27t/4)dt for t>=0), and Z=E B plus D_R. Here E beta=x^2 y beta(log r), the cubic coefficient j(beta) is continuous on B, and the target is Y=E G plus R. The actual positive axis rate and endpoint estimates were independently verified earlier in this run.

Choose a smooth radial cutoff chi_0 equal to1 near0 and0 outside a compact set, and put

 beta_0(t)=chi_0(e^t), e_0=E beta_0.

Then beta_0 belongs to B. Indeed beta_0/H equals1+O(e^(2t)) at negative infinity, its derivative has that same decay, and it vanishes near positive infinity. It has cubic coefficient1. Proof 43 proves that e_0 belongs to Z. It also belongs to every intended high space in which the free cubic coordinate is separated and its remainder is measured at origin exponent delta<2.

But beta_0 does not belong to G: its squared norm contains the divergent integral of e^(-t/2) near negative infinity. The uniqueness of the target decomposition forces the jet of e_0 in Y, if it existed, to equal beta_0. Thus e_0 is not in Y. In particular an X_H containing this permitted free cubic direction cannot be contained in Y_H subset Y. For nonzero lambda, T e_0-lambda e_0 is not in Y, since T e_0 is in Y. The physical spectral shift is not a map on the specified spaces.

Restricting to j=0 does not repair this argument without changing the theorem. By the proved low Fredholm theorem and proof 85, this restriction has index -1 as a map to the original target Y. Its missing scalar compatibility cannot be omitted. Restricting the target to a matching range would require a new, explicitly proved realization.

## Why simply subtracting the cubic coordinate does not give the stated resolvent estimate

The bounded map P_0:Z->Y given by

 P_0 h=h-j(h)e_0

is well defined. For its jet this follows from the Hardy estimates of proof 38: beta-j(beta)chi_0 belongs to G, with norm bounded by ||beta||_B. The remainder is already in R. But P_0 e_0=0.

More generally, hypothesis1 forces every vector h in D_H with J_s h=0 to vanish. For otherwise

 ||h||_X_H<=M/(lambda-omega)||T h||_Y_H

holds for all sufficiently large lambda, and letting lambda tend to infinity gives a contradiction. Therefore P_0 cannot obey hypothesis1 on any D_H containing e_0. Even adding a smooth rank-one target does not solve this in the usual way: if f belongs to D_H intersect Y and has zero cubic coefficient, the shift P_0+j(.)f kills e_0-f. Any different shift requires an independent proof of its resolvent and of (1); the latter is no longer automatic from positivity of the physical identity.

## Additional audit points

For an ordinary common-state transport generator T=V.grad-1 with a strongly continuous composition semigroup, the formal formula is

 (T-lambda)^(-1)f=-integral_0^infinity e^(-(1+lambda)s)f composed with Phi_s ds.

A bound on this formula requires a compatible state space and its generator domain, in addition to estimates on the composition maps. A variable regularity order that is nondecreasing along Phi_s has the correct sampling direction: the value at X samples data at the downstream point Phi_s(X). This direction is necessary for the proposed argument, but by itself supplies neither the finite composition bounds nor the jet compatibility just shown to fail.

The negative frozen source energy margin for transport alone explains why the known coupled energy estimate cannot be continued by removing the coupling. Its sign alone does not prove any semi-Fredholm assertion. For example d/dx+a on a circle is invertible whenever a is a nonzero real number, regardless of the sign of its real quadratic form. The source-specific claim that transport is not semi-Fredholm needs a separate spectral or singular-sequence proof.

The conclusions about the abstract theorem are CONFIRMED. Its proposed direct application through X_H subset Y_H to the actual free-J realization is REFUTED. Construction of a compatible replacement and the actual high inverse remain OPEN.
