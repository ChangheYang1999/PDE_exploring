"""Archive closed old replay streams with verified restoration metadata first."""
from __future__ import annotations

import argparse
from collections import Counter, deque
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import time

from bot_research.experiments.validation.artifact_io import atomic_json

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
PROGRAM = E / 'archive_mature_replays_004.py'
PLAN = R / 'archived-mature-replays-004-plan.json'
MANIFEST = R / 'archived-mature-replays-004.json'
COMPLETION = R / 'archived-mature-replays-004-completion.json'
README = R / 'ARCHIVED_MATURE_REPLAYS_004.md'
CUTOFF = datetime(2026, 10, 31, 18, tzinfo=timezone.utc)
TARGET_SAVING = 150_000_000
ROOT_NAMES = (
    'terminal-candidate-declaration-001.json',
    'wall-prefix-selector-001.json',
    'wall-prefix-selector-checker-amendment-001.json',
    'delayed-wall-counter-001.json',
    'reserved-wall-counter-001.json',
    'two-round-wall-selector-001.json',
    'late-reserved-wall-counter-001.json',
    'ten-policy-game-declaration-001.json',
    'support-only-certificate-001.json',
    'immune-shortcut-001.json',
    'immune-shortcut-followup-001.json',
    'delayed-signal-ambiguity-001.json',
    'wall-timing-transfer-001.json',
)
ANALYSES = (
    'wall_prefix_selector', 'delayed_wall_counter', 'reserved_wall_counter',
    'two_round_wall_selector', 'late_reserved_wall_counter', 'ten_policy_game',
    'support_only_certificate', 'immune_runtime_shortcut', 'immune_shortcut_followup',
    'delayed_signal_ambiguity',
)


