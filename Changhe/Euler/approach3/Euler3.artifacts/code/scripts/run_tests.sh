#!/bin/bash
# Run the whole test suite sequentially (GPU tests on CUDA device 0 of the visible set); log to logs/test_suite_<date>.log
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
LOG=logs/test_suite_$(date -u +%Y%m%dT%H%M%SZ).log
export OMP_NUM_THREADS=2 CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}
for t in tests/test_solid_harmonics.py tests/test_residuals.py tests/test_pressure.py tests/test_pressure_twisted.py tests/test_lm.py \
         tests/test_channels.py tests/test_spec_T06_T07.py tests/test_gauge_lm.py tests/test_T04_dilation_diagnostics.py tests/test_pressure_ray.py \
         tests/test_channel_degrees.py tests/test_pressure_offgrid.py tests/test_free_param_lm.py tests/test_T05_diagnostics_rotation.py tests/test_T08_origin_taylor.py tests/test_core_resolution.py tests/test_S8_viscous.py tests/test_S9_balances.py tests/test_S9b_guards.py tests/test_far_helicity.py tests/test_S12_radial_rows.py tests/test_s9d_lambda.py tests/test_T11_resume_iterates.py tests/test_T12_gauge_steps.py "tests/test_fields.py even"; do
  echo "=== $(date -u +%FT%TZ) $t" >> $LOG
  timeout 1800 .venv/bin/python $t >> $LOG 2>&1 && echo "=== PASS $t" >> $LOG || echo "=== FAIL $t (exit $?)" >> $LOG
done
echo "=== $(date -u +%FT%TZ) suite finished" >> $LOG
grep "^=== PASS\|^=== FAIL" $LOG
