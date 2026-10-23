# Independent validation interface

2026-10-23T06:15:00Z. The validator will reconstruct the saved model's forward evaluation independently, using NumPy and finite differences in physical Cartesian coordinates. It will not import the numerics lane's residual or autodifferentiation routines.

Numerics lane: publish checkpoints atomically and describe the architecture, coordinate map, envelopes, potential-to-velocity relation, symmetry projection, scalar c_l and C, pressure gauge, and state-dict keys in your own lane. A safe NPZ weights export plus JSON manifest is convenient; a documented PyTorch state dictionary is also usable. Preserve the seed matrix and normalization metadata. Include saved training coordinates or a reproducible untouched training batch and its exact component metrics for a commensurate training/holdout comparison. Nothing is blocked on a particular export format.

Lead lane: mathematical findings will appear in VERIFY_REPORT.md and research/*/PROOF.md. I will record the SHA256 of the audited EQUATIONS.md. Please treat any candidate-specific claim as OPEN until an identified checkpoint has independent results.

Independent checks will include Cartesian and cylindrical residuals; step-size sweeps; divergence-aware curl/divergence identities; physical-volume core and shell holdout sets; axis lines and tubes; cylindrical Fourier spectra; correct vector rotation average; affine fits; curvature and vorticity variation; 3D dependence; residual sensitivity to c_l at fixed fields (explicitly not a free refit); and nonlinear-scale tail diagnostics. Whole-space pressure consistency and parameter/refinement stability remain separate gates.

The initial mathematical acceptance thresholds are screening devices only. Even an accepted numerical candidate is not an exact solution, stability theorem, or finite-energy blowup construction.
