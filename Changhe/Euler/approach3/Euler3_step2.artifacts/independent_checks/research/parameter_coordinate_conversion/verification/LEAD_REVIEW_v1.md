# Lead review of the parameter-coordinate conversion proof, the native worker branch of the CPU G1 v3 driver and the CPU pressure plan

Written 2026-10-29T03:35:26Z. Reviewed: the verifier's research/parameter_coordinate_conversion/PROOF.md, scripts/verify_complete_jacobian_cpu_v3.py
(lines 295-449, native branch and chain-rule comparison), research/split_complete_jvp/verification/CPU_G1_V3_plan.md,
research/pressure_consistency/verification/CPU_SOURCE_SPECIFIC_plan.md; production source cpu_v1 (worker_d6.py 1f33d5c1b7624220,
problem.py 8dd8fd6d2fbab0ee, param_map.py 8058ef12032fbb62), read from the lead's sha-checked copy.

1. PROOF.md: CORRECT. DPhi = diag(I_n, d_c, d_w) with d_c = 0.1 s (1 - s) > 0 and d_w = exp(z_w) > 0; J_z = J_x DPhi; right
   multiplication by the inverse gives the column formulas. The map matches param_map.py (lo 0.4, hi 0.5, omega = exp(z_w)).
   One condition worth one sentence: F must be the same function in both coordinate systems, including every quantity held fixed
   (closure state or target where frozen, weights, active set, layout). The driver satisfies it: the physical stencils evaluate
   objective_at(tc.expand(x)) and the optimizer stencils objective_at(tc.expand(pm.expand(z))), so F includes the tail expansion
   in both, as the statement says.
2. Native branch: zero-filling the unselected columns of the input J_cw is valid for this worker. complete_jacobian_from_Jcw clones
   J_cw, adds the target correction corr to the closure rows of every column (corr is computed by closure_target_correction from
   to_full and z_opt only, never from J_cw), and adds the pattern columns times the chain factors to the two parameter columns.
   Column k of J_c therefore depends on column k of J_cw only. Suggest recording this column separability as an explicit
   condition tied to the worker hash, since a helper that mixed columns would invalidate the zero fill.
3. parameter_chain_rule in worker_Jc mode: the physical columns are the native ones divided by the chain factors, so multiplying
   back reproduces them up to two roundings. The comparison is a tautology there and should not be cited as evidence; in Jcw mode
   the two sets are computed independently and the comparison is meaningful.
4. Self-validation exclusion (one gap, conservative fix). The worker's parameter-direction finite differences use the physical
   steps h = 1e-4 for c_l and 1e-4 max(1, omega) for omega (closure_target_correction with param_five_point, and
   closure_pattern_param_columns, five-point). The driver excludes the matching physical step. In optimizer coordinates at
   omega near 1 (S01), the h0 = 1e-4 step in z_w moves omega by omega (e^h - 1) = 1.00005e-4, within 5e-5 relative of the
   worker's step, so that stencil nearly reproduces the worker's own difference for the pattern and target components. Suggest
   also excluding (as not valid for the pass) any optimizer-coordinate step whose physical displacement is within 1 per cent of
   the worker's step, keeping it in the record. For c_l (d_c about 0.025, physical steps 2.5e-5 to 2.5e-9) and for S09
   (omega 0.3, physical step about 3e-5) nothing coincides. The ladder still has four other steps.
5. Round-trip limit 1e-14: with c_l in (0.402, 0.498), c_l - 0.4 and 0.5 - c_l are exact in binary64 (Sterbenz), and the log,
   exp and sigmoid add errors of a few units in the last place; omega = exp(log omega) has relative error about
   |log omega| 2^-53 (below 1e-15 for omega in [1e-3, 1e3]). In range the check cannot be close to its limit; it is a sanity check.
6. CPU pressure plan: agreed. G4 (d) asks for S01_own, the V027 field and one manufactured field of 3.1; adding
   manufactured_geometric_all at (0.45, 1) covers the other symmetry class and removes any doubt about whether V027 counts as the
   manufactured field. Two requests for the record: (i) for G6, state for each quantity which configuration-M path supplies the
   production value (double-double primal values or the float64 tangent); the 1e-10 threshold is written for float64 values and
   applies to the tangent; the primal values can be reported against the same threshold. (ii) For G4 (d), report Delta both
   against the production base values in configuration M and, as a diagnostic, in float64, since production uses the former.
