"""Check scenario repairs and cross-directory source-version accounting."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from copy import deepcopy

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.match import TimedBot
from bot_research.harness.scenarios import make_overrides
from bot_research.harness.baselines import random_legal
from bot_research.harness.tournament import summarize
from bot_research.experiments.validation.evaluate import source_hashes


def main():
    engine = Engine(balanced_config(), ('A', 'B'))
    def untouched(obs):
        return []
    def mutating(obs):
        obs['players'][obs['player']]['gold'] = 0
        return []
    def raising(obs):
        raise RuntimeError('intentional audit error')
    results = {}
    for name, fn in [('untouched', untouched), ('mutating', mutating), ('raising', raising)]:
        tested = TimedBot(fn, make_overrides('eco:1')[0])
        actions, errors = collect_actions([tested, TimedBot(untouched)],
                                         [engine.observation(p) for p in (0, 1)])
        results[name] = {'actions': actions[0], 'engine_errors': errors,
                         'scenario_errors': tested.scenario_errors}
        assert len(actions[0]) == 5
        assert not any(errors)
    assert len(results['raising']['scenario_errors']) == 1
    illegal = []
    for seed in range(100):
        obs = engine.observation(0)
        obs['players'][0]['gold'] = 1
        if any(a['op']=='buy_factory' for a in random_legal(seed)(obs)):
            illegal.append(seed)
    assert illegal == []
    # Synthetic summary inputs represent two completed batches with unchanged
    # entry-directory versions but distinct imported dependency versions.
    def row(dep_hash, scenario, win):
        stats = {'n_rejected': 0, 'bot_errors': []}
        return {'spec_a': 'example:decide', 'spec_b': 'other:decide',
                'version_a': 'same_entry_directory', 'version_b': 'same_other_directory',
                'sources': {'bot_research/bots/economy/plan.py': dep_hash},
                'candidate_side': 0, 'winner': win, 'scenario': scenario, 'rounds': 50,
                'hp_diff_a': 5 if win==0 else -5, 'players': [stats, stats],
                'decide_seconds': [0, 0], 'decide_max_seconds': [0, 0], 'reason': 'max_rounds'}
    grouped = summarize([row('first', None, 0), row('second', 'eco:1', 1)])
    merged_line = next(line for line in grouped.splitlines() if line.startswith('| example:decide | other:decide |'))
    assert '| 2 | 1 | 0 | 1 |' in merged_line
    output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'sources': source_hashes(),
              'scenario_checks': results, 'random_unaffordable_factory_seeds': illegal,
              'synthetic_different_dependencies_and_scenarios_summary': grouped,
              'summary_still_merges_different_dependencies_and_scenarios': True,
              'scope': 'repair checks and synthetic aggregation audit, not strength evidence'}
    with Path('bot_research/runs/validation/harness-audit-002.json').open('x') as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps({'scenario_repairs_pass': True, 'random_affordability_pass': True,
                      'summary_grouping_gap_reproduced': True}))


if __name__ == '__main__':
    main()
