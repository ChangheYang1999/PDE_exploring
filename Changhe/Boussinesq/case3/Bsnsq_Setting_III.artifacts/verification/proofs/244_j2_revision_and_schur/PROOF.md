# Revised J2 diagnostics: exact finite-matrix implications and limits

## Statement and notation

This is an audit of the revised NUM_REPORT section7m(ii)(g), not a theorem about a Boussinesq solution. Let T be the fitted forced map, x its stored coefficient vector, J the supplied sampled difference matrix, f=T(x)-x the supplied defect, and A=I-J. Let q be the strain row, T_p the supplied parameter column, and m the stored scalar mismatch. Denote by m_p^partial the explicit parameter derivative at fixed x. The finite-array reduced derivative is

    v_p=A^(-1)T_p,  m_p=q v_p+m_p^partial.

Every conclusion here is conditional on the supplied arrays as arrays. No independent regeneration of T or of its difference columns is claimed. In particular, the twelve stored step-comparison norms permit checking their range, not their underlying derivative errors.

## Exact linear-algebra assertions

If A is invertible, the augmented matrix B_p with upper block [A,-T_p] and lower row [q,m_p^partial] sends (v_p,1) to (0,m_p). By the variational characterization of its smallest singular value,

    sigma_min(B_p) <= |m_p| / sqrt(1+||v_p||^2).

This is an upper bound. A small singular value is thus compatible with order-one m_p when the state response ||v_p|| is large. It is not a certificate of a fold. The right-hand side follows directly by evaluating one unit vector; no numerical spectral theorem beyond this variational identity is needed.

The linearized simultaneous correction at fixed lambda solves

    A dx = f+T_beta d_beta,
    m+q dx+m_beta^partial d_beta=0.

Substitution gives d_beta=-(m+q A^(-1)f)/m_beta when m_beta is nonzero. This corrects both the inner defect and the scalar mismatch. It is a displacement of the linearized finite system. A nearby nonlinear root requires additional existence and error control.

For a normalized right singular vector v, the squared coefficient mass assigned to a set of coefficient indices E is sum_(i in E)|v_i|^2. Grouping the same coefficients by Fourier mode or radial-spline index is an exact partition of the coefficient norm. The grouping does not describe the support or physical L2 norm of the represented function: spline supports overlap and evaluation multiplies the coefficients by nonconstant basis functions and weights. Therefore the reported43.6 percent in three radial indices is solely a coefficient statement.

A finite set of unstable difference quotients does not establish an unstable exact derivative. To see this, choose delta smaller than every positive sampled step and define chi(x)=exp(1-1/(1-(x/delta)^2)) for |x|<delta, extended by0 outside. Then T(x)=2x(1-chi(x)) is smooth, T(0)=0, T'(0)=0, yet (T(h)-T(0))/h=2 for all sampled h with |h|>=delta. By continuity of T', it is locally contractive at0. Thus the distinction made in the revised report between the sampled matrix and the actual nonlinear map is necessary.

## Provenance and checks to perform

Freeze the current report, NUM summaries and the P234 independent matrix audit. Recompute the weak-vector identities and coefficient energies directly from the supplied matrix/vector arrays. Independently calculate all new scalar ratios, parameter cosines, the Schur upper bound and corrected displacement. Compare the twelve logged step ranges with the revised rounding, explicitly retaining their status as logged summaries. The report's residual-grid metric is different from P234's full-plane integral metric. Agreement with the supplied residual-grid summary is a report-consistency check only.

The main B2 problem, exact map derivatives, existence of a smooth zero curve, folds and every physical-space error bound remain OPEN. The two forced states have different fixed sources and amplitudes, so their comparison does not isolate distance to a vertex. This argument neither proves nor disproves any Boussinesq profile.
