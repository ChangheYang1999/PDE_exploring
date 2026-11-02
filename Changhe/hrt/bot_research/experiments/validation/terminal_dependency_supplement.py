"""Seal omitted terminal dependencies without reading reserve parameters or calling bots.

Only the existing declaration and earlier receipt metadata are parsed. The
reserved manifest and prefix receipt are treated as opaque hashed bytes.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure

E = Path('bot_research/experiments/validation')
A = E / 'analysis/terminal_reserved_validation'
V = A / 'verification'
DECLARATION = E / 'terminal-candidate-declaration-001.json'
DECLARATION_SHA256 = '2b5fa9c56b6219233731c8559b012ff12ebe0be43b86395ebee4e51b8fa325e1'
CANDIDATE_SHA256 = '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87'
MANIFEST_SHA256 = '9267cb4367f21dc0a572594c3523a466769ef1ea3185beb4dd94d632270e07b7'
GATE = datetime.fromisoformat('2026-10-31T23:00:00+00:00')
SEAL = V / 'dependency_supplement_001.json'
ARCHIVE = V / 'dependency_supplement_sources'
DOCUMENT = A / 'DEPENDENCY_SUPPLEMENT.md'
REVIEW = E / 'reviews/terminal-readiness-review-2145.md'
MODULE_NAMES = (
    'run_terminal_pipeline', 'terminal_validation', 'audit_terminal_campaign',
    'audit_terminal_separation', 'audit_terminal_scenario_separation',
    'snapshot_audit_inputs', 'replay_campaign_bounded', 'replay_audit',
    'summarize_reserved_replays', 'render_terminal_summary',
    'diagnose_reserved_losses', 'audit_best_entrypoints_bounded',
    'check_best_entrypoints', 'summarize_entrypoint_audits',
    'publish_terminal_evidence', 'publish_terminal_validation', 'isolated_match',
    'terminal_logged', 'final_validation', 'terminal_dependency_supplement',
)
ROOTS = tuple(sorted({'bot_research.bots.best'} | {
    'bot_research.experiments.validation.' + name for name in MODULE_NAMES}))
PRIOR_RECEIPTS = (
    ('bot_research/runs/validation/saturation-ablation-001-shard0/freeze.json',
     '7946e651129b38b399bbd449659a69ed8e6a0c72e0d64face3679e4f92926a7e',
     'source_sha256', (
         'bot_research/experiments/validation/evaluate.py',
         'bot_research/experiments/validation/isolated_match.py',
         'bot_research/experiments/validation/final_validation.py',
         'td_bots/__init__.py', 'td_bots/protocol.py')),
    ('bot_research/runs/validation/projection-selector-b001/freeze.json',
     '7ebd198e7fc60988d7d92ed28b0ba749147fdd5ce736e4ec4a39bd198876c8d0',
     'source_sha256', (
         'bot_research/experiments/validation/compare_recorded_controls.py',
         'bot_research/experiments/validation/replay_audit.py')),
    ('bot_research/runs/validation/entrypoint-preflight-001/metadata.json',
     '5c236bebbd714431e7636382db54958eb13a200b24e4dca60c06e915656f0d55',
     'inputs', ('bot_research/experiments/validation/check_best_entrypoints.py',)),
)


def now():
    return datetime.now(timezone.utc)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_path(name):
    path = Path(name)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('Expected a project-relative path: ' + str(path))
    return path


def read_declaration():
    raw = DECLARATION.read_bytes()
    if digest(raw) != DECLARATION_SHA256:
        raise ValueError('Original declaration bytes changed.')
    d = json.loads(raw)
    if (d['candidate'] != 'bot_research.bots.best:decide'
            or d['candidate_sha256'] != CANDIDATE_SHA256
            or d['manifest_sha256'] != MANIFEST_SHA256
            or d['expected_conditions'] != 96
            or d['candidate_and_opponent_calls'] != 0
            or len(d['source_sha256']) != 85
            or datetime.fromisoformat(d['not_before_utc']) != GATE):
        raise ValueError('Original declaration metadata is inconsistent.')
    return d, raw


def current_closure(d):
    paths = set(static_closure(ROOTS))
    explicit = sorted(map(str, paths))
    paths.update(safe_path(p) for p in d['source_sha256'])
    raw = {str(p): p.read_bytes() for p in sorted(paths)}
    hashes = {p: digest(value) for p, value in raw.items()}
    for path, expected in d['source_sha256'].items():
        if hashes[path] != expected:
            raise ValueError('Original declaration source changed: ' + path)
    return explicit, raw, hashes


def preserve(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)
    if path.read_bytes() != raw:
        raise ValueError('Snapshot byte comparison failed: ' + str(path))


def prior_identities(source_hashes):
    rows, receipts = [], {}
    for name, expected, field, sources in PRIOR_RECEIPTS:
        path = safe_path(name)
        raw = path.read_bytes()
        if digest(raw) != expected:
            raise ValueError('Earlier receipt bytes changed: ' + name)
        receipt = json.loads(raw)
        stamp = receipt['started_utc']
        if datetime.fromisoformat(stamp) >= GATE:
            raise ValueError('Earlier receipt does not predate D gate.')
        receipts[name] = raw
        for source in sources:
            old = receipt[field][source]
            if old != source_hashes[source]:
                raise ValueError('Earlier source pin differs from current bytes: ' + source)
            original = path.parent / 'sources' / source if field == 'source_sha256' else None
            archived = original is not None and original.is_file()
            if archived and digest(original.read_bytes()) != old:
                raise ValueError('Earlier source archive differs from its receipt: ' + source)
            rows.append(dict(source=source, earlier_receipt=name,
                earlier_receipt_sha256=expected, map_field=field,
                recorded_utc=stamp, earlier_source_sha256=old,
                current_sha256=source_hashes[source], same_bytes=True,
                original_archive=str(original) if archived else None,
                original_archive_verified=archived))
    return rows, receipts


def seal():
    started = now()
    if started >= GATE:
        raise ValueError('A new pre-D supplement cannot be sealed after the gate.')
    if SEAL.exists() or ARCHIVE.exists():
        raise ValueError('Supplement or snapshot already exists; preserve it.')
    d, declaration_raw = read_declaration()
    explicit, raw, sources = current_closure(d)
    identities, receipts = prior_identities(sources)
    added = sorted(set(sources) - set(d['source_sha256']))
    supporting = {str(DECLARATION): declaration_raw,
                  str(DOCUMENT): DOCUMENT.read_bytes(),
                  str(REVIEW): REVIEW.read_bytes(), **receipts}
    ARCHIVE.mkdir(parents=True, exist_ok=False)
    source_archive, input_archive = {}, {}
    for name in added:
        target = ARCHIVE / 'current' / name
        preserve(target, raw[name])
        source_archive[name] = str(target)
    for name, value in supporting.items():
        target = ARCHIVE / 'inputs' / name
        preserve(target, value)
        input_archive[name] = str(target)
    for name, value in raw.items():
        if safe_path(name).read_bytes() != value:
            raise ValueError('Source changed during seal: ' + name)
    for name, value in supporting.items():
        if safe_path(name).read_bytes() != value:
            raise ValueError('Supporting input changed during seal: ' + name)
    completed = now()
    if completed >= GATE:
        raise ValueError('Snapshot did not finish before the D gate.')
    result = dict(schema=1, started_utc=started.isoformat(),
        sealed_utc=completed.isoformat(), not_before_utc=GATE.isoformat(),
        declaration=str(DECLARATION), declaration_sha256=DECLARATION_SHA256,
        original_declaration_source_count=85,
        original_declaration_source_sha256=d['source_sha256'],
        candidate_sha256=CANDIDATE_SHA256, manifest_sha256=MANIFEST_SHA256,
        policy_calls=0, game_calls=0, reserved_parameters_parsed=False,
        explicit_runtime_roots=list(ROOTS),
        explicit_local_python_source_paths=explicit,
        source_sha256=sources, newly_covered_files=added,
        source_archive=source_archive,
        input_sha256={p: digest(value) for p, value in supporting.items()},
        input_archive=input_archive, earlier_source_identities=identities,
        files_without_selected_earlier_pin=sorted(set(added) - {x['source'] for x in identities}),
        limits=[
            'This is a later pre-D seal. Declaration001 and its 85 pins are unchanged.',
            'Earlier matching receipts establish byte identity at those records, not continuous monitoring.',
            'Static closure requires explicitly declared subprocess roots and does not infer arbitrary computed imports.',
            'The reserved manifest and prefix evidence are hashed as opaque bytes; no reserve parameters are parsed.',
            'This supplements source provenance only. It neither runs nor substitutes for final games, replay, entry checks, or protected-file integrity.',
            'The existing pipeline does not import this supplement. Independent pre-D and post-D receipts must accompany its final evidence.',
        ])
    problems = verify_record(result, phase='pre-d')
    if problems:
        raise ValueError('Supplement did not self-verify: ' + repr(problems))
    atomic_json(SEAL, result, exclusive=True)
    print(json.dumps(dict(sealed_utc=result['sealed_utc'], seal=str(SEAL),
        seal_sha256=digest(SEAL.read_bytes()), source_files=len(sources),
        added_source_files=len(added), original_pins_verified=85,
        prior_matching_sources=len(identities), policy_calls=0)))


def verify_record(record, *, phase):
    """Return every detected mismatch; neither imports bots nor rewrites inputs."""
    problems = []

    def require(condition, message):
        if not condition:
            problems.append(message)

    try:
        d, _ = read_declaration()
        explicit, _, current = current_closure(d)
        require(record['schema'] == 1, 'Unsupported schema.')
        require(record['declaration'] == str(DECLARATION), 'Declaration path changed.')
        require(record['declaration_sha256'] == DECLARATION_SHA256, 'Declaration hash changed.')
        require(record['candidate_sha256'] == CANDIDATE_SHA256, 'Candidate hash changed.')
        require(record['manifest_sha256'] == MANIFEST_SHA256, 'Manifest hash changed.')
        require(record['not_before_utc'] == GATE.isoformat(), 'Gate changed.')
        sealed = datetime.fromisoformat(record['sealed_utc'])
        started = datetime.fromisoformat(record['started_utc'])
        require(started <= sealed < GATE, 'Seal was not completed before D gate.')
        require(sealed <= now(), 'Seal timestamp is in the future.')
        if phase == 'pre-d':
            require(now() < GATE, 'Pre-D verification is after D gate.')
        elif phase == 'post-d':
            require(now() >= GATE, 'Post-D verification is before D gate.')
        else:
            require(False, 'Unknown verification phase.')
        require(record['policy_calls'] == record['game_calls'] == 0,
                'Supplement has nonzero policy/game calls.')
        require(record['reserved_parameters_parsed'] is False, 'Reserved parameter flag changed.')
        require(record['original_declaration_source_count'] == 85, 'Original pin count changed.')
        require(record['original_declaration_source_sha256'] == d['source_sha256'],
                'Original pin map changed.')
        require(record['explicit_runtime_roots'] == list(ROOTS), 'Explicit subprocess roots changed.')
        require(record['explicit_local_python_source_paths'] == explicit, 'Static executable closure changed.')
        require(record['source_sha256'] == current, 'Sealed source map differs from current complete closure.')
        added = sorted(set(current) - set(d['source_sha256']))
        require(record['newly_covered_files'] == added, 'Newly covered source list changed.')
        require(set(record['source_archive']) == set(added), 'Source snapshots are incomplete.')
        for name, archive in record['source_archive'].items():
            require(safe_path(archive) == ARCHIVE / 'current' / name,
                    'Unexpected source snapshot path: ' + name)
            require(digest(safe_path(archive).read_bytes()) == current[name],
                    'Source snapshot changed: ' + name)
        expected_inputs = {str(DECLARATION), str(DOCUMENT), str(REVIEW)} | {r[0] for r in PRIOR_RECEIPTS}
        require(set(record['input_sha256']) == expected_inputs, 'Supporting input set changed.')
        require(set(record['input_archive']) == expected_inputs, 'Supporting snapshots are incomplete.')
        for name, expected in record['input_sha256'].items():
            require(digest(safe_path(name).read_bytes()) == expected, 'Supporting input changed: ' + name)
            archive = safe_path(record['input_archive'][name])
            require(archive == ARCHIVE / 'inputs' / name, 'Unexpected input snapshot path: ' + name)
            require(digest(archive.read_bytes()) == expected, 'Supporting snapshot changed: ' + name)
        identities, _ = prior_identities(current)
        require(record['earlier_source_identities'] == identities, 'Earlier source identity evidence changed.')
        require(record['files_without_selected_earlier_pin'] ==
                sorted(set(added) - {x['source'] for x in identities}),
                'Unmatched earlier-pin accounting changed.')
    except (KeyError, TypeError, ValueError, OSError) as error:
        problems.append(public_diagnostic(type(error).__name__ + ': ' + str(error)))
    return problems


def verify(phase, output):
    output = safe_path(output)
    if (output.parent != V or not output.name.startswith('dependency_supplement_')
            or output.suffix != '.json' or output == SEAL):
        raise ValueError('Verification output must be a new dependency_supplement_*.json receipt.')
    raw = SEAL.read_bytes()
    record = json.loads(raw)
    problems = verify_record(record, phase=phase)
    receipt = dict(time_utc=now().isoformat(), phase=phase, all_passed=not problems,
        seal=str(SEAL), seal_sha256=digest(raw), declaration_sha256=DECLARATION_SHA256,
        original_pins_verified=85 if not problems else None,
        source_files_verified=len(record['source_sha256']) if not problems else None,
        source_snapshot_count=len(record['source_archive']),
        earlier_identity_count=len(record['earlier_source_identities']),
        policy_calls=0, game_calls=0, reserved_parameters_parsed=False,
        issues=problems, verifier_sha256=digest(Path(__file__).read_bytes()),
        scope='Current and archived source identity. Post-D phase labels time after the gate; it does not assert that D games completed.')
    atomic_json(output, receipt, exclusive=True)
    print(json.dumps(receipt))
    return 0 if not problems else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('seal')
    check = commands.add_parser('verify')
    check.add_argument('--phase', choices=('pre-d', 'post-d'), required=True)
    check.add_argument('--output', required=True)
    args = parser.parse_args()
    if args.command == 'seal':
        seal()
        return 0
    return verify(args.phase, args.output)


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (KeyError, TypeError, ValueError, OSError) as error:
        print(json.dumps(dict(error=public_diagnostic(type(error).__name__ + ': ' + str(error)))))
        raise SystemExit(2)
