"""Switch from a guarded grower to F34 at a public HP trigger or deadline."""
from copy import deepcopy

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.screened_guard_maze import ScreenedGuardMaze
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v34.fortress import make as make_defender


class HPHandoff:
    def __init__(self, deadline=10, lead_from=None, lead_margin=0,
                 panic_hp=None, panic_from=2, replan_iters=5000, **parameters):
        self.deadline = int(deadline)
        self.lead_from = None if lead_from is None else int(lead_from)
        self.lead_margin = int(lead_margin)
        self.panic_hp = None if panic_hp is None else int(panic_hp)
        self.panic_from = int(panic_from)
        rounds = [self.deadline, self.panic_from]
        if self.lead_from is not None:
            rounds.append(self.lead_from)
        if any(r < 1 or r > 50 for r in rounds):
            raise ValueError('Trigger rounds must be in 1..50.')
        if self.lead_margin < 0 or (self.panic_hp is not None and self.panic_hp < 0):
            raise ValueError('HP thresholds must be nonnegative.')
        if int(parameters.get('upgrade_round', 9)) != 9:
            raise ValueError('The opening uses the fixed round9 gun extension.')
        parameters['upgrade_round'] = 9
        self.opening = ScreenedGuardMaze(**parameters)
        self.defender = make_defender(attack='none', round1_poke=0,
                                      replan_iters=int(replan_iters))
        self.switched = False
        self.switch_trace = []
        self.rejected_proposals = []

    def decide(self, observation):
        rnd = observation['round']
        side = observation['player']
        own_hp = observation['players'][side]['hp']
        enemy_hp = observation['players'][1-side]['hp']
        if not self.switched:
            reasons = []
            if rnd >= self.deadline:
                reasons.append('deadline')
            if self.lead_from is not None and rnd >= self.lead_from and own_hp > enemy_hp + self.lead_margin:
                reasons.append('lead')
            if self.panic_hp is not None and rnd >= self.panic_from and own_hp <= self.panic_hp:
                reasons.append('panic')
            if reasons:
                self.switched = True
                self.switch_trace.append(dict(round=rnd, own_hp=own_hp,
                                              opponent_hp=enemy_hp, reasons=reasons))
        private_observation = deepcopy(observation)
        proposed = (self.defender(private_observation) if self.switched
                    else self.opening.decide(private_observation))
        state = player_from_snapshot(observation['players'][side])
        config = config_from_dict(observation['rules'])
        actions = []
        for action in proposed:
            event = apply_action(state, action, rnd, config)
            if event['accepted']:
                actions.append(action)
            else:
                self.rejected_proposals.append(dict(round=rnd, action=action,
                                                    reason=event['reason']))
        return actions


def make(**parameters):
    return HPHandoff(**parameters).decide
