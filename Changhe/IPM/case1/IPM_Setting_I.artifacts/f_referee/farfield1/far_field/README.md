# Numerical verification

All computations used Python/NumPy/SciPy, one numerical thread, and a
1900 MiB address-space limit, under `timeout 540`. Source files and supplied
archives were read only. No GPU, JavaScript, server, or RLScience cluster
was used. No fit with rows extending to 9000 L was inspected.

The optional Opus collaboration could not run: the configured model is
`us.anthropic.claude-opus-5-5`, but both existing AWS profiles failed
credential retrieval. No other reviewer model was substituted.

## Reproduction

Run from the workspace root, with `PYTHONDONTWRITEBYTECODE=1`:

1. `audit.py 32768` and `audit.py 65536` extract endpoint values and derivatives,
   invert the angular Poisson operator by Fourier coefficients, and evaluate
   the formal residual coefficients.
2. `approximation.py` performs sampled minimax tests on 4097 quadrant points
   and checks the resulting approximants on 8193 points.
3. `tail_closure.py 1024 24` and `tail_closure.py 2048 32` integrate the
   difference between the formula's true exterior source and the export's
   matched two-power closure beyond 10000 L. Only selected rows of each
   large export array are retained.

## Findings

- The endpoint mismatch is 0.0040831106577 on the original angular mask,
  and its y-axis limit is 0.0040842822010.
- At the masked maximum, Theta1_formula is -42.5464664, not -42.3.
- A plain cosine projection through m=200 has maximum error about
  3.58e-5. Sampled minimax errors are about 2.08e-5 for cosines alone,
  and 1.85e-5 with the fractional basis function. The latter uses a very
  large fractional coefficient and is not a recommended well-conditioned
  parameter update.
- A weighted cosine approximation achieves error about 6.01e-6 on
  1.4 < theta <= pi/2, with approximately 6.00e-5 maximum error elsewhere.
  Thus local and whole-quadrant accuracy must not be conflated.
- Near theta=1.5681, the first three pure-power normalized residual
  coefficients are approximately 0.01582146, -88.78303, and 119002.41.
  The additional r^-2 coefficient is about 782.10237.
- At 9503 L these four retained terms predict about 9.65e-7, versus the
  supplied export's 9.45e-7. This is evidence of substantial ordinary
  higher terms, not a certified remainder estimate.
- Correcting only the exterior velocity closure changes the normalized
  residual by about 1.42e-10, 1.56e-10, 2.10e-10, 4.29e-10, and 7.61e-10
  at the five reported near-axis radii. Doubling the angular grid and
  increasing quadrature order changes these values by less than 5e-17.
- The export uses c_l=5.57536260722867, versus the stored reciprocal
  5.575362610641546. Its leading constant drift offset in R/N_v would
  therefore be about -5.19e-10 if this exported drift were held fixed
  when taking infinity. This is negligible for the reported band but
  matters to an exact asymptotic statement.

These are floating-point experiments, not interval-certified proofs.
The minimax computations do not prove a continuous lower bound.
The closure experiment does not bound the export's interior discretization
error or explain how the density coefficients were selected during fitting.
