# Fredholm index zero on the actual high spaces

## Exact statement

Use the exact modal background, X_s, D_s and S=T+C_R of proof 149, with graph norm on D_s. Then

 S:D_s->X_s

is Fredholm of index zero. More generally S-lambda has that property for every real lambda>=0.

Define a(t)=e^(-3t)b(t), Gamma_H=a H^(25/4)(R), and choose a smooth cutoff chi_0(t) equal to one near negative infinity and zero near positive infinity. The scalar domain is

 B_H={beta=J chi_0+a v:J in R, v in H^(29/4)(R)},
 ||beta||B_H=|J|+||v||H^(29/4).

The representation is unique because chi_0/a is not square integrable at negative infinity. This is the scalar graph domain of proof 114, with equivalent norm. Let E beta=x^2 y beta(log r), A_axis beta=d beta'+(D-d-2d')beta, D=4c_l-1, and d the actual positive vertical-axis transport rate.

For h=E beta+u, beta in B_H, u in D_s, define the exact coordinate operator

 L_ren(beta,u)=(A_axis beta+Gamma_C[E beta+u],
               G beta+S u),
 G beta=(T E beta-E A_axis beta)+C_R E beta.              (1)

Then L_ren:B_H plus D_s -> Gamma_H plus X_s is Fredholm of index zero. For every fixed zeta in Gamma_H plus X_s, the operator

 L_red=L_ren+c[E beta+u] zeta                            (2)

has the same property. In particular this applies to the actual moving-tail vector zeta whose membership was checked in topics83 and123. The uncut physical identity term is not silently substituted for (1)-(2).

If the corresponding low realization of either L_ren or L_red is injective, that high realization is bijective and its inverse is the restriction of the low inverse. The present theorem does not prove that injectivity or a numerical inverse bound.

## Closed domains and the large parameter endpoint

The domain D_s is complete because T is distributionally closed and the embedding of X_s in distributions is continuous. Proof 126 identifies it with the generator domain of the actual strongly continuous transport semigroup. There are finite omega and M such that

 ||(T-lambda)^(-1)||_(X_s->X_s)<=M/(lambda-omega), lambda>omega.

Here M may exceed one in the chosen equivalent norm. Set c_H=||C_R||_(X_s->X_s) and choose

 lambda_*=omega+1+2M c_H,

increasing omega to be nonnegative if needed. Then

 S-lambda_*=[I+C_R(T-lambda_*)^(-1)](T-lambda_*),
 ||C_R(T-lambda_*)^(-1)||<1/2.

The Neumann series gives an isomorphism D_s->X_s. Its inverse is bounded into the graph domain because T u=f+lambda_*u-C_Ru. This endpoint argument requires no numerical value of omega or c_H.

## The compact estimate and index continuation

For every finite parameter interval, proof 149 gives a common compact K:X_s->W_0 and

 ||u||X_s<=C||(S-lambda)u||X_s+||Ku||W_0.

Since Tu=(S-lambda)u-C_Ru+lambda u, the same estimate controls the graph norm, with changed constants. K is compact on D_s as well, through its continuous inclusion in X_s. The standard compactness argument gives finite-dimensional kernel and closed range: otherwise a normalized sequence in the kernel, or in a fixed complement with images tending to zero, would have a K-convergent subsequence and then a graph-norm convergent subsequence, contradicting its normalization or separation. Thus every S-lambda on that interval is upper semi-Fredholm.

For completeness, index constancy here has an elementary Hilbert-space proof. At an upper semi-Fredholm operator, split the graph domain into its finite-dimensional kernel and an orthogonal complement, and split the target into the closed range and its orthogonal complement. The block from the domain complement onto the range is invertible. A sufficiently small operator perturbation preserves that block. Eliminating the other off-diagonal blocks reduces kernel and cokernel to a map from the fixed finite-dimensional kernel into the fixed range complement. Its extended index is the dimension of the former minus the dimension of the latter, independently of this remaining finite block. If the latter is infinite the extended index is minus infinity. Therefore the extended index is locally constant on the upper semi-Fredholm set.

The path lambda->S-lambda is continuous in operators D_s->X_s. Its connected interval has the index of the invertible endpoint, namely zero. In particular the cokernel is finite dimensional. For a given larger lambda one enlarges the finite interval to include both it and lambda_*, obtaining the same conclusion. This proves the remainder assertion.

## The scalar row and the full block

Proof 114 proves A_axis:B_H->Gamma_H is an isomorphism with the stated physical free cubic coefficient. The scalar domain norm written above is equivalent to its graph norm; its endpoint proof uses 1/4<delta<2 and gamma<min(k,-3/8), all satisfied by the present parameters. No spectral shift is applied to this free cubic coordinate.

Proof 123 proves G:B_H->X_s is bounded and Gamma_C:E B_H plus X_s->Gamma_H is compact. The lower triangular operator

 M(beta,u)=(A_axis beta,G beta+S u)

factors as

 M=[[I,0],[G A_axis^(-1),I]] diag(A_axis,S).

The first factor is an isomorphism of the target direct sum, with bounded inverse obtained by changing the sign of the lower off-diagonal entry. Hence M is Fredholm of index zero. The first-row Gamma_C correction in (1) is compact on B_H plus D_s, because it is already compact on the weaker B_H plus X_s domain. Compact perturbation invariance proves the assertion for L_ren.

The functional c is bounded on the low domain and on this high domain through the verified continuous embedding. Multiplying it by the fixed high-target vector zeta in (2) gives a rank-one bounded operator, hence a compact one. This proves the assertion for L_red.

All embeddings identify the same distributional functions and preserve the exact operator identities. A high null vector is therefore a low null vector. Under low injectivity, the high Fredholm map of index zero has zero kernel and zero cokernel, so is bijective. The bounded inverse theorem gives a bounded high graph-domain inverse. Uniqueness in the low realization identifies the solutions. This supplies no explicit constant and does not assert that every low null vector has high regularity.

## Scope

This is a qualitative Fredholm theorem for the actual high spaces, not a finite-basis complement certificate. The compact operators in proof 149 have not been approximated with a numerical norm bound. A finite section with positive singular values alone still does not certify injectivity. The nonlinear residual, second derivative bounds, derivative loss and uniformity for perturbed backgrounds remain separate from this theorem.
