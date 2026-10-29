#!/usr/bin/env python3
"""Check an exchange record without importing its evaluator or executing its code."""
from pathlib import Path
import argparse, datetime, json, time
import numpy as np
from independent_artifacts import atomic_json, sha256
from piecewise_loading import load_piecewise

ROOT = Path(__file__).resolve().parent

def preflight(export, source_result=None, check_samples=True):
    export = Path(export).resolve()
    start = time.perf_counter()
    cpu = time.process_time()
    required = ['BASIS.md', 'candidate.json', 'coeffs.npz', 'samples.npz']
    paths = {name: export/name for name in required}
    if source_result is None and (export/'source_run_result.json').exists():
        source_result = export/'source_run_result.json'
    if source_result is not None:
        paths['source_run_result.json'] = Path(source_result).resolve()
    hashes = {name: sha256(path) for name, path in paths.items()}
    candidate = json.loads(paths['candidate.json'].read_text())
    issues = []
    checks = []
    def compare(label, actual, expected, tolerance=2e-13):
        error = abs(float(actual)-float(expected))/(1+abs(float(expected)))
        passed = bool(np.isfinite(error) and error <= tolerance)
        checks.append(dict(name=label, actual=float(actual), expected=float(expected),
                           scaled_error=error, tolerance=tolerance, passed=passed))
        if not passed:
            issues.append(dict(kind='METADATA_MISMATCH', name=label))
    with np.load(paths['coeffs.npz'], allow_pickle=False) as data:
        metadata = json.loads(str(data['meta_json']))
        finite = all(np.all(np.isfinite(data[key])) for key in data.files if key != 'meta_json')
    if not finite:
        issues.append(dict(kind='NONFINITE_COEFFICIENTS', name='coefficient arrays'))
    for record, label in [(candidate, 'candidate'), (metadata, 'coefficient metadata')]:
        compare(label+' alpha formula', record['alpha'], (1-record['cl'])/record['cl'])
    compare('candidate versus coefficient c_l', candidate['cl'], metadata['cl'])
    if source_result is not None:
        source = json.loads(paths['source_run_result.json'].read_text())
        compare('export versus final run c_l', metadata['cl'], source['cl'])
        compare('export versus final run alpha', metadata['alpha'], source['alpha'])
        if 'L_to_reporting_gauge' in source:
            compare('export versus final run dilation', candidate['L_to_reporting_gauge'], source['L_to_reporting_gauge'])
    samples = []
    # Do not spend effort checking a field known not to represent its claimed run.
    if not issues and check_samples:
        field = load_piecewise(paths['coeffs.npz'])
        with np.load(paths['samples.npz'], allow_pickle=False) as data:
            got = field.cylindrical(data['r'], data['z'], 3)
            fields = [('phi', got['phi'][0,0]), ('q', got['q'][0,0]),
                      ('Ur', got['U'][:,0]), ('Utheta', got['U'][:,1]),
                      ('Uz', got['U'][:,2]), ('eta', got['eta'])]
            for name, values in fields:
                error = abs(values-data[name])
                scale = 1+float(np.max(abs(data[name])))
                scaled = float(np.max(error))/scale
                at = int(np.argmax(error))
                passed = bool(np.isfinite(scaled) and scaled <= 2e-11)
                samples.append(dict(name=name, count=int(values.size), max_abs_error=float(np.max(error)),
                    scaled_error=scaled, tolerance=2e-11, passed=passed, worst_index=at,
                    worst_point=[float(data['r'][at]),float(data['z'][at])]))
                if not passed:
                    issues.append(dict(kind='FIELD_REPRODUCTION_MISMATCH', name=name))
    for name, path in paths.items():
        if sha256(path) != hashes[name]:
            raise RuntimeError('exchange input changed while being checked: '+name)
    status = 'PASS' if not issues else 'FAIL'
    return dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), status=status,
        c_l=float(metadata['cl']), alpha=float(metadata['alpha']), export_directory=str(export),
        input_paths={name:str(path) for name,path in paths.items()}, input_sha256=hashes,
        source_sha256={str(Path(__file__).relative_to(ROOT)):sha256(__file__),
                       'src/piecewise_adapter.py':sha256(ROOT/'src/piecewise_adapter.py'),
                       'src/piecewise_jacobi.py':sha256(ROOT/'src/piecewise_jacobi.py'),
                       'src/piecewise_loading.py':sha256(ROOT/'src/piecewise_loading.py')},
        metadata_checks=checks, sample_checks=samples, issues=issues,
        source_run_checked=source_result is not None, samples_requested=check_samples,
        wall_seconds=time.perf_counter()-start, cpu_seconds=time.process_time()-cpu,
        scope='Exchange integrity and independent field reproduction only. No Euler residual or acceptance claim.')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('export',type=Path)
    ap.add_argument('--source-result',type=Path)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--metadata-only',action='store_true')
    a=ap.parse_args()
    if not a.output.resolve().is_relative_to(ROOT.parent): raise ValueError('output outside lane')
    if a.output.exists(): raise FileExistsError('preserve previous audit')
    result=preflight(a.export,a.source_result,not a.metadata_only)
    atomic_json(a.output,result)
    print(json.dumps({key:result[key] for key in ['status','c_l','issues','wall_seconds']}),flush=True)
    raise SystemExit(0 if result['status']=='PASS' else 2)
if __name__=='__main__': main()
