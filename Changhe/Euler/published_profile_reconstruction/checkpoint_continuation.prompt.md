# Continue reconstruction from job 6878470

Continue the numerical reconstruction of the published AGD Euler profile from
the existing checkpoints of SLURM job 6878470. Do not restart the search.

Find a nontrivial full-plane solution that simultaneously matches the published
profile and achieves small independently validated PDE residuals. Fix lambda=1/2
and solve C jointly. Do not identify plotting and recentered stability origins.
Preserve Poisson, velocity coupling, symmetry and far-field behavior. Published
amplitudes are observations, not exact boundary conditions.

Examine C_01, C_02 and C_05: image fits, scales, transport residuals and C. Diagnose
branch drift after removing image penalties. Start several independent
continuations from C_01 and C_02 using persistent progressively reduced image
penalties, trust regions and adaptive spatial sampling. Do not abruptly remove
image constraints. Keep C, amplitude and admissible scales trainable. Investigate
C drift without arbitrarily fixing C. Refine radial expressiveness as indicated
by independent diagnostics, allowing distinct U/Omega/Psi radial breadths while
preserving their differential relations.

Compare promising states against earlier compact models on identical independent
validation sets in consistent physical units. Historical benchmark approximately
RU=8.36e-4, ROmega=3.67e-3, sampled maximum=.0734.

Use independent full-plane near-axis/intermediate/far-field samples. Validate
axis profiles, Poisson, transport, amplitude, scales and nontriviality. Track
physics and resemblance; retain Pareto states rather than only training-loss
winners. Use existing Resnick HPC workflow, check active jobs first, preserve all
old checkpoints and snapshots. If resources permit, perform substantive
continuation with up to two hours actual optimization and periodic validation.
Do not stop after the first failed experiments; explore alternatives while
preserving useful states.

Report the best published-branch-matching checkpoint, best PDE-residual
checkpoint, whether any improves both objectives, exact paths, independent
errors and remaining obstacles.
