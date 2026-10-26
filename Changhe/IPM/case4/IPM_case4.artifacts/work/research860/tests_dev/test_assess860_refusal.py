"""E7 (d) regression on the real assess860: --no-integral without --spot-only exits 2 with the reason on stderr and writes no output JSON; the refusal precedes every
library import, so this runs without the guard. --no-integral together with --spot-only is accepted at parse time (the process is killed after 3 s to avoid any evaluation
outside the guard; the check is only that it did not exit 2 at the parser). Usage: fixture_assess860_refusal.py <assess860.py> <out.json>"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, subprocess, hashlib, tempfile, os
from pathlib import Path
src = Path(sys.argv[1]).resolve(); out = Path(sys.argv[2]).resolve(); LANE = Path((_artifact_root))
res = {'source': str(src), 'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': {}}
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:300], flush=True)
with tempfile.TemporaryDirectory(dir=str(out.parent)) as td:
    o = Path(td)/'a.json'
    p = subprocess.run([sys.executable, '-B', str(src), str(o), str(LANE/'outputs/dev_v9/tmp_manifest_kappa.json'), str(LANE/'outputs/campaign860/seed/seed_860.json'), '4', '--no-integral'], capture_output=True, text=True, timeout=60)
    record('no_integral_without_spot_only_exits_2_no_output', p.returncode == 2 and not o.exists() and 'REFUSAL' in p.stderr and 'spot-only' in p.stderr, returncode=p.returncode, stderr=p.stderr[-200:])
    try:
        p2 = subprocess.run([sys.executable, '-B', str(src), str(o), str(LANE/'outputs/dev_v9/tmp_manifest_kappa.json'), str(LANE/'outputs/campaign860/seed/seed_860.json'), '4', '--no-integral', '--spot-only'], capture_output=True, text=True, timeout=3); rc2 = p2.returncode; err2 = p2.stderr[-200:]
    except subprocess.TimeoutExpired as e: rc2 = 'running past the parser (killed at 3 s)'; err2 = (e.stderr or b'')[-200:].decode(errors='replace') if isinstance(e.stderr, bytes) else str(e.stderr)[-200:]
    record('no_integral_with_spot_only_passes_the_parser', rc2 != 2, returncode=rc2, stderr=err2)
res['passed'] = all(c['passed'] for c in res['cases'].values()); out.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
