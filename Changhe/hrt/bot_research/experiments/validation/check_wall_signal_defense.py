"""Check fixed one-round defense proposals on selected signal-attack losses."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
import traceback

from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v38.fortress import make as make_fortress
from bot_research.bots.economy.frozen.v17.freeplan import free_plan
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.replay_audit import normalized

E = Path('bot_research/experiments/validation')
A = E / 'analysis/wall_signal_defense_diagnosis'


def main():
    declaration = json.loads((E / 'wall-signal-defense-001.json').read_text())
    inputs = declaration['input_sha256']
    def verify():
        for p, h in inputs.items():
            assert hashlib.sha256(Path(p).read_bytes()).hexdigest() == h, p
    verify()
    results = []
    for item in declaration['cases']:
        row = json.loads(Path(item['result']).read_text())
        side = row['condition']['candidate_side']
        assert side == 0 and row['condition']['opponent_id'] == 'H'
        assert not any(row['bot_errors']) and not any(row['rejected_actions'])
        records = [json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        audit = json.loads(Path(item['forecasts']).read_text())
        assert audit['all_passed']
        case = next(c for c in audit['cases'] if c['result_path'] == item['result'])
        rnd = next(i for i, h in enumerate(row['history'], 1)
                   if h['players'][side]['combat']['base_damage'] > 0)
        trace = case['rounds'][rnd - 1]
        assert trace['round'] == rnd and trace['model_matches']
        def replay_prefix():
            cfg = balanced_config()
            engine = Engine(cfg, tuple(row['bot_specs']))
            assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
            for r in range(1, rnd):
                pair = records[2*r:2*r+2]
                acts = [[e['action'] for e in p['event'] if e['kind'] == 'action'] for p in pair]
                assert normalized(engine.play_round(acts)) == pair
            return cfg, engine
        cfg, engine = replay_prefix()
        observation = engine.observation(side)
        original = records[2*rnd:2*rnd+2]
        original_actions = [[e['action'] for e in p['event'] if e['kind'] == 'action'] for p in original]
        assert trace['predicted_actions'] == original_actions[1-side]
        original_hp = observation['players'][side]['hp']
        assert normalized(engine.play_round(original_actions)) == original
        original_damage = original_hp - engine.observation(side)['players'][side]['hp']
        assert original_damage == trace['forecast_residual_damage'] > 0
        enemy = player_from_snapshot(observation['players'][1-side])
        assert all(apply_action(enemy, a, rnd, cfg)['accepted'] for a in trace['predicted_actions'])
        threat = [r.type for r in enemy.roster if r.active(rnd)]
        proposals = []
        for planner in ('free30', 'fortress38'):
            view = deepcopy(observation)
            start = time.perf_counter()
            if planner == 'free30':
                proposed = free_plan(view, view['players'][side]['gold'], [threat],
                                     partial='best', max_steps=30)
            else:
                proposed = make_fortress(attack='none', round1_poke=0, replan_iters=5000)(view)
            elapsed = time.perf_counter() - start
            assert view == observation
            actions = [a for a in proposed if a['op'] in ('build_wall', 'build_turret')]
            own = player_from_snapshot(observation['players'][side])
            checks = [apply_action(own, a, rnd, cfg) for a in actions]
            legal = all(e['accepted'] for e in checks)
            outcome = None
            if legal:
                _, alternative = replay_prefix()
                submissions = deepcopy(original_actions)
                submissions[side] = actions
                alternative_records = normalized(alternative.play_round(submissions))
                after = alternative.observation(side)
                outcome = dict(base_damage=original_hp-after['players'][side]['hp'],
                               round_records=alternative_records,
                               gold_after_actions=own.gold,
                               hp_after=after['players'][side]['hp'])
            proposals.append(dict(planner=planner, planning_seconds=elapsed,
                                  proposed_actions=proposed, construction_actions=actions,
                                  acceptance=checks, all_actions_legal=legal, outcome=outcome))
        result = dict(label=item['label'], result_path=item['result'], round=rnd,
                      observation=observation, available_gold=observation['players'][side]['gold'],
                      original_damage=original_damage, forecast_damage=trace['forecast_residual_damage'],
                      predicted_enemy_actions=trace['predicted_actions'], predicted_threat=threat,
                      proposals=proposals,
                      witness_found=any(p['all_actions_legal'] and p['outcome']['base_damage'] == 0
                                        for p in proposals))
        results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k not in
                         ('observation','proposals','predicted_enemy_actions')}), flush=True)
    verify()
    stamp = datetime.now(timezone.utc).isoformat()
    confirmed = all(r['witness_found'] for r in results)
    output = dict(time_utc=stamp, all_checks_completed=True,
                  hypothesis_verdict='CONFIRMED' if confirmed else 'OPEN',
                  cases=results, new_strength_games=0,
                  alternative_one_round_checks=sum(p['all_actions_legal'] for r in results for p in r['proposals']),
                  input_sha256=inputs)
    atomic_json(A/'verification/feasibility.json', output, exclusive=True)
    lines = ['# First-leak defense witnesses', '', f'Checked {stamp}.', '',
             'Existential defense claim: ' + output['hypothesis_verdict'] + '.', '',
             '| Selected attack | Round | Available gold | Original damage | Planner | Legal | Construction cost | Alternative damage | Seconds |',
             '|---|---:|---:|---:|---|---|---:|---:|---:|']
    for r in results:
        for p in r['proposals']:
            o = p['outcome']
            cost = r['available_gold']-o['gold_after_actions'] if o else None
            damage = o['base_damage'] if o else None
            lines.append(f'| {r["label"]} | {r["round"]} | {r["available_gold"]} | {r["original_damage"]} | {p["planner"]} | {p["all_actions_legal"]} | {cost} | {damage} | {p["planning_seconds"]:.6f} |')
    lines += ['', 'Every original prefix and selected round reproduces exactly in the unchanged Engine. '
              'Every recorded private H prediction matches the actual opponent action list, and its positive residual-damage prediction equals the original received damage. '
              'The table tests the construction projection of each proposal from the same public state. All full proposals, action acceptance records, observations and alternative round records are retained.', '',
              'A zero-damage row is a legal one-round feasibility witness, not a winning complete policy. '
              'If no row succeeds for a state, the existential claim remains open because these searches are not exhaustive. '
              'No new full strength game was run. The original wall-signal losses and delayed-grid results are unchanged. '
              'These selected failure states do not estimate an average repair rate or a general advantage of one planner.', '',
              'Reproduce with python -B -m bot_research.experiments.validation.check_wall_signal_defense after restoring the pinned sources and original replays. '
              'The exclusive result paths must first be archived or a separate reproduction directory used.', '']
    with (A/'RESULTS.md').open('x') as f:
        f.write('\n'.join(lines))
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: First-leak defense diagnosis complete\n\nClaim: the first leak at each of three selected twenty-wall failure states can be prevented within the same gold against the same H action list. Method: exact original-prefix replay plus the two declared construction planners, six one-round interventions. Result: {sum(r["witness_found"] for r in results)} of three states have a zero-damage witness; original private predictions and positive residual damage are exact in all three. Verdict: {output["hypothesis_verdict"]}. This is conditional one-round feasibility, with zero new full strength games. Evidence: experiments/validation/analysis/wall_signal_defense_diagnosis/RESULTS.md.\n')
    print(json.dumps(dict(time_utc=stamp, verdict=output['hypothesis_verdict'], states=len(results),
                          alternative_rounds=output['alternative_one_round_checks'])), flush=True)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(public_diagnostic(traceback.format_exc()), flush=True)
        raise SystemExit(1)
