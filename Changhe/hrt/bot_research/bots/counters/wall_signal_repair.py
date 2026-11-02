"""Keep the signal/strike policy and repair strictly worse local defense plans."""
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.wall_signal_timing import WallSignalTiming
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v17.freeplan import free_plan
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate


class WallSignalRepair(WallSignalTiming):
    def __init__(self):
        super().__init__(wall_count=20)
        self.repair_trace = []

    def decide(self, observation):
        original = super().decide(observation)
        rnd, side = observation['round'], observation['player']
        trace = self.trace[-1]
        old_damage = trace['forecast_residual_damage']
        if rnd >= 4:
            cfg = config_from_dict(observation['rules'])
            predicted = player_from_snapshot(observation['players'][1-side])
            for action in trace['predicted_actions']:
                if not apply_action(predicted, action, rnd, cfg)['accepted']:
                    raise ValueError('Private forecast contains an illegal action.')
            active = [entry.type for entry in predicted.roster if entry.active(rnd)]
            normal = player_from_snapshot(observation['players'][side])
            for action in original:
                if not apply_action(normal, action, rnd, cfg)['accepted']:
                    raise ValueError('Original policy proposes an illegal action.')
            normal_map = MapModel([(b.x, b.y, b.type) for b in normal.buildings], observation['rules'])
            old_damage = simulate(normal_map, active, observation['rules'])[1]
            trace['forecast_residual_damage'] = old_damage
        detail = dict(round=rnd, original_predicted_damage=old_damage,
                      replacement_predicted_damage=None, selected=False,
                      proposed_construction=[], proposed_actions_legal=None)
        if rnd >= 4 and old_damage > 0:
            cfg = config_from_dict(observation['rules'])
            enemy = player_from_snapshot(observation['players'][1-side])
            for action in trace['predicted_actions']:
                if not apply_action(enemy, action, rnd, cfg)['accepted']:
                    raise ValueError('Private forecast contains an illegal action.')
            threat = [entry.type for entry in enemy.roster if entry.active(rnd)]
            own = player_from_snapshot(observation['players'][side])
            planned = free_plan(deepcopy(observation), own.gold, [threat],
                                partial='best', max_steps=30)
            checks = [apply_action(own, a, rnd, cfg)['accepted'] for a in planned]
            detail.update(proposed_construction=deepcopy(planned),
                          proposed_actions_legal=all(checks))
            if all(checks):
                model = MapModel([(b.x, b.y, b.type) for b in own.buildings], observation['rules'])
                residual = simulate(model, threat, observation['rules'])[1]
                detail['replacement_predicted_damage'] = residual
                if residual < old_damage:
                    original = list(planned)
                    if rnd < 48:
                        count = min(self.max_factories, own.gold // cfg.globals.factory_cost)
                        original += [{'op': 'buy_factory'}] * count
                    detail['selected'] = True
                    trace['forecast_residual_damage'] = residual
        self.repair_trace.append(detail)
        return original


def make():
    return WallSignalRepair().decide
