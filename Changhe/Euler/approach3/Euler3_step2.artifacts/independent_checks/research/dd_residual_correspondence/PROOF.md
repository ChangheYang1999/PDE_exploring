# Conditional correspondence of the finite momentum residual

Written 2026-10-29 before the source-extracted assembly fixtures. Status: proved algebraic correspondence under the hypotheses below. The associated source review and finite comparisons are numerical checks, not a uniform arithmetic theorem or an Euler existence result.

## Exact statement and hypotheses

Let c be a nonzero real number, omega real, R0 and R1 positive, rho=|y|^2, s=(rho+R0^2)^(1/2), alpha=(1-c)/c, and beta=omega log(1+rho/R0^2)/(2c). Let the angular basis consist of finitely many real homogeneous harmonic polynomials H_q of positive integral degrees ell_q, in cosine/sine pairs with azimuthal frequencies m_q. Let every radial coefficient polynomial be finite, and let the core damping exponent be a nonnegative integer. The channels are A and B for the toroidal potential T, and C, D and E for the poloidal potential S. Their envelope powers are respectively alpha+ell, 2alpha+1+ell, alpha+ell-1, 2alpha+ell, and 2ell+1. The B, D and E polynomials include (rho/(rho+R1^2))^core_damp. All channels except E use the same twist by beta. The E coefficients at degrees below two are zero. Tail constraints have viscosity parameter zero and nonsingular eliminated-coefficient matrices.

Define U=curl(Ty)+curl curl(Sy), G_mi=partial_m U_i and f=sum_mi G_mi G_im. All fields are smooth on R^3 under these assumptions. Fix a finite angular analysis/synthesis rule, radial interpolation rule and radial Green quadrature. Use the same fixed geometry in every expression below. For each angular pressure degree ell, split its Green sum into the below-radius and above-radius contributions t1_ell and t2_ell, including the factor 1/(2ell+1). Define P_ell=t1_ell+t2_ell and d_ell=(-(ell+1)t1_ell+ell t2_ell)/r at strictly positive evaluation radii. These are definitions of the finite pressure evaluation, not an assertion that its derivative or Laplacian equals the derivative or Laplacian of an exact full-space integral.

Let A U=(1-c)U+c(y dot grad)U-omega[(Jy dot grad)U-JU], J(y1,y2,y3)=(-y2,y1,0). On a fixed finite grid, with nonnegative fixed node and angular weights and nonnegative balance weights, the momentum rows are the component-major flattening of

    sqrt(w_node w_ang) (1+rho/R0^2)^(alpha/2) sqrt(w_balance)
        * [A U + G U + grad P_finite].

When balance weighting is disabled the last square-root factor is one. Closure and gauge rows are appended in that order. There are no additional vorticity, separate far-model, viscous or radial-penalty rows. The gauge uses the main grid, with sigmaZ absent. For a J_f reference the balance weights and closure target are held at the registered base point; for J_cw the weights are recomputed at the current point and the closure target is held; for J_c both are recomputed. Parameter-dependent pressure tables in every recomputed quantity use the current parameters.

Under exact evaluation of these scalar formulas, contraction, twist, potential assembly, source formation, finite Green sums, residual assembly and the three held/recomputed conventions give the same finite residual map. This statement does not assert equality between two different floating-point executions of that map. In particular the campaign copy retains selected production float64 closure, gauge and weight quantities, while using extended arithmetic for the registered ingredients. Its empirical comparison with production is a separate requirement.

## Proof

