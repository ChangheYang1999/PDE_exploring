"""Regenerate both policies and compare complete public prefixes without renaming."""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def value_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--expected', type=int, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    root = Path(args.campaign)
    hashes = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_prefix_fork'})}
    for p, h in json.loads((root/'freeze.json').read_text())['source_sha256'].items():
        assert digest(p) == h, p
        if p in hashes:
            assert hashes[p] == h
        hashes[p] = h
    hashes[str(root/'jobs.json')] = digest(root/'jobs.json')
    cases, prefix_groups = [], defaultdict(list)
    for job in json.loads((root/'jobs.json').read_text()):
        path = root/'results'/(job['id']+'.json')
        checked_row(str(path), hashes)
        row = json.loads(path.read_text())
        records = [json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        cfg = balanced_config()
        engine = Engine(cfg, tuple(job['names']))
        assert row['bot_specs'] == job['names']
        side = job['condition']['candidate_side']
        assert job['names'][side] == 'anonymous_target'
        assert job['names'][1-side] == 'anonymous_selector'
        assert normalized(engine.initial_records(tuple(job['names']))) == records[:2]
        policies = [resolve(description) for description in job['bots']]
        prefixes, differences, decisions = [], [], []
        for rnd in range(1, row['rounds']+1):
            observations = [engine.observation(i) for i in (0, 1)]
            if rnd <= 4:
                prefixes.append(deepcopy(observations))
            fresh = []
            for i in (0, 1):
                observation = observations[i]
                saved = deepcopy(observation)
                before = time.perf_counter()
                actions = policies[i].decide(observation)
                seconds = time.perf_counter()-before
                assert observation == saved
                state = player_from_snapshot(observation['players'][i])
                assert all(apply_action(state, action, rnd, cfg)['accepted'] for action in actions)
                fresh.append(actions)
                decisions.append(dict(round=rnd, player=i, decision_seconds=seconds, action_sha256=value_digest(actions)))
            pair = records[2*rnd:2*rnd+2]
            actual = [[e['action'] for e in rec['event'] if e['kind'] == 'action'] for rec in pair]
            for i in (0, 1):
                if fresh[i] != actual[i]:
                    differences.append(dict(round=rnd, player=i))
            assert normalized(engine.play_round(actual)) == pair
        assert engine.result == row['result']
        prefix_groups[side].append(dict(job=job['id'], observations=prefixes))
        cases.append(dict(job=job['id'], condition=job['condition'], result=str(path),
            prefix_sha256=value_digest(prefixes), differing_decisions=differences,
            decisions=decisions, observations_unchanged=True, fresh_actions_legal=True, original_engine_replay=True))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(), finished=job['id'], differences=differences)), flush=True)
    comparisons = []
    for side, group in sorted(prefix_groups.items()):
        assert len(group) == 6
        reference = group[0]
        for other in group[1:]:
            comparisons.append(dict(candidate_side=side, reference=reference['job'], other=other['job'],
                full_public_prefix_equal=reference['observations'] == other['observations']))
    assert len(cases) == args.expected
    assert all(digest(p) == h for p, h in hashes.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes, cases=cases, comparisons=comparisons,
        all_prefixes_equal=all(c['full_public_prefix_equal'] for c in comparisons),
        all_fresh_decisions_equal=all(not c['differing_decisions'] for c in cases),
        all_observations_unchanged=True, all_actions_legal=True, all_replayed=True,
        representative_full_public_prefixes={str(side): group[0] for side, group in prefix_groups.items()},
        scope='Full unchanged public observations, including names, before rounds1-4; fixed physical assignment; three selector modes and both hidden target continuations. Full-game fresh actions for both policies.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'runtime_seconds', 'all_prefixes_equal', 'all_fresh_decisions_equal')}), flush=True)
    assert output['all_prefixes_equal'] and output['all_fresh_decisions_equal']


if __name__ == '__main__':
    main()
