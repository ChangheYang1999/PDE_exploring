"""Converter for the typed kappa record (lead ruling 2026-10-24T09:22Z; this file is a pending development copy until it is frozen in the G3 manifest; the G3 audit reruns
the frozen copy on the bound sources and byte-compares the output with the bound typed record): kappa_calibration.json + the calibration step JSON -> outputs/campaign860/kappa_calibration_typed.json with the sha256 of both sources,
kappa and rho_max copied exactly, coverage as typed records {set, covered, count, reason}, T2.6d covered false with the t26 bitwise-equality reason, and the T3.6 count equal
to the number of points actually evaluated. Usage: kappa_typed_converter.py <step.json> <kappa_calibration.json> <out typed.json>"""
import json, sys, hashlib
from pathlib import Path
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
step_path, kappa_path, out_path = map(Path, sys.argv[1:4])
step = json.loads(step_path.read_text()); kap = json.loads(kappa_path.read_text())
if not step.get('passed'): raise SystemExit('calibration step JSON did not pass; no typed file is written')
if step.get('kappa') != kap.get('kappa') or step.get('rho_max') != kap.get('rho_max'): raise SystemExit('kappa/rho_max differ between the step JSON and kappa_calibration.json')
cov = kap['coverage']; rows = []
t36 = sum(1 for r in step['rows'] if str(r.get('point', '')).startswith('T3.6_'))//max(1, len(step.get('seconds_per_cl', {})) or 1)
rows.append({'set': 'T2.6c_finite_v92', 'covered': True, 'count': int(cov['T2.6c_finite_v92']), 'reason': None})
rows.append({'set': 'T2.6b_far', 'covered': True, 'count': int(cov['T2.6b_far']), 'reason': None})
rows.append({'set': 'T2.6x_parameter_values', 'covered': True, 'count': len(cov['T2.6x_parameter_values']), 'reason': None})
rows.append({'set': 'T2.6d_embedded_training_sized_configuration_of_the_T2.6c_points', 'covered': False, 'count': None, 'reason': 'not evaluated: g2_v4 t26 T2.6d found R_f bitwise equal between the training-sized embedded call and the one-point and batch shapes at these points at the seed c_l, but it did not compare the condition sums S_R, so rho in the training-sized configuration is not established for these points'})
rows.append({'set': 'T3.6_diagnosed_points', 'covered': t36 > 0, 'count': int(t36), 'reason': (None if t36 > 0 else 'no T3.6 diagnosed points were available at run time')})
rows.append({'set': 'near_y_axis_training_nodes_v913', 'covered': True, 'count': len(cov['near_y_axis_training_nodes_v913']['indices']), 'reason': None})
typed = {'schema': 'kappa_calibration_typed_v1', 'kappa': kap['kappa'], 'rho_max': kap['rho_max'], 'rho_argmax': kap.get('rho_argmax'), 'definition': kap.get('definition'), 'u': kap.get('u'), 'coverage': rows,
         'source_step_json': str(step_path.resolve()), 'source_step_json_sha256': digest(step_path), 'source_kappa_json': str(kappa_path.resolve()), 'source_kappa_json_sha256': digest(kappa_path), 'code_manifest_sha256_of_calibration': step.get('code_manifest_sha256'), 'utc': step.get('finished_utc')}
if out_path.exists(): raise SystemExit('typed file exists; refusing to overwrite')
out_path.write_text(json.dumps(typed, indent=1)+'\n'); print('typed kappa file written', out_path, digest(out_path))
