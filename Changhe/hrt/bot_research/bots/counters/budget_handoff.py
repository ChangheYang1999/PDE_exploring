"""Early heavy strike, then public-budget defense without a policy model."""
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.screened_guard_maze import ScreenedGuardMaze
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v17.freeplan import free_plan
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate


class BudgetHandoff:
    def __init__(self, deadline=6, strike_round=5, strike_tier='tier4', strike_count=1,
                 numerator=1, denominator=2, max_new=120, free_steps=15,
                 max_factories=80, **opening_parameters):
        self.deadline, self.strike_round = int(deadline), int(strike_round)
        self.strike_tier, self.strike_count = str(strike_tier), int(strike_count)
        self.numerator, self.denominator = int(numerator), int(denominator)
        self.max_new, self.free_steps = int(max_new), int(free_steps)
        self.max_factories = int(max_factories)
        if not 1 <= self.strike_round < self.deadline <= 50:
            raise ValueError('The strike must precede handoff.')
        if self.strike_tier not in ('tier4', 'tier5') or not 0 <= self.strike_count <= 4:
            raise ValueError('Invalid bounded heavy strike.')
        if not 0 <= self.numerator <= self.denominator or self.denominator < 1:
            raise ValueError('Require a budget fraction in [0,1].')
        if not 1 <= self.max_new <= 1000 or not 1 <= self.free_steps <= 60:
            raise ValueError('Invalid finite search bound.')
        if not 0 <= self.max_factories <= 2000:
            raise ValueError('Invalid factory bound.')
        self.opening = ScreenedGuardMaze(**opening_parameters)
        self.trace, self.filtered_proposals = [], []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][side])
        opponent = player_from_snapshot(observation['players'][1-side])
        visible = [entry.type for entry in opponent.roster if entry.active(rnd)]
        budget = opponent.gold * self.numerator // self.denominator
        counts = {tier:min(self.max_new, budget // item.cost)
                  for tier, item in cfg.minions.items()}
        scenarios = [visible] + [visible + [tier] * count for tier, count in counts.items() if count]
        actions = []
        def add(action):
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                actions.append(action)
                return True
            self.filtered_proposals.append(dict(round=rnd, action=action, reason=event['reason']))
            return False
        switched = rnd >= self.deadline
        if switched:
            proposed = free_plan(deepcopy(observation), state.gold, scenarios,
                                 partial='best', max_steps=self.free_steps)
        else:
            proposed = self.opening.decide(deepcopy(observation))
            if rnd == self.strike_round:
                for _ in range(self.strike_count):
                    if not add(dict(op='buy_minion', type=self.strike_tier)):
                        break
        for action in proposed:
            add(action)
        if switched and rnd < 48:
            for _ in range(min(self.max_factories, state.gold // cfg.globals.factory_cost)):
                if not add(dict(op='buy_factory')):
                    raise RuntimeError('Computed affordable factory rejected.')
        own_map = MapModel([(b.x, b.y, b.type) for b in state.buildings], observation['rules'])
        residuals = [simulate(own_map, types, observation['rules'])[1] for types in scenarios]
        self.trace.append(dict(round=rnd, switched=switched, public_budget=budget,
            visible_types=visible, hypothetical_counts=counts, scenario_residuals=residuals,
            defense_cost=sum(1 if a['op']=='build_wall' else cfg.turrets[a['type']].cost
                for a in actions if a['op'] in ('build_wall','build_turret'))))
        return actions


def make(**parameters):
    return BudgetHandoff(**parameters).decide
