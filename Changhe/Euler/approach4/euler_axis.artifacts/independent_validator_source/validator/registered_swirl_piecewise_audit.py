"""Three-resolution prescribed swirl fractions of an already registered field."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, time
from piecewise_loading import load_piecewise
from piecewise_dynamics import core_swirl_fraction, far_swirl_fraction
from independent_artifacts import atomic_json, sha256, verify_source_identity
ROOT = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('candidate', type=Path)
ap.add_argument('--geometry', type=Path, required=True)
ap.add_argument('--output', type=Path, required=True)
a = ap.parse_args()
a.output = a.output.resolve()
assert a.output.is_relative_to(ROOT.parent) and not a.output.exists()
start, cpu = time.perf_counter(), time.process_time()
geometry = json.loads(a.geometry.read_text())
field = load_piecewise(a.candidate)
L = float(geometry['gauge']['dilation_L'])
a_eff = float(geometry['core']['a_eff'])
paths = [Path(__file__), ROOT/'src/piecewise_loading.py', ROOT/'src/piecewise_dynamics.py',
         ROOT/'src/piecewise_adapter.py', ROOT/'src/piecewise_jacobi.py',
         ROOT/'src/piecewise_precision.py', ROOT/'src/independent_fields.py',
         ROOT.parent/'research/piecewise_characteristics/PROOF.md']
hashes = {str(p.relative_to(ROOT.parent)): sha256(p) for p in paths}
inputs = {str(p.resolve()): sha256(p) for p in [a.candidate, a.geometry]}
rows = []
for nr, na in [(24,64), (48,96), (72,128)]:
    row = core_swirl_fraction(field, 4*a_eff/L, nradial=nr, nangle=na)
    row['coordinates'] = 'exported working coordinates'
    row['far'] = far_swirl_fraction(field, nangle=na)
    rows.append(row)
    print(nr, na, row['s_core'], row['far']['s_far'], flush=True)
# Dilation preserves fractions; integral values scale by L^5.
reported = core_swirl_fraction(field.dilate(L), 4*a_eff, nradial=72, nangle=128)
changes = [abs(rows[i]['s_core']-rows[i-1]['s_core']) for i in range(1,len(rows))]
checks = {
    'working_vs_reporting_fraction': abs(rows[-1]['s_core']-reported['s_core']) < 1e-12,
    'integral_dilation_total': abs(reported['total_velocity_squared_integral']/(L**5*rows[-1]['total_velocity_squared_integral'])-1) < 1e-11,
    'integral_dilation_swirl': abs(reported['swirl_velocity_squared_integral']/(L**5*rows[-1]['swirl_velocity_squared_integral'])-1) < 1e-11,
    'last_refinement_change_below_1e-8': changes[-1] < 1e-8,
    'swirl_magnitude_filter': rows[-1]['s_core'] >= .05 and rows[-1]['far']['s_far'] >= .05,
}
verify_source_identity(ROOT.parent, hashes)
assert all(sha256(Path(p)) == h for p,h in inputs.items())
result = dict(completed_utc=datetime.now(timezone.utc).isoformat(), candidate_sha256=sha256(a.candidate),
    source_sha256=hashes, input_sha256=inputs, rows=rows, reporting=reported,
    a_eff_reporting=a_eff, dilation_L=L, refinement_changes=changes, checks=checks,
    wall_seconds=time.perf_counter()-start, cpu_seconds=time.process_time()-cpu,
    scope='Numerical quadrature on a fixed piecewise field and a finite-search a_eff. Core radius is exactly 4 a_eff and the far fraction uses the analytic leading coefficient. Changes concern integration resolution, not B2 stability between candidate resolutions. No interval error bound or exact-profile claim.')
atomic_json(a.output, result)
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','source_sha256','input_sha256']}, indent=2))
