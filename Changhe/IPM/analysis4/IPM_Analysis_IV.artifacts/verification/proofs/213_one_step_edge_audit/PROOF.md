# Finite one-step edge truncation of the logarithmic recurrence

Status: finite arithmetic CONFIRMED inV449, conditional on the reset input. The complete one-step equation and all seven rounded truncation errors pass.

## Statement and hypotheses

Fix delta=2/3, c=3 and the canonical polynomial-log branch with leading density sin(theta). Write t=log(r), p_j=1-2j/3, P_i=2-2i/3, D=partial_t and lambda_n=2(n-1). Let F_j and G_i be the stored density and stream polynomials. For an integer L>=1, define

    F_n^[L] = (lambda_n-3D)^(-1)
        sum_(i+j=n, min(i,j)<=L)
        [(P_i+D)G_i partial_theta F_j
         - partial_theta G_i (p_j+D)F_j].

The norm is the sum of the absolute values of all positive sine-mode coefficients and all powers of t. The reported one-step relative error is

    epsilon_n(L) = ||F_n-F_n^[L]|| / ||F_n||.

This quantity compares one recomputed coefficient with the given lower coefficients. It is not the error of a separately evolved edge-truncated recurrence and does not bound accumulated error at later orders. All comparisons involving the continuation after329 are conditional on the reset input; they do not recover the discarded earlier interval uncertainty.

## Independent convolution and linear inverse

Represent a sine polynomial by its signed real Laurent coefficients: a sin(m theta) is mapped to a(z^m-z^(-m))/2. If E=z partial_z, the signed Laurent transform of the angular forcing is

    (P_i+D)G_i E F_j - E G_i (p_j+D)F_j.

This identity follows by multiplying the sine and cosine exponentials, or by the independently checked Cartesian derivatives in97. Both ordered pairs i,j and j,i are retained when distinct. No factor two is inserted at the central pair i=j.

At fixed output order n, encode a logarithmic column q and angular frequency m as the polynomial degree q(4n+1)+2i+m for an order-i input. The frequency support is at most2i in absolute value. Products therefore have angular indices0 through4n, and the stride4n+1 prevents carry between logarithmic columns. Ordinary directed polynomial multiplication computes every coefficient of the signed convolution.

For a forcing S=sum_q s_q t^q, solve downward:

    x_q = [s_q+3(q+1)x_(q+1)]/lambda_n.

The terminal coefficient is zero beyond the degree of S. Substitution proves (lambda_n-3D)X=S coefficientwise. Since lambda_n>0, the inverse is unique on polynomials. This evaluation order differs from the producer's finite Neumann sum.

## Verification procedure and scope

The audit uses directed ball arithmetic for all coefficient operations and norm sums. It first checks complete low-order equations against an exact Cartesian reference through12, then accumulates the ordered pairs at n350 by min(i,j), recording the requested truncations. A final complete sum must enclose the stored coefficient in the sense that every residual interval contains zero. The source checkpoint and source program hashes identify the inputs; no large duplicate checkpoint is needed.

The check proves finite arithmetic consistency under the stated input enclosure assumptions. A small epsilon_n(L) at one or several orders gives no all-order convergence result and no bound on a limiting cycle or singularity location.

The reset checkpoint is deliberately not used as an exact low-order reference: its coefficients through329 are rounded midpoint inputs after radii were discarded. They do not enclose the earlier exact recurrence. The initial diagnostic failed this inappropriate low-order check; that failure is retained separately. The finite order350 check uses the saved midpoint prefix as input and retains its conditional scope.

## Completed audit

At 2026-10-31T16:17:00+00:00, the independent full sum contains all349 ordered pairs and every residual coordinate encloses zero. The largest omitted central-pair error is2.5866850265e-7 relative at cutoff174; the full error enclosure at175 is below8.09e-126. The source receipt retains all intermediate cutoffs and exact dyadic enclosures.
