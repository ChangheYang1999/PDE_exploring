"""Check plan guards, returned-value isolation and actual source decisions."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from bot_research.bots.counters.compiled_plan import CompiledPlan
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--plan', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    plan_path = Path(args.plan)
    plan_hash = hashlib.sha256(plan_path.read_bytes()).hexdigest()
    plan = json.loads(plan_path.read_text())
    source = Path(plan['source_result'])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == plan['source_result_sha256']
    row = json.loads(source.read_text())
    observations, actions = observations_and_actions(row, row['condition']['candidate_side'])
    checks = []
    for side in (0, 1):
        policy = CompiledPlan(args.plan, plan_hash, fallback='idle')
        for rnd, observation in sorted(observations.items()):
            obs = deepcopy(observation)
            if side != obs['player']:
                obs['players'].reverse()
                obs['player'] = side
            for player in obs['players']:
                player['name'] = 'renamed public label'
            result = policy.decide(obs)
            assert result == actions[rnd] and not policy.switched
            result.clear()
            assert policy.rounds[rnd]['actions'] == actions[rnd]
        checks.append({'test': 'renamed complete source decisions', 'side': side, 'passed': True})
    for field in ('hp', 'gold', 'n_factories'):
        policy = CompiledPlan(args.plan, plan_hash, fallback='idle')
        changed = deepcopy(observations[2])
        changed['players'][changed['player']][field] += 1
        assert policy.decide(changed) == [] and policy.switched
        assert policy.decide(observations[3]) == [] and policy.switched
        checks.append({'test': 'permanent departure guard', 'field': field, 'passed': True})
    policy = CompiledPlan(args.plan, plan_hash, fallback='idle')
    changed = deepcopy(observations[2])
    changed['rules']['globals']['max_rounds'] += 1
    assert policy.decide(changed) == [] and policy.switched
    checks.append({'test': 'rules guard', 'passed': True})
    try:
        CompiledPlan(args.plan, '0' * 64, fallback='idle')
    except ValueError:
        checks.append({'test': 'data digest guard', 'passed': True})
    else:
        raise AssertionError('Wrong data digest accepted.')
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'plan': str(plan_path), 'plan_sha256': plan_hash, 'checks': checks,
              'scope': 'Plan guard checks; actual fresh games remain a separate test.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'passed': len(checks), 'plan_sha256': plan_hash}))


if __name__ == '__main__':
    main()
