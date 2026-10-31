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
   quadrature, exact integration of the represented main-main leading tail,
   and no imposed zero source moments. On the final interval s=T/t,
   subtract that leading power/log term from the full reconstructed
   source at every quadrature node and integrate the remainder numerically.
   This retains the B/D/E mixed terms and main-channel subleading terms;
   no error enclosure for this remainder quadrature is claimed. Every shell radius is a source-panel edge.
6. Keep all point sets fixed during pressure refinement; retain per-shell
   pressure-gradient differences and resulting changes of the residual
   norms. These differences are not certified error bounds.
7. Preserve five-term denominators, nonlinear and linear group ratios,
   single-term ratios, Gram data, weighted absolute residuals, divergence,
   and denominator flags. A partial momentum check is never a full Tier gate.
8. Before final-state claims, add centered-core balls, vorticity and origin
   checks, source/Poisson consistency, and the registered extended-precision
   far checkpoints. Any incomplete item remains OPEN.

Implementation note added after the 23:48Z review: use the stable equivalent
volume transform `a*cbrt(1+t*expm1(3*log1p((b-a)/a)))` for a>0. The
reviewed original plan is retained as plan_v1_reviewed.md.


Update 2026-10-28T23:56:48.874266+00:00: the pilot also records the six-term split, r_k^alpha and r_k^(2alpha+1) absolute residuals, and the N/L norm ratio. It adds the explicitly registered ball r<r_core/32 alongside the absolute dyadic partition. Dedicated axis sets, y=0 and centered-core balls remain separate pending diagnostics. No full Tier or pairwise-ranking verdict is made by this pilot.
