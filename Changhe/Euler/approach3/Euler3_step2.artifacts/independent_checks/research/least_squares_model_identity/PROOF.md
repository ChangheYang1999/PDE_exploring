# What a least-squares factor comparison establishes

## Statement and notation

Let n, m_1, m_2 be positive integers. For i in {1,2}, let J_i belong to R^{m_i by n}, let r_i belong to R^{m_i}, and define the quadratic function q_i on R^n by

    q_i(h) = (1/2) ||r_i + J_i h||_2^2.

All norms here are Euclidean. Define a_i = ||r_i||_2^2, g_i = J_i^T r_i and G_i = J_i^T J_i. Then q_1(h) = q_2(h) for every h in R^n if and only if a_1 = a_2, g_1 = g_2 and G_1 = G_2. Equal Gram matrices and column norms alone do not imply equality of these quadratic functions. Even equality of all three quantities does not imply equality of J_1 and J_2 when their row dimensions agree.

## Proof

Expansion of the squared norm gives, for each i and every h,

    q_i(h) = (1/2) a_i + g_i^T h + (1/2) h^T G_i h.

Equality of a_i, g_i and G_i therefore suffices. Conversely suppose q_1 = q_2. Evaluation at h=0 gives a_1=a_2. For each standard coordinate vector e_j, subtract the equality at -e_j from that at e_j. Since q_i(e_j)-q_i(-e_j)=2(g_i)_j, this gives g_1=g_2. Adding those two evaluations and subtracting twice the value at zero gives (G_1)_{jj}=(G_2)_{jj}. For distinct j,k, evaluate at e_j+e_k and subtract the evaluations at e_j and e_k, then add the value at zero. The result equals (G_i)_{jk}, because G_i is symmetric. Hence every matrix entry agrees. This proves the equivalence.

For the first non-implication, take m_1=m_2=n=2,

    J_1 = diag(1,1), J_2 = diag(-1,1), r_1=r_2=(1,1)^T.

Both Gram matrices are I_2, both columns have norm 1, and both squared residual norms are 2. But g_1=(1,1)^T and g_2=(-1,1)^T. In particular q_1(e_1)=5/2 whereas q_2(e_1)=1/2. Thus even an additional residual-norm comparison does not repair the missing gradient comparison.

For the second non-implication, take J_1=diag(1,1), J_2=diag(1,-1), and r_1=r_2=(1,0)^T. Now both triples (a_i,g_i,G_i) equal (1,(1,0)^T,I_2), so the quadratic functions agree, while J_1 and J_2 differ in their lower-right entry. This proves the stated limitation without invoking rounding or rank deficiency.

## Gradient from a scaled QR record

Let m>=n, let J belong to R^{m by n}, and r belong to R^m. Let P be an n by n permutation matrix and D a positive diagonal n by n matrix. Suppose

    J P D^{-1} = Q R,   Q^T Q = I_n,

with Q in R^{m by n} and R in R^{n by n}. Set t=Q^T r. Transposition and multiplication give

    P^T J^T r = D R^T t.

Indeed R^T t=R^T Q^T r=(Q R)^T r=D^{-1} P^T J^T r. Multiplication by D proves the claim. No inverse of J or R is needed. If a scale vector D_native is stored in the original column order, J[:,perm] is Q R times diag(D_native[perm]), and the gradient entries in permuted order are D_native[perm] times (R.T @ Qtr). If the recorder has already saved D_perm = D_native[perm], those entries are D_perm times (R.T @ Qtr); the permutation must not be applied to D_perm a second time. The convention must be established from the recorder, not selected merely because a numerical comparison looks favorable.

An orthogonal row change S applied to both J and r preserves all three quantities: ||Sr||^2=||r||^2, (SJ)^T(Sr)=J^T r, and (SJ)^T(SJ)=J^T J. A row permutation is a special case. Thus a valid comparison may establish the same local quadratic model while using different residual row orders. To establish equality of vector-valued Jacobians after reordering, the actual row correspondence and the reordered entries or independently sufficient witnesses must also be checked.

## Dependencies and scope

The argument uses only finite real matrix multiplication and expansion of a squared Euclidean norm. The related scaled_qr_identity/PROOF.md establishes the corresponding Gram reconstruction identity; this proof gives its gradient analogue independently. The exact examples are mathematical proofs; the executable integer controls only check their transcription. Approximate agreement of numerical factors requires explicit norms and tolerances and does not itself supply a bound for nonlinear optimization or a proof of the Euler equations. No numerical assertion about a campaign Jacobian follows from the counterexamples.
