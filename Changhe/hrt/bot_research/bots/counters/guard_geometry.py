"""A corner gun opening followed by frozen economy17.

The only change from GuardRoster is the declared gun coordinate. A gun1 at
(10,1) covers seven consecutive cells on the initial route. Whole-game
behavior still depends on how later legal buildings change that route.
"""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v17.econ17 import make as economy17


class GuardGeometry:
    def __init__(self, roster=('tier1',), x=10, y=1, parameters=None):
        self.roster = tuple(roster)
        self.x, self.y = int(x), int(y)
        self.parameters = dict(free_fallback='zero', foreign_attack_from=11)
        self.parameters.update(parameters or {})
        self.policy = economy17(**self.parameters)

    def decide(self, observation):
        if observation['round'] != 1:
            return self.policy(observation)
        self.policy = economy17(**self.parameters)
        config = config_from_dict(observation['rules'])
        player = player_from_snapshot(observation['players'][observation['player']])
        actions = [{'op':'build_turret', 'type':'gun1', 'x':self.x, 'y':self.y}]
        actions += [{'op':'buy_minion', 'type':tier} for tier in self.roster]
        for action in actions:
            if not apply_action(player, action, 1, config)['accepted']:
                raise ValueError('The declared opening is not legal for this observation.')
        while player.gold >= config.globals.factory_cost:
            action = {'op':'buy_factory'}
            assert apply_action(player, action, 1, config)['accepted']
            actions.append(action)
        return actions


def make(**parameters):
    return GuardGeometry(**parameters).decide
