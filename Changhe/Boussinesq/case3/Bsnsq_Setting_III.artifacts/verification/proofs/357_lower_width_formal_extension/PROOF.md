# Lower-width check of the extended formal hierarchy

Prepared 2026-10-22T11:58:49.889959+00:00, before launching the calculation. This is a finite exact comparison, not a B2 candidate or convergence theorem.

## Statement and construction

Use beta=2, C=1, k=-1, B(s)=s-s^2+s^13/260, the normalized factors t=s^10 times a unit, Y=s^6 times a unit, B t'=(8+2B')t, B Y'=(5+B')Y, J'=t/(BY),J(0)=0, theta_1=t/2 and omega_0=Y(1/231-J). Coefficients theta_n,omega_j,v_j are factorial-free in x as in the exact coefficient equations of P324. The Poisson update is v_(j+1)=-(omega_j+v_j''/(2j+1))/(2j+2), v_0=B. At stage n the two compatible constants solve the residue matrix with entries -12/[5(2n+1)],0; -(2n+5)/[385(2n+1)],9/(10n). It is nonsingular for all n>=2. The meromorphic-primitive normalization is the same as P321/P324.

Run the verifier-owned source f60b8ed5, version4 despite its historical v5 tags, requesting order12 and width200 with a24-minute wall limit. Compare all shared completed E,F and fixed residue values against the frozen width300 stage11 result in P354. Compare finalized theta_n through the shared stage, omega_j through one less and v_j through the shared stage, below both propagated precision bounds. At least20 coefficient powers must be compared in each range. Verify every recorded stage's direct transport substitutions and deliberate E+1/F+1 residue controls, source and arithmetic hashes, and time/progress metadata. Poisson equalities are update consistency, not an independent elliptic solve.

## Why this criterion is valid

Coefficient comparison reduces each analytic scalar equation Bf'-hf=R to the residue condition for R/(Bz), where z is its normalized homogeneous solution. A zero residue permits a meromorphic primitive with no logarithm; multiplication by z produces an analytic coefficient. The two-stage matrix fixes the otherwise free homogeneous constants. Later stages change higher transverse indices only, so the specified shared ranges are final and comparable. Finite rational equality below valid precision boundaries is equality of those truncated coefficients. The deliberate perturbations check that the recomputed nonlinear forcings respond by the separately known nonzero matrix columns. They do not prove the matrix at all indices; P321 supplies that proof.

Freeze only a coherent completed checkpoint, inspecting its final record, field index sets and final leading coefficients. A timeout or interrupted stage contributes no new completed order. Stable reads and matching indices address the metadata-before-coefficients dump order. Preserve the actual elapsed clocks and any unfinished request. The earlier width300 process was absent by11:58:18Z after its nominal75-minute timeout, with only n11 completed. There is no overlap of heavy jobs.

## Scope and dependencies

The second width still uses shared verifier-owned arithmetic and recurrence, so this is a precision consistency test rather than a second independent PDE implementation. P321 and P326 supply formal compatibility and a common axis disk; neither finite run supplies transverse convergence. Coefficient growth is diagnostic only. No global inverse, attachment to the marked center, far-field profile or full B2 YES/NO follows. General B2 remains OPEN. Writes only in verification. No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake builds, commits/pushes/posts or human contact; one single-thread low-priority CPU job, memory below16GiB.
