"""Begin the early branch's defense when public current-map damage is positive."""
from td_game.combat import simulate_map
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.route_projection_selector import RouteGatedSelector
from bot_research.bots.counters.template_handoff import TemplateHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot


def visible_incoming(observation):
    side, rnd = observation['player'], observation['round']
    cfg = config_from_dict(observation['rules'])
    own = player_from_snapshot(observation['players'][side])
    enemy = player_from_snapshot(observation['players'][1-side])
    g = cfg.globals
    route = shortest_path(g.width, g.height, [(b.x, b.y) for b in own.buildings],
                          tuple(g.spawn), tuple(g.base))
    if route is None:
        raise ValueError('The visible own map must retain a route.')
    return simulate_map(enemy, own, route, rnd, cfg).damage


class EmergencyTemplate(TemplateHandoff):
    def __init__(self, emergency_rule='damage', emergency_from=5, **parameters):
        super().__init__(**parameters)
        if emergency_rule not in ('damage', 'none', 'always'):
            raise ValueError('Unknown emergency trigger.')
        if not isinstance(emergency_from, int) or not 5 <= emergency_from <= 50:
            raise ValueError('Emergency defense must begin after round four.')
        self.emergency_rule = emergency_rule
        self.emergency_from = emergency_from
        self.emergency_checks = []

    def decide(self, observation):
        rnd = observation['round']
        damage = None
        activated = False
        if self.triggered_round is None and rnd >= self.emergency_from:
            if self.emergency_rule == 'damage':
                damage = visible_incoming(observation)
                activated = damage > 0
            elif self.emergency_rule == 'always':
                activated = True
            if activated:
                self.triggered_round = rnd
        self.emergency_checks.append(dict(round=rnd, visible_incoming=damage,
                                           emergency_activated=activated))
        return super().decide(observation)


class EmergencyRouteSelector(RouteGatedSelector):
    def __init__(self, mode='adaptive', emergency_rule='damage', emergency_from=5):
        super().__init__(mode=mode)
        self.early = EmergencyTemplate(emergency_rule=emergency_rule, emergency_from=emergency_from,
            layout='empty', growth_rounds=6, bait=[], bait_round=2, tier='tier5',
            factory_cap=2000, purchase_cap=1000, upgrade_round=9,
            strike_round=4, strike_tier='tier4', strike_count=1, max_new=120,
            numerator=1, denominator=2, lead_from=5, lead_margin=0,
            early_gun=True, planner='template')


def make(**parameters):
    return EmergencyRouteSelector(**parameters).decide
