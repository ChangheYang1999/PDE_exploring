"""Check each delayed signal's legal prefix and private-model agreement."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.wall_signal_delayed import DelayedWallSignal
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.artifact_io import atomic_json
E = Path('bot_research/experiments/validation')
A = E / 'analysis/wall_signal_delayed'


def main():
    declaration = json.loads((E / 'wall-signal-delayed-campaigns-001.json').read_text())
    inputs = declaration['input_sha256']
    verify = lambda: all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == h for p, h in inputs.items())
    assert verify()
    cases = []
    for campaign in declaration['campaigns']:
        for target in ('J', 'H', 'I'):
            for side in (0, 1):
                cfg = balanced_config()
                engine = Engine(cfg, ('a', 'b'))
                attacker = DelayedWallSignal(campaign['attack_round'], campaign['tier'])
                opponent = resolve(declaration['policies'][target])
                rounds = []
                for rnd in range(1, 9):
                    obs, other = engine.observation(side), engine.observation(1 - side)
                    saved = deepcopy((obs, other))
                    actions, answer = attacker.decide(obs), opponent.decide(other)
                    assert (obs, other) == saved
                    for view, acts in ((obs, actions), (other, answer)):
                        state = player_from_snapshot(view['players'][view['player']])
                        assert all(apply_action(state, action, rnd, cfg)['accepted'] for action in acts)
                    exact = attacker.trace[-1]['predicted_actions'] == answer
                    if target in ('H', 'J'):
                        assert exact
                    if rnd == 2:
                        assert obs['players'][side]['n_walls'] == 20 and not obs['players'][side]['roster']
                    pair = [None, None]
                    pair[side], pair[1 - side] = actions, answer
                    engine.play_round(pair)
                    rounds.append(dict(round=rnd, model_matches=exact, attacker_actions=actions))
                    if engine.result is not None:
                        break
                cases.append(dict(setting=campaign['label'], target=target, side=side, rounds=rounds))
    assert len(cases) == 24 and verify()
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), all_passed=True, cases=cases, input_sha256=inputs)
    atomic_json(A / 'verification/components.json', result, exclusive=True)
    print(json.dumps(dict(all_passed=True, cases=len(cases), checked_rounds=sum(len(c['rounds']) for c in cases))), flush=True)


if __name__ == '__main__':
    main()