def now():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    return json.loads(Path(path).read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def refs(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from refs(key)
            yield from refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from refs(item)
    elif isinstance(value, str) and value.startswith('bot_research/'):
        p = Path(value)
        if not p.is_absolute() and '..' not in p.parts and '\n' not in value:
            yield value


def protection():
    roots = [E / name for name in ROOT_NAMES]
    for name in ANALYSES:
        roots.extend(sorted((E / 'analysis' / name / 'verification').glob('*.json')))
    root_hashes = {str(p): sha(p) for p in roots}
    terminal = read(E / ROOT_NAMES[0])['source_sha256']
    assert len(terminal) == 85
    assert all(sha(p) == h for p, h in terminal.items())
    protected = set(terminal) | set(root_hashes)
    # Reserved terminal JSON contents stay opaque; their exact bytes are pinned.
    pending = deque(p for p in roots if p != E / ROOT_NAMES[0])
    visited = set()
    while pending:
        p = pending.popleft()
        name = str(p)
        if name in visited:
            continue
        visited.add(name)
        for ref in refs(read(p)):
            protected.add(ref)
            q = Path(ref)
            if q.suffix == '.json' and q.is_file() and ref not in visited and ref not in terminal:
                pending.append(q)
    return protected, root_hashes, terminal


def processes():
    """Read only local process metadata; retain relative validation references."""
    cwd = Path.cwd()
    rows = []
    for p in Path('/proc').iterdir():
        if not p.name.isdigit() or int(p.name) == os.getpid():
            continue
        try:
            if not (p / 'comm').read_text().strip().startswith('python'):
                continue
            args = (p / 'cmdline').read_bytes().decode(errors='replace').split('\0')
            if Path(os.readlink(p / 'cwd')) != cwd and not any('bot_research' in a for a in args):
                continue
            module = args[args.index('-m') + 1] if '-m' in args else 'python-worker'
            opened = []
            for fd in (p / 'fd').iterdir():
                try:
                    target = Path(os.readlink(fd))
                    relative = target.relative_to(cwd)
                    if str(relative).startswith(str(R) + '/'):
                        opened.append(str(relative))
                except (OSError, ValueError):
                    pass
            rows.append(dict(pid=int(p.name), module=module,
                             references=sorted(set(opened)), _args=args))
        except (OSError, ValueError, IndexError):
            continue
    return rows


def active_campaign(name, proc):
    prefix = str(R / name) + '/'
    return any(any(name in arg for arg in row['_args']) or
               any(ref.startswith(prefix) for ref in row['references']) for row in proc)


def public_processes(proc):
    return [{k: v for k, v in row.items() if k != '_args'} for row in proc]


def old_regular(p):
    return p.is_file() and not p.is_symlink() and p.stat().st_mtime < CUTOFF.timestamp()


def plan():
    started = now()
    protected, root_hashes, terminal = protection()
    proc = processes()
    candidates, closed, skipped = [], {}, Counter()
    for directory in sorted(R.iterdir()):
        if not directory.is_dir() or directory.is_symlink():
            continue
        name = directory.name
        if name.startswith('reserved-') or active_campaign(name, proc):
            skipped['reserved_or_active_campaign'] += 1
            continue
        summary, jobs, matches = [directory / leaf for leaf in ('summary.json', 'jobs.json', 'matches.jsonl')]
        if not all(old_regular(p) for p in (summary, jobs, matches)):
            continue
        state = read(summary)
        try:
            closed_at = datetime.fromisoformat(state['time_utc'])
            assert closed_at.tzinfo is not None
        except (KeyError, ValueError, TypeError, AssertionError):
            skipped['missing_or_invalid_closing_time'] += 1
            continue
        if (not state.get('complete') or state.get('failures') or state.get('invalid') or
                state.get('planned') != state.get('valid_completed') or
                closed_at >= CUTOFF):
            skipped['incomplete_or_failed_campaign'] += 1
            continue
        job_rows = read(jobs)
        match_rows = [json.loads(line) for line in matches.read_text().splitlines()]
        if not (len(job_rows) == len(match_rows) == state['planned']):
            skipped['campaign_accounting_mismatch'] += 1
            continue
        job_paths = {j['replay_path'] for j in job_rows}
        match_paths = {r['replay_path'] for r in match_rows}
        if job_paths != match_paths or len(match_paths) != len(match_rows):
            skipped['campaign_replay_accounting_mismatch'] += 1
            continue
        accepted = []
        for p in sorted((directory / 'replays').glob('*.jsonl')):
            if str(p) in protected:
                skipped['protected_replay'] += 1
                continue
            if not old_regular(p) or str(p) not in job_paths:
                skipped['recent_or_unaccounted_replay'] += 1
                continue
            if p.with_suffix('.jsonl.gz').exists():
                skipped['existing_compressed_copy'] += 1
                continue
            result = directory / 'results' / (p.stem + '.json')
            if not old_regular(result):
                skipped['missing_or_recent_result'] += 1
                continue
            row = read(result)
            if row.get('result') is None or row.get('replay_path') != str(p):
                skipped['nonterminal_or_mismatched_result'] += 1
                continue
            stat = p.stat()
            accepted.append(dict(original_path=str(p), original_bytes=stat.st_size,
                                 original_mtime_ns=stat.st_mtime_ns,
                                 result_path=str(result), result_sha256=sha(result),
                                 campaign=name))
        if accepted:
            closed[name] = dict(summary_sha256=sha(summary), jobs_sha256=sha(jobs),
                                matches_sha256=sha(matches), complete=state['complete'],
                                planned=state['planned'], valid_completed=state['valid_completed'],
                                closed_utc=state['time_utc'])
            candidates.extend(accepted)
    candidates.sort(key=lambda row: (-row['original_bytes'], row['original_path']))
    value = dict(time_utc=now(), started_utc=started, cutoff_utc=CUTOFF.isoformat(),
                 target_saved_bytes=TARGET_SAVING, candidates=candidates,
                 candidate_original_bytes=sum(r['original_bytes'] for r in candidates),
                 closed_campaigns=closed, exclusions=dict(skipped),
                 protected_roots_sha256=root_hashes, protected_paths=sorted(protected),
                 terminal_source_sha256=terminal, processes=public_processes(proc),
                 archive_program_sha256=sha(PROGRAM))
    atomic_json(PLAN, value, exclusive=True)
    print(json.dumps(dict(time_utc=now(), plan=str(PLAN), candidates=len(candidates),
                          candidate_original_bytes=value['candidate_original_bytes'],
                          closed_campaigns=len(closed), exclusions=dict(skipped),
                          protected_paths=len(protected), terminal_pins=len(terminal))), flush=True)


def verify_plan(value):
    assert sha(PROGRAM) == value['archive_program_sha256']
    assert all(sha(p) == h for p, h in value['protected_roots_sha256'].items())
    assert all(sha(p) == h for p, h in value['terminal_source_sha256'].items())
    for name, detail in value['closed_campaigns'].items():
        for leaf in ('summary', 'jobs', 'matches'):
            p = R / name / (leaf + ('.jsonl' if leaf == 'matches' else '.json'))
            assert old_regular(p) and sha(p) == detail[leaf + '_sha256']


def archive():
    started, begin = now(), time.perf_counter()
    value = read(PLAN)
    verify_plan(value)
    protected, root_hashes, terminal = protection()
    assert root_hashes == value['protected_roots_sha256']
    assert terminal == value['terminal_source_sha256']
    assert protected == set(value['protected_paths'])
    proc = processes()
    files, skipped, saved = [], [], 0
    for row in value['candidates']:
        p = Path(row['original_path'])
        if str(p) in protected or active_campaign(row['campaign'], proc):
            skipped.append(dict(path=str(p), reason='protected_or_active'))
            continue
        stat = p.stat()
        assert old_regular(p) and stat.st_size == row['original_bytes'] and stat.st_mtime_ns == row['original_mtime_ns']
        assert sha(row['result_path']) == row['result_sha256']
        target = p.with_suffix('.jsonl.gz')
        if target.exists():
            skipped.append(dict(path=str(p), reason='existing_compressed_copy'))
            continue
        original = p.read_bytes()
        compressed = gzip.compress(original, compresslevel=6, mtime=0)
        with target.open('xb') as stream:
            stream.write(compressed)
            stream.flush()
            os.fsync(stream.fileno())
        restored = gzip.decompress(target.read_bytes())
        assert restored == original
        detail = dict(row, archived_path=str(target), archived_bytes=len(compressed),
                      original_sha256=digest(original), archived_sha256=digest(compressed))
        files.append(detail)
        saved += len(original) - len(compressed)
        if len(files) % 50 == 0:
            print(json.dumps(dict(time_utc=now(), compressed=len(files), prospective_saved_bytes=saved)), flush=True)
        if saved >= TARGET_SAVING:
            break
    verify_plan(value)
    proc = processes()
    assert not any(active_campaign(r['campaign'], proc) for r in files)
    manifest = dict(time_utc=now(), started_utc=started, files=files,
                    planned_target_saved_bytes=TARGET_SAVING, saved_bytes=saved,
                    original_bytes=sum(r['original_bytes'] for r in files),
                    archived_bytes=sum(r['archived_bytes'] for r in files),
                    plan_path=str(PLAN), plan_sha256=sha(PLAN),
                    archive_program_sha256=sha(PROGRAM),
                    restore_program_sha256=sha(E / 'restore_archived_replay.py'),
                    protected_roots_sha256=root_hashes, terminal_source_sha256=terminal,
                    protected_paths=value['protected_paths'],
                    closed_campaigns={n: value['closed_campaigns'][n] for n in sorted({r['campaign'] for r in files})},
                    exclusions=value['exclusions'], newly_skipped=skipped,
                    processes=public_processes(proc),
                    scope='Lossless gzip of closed pre-18:00 replay streams; restoration metadata published before unlink; no source/result/content edits.')
    atomic_json(MANIFEST, manifest, exclusive=True)
    # The durable manifest exists before any original is removed.
    for row in files:
        p, a = Path(row['original_path']), Path(row['archived_path'])
        assert p.stat().st_mtime_ns == row['original_mtime_ns']
        assert sha(p) == row['original_sha256'] and sha(a) == row['archived_sha256']
        p.unlink()
    verify_plan(value)
    assert all(not Path(r['original_path']).exists() and sha(r['archived_path']) == r['archived_sha256'] for r in files)
    finished = now()
    text = f'''# Closed replay archive 003

Started {started}; finished {finished}. Archived {len(files)} replay streams from {len(manifest['closed_campaigns'])} completed campaigns. Original bytes: {manifest['original_bytes']}; gzip bytes: {manifest['archived_bytes']}; saved bytes: {saved}. The requested target was {TARGET_SAVING} bytes. The retained plan records the eligible set and all exclusions.

Only replay streams and campaign summaries older than 2026-10-31T18:00:00Z were eligible. Jobs, root matches and successful summary counts were reconciled; each replay had a terminal result file. Campaigns with failures, recent files, existing gzip copies, protected references or active process references were excluded. Reserved campaigns were additionally excluded by name. All 85 terminal declaration source pins were verified before and after. Current O/P/Q/R/S, ten-policy and shortcut151/152 receipt closures were protected, including the old G/H and L/H controls and recent R/H, S/R, S/L and S/G records.

Every gzip stream was decompressed and compared byte for byte with its original before publication. Both SHA-256 hashes and sizes are in `archived-mature-replays-004.json`. That complete manifest was published before any original was unlinked. Original result files, matches, summaries, declarations and sources were unchanged. This is a storage operation, not a new policy run or game validation. The completion receipt verifies the archive files and removal state after publication.

Restore one named original from the project root when an older reader requires its uncompressed path:

```sh
PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 taskset -c 29 .venv/bin/python -B -m bot_research.experiments.validation.restore_archived_replay --manifest bot_research/runs/validation/archived-mature-replays-004.json --replay ORIGINAL_RELATIVE_PATH
```

Replace `ORIGINAL_RELATIVE_PATH` with one original_path entry. The existing helper verifies compressed and original hashes and refuses to overwrite an existing original. Restoring increases disk usage by the original size. Gzip-aware readers can consume the archived bytes directly. No JavaScript, server, cluster, remote compute or GPU was used.
'''
    with README.open('x') as stream:
        stream.write(text)
        stream.flush()
        os.fsync(stream.fileno())
    atomic_json(COMPLETION, dict(time_utc=finished, started_utc=started,
                                elapsed_seconds=time.perf_counter()-begin,
                                files=len(files), campaigns=len(manifest['closed_campaigns']),
                                saved_bytes=saved, manifest_sha256=sha(MANIFEST),
                                readme_sha256=sha(README),
                                terminal_pins_unchanged=len(terminal),
                                all_archives_verified=True, all_originals_removed=True,
                                all_protected_roots_unchanged=True), exclusive=True)
    print(json.dumps(read(COMPLETION)), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('plan', 'archive'))
    args = parser.parse_args()
    globals()[args.mode]()


if __name__ == '__main__':
    main()
