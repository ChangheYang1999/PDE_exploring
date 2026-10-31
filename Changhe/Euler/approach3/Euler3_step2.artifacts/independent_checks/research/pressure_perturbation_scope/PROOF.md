# Propagation of finite pressure-table perturbations into derivative differences

## Statement and notation

Fix positive integers n,m,k. All quantities in this statement are real and finite. Let f in R^n, b in R^k, T in R^(m by n), B in R^(k by m), and a diagonal matrix W in R^(k by k). Define a residual vector

    R(T) = b + W B T f.

Here f is a fixed source coefficient vector, T a finite pressure table, B a reconstruction matrix, and W fixed residual row weights. This is an abstract finite linear stage, not an assertion that every part of the Euler implementation has this form. At a given parameter point, any other dependencies are held fixed for this comparison.

For a matrix or vector A, write |A| for entrywise absolute value. Suppose a nonnegative matrix E satisfies |T_tilde - T| <= E entrywise. Define the nonnegative vector

    e = |W| |B| E |f|.

For every row index i, |R(T_tilde)_i - R(T)_i| <= e_i. Consequently, for every set G of residual rows,

    ||R(T_tilde)-R(T)||_(2,G) <= ||e||_(2,G).

No condition on the signs or cancellation of f, B or T is needed.

Now let h>0 and suppose the residual comparison is made at four parameter offsets +h,-h,+2h,-2h. Quantities f,B,W,E may differ at each offset. Denote the corresponding row-group error upper bounds by e_G(+h), e_G(-h), e_G(+2h), e_G(-2h). Define centered and five-point differences by

    D_h  = (R(+h)-R(-h))/(2h),
    D4_h = (8R(+h)-8R(-h)-R(+2h)+R(-2h))/(12h).

The differences constructed from perturbed residuals satisfy

    ||D_tilde_h-D_h||_(2,G)
        <= [e_G(+h)+e_G(-h)]/(2h),
    ||D4_tilde_h-D4_h||_(2,G)
        <= [8e_G(+h)+8e_G(-h)+e_G(+2h)+e_G(-2h)]/(12h).

These are exact-real-arithmetic statements. A floating-point certificate must additionally bound its own arithmetic or distinguish measured quantities from upper bounds.

## Proof

Subtract the residual definitions to obtain delta R = W B (T_tilde-T) f. For each row, apply the triangle inequality first to the multiplication by B and then to the multiplication by T_tilde-T. The resulting sum is exactly the corresponding entry of |W| |B| E |f|. The Euclidean row-group inequality follows by squaring each nonnegative component bound, summing over G and taking the square root.

Subtract the two formulas for each finite difference. The centered difference contains the two residual errors with coefficients 1/(2h) and -1/(2h); the five-point difference contains four errors with coefficients 8/(12h), -8/(12h), -1/(12h), and 1/(12h). Apply the norm triangle inequality and the already established bounds at each point. This proves both statements.

## Finite exponential sums

Suppose a table entry is a finite sum T_ij = sum_q a_ijq exp(x_ijq), with all a_ijq fixed. At a selected subset S_ij, assume exp(x_ijq) <= epsilon and the absolute value of its computed replacement is at most epsilon_hat. Then the contribution of those selected entries to table error satisfies

    E_ij = (epsilon + epsilon_hat) sum_(q in S_ij) |a_ijq|.

Indeed, each selected exponential error has absolute value at most epsilon+epsilon_hat, and the triangle inequality gives the sum. If selected terms are replaced by exact floating zero, take epsilon_hat=0. If the computed low and high parts are both retained, a sufficient measured magnitude is |high|+|low|, but a measured magnitude alone is not a verified upper bound on the mathematical implementation for unseen inputs.

For the pressure kernels, the coefficient a includes the quadrature weight, radial basis factor, trigonometric factor and Green normalization. A statement about count times epsilon controls this table sum only after those factors are included. To compare with derivative noise, the later source coefficients, reconstruction, residual weights and the finite-difference divisions must also enter the preceding inequalities. Source-node exponential factors must not be conflated with the active Green-kernel exponent.

## Several changed factors

For products of matrices of compatible finite sizes, write A_s ... A_1 and B_s ... B_1. Inserting and subtracting the intermediate products gives

    B_s ... B_1 - A_s ... A_1
      = sum_(j=1)^s B_s ... B_(j+1) (B_j-A_j) A_(j-1) ... A_1.

To verify the identity, expand the sum. Adjacent mixed products cancel, leaving only the first all-B product and the last all-A product. Entrywise absolute values and the triangle inequality give a propagation bound for every term. Thus if a replacement changes both the kernel trigonometry and source-node rotations, each changed factor must be accounted for; the single-table bound with a fixed f is insufficient by itself.

## Scope and counterexample

Small table error alone gives no universal residual bound. In one dimension take f=1, B=1, W=G, b=0, and T_tilde-T=epsilon>0. Then |delta R|=G epsilon, which is arbitrarily large as G increases. Likewise a fixed residual-error bound is divided by the stencil step. Counting small exponentials without those multipliers does not establish a comparison with a derivative noise floor.

These conditional inequalities depend only on finite-dimensional linear algebra and the norm triangle inequality. They do not establish actual numerical values for the campaign's coefficients, table sums, source or reconstruction norms. They do not certify quadrature or a pressure-Poisson solution. For the campaign's replacement experiment, a direct same-input residual-difference measurement at every registered offset is a separate empirical route; it must retain its rounding convention and cannot be called a uniform bound.

## Dependencies and verification status

The argument uses finite sums, entrywise matrix multiplication, the scalar triangle inequality and the Euclidean norm triangle inequality. It does not depend on a PDE regularity theorem or on an external numerical library. Each formula was checked directly before any proposed formalization. This is an informal proof; no formal source or machine-checked theorem is claimed. Numerical use requires actual bounds for the stated factors, and those remain open.
