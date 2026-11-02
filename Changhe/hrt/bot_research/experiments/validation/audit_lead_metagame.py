"""Independently replay a complete lead round robin and export its exact game."""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.replay_audit import check, normalized
from bot_research.experiments.validation.source_closure import static_closure, module_file


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational(value):
    return {'numerator': value.numerator, 'denominator': value.denominator}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    path = Path(args.input)
    input_hashes = {str(path): sha(path)}
    sources = {str(p): sha(p) for p in static_closure({'bot_research.experiments.validation.audit_lead_metagame'})}
    sources['td_game/balanced.json'] = sha('td_game/balanced.json')
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    specs = sorted({r[s] for r in rows for s in ('spec_a', 'spec_b')})
    indices = {spec: i for i, spec in enumerate(specs)}
    versions, entries, pairs = defaultdict(set), defaultdict(set), defaultdict(list)
    cases = []
    for index, row in enumerate(rows):
        check(row['scenario'] is None, 'Only the declared standard initial state is supported.')
        check(not row.get('error') and not row['source_changed'], 'Match failure or source drift.')
        check(not any(row['scenario_errors']), 'Scenario errors in standard game.')
        check(all(not p['bot_errors'] and not p['rejected'] for p in row['players']), 'Invalid actions or bot errors.')
        for side in ('a', 'b'):
            spec = row['spec_' + side]
            versions[spec].add(row['version_' + side])
            entries[spec].add(row['hash_' + side])
            entry = str(module_file(spec.partition(':')[0]))
            check(row['sources'].get(entry) == row['hash_' + side], 'Missing or inconsistent bot entry attestation.')
        core = ('engine', 'combat', 'actions', 'config', 'state', 'pathfinding')
        for name in core:
            source = 'td_game/' + name + '.py'
            check(row['sources'].get(source) == sources[source], 'Engine source differs from recorded game.')
        replay = Path(row['log'])
        check(not replay.is_absolute() and '..' not in replay.parts and replay.parts[:1] == ('bot_research',),
              'Expected a project-relative replay path.')
        input_hashes[str(replay)] = sha(replay)
        records = [json.loads(line) for line in replay.read_text().splitlines()]
        check(len(records) == 2 * (row['rounds'] + 1), 'Incomplete replay.')
        names = (row['spec_a'], row['spec_b'])
        game = Engine(balanced_config(), names)
        initial = normalized(game.initial_records(names))
        extra = {'research_specs': list(names), 'research_scenario': None}
        if row.get('metadata'):
            extra['research_metadata'] = row['metadata']
        for record in initial:
            record['match'].update(extra)
        check(records[:2] == initial, 'Initial records differ.')
        for rnd in range(1, row['rounds'] + 1):
            pair = records[2 * rnd:2 * rnd + 2]
            check([r['round'] for r in pair] == [rnd, rnd] and [r['player'] for r in pair] == [0, 1],
                  'Round or assignment records differ.')
            check(game.result is None, 'Replay continues after terminal result.')
            actions = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
            check(all(not any(e['kind'] == 'bot_error' for e in r['event']) for r in pair), 'Bot error in replay.')
            check(normalized(game.play_round(actions)) == pair, 'Original engine disagrees with a recorded round.')
        check(game.result is not None, 'No terminal outcome.')
        check(game.result == {'winner': row['winner'], 'reason': row['reason']}, 'Outcome differs from lead row.')
        check([p.hp for p in game.players] == [row['hp_a'], row['hp_b']], 'Final HP differs.')
        check(row['hp_diff_a'] == row['hp_a'] - row['hp_b'], 'HP difference differs.')
        i, j = indices[row['spec_a']], indices[row['spec_b']]
        check(i != j, 'Expected only off-diagonal games.')
        payoff = 0 if row['winner'] is None else (1 if row['winner'] == 0 else -1)
        pairs[tuple(sorted((i, j)))].append((i, j, payoff))
        cases.append({'row': index, 'spec_a': row['spec_a'], 'spec_b': row['spec_b'],
                      'rounds': row['rounds'], 'hp': [row['hp_a'], row['hp_b']],
                      'result': game.result, 'replay_path': str(replay), 'passed': True})
        print(json.dumps({'replayed': index + 1, 'of': len(rows)}), flush=True)
    check(all(len(v) == 1 for v in versions.values()) and all(len(v) == 1 for v in entries.values()),
          'A policy changed version within the matrix.')
    n = len(specs)
    check(len(pairs) == n * (n - 1) // 2, 'Missing policy pairs.')
    matrix = [[Fraction(0) for _ in specs] for _ in specs]
    for (i, j), games in pairs.items():
        check(sorted((a, b) for a, b, _ in games) == [(i, j), (j, i)], 'Need exactly two assignments per pair.')
        matrix[i][j] = sum((Fraction(v if a == i else -v) for a, b, v in games), Fraction(0)) / 2
        matrix[j][i] = -matrix[i][j]
    changed = [p for p, h in sources.items() if sha(p) != h]
    check(not changed, 'Audit source changed.')
    output = {'time_utc': now(), 'runtime_seconds': time.perf_counter() - started,
              'source_sha256': sources, 'source_changed_during_run': changed, 'input_sha256': input_hashes,
              'policies': specs, 'versions': {k: next(iter(v)) for k, v in versions.items()},
              'entry_sha256': {k: next(iter(v)) for k, v in entries.items()},
              'matrix': [[rational(v) for v in row] for row in matrix], 'cases': cases,
              'all_replays_passed': True,
              'scope': 'Exact empirical payoff table from the recorded standard-condition games. Both assignments averaged; self-play diagonal is zero by symmetry. Not a full-game or future-performance guarantee.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'policies': n, 'games': len(cases), 'all_replays_passed': True}))


if __name__ == '__main__':
    main()
