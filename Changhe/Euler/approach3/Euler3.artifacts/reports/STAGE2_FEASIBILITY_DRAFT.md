# Stage II feasibility and GPU-hour estimates (numerics draft 2026-10-25T03:41Z, prototype readings added 2026-10-25T04:52Z, far-closure note 2026-10-25T10:24Z; for the gate response due 2026-10-25T20:00Z)

Measured costs on one A100 80 GB (this campaign, float64, LM with forward-mode Jacobian, 300 iterations per arm unless stated):
| configuration | unknowns | residual rows | s per LM iteration | GPU memory | GPU-h per 300 iterations |
|---|---|---|---|---|---|
| L2 Nk8 (nest2 start) | about 100 | 24 x 264 x 3 | about 0.3 (75 s per 200-iteration start) | < 2 GB | 0.02 |
| L4 Nk12 (nest4) | about 400 | 36 x 594 x 3 | 0.6 (190 s per 300) | < 4 GB | 0.05 |
| L6 Nk16, channels at degree L | 770-1100 | 48 x 760 x 3 | 1.2-1.8 | 8-13 GB | 0.1-0.15 |
| L6 Nk16, SPEC-degree channels B15/D14/E6 (+ closure rows) | 1467 (reduced) | 51 x 2812 x 3 = 430k | 8-15 (shared GPU) | 23 GB | 0.7-1.2 |
| L8 Nk20, SPEC-degree channels B19/D18/E8 | 2719 | 63 x 4140 x 3 = 782k | 37-58 | 33 GB (75 GB observed with closure rows at chunk 128) | 3.1-4.8 |
| L10 Nk24, channels at degree L (d6u_L10) | about 2400 | 72 x 1104 x 3 | 10.5 | 58-70 GB | 0.9 |
| L10 Nk24, SPEC-degree channels B23/D22 (not run) | about 5000 | about 1.3 M | estimate 120-200 (chunk 64) | estimate 50-70 GB | estimate 10-17 per state |
Free-parameter arms cost 4-6 times more per iteration (rebuilt pressure kernels per step): L6 free 55 s per iteration.
Diagnostics per finished start: two shell families + spheres + Gram + structure 30-130 s (L6-ext), 300 s (L8-ext); G closure 2-40 s; ray functionals 60-140 s.

