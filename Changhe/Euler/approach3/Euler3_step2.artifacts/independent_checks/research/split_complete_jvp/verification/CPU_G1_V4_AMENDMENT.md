# Native worker step-exclusion amendment

Registered 2026-10-29T03:41:35.955021+00:00, before any CPU native worker v3 or v4 Euler result. This amends the execution plan only by strengthening the exclusion of self-validation steps. Thresholds, finite-difference ladders, coefficients, fields and resolution are unchanged.

Use verify_complete_jacobian_cpu_v4.py and audit_complete_jacobian_cpu_v4.py for the upcoming native worker runs. At each parameter stencil point, divide its actual absolute physical parameter displacement from the worker base by the absolute stencil factor (1 or 2). If any of these four unit displacements differs by at most 1 percent from the worker's own physical step, mark the entire stencil ineligible for a passing pair. Keep all values and the reason. The worker steps are 1e-4 for c_l and 1e-4 max(1,abs(omega)) for omega. Coefficient stencils and J_cw have no such exclusion.

The independent auditor recomputes the exclusion from saved physical coordinates, using its own arithmetic expression. A synthetic tampered-flag case must fail integrity even when its reported assessments were recomputed to agree with the tampered flag. Additional controls cover S01, S09, both coordinate maps, coefficient directions, the unaffected J_cw case and points on both sides of the 1-percent band. Execute scripts/qualify_complete_jacobian_cpu_v4.py before the first native worker run. It remains pending while S01 J_cw v3 occupies CPU35.

Zero-filled unselected input columns are allowed only for the exact reviewed worker and problem hashes in parameter_coordinate_conversion/verification/COLUMN_SEPARABILITY_v1.json. The driver rejects a mismatch. The worker parameter-chain comparison is labelled a conversion consistency check, not independent derivative evidence.

The current S01 J_cw v3 process and its source dependencies remain unchanged. The next sequence is its audit, v4 qualification, S01 worker_Jc v4, S09 J_cw and S09 worker_Jc. CPU35, one busy computation, one thread and no GPU remain mandatory.