For S=sum_q g_q(rho)H_q(y), the product rule and homogeneity give

    K=y dot grad S+S=sum_q [(ell_q+1)g_q+2rho g_q']H_q,
    D=Delta S=sum_q [(6+4ell_q)g_q'+4rho g_q'']H_q.

Indeed grad rho=2y, Delta rho=6, Delta H_q=0 and y dot grad H_q=ell_q H_q. Expanding curl curl(Sy)=grad div(Sy)-Delta(Sy) gives grad K-yD. Expanding curl(Ty) gives -y cross grad T. Thus

    U_i=-sum_jk eps_ijk y_j partial_k T+partial_i K-y_i D,
    G_mi=-sum_k eps_imk partial_k T
          -sum_jk eps_ijk y_j partial_m partial_k T
          +partial_m partial_i K-delta_mi D-y_i partial_m D.

The source f is tr(GG), so it uses G_mi G_im, not the squared Frobenius norm. Convection in component i is sum_m U_m G_mi. These expansions establish the field, derivative, source and convection correspondence.

For each radial channel the nth derivative of a product is the sum of binomial(n,k) times its kth and (n-k)th derivatives. Applying this to the polynomial, envelope, damping and sine/cosine twist establishes the radial-table and twist correspondence. A power-series jet stores the nth derivative divided by n!, so converting to derivative arrays multiplies its nth entry by n!. E is added after twisting. Its omitted degree-zero and degree-one table rows multiply zero coefficients under the hypothesis.

The stable linear identity, proved in ../stable_linear_operator/PROOF.md, applies the scalar operators b+c y dot grad-omega partial_phi to the potentials, with b=1-c for T and b=1-2c for S. For a twisted envelope of power nu and radial polynomial P(rho), the transformed polynomial is

    [delta+c nu R0^2/(rho+R0^2)]P+2c rho P'
        -i m omega R0^2/(rho+R0^2) P,
    delta=b+c ell-c nu.

The cosine/sine partner signs are the real form of the final complex term. In the A, C, B and D channels delta is respectively 0, 0, -1 and -1. In E, delta=1-c(ell+3); E is untwisted so its rotational partner term is -i m omega P without the radial factor. Applying the same velocity assembly to the transformed potentials therefore gives A U.

For the finite pressure operation, analyze f in the fixed angular basis, untwist with the partner signs, multiply by the fixed radial harmonic factor and parameter-dependent source factor, then contract the below and above Green tables. Linearity gives P_ell=t1_ell+t2_ell. The designated radial derivative is d_ell. Since a homogeneous harmonic has gradient r^(ell-1) times its angular-gradient table, angular synthesis of the gradient gives

    grad_i P_finite = sum_q (P_q/r) A1_iq
                    + n_i sum_q [d_q-ell_q P_q/r] A0_q.

This proves correspondence of every pressure operation, including the radial coefficients and the sign convention -Delta P=f of the continuous Green formula that motivates the discretization. It does not prove that quadrature and interpolation preserve that differential equation exactly.

The tail elimination solves the same four real linear equations for each nonzero-m pair and two for each zero-m column: k^2 moments vanish and the fourth-order moments equal the envelope and twist combinations. Nonsingularity implies uniqueness, so solving the same systems gives the same eliminated coefficients in exact arithmetic. E is unchanged. Finally, multiplying the three momentum components by the stated weights and appending the same closure and gauge rows proves the claimed residual correspondence for each specified reference convention.

## Why the degree restriction is necessary

The degree-one E basis is present in the stored coefficient layout even though production masks it in radial evaluation. Take the unnormalized degree-one harmonic H(y)=y3, zero other channels, and S=f(rho)y3 with f smooth. The preceding formulas give

    U=(2f+2rho f')e3-2f' y3 y.

At y=(0,0,r), r>0, this has U3=2f(r^2). For an E k=0 coefficient with the prescribed positive envelope and positive damping at r>0, this is nonzero. Masking that coefficient produces zero. Therefore a copy that omits the mask is not equivalent for arbitrary stored coefficients. In the two named campaign checkpoints all four E coefficients of their only degree-one mode (1,0,0) are exactly zero. Tail reduction leaves them unchanged, parameter-only stencils leave them unchanged, and phase alignment acts trivially on m=0. The restriction therefore holds for those stencils once these recorded facts have been checked.

## Arithmetic and scope

The copy's table contractions omit low-word times low-word products and round cross terms in float64. Some other helpers include such terms only inside a rounded sum. The table jets use 34-digit mpmath, selected fixed geometric quantities remain binary64 inputs, and the tail k4 constant is computed in extended arithmetic. These facts prevent an exact-arithmetic statement about the executed pairs. The same-function checks, named stencil reproductions and elementary replacement experiments must be reported with their individual finite scopes. No theorem here bounds omitted products, transcendental errors, quadrature errors, interpolation errors, cancellation, or pressure amplification uniformly.

Dependencies: elementary product rules, homogeneity and harmonicity, uniqueness of nonsingular finite linear systems, and the standalone stable-linear identity cited above. No formal proof was built. Source hashes, exact saved-state checks, finite fixtures and the source mapping are in verification/.
