# Fixed-geometry factorization of the finite pressure tables

## Exact statement

Let Q, N, E, L and M be positive integers except that L and M may be zero. Fix real arrays b_q, t_q, L_q, H_q, e_j, weights w_q, basis values Phi_qk, and effective degrees ell_l. The indices are 1<=q<=Q, 1<=k<=N, 1<=j<=E, 0<=l<=L and 0<=m<=M. Fix two masks chi_1jq and chi_2jq in {0,1}. All these arrays are independent of the real parameters c>0 and omega. Define

    G_1ljq = (l+2)(L_q-e_j) + e_j + ell_l(L_q-H_q),
    G_2ljq = l(e_j-L_q) + L_q + ell_l(L_q-H_q),
    A_sljq = chi_sjq w_q exp(G_sljq),
    B_q(c) = exp(-2b_q/c),
    theta_mq(c,omega) = m omega t_q/(2c).

The finite cosine and sine pressure tables are

    Qc_lmsjk = (2l+1)^-1 sum_q A_sljq B_q cos(theta_mq) Phi_qk,
    Qs_lmsjk = (2l+1)^-1 sum_q A_sljq B_q sin(theta_mq) Phi_qk.

They are smooth on (0,infinity) x R. With a_q=2b_q/c^2, d_mq=m omega t_q/(2c^2) and v_mq=m t_q/(2c), their derivatives are obtained by replacing the factor B cos(theta) or B sin(theta) in the preceding sums with, respectively,

    d_c(B cos(theta)) = B(a cos(theta) + d sin(theta)),
    d_c(B sin(theta)) = B(a sin(theta) - d cos(theta)),
    d_omega(B cos(theta)) = -B v sin(theta),
    d_omega(B sin(theta)) = B v cos(theta).

In exact arithmetic these tables agree with the unfactored kernels

    chi_sjq w_q exp(G_sljq - p0 b_q),  p0=2(1-c)/c+2,

contracted against the same trigonometric factors and Phi. A finite array A can therefore be computed once at high precision on the fixed geometry, while the parameter-dependent exponential and trigonometric factors are recomputed at each parameter value. This is an algebraic reuse opportunity; no runtime or memory saving is asserted without measurement.

## Proof

The identity p0=2/c follows by expanding 2(1-c)/c+2. The real exponential product identity gives exp(G-2b/c)=exp(G) exp(-2b/c), which proves the table factorization term by term. The arrays have finite sizes and all denominators 2l+1 are positive. The functions exp, sin and cos are smooth, and c is nonzero, so the finite sums are smooth on the stated domain.

Differentiation gives d_c B=2b B/c^2, d_c theta=-m omega t/(2c^2) and d_omega theta=m t/(2c). The four displayed derivative formulas now follow by the product and chain rules. Differentiation commutes with the finite sums, giving the claimed table derivatives. No differentiation under an infinite integral is used.

## Other table factors

On the same fixed geometry, the volume-moment table has summands w_q s_q^2 B_q Phi_qk. Its c derivative multiplies each summand by 2b_q/c^2; its omega derivative is zero. The degree-one source moments use w_q exp(L_q-H_q) B_q, with either no twist, cos(theta_1q) or sin(theta_1q), so the same derivative formulas apply.

For a fixed source-node array u_i, t_i and fixed integer orders m_a, the remaining table factors are

    sfac_i = exp(2u_i/c), beta_i = omega t_i/(2c),
    cosb_ia = cos(m_a beta_i), sinb_ia = sin(m_a beta_i).

Their derivatives are sfac_c=-2u_i sfac_i/c^2, sfac_omega=0, beta_c=-omega t_i/(2c^2), beta_omega=t_i/(2c), followed by the ordinary trigonometric chain rule.

## Relation to the captured production code and limitations

In PressureSolver.build_tables, L_q=log(r_q), H_q=log(sqrt(r_q^2+R0^2)), b_q=log(sqrt(r_q^2+R0^2)/R0), e_j=log(r_j), and t_q=log1p(r_q^2/R0^2). In the implementation these are stored geometry arrays. This statement treats their stored binary64 values as exact inputs; it does not assert their equality to exact logarithms of exact radii.

The statement covers the default parameter-dependent p0 and the ordinary interior/exterior masks with exterior_monopole disabled. The manufactured-source option with independently supplied p0 needs its own derivative convention. The source clamps active log kernels above700; the algebra above applies to its unclamped mathematical kernels and to the implementation only where that clamp is inactive. The source implements inactive masks by exp(-10000), which underflows to zero in binary64. The corresponding finite mathematical masks above are exact zeros. A high-precision implementation should apply those masks explicitly rather than introduce tiny nonzero terms.

A factored implementation must preserve both components of any double-double table and contraction, respect intermediate exponent ranges, and check its agreement with the intended residual function. The real algebra does not certify a floating-point implementation, quadrature accuracy, the pressure-Poisson equation, or the accuracy of an Euler profile. The accompanying small synthetic-geometry controls compare finite tables and analytic parameter derivatives with the captured automatic-differentiation source only.
