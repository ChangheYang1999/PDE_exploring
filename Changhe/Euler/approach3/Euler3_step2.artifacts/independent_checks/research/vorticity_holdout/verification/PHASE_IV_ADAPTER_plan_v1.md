# Frozen-cohort vorticity adapter plan

Registered 2026-10-29T22:39:27.948848+00:00, before any final cohort or final sampling draw. This extends the existing Phase IV plan without changing a Tier threshold.

Read ../PROOF.md, ../../vorticity_potentials/PROOF.md and ../../angular_residual_norms/PROOF.md first. No new mathematical claim is introduced.

Reuse the qualified tensor and Cartesian vorticity evaluators and five-term metrics. Generalize the segment-one driver from two hard-coded pair names to an explicit positive reference core radius and an unsigned 64-bit seed. The input and sampled center are read from a completed, same-input primary momentum record. In final execution that record must itself pass the frozen-cohort auditor. The vorticity seed is the separately derived, already frozen seed. The same phase is used within comparisons.

Use full-sphere levels (N_r,N_mu,N_phi)=(4,16,32),(8,32,64), including dyadic and half-offset families, thirteen common physical shells with R0=.3, the reference-core/32 and reference-core/256 balls, the unit ball and the physical partition of the radius-1024 ball. These are finite quadrature rules, not error enclosures. Use both axis caps sin(theta)<.05 with N_mu per hemisphere=N_r and N_phi equal to the full-sphere count, increasing the old cap azimuthal count by a factor of two. For displaced balls at a_eff/2 and a_eff/4 use N_r and half the full-sphere angular counts, as in the qualified route. Their domains depend on the sampled maximum of each state and are labelled accordingly. No continuous maximizer is certified.

The finer full-sphere and axis grids have N_phi=64. The lower rule is intentionally retained as an empirical refinement comparison; neither level is declared sufficient from its size alone. All finite terms, undefined denominators and observed changes are retained. The finite radius-1024 result does not include the exterior.

The adapted scalar auditor verifies source/input identity, the explicit seed and core scale, family endpoints, sample counts including the enlarged caps, all reported ratios, physical-volume combination and observed changes. Exact origin exclusion is supplied by the separate bound general-mode origin audit, not by selecting an old pair-specific exact result. A scalar audit does not reconstruct unsaved bulk field arrays.

Qualify argument refusal and bind sources before final sampling. Re-evaluate one existing development input under the new driver and auditor, with the unchanged main rules, to test the actual I/O path. This development evaluation cannot become a final holdout. The wrapper rejects test cohorts, wrong primary identities and missing source bindings before launching computation. Each final run holds the common side lock and a finite time budget, uses only CPU35 and one thread, and preserves failures.

No JavaScript/TypeScript, servers/listeners, remote or paid compute, RLScience cluster, GPU, Lean/Lake build or write outside this side is used.
