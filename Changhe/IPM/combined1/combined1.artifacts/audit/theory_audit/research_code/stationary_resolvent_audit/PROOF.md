# Audit of the positive-real resolvent continuation route

## 1. Reviewed statement and notation

The target is T1 proposal TP-1 and its finite-rank extension TP-1b in source/T1_REVIEW_v05.md. This audit concerns the analytic argument, not the newly optimized numerical constants printed before TP-1.

Let H=L2 in real S1, X=X_s as in T4-019, and B the normalized X ball of radius R. Assume (A),(C),(D) of T4-019. Set

    b=||h||2, b_s=||J^s h||2, a=||D J^s h||2,
    P=||omega D^2 J^s h||2,
    X(h)^2=P^2+2^14 a^2+2^18 b_s^2.

Assume the smooth derivative rows and b<=b_s<=b+s a. In the notation of T4-051, put alpha=m1-s q>0 and m2>0. Let A_k be the maximal low realization. The additional hypothesis is

(L0) Every real lambda>=0 belongs to rho(A_k), and ||A_k^(-1)||_(H to H)<=K_L, for every k in B.

For smooth k, the high semigroup construction uses the finite-time triangular Gronwall bound in the T4-051 addendum, without a low decay assertion. Its generator is the part of the low generator in X. This consistency is a required domain fact, supplied by the smooth flow and bounded perturbation construction.

## 2. A priori high estimate at every nonnegative real parameter

Fix smooth k in B, h in its high domain, and f=(A_k-lambda)h, lambda>=0. The graph-core extension of the derivative identities gives

    (alpha+lambda)a <= f1+q b,
    (m2+lambda)P^2 <= (f2+k1 a+v1 b)P+40a^2,              (1)

where f1=||D J^s f||2, f2=||omega D^2 J^s f||2 and k1=u1+s v1. The low inverse yields b<=K(lambda) f0, f0=||f||2, K(lambda)=||(A_k-lambda)^(-1)||. Hence

    G1=(f1+q K(lambda)f0)/alpha,
    G0=K(lambda)f0+s G1,
    G2=(f2+k1 G1+v1 K(lambda)f0)/m2+sqrt(40/m2)G1          (2)

bound a,b_s,P respectively. Replacing alpha+lambda,m2+lambda by alpha,m2 only enlarges the bounds. Thus

    X(h)<=C(K(lambda)) X(f),                              (3)

with an explicit finite continuous increasing C. The square-root estimate used in (2) follows by completing the quadratic in P. It remains valid when P=0 or a=0 by continuity. This is a domain estimate; it does not presume that every high f is in the high range.

## 3. Continuation of high invertibility down the real axis

Let A_H be the smooth high generator and S={lambda>=0:lambda in rho(A_H)}. This set is nonempty because the high semigroup has a finite growth bound. It is relatively open by the resolvent identity.

Let lambda_n in S tend to lambda_*. Hypothesis (L0) and local continuity of the low resolvent give a finite bound on K(lambda_n) near lambda_*. By (3), ||(A_H-lambda_n)^(-1)|| is uniformly bounded by some C_*. For large n, |lambda_*-lambda_n| C_*<1. Factoring A_H-lambda_* through A_H-lambda_n and applying a Neumann series proves lambda_* in rho(A_H). This direct argument establishes relative closedness without any assumption about normality or spectral distance equality.

Connectedness of [0,infinity) therefore gives S=[0,infinity). At zero, (2) with K(0)<=K_L gives the claimed component bound. Writing the three linear forms as the rows of a nonnegative matrix N acting on

    x_f=(f2,128 f1,512 f0)

gives X(A_k^(-1)f)<=||N x_f||<=||N||X(f). This avoids replacing the Euclidean input unit ball by a coordinate cube.

For rough k, use normalized smooth approximants in B and the resolvent identity of the T4-051 addendum, replacing its factor2 by K_L. The right side tends to zero in H. Weak X compactness passes the final high norm bound. Thus no high energy identity needs to be extended separately to rough coefficients.

