"""Guarded growth, then bounded defense against a synchronized public model."""
from copy import deepcopy

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.screened_guard_maze import ScreenedGuardMaze
from bot_research.bots.counters.stateful_public import PersistentFactoryModel
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v17.freeplan import free_plan
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate

MODEL = 'bot_research.experiments.lead.v28:@make'
MODEL_PARAMETERS = dict(passive_until=5, poke_reactive='turret_only', fail_limit=2,
                        passive_turret=False, robust_k=None, behind_mode='current')


class ForecastHandoff:
    def __init__(self, deadline=10, lead_from=None, forecast=True, free_steps=15,
                 max_factories=80, model_spec=MODEL, model_parameters=None,
                 **opening_parameters):
        self.deadline = int(deadline)
        self.lead_from = None if lead_from is None else int(lead_from)
        self.forecast = bool(forecast)
        self.free_steps = int(free_steps)
        self.max_factories = int(max_factories)
        if not 1 <= self.deadline <= 50 or (self.lead_from is not None and not 1 <= self.lead_from <= 50):
            raise ValueError('Switch rounds must be in 1..50.')
        if not 1 <= self.free_steps <= 60 or not 0 <= self.max_factories <= 2000:
            raise ValueError('Invalid bounded planner or factory budget.')
        self.opening = ScreenedGuardMaze(**opening_parameters)
        parameters = dict(MODEL_PARAMETERS if model_parameters is None else model_parameters)
        self.model = PersistentFactoryModel(model_spec, parameters)
        self.switched = False
        self.trace = []
        self.rejected_proposals = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        me, opponent = observation['players'][side], observation['players'][1-side]
        predicted, enemy = predict(observation, self.model)
        reasons = []
        if not self.switched:
            if rnd >= self.deadline:
                reasons.append('deadline')
            if self.lead_from is not None and rnd >= self.lead_from and me['hp'] > opponent['hp']:
                reasons.append('lead')
            self.switched = bool(reasons)
        state = player_from_snapshot(me)
        config = config_from_dict(observation['rules'])
        if self.switched:
            forecast_state = enemy if self.forecast else player_from_snapshot(opponent)
            threat = [entry.type for entry in forecast_state.roster if entry.active(rnd)]
            proposed = free_plan(deepcopy(observation), state.gold, [threat],
                                 partial='best', max_steps=self.free_steps)
        else:
            threat = [entry.type for entry in enemy.roster if entry.active(rnd)]
            proposed = self.opening.decide(deepcopy(observation))
        actions = []
        for action in proposed:
            event = apply_action(state, action, rnd, config)
            if event['accepted']:
                actions.append(action)
            else:
                self.rejected_proposals.append(dict(round=rnd, action=action, reason=event['reason']))
        if self.switched and rnd < 48:
            for _ in range(min(self.max_factories, state.gold // config.globals.factory_cost)):
                action = dict(op='buy_factory')
                event = apply_action(state, action, rnd, config)
                if not event['accepted']:
                    raise ValueError('A computed affordable factory was rejected.')
                actions.append(action)
        own_map = MapModel([(b.x, b.y, b.type) for b in state.buildings], observation['rules'])
        residual = simulate(own_map, threat, observation['rules'])[1]
        self.trace.append(dict(round=rnd, switched=self.switched, switch_reasons=reasons,
            own_hp=me['hp'], opponent_hp=opponent['hp'], predicted_actions=predicted,
            threat_types=threat, forecast_residual_damage=residual,
            defense_cost=sum(event_cost(a, observation['rules']) for a in actions
                             if a['op'] in ('build_turret', 'build_wall'))))
        return actions


def event_cost(action, rules):
    if action['op'] == 'build_wall':
        return rules['wall_cost']
    return rules['turrets'][action['type']]['cost']


def make(**parameters):
    return ForecastHandoff(**parameters).decide
