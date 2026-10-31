# Verification plan, before holdout implementation

1. Read immutable full coefficients and actual saved free parameters. Do not
   reproject, renormalize or refit a saved state.
2. Locate a sampled enstrophy core radius on a broad logarithmic grid; record
   the window and flag an endpoint maximum. This is a sampled location, not
   a certified continuous maximizer.
3. Use fresh azimuthal phases and volume-coordinate radial nodes on both
   absolute dyadic shell families. Add |y|<1, the small origin ball, and thin
   far shells separately. Report all domains and reference radii.
4. Reconstruct U and DU with independent radial jets and 70-digit angular
   features. Evaluate the linear momentum term with the independently
   derived stable formula. Check it against the separate 70-digit evaluator.
5. Recompute the pressure from tr((DU)^2), using full-space radial Green
   quadrature, exact integration of the represented leading tail, and no
   imposed zero source moments. Every shell radius is a source-panel edge.
6. Keep all point sets fixed during pressure refinement; retain per-shell
   pressure-gradient differences and resulting changes of the residual
   norms. These differences are not certified error bounds.
7. Preserve five-term denominators, nonlinear and linear group ratios,
   single-term ratios, Gram data, weighted absolute residuals, divergence,
   and denominator flags. A partial momentum check is never a full Tier gate.
8. Before final-state claims, add centered-core balls, vorticity and origin
   checks, source/Poisson consistency, and the registered extended-precision
   far checkpoints. Any incomplete item remains OPEN.
