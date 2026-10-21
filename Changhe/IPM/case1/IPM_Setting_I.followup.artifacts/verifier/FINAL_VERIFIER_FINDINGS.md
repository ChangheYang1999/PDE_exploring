# Final independent verifier findings

Scientific record through AV156, 2026-10-21T00:36:58Z. This document reports completed checks. It does not anticipate an ending clock observation.

**Neither YES_inf nor NO_inf has been established.** The verified results do not authorize an early scientific endpoint. The scheduled verifier run cap was 2026-10-21T00:46:23Z, measured from T0=2026-10-20T00:46:23Z. The subsequent ending observation was T_end=2026-10-21T00:46:25.319145Z, elapsed 86402.319145 seconds, including cleanup. The later preservation check was bookkeeping, not additional research. These timestamps record elapsed time and do not by themselves verify active research time. The report contains the verification timeline; topic proofs and evidence are indexed in INDEX.md.

## What the numerical checks establish

The verifier independently implemented the represented density, Cartesian differentiation and whole-plane inverse. Candidate NPZ data were read as inputs; no new evaluator imports code from the numerical lane. Manufactured fields, parity, center velocity, harmonic gauge, far-field estimates, center normalization and identity, and separate inverse/differentiation sensitivities are recorded in the indexed studies. Earlier inherited confirmations are identified separately from the verifier's independently reconstructed AV entries.

For the five frozen L=8 states, the common58-point maximum of |R|/N_f is:

|N,M|Maximum normalized residual|RMS normalized residual|
|---|---:|---:|
|72,30|0.00590303704436|0.00142155859168|
|84,35|0.00678329917656|0.00141471184190|
|96,40|0.00548170121831|0.00129301162919|
|108,44|0.00252613493977|0.00081656410675|
|120,48|0.00262698041560|0.00064885122054|

Here R=(c_l X+U) dot grad(rho)-rho and N_f=|rho|+sum_i |(c_l X_i+U_i)partial_i rho|. These are sample values, not rigorous continuum residual bounds. The sample maxima increase72to84 and108to120, including with a fixed120 denominator; the RMS decreases at all four steps. Neither behavior determines convergence. The radial quadratures differ and their interior error is not certified. See five-grid-comparison/PROOF.md and RESULTS.md, AV153. All290 residual rows have exact rational component reconstructions, with1450additional Decimal arithmetic checks on the same inputs.

The L=4,8,16 N=96 trials have common-sample maxima0.00382566619,0.00548170122,0.00892470775. Two independent fixed-c_l corrections improve the fit sample, but maxima on84 withheld points remain0.00168358217 and0.00114210545. These computations do not meet the requested transport standard about1e-6. They concern the specified follow-up trial fields; they do not retract the published evidence for the distinct weaker P_2 problem.

The final108field audit is complete and manually accepted (AV150). Its eight additional-point maximum is0.00282504496. Near the numerically located root in[8,9], the normalized elliptic defects are about6.38e-8 and2.14e-8 at offsets y=0.1 and1.0. The whole-plane identity defect3c_l-1-psi_xy(0) is rigorously nonzero, about-6.2641713e-7, by two overlapping interval calculations. Exact center coefficients exclude C^5 for that fixed interpolant and exclude its exact transport equation. These are fixed-field results. They do not exclude a smooth limiting profile or supply reliable B_3,B_5,B_7 measurements for a coupled solution. See fifth-grid/RESULTS.md.

The domain/resolution physical linearizations, inverse refinements, second point samples and mixtures are completed finite-subspace diagnostics. They give no continuum lower bound, kernel dimension, isolation theorem or nonlinear family. Q1 remains open. The late controller stages were subsequently reviewed manually: AV146 for the84 refinement, AV149 for its64point experiment and mixtures, and AV150 for108. A generic automated ending note about unreviewed late outputs does not supersede those dated manual acceptances.

## Analytic conclusions and their limits

The full-class strong question remains open. Conditional exclusions retain their exact extra assumptions. In particular, axis-only sign constructions and local frozen examples cannot replace global coupling and canonical velocity. The center homogeneous coefficient is ell_3+B_3; identifying it with B_3 requires a source condition forcing ell_3=0. Source regularity inferences from B_3 also need the stated center condition. Resonant higher orders retain their separate qualifications.

Lead FINAL_REPORT.md and SPEC5.50 were independently audited in AV148; their accepted MD5 values are a0bf2065c168cff51048c4749f883430 and4d34bd2a3909016f8a68bc10649d3186. Their report cutoff00:00:37Z is not the ending of this verifier run. Later finite diagnostics and packet results do not change their endpoint conclusion.

The new compact-packet result (AV151) proves scalar trace rigidity only for its specified compact annular frequency class. The explicit noncompact example in topics85to87 tests that hypothesis sharply:

- Nonzero real odd Schwartz data have every relevant scalar weighted moment zero and a smooth nonzero first trace (AV152).
- The two-dimensional packet is nevertheless not C1 on any neighborhood of its frozen-source origin (AV154).
- Every ordinary transverse slice derivative G_j(s)=partial_y^jV(s,0) exists and is a smooth function on R, while joint C1regularity still fails (AV156).

All statements have standalone proofs written before their checks, completed actual Claude Opus5.5 reviews, independent reconstruction and pinned evidence. They concern explicit frozen packets, not the physical normalized center, an arbitrary coupled kernel or an admissible IPM profile. Smooth axis trace functions alone cannot establish joint regularity.

## Reports, collaboration and evidence

The numerics report's incorrect fifth-grid median1.5e-4 was corrected to1.3e-4. AV155 independently checked the repaired bytes, MD5bc3b9ab5db46b174ddfbd8b1d396b507, and their common-grid comparison. Earlier REFUTED entries remain the history of a repaired error.

The independent verifier took over at2026-10-20T13:06:38Z. The initial lane checks were by Claude Opus5.5 and are labeled inherited. New second-model reviews used the permitted Python Bedrock client, with actual response model claude-opus-5-5 recorded. Truncated reviews were not treated as completed approvals; disagreements were followed up and reviewer errors were corrected. The numerical teammate's Fable5.1 model is not silently labeled Opus5.5.

No JavaScript/TypeScript tooling, servers, RLScience cluster use, Lean/Lake builds, external writes, commits, pushes or public messages were used for these checks. All writes remain in this verifier lane. Individual code/evidence pins identify what was actually checked. The accompanying artifacts contain the selected code and evidence. Historical hashes identify the original reviewed files; they do not certify mathematical truth. The observed ending is recorded only after the actual cap or a recorded controller error, with the distinction explicit.
