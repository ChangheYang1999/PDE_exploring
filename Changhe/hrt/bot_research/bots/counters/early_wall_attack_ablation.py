"""Change only the early-wall policy's optional fourth-round purchase."""
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard


class EarlyWallAttackAblation(EarlyWallGuard):
    def __init__(self, round4_type='tier4'):
        if round4_type not in (None, 'tier3', 'tier4'):
            raise ValueError('The declared ablation uses None, tier3 or tier4.')
        super().__init__(witness='guard00')
        self.round4_type = round4_type

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][side])
        actions = []
        def submit(action):
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                actions.append(action)
                return True
            self.filtered_proposals.append(dict(round=rnd, action=action, reason=event['reason']))
            return False
        if rnd >= 5:
            for action in self.defender(deepcopy(observation)):
                submit(action)
        else:
            if rnd == self.witness['wall_round']:
                for x, y in self.witness['walls']:
                    submit(dict(op='build_wall', x=x, y=y))
            if rnd == 3:
                for turret in self.witness['turrets']:
                    submit(dict(op='build_turret', **turret))
            if rnd == 4 and self.round4_type is not None:
                if state.gold >= cfg.minions[self.round4_type].cost:
                    submit(dict(op='buy_minion', type=self.round4_type))
            while state.gold >= cfg.globals.factory_cost:
                if not submit(dict(op='buy_factory')):
                    break
        self.trace.append(dict(round=rnd, witness=self.witness['id'], defender_active=rnd >= 5,
            round4_type=self.round4_type,
            filtered_proposals=sum(p['round'] == rnd for p in self.filtered_proposals)))
        return actions


def make(**parameters):
    return EarlyWallAttackAblation(**parameters).decide
