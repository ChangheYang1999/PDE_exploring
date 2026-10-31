# Precision-path labels and float64 anchor diagnostic

Registered 2026-10-29T03:42:43.212885+00:00, before the new CPU pressure or multiprecision drivers have run. Use verify_mp_fields_cpu_v2.py and verify_anchor_pressure_cpu_v2.py in place of their prepared v1 copies. Other field choices, resolution and pass thresholds are unchanged.

G6 tests the regular field map: angular tables evaluated in double-double and rounded once, followed by float64 radial factors, twist, assembly and tangents. It does not test the unrounded source_dd pressure path. Each quantity's actual route is recorded, and angular evaluation is explicitly requested with path=dd. The momentum derivative without pressure is the direct Cartesian identity, separately labelled from the stable-linear implementation.

G4(d) retains the actual selected primary precision mode and the bitwise pressure-primal identity. A separate float64 Problem at the same geometry, coefficients, parameters and pivot supplies a diagnostic residual with its own recomputed weights. Report its pressure substitution, anchor norm and implied O1 change beside configuration M. Also retain the float64-to-primary pressure difference under primary weights. No diagnostic can replace a failed primary gate. The existing discrete-moment diagnostic contracts the regular float64 GU and is explicitly labelled; it is not an unrounded double-double source integral.

All earlier CPU, single-core, memory, disk and no-server restrictions remain in force. No result has been assumed from preparing these changes.
