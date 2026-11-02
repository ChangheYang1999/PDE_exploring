"""One fixed wall insertion before the public-budget defensive handoff."""
from copy import deepcopy
from dataclasses import asdict
from td_game.actions import apply_action
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.guarded_round4_trigger import GuardedRound4Trigger
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v7.plan import plan_walls


def snapshot_after_builds(snapshot, state, config):
    result = deepcopy(snapshot)
    result.update(gold=state.gold, buildings=[asdict(b) for b in state.buildings],
                  n_turrets=sum(b.type != 'wall' for b in state.buildings),
                  n_walls=sum(b.type == 'wall' for b in state.buildings))
    g = config.globals
    path = shortest_path(g.width, g.height, ((b.x, b.y) for b in state.buildings), g.spawn, g.base)
    if path is None:
        raise RuntimeError('Accepted construction unexpectedly lost the route.')
    result['length_path'] = len(path) - 1
    return result


class WalledHandoff(GuardedRound4Trigger):
    def __init__(self, wall_mode='full', **parameters):
        super().__init__(**parameters)
        if wall_mode not in ('none', 'stage_a', 'full'):
            raise ValueError('Unknown fixed wall mode.')
        self.wall_mode = wall_mode
        self.walls_attempted = False
        self.wall_trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        own, enemy = observation['players'][side], observation['players'][1-side]
        triggering = (self.triggered_round is not None or
            (rnd >= self.lead_from and own['hp'] > enemy['hp'] + self.lead_margin))
        if self.wall_mode == 'none' or self.walls_attempted or not triggering:
            return super().decide(observation)
        self.walls_attempted = True
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(own)
        stage = 0 if self.wall_mode == 'stage_a' else None
        proposed = plan_walls(deepcopy(observation), state.gold, stage=stage)
        walls = []
        for action in proposed:
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                walls.append(action)
            else:
                self.filtered_proposals.append(dict(round=rnd, action=action,
                    reason=event['reason'], stage='wall_filter'))
        hypothetical = deepcopy(observation)
        hypothetical['players'][side] = snapshot_after_builds(own, state, cfg)
        after = super().decide(hypothetical)
        self.trace[-1]['defense_cost'] += len(walls) * cfg.wall_cost
        self.trace[-1]['inserted_walls'] = len(walls)
        self.wall_trace.append(dict(round=rnd, actions=walls,
            route_before=own['length_path'], route_after=hypothetical['players'][side]['length_path']))
        return walls + after


def make(**parameters):
    return WalledHandoff(**parameters).decide