Arms of reports/stage2_plan_draft.md (lead): rough numerics estimates, 4 GPUs for 42 hours = 168 GPU-h in Stage II (minus the independent route's share).
- S1 resolution ladder (half of numerics GPU time, about 80 GPU-h): per branch L6 (0.7-1.2) + L8 (3-5) + L10-ext (10-17, exclusive, memory to be
  verified) at 300 iterations; V10 stationarity needs 600-900 iterations at L6/L8 (observed: no arm stationary at 300) -> about 25-45 GPU-h
  per branch for three levels; feasible for 2-3 branches (D6 lineage d6w3, nest (0.45, 1), nest (0.42, 0.3)), not for 5.
- S2 Newton-Krylov on d(U) = U + G N(U): PROTOTYPED (2026-10-25T04:52Z; src/optimization/backward_defect.py, scripts/s2s3_prototype.py, reports/s2s3_*.json).
  G in the azimuthal-mode form with an O(h^4) cumulative rule (16 radii per octave, R0 2^-14 to R0 2^16; G[L U] = U to 7e-7 at L2, 4e-6 at L4/L6),
  Galerkin projection onto the tail-constrained basis at the training nodes, bordered square system (dilation and rotation generators, two gauge
  rows). Measured: one d(U) evaluation 0.13 s (L2) / 0.16 s (L4) / 0.20 s (L6, no channels); one JVP 0.25-0.4 s; the dense Jacobian by
  forward-mode AD 0.4 s (50 unknowns, L2) / 3.4 s (242, L4) / (L6: about 770 unknowns, minutes). JVP vs central differences 1e-11 to 1e-9.
  GMRES (restart 50, no preconditioner) to 1e-3: 28 iterations at L2 (cond 2.3e5); NOT reached in 2000 iterations at L4 (cond 1.3e8, sigma_min
  8e-5; a Jacobi preconditioner does not help). The damped Newton step lowers ||P_n d|| by 12 per cent (L2, t = 0.5) and 7 per cent (L4, t = 1/8)
  and worsens the holdout rho_u^max at L4 (0.058 -> 0.063) and L6 (0.055 -> 0.071). Cost is not the issue (a 20-step Newton solve at L6 is about 1-3 GPU-h with the
  dense Jacobian, 5-15 GPU-h at L8); the conditioning is (column-scaled cond 1.3e3 / 1.3e5 / 1.5e7 at L2 / L4 / L6; whether it sits in the basis geometry or in the
  operator I + P_n G N'(U) was OPEN until the field-norm values were read, verifier 05:29Z; in field-norm coordinates J_field = diag(R, I) J_s diag(R, I)^-1
  the condition number is 1.3e3 / 2.5e4 / 3.8e5 at L2 / L4 / L6 (2026-10-25T05:46Z), so the growth belongs to the projected operator): S2 needs a preconditioner (for example the LM normal matrix of the shell-weighted
  residual, or P_n G applied to the linearized L) and a trust region, and even then the step direction may not descend in the SPEC diagnostics.
  Recommendation: keep S2 as a failure-map probe at L4-L6 (sigma_min and GMRES counts per level; about 1 GPU-h per level), not as a refinement
  engine, unless a preconditioned variant converges on the L4 state first.
- S3 stabilized fixed point: PROTOTYPED. Five iterations from the best nest2 L2 state and from the nest4 L4 state (stabilized, eta = 2, and the
  plain normalized control): every variant leaves the basin at the first step (holdout rho_u^max 0.108 -> 0.80 / 0.66 at L2, 0.058 -> 0.40 / 0.24
  at L4), successive-change ratios 0.1 to 25, m(U) changes sign by the third iteration; <U, T(U)>_eta/<U, U>_eta is 0.63 / 0.71 at the start
  (exact profile 1). One iteration costs seconds at L2-L4 (about a minute at L6-ext). Not contracting near any saved state: not usable as a
  Stage II arm from Stage I states; at most a cheap control run (0.1 GPU-h) on any S1 refinement product.
- S4 continuation in (c_l, omega) and the all-m class: 300-iteration L6 arms at 0.1-1.2 GPU-h each; a 10-point path per branch 1-12 GPU-h;
  pseudo-arclength needs the free-parameter Jacobian columns (implemented) at the 4-6x per-iteration cost.
- S5 infinity: E1 (shells with analytic tail integrals) exists (tail constraints, far anchoring, channels, closure rows); E2 (factored
  compactified exterior in x = R_0/r with the correction powers in the basis) needs a new radial basis for the exterior: 1-2 shifts of
  implementation before any run; matching-radius variation (R_0 0.15/0.3/0.6) is cheap (0.1-1 GPU-h per point at L6).
- S7 mean-swirl fraction seeds (f_sw 0.8/0.5/0.2/0, m = 2 eddy seeds) at L6-8: 0.1-5 GPU-h per seed; can start before the gate on a free slot.
Infeasible or costly items: L10 with SPEC-degree channels for more than one or two states (memory near the 80 GB limit, 10-17 GPU-h each);
600-900-iteration stationarity at L8-ext for several branches (5-15 GPU-h each); E2 before Stage II (implementation time).

Far closure in Stage II (SPEC v1.24 7.8; lead 2026-10-25T10:12Z; reports/FAR_COEFFICIENTS.md, 2026-10-25T10:24Z): no export carries the first nonlinear far
correction (energy ratios -434 to +29.7, helicity ratios 0.18 to 4.2; m = ||G_carried - G_required||/||G_required|| 0.22 to 4.3, with 42-67 per cent of
the squared defect along F and the rest an angular-shape error of the same radial order). Closure rows exist (d6w3: m 0.22 at L6, correlation 0.99;
ineffective at L8, FAILURE_ANALYSIS 25). For Stage II S1/S5 the closure rows stay the full vector rows; the worker, re-evaluation and export now
record the F-component int F.(G_carried - G_required) dS and the orthogonal norm beside m (meta_supplement_v124.json for existing exports), so an S1
product can be read on both the energy ratio (bounded by m/c, c = 0.007-0.044 on these states) and the angular shape. Cost: the closure block is
2-45 s per state at L6-ext and about 2 min at L8-ext (CPU); the rows add about 10 per cent to an LM iteration.
