"""Recompute incoming damage after every submitted guarded-forecast action."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.guard_geometry import GuardGeometry
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_adaptive_attacks import combat
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    strict = json.loads(Path(args.strict_audit).read_text())
    inputs = {args.strict_audit: digest(args.strict_audit)}
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.audit_guarded_survival'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for case in strict['cases']:
        path = case['result_path']
        inputs[path] = digest(path)
        assert inputs[path] == strict['input_sha256'][path], 'Strict result bytes changed.'
        row = json.loads(Path(path).read_text())
        replay = row['replay_path']
        inputs[replay] = digest(replay)
        assert inputs[replay] == row['trajectory_sha256'], 'Replay bytes changed.'
        records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
        side = row['condition']['candidate_side']
        details = []
        assert len(row['forecast_trace']) == row['rounds']
        for trace in row['forecast_trace']:
            rnd = trace['round']
            before = [records[2*(rnd-1)+i]['snapshot'] for i in (0, 1)]
            after = [records[2*rnd+i]['snapshot'] for i in (0, 1)]
            actions = [[e['action'] for e in records[2*rnd+i]['event'] if e['kind'] == 'action'] for i in (0, 1)]
            assert trace['predicted_actions'] == actions[1-side], 'Opponent prediction differs.'
            config = config_from_dict(row['rules'])
            players = [player_from_snapshot(p) for p in before]
            for i in (0, 1):
                for action in actions[i]:
                    assert apply_action(players[i], action, rnd, config)['accepted'], 'Submitted action rejected.'
            incoming = combat(players[1-side], players[side], rnd, config)
            observed = before[side]['hp'] - after[side]['hp']
            assert incoming == observed, 'Original incoming combat differs from recorded HP change.'
            if rnd == 1:
                roster = [a['type'] for a in actions[side] if a['op'] == 'buy_minion']
                detail = trace['defense']
                opening = GuardGeometry(roster=roster, x=detail['x'], y=detail['y'])
                obs = dict(round=1, player=side, rules=row['rules'], players=deepcopy(before))
                assert opening.decide(obs) == actions[side], 'Prescribed first-round actions differ.'
                assert trace['forecast_residual_damage'] == incoming, 'Opening residual differs.'
            else:
                assert not any(a['op'] == 'buy_minion' for a in actions[side]), 'Unexpected later attack in a zero-share campaign.'
            residual = trace['forecast_residual_damage']
            details.append(dict(round=rnd, actual_incoming_damage=incoming,
                defense_residual_before_later_saturation=residual,
                residual_equals_final_damage=residual == incoming,
                false_zero_residual=residual == 0 and incoming > 0))
        opening_margin = records[2+side]['snapshot']['hp'] - records[2+1-side]['snapshot']['hp']
        margin = row['hp'][side] - row['hp'][1-side]
        cases.append(dict(result_path=path, condition=row['condition'],
            opening_hp_margin=opening_margin, final_hp_margin=margin,
            outcome=row['candidate_outcome'],
            no_incoming_after_opening=all(d['actual_incoming_damage'] == 0 for d in details[1:]),
            positive_opening_margin_remains_positive=opening_margin > 0 and margin > 0,
            rounds=details))
        print(json.dumps(dict(checked=case['job'], opening_margin=opening_margin,
            final_margin=margin, outcome=row['candidate_outcome'])), flush=True)
    assert all(digest(p) == h for p, h in {**inputs, **sources}.items()), 'Audit source or input changed.'
    false_zeros = sum(d['false_zero_residual'] for c in cases for d in c['rounds'])
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        source_sha256=sources, input_sha256=inputs, all_original_damage_checks_passed=True,
        false_zero_residual_rounds=false_zeros,
        residual_final_damage_disagreements=sum(not d['residual_equals_final_damage'] for c in cases for d in c['rounds']),
        cases=cases,
        scope='Original combat after all submitted actions agrees with every recorded incoming HP change. Guard openings are checked independently. The recorded defense residual is computed before any later saturation construction, so its equality with final damage is reported separately. No untested survival guarantee follows.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(games=len(cases), false_zero_residual_rounds=false_zeros,
        runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
