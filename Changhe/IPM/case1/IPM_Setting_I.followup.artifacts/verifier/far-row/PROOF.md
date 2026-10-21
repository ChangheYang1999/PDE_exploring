# What a far-row-radius comparison establishes

Date: 2026-10-20. Status: mathematical audit of a numerical comparison, not a spectrum certificate.

## Definitions

The numerics lane supplies two residual systems using the same120 by48 unknown density nodes but different placements of the row representing infinity, r_far=10^10 and10^8. It supplies24 Euclidean-orthonormal parameter directions Q and their finite-difference action matrices D, at separately computed trial states. The source files are ritz_n120m48_S.pt and ritz_n120m48_R8.pt; the corresponding states are dnSB_n120m48.npz and dnR8_n120m48.npz. A change in the location of this residual row is not a change of the outer radius used by the independent full-plane inverse.

For an exact Jacobian J and an orthonormal Q, the singular values of JQ describe the restriction to range Q. In particular min singular value(J)<=min singular value(JQ), by minimizing over a larger unit sphere. This is an upper bound, not equality or a lower bound on the full Jacobian. If D approximates JQ and ||D-JQ||_2<=epsilon, then each corresponding singular value differs by at most epsilon. This follows from the min-max characterization and ||(D-JQ)v||<=epsilon on unit vectors. Without such an error bound, singular values of D are numerical action measurements, not certified spectral bounds.

The two measured24-dimensional subspaces need not be identical. Their principal angles are determined by the singular values of Q_0^T Q_1. This describes overlap of the supplied parameter subspaces, not convergence to the continuum kernel. Even identical subspaces and stable small measured values at two row radii cannot exclude errors shared by both systems, such as angular discretization, orbit integration, trial-state bias or a persistent row error. There is no theorem that two similar measurements prove independence from a numerical parameter.

## Checks

The accompanying independently written code reads only the saved arrays and metadata, recomputes orthogonality, action singular values, overlaps and relative changes with NumPy, and computes state differences from the saved density nodes. It does not import or execute the numerics residual or Jacobian code. Results and byte hashes are in verification/audit.json.

Claims about agreement to three digits must be checked on each quantity. Claims that a difference is within roundoff require a separately justified numerical error bound; observed finite-difference step sensitivity is not itself such a bound. A re-solved residual being stable supports weak sensitivity of that residual at the two tested radii. It does not establish a continuum family, an exact kernel, complete truncation independence or an existence endpoint.

## Independent physical checks and verdict

The changed trial dnR8 is reconstructed independently by cosine transforms and mapped-coordinate inversion. Its transport is checked by the full-plane paired kernel and Cartesian eighth-order differences, as proved in ../inverse/PROOF.md. The omitted radius beyond10^30 is bounded independently with exact rational coefficient bounds from ../exterior-tail/PROOF.md; this is not the orbit far-row radius. Density parities imply U(0)=0 exactly. The first radial row equals one exactly, preserving a(0)=1. Center and logarithmic-velocity obstructions follow from ../center-regularity/PROOF.md and its ball implementation.

The two smallest supplied action singular values change13.7 and42.3percent. Their tiny absolute sizes remain unvalidated as exact derivatives; the claim of three-digit agreement is false as a claim about these measured values, and the assertion that their difference is within roundoff has no error certificate. The remaining first ten are close, but the full24-spaces need not match. The nonlinear orbit residual changes only4.28e-5 relatively between the two solved trials.

Own physical normalized transport residuals at radius10 are0.00359328 and0.00260350, stable to less than6e-13 under2048-to4096 angular refinement. The near-source elliptic ratios E/|rho_x| are1.889e-7 and9.935e-8. The canonical strain identity defect is-2.091e-7, while exact center coefficient intervals exclude smoothness and exact compatible transport. The omitted full-plane velocity is below5.219e-13 for observation radius at most10^5. These computations show failure of the required residual standard for this trial, not exclusion of nearby exact profiles. Full data, byte hashes and reproducible summary code accompany this argument.