The original normalization and complete-low-ball contraction proof now applies with contraction K_L c_s R. TP-1 is therefore CONFIRMED under its stated positive alpha,m2 and consistency hypotheses. In particular (L0) is stronger than invertibility only at zero. The real-axis hypothesis cannot be dropped from this continuation proof without another high surjectivity argument.

## 4. Finite-rank reduction and the additional positivity condition

Write A_0=D_0+Psi Phi, where Psi e_j=psi_j in X and (Phi h)_j=<phi_j,h> with phi_j in H. Suppose D_0 has low dissipativity gap beta_D>0, and let D_k=D_0+U[k].D. Complete Lipschitz transport plus bounded finite-rank perturbation gives the maximal low realization. The skew added transport preserves the gap, so

    R_k(lambda)=(D_k-lambda)^(-1),
    ||R_k(lambda)||<=1/(beta_D+lambda), lambda>=0.

The standard finite-dimensional factorization proves that A_k-lambda is invertible exactly when

    M_k(lambda)=I+Phi R_k(lambda)Psi

is invertible. In that case

    (A_k-lambda)^(-1)
       =R_k-R_k Psi M_k^(-1) Phi R_k.                       (4)

For g_j=R_0(lambda)psi_j in X, the common-domain identity is

    R_k(lambda)psi_j-g_j=-R_k(lambda)(U[k].Dg_j).

Using ||k||2<=R/512 and ||Dg_j||infinity<=c_s X(g_j), its i,j matrix element has absolute value at most

    ||phi_i||2 (R/512)c_s X(g_j)/(beta_D+lambda).            (5)

Thus a certified lower bound on sigma_min(M_0(lambda)) larger than the operator norm of the matrix of bounds (5) proves invertibility uniformly in k. A Frobenius bound on that error matrix is sufficient. A certified interval cover in lambda plus the elementary large-lambda Neumann bound can implement this step. No such numerical certificate is supplied here.

There is one missing condition in TP-1b as printed. Its proposed bound for X(g_j) uses the derivative rows after subtracting Psi Phi. Put

    d1=sum_j ||D J^s psi_j||2 ||phi_j||2,
    d2=sum_j ||omega D^2 J^s psi_j||2 ||phi_j||2.

The safe modified rows have q'=q+d1 and v1'=v1+d2. Their triangular coefficient is

    alpha'=m1-s(q+d1),                                    (6)

with k1'=u1+s(v1+d2). The proposed application of the argument in Sections 2 and 3 requires alpha'>0 and m2>0. Finiteness of the rank and membership psi_j in X do not imply (6) is positive. An arbitrarily large d1 can make it fail. Alternatively, one may supply an independent certified high bound on the g_j without these rows.

Accordingly, the Woodbury formula and perturbation estimate of TP-1b are CONFIRMED, but its automatic high bound from the modified rows is OPEN unless alpha'>0 is added or another high regularity certificate is supplied. This is a gap in the stated sufficient conditions, not a counterexample to the finite-rank strategy.

At lambda=0, a resulting low inverse constant can be bounded explicitly from (4): if sigma_min(M_k(0))>=epsilon>0, then

    ||A_k^(-1)||<=1/beta_D
       +||Psi|| ||Phi||/(beta_D^2 epsilon).                (7)

This value, or any smaller independently certified value, must be used as K_L in TP-1. Merely proving that M_k is nonsingular does not provide a useful numerical K_L without a quantitative margin.

## 5. Scope

This audit establishes the positive-real continuation argument and pinpoints the extra high-row positivity required by its proposed finite-rank implementation. It does not verify the background rows, low dissipativity, finite-rank approximation, real-axis matrix certificate or residual threshold for any profile. No nonlinear existence claim follows until those conditions are supplied.

Dependencies are the audited derivative rows of T4-013/T4-051, the corrected rough approximation in the T4-051 addendum, the closed-operator resolvent identity, a finite-dimensional factorization, and Hilbert weak compactness. The optimized matrix norms printed in R1-009 are separate numerical claims and are not part of this verdict.
