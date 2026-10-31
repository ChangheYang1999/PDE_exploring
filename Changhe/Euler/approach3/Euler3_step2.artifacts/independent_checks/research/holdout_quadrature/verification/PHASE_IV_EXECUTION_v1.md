# Frozen final holdout execution

Status: wrapper and compact result auditor qualified by V377. No final cohort has been selected, no final entropy drawn and no final Euler evaluation run by this qualification.

The registered scientific plan is PHASE_IV_plan_v2.md. Use exact modern checkpoint imports, with B0 and the selected FREE endpoint and, when available, its FIXED control. Record the selection, reasons and actual time before sampling. The selection schema and freeze checks are in scripts/phase_iv_manifest_v2.py. Test-only cohorts are unusable for execution.

From this side, after creating the actual read-only selection JSON:

```sh
bash scripts/python.sh scripts/phase_iv_execution_v1.py binding --output artifacts/phase_iv_source_binding.json
bash scripts/python.sh scripts/phase_iv_manifest_v2.py --selection artifacts/phase_iv_selection.json --binding artifacts/phase_iv_source_binding.json --output artifacts/phase_iv_frozen
bash scripts/python.sh scripts/phase_iv_execution_v1.py inspect --cohort artifacts/phase_iv_frozen
```

Run each selected state serially, using its exact state identifier and a new output directory. The following identifier is a placeholder, not an actual selected state:

```sh
bash scripts/python.sh scripts/phase_iv_execution_v1.py run --cohort artifacts/phase_iv_frozen --state SELECTED_STATE_ID --output-directory artifacts/phase_iv_runs/SELECTED_STATE_ID --seconds 2700
```

Detach this command for a long evaluation and poll its log; no shell tool invocation may wait ten minutes. Never run two busy verifier jobs concurrently. The wrapper locks executions, pins CPU35, disables GPUs, limits address space to 48 GiB and requires single-thread libraries and low priority. It checks allocated side storage below 9.9 GB and filesystem free space at least 20 GiB. Its scientific child is terminated at the declared duration or earlier resource failure. No scientific run may extend beyond 2026-10-30T19:00:31Z, leaving thirty minutes before the team stop. A duration is at most 3600 seconds; choose it from measured capacity and the remaining deadline.

All sampling and quadrature flags come from the immutable cohort. The wrapper permits no command-line seed or grid override. It uses 12 radial points, 42 by 84 field angles, pressure radial orders 24 and 40, pressure angular orders 64 and 80, the frozen pressure phase, and the frozen holdout stream. It uses the branch's B0 core reference and R0=0.3 as registered by the current plan.

The wrapper preserves request, process, result, audit, status and log files. A status AUDITED means the complete scientific child exited successfully and its output passed the compact audit, including exact input and source identities, saved complete grids, witness integrity, scalar norm identities, and summary arithmetic. This is not a certified error bound. Full unsaved field norms cannot be independently reconstructed from compact witnesses. Differences between pressure resolutions remain observations. Failed or partial evaluations are retained and cannot become accepted results by renaming files.

Sources qualified in V377:

- scripts/phase_iv_execution_v1.py: f62eb3ef5ad603eb766f2b388edec00a0da8634640716cfc40fe39c848d905ec
- scripts/phase_iv_result_audit_v1.py: 3d845ce4211782f479960fd3d512a5fe861b76d167ea88ef8456bafdf68ac54a
- scripts/phase_iv_manifest_v2.py: 1eb6a71598cebec818dacbbb0ef24f5563ead68b4c69518e2f5810e541628576

The final source binding must be generated from the actual current sources. A source change requires reviewing the affected qualification before final use. The historical record replay used its original settings under a synthetic test snapshot; it is not a final result or a rerun at the final settings.
