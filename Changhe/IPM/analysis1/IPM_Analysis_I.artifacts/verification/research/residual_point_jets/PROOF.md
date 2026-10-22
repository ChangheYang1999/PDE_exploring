# Residual derivative enclosures at thirteen fixed log radii

## Statement and dependencies

This result extends the finite-point calculation of topic 28 to log-radial derivatives through order five. It does not bound derivatives on whole cells or on an annulus. The exact points and interval input boxes are the thirteen records in research/residual_samples/evidence/sample_result.json, digest 0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c. That result supplies canonical density moments and degree-seven density polynomials at each point. The validity of these input boxes is inherited from topic 28; no new canonical integration is performed here. The input and its independent audit, all their recorded dependencies and the current exact trial parameters must pass digest checks.

Fix a point t = t_c strictly inside one original spline span. Write r = exp(t), w_j = 2j + 1, m_n = 2n, and

    rho = exp(3t) sum_{j=0}^{260} H_j(t) sin(w_j theta).

Each H_j is a polynomial of degree at most seven near t_c. H_261 = 0 is padding. Superscripts in parentheses below denote derivatives with respect to t. Let I_n and J_n be the canonical density moments at the point, satisfying locally

    I_n' = -(m_n + 4) I_n + H_{n-1},
    J_n' =  (m_n - 4) J_n - H_n.

The defining Green identities give

    A_n = exp(4t) [(H_{n-1} + H_n)/2 - m_n I_n],
    B_n = exp(4t) [m_n J_n - (H_{n-1} + H_n)/2],
    A_n' = -m_n A_n + g_n,   B_n' = m_n B_n - g_n,

where

    g_n = exp(4t) [(D + 3 - w_{n-1}) H_{n-1}
                         + (D + 3 + w_n) H_n]/2.

Here D means ordinary differentiation. The two representations agree by substituting the I and J equations and w_{n-1} = m_n - 1, w_n = m_n + 1. The last term vanishes when n = 261.

Let c = 1/k for the exact trial k and define epsilon = (cX + U).grad rho - rho, with U = (-psi_y, psi_x) and psi_n = (A_n+B_n)/(2m_n). At each specified point, the goal is to enclose every odd Fourier coefficient of D^i epsilon, 0 <= i <= 5, by two independent formulas. There are 522 possible odd modes, indexed 0 through 521. Index 521 is the highest possible nonzero mode and must be retained.

The finite computed conclusions consist of coefficient intervals and the weighted Wiener sums

    V_ij(t_c) = sum_{N=0}^{521} (2N+1)^j |D^i epsilon_N(t_c)|,
       0 <= i, 0 <= j, i+j <= 5.

A comparison with a saved producer W_i_j at the same cell identifier is a diagnostic only. Such a comparison supplies no derivative supremum, no bound for another radius and no source-execution provenance. Neither a Wiener lower bound nor a coefficient lower bound is automatically a pointwise residual lower bound at a given angle.

## First derivation: physical Green jets and trigonometric products

For any polynomial H, direct differentiation gives

    D^a[exp(beta t) H] = exp(beta t)
                  sum_{b=0}^a binom(a,b) beta^(a-b) H^(b).

Evaluate density derivatives R_j^(a) for 0 <= a <= 6 by this formula. Build A_n and B_n at order zero from the moments. Their ODEs then determine all derivatives through order five from independently evaluated derivatives of g_n. This is differentiation of exact functions, not of a uniform Taylor remainder.

Define half-amplitudes P_n = -exp(-2t)(A_n+B_n)/4 and Q_n = exp(-2t)(B_n-A_n)/4. Leibniz gives every derivative of P_n and Q_n through order five. As in topic 123, the exact coefficient at derivative order i is

    c R_N^(i+1) - R_N^(i)
    + sum_{n,j,l} binom(i,l) [
       P_n^(l) R_j^(i+1-l) (sine sum + sine difference)
       + Q_n^(l) w_j R_j^(i-l) (sine sum - sine difference)].

In this display the sum frequency is w_j + m_n and the difference frequency is w_j - m_n. Negative sine frequencies are replaced by their positive opposites with a minus sign. The sum index is at most 521 and every difference frequency is nonzero. The ordinary product rule proves this formula for all six derivative orders because the point lies within a polynomial span and all functions there are smooth. The formulas in topic 123 through order four extend without a change of constants or signs.

## Second derivation: density-moment jets and Laurent multiplication

Differentiate the I and J equations directly at the point, using exact polynomial jets H_j^(a). Define full velocity amplitudes

    p_n = -(m_n/2) exp(2t) (J_n-I_n),
    q_n = exp(2t) [m_n(J_n+I_n)-H_{n-1}-H_n]/2.

They satisfy U_r/r = sum p_n cos(m_n theta) and U_theta/r = sum q_n sin(m_n theta). Thus

    epsilon = c rho_t - rho + (U_r/r) rho_t + (U_theta/r) rho_theta.

Leibniz gives derivative i of each product as the sum of binomially weighted pairs of jets. Construct the angular products as Laurent polynomials, using cos(a theta) = (z^a+z^-a)/2 and sin(a theta) = (z^a-z^-a)/(2i). A real antisymmetric encoding stores 2i times each sine polynomial; multiplying it by a cosine polynomial produces the corresponding encoded sine product. Recover the positive-frequency sine amplitudes with the same factor. This construction avoids the first method's difference-frequency scatter.

All interval coefficients are rounded outward to a fixed dyadic grid before multiplication. If an encoded polynomial has integer midpoint array m and nonnegative radius array r, exact integer convolution bounds a product with midpoint m_1*m_2 and radius

    |m_1|*r_2 + r_1*|m_2| + r_1*r_2.

This follows by expanding (m_1+e_1)(m_2+e_2), with |e_a| <= r_a, coefficient by coefficient. Arrays must include both signs of every angular frequency and sufficient zero padding; no cyclic convolution is used. The product is exact as an integer-polynomial operation. Dividing by the two quantization denominators gives rigorous real intervals. Summing all Leibniz terms and the linear term gives the second enclosure.

## Finite checks and interpretation

Use Arb for the physical Green recurrence and direct sine scatter, and mpmath.iv for the density-moment recurrence, with exact integer angular convolution. Check all input box decodings, all output coefficients, every derivative order and all thirteen point identifiers. The order-zero coefficients must overlap the accepted topic-28 result. Both methods must retain the full interval inputs, including the common normalization correction. Interval dependence may widen boxes, but cannot invalidate an enclosure.

For each coefficient, overlapping valid enclosures may be intersected. Summing absolute-value intervals with the positive integer angular weights bounds V_ij. Comparisons with the producer's binary64 saved W_i_j use exact rational decoding. Missing higher-order producer fields are reported as unavailable. Any comparison failure is reported with its exact point and derivative order and does not by itself refute a cell claim without a separate identification of its true cell geometry.

The result proves no derivative Taylor remainder, cell covering, global derivative norm, Sobolev forcing norm, inverse bound, nonlinear estimate or IPM endpoint. This restriction remains even if every finite comparison passes.
