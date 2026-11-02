"""Compare old and emergency round-five actions on exact anonymous-prefix histories."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.emergency_route_selector import EmergencyRouteSelector
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    root = Path('bot_research/runs/validation/prefix-fork-001')
    area = Path('bot_research/experiments/validation/analysis/emergency_after_strike')
    inputs = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_emergency_component'})}
    inputs[str(area/'PROOF.md')] = digest(area/'PROOF.md')
    results = []
    for job in json.loads((root/'jobs.json').read_text()):
        c = job['condition']
        if c['opponent_id'] != 'route_adaptive':
            continue
        path = root/'results'/(job['id']+'.json')
        checked_row(str(path), inputs)
        row = json.loads(path.read_text())
        records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        side = 1-c['candidate_side']
        for rule in ('none', 'damage'):
            engine = Engine(balanced_config(), tuple(job['names']))
            policy = EmergencyRouteSelector(emergency_rule=rule)
            assert normalized(engine.initial_records(tuple(job['names']))) == records[:2]
            for rnd in range(1, 5):
                pair = records[2*rnd:2*rnd+2]
                actions = [[e['action'] for e in rec['event'] if e['kind'] == 'action'] for rec in pair]
                obs = engine.observation(side); saved = deepcopy(obs)
                assert policy.decide(obs) == actions[side] and obs == saved
                assert normalized(engine.play_round(actions)) == pair
            obs = engine.observation(side); saved = deepcopy(obs)
            actions = policy.decide(obs)
            assert obs == saved
            state = player_from_snapshot(obs['players'][side])
            assert all(apply_action(state, a, 5, engine.config)['accepted'] for a in actions)
            target_actions = [e['action'] for e in records[10+(1-side)]['event'] if e['kind'] == 'action']
            submitted = [target_actions, target_actions]
            submitted[side] = actions
            pair = normalized(engine.play_round(submitted))
            if rule == 'none':
                assert pair == records[10:12]
            result = dict(target=c['candidate_id'], candidate_side=c['candidate_side'], rule=rule,
                hp_before=[p['hp'] for p in obs['players']], hp_after=[p['snapshot']['hp'] for p in pair],
                actions=actions, target_actions=target_actions,
                incoming_damage=next(e['base_damage'] for e in pair[side]['event'] if e['kind'] == 'combat'),
                outgoing_damage=next(e['base_damage'] for e in pair[1-side]['event'] if e['kind'] == 'combat'),
                emergency_check=policy.early.emergency_checks[-1], selected=policy.selected,
                trigger_round=policy.early.triggered_round, old_prefix_exact=True, observations_unchanged=True,
                actions_legal=True, original_engine_combat=True)
            results.append(result)
    assert len(results) == 8
    for side in (0, 1):
        old = next(r for r in results if r['target'] == 'flood' and r['candidate_side'] == side and r['rule'] == 'none')
        new = next(r for r in results if r['target'] == 'flood' and r['candidate_side'] == side and r['rule'] == 'damage')
        assert new['incoming_damage'] < old['incoming_damage'] and new['emergency_check']['emergency_activated']
    assert all(digest(p) == h for p, h in inputs.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), input_sha256=inputs, results=results,
                  all_passed=True, scope='One-round counterfactual at reached round-five states only; no full-game conclusion.')
    atomic_json(area/'verification/component.json', output, exclusive=True)
    print(json.dumps(output, sort_keys=True))


if __name__ == '__main__':
    main()
