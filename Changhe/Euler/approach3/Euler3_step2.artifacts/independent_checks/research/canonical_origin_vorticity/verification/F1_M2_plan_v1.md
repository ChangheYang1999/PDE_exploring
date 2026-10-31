# Exact origin check at F1 medium segment 2

Registered 2026-10-30T01:25:43.057016+00:00 before origin evaluation. Use iteration 386 of f1_S05_m2_L6_cl0.4500_om0.3000_free, the raw full vector bound in V560. Copy the small checkpoint immutably and decode its exact coefficient layout with the previously qualified importer. No normalization, phase rotation, refit or tail-map reapplication is made.

Apply verify_origin_group_v1.py unchanged: exact rational origin/Taylor calculation, outward intervals and signed axial residual/vorticity ratio, with the independent extended Cartesian comparison tolerance 2e-12 and floor 1e-30. Mathematical scope and notation are the parent PROOF.md, general_modes/PROOF.md and signed_ratio/PROOF.md. The result applies only to this exact represented field and does not exclude a neighborhood of coefficients or parameters.

Bind all scripts and input hashes before evaluation. Run serially on CPU 35 with one thread and CUDA_VISIBLE_DEVICES empty inside the bounded recursive pause. Limits: importer 30 s, origin driver 115 s, complete pause 180 s. No JavaScript/TypeScript, servers, RLScience/cluster, remote compute, outside writes, or Lean/Lake builds.
