# Lead review of the verifier's pressure-moment argument

Written 2026-10-28T22:17Z. Reviewed file: independent verifier/research/pressure_moments/PROOF.md, sha256
744135c3cff08dfe465102021a5ef98a0d15990100dd6db87a2feb91a9a59c2c (108 lines).

## Verdict

The argument is correct as stated, for exact fields under its hypotheses. I checked each step.

1. Identity f = sum_ij d_i d_j (U_i U_j) for div U = 0, U in C^2: d_j(U_i U_j) = U_j d_j U_i; then
   d_i(U_j d_j U_i) = (d_i U_j)(d_j U_i) + U_j d_j(div U) = tr(DU^2). Correct; A = (U . grad) U and f = div A.
2. Bounds: |tr(M^2)| <= |M|_F^2 (Cauchy-Schwarz on <M^T, M>_F) and |DU U| <= |DU|_F |U|. Correct.
3. Zeroth moment: boundary term 4 pi R^2 C0 C1 (1+R)^(-2 beta - 1) -> 0 for beta > 1/2; f integrable for beta > 1/2.
   First moment: int_BR x_k div A = int_dBR x_k A.n - int_BR A_k, and A_k = d_j(U_k U_j), so the second term is the
   surface integral of U_k (U.n); bounds R^(2 - 2 beta) and R^(2 - 2 beta), both -> 0 for beta > 1; x_k f integrable
   for beta > 1. Correct; dominated convergence gives the limits.
4. Mixed source: d_i d_j (V_i U_j + U_i V_j) = 2 tr(DU DV) using both divergences; A_p = DV U + DU V. Correct.
5. Radial form: Y_00 is constant and r Y_1m spans x_1, x_2, x_3, so M_lm = int_0^inf s^(l+2) f_lm ds = 0 for l = 0, 1.
   The Newton coefficient with 1/(2 l + 1) is the standard expansion of 1/(4 pi |x - y|); substituting M_lm = 0 gives the
   exterior-only form, and its r-derivative has cancelling endpoint terms (checked: +r f(r) and -r f(r)). Correct.

## Hypotheses as they apply to the represented fields

(a) Decay. On 0.4 < c_l < 0.5 the far exponent alpha = (1 - c_l)/c_l lies in (1, 1.5), so a beta in (1, alpha) exists.
    The margin vanishes as c_l -> 0.5 (alpha = 1.041 at c_l = 0.49): the first-moment boundary terms decay like
    R^(2 - 2 beta), and the exterior integral int_r^inf s^3 f_1m ds converges like r^(2 - 2 alpha). Any numerical use
    of the exterior-only l = 1 formula therefore depends on the analytic tail beyond the outermost node, which must be
    the same tail model the production exterior integrals already use.
(b) Logarithms. The twisted angle phi - (omega/c_l) log r and the parameter derivatives (d alpha / d c_l) log r, and
    log r factors of the correction channels, are absorbed by beta < alpha, as the file states. Correct.
(c) Regularity. The divergence theorem step needs U in C^2, or U in C^1 with div U = 0, using the identity in the
    distributional sense. The represented field must be checked to have no lower-regularity matching surface between
    the inner basis, the tail expansion and the correction channels. If the matching is only C^0 in DU, the identity
    can fail by a surface term. This is a property of the code's representation and is not verified by the proof.
(d) Solenoidality. G5 (b) gives div U to 1e-10 relative at test points. A nonzero div U adds U_j d_j(div U) and
    U_i div U terms whose moments need not vanish; the size of the discrete moment then also measures this.

## What the identity can and cannot be used for

- As a diagnostic it is valuable: the discrete moments M_lm^disc (l = 0, 1) of the production source and of the
  derivative source, relative to int s^(l+2) |f_lm| ds, measure quadrature, angular truncation and solenoidality
  error. If M^disc does not decrease under radial and angular quadrature refinement at fixed coefficients, one of the
  hypotheses (c), (d) or the tail model fails for the represented field, which is itself a finding.
- At the discrete level the exterior-only formula is the production formula minus M_lm^disc r^(-l-1) Y_lm / (2 l + 1),
  which is a harmonic function fixed by the discrete moments. The task forbids an independent harmonic pressure
  correction. The change is admissible as a pressure evaluation for this campaign only if it is shown to remove
  discretization error: M^disc decreases toward zero under quadrature refinement, the two formulas agree in the
  resolved range to the G4 (c) tolerance, and the O1 change on saved states is reported. Without that evidence it is
  a harmonic correction and is not allowed in production.
- Expected effect: at the far radii the computed l = 0, 1 pressure is a cancellation down to the true size of order
  r^(-2 alpha), while M^disc / r and M^disc / r^2 decay more slowly; the rounding part of M^disc is amplified by about
  r^(2 alpha - 1). With alpha near 1.22 and r up to 65536 R0 = 2e4 this is of the order 1e5 to 1e6, which matches
  the size of the unexplained far-row noise in V043 (implied evaluation noise of the order 1e-11 to 1e-10 of the block
  residual, against a float64 unit of 1e-16).
  This is a hypothesis to test, not a finding: the far-row stencil noise should be split into its pressure-gradient
  term and the rest before any change is made.
