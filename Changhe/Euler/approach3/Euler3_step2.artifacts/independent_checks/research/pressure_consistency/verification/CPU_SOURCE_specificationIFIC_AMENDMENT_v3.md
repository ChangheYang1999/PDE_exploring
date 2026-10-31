# Saved-value audit amendment

Registered 2026-10-29T04:02:36.744686+00:00, before any v3 field or pressure evaluation. The numerical fields, quadratures and thresholds in v1/v2 are unchanged.

Use verify_mp_fields_cpu_v3.py and its separate Decimal auditor. The record includes 70-digit absolute-term scales and angular reference/test values, plus the existing field values. V157 qualifies the saved-value auditor with 21 controls.

Use verify_anchor_pressure_cpu_v3.py and its separate array auditor. Save complete primary and float64 diagnostic residuals and anchor indices. The primal identity compares tensor shape, dtype and bytes, including signed zero. V158 qualifies the pressure-array auditor with 16 controls.

The controls are synthetic. Neither driver has produced a new source-specific scientific result. Only CPU35, one busy computation, no GPUs or servers; all side restrictions continue.
