"""A prescribed cheap guard, then defense against a public-policy clone.

The clone is advanced in round one even though its predicted actions do not
choose that round's guard. Later decisions use FreeForecast unchanged.
"""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.free_forecast import FreeForecast
from bot_research.bots.counters.guard_geometry import GuardGeometry
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types


class GuardedForecast(FreeForecast):
    def __init__(self, roster=('tier1',), x=10, y=1, **parameters):
        parameters.setdefault('attack_share', 0)
        super().__init__(**parameters)
        self.opening = GuardGeometry(roster=roster, x=x, y=y)

    def decide(self, observation):
        if observation['round'] != 1:
            return super().decide(observation)
        predicted, enemy = predict(observation, self.model)
        actions = self.opening.decide(observation)
        side, rules = observation['player'], observation['rules']
        own = player_from_snapshot(observation['players'][side])
        config = config_from_dict(rules)
        for action in actions:
            if not apply_action(own, action, 1, config)['accepted']:
                raise ValueError('The prescribed guard opening is not legal.')
        threat = [entry.type for entry in enemy.roster if entry.active(1)]
        own_map = MapModel([(b.x, b.y, b.type) for b in own.buildings], rules)
        enemy_map = MapModel([(b.x, b.y, b.type) for b in enemy.buildings], rules)
        before = active_types(observation['players'][side]['roster'], 1)
        after = [entry.type for entry in own.roster if entry.active(1)]
        residual = simulate(own_map, threat, rules)[1]
        gain = simulate(enemy_map, after, rules)[1] - simulate(enemy_map, before, rules)[1]
        sequence = [a['type'] for a in actions if a['op'] == 'buy_minion']
        self.trace.append(dict(round=1, predicted_actions=predicted,
            attack_count=len(sequence), selected_sequence=sequence,
            forecast_attack_gain=gain, forecast_residual_damage=residual,
            defense=dict(selected='prescribed_guard', x=self.opening.x, y=self.opening.y),
            prescribed_opening=True))
        return actions


def make(**parameters):
    return GuardedForecast(**parameters).decide
