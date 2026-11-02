"""Fresh HP-handoff shadows on recorded public histories, with original replay."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse
import hashlib
import json
import time

from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.hp_handoff import HPHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--campaigns', nargs='+', required=True)
    p.add_argument('--candidate-ids', nargs='+', required=True)
    p.add_argument('--opponent-ids', nargs='+')
    p.add_argument('--expected', type=int, required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    start = time.perf_counter()
    digest = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
    hashes = {str(f): digest(f) for f in static_closure(
        {'bot_research.experiments.validation.check_hp_handoff_histories'})}
    cases = []
    for directory in args.campaigns:
        root = Path(directory)
        for f, h in json.loads((root / 'freeze.json').read_text())['source_sha256'].items():
            assert digest(f) == h
            if f in hashes:
                assert hashes[f] == h
            hashes[f] = h
        jobs = root / 'jobs.json'
        hashes[str(jobs)] = digest(jobs)
        for job in json.loads(jobs.read_text()):
            c = job['condition']
            if c['candidate_id'] not in args.candidate_ids:
                continue
            if args.opponent_ids and c['opponent_id'] not in args.opponent_ids:
                continue
            path = root / 'results' / (job['id'] + '.json')
            checked_row(str(path), hashes)
            row = json.loads(path.read_text())
            records = [json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
            side = 1 - c['candidate_side']
            cfg = balanced_config()
            engine = Engine(cfg, tuple(row['bot_specs']))
            assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
            spec = c['opponent_spec']
            assert spec.split(':')[0] == 'bot_research.bots.counters.hp_handoff'
            params = {k: json.loads(v[0]) for k, v in parse_qs(spec.partition('?')[2]).items()}
            policy = HPHandoff(**params)
            differences, times, attack_rounds = [], [], []
            for rnd in range(1, row['rounds'] + 1):
                obs = engine.observation(side)
                saved = deepcopy(obs)
                t = time.perf_counter()
                fresh = policy.decide(obs)
                times.append(time.perf_counter() - t)
                assert obs == saved
                state = player_from_snapshot(obs['players'][side])
                assert all(apply_action(state, a, rnd, cfg)['accepted'] for a in fresh)
                if policy.switched and any(a['op'] == 'buy_minion' for a in fresh):
                    attack_rounds.append(rnd)
                pair = records[2*rnd:2*rnd+2]
                actual = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
                if fresh != actual[side]:
                    differences.append(dict(round=rnd, recorded_actions=actual[side], fresh_actions=fresh))
                assert normalized(engine.play_round(actual)) == pair
            assert engine.result == row['result']
            assert len(policy.switch_trace) <= 1
            cases.append(dict(condition=c, result=str(path), rounds=row['rounds'],
                              replayed=True, observations_unchanged=True, fresh_actions_legal=True,
                              switch_trace=policy.switch_trace,
                              internal_rejected_proposals=policy.rejected_proposals,
                              policy_action_differences=differences,
                              fresh_post_handoff_attack_rounds=attack_rounds,
                              decision_seconds=times))
            print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),
                                  finished=job['id'], candidate=c['candidate_id'],
                                  opponent=c['opponent_id'], switches=policy.switch_trace,
                                  differences=len(differences))), flush=True)
    assert len(cases) == args.expected
    assert all(digest(f) == h for f, h in hashes.items())
    out = dict(time_utc=datetime.now(timezone.utc).isoformat(),
               runtime_seconds=time.perf_counter()-start,
               all_replayed=True, all_observations_unchanged=True, all_fresh_actions_legal=True,
               exact_policy_reproduction=all(not c['policy_action_differences'] for c in cases),
               no_internal_rejections=all(not c['internal_rejected_proposals'] for c in cases),
               no_post_handoff_attacks=all(not c['fresh_post_handoff_attack_rounds'] for c in cases),
               input_sha256=hashes, cases=cases,
               scope='Fresh policies on recorded public observations. Original actions drive replay. '
                     'Clock-limited divergences are reported. This creates no independent strength sample.')
    atomic_json(args.output, out, exclusive=True)
    print(json.dumps({k: out[k] for k in ('time_utc', 'runtime_seconds', 'exact_policy_reproduction',
                                          'no_internal_rejections', 'no_post_handoff_attacks')}))


if __name__ == '__main__':
    main()
