"""Offline source/JSON/exact-arithmetic audit. Never imports or calls a game policy.

Run from the project root. Writes only the explicitly requested JSON receipt.
Existing result bytes, logs and all project source files are read-only inputs.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import itertools
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

RESULT = Path('bot_research/runs/lead/frr1/results.jsonl')
EXPECTED_RESULT_HASH = '2df0933ba2f8872c064d5edbfd1640d07713c3335a107b4e2aa0de9350113b00'
NAMES = ['best_v9e', 'best_v9f', 'af2g', 'P5TNUBM', 'v41', 'V29', 'g1', 'guard00', 'threat_defender', 'AS1C']
E29 = 'bot_research.bots.economy.frozen.v29.econ29:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400&replan_base=true&own_in_layout="replan"&own_min_s=1200&min_cap=3000&active_cap=4000&fill=true&fill_reserve=true&fill_threat=true'
SPECS = [
 'bot_research.experiments.lead.frozen.best_v9e:@make',
 'bot_research.experiments.lead.frozen.best_v9f:@make',
 'bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null',
 'bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5',
 'bot_research.bots.defense.frozen.v41.fortress:@make', E29, E29 + '&attack_from=7',
 'bot_research.bots.counters.early_wall_guard:@make?witness="guard00"',
 'bot_research.harness.baselines:@threat_defender',
 'bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5',
]


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def module_file(name):
    base = Path(*name.split('.'))
    for path in (base.with_suffix('.py'), base / '__init__.py'):
        if path.is_file():
            return path
    return None


def static_files(spec):
    """Reconstruct match.py's static bot_research digest definition without imports."""
    seen = {}
    todo = [spec.partition(':')[0]]
    while todo:
        name = todo.pop()
        if name in seen or not name.startswith('bot_research'):
            continue
        path = module_file(name)
        if path is None:
            continue
        seen[name] = path
        parts = name.split('.')
        todo.extend('.'.join(parts[:i]) for i in range(1, len(parts)))
        package = name if path.name == '__init__.py' else '.'.join(parts[:-1])
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, ast.Import):
                todo.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    parts = package.split('.')
                    target = '.'.join(parts[:len(parts) - node.level + 1] + ([node.module] if node.module else []))
                else:
                    target = node.module or ''
                todo.append(target)
                todo.extend(target + '.' + a.name for a in node.names)
    return set(seen.values()) | set(Path('bot_research/harness').glob('*.py'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    output = Path(args.output)
    allowed = Path('bot_research/experiments/validation/analysis/frr1_equilibrium/verification').resolve()
    assert output.resolve().parent == allowed and not output.exists()
    started = stamp()
    assert sha(RESULT) == EXPECTED_RESULT_HASH
    rows = [json.loads(s) for s in RESULT.read_text().splitlines()]
    expected = [(i, side, (a, b) if side == 0 else (b, a))
                for i, (a, b) in enumerate(itertools.combinations(SPECS, 2)) for side in (0, 1)]
    actual = [(r['pair'], r['candidate_side'], (r['spec_a'], r['spec_b'])) for r in rows]
    assert len(rows) == 90 and sorted(actual) == sorted(expected)
    assert all(r['error'] is None and r['source_changed'] is False and r['scenario'] is None
               and r['experiment'] == 'frr1' and r['scenario_errors'] == [[], []] for r in rows)
    assert all(p['n_rejected'] == 0 and not p['rejected'] and not p['bot_errors']
               for r in rows for p in r['players'])
    source_sets = defaultdict(set)
    for row in rows:
        for path, digest in row['sources'].items():
            source_sets[path].add(digest)
    assert all(len(v) == 1 for v in source_sets.values())
    loaded_sources = {p: next(iter(v)) for p, v in sorted(source_sets.items())}
    assert all(sha(p) == h for p, h in loaded_sources.items())
    versions = {}
    entries = {}
    static_sources = {}
    for name, spec in zip(NAMES, SPECS):
        files = sorted(static_files(spec))
        source_map = {p.as_posix(): sha(p) for p in files}
        static_sources.update(source_map)
        digest = hashlib.sha256(''.join(p + '\0' + h + '\n' for p, h in source_map.items()).encode()).hexdigest()
        assert {r['version_' + k] for r in rows for k in 'ab' if r['spec_' + k] == spec} == {digest}
        entry = module_file(spec.partition(':')[0]).as_posix()
        assert {r['hash_' + k] for r in rows for k in 'ab' if r['spec_' + k] == spec} == {sha(entry)}
        versions[name] = digest
        entries[name] = {'spec': spec, 'entry': entry, 'sha256': sha(entry)}
    ids = {s: i for i, s in enumerate(SPECS)}
    matrix = [[0 for _ in NAMES] for _ in NAMES]
    hp = {}
    standings = {n: Counter() for n in NAMES}
    paths = [Path(r['log']) for r in rows]
    assert len(set(paths)) == 90 and set(paths) == set(paths[0].parent.iterdir())
    balanced_path = Path('td_game/balanced.json')
    balanced = json.loads(balanced_path.read_text())
    expected_initial = {'hp': 800, 'gold': 100, 'n_factories': 0, 'n_turrets': 0,
                        'n_walls': 0, 'length_path': 22, 'buildings': [], 'roster': []}
    logs = {}
    events = Counter()
    record_count = 0
    for row, path in zip(rows, paths):
        i, j = ids[row['spec_a']], ids[row['spec_b']]
        score = 0 if row['winner'] is None else 1 if row['winner'] == 0 else -1
        assert row['winner'] is None or type(row['winner']) is int and row['winner'] in (0, 1)
        matrix[i][j] = score
        hp[i, j] = row['hp_diff_a']
        for side, index, outcome in ((0, i, score), (1, j, -score)):
            standings[NAMES[index]][{1: 'W', 0: 'D', -1: 'L'}[outcome]] += 1
        raw = path.read_bytes()
        logs[path.as_posix()] = hashlib.sha256(raw).hexdigest()
        records = [json.loads(s) for s in raw.splitlines()]
        record_count += len(records)
        assert [(x['round'], x['player']) for x in records] == [
            (r, side) for r in range(row['rounds'] + 1) for side in (0, 1)]
        assert all(x['schema_version'] == 1 for x in records)
        assert all('result' not in x for x in records[:-2])
        for side, key in enumerate('ab'):
            first, last = records[side], records[-2 + side]
            match = first['match']
            assert match == records[1 - side]['match']
            assert match['research_specs'] == match['bots'] == [row['spec_a'], row['spec_b']]
            assert match['research_scenario'] is None
            assert match['research_metadata'] == row['metadata'] == {
                'pair': row['pair'], 'candidate_side': row['candidate_side']}
            assert match['rules'] == balanced
            assert match['action_order'] == 'A[0], B[0], A[1], B[1], ...'
            assert match['neighbor_order'] == ['right', 'down', 'left', 'up']
            assert match['tick_order'] == ['spawn', 'move older minions', 'base hits', 'turrets', 'remove dead']
            assert first['event'] == [{'kind': 'initial'}]
            assert {k: v for k, v in first['snapshot'].items() if k != 'name'} == expected_initial
            assert all(x['snapshot']['name'] == row['spec_' + key] for x in records if x['player'] == side)
            assert last['result'] == {'winner': row['winner'], 'reason': row['reason']}
            assert last['snapshot']['hp'] == row['hp_' + key] == row['players'][side]['hp']
            assert all(last['snapshot'][k] == row['players'][side][k] for k in (
                'name', 'gold', 'n_factories', 'n_turrets', 'n_walls', 'length_path'))
        assert row['hp_diff_a'] == row['hp_a'] - row['hp_b']
        a, b = row['hp_a'], row['hp_b']
        if a <= 0 and b <= 0:
            result = {'winner': None, 'reason': 'both_bases_destroyed'}
        elif min(a, b) <= 0:
            result = {'winner': 0 if b <= 0 else 1, 'reason': 'base_destroyed'}
        else:
            assert row['rounds'] == 50
            result = {'winner': None if a == b else 0 if a > b else 1, 'reason': 'round_limit'}
        assert result == records[-1]['result']
        for record in records:
            for event in record['event']:
                events[event['kind']] += 1
                assert event['kind'] != 'bot_error'
                if event['kind'] == 'action':
                    assert event['accepted'] is True
        assert path.name.startswith('20261031T213053-')
        assert int(path.name.split('-')[1]) == row['pair'] * 2 + row['candidate_side'] + 1
    assert len(hp) == 90
    assert all(matrix[i][j] == -matrix[j][i] and hp[i, j] == -hp[j, i] for i, j in hp)
    assert all(sum(c.values()) == 18 for c in standings.values())
    out_path = Path('bot_research/runs/lead/frr1.out')
    lines = out_path.read_text().splitlines()
    assert len(lines) == 92 and lines[0] == '90 matches -> bot_research/runs/lead/frr1'
    assert [int(re.match(r'\[(\d+)/90\]', s).group(1)) for s in lines[1:-1]] == list(range(1, 91))
    assert all('ERROR' not in s for s in lines)
    assert lines[-1] == 'done in 2109.8s; summary at bot_research/runs/lead/frr1/summary.md'
    queue_path = Path('bot_research/runs/lead/queue_h15A.log')
    queue = queue_path.read_text()
    assert queue.count('start frr1 ') == queue.count('end frr1 ') == 1
    assert 'start frr1 2026-10-31T21:30:53Z' in queue and 'end frr1 exit 0 2026-10-31T22:06:03Z' in queue
    # Fraction arithmetic on all three vertices certifies the whole affine face.
    certificates = {}
    for support in ('AS1C', 'best_v9f', 'P5TNUBM'):
        p = [Fraction(1, 3) if n in ('g1', 'guard00', support) else Fraction(0) for n in NAMES]
        primal = [sum(p[i] * matrix[i][j] for i in range(10)) for j in range(10)]
        dual = [sum(matrix[i][j] * p[j] for j in range(10)) for i in range(10)]
        assert sum(p) == 1 and min(primal) == 0 and max(dual) == 0
        assert all(x == -y for x, y in zip(primal, dual))
        certificates[support] = {'mixture': list(map(str, p)), 'primal_column_scores': list(map(str, primal)),
                                 'dual_row_scores': list(map(str, dual))}
    strict_dual = [Fraction(v) for v in certificates['AS1C']['dual_row_scores']]
    excluded = [n for n, value in zip(NAMES, strict_dual) if value < 0]
    assert excluded == ['best_v9e', 'af2g', 'v41', 'V29', 'threat_defender']
    dominance = {}
    e = NAMES.index('best_v9e')
    for name in ('AS1C', 'best_v9f'):
        i = NAMES.index(name)
        delta = [matrix[i][j] - matrix[e][j] for j in range(10)]
        assert min(delta) >= 0 and max(delta) > 0
        dominance[name] = {n: v for n, v in zip(NAMES, delta) if v}
    references = ['bot_research/reports/REPORT.md', 'bot_research/runs/lead/frr1/summary.md',
                  'bot_research/experiments/lead/queue_h15.sh', 'bot_research/experiments/lead/rr_specs.sh',
                  'bot_research/tmp/rr_nash.py', 'bot_research/tmp/rr_table.py']
    # Current source pins are checked again at the end of this short, offline audit.
    combined = {**loaded_sources, **static_sources}
    assert all(sha(p) == h for p, h in combined.items())
    assert sha(RESULT) == EXPECTED_RESULT_HASH
    evidence = {
      'schema': 'frr1-equilibrium-independent-review-001', 'started_utc': started, 'finished_utc': stamp(),
      'model': 'GPT-6 Astra', 'role': 'hrt-w3 independent recorded-data and exact-matrix review',
      'methods': ['stdlib JSON parsing', 'static Python AST and file hashing', 'Fraction arithmetic'],
      'policy_imports_constructors_decisions_games_replays': 0,
      'input_hashes': {p: sha(p) for p in [str(RESULT), str(out_path), str(queue_path), str(balanced_path)] + references},
      'checker_sha256': sha(__file__), 'names': NAMES, 'policy_entries': entries,
      'matrix_row_payoff_WDL': matrix, 'diagonal': 'zero by symmetric empirical-matrix convention; no self-play measured',
      'maxmin_set': {'g1': '1/3', 'guard00': '1/3', 'AS1C_best_v9f_P5TNUBM_total': '1/3',
                     'remaining_policies': '0', 'three_free_weights': 'each nonnegative'},
      'value': '0', 'primal_dual_vertex_certificates': certificates,
      'strict_dual_excludes': excluded, 'weak_dominance_differences': dominance,
      'proof_of_necessity': 'PROOF.md supplies the argument; vertex feasibility alone does not prove necessity.',
      'loaded_sources': loaded_sources, 'static_digest_sources': static_sources,
      'recorded_spec_versions': versions, 'combined_source_count': len(combined),
      'loaded_source_count': len(loaded_sources), 'static_source_count': len(static_sources),
      'all_current_source_identity_checks_passed': True,
      'log_hashes': dict(sorted(logs.items())), 'canonical_log_hashmap_sha256': hashlib.sha256(canonical(logs)).hexdigest(),
      'rules_canonical_sha256': hashlib.sha256(canonical(balanced)).hexdigest(),
      'initial_snapshot_without_name_canonical_sha256': hashlib.sha256(canonical(expected_initial)).hexdigest(),
      'matches': 90, 'unordered_pairs': 45, 'ordered_seats_per_pair': 2, 'self_play_games': 0,
      'records': record_count, 'events': dict(events), 'standings': {n: dict(c) for n, c in standings.items()},
      'error_failed_or_incomplete_retained_attempts': 0, 'rejected_actions': 0, 'bot_errors': 0,
      'source_changed_rows': 0, 'scenario_errors': 0, 'orphan_or_missing_match_logs': 0,
      'run_start_utc': '2026-10-31T21:30:53Z', 'run_end_utc': '2026-10-31T22:06:03Z',
      'queue_exit': 0, 'driver_wall_seconds_reported': '2109.8',
      'maximum_recorded_decide_seconds': max(d for r in rows for d in r['decide_max_seconds']),
      'limits': [
        'Recorded data were parsed and source identities checked; engine trajectories were not replayed.',
        'No independent process attempt journal exists here. Retained artifacts do not exclude erased or unrecorded attempts.',
        'Source before/after comparisons are harness records; current matching bytes do not prove absence of transient historical edits.',
        'Only one completed game per ordered pair was measured. There is no repeatability or population claim.',
        'The empirical matrix uses W/D/L only. Different diagonal or HP-payoff conventions define different games.',
        'The theorem concerns this ten-policy standard-start matrix, not the full tower-defense game.'
      ],
      'verdict': 'CONFIRMED for the defined recorded matrix',
    }
    with output.open('x') as stream:
        json.dump(evidence, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write('\n')
    print(json.dumps({'output': output.as_posix(), 'sha256': sha(output), 'finished_utc': evidence['finished_utc'],
                      'records': record_count, 'all_actions_accepted': events['action'], 'verdict': evidence['verdict']}))


if __name__ == '__main__':
    main()
