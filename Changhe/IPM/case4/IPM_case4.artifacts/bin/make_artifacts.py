"""Assemble the publishable subset of the numerics lane into <lane>/artifacts (relative paths preserved), under a total size cap.
Selection (all relative to the lane directory): the required documents and lane reports; lane tooling bin/ (no __pycache__); the new
code work/research860 (tests included, no __pycache__); manifests, environment, integrity records; the 860 seed and campaign policies;
G2/G3 step records and session verdicts; qualification and development records that are text or JSON; campaign roots under
outputs/campaign860 (commits, trajectory, ledgers, slice records, supervisor log, small accepted snapshots). Excluded: sampler and
resource JSONL streams, Python caches, large arrays. Per-file cap and a total cap; if the total exceeds the cap, the largest files of the
droppable groups are left out and the omissions are recorded. Writes artifacts/ARTIFACTS_MANIFEST.json (path, bytes, sha256, mtime) and
artifacts/README_ARTIFACTS.md. The previous artifacts directory is replaced atomically (staging directory, then rename); nothing else is touched.
Usage: python3 make_artifacts.py [--total-cap-mib 47] [--file-cap-mib 1.5] [--dry-run]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import argparse, fnmatch, hashlib, json, os, shutil, sys, time
from pathlib import Path
LANE = Path(__file__).resolve().parents[1]
INCLUDE = [  # (glob relative to the lane, droppable group or None)
    ('*.md', None), ('CPUS', None), ('GPU', None), ('MODEL', None),
    ('bin/*.sh', None), ('bin/*.py', None), ('bin/*.md', None),
    ('work/research860/*.py', None), ('work/research860/*.md', None), ('work/research860/*.json', None),
    ('work/research860/tests/*', None), ('work/research860/tests_dev/*', None),
    ('outputs/*.json', None), ('outputs/*.md', None),
    ('outputs/manifests/*', None), ('outputs/integrity/*', None), ('outputs/tests/*', 'tests'),
    ('outputs/campaign860/*.json', None), ('outputs/campaign860/seed/*', None), ('outputs/campaign860/ACTIVE_MANIFEST', None),
    ('outputs/campaign860/*/*.json', None), ('outputs/campaign860/*/*.log', None), ('outputs/campaign860/*/*.md', None),
    ('outputs/campaign860/*/STOP*', None), ('outputs/campaign860/*/FAULTED', None), ('outputs/campaign860/*/SUPERVISOR_PID', None),
    ('outputs/campaign860/*/trajectory.jsonl', None), ('outputs/campaign860/*/commits/*', 'commits'),
    ('outputs/campaign860/*/slice_completion/*', None), ('outputs/campaign860/*/assessments/*.json', 'assess'),
    ('outputs/campaign860/*/assessments/*.jsonl', None), ('outputs/campaign860/*/assessments/*.md', None),
    ('outputs/campaign860/*/snapshots/*.json', 'snap'), ('outputs/campaign860/*/snapshots/*.npz', 'snap'),
    ('outputs/campaign860/*/proposals/*', 'proposals'), ('outputs/campaign860/*/outcomes/*', 'proposals'),
    ('outputs/campaign860/*/guard_session*/runs/*/result.json', None), ('outputs/campaign860/*/guard_session*/runs/*/worker.log', None),
    ('outputs/campaign860/*/guard_session*/runs/*/running.json', None), ('outputs/campaign860/*/guard_session*/*.json', None),
    ('outputs/g3/*.log', None), ('outputs/g3/g3_v1/*.json', 'g3'), ('outputs/g3/g3_v1/*.md', None), ('outputs/g3/g3_v1/run.log', None),
    ('outputs/g3/tools/*', None), ('outputs/g3/session_*/runs/*/result.json', None), ('outputs/g3/session_*/runs/*/running.json', None),
    ('outputs/g3/session_*/runs/*/worker.log', 'g3'),
    ('outputs/g2/*.md', None), ('outputs/g2/*.log', 'g2'), ('outputs/g2/g2_v*/*.json', 'g2'), ('outputs/g2/g2_v*/*.md', 'g2'), ('outputs/g2/g2_v*/*.log', 'g2'),
    ('outputs/g2/session_*/runs/*/result.json', 'g2'),
    ('outputs/qual/*.md', 'qual'), ('outputs/qual/*.json', 'qual'), ('outputs/qual/*.log', 'qual'), ('outputs/qual/*.txt', 'qual'),
    ('outputs/qual/*/*.md', 'qual'), ('outputs/qual/*/*.json', 'qual'), ('outputs/qual/*/*.log', 'qual'), ('outputs/qual/*/*.txt', 'qual'),
    ('outputs/qual/*/*/*.md', 'qual'), ('outputs/qual/*/*/*.json', 'qual'), ('outputs/qual/*/*/*.log', 'qual'), ('outputs/qual/*/*/*.txt', 'qual'),
    ('outputs/qual/*/*/*/*.md', 'qual'), ('outputs/qual/*/*/*/*.json', 'qual'), ('outputs/qual/*/*/*/*.log', 'qual'),
    ('outputs/qual/*/runs/*/result.json', 'qual'),
    ('outputs/checks/*', 'checks'), ('outputs/checks/*/*', 'checks'), ('outputs/diag/*', 'diag'), ('outputs/diag/*/*', 'diag'),
    ('outputs/dev_v9/*.md', 'dev'), ('outputs/dev_v9/*.py', 'dev'), ('outputs/dev_v9/*.sh', 'dev'), ('outputs/dev_v9/*.json', 'dev'), ('outputs/dev_v9/*.log', 'dev'),
    ('outputs/dev_v9/pending/*', 'dev'), ('outputs/dev_v9/pending_g4/*', None),
    ('outputs/dev_v9/farfield_states.py', None), ('outputs/dev_v9/read_assessment.py', None), ('outputs/dev_v9/farfield_states/TABLE.md', None), ('outputs/g3/eta/*.json', None),
    ('shifts/*', None), ('astra/*/question.md', 'astra'), ('astra/*/answer.md', 'astra'),
]
EXCLUDE_NAMES = ['*_rss.jsonl', 'resources.jsonl', '*.pyc', '*.pid', '*.lock', '*.tmp', '*.bak']
EXCLUDE_DIRS = ['__pycache__', 'artifacts', 'artifacts.staging', 'env', 'pip-cache', 'tmp']
GROUP_DROP_ORDER = ['dev', 'qual', 'diag', 'checks', 'astra', 'g2', 'proposals', 'tests', 'snap', 'assess', 'g3', 'commits']
def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
def select(file_cap):
    chosen = {}; skipped_big = []
    for pat, group in INCLUDE:
        for p in LANE.glob(pat):
            if not p.is_file() or p.is_symlink(): continue
            rel = p.relative_to(LANE)
            if any(part in EXCLUDE_DIRS for part in rel.parts[:-1]): continue
            if any(fnmatch.fnmatch(p.name, e) for e in EXCLUDE_NAMES): continue
            size = p.stat().st_size
            if size > file_cap: skipped_big.append((str(rel), size)); continue
            if str(rel) not in chosen or chosen[str(rel)][1] is None: chosen[str(rel)] = (size, group)
    return chosen, skipped_big
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--total-cap-mib', type=float, default=47.); ap.add_argument('--file-cap-mib', type=float, default=1.5); ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args(); total_cap = int(a.total_cap_mib*2**20); file_cap = int(a.file_cap_mib*2**20)
    chosen, skipped_big = select(file_cap); dropped = []
    total = sum(s for s, g in chosen.values())
    for group in GROUP_DROP_ORDER:
        if total <= total_cap: break
        cand = sorted([(s, r) for r, (s, g) in chosen.items() if g == group], reverse=True)
        for s, r in cand:
            if total <= total_cap: break
            # keep the newest snapshot/commit files: drop oldest first within the group when names sort chronologically
            dropped.append((r, s, group)); del chosen[r]; total -= s
    print('selected %d files, %.2f MiB (cap %.1f MiB); %d above the per-file cap; %d dropped for the total cap' % (len(chosen), total/2**20, a.total_cap_mib, len(skipped_big), len(dropped)))
    if total > total_cap: print('ERROR: still above the cap after dropping every droppable group', file=sys.stderr); sys.exit(2)
    if a.dry_run:
        for r in sorted(chosen): print('  %9d  %s' % (chosen[r][0], r))
        for r, s in skipped_big: print('  SKIPPED(big) %9d %s' % (s, r))
        for r, s, g in dropped: print('  DROPPED(%s) %9d %s' % (g, s, r))
        return
    staging = LANE/'artifacts.staging'; final = LANE/'artifacts'
    if staging.exists(): shutil.rmtree(staging)
    staging.mkdir()
    rows = []
    for r in sorted(chosen):
        src = LANE/r; dst = staging/r; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(src, dst)
        st = dst.stat(); rows.append({'path': r, 'bytes': st.st_size, 'sha256': sha256(dst), 'mtime_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(st.st_mtime)), 'group': chosen[r][1]})
    man = {'schema': 'c4num_artifacts_v1', 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'lane': str(LANE), 'total_bytes': sum(x['bytes'] for x in rows), 'n_files': len(rows),
           'total_cap_bytes': total_cap, 'file_cap_bytes': file_cap, 'files': rows, 'skipped_above_file_cap': [{'path': r, 'bytes': s} for r, s in skipped_big],
           'dropped_for_total_cap': [{'path': r, 'bytes': s, 'group': g} for r, s, g in dropped],
           'note': 'Paths are relative to the lane directory; the same relative layout is kept here. Sampler and resource JSONL streams, Python caches, the virtual environment and large arrays are not included; they remain in the lane directory.'}
    (staging/'ARTIFACTS_MANIFEST.json').write_text(json.dumps(man, indent=1))
    readme = ['# Artifacts of the numerics lane (c4-num), assembled %s' % man['utc'], '',
              ('Publishable subset of ' + _artifact_root + ' (%d files, %.2f MiB). Relative paths are the lane paths.') % (len(rows), man['total_bytes']/2**20), '',
              'Start with: START_HERE_NEW_RUN.md, NUM_REPORT.md, LINUX_QUALIFICATION.md, BASIS_860_IMPLEMENTATION.md, EMBEDDING_TESTS.md,',
              'OPTIMIZATION_860_LOG.md, RESULTS_860.md, RUNBOOK_860.md. Machine-readable: ARTIFACTS_MANIFEST.json (this subset), outputs/manifests/',
              '(frozen code manifests and environment.json), outputs/integrity/ (protected-source checksums before and after), outputs/campaign860/',
              '(860 seed, policies, campaign roots with commits and ledgers), outputs/g3/g3_v1/ (chart gate t4.json, bench.json, ETA records).', '',
              'Not included (kept in the lane): the Python environment env/, the full working copy work/ other than the new research860 code,',
              'resource and RSS sampler streams, arrays above %.1f MiB, and %d files dropped for the total cap (listed in ARTIFACTS_MANIFEST.json).' % (a.file_cap_mib, len(dropped)), '',
              'No optimizer state in these files is an exact PDE solution; see RESULTS_860.md for the caveats.']
    (staging/'README_ARTIFACTS.md').write_text('\n'.join(readme)+'\n')
    if final.exists():
        prev = LANE/('artifacts.prev_%s' % time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())); final.rename(prev); staging.rename(final); shutil.rmtree(prev)
    else: staging.rename(final)
    print('written', final, 'files', len(rows), 'bytes', man['total_bytes'])
if __name__ == '__main__': main()
