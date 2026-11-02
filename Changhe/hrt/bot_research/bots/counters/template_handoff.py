"""Change only the defensive planner after a public HP lead."""
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.guarded_round4_trigger import GuardedRound4Trigger
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v7.plan import plan_defense
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate


class TemplateHandoff(GuardedRound4Trigger):
    def __init__(self, planner='template', **parameters):
        super().__init__(**parameters)
        if planner not in ('free', 'template'):
            raise ValueError('Unknown defensive planner.')
        self.planner = planner

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        own_hp = observation['players'][side]['hp']
        enemy_hp = observation['players'][1-side]['hp']
        triggering = (self.triggered_round is not None or
            (rnd >= self.lead_from and own_hp > enemy_hp + self.lead_margin))
        if self.planner == 'free' or not triggering:
            return super().decide(observation)
        if self.triggered_round is None:
            self.triggered_round = rnd
        self.deadline = self.triggered_round
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][side])
        opponent = player_from_snapshot(observation['players'][1-side])
        visible = [entry.type for entry in opponent.roster if entry.active(rnd)]
        budget = opponent.gold * self.numerator // self.denominator
        counts = {tier: min(self.max_new, budget // item.cost)
                  for tier, item in cfg.minions.items()}
        scenarios = [visible] + [visible + [tier] * count
            for tier, count in counts.items() if count]
        proposed = plan_defense(deepcopy(observation), state.gold,
            threat_types=scenarios, allow_guns=True, partial='best')
        actions = []
        def add(action):
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                actions.append(action)
                return True
            self.filtered_proposals.append(dict(round=rnd, action=action,
                reason=event['reason'], stage='template_filter'))
            return False
        for action in proposed:
            add(action)
        if rnd < 48:
            for _ in range(min(self.max_factories, state.gold // cfg.globals.factory_cost)):
                if not add(dict(op='buy_factory')):
                    raise RuntimeError('Computed affordable factory rejected.')
        own_map = MapModel([(b.x, b.y, b.type) for b in state.buildings], observation['rules'])
        self.trace.append(dict(round=rnd, switched=True, public_budget=budget,
            visible_types=visible, hypothetical_counts=counts,
            scenario_residuals=[simulate(own_map, types, observation['rules'])[1] for types in scenarios],
            defense_cost=sum(cfg.wall_cost if a['op'] == 'build_wall' else cfg.turrets[a['type']].cost
                for a in actions if a['op'] in ('build_wall', 'build_turret')),
            triggered_round=self.triggered_round, trigger_hp_self=own_hp,
            trigger_hp_enemy=enemy_hp, planner='template'))
        return actions


def make(**parameters):
    return TemplateHandoff(**parameters).decide
