"""Fixed early roster purchases followed by the declared bluff growth policy."""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.feature_bluff import FeatureBluff
from bot_research.bots.counters.visible_search import player_from_snapshot


class RosterBait(FeatureBluff):
    def __init__(self, bait=None, bait_round=2, **parameters):
        super().__init__(**parameters)
        self.bait = list(bait or [])
        self.bait_round = int(bait_round)
        if not 1 <= self.bait_round <= self.growth_rounds:
            raise ValueError('Bait must be during the growth phase.')
        if len(self.bait) > 1000 or any(k not in ('tier1', 'tier2') for k in self.bait):
            raise ValueError('Use at most 1000 tier1 or tier2 bait entries.')

    def decide(self, observation):
        original = super().decide(observation)
        if observation['round'] != self.bait_round or not self.bait:
            return original
        config = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][observation['player']])
        actions = []
        for action in original:
            if action['op'] == 'buy_factory':
                continue
            if not apply_action(state, action, self.bait_round, config)['accepted']:
                raise RuntimeError('The parent proposed an invalid retained action.')
            actions.append(action)
        for kind in self.bait:
            action = dict(op='buy_minion', type=kind)
            if not apply_action(state, action, self.bait_round, config)['accepted']:
                break
            actions.append(action)
        count = min(max(0, self.factory_cap-state.n_factories),
                    state.gold // config.globals.factory_cost)
        for _ in range(count):
            action = dict(op='buy_factory')
            if not apply_action(state, action, self.bait_round, config)['accepted']:
                raise RuntimeError('Computed factory budget was not affordable.')
            actions.append(action)
        return actions


def make(**parameters):
    return RosterBait(**parameters).decide
