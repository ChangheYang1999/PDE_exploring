"""Keep the delayed public signal and reserve its round-four tier4 purchase."""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.delayed_wall_guard import DelayedWallGuard
from bot_research.bots.counters.visible_search import player_from_snapshot


class ReservedWallGuard(DelayedWallGuard):
    def __init__(self):
        super().__init__()
        self.reservation_trace = []

    def decide(self, observation):
        actions = super().decide(observation)
        if observation['round'] != 3:
            return actions
        config = config_from_dict(observation['rules'])
        own = player_from_snapshot(observation['players'][observation['player']])
        prefix = [a for a in actions if a['op'] != 'buy_factory']
        factories = len(actions) - len(prefix)
        if actions != prefix + [{'op': 'buy_factory'}] * factories:
            raise ValueError('The supported opening requires trailing factory purchases.')
        for action in prefix:
            if not apply_action(own, action, 3, config)['accepted']:
                raise ValueError('The parent opening must be legal.')
        rules = config.globals
        path = shortest_path(rules.width, rules.height,
            ((b.x, b.y) for b in own.buildings), rules.spawn, rules.base)
        if path is None:
            raise ValueError('The parent opening must retain a route.')
        target = config.minions['tier4'].cost
        def projected(k):
            return (own.gold - k * rules.factory_cost + (len(path)-1) * rules.path_income_per_step
                    + (own.n_factories+k) * rules.factory_income)
        chosen = factories
        while chosen and projected(chosen) < target:
            chosen -= 1
        self.reservation_trace.append(dict(round=3,original_factories=factories,
            chosen_factories=chosen,projected_gold=projected(chosen),target=target,
            feasible=projected(chosen)>=target))
        return prefix + [{'op': 'buy_factory'}] * chosen


def make():
    return ReservedWallGuard().decide
