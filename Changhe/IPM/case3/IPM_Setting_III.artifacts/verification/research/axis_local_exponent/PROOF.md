# Independent local exponents on the two symmetry axes

Result94. Derivation written before its numerical implementation. This is a diagnostic identity, not an existence or regularity theorem.

Let rho=y a(x^2,y^2) be a smooth symmetric saved Q field, with a0=rho_y(0) != 0. Define q=rho/(a0 y) away from y=0, extended to y=0 by rho_y/a0. On either axis parameterize the positive radius by r. Whenever 1-q(r) != 0, its logarithmic exponent is

    s_local(r) = d log|1-q(r)|/d log r = -r q'(r)/(1-q(r)).

For the saved Q chart r=L sqrt(sigma)/[2(1-sigma)]^kappa, write w=1-sigma, t=2sigma-1 and

    q_axis = w sum_j epsilon_j sigma^j B_j(t)/a0,
    epsilon_j = 1 on the x-axis, (-1)^j on the y-axis.

The implicit chart derivative is sigma_dot=2 sigma w/(w+2 kappa sigma), where the dot denotes d/d log r. If F=sum epsilon_j sigma^j B_j(t), then

    F_sigma=sum epsilon_j [j sigma^(j-1) B_j(t)+2sigma^j B'_j(t)],
    q_dot = sigma_dot (-F+w F_sigma)/a0.

The j=0 first term in F_sigma is zero. These formulas follow by differentiating the finite sums and the logarithm of the chart relation. The quotient on the x-axis is the actual limiting value; no division of the zero density by zero is performed.

The independent implementation evaluates Chebyshev polynomials and derivatives with forward recurrences. It compares q_dot against a fourth-order centered derivative of q(exp(t)) in t=log r at two step sizes. The finite-difference evaluation uses Clenshaw recurrence and does not reuse the analytic derivative. The comparison is empirical precision and differentiation evidence. Points with exactly zero 1-q have an undefined exponent and must be marked so.

For a field with nonzero cubic coefficient b or e, the formal Taylor expansion gives q_x=1+(b/a0)r^2+O(r^4), q_y=1+(e/a0)r^2+O(r^4), hence s_local tends to 2 at zero. Finite values on a finite radius table cannot prove a limiting Holder exponent or distinguish a shrinking transition from convergence by themselves. For scale comparisons, ell_core=sqrt(|a0/b|) when b != 0; a further grid may use r/ell_core. Under rho_lambda(X)=lambda rho(X/lambda), s_local,lambda(r)=s_local(r/lambda) and ell_core,lambda=lambda ell_core.

Dependencies: saved Q density definition, the elementary implicit derivative above, and exact input jets. No producer inverse, differentiation matrix, or local-exponent code is imported. The full inverse is not needed for this density-only diagnostic.
