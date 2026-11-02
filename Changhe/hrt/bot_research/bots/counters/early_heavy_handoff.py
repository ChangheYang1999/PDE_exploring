"""A public-model defender with a bounded early heavy purchase."""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.forecast_handoff import ForecastHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot


class EarlyHeavyHandoff(ForecastHandoff):
    def __init__(self, strike_round=5, strike_tier='tier4', strike_count=1, **parameters):
        super().__init__(**parameters)
        self.strike_round = int(strike_round)
        self.strike_tier = str(strike_tier)
        self.strike_count = int(strike_count)
        if not 1 <= self.strike_round < self.deadline <= 50:
            raise ValueError('The strike must precede the deadline.')
        if self.strike_tier not in ('tier4', 'tier5') or not 0 <= self.strike_count <= 4:
            raise ValueError('Choose zero to four heavy copies.')
        self.strike_trace = []
        self.filtered_parent_proposals = []

    def decide(self, observation):
        proposed = super().decide(observation)
        rnd, side = observation['round'], observation['player']
        if rnd != self.strike_round or self.switched:
            return proposed
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][side])
        actions = []
        for _ in range(self.strike_count):
            action = dict(op='buy_minion', type=self.strike_tier)
            if not apply_action(state, action, rnd, cfg)['accepted']:
                break
            actions.append(action)
        accepted_copies = len(actions)
        for action in proposed:
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                actions.append(action)
            else:
                self.filtered_parent_proposals.append(dict(round=rnd, action=action, reason=event['reason']))
        self.strike_trace.append(dict(round=rnd, requested=self.strike_count,
                                     accepted=accepted_copies, tier=self.strike_tier,
                                     post_action_gold=state.gold))
        return actions


def make(**parameters):
    return EarlyHeavyHandoff(**parameters).decide
