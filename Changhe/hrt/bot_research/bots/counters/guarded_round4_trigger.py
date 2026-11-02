"""Add an affordable corner gun to a public-budget early heavy strike."""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.triggered_budget_handoff import TriggeredBudgetHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate


class GuardedRound4Trigger(TriggeredBudgetHandoff):
    def __init__(self, early_gun=True, **parameters):
        super().__init__(**parameters)
        if not isinstance(early_gun, bool):
            raise ValueError('early_gun must be a boolean.')
        self.early_gun = early_gun

    def decide(self, observation):
        proposed = super().decide(observation)
        if not self.early_gun or observation['round'] != self.strike_round:
            return proposed
        side, rnd = observation['player'], observation['round']
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][side])
        actions = []
        gun = dict(op='build_turret', type='gun1', x=10, y=1)
        gun_accepted = False
        for index, action in enumerate([gun] + proposed):
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                actions.append(action)
                if index == 0:
                    gun_accepted = True
            else:
                self.filtered_proposals.append(dict(round=rnd, action=action,
                    reason=event['reason'], stage='early_gun_filter'))
        trace = self.trace[-1]
        visible = trace['visible_types']
        scenarios = [visible] + [visible + [tier] * count
            for tier, count in trace['hypothetical_counts'].items() if count]
        own_map = MapModel([(b.x, b.y, b.type) for b in state.buildings], observation['rules'])
        trace['scenario_residuals'] = [simulate(own_map, types, observation['rules'])[1]
                                     for types in scenarios]
        trace['defense_cost'] = sum(1 if a['op'] == 'build_wall' else cfg.turrets[a['type']].cost
            for a in actions if a['op'] in ('build_wall', 'build_turret'))
        trace['early_gun_accepted'] = gun_accepted
        return actions


def make(**parameters):
    return GuardedRound4Trigger(**parameters).decide
