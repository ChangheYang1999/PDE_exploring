"""Validated kappa calibration file (SPEC v9.7, v9.12 (d), v9.15 (4); typed schema per the lead ruling 2026-10-24T09:22Z); shared by campaign860 and assess860. kappa comes ONLY from the typed
file outputs/campaign860/kappa_calibration_typed.json written by kappa_typed_converter.py (pending development copy until frozen in the G3 manifest) from the calibration step JSON
and kappa_calibration.json; the manifest-binding refusal below is kept."""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, hashlib
from pathlib import Path
LANE = Path((_artifact_root))     # the lane root (fixed; the manifest paths are lane-relative)
NEEDED = ('T2.6c', 'T2.6x', 'T2.6d', 'T3.6', 'near_y_axis')

def _digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def load_kappa(kappa_file, manifest_path):
    """Refuses (ValueError) unless: kappa finite and >= 2048 and == max(2048, 4 rho_max) with rho_max finite and >= 0; coverage is a LIST of typed records
    {set: str, covered: bool, count: int|null, reason: str|null} naming T2.6c, T2.6x, T2.6d, T3.6 and near_y_axis (an uncovered set needs a reason); the file names
    its sources (source_step_json, source_kappa_json) with sha256 values that match the files on disk; the typed file's own sha256 is bound in the manifest under
    its exact lane-relative path."""
    if not kappa_file: raise ValueError('kappa: --kappa-file is mandatory (SPEC v9.12 (d))')
    kp = Path(kappa_file); k = json.loads(kp.read_text()); kappa = k.get('kappa'); rho = k.get('rho_max')
    if not isinstance(kappa, (int, float)) or isinstance(kappa, bool) or not math.isfinite(float(kappa)): raise ValueError('kappa: not finite')
    if float(kappa) < 2048.: raise ValueError('kappa: below 2048')
    if not isinstance(rho, (int, float)) or isinstance(rho, bool) or not math.isfinite(float(rho)) or float(rho) < 0: raise ValueError('kappa: rho_max missing, nonfinite or negative (%r)' % (rho,))
    if float(kappa) != max(2048., 4*float(rho)): raise ValueError('kappa: not equal to max(2048, 4 rho_max) recomputed from the file (%r vs %r)' % (kappa, max(2048., 4*float(rho))))
    cov = k.get('coverage')
    if not isinstance(cov, list) or not cov: raise ValueError('kappa: coverage must be a non-empty list of typed records {set, covered, count, reason}')
    names = []
    for rec in cov:
        if not (isinstance(rec, dict) and isinstance(rec.get('set'), str) and isinstance(rec.get('covered'), bool) and (rec.get('count') is None or (isinstance(rec.get('count'), int) and not isinstance(rec.get('count'), bool))) and (rec.get('reason') is None or isinstance(rec.get('reason'), str))):
            raise ValueError('kappa: coverage record %r is not typed {set: str, covered: bool, count: int|null, reason: str|null}' % (rec,))
        if rec['covered'] is False and not rec.get('reason'): raise ValueError('kappa: uncovered set %r has no reason' % rec['set'])
        names.append(rec['set'])
    missing = [n for n in NEEDED if not any(n in nm for nm in names)]
    if missing: raise ValueError('kappa: coverage does not name the point sets %s' % missing)
    for key in ('source_step_json', 'source_kappa_json'):
        src = k.get(key); sha = k.get(key+'_sha256')
        if not (isinstance(src, str) and isinstance(sha, str) and Path(src).exists()): raise ValueError('kappa: %s missing or absent on disk' % key)
        if _digest(src) != sha: raise ValueError('kappa: %s sha256 does not match the file on disk' % key)
    sha = _digest(kp); m = json.loads(Path(manifest_path).read_text())
    try: rel = str(kp.resolve().relative_to(LANE))
    except ValueError: rel = str(kp.resolve())
    rows = [r for r in m.get('files', []) if r.get('path') in (rel, str(kp.resolve()))]
    if not rows or any(r.get('sha256') != sha for r in rows): raise ValueError('kappa: typed file sha256 %s is not bound in the manifest %s (exact path %s)' % (sha[:16], manifest_path, rel))
    return {'kappa': float(kappa), 'rho_max': float(rho), 'source': str(kp.resolve()), 'source_sha256': sha, 'coverage': cov, 'definition': k.get('definition', 'SPEC v9.7'), 'source_step_json_sha256': k['source_step_json_sha256'], 'source_kappa_json_sha256': k['source_kappa_json_sha256']}
