"""Verify fixed-schedule forecast removal on recorded, replay-checked states."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import parse_qs
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.guarded_schedule import GuardedSchedule
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.threat import active_types
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.final_validation_strict import read_result
from bot_research.experiments.validation.replay_audit import audit_row
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', required=True, nargs='+')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rows = []
    inputs = {}
    for filename in args.results:
        path = Path(filename)
        directory = path.parent.parent
        metadata = json.loads((directory/'freeze.json').read_text())
        job = json.loads((directory/'jobs'/(path.stem+'.json')).read_text())
        row = read_result(path, job, metadata['source_sha256'])
        assert not any(row['bot_errors']) and not any(row['rejected_actions'])
        assert not row['source_changed_during_match']
        replay_check = audit_row(row)
        side = row['condition']['candidate_side']
        observations, submitted = observations_and_actions(row, side)
        _, enemy_submitted = observations_and_actions(row, 1-side)
        query = parse_qs(row['condition']['candidate_spec'].partition('?')[2])
        parameters = {k: json.loads(v[0]) for k,v in query.items()
                      if k not in ('model_spec', 'model_parameters')}
        policy = GuardedSchedule(**parameters)
        prediction = {r['round']:r['predicted_actions'] for r in row['forecast_trace']}
        mismatches, threat_mismatches = [], []
        decision_seconds = 0
        for rnd, observation in observations.items():
            assert prediction[rnd] == enemy_submitted[rnd]
            cfg = config_from_dict(observation['rules'])
            enemy = player_from_snapshot(observation['players'][1-side])
            for action in prediction[rnd]:
                assert apply_action(enemy, action, rnd, cfg)['accepted']
            forecast = [entry.type for entry in enemy.roster if entry.active(rnd)]
            visible = list(policy.initial_threat) if rnd == 1 else active_types(observation['players'][1-side]['roster'], rnd)
            if forecast != visible:
                threat_mismatches.append(rnd)
            untouched = deepcopy(observation)
            start = time.perf_counter()
            actual = policy.decide(observation)
            decision_seconds += time.perf_counter() - start
            assert observation == untouched
            if actual != submitted[rnd]:
                mismatches.append(rnd)
        assert not mismatches and not threat_mismatches, (filename,mismatches,threat_mismatches)
        for source in (path,directory/'freeze.json',directory/'jobs'/(path.stem+'.json'),Path(row['replay_path'])):
            inputs[str(source)] = digest(source)
        rows.append({'source_result':filename, 'source_condition':row['condition'],
                     'evidence_type':'deduced_identical_trajectory', 'rounds_checked':len(observations),
                     'threat_mismatch_rounds':threat_mismatches, 'action_mismatch_rounds':mismatches,
                     'replay_audit':replay_check, 'guarded_schedule_parameters':parameters,
                     'decision_seconds_observed_on_recorded_states':decision_seconds,
                     'source_counter_decision_seconds':row['decision_seconds'][side],
                     'hp_candidate_first':row['hp'][::1 if side==0 else -1]})
    sources = set(static_closure({'bot_research.experiments.validation.check_visible_schedule'}))
    output = {'time_utc':now(), 'all_passed':True, 'cases':rows, 'input_sha256':inputs,
              'source_sha256':{str(p):digest(p) for p in sorted(sources)},
              'scope':'Exact action-equality certificates on fully replayed source histories. These are deductions of existing trajectories, not additional independently played matches.'}
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({'all_passed':True,'cases':len(rows),'rounds_checked':sum(r['rounds_checked'] for r in rows)}))


if __name__ == '__main__':
    main()
