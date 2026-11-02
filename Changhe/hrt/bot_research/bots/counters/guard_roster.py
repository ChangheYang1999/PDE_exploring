"""Fixed guarded opening, followed by the frozen economy17 policy.

Only the opening roster varies. The guard is at the previously checked (3,1)
cell; all remaining affordable gold buys factories. The continuation starts
in round 2 and receives the real observation. No opponent model is evaluated.
"""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v17.econ17 import make as economy17


class GuardRoster:
    def __init__(self, roster=('tier1',), parameters=None):
        self.roster = tuple(roster)
        self.parameters = dict(free_fallback='zero', foreign_attack_from=11)
        self.parameters.update(parameters or {})
        self.policy = economy17(**self.parameters)

    def decide(self, observation):
        if observation['round'] != 1:
            return self.policy(observation)
        self.policy = economy17(**self.parameters)
        config = config_from_dict(observation['rules'])
        player = player_from_snapshot(observation['players'][observation['player']])
        actions = [{'op': 'build_turret', 'type': 'gun1', 'x': 3, 'y': 1}]
        actions += [{'op': 'buy_minion', 'type': tier} for tier in self.roster]
        for action in actions:
            event = apply_action(player, action, 1, config)
            if not event['accepted']:
                raise ValueError('The declared opening is not legal for this observation.')
        while player.gold >= config.globals.factory_cost:
            action = {'op': 'buy_factory'}
            assert apply_action(player, action, 1, config)['accepted']
            actions.append(action)
        return actions


def make(**parameters):
    return GuardRoster(**parameters).decide
