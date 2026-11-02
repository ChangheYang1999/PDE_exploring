"""A round-five public-roster test with a fixed additional attack package."""
from copy import deepcopy
from dataclasses import asdict
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
from bot_research.bots.counters.visible_search import player_from_snapshot


class EarlyWallFollowup(EarlyWallGuard):
    def __init__(self, package='one_tier3'):
        packages = {'disabled': (), 'one_tier3': ('tier3',),
                    'two_tier3': ('tier3', 'tier3'), 'one_tier4': ('tier4',)}
        if package not in packages:
            raise ValueError('Use one of the four declared packages.')
        super().__init__(witness='guard00')
        self.package_name = package
        self.package = packages[package]
        self.followup_trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        enemy = player_from_snapshot(observation['players'][1-side])
        triggered = rnd == 5 and bool(self.package) and not any(e.active(rnd) for e in enemy.roster)
        if not triggered:
            if rnd == 5:
                self.followup_trace.append(dict(round=rnd, triggered=False,
                    package=self.package_name, purchases=[]))
            return super().decide(observation)
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][side])
        actions = []
        purchases = []
        for tier in self.package:
            if state.gold < cfg.minions[tier].cost:
                break
            action = dict(op='buy_minion', type=tier)
            assert apply_action(state, action, rnd, cfg)['accepted']
            actions.append(action)
            purchases.append(tier)
        local = deepcopy(observation)
        own = local['players'][side]
        own['gold'] = state.gold
        own['roster'] = [dict(asdict(e), remaining_rounds=None if e.expires_after_round is None
                             else e.expires_after_round-(rnd-1)) for e in state.roster]
        for action in self.defender(local):
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                actions.append(action)
            else:
                self.filtered_proposals.append(dict(round=rnd, action=action, reason=event['reason']))
        self.trace.append(dict(round=rnd, witness=self.witness['id'], defender_active=True,
            filtered_proposals=sum(p['round']==rnd for p in self.filtered_proposals)))
        self.followup_trace.append(dict(round=rnd, triggered=True,
            package=self.package_name, purchases=purchases,
            continuation_gold=own['gold'], continuation_roster=deepcopy(own['roster'])))
        return actions


def make(**parameters):
    return EarlyWallFollowup(**parameters).decide
